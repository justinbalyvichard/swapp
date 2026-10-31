# 02 — Base de données (Supabase Postgres)

Ce document fixe le modèle et les règles d'accès. L'agent `dev-base-de-donnees` le traduit en migrations ; toute divergence passe par le superviseur et `docs/DECISIONS.md`.

## Principe de sécurité central

**Les clients ne lisent jamais les tables d'autres membres directement.** Toute lecture d'un autre profil passe par des fonctions SQL `SECURITY DEFINER` (RPC) qui appliquent, dans cet ordre :

1. le demandeur est authentifié, son compte est actif, sa ville est ouverte (sauf RPC autorisées en ville en attente) ;
2. blocages dans les deux sens ;
3. cercle masqué et personnes masquées, dans les deux sens ;
4. niveau de visibilité de la cible (Fantôme, Sans photo, Flouté, Visible) et relation entre les deux (intérêt envoyé, intérêt mutuel, accès album) ;
5. statut de la cible (actif, en pause, masqué par la modération, banni, inactif > 60 jours) ;
6. limitation de débit (anti-aspiration) ;
7. projection : seules les colonnes autorisées pour cette relation sortent (jamais la position exacte, jamais les « Non » de la grille d'envies, jamais les notes détaillées).

La RLS des tables de base n'autorise que **son propre contenu** (`owner = auth.uid()` via les membres du profil). Tout le reste : refus par défaut.

## Extensions

`postgis`, `pg_cron`, `pg_net`, `pgmq`, `pgcrypto`, `pg_trgm`, `pgtap` (tests).

## Schémas

| Schéma | Contenu | Accès client |
|---|---|---|
| `public` | Tables métier (RLS stricte) + RPC exposées | Oui, via RLS et RPC |
| `private` | Fonctions internes, empreintes du cercle masqué, paramètres | Non |
| `admin` | Rôles admin, journal d'audit, dossiers de modération | Non (uniquement Edge Functions et serveur admin, MFA aal2) |

## Types énumérés

```sql
profile_kind:        solo | couple
member_gender:       femme | homme | trans_femme | trans_homme | non_binaire | autre
orientation:         hetero | bi | bi_curieux | gay | lesbienne | pan
visibility_level:    fantome | sans_photo | floute | visible
profile_status:      onboarding | actif | en_pause | masque_moderation | suspendu | banni | archive
verification_status: aucune | en_cours | verifie | refuse
desire_state:        oui | curieux | non
interest_level:      clin_oeil | curieux_de | demande_album
interest_status:     en_attente_validation_couple | envoye | accepte | refuse | expire | annule
photo_kind:          publique | privee | message | verification
moderation_status:   en_attente | approuve | retire | revue_humaine
city_status:         waitlist | open
```

## Tables principales

### Personnes et profils

| Table | Colonnes clés | Notes |
|---|---|---|
| `members` | `id` (= `auth.users.id`), `birthdate`, `gender`, `orientation`, `height_cm?`, `smoker?`, `languages[]`, `verification_status`, `identity_verified bool`, `phone_hash?`, `email_hash`, `is_test bool`, `created_at` | Une personne réelle. 18+ vérifié par contrainte (`birthdate <= now() - interval '18 years'`) |
| `profiles` | `id`, `kind`, `pseudo` (unique, modifiable 1×/mois), `city_id`, `geo geography(Point)` **déjà floutée**, `radius_km`, `visibility`, `status`, `tagline` (80), `about`, `looking_for`, `prompts jsonb` (3 max), `experience` (`decouverte` / `initie`), `hosts` / `travels`, `couple_validation` (`un` / `deux`), `couple_mode` (`transparence` / `jardin`), `online_visible bool`, `read_receipts bool`, `member_number bigint unique` (null tant que non vérifié), `member_number_public bool` (défaut faux), `grade`, `rating_avg`, `rating_count`, `meetings_count`, `last_active_week date`, `boost_until` (nouveaux 14 j), `is_test` | L'entité visible. Un solo = 1 membre, un couple = 2 |
| `profile_members` | `profile_id`, `member_id`, `role` (`solo`, `partenaire_1`, `partenaire_2`), `confirmed_at` | Un couple n'est actif que si 2 membres vérifiés |
| `couple_links` | `solo_profile_id`, `couple_profile_id`, `partner_confirmed_at`, `link_public bool` | Badge « En couple ». Lien actif seulement après confirmation du partenaire |
| `couple_invites` | `couple_profile_id`, `code`, `expires_at`, `accepted_by` | Invitation du second membre |

**Numéro de membre** : séquence `private.member_number_seq`, attribuée par un trigger quand le profil passe vérifié pour la première fois (couple : quand il devient actif). Jamais modifié, jamais réattribué (la séquence ne recule pas, un compte supprimé garde son trou). Exclu de toute recherche, de tout tri et de toute URL ; `profile_view` ne le renvoie que si `member_number_public` est vrai ou si le demandeur est le propriétaire. Les profils `is_test` n'en reçoivent pas.

**Position** : à l'enregistrement, la position est arrondie à une maille de 1 km puis décalée d'un vecteur aléatoire fixe par profil (≤ 800 m). Aucune autre position n'est stockée, pas d'historique. Les distances affichées sont arrondies à 5 km (« ~10 km »).

### Envies, limites et recherche

| Table | Colonnes | Notes |
|---|---|---|
| `desire_catalog` | `id`, `category` (8 catégories de la grille), `label`, `order`, `active` | Contenu éditable dans la console |
| `member_desires` | `member_id`, `desire_id`, `state`, `scope` (`couple` / `solo`) | Les `non` ne sortent jamais par une RPC publique |
| `member_limits` | `member_id`, `limit_code`, `custom_text?`, `public bool` | Limites affichables (« jamais ») |
| `profile_highlights` | `profile_id`, `desire_id`, `order` (≤ 6) | Mise en avant |
| `profile_desires_public` (vue matérialisée ou fonction) | `profile_id`, `desire_id`, `who` (`nous_deux` / `elle` / `lui` / `moi`) | Calcul : accord visible, désaccord privé (non affiché) |
| `profile_preferences` | `profile_id`, `accepted_kinds[]`, `age_min`, `age_max`, `max_km`, `require_common_desire`, `contact_rule` (`verifies` / `types_cherches` / `envie_commune`), `open_to[]` (`hommes_seuls`, `debutants`) | « Ce que je cherche » + « Qui peut me contacter » |
| `saved_radars` | `id`, `profile_id`, `name`, `filters jsonb`, `last_digest_at` | Gratuits : 2 ; au-delà, suggestion Premium |
| `tonight` | `profile_id`, `until` (≤ 12 h) | Mode Ce soir |
| `favorites` | `owner_profile_id`, `target_profile_id` | Profils mis de côté |
| `private_notes` | `owner_profile_id`, `target_profile_id`, `body` | Visibles du seul auteur |
| `availability` | `profile_id`, `starts_at`, `ends_at` | Nos disponibilités |

### Photos

| Table | Colonnes | Notes |
|---|---|---|
| `photos` | `id`, `profile_id`, `kind`, `storage_path`, `blurred_path`, `width`, `height`, `phash`, `order`, `moderation_status`, `moderation_labels jsonb`, `removed_reason?`, `created_at` | Publiques 1–6, privées ≤ 30. `verification` jamais exposée |
| `album_access` | `owner_profile_id`, `viewer_profile_id`, `granted_at`, `revoked_at?` | Révocable à tout moment |

Storage : bucket `photos` **privé**. Chemins `{profile_id}/{photo_id}.webp` et `{profile_id}/{photo_id}.blur.webp`. Aucune URL publique. L'Edge Function `photo-url` signe des URL valides 10 minutes après vérification des droits (visibilité, intérêt mutuel, accès album). EXIF supprimé sur le téléphone **et** revérifié côté serveur.

### Contacts et messagerie

| Table | Colonnes | Notes |
|---|---|---|
| `interests` | `id`, `from_profile_id`, `to_profile_id`, `level`, `desire_id?`, `status`, `created_at`, `expires_at` (+14 j), `delivered_after_verification bool` | Unicité par paire et niveau actif |
| `interest_approvals` | `interest_id`, `member_id`, `approved_at` | Couples en validation à deux |
| `refusals` | `interest_id`, `template_id?`, `custom_text?`, `send_at` (délai aléatoire 1–6 h), `sent_at?` | « Pas pour nous » |
| `refusal_templates` | `id`, `from_form` (`je` / `nous`), `to_form` (`tu` / `vous`), `reason?` (`type`, `distance`, `age`, `aucune`), `body` avec variables, `active` | 40 textes au lancement |
| `refusal_history` | `recipient_profile_id`, `template_id` | Jamais deux fois le même texte au même destinataire |
| `conversations` | `id`, `profile_a`, `profile_b` (a < b), `opened_at`, `paused_by?` | Créée uniquement par un intérêt réciproque |
| `messages` | `id`, `conversation_id`, `sender_profile_id`, `sender_member_id`, `body?`, `photo_id?`, `status` (`en_moderation`, `livre`, `retire`), `flags jsonb`, `created_at` | Photos : livrées après analyse. Chiffrement au repos (colonne `body` chiffrée par pgsodium/Vault ou chiffrement applicatif, décision en P1) |
| `message_reads` | `conversation_id`, `profile_id`, `last_read_at` | Accusés de lecture si activés |
| `blocks` | `blocker_profile_id`, `blocked_profile_id` | Effet immédiat, bidirectionnel à la lecture |
| `hidden_people` | `owner_member_id`, `target_hash` | Masquer une personne précise (empreinte du téléphone ou de l'email) |
| `hidden_pairs` | `member_a`, `member_b`, `source` (`cercle`, `manuel`) | Résultat du cercle masqué ; seules les correspondances sont gardées |

**Cercle masqué** : le téléphone normalise les numéros de son répertoire (E.164), calcule `HMAC-SHA256(numéro, clé_app)` et envoie les empreintes par lots à la RPC `circle_sync`. Le serveur compare aux `phone_hash` des membres, insère les paires trouvées dans `hidden_pairs`, et **ne stocke pas les empreintes envoyées**. Les `phone_hash` des membres sont recalculés côté serveur avec un poivre stocké dans Vault (double hachage), pour qu'une fuite de la clé applicative ne suffise pas.

### Rencontres, notes et grades

| Table | Colonnes | Notes |
|---|---|---|
| `meetings` | `id`, `profile_a`, `profile_b`, `date`, `confirmed_a_at?`, `confirmed_b_at?` | « Vous vous êtes vus ? » |
| `ratings` | `meeting_id`, `rater_profile_id`, `rated_profile_id`, `respect`, `hygiene`, `fidele`, `fiabilite`, `discretion`, `ambiance` (1–5), `created_at`, `revealed_at?` | Révélées quand les deux ont noté ou après 7 jours. Jamais lisibles en détail par le noté |
| Fonction `private.recompute_reputation(profile_id)` | | Moyenne (affichée dès 5 notes), grade (Curieux → Épicurien), déclenchement d'examen si `respect ≤ 2` |

### Soirées et lancement

| Table | Colonnes | Notes |
|---|---|---|
| `venues` | `id`, `name`, `city_id`, `address`, `siret?`, `verified_at?` | Clubs |
| `pro_accounts` | `member_id`, `venue_id?`, `kind` (`club` / `organisateur`), `verified_at?` | SIRET ou identité |
| `events` | `id`, `venue_id?`, `organizer_pro_id`, `title`, `starts_at`, `ends_at`, `city_id`, `ambiance[]`, `accepts_solo_men bool`, `accepts_beginners bool`, `capacity?`, `status` (`brouillon`, `a_valider`, `publie`, `annule`) | Validées avant publication |
| `event_registrations` | `event_id`, `profile_id`, `status` (`inscrit`, `liste_attente`, `annule`) | |
| `cities` | `id`, `name`, `geo`, `status`, `threshold_total`, `threshold_ratio_couples_femmes`, `opened_at?` | Villes à seuil |
| `waitlist` | `email`, `city_id`, `profile_kind`, `created_at`, `invited_at?` | Site vitrine |
| `invite_codes` | `code`, `owner_profile_id?`, `venue_id?`, `uses_left`, `expires_at` | Passe-droit dans la liste d'attente uniquement |

### Notifications

| Table | Colonnes | Notes |
|---|---|---|
| `push_tokens` | `member_id`, `platform` (`ios`, `web`), `token`, `last_seen_at` | |
| `notification_settings` | `member_id`, `push_message`, `push_accept`, `push_event`, `digest_hour` (défaut 19), `digest_enabled`, `neutral_text` (défaut vrai) | |
| `notification_log` | `member_id`, `kind`, `sent_at` | Plafond 5 push/jour, le reste part au digest |
| `digest_items` | `member_id`, `kind`, `payload jsonb`, `created_at`, `sent_in_digest_at?` | Clins d'œil, Radars, expirations, coach de profil |

### Compte, abonnement, conformité

| Table | Colonnes | Notes |
|---|---|---|
| `entitlements` | `profile_id`, `plan` (`free`, `premium`), `source` (`launch_free`, `apple`, `stripe`), `expires_at?` | Un Premium couvre le couple et ses solos liés |
| `paywall_events` | `profile_id`, `moment`, `shown_at` | Au plus une suggestion par jour |
| `data_requests` | `member_id`, `kind` (`export`, `suppression`), `status`, `completed_at?` | Export et suppression en 1 tap |
| `devices` | `member_id`, `device_hash`, `attested bool`, `first_seen_at` | Comptes multiples, contournement de bannissement |

### Modération (schéma `admin`)

| Table | Colonnes | Notes |
|---|---|---|
| `admin.admin_users` | `user_id`, `role` (`super_admin`, `moderateur`, `support`, `lecture`), `created_at` | Un compte admin ne peut pas avoir de profil membre (contrainte + trigger) |
| `reports` | `id`, `reporter_profile_id`, `target_profile_id`, `message_id?`, `photo_id?`, `reason`, `details`, `created_at` | Public (insertion seulement) |
| `admin.cases` | `id`, `target_profile_id`, `source` (`signalement`, `photo`, `texte`, `note`, `auto`), `severity` (`mineur`, `venal`, `menace`, `harcelement`, `autre`), `ai_summary`, `ai_action`, `ai_confidence`, `status` (`ouvert`, `en_reflexion`, `clos`), `decision_due_at?` | File de la console |
| `admin.sanctions` | `id`, `profile_id`, `kind` (`avertissement`, `suspension`, `bannissement`, `gel`), `reason_code`, `reason_text`, `automatic bool`, `starts_at`, `ends_at?`, `effective_at` (+24 h pour un bannissement proposé), `lifted_at?` | Motif toujours communiqué |
| `admin.appeals` | `sanction_id`, `body`, `created_at`, `decided_at?`, `decision` | Délai 15 jours |
| `admin.audit_log` | `id`, `admin_user_id`, `action`, `target`, `details jsonb`, `ip`, `created_at` | **Append-only** : aucune mise à jour ni suppression (trigger qui lève une exception) |
| `admin.settings` | `key`, `value jsonb` | Seuils de confiance IA, seuils des villes, plafonds |

## RPC exposées (liste minimale)

| RPC | Rôle |
|---|---|
| `discover(filters, page)` | Résultats Découvrir, classés (compatibilité, distance, activité, bonus grade plafonné, coup de pouce nouveaux, rotation), projection selon la relation |
| `profile_view(profile_id)` | Fiche d'un profil, sans trace de consultation |
| `send_interest(to, level, desire_id?)` | Contrôles : vérifié (ou 3 intérêts en attente pendant la vérification), règles « Qui peut me contacter », profil très sollicité, quotas, validation couple |
| `respond_interest(id, accept / pas_pour_nous, template_override?)` | Ouvre la conversation si réciproque ; planifie le refus |
| `grant_album(viewer)` / `revoke_album(viewer)` | Albums |
| `circle_sync(hashes[])` | Cercle masqué |
| `confirm_meeting(meeting_id)` / `submit_rating(...)` | Notes |
| `city_status()` | Statut et progression de la ville (compteur réel) |
| `set_visibility(level)` | Effet immédiat |
| `request_data_export()` / `delete_account()` | RGPD |

## Index

- `profiles` : GiST sur `geo` ; B-tree `(city_id, status, visibility)` ; `(last_active_week)`.
- `member_desires` : `(desire_id, state)`.
- `interests` : `(to_profile_id, status)`, `(from_profile_id, created_at)`.
- `messages` : `(conversation_id, created_at desc)`.

## Tâches planifiées (pg_cron)

| Tâche | Fréquence |
|---|---|
| Expiration des intérêts > 14 j (+ entrée digest bienveillante) | horaire |
| Envoi des refus planifiés | toutes les 5 min |
| Bannissements arrivés au bout des 24 h | toutes les 15 min |
| Digest du soir (par fuseau et heure choisie) | toutes les 15 min |
| Révélation des notes à 7 j, recalcul des grades | horaire |
| Retrait des recherches après 60 j d'inactivité ; archivage à 6 mois (après email) | quotidien |
| Ouverture des villes au seuil | toutes les heures |
| Suppression réelle des photos 30 j après retrait | quotidien |
| Tirage des 20 décisions de contrôle du lundi | hebdomadaire |

## Tests obligatoires (pgTAP, `supabase/tests`)

Une **matrice de visibilité** est testée en entier : pour chaque niveau (Fantôme, Sans photo, Flouté, Visible) × relation (aucune, intérêt envoyé par moi, intérêt reçu, mutuel, album accordé, album révoqué, bloqué, cercle masqué, personne masquée) × statut de la cible (actif, pause, masqué, banni, inactif), on vérifie ce que `discover`, `profile_view` et `photo-url` renvoient. Toute nouvelle colonne exposée ajoute ses cas.

Autres tests : un membre ne lit aucune ligne d'un autre membre en accès direct aux tables ; les `non` ne sortent jamais ; aucune position exacte ; le journal d'audit refuse UPDATE et DELETE ; un compte admin ne peut pas créer de profil ; la production refuse `is_test = true`.

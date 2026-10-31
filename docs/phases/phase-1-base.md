# Phase 1 — Base de données et sécurité

**Branche** : `phase/1-base` · **Objectif** : tout le modèle de `docs/02-base-de-donnees.md`, verrouillé et testé, avant le moindre écran métier.
Relecteur-securite obligatoire sur **chaque** lot.

### P1-01 · dev-base-de-donnees · Membres, profils, couples, villes
Énumérés, `members` (contrainte 18+), `profiles`, `profile_members`, `couple_links`, `couple_invites`, `cities`. Fonction `private.fuzz_location(point, profile_id)` (maille 1 km + décalage fixe ≤ 800 m).
- [ ] Aucune colonne de position exacte n'existe
- [ ] Un couple n'est `actif` qu'avec 2 membres vérifiés (test)

### P1-02 · dev-base-de-donnees · Envies et limites
`desire_catalog` rempli avec **toute** la grille du cahier des charges (8 catégories, libellés exacts de `docs/annexe-produit.md`), `member_desires`, `member_limits`, `profile_highlights` (≤ 6), fonction `profile_desires_public` (nous deux / elle / lui ; désaccord jamais exposé).
- [ ] Tests : un « non » ne sort jamais ; un désaccord n'apparaît pas ; l'accord affiche le bon « who »

### P1-03 · dev-base-de-donnees · Photos et Storage
Table `photos`, `album_access`, bucket privé `photos`, politiques Storage (écriture dans son dossier uniquement, lecture interdite côté client : tout passe par `photo-url`).
- [ ] Aucun objet du bucket n'est lisible sans URL signée

### P1-04 · dev-base-de-donnees · Contacts et messagerie
`interests`, `interest_approvals`, `refusals`, `refusal_templates`, `refusal_history`, `conversations`, `messages` (chiffrement au repos décidé et consigné), `message_reads`, `blocks`, `hidden_people`, `hidden_pairs`, `reports`.
- [ ] Une conversation ne peut naître que d'un intérêt réciproque (contrainte ou RPC unique)

### P1-05 · dev-base-de-donnees · Rencontres, notes, grades
`meetings`, `ratings`, `private.recompute_reputation`. Seuils des grades exactement ceux de `docs/annexe-produit.md`.
- [ ] Tests des 5 grades, de l'affichage de la moyenne à partir de 5 notes, de la révélation à l'aveugle (les deux ont noté ou 7 j)

### P1-06 · dev-base-de-donnees · Soirées et lancement
`venues`, `pro_accounts`, `events`, `event_registrations`, `waitlist`, `invite_codes`, RPC `city_status`.
- [ ] Le compteur de `city_status` ne compte que des profils vérifiés réels (`is_test = false` en prod)

### P1-07 · dev-base-de-donnees · Notifications, compte, conformité
`push_tokens`, `notification_settings`, `notification_log`, `digest_items`, `entitlements`, `paywall_events`, `data_requests`, `devices`, `consents`.

### P1-08 · dev-base-de-donnees · Schéma admin
`admin.admin_users`, `admin.cases`, `admin.sanctions`, `admin.appeals`, `admin.audit_log` (append-only par trigger), `admin.settings` (valeurs par défaut), Custom Access Token Hook (`app_role`).
- [ ] UPDATE/DELETE sur `audit_log` lèvent une exception ; un admin ne peut pas avoir de profil ; RPC admin refusée en aal1

### P1-09 · dev-base-de-donnees · RPC de lecture
`discover`, `profile_view`, `city_status`, `set_visibility`, `circle_sync` avec les 7 contrôles et la limitation de débit (table `private.rate_limits`). Classement : compatibilité des envies, distance, activité récente, bonus grade plafonné, coup de pouce 14 j, rotation (poids dans `admin.settings`).
- [ ] `discover` < 400 ms sur 50 000 profils de test (script de charge local, `EXPLAIN ANALYZE` joint au rapport)

### P1-10 · dev-base-de-donnees · Matrice de visibilité
Tests pgTAP de la matrice complète (`docs/02`, section Tests).
- [ ] 100 % des combinaisons niveau × relation × statut couvertes, toutes vertes

### P1-11 · dev-base-de-donnees · Tâches planifiées
Fonctions SQL des tâches pg_cron de `docs/02` (corps testés), planification déclarée dans une migration.

### P1-12 · dev-base-de-donnees · Seeds et garde-fou production
`seed.sql` : profils fictifs évidents (`is_test = true`), uniquement local/staging. Trigger qui refuse `is_test = true` si `admin.settings.environment = 'production'`.

**Fin de phase** : relecture sécurité globale renforcée (le relecteur tente activement de lire des données interdites avec un jeton membre), rapport.

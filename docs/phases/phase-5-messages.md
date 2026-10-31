# Phase 5 — Intérêts et messagerie

**Branche** : `phase/5-messages` · **Référence** : maquettes Intérêt, Messages, Conversation, Pas pour nous.

### P5-01 · dev-mobile + dev-base-de-donnees · Envoyer un intérêt
Clin d'œil, Curieux de… (envie choisie), Demande d'album. Contrôles : vérifié (ou 3 en attente pendant la vérification), « Qui peut me contacter », profil très sollicité (« sois précis »), quotas hebdomadaires (au-delà : suggestion Premium), validation à deux pour les couples (l'autre membre reçoit la demande de validation).

### P5-02 · dev-mobile · Recevoir et répondre
Liste des intérêts reçus, Oui / Pas pour nous / plus tard, expiration à 14 jours (annonce bienveillante dans le digest), « X personnes attendent ta réponse » dans le digest.

### P5-03 · dev-backend + dev-mobile · Pas pour nous
Sélection dans `packages/core` (formes je/nous × tu/vous, raison réelle avec vraies valeurs, jamais deux fois le même texte), 40 modèles rédigés (les exemples du cahier des charges + 30 nouveaux, même ton), délai aléatoire 1–6 h, modification avant envoi, 3 messages personnels.
- [ ] relecteur-design valide chacun des 40 textes

### P5-04 · dev-mobile · Messagerie
Liste des conversations, conversation temps réel (Supabase Realtime), envoi optimiste, file d'envoi hors ligne avec renvoi, accusés de lecture si activés, mettre en pause, photos dévoilées des deux côtés à l'ouverture.

### P5-05 · dev-backend · Photos en message
Statut `en_moderation` → `livre` après analyse ; l'expéditeur voit « envoyé » tout de suite ; le destinataire ne reçoit rien avant validation.

### P5-06 · dev-backend · Protection des conversations
Détection des coordonnées, liens et tarifs (premier message analysé par LLM, ensuite règles), ralentissement des messages copiés-collés en masse.

### P5-07 · dev-mobile + dev-backend · Bloquer et signaler
Depuis un profil, un message, une photo, en 1 tap ; création des `reports` et des `admin.cases`.

### P5-08 · dev-web · Parité PWA

### P5-09 · testeur-qa · E2E
Intérêt réciproque → conversation ; validation à deux ; Pas pour nous reçu avec le bon ton et la bonne raison ; photo en message refusée jamais reçue ; blocage effectif dans les deux sens ; réseau coupé pendant l'envoi.

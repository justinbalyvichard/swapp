# Décisions

Format : `D-NNN — date — contexte — décision — raison`. Une décision ne contredit jamais les non-négociables ni `06-conformite.md`.

## Décisions prises avant le développement (Justin)

- **D-001** — Base de données : Supabase, région UE (Paris de préférence), offre Pro avant les premiers vrais utilisateurs.
- **D-002** — Accès aux données : supabase-js et RPC SQL, sans Prisma (Prisma contournerait la RLS). Types générés par Supabase.
- **D-003** — Git : une branche par phase, créée par Justin. Les agents ne créent jamais de branche.
- **D-004** — Autonomie : les agents ne sollicitent Justin qu'aux 5 points d'arrêt d'`AGENTS.md` ; le superviseur répond à toutes les autres questions.
- **D-005** — Connexion : Apple, Google, code email à 6 chiffres. Pas de mot de passe au MVP.
- **D-006** — Fournisseurs par défaut derrière adaptateurs : Sightengine (images), LLM hébergé en UE (défaut Mistral), prestataire de vérification à choisir par Justin (mock en attendant), Resend, PostHog UE, Sentry UE.
- **D-007** — Aucun faux profil, y compris au lancement. Démarrage par villes à seuil, clubs partenaires et codes d'invitation.
- **D-008** — Paiement : aucun au MVP, Premium affiché « Gratuit pour l'instant ».
- **D-009** — Pas de badge « Membre fondateur ». À la place, un **numéro de membre** : attribué à la première vérification (jamais à l'inscription), un par profil (couple et solos liés ont chacun le leur), définitif et jamais réattribué, privé par défaut (visible du seul membre) avec option d'affichage public, jamais utilisé comme identifiant technique ni dans une URL.

## Décisions du superviseur


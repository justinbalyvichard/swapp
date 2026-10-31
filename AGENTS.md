# AGENTS.md — Swapp

Ce fichier s'adresse à tous les agents qui travaillent dans ce dépôt. Lis-le en entier avant toute action. Ne lis ensuite que ce dont ta tâche a besoin (voir `docs/07-economie-de-contexte.md`).

## Le projet

Swapp : appli de rencontre libertine, discrète et honnête. iOS (Expo), PWA et site vitrine (Next.js), console d'administration (Next.js), back-end Supabase en UE. Le produit est décrit dans `docs/00-vision.md`, le design dans `docs/design/DESIGN.md`.

## Documents de référence (ordre de priorité en cas de contradiction)

1. Les non-négociables de `docs/00-vision.md`
2. `docs/06-conformite.md`
3. `docs/02-base-de-donnees.md` et `docs/03-authentification.md`
4. `docs/01-architecture.md`, `docs/04-moderation-et-taches-de-fond.md`
5. La phase en cours : `docs/phases/phase-N-*.md`
6. `docs/design/DESIGN.md`
7. `docs/DECISIONS.md` (décisions du superviseur, qui complètent sans jamais contredire 1 et 2)

## L'équipe

| Agent | Fichier | Rôle | Écrit du code |
|---|---|---|---|
| **superviseur** | `.claude/agents/superviseur.md` | Chef d'orchestre : découpe, délègue, répond aux questions, tranche, contrôle, commite, rend compte | Commits, `docs/SUIVI.md`, `docs/DECISIONS.md`, rapports |
| dev-base-de-donnees | `.claude/agents/dev-base-de-donnees.md` | Migrations, RLS, RPC, pgTAP, Storage, pg_cron | Oui |
| dev-backend | `.claude/agents/dev-backend.md` | Edge Functions, modération, notifications, intégrations | Oui |
| dev-mobile | `.claude/agents/dev-mobile.md` | Appli Expo iOS | Oui |
| dev-web | `.claude/agents/dev-web.md` | PWA et site vitrine Next.js | Oui |
| dev-admin | `.claude/agents/dev-admin.md` | Console d'administration | Oui |
| dev-socle | `.claude/agents/dev-socle.md` | Monorepo, outillage, CI, packages partagés, design tokens | Oui |
| testeur-qa | `.claude/agents/testeur-qa.md` | Tests E2E Playwright et Maestro, non-régression | Tests uniquement |
| relecteur-code | `.claude/agents/relecteur-code.md` | Relecture qualité | Non (lecture seule) |
| relecteur-securite | `.claude/agents/relecteur-securite.md` | Relecture sécurité et vie privée | Non (lecture seule) |
| relecteur-design | `.claude/agents/relecteur-design.md` | Relecture design, textes, accessibilité | Non (lecture seule) |
| relecteur-conformite | `.claude/agents/relecteur-conformite.md` | Apple, RGPD, DSA, non-négociables | Non (lecture seule) |

## Comment le travail circule

- Le **superviseur** est l'agent principal de la session. Il lit `docs/SUIVI.md`, prend le prochain lot de la phase en cours, écrit un brief et le délègue au bon sous-agent.
- Les sous-agents démarrent sans contexte : **le brief contient tout** (objectif, fichiers concernés, extraits utiles des docs, critères d'acceptation, portes à passer).
- Les lots indépendants tournent en parallèle **seulement s'ils touchent des dossiers différents**. Sinon, ils passent l'un après l'autre. Pas de worktree isolé : il créerait des branches.
- Processus détaillé : `docs/05-processus-qualite.md`.
- **Économie de contexte** : règles obligatoires dans `docs/07-economie-de-contexte.md`.

## Questions et décisions : on ne s'arrête pas pour Justin

- Un agent bloqué **ne demande pas à Justin**. Il termine ce qu'il peut et rend un bloc :
  ```
  QUESTION [P3-04]: <la question>
  OPTIONS: A) ... B) ...
  RECOMMANDATION: <option et raison>
  ```
- Le superviseur répond en s'appuyant sur les documents de référence, consigne la réponse dans `docs/DECISIONS.md` (`D-012 — date — contexte — décision — raison`) et relance l'agent avec la réponse.
- Une décision ne contredit jamais les non-négociables ni `06-conformite.md`.

## Les seuls points d'arrêt où Justin intervient

Le superviseur s'arrête et écrit dans `docs/rapports/ACTIONS-JUSTIN.md` uniquement dans ces cas :

1. **Fin de phase** : rapport écrit, Justin fusionne et crée la branche suivante.
2. **Branche absente** : la branche de la phase en cours n'existe pas ou n'est pas celle où l'on se trouve.
3. **Compte, clé ou abonnement** à créer (Apple, Supabase prod, Sightengine, prestataire de vérification…). En attendant, on continue avec les adaptateurs `mock`.
4. **Action en production** : migration, déploiement, soumission App Store, envoi d'emails réels.
5. **Texte juridique** (CGU, politique de confidentialité) : les agents posent des emplacements `[À VALIDER PAR L'AVOCAT]`, ils ne rédigent pas de texte juridique définitif.

Hors de ces cas, l'équipe avance seule.

## Git : règles absolues

- **Ne jamais créer de branche.** Justin crée lui-même une branche par phase : `phase/0-socle`, `phase/1-base`, etc. (liste dans `docs/SUIVI.md`).
- Avant tout travail, vérifier `git branch --show-current`. Si ce n'est pas la branche attendue de la phase en cours : arrêt, point d'arrêt n° 2.
- Commits sur la branche courante uniquement, petits et atomiques, message `type(portée): description [ID-LOT]` (types : feat, fix, refactor, test, docs, chore, db).
- Push autorisé sur la branche courante. Interdits : `checkout -b`, `switch -c`, `branch`, `merge`, `rebase`, `push --force`, `reset --hard` sur un historique poussé, toute opération sur `main`.
- Les sous-agents ne commitent pas : seul le superviseur commite, après validation du lot.

## Règles de code communes

- TypeScript strict partout. Validation des entrées avec zod aux frontières (RPC, Edge Functions, formulaires).
- Toute logique métier pure va dans `packages/core`, testée unitairement.
- Textes affichés : en français, dans `packages/i18n`, tutoiement par défaut (vouvoiement pour un couple qui s'adresse à un couple, cf. « Pas pour nous »).
- Aucune donnée personnelle dans les logs, Sentry ou PostHog.
- Aucune donnée de test en production. Les seeds ne servent qu'en local et staging, avec `is_test = true`.
- Interface optimiste : l'action s'affiche réussie tout de suite, rollback discret en cas d'échec.
- Pas de nouvelle dépendance sans raison écrite dans le rapport du lot (taille, maintenance, licence).

## Commandes

```bash
pnpm install
pnpm dev                 # tout en parallèle
supabase start           # base locale
pnpm db:reset            # migrations + seed local
pnpm db:test             # pgTAP
pnpm db:types            # types TypeScript
pnpm lint && pnpm typecheck && pnpm test && pnpm build
pnpm e2e:web             # Playwright
pnpm e2e:mobile          # Maestro (Mac + simulateur)
```

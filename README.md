# Swapp — cahier des charges pour le développement par agents

Ce dossier se copie **à la racine du futur dépôt Swapp**. Il contient tout ce dont une équipe d'agents (Cursor ou Claude Code) a besoin pour développer l'appli en autonomie : règles, rôles des agents, architecture, base de données, authentification, processus de relecture, et un plan en 9 phases.

## Ce que contient le dossier

| Élément | Rôle |
|---|---|
| `AGENTS.md` | La règle du jeu pour tous les agents : équipe, circulation du travail, questions, Git, points d'arrêt |
| `CLAUDE.md` | Point d'entrée pour Claude Code (importe `AGENTS.md`) |
| `.claude/agents/` | 12 sous-agents : superviseur, 6 développeurs, testeur, 4 relecteurs en lecture seule (lus par Cursor et Claude Code) |
| `.claude/settings.json`, `.claude/hooks/` | Garde-fou Git pour Claude Code : bloque création de branche, merge, rebase, push forcé |
| `.cursor/rules/` | Règles par dossier, chargées automatiquement par Cursor selon les fichiers touchés |
| `docs/INDEX.md` | Où trouver chaque sujet, pour lire une section plutôt qu'un document entier |
| `docs/07-economie-de-contexte.md` | Règles pour limiter la consommation : lecture ciblée, sorties courtes, tests sur ce qui change, modèle par rôle |
| `docs/00-vision.md` | Le produit résumé, non-négociables, périmètre MVP, lancement sans faux profils |
| `docs/01-architecture.md` | Socle infra, choix techniques, environnements, coûts |
| `docs/02-base-de-donnees.md` | Modèle Supabase complet, RLS, RPC, tâches planifiées, matrice de visibilité |
| `docs/03-authentification.md` | Connexion membres (Apple, Google, code email) et admin (Cloudflare Access + MFA) |
| `docs/04-moderation-et-taches-de-fond.md` | Modération IA, notifications, digest, « Pas pour nous » |
| `docs/05-processus-qualite.md` | Cycle d'un lot, portes automatiques, relectures, définition de « terminé » |
| `docs/06-conformite.md` | App Store, RGPD, DSA, accessibilité |
| `docs/annexe-produit.md` | Contenus exacts : grille d'envies, grades, notes, visibilité, Premium |
| `docs/phases/` | 9 phases découpées en lots, avec critères d'acceptation |
| `docs/design/` | `DESIGN.md` (Nuit et corail) et le pack de marque Swapp |
| `docs/SUIVI.md`, `docs/DECISIONS.md`, `docs/rapports/` | Suivi tenu par le superviseur |
| `docs/KICKOFF.md` | Les prompts à coller dans Cursor |
| `.env.example`, `.github/workflows/ci.yml` | Variables et CI |

## Démarrer

1. Crée le dépôt, copie ce dossier à la racine, commite sur `main`.
2. Fais la liste « Avant de lancer la phase 0 » de `docs/rapports/ACTIONS-JUSTIN.md`.
3. Crée la branche `phase/0-socle`.
4. Exporte les écrans du canevas de maquettes en PNG dans `docs/design/maquettes/` (les agents s'en servent comme référence visuelle).
5. Règle le champ `model` de chaque agent selon le tableau de `docs/07-economie-de-contexte.md` (facultatif, réduit le coût).
6. Ouvre une session dans Cursor ou Claude Code et colle le prompt « Démarrer une phase » de `docs/KICKOFF.md`.

À chaque fin de phase, le superviseur s'arrête avec un rapport : tu relis, tu testes, tu fusionnes, tu crées la branche suivante, tu relances.

## Références externes

- Cahier des charges fonctionnel : document « Cahier des charges — App libertine idéale »
- Maquettes : canevas « Swapp — maquette Nuit et corail »
- Charte de marque : page « Charte Swapp »

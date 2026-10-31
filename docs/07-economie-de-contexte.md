# 07 — Économie de contexte

Le coût d'un développement autonome vient surtout de ce que les agents lisent et relisent. Ces règles sont obligatoires pour tous les agents.

## Lire moins

- **Jamais un document entier « au cas où ».** Cherche d'abord (`rg -n "mot" docs/`), puis lis la section utile avec un intervalle de lignes. `docs/INDEX.md` dit où se trouve chaque sujet.
- **Ne relis pas un fichier déjà lu dans la session**, sauf s'il a changé.
- **Code** : `rg` pour localiser, puis lecture ciblée. Pas de lecture de dossiers entiers, pas de `node_modules`, `.next`, `ios/`, `dist`, fichiers générés (`packages/supabase/src/types.ts` : chercher le type voulu, ne pas le lire en entier).
- **Les sous-agents ne lisent pas `AGENTS.md` ni les docs** si le brief leur suffit. Le brief contient les extraits nécessaires.

## Produire des sorties courtes

- **Commandes** : uniquement l'essentiel. Tests avec un rapporteur compact (`vitest --reporter=dot`, `playwright --reporter=line`), et en cas d'échec seulement les 60 dernières lignes (`2>&1 | tail -60`).
- **Rendus des sous-agents** : 40 lignes maximum. Résumé, fichiers modifiés (liste), preuves (commande + résultat en une ligne), questions. Pas de code recopié dans le rendu, le superviseur lit le diff.
- **Verdicts des relecteurs** : format fixe, uniquement les problèmes. Rien sur ce qui va bien.
- **Rapports de phase** : 2 pages maximum.

## Déléguer intelligemment

- **Briefs de 150 lignes maximum** : objectif, critères, chemins, extraits ciblés (avec la référence `fichier:lignes` plutôt que le texte quand l'agent peut le lire lui-même).
- **Reprendre plutôt que relancer** : pour une correction ou une réponse à une question, reprendre la session du sous-agent (son ID) et n'envoyer que le nouvel élément.
- **Relecteurs nourris avec le diff** (`git diff --stat` puis `git diff -- <chemins>`), le brief et les critères. Pas le dépôt entier.
- **Relectures proportionnées** : uniquement les relecteurs obligatoires pour le lot (`docs/05-processus-qualite.md`). Un lot de 20 lignes de documentation n'a besoin que de `relecteur-code`.
- **Parallèle raisonnable** : 3 sous-agents simultanés maximum.

## Tester ce qui a changé

- **Par lot** : portes limitées aux paquets touchés (`pnpm turbo run lint typecheck test --filter=...[HEAD]`), tests pgTAP complets seulement si `supabase/` change, E2E web seulement du parcours touché, E2E mobile à la fin de la phase.
- **En fin de phase** : toutes les portes et tous les E2E, une seule fois.
- Le cache Turborepo reste activé.

## Une session par phase

- Le superviseur démarre une **nouvelle session à chaque phase**. La mémoire passe par `docs/SUIVI.md`, `docs/DECISIONS.md` et les rapports, jamais par l'historique de conversation.
- Si la session devient longue (plusieurs dizaines de lots), le superviseur met `SUIVI.md` à jour et demande une nouvelle session avec le prompt « Reprendre » de `docs/KICKOFF.md`.

## Choisir le bon modèle par rôle

Les fichiers d'agents sont en `model: inherit`. Pour réduire le coût, règle le champ `model` selon ce tableau avec les modèles disponibles dans ton outil :

| Niveau | Agents | Pourquoi |
|---|---|---|
| Le plus puissant | superviseur, dev-base-de-donnees, relecteur-securite | Décisions, RLS et vie privée : une erreur coûte très cher |
| Intermédiaire | dev-backend, dev-mobile, dev-web, dev-admin, relecteur-code, relecteur-conformite | Implémentation guidée par un brief précis |
| Rapide et économique | dev-socle, testeur-qa, relecteur-design | Tâches cadrées, listes de vérification |

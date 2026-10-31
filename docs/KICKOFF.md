# Prompts de lancement

Le dépôt fonctionne avec **Cursor** et avec **Claude Code** :
- les sous-agents sont dans `.claude/agents/`, que les deux outils lisent ;
- les règles par dossier sont dans `.cursor/rules/` (chargées automatiquement par Cursor, indiquées par `CLAUDE.md` pour Claude Code) ;
- Claude Code bloque en plus les commandes Git interdites avec un hook (`.claude/hooks/garde-git.sh`).

Une nouvelle session par phase (voir `docs/07-economie-de-contexte.md`).

## Démarrer une phase

```
Tu es le superviseur de Swapp. Applique .claude/agents/superviseur.md et docs/07-economie-de-contexte.md.
Lis docs/SUIVI.md, docs/DECISIONS.md et le fichier de la phase en cours dans docs/phases/.
Vérifie la branche, puis exécute tous les lots de la phase en autonomie complète :
délègue aux sous-agents, réponds à leurs questions, fais relire chaque lot, fais passer les portes et les E2E, commite, mets à jour le suivi.
Ne t'arrête qu'aux 5 points d'arrêt d'AGENTS.md. À la fin de la phase, écris le rapport et arrête-toi.
```

- **Cursor** : ouvre une session Agent sur la branche de phase, choisis le modèle le plus puissant pour cette session (c'est le superviseur), colle le prompt.
- **Claude Code** : dans le dossier du dépôt, lance `claude`, puis colle le prompt. Pour une phase longue sans surveillance, autorise à l'avance les commandes courantes (`pnpm`, `supabase`, `git add`, `git commit`, `git push`) avec `/permissions`, le hook Git restant actif.

## Reprendre après une interruption

```
Tu es le superviseur de Swapp. Reprends là où docs/SUIVI.md s'est arrêté.
Vérifie d'abord l'état réel (git status, portes sur les paquets modifiés) avant de continuer.
```

## Après une fin de phase

1. Lis `docs/rapports/phase-N.md` et `docs/rapports/ACTIONS-JUSTIN.md`.
2. Teste toi-même les parcours de la phase (liste dans le rapport).
3. Fusionne la branche dans `main`, crée `phase/N+1-...`, mets « Phase en cours » à jour dans `docs/SUIVI.md`.
4. Ouvre une **nouvelle** session et relance « Démarrer une phase ».

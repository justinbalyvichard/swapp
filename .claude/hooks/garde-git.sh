#!/bin/bash
# Bloque les commandes Git interdites par AGENTS.md (Justin crée les branches lui-même).
input=$(cat)
cmd=$(printf '%s' "$input" | tr '\n' ' ')
if printf '%s' "$cmd" | grep -Eq 'git[^"]*(checkout[^"]* -b|checkout[^"]* -B|switch[^"]* -c|switch[^"]* -C|branch [^-"][^"]*|worktree add|merge |rebase|push[^"]*(--force|-f( |")|--force-with-lease)|reset --hard)'; then
  echo "Commande Git interdite par AGENTS.md : pas de création de branche, merge, rebase, push forcé ni worktree. Si la branche de phase manque, écris le point d'arrêt dans docs/rapports/ACTIONS-JUSTIN.md et arrête-toi." >&2
  exit 2
fi
if printf '%s' "$cmd" | grep -Eq 'git[^"]*(push[^"]* main([^a-zA-Z0-9/_-]|$)|push[^"]*:main|checkout main|switch main)'; then
  echo "Aucune opération sur main. Travaille sur la branche de phase." >&2
  exit 2
fi
exit 0

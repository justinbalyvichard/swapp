# CLAUDE.md

@AGENTS.md

## Règles par dossier (à lire seulement avant de modifier un fichier de ce dossier)

| Dossier | Règle |
|---|---|
| tout fichier `.ts` / `.tsx` | `.cursor/rules/10-typescript.mdc` |
| `supabase/` (hors `functions/`) | `.cursor/rules/20-supabase.mdc` |
| `supabase/functions/` | `.cursor/rules/21-edge-functions.mdc` |
| `apps/mobile/`, `packages/ui-native/` | `.cursor/rules/30-mobile.mdc` |
| `apps/web/`, `packages/ui-web/` | `.cursor/rules/31-web.mdc` |
| `apps/admin/` | `.cursor/rules/32-admin.mdc` |
| tests, `e2e/`, `supabase/tests/` | `.cursor/rules/40-tests.mdc` |
| écrans et textes | `.cursor/rules/50-design-textes.mdc` |

Les règles Git d'`AGENTS.md` sont en plus imposées par un hook (`.claude/hooks/garde-git.sh`).

# Phase 0 — Socle

**Branche** : `phase/0-socle` · **Objectif** : un monorepo qui démarre, se teste et se déploie à vide, avec le design system en place.

### P0-01 · dev-socle · Monorepo
pnpm + Turborepo, `packages/config` (tsconfig strict, lint, Vitest), scripts racine (`dev`, `lint`, `typecheck`, `test`, `build`, `db:*`, `e2e:*`).
- [ ] `pnpm install && pnpm lint && pnpm typecheck && pnpm test && pnpm build` verts sur un dépôt neuf
- [ ] Versions exactes épinglées, consignées dans `DECISIONS.md`

### P0-02 · dev-socle · Packages partagés vides mais branchés
`core`, `supabase`, `i18n` (FR, structure tu/vous et je/nous), avec un test exemple chacun.
- [ ] Chaque package importable depuis les 3 applis

### P0-03 · dev-socle · Design tokens et composants de base
`ui-tokens` depuis `docs/design/DESIGN.md` et `docs/design/marque/tokens/`. `ui-native` et `ui-web` : Bouton (principal, secondaire, discret), Liste groupée, Sélecteur segmenté, Interrupteur, Barre d'onglets, Bandes 70s, Porte-clés, Photo en attente (trame de points), Badge vérifié, Logo (symbole, horizontal).
- [ ] Aucune valeur de couleur en dur hors `ui-tokens` (règle lint)
- [ ] Page de démonstration des composants (web) et écran de démonstration (mobile, route dev uniquement)
- [ ] relecteur-design : APPROUVE

### P0-04 · dev-base-de-donnees · Supabase local
`supabase init`, extensions (postgis, pg_cron, pg_net, pgmq, pgcrypto, pg_trgm, pgtap), schémas `private` et `admin`, test pgTAP minimal, `pnpm db:types`.
- [ ] `supabase db reset && supabase test db` verts

### P0-05 · dev-mobile · Squelette Expo
expo-router, 4 onglets vides (Découvrir, Soirées, Messages, Profil), écran de lancement (symbole centré + bandes, cf. `docs/design/marque/app-ios/`), icône d'app, nom affiché neutre, Sentry (`sendDefaultPii: false`), `eas.json` (development, preview, production).
- [ ] L'appli démarre sur le simulateur iOS avec l'icône et l'écran de lancement Swapp

### P0-06 · dev-web · Squelette Next.js PWA
Manifeste, favicons et icônes de `docs/design/marque/web/`, `@supabase/ssr`, route vitrine `/` vide, Sentry.
- [ ] Lighthouse PWA installable ; favicon visible sur onglet clair et sombre

### P0-07 · dev-admin · Squelette console
Next.js séparé, page de connexion vide, middleware de protection (refus par défaut).
- [ ] Toute route non publique renvoie vers la connexion

### P0-08 · dev-socle · CI et E2E
`.github/workflows/ci.yml` (G1–G7 + E2E web), gitleaks, Playwright et Maestro initialisés avec un test « l'appli démarre ».
- [ ] CI verte sur la branche

### P0-09 · dev-socle · Environnements
`.env.example` complet et commenté, chargement validé par zod dans chaque appli, `docs/DEV.md` (installer, lancer, tester).
- [ ] Un test échoue si une variable publique contient `service_role` ou une clé secrète

**Fin de phase** : rapport `docs/rapports/phase-0.md`.

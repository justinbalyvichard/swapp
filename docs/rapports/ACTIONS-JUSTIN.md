# Actions attendues de Justin

Le superviseur ajoute ici tout ce qui demande une intervention humaine (points d'arrêt d'`AGENTS.md`).

## Avant de lancer la phase 0

- [ ] Créer le dépôt GitHub et la branche `phase/0-socle`
- [ ] Installer : Node LTS, pnpm, Docker (pour Supabase local), Supabase CLI, Xcode + simulateur iOS, Maestro, compte Expo
- [ ] Copier `.env.example` en `.env.local` (les valeurs locales sont données par `supabase start`)

## Xcode et iPhone (ce que les agents ne peuvent pas faire)

- [ ] **Avant la phase 0** : installer Xcode, l'ouvrir une fois, accepter la licence, télécharger le simulateur iOS, connecter son identifiant Apple (Réglages › Comptes)
- [ ] **Fin de phase 2** : brancher l'iPhone, activer le mode développeur, installer le build de développement fourni par les agents ; tester la connexion Apple, Google et Face ID sur le vrai téléphone
- [ ] **Fin de phase 8** : tester les notifications sur l'iPhone ; lancer la mesure d'ouverture avec Instruments si le rapport le demande
- [ ] **Si un rapport le signale** : récupérer un journal de plantage natif dans Xcode (Window › Devices and Simulators)

## Avant la bêta (peut attendre)

- [ ] Créer la société (SAS/SASU) et le compte Apple Developer à son nom
- [ ] Créer les projets Supabase `swapp-staging` et `swapp-prod` en région UE (prod en offre Pro)
- [ ] Choisir et contractualiser le prestataire de vérification (Veriff, Ubble ou Onfido)
- [ ] Ouvrir les comptes Sightengine, fournisseur LLM UE, Resend, Sentry (région UE), PostHog UE, Cloudflare (Access)
- [ ] Acheter le nom de domaine, vérifier la marque « Swapp » (INPI, EUIPO)
- [ ] Faire valider par l'avocat : CGU, CGV, charte, politique de confidentialité, AIPD

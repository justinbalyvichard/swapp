# Phase 2 — Authentification et inscription

**Branche** : `phase/2-inscription` · **Référence** : `docs/03-authentification.md`, maquettes Bienvenue, Lancement, Type de profil, Qui peut te voir, Selfie.

### P2-01 · dev-backend · Configuration Auth
Apple, Google, OTP email (modèles FR neutres, SMTP Resend documenté), CAPTCHA web, limites de débit. Clients `packages/supabase` mobile (SecureStore) et web (`@supabase/ssr`).

### P2-02 · dev-mobile · Bienvenue et connexion
Écran Bienvenue (logo horizontal inversé, 3 boutons), Apple natif, Google natif, OTP 6 chiffres.
- [ ] Les 3 méthodes fonctionnent en local (Apple et Google simulés par mock du jeton d'identité en E2E)

### P2-03 · dev-mobile · Type de profil, âge, ville, consentement
Type (solo : femme, homme, trans, non-binaire ; couple F/H, F/F, H/H), date(s) de naissance (< 18 ans : refus sans création), ville (choix dans une liste ou position approximative), consentement données sensibles + charte en 5 lignes (table `consents`).
- [ ] 3 écrans maximum avant l'appli (en comptant P2-04 et P2-05)

### P2-04 · dev-mobile · Qui peut te voir
4 niveaux, Flouté présélectionné, effet immédiat (`set_visibility`).

### P2-05 · dev-backend + dev-mobile · Selfie de vérification asynchrone
Edge Function `verify-start`, adaptateur `VerificationProvider` (mock), webhook signé, selfie supprimé après décision, push de service. Badge « Vérification en cours » immédiat ; refus avec motif et nouvel essai.
- [ ] Le membre continue sans attendre ; jusqu'à 3 intérêts mis en attente (livrés ou annulés selon le résultat, logique branchée en P5)

### P2-06 · dev-mobile + dev-backend · Couple
Invitation du ou de la partenaire (code et lien), onboarding et vérification du second membre, profil couple actif quand les deux sont vérifiés, selfie à deux pour « Couple vérifié ».

### P2-07 · dev-mobile + dev-web · Ville en attente
Écran « Swapp arrive à {ville} » avec compteur réel, ce qu'on peut déjà faire (profil, envies, Soirées), code d'invitation. Découvrir et Messages verrouillés tant que la ville est `waitlist`.
- [ ] Aucun chiffre inventé ; le compteur vient de `city_status`

### P2-08 · dev-mobile + dev-backend · Sécurité du compte
Verrou PIN / Face ID, vignette neutre en arrière-plan, déconnexion de tous les appareils, suppression du compte depuis l'appli (révocation du jeton Apple, effacement planifié).

### P2-09 · dev-web · Parité PWA
Connexion et inscription identiques sur la PWA (sans PIN natif ; verrou par code optionnel).

### P2-10 · testeur-qa · E2E
Inscription solo, inscription couple complète, refus < 18 ans, vérification acceptée puis refusée, ville en attente, suppression de compte.

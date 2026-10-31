# Phase 8 — Notifications, Premium, finitions, préparation du lancement

**Branche** : `phase/8-lancement`

### P8-01 · dev-backend + dev-mobile + dev-web · Notifications push
Enregistrement des jetons, Edge Function `send-push`, Expo Push et Web Push, texte neutre, 3 types + service, plafond 5/jour avec bascule au digest.

### P8-02 · dev-backend · Digest du soir et coach de profil
Digest à l'heure choisie (email neutre ou in-app selon réglage), coach hebdomadaire, repères réalistes par type de profil.

### P8-03 · dev-mobile + dev-web · Premium « Gratuit pour l'instant »
Écran de la maquette Premium, suggestions aux 4 moments prévus, une à la fois, au plus une par jour, jamais à l'ouverture. `entitlements` en `launch_free`. Aucun lien de paiement.

### P8-04 · dev-backend · Hygiène et conservation
Inactivité 60 j / 6 mois (email de prévenance), purge des photos à 30 j, durées de conservation de la table du cahier des charges.

### P8-05 · dev-mobile + dev-web · Mesure d'audience
PostHog UE, sans autocapture ni enregistrement de session, identifiants hachés, liste d'événements dans `docs/ANALYTICS.md`, indicateur clé (conversations → rencontres).

### P8-06 · dev-socle + dev-backend · Durcissement
App Attest et plafond de comptes par appareil, revue des limites de débit, filtrage Sentry, en-têtes de sécurité web (CSP stricte, HSTS), audit des dépendances.

### P8-07 · dev-mobile + dev-web · Accessibilité et performance
VoiceOver sur tous les écrans, taille dynamique, contrastes ; ouverture < 2 s ; images optimisées.

### P8-08 · dev-mobile · Préparation App Store
`PrivacyInfo.xcprivacy`, fiche « Données collectées », notes de soumission (4.3(b), 1.2), textes de fiche sans contenu suggestif, captures à partir de comptes de démonstration clairement fictifs **uniquement pour les captures**, configuration EAS production. Soumission : action de Justin.

### P8-09 · dev-socle · Runbook
`docs/RUNBOOK.md` : déploiement des migrations en production, sauvegardes et test de restauration mensuel, supervision, rotation des clés, incident de fuite, procédure mineur suspecté.

### P8-10 · superviseur · Relecture finale
Les 4 relecteurs sur l'ensemble du produit, tous les E2E, rapport de lancement `docs/rapports/phase-8.md` avec la liste complète des actions de Justin avant la bêta.

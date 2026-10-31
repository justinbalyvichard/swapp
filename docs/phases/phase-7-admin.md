# Phase 7 — Console d'administration et modération

**Branche** : `phase/7-admin` · **Référence** : maquette Admin, `docs/03` (partie admin), `docs/04`.
Relecteur-securite obligatoire sur chaque lot.

### P7-01 · dev-admin · Accès
Connexion, MFA TOTP obligatoire (enrôlement au premier accès), garde `aal2` + rôle sur chaque route, déconnexion après 15 min, script de création du compte de Justin, procédure Cloudflare Access documentée (`docs/RUNBOOK.md`).

### P7-02 · dev-admin · Tableau de bord
Inscrits, vérifiés, actifs de la semaine, répartition par type, taux de réponse, délai moyen de modération, files en attente, progression des villes, « temps humain estimé aujourd'hui ».

### P7-03 · dev-backend · Triage et sanctions automatiques
Edge Function `triage-case` (adaptateur LLM + mock), table de règles du chapitre « Signalements et sanctions », bannissements en réflexion 24 h, mineur suspecté : gel + alerte immédiate.

### P7-04 · dev-admin · Files
Signalements (tri par gravité), vérifications (doublons de visage), photos (revue humaine).

### P7-05 · dev-admin · Fiche membre et actions
Profil, historique, sanctions, appareils, comptes liés, couple et solos ; actions avec motifs pré-écrits ; tout est journalisé.

### P7-06 · dev-admin + dev-mobile · Bannissements et appels
Annulation pendant la réflexion ; formulaire d'appel côté membre (dans l'appli, 15 jours) ; traitement dans la console.

### P7-07 · dev-admin · Clubs et soirées
Validation des comptes pro et des soirées.

### P7-08 · dev-admin + dev-mobile · Support
Formulaire de support dans l'appli, réponses types, historique, objectif 24 h.

### P7-09 · dev-admin · RGPD et réquisitions
Demandes d'export et de suppression, export des preuves pour réquisition (journalisé).

### P7-10 · dev-admin · Contenus et réglages
Banque « Pas pour nous », charte, textes du coach, catalogue d'envies, seuils de confiance IA, seuils et statut des villes.

### P7-11 · dev-backend · Récapitulatifs admin
Une alerte par jour (sauf mineur), tirage de 20 décisions le lundi.

### P7-12 · testeur-qa · E2E et attaque
Parcours de modération complets ; tentatives d'accès sans MFA, avec un compte membre, sans Cloudflare (local : en-tête simulé) ; vérification que tout est journalisé.

# 06 — Conformité (Apple, RGPD, DSA)

L'agent `relecteur-conformite` vérifie chaque phase contre cette liste. Un point « bloquant » non respecté bloque la phase.

## App Store

| Règle | Exigence vérifiable | Bloquant |
|---|---|---|
| 1.1.4 | Aucune nudité ni pose sexuelle, nulle part ; pipeline photo actif sur profil, albums, messages | Oui |
| 1.2 | Filtrage avant diffusion, signalement depuis chaque profil, message et photo, blocage en 1 tap, contact publié dans l'appli | Oui |
| 1.2 | Aucune notation de l'apparence : les 6 critères ne parlent jamais du physique | Oui |
| 2.3.8 | Captures, icône, description sans contenu suggestif ; pas le mot « hookup » | Oui (au moment de la soumission) |
| 3.1.1 | Tout achat dans l'appli iOS passe par l'achat intégré (au MVP : pas d'achat, paywall « Gratuit pour l'instant », aucun lien vers un paiement externe) | Oui |
| 4.3(b) | Notes de soumission qui décrivent les fonctions signature (Radar, intérêt gradué, couple comme équipe, visibilité à 4 niveaux, modération) | Oui (soumission) |
| 4.8 | Sign in with Apple proposé dès que Google l'est | Oui |
| 5.1.1(v) | Suppression du compte depuis l'appli, révocation du jeton Apple | Oui |
| 5.1.1(ix) | Compte Apple Developer au nom d'une société | Action de Justin |
| 5.1.2 | Répertoire jamais stocké ni contacté ; texte d'autorisation clair | Oui |
| Confidentialité | Manifeste de confidentialité (`PrivacyInfo.xcprivacy`) et fiche « Données collectées » exacts | Oui |

## RGPD

| Exigence | Où |
|---|---|
| Consentement explicite au traitement de données sensibles (art. 9), séparé des CGU, à l'inscription | Écran d'inscription, table `consents` (version, date) |
| Hébergement et traitement en UE | Supabase UE, Sightengine, LLM UE, Resend UE, PostHog UE, Sentry UE (région `de`) |
| Minimisation | Position floutée, pas d'historique, selfie supprimé après décision, pièce d'identité jamais stockée |
| Export en 1 tap | `request_data_export` → archive JSON + photos, lien signé 7 jours |
| Suppression réelle | Photos sous 30 jours, compte effacé sous 30 jours sauf identification légale 1 an |
| Décisions automatisées (art. 22) | Motif, mention « automatique », appel humain |
| Durées de conservation | Table « Données et durées » du cahier des charges, appliquées par pg_cron |
| AIPD, registre, contrats de sous-traitance | Action de Justin + avocat (hors code) |

## DSA

Point de contact affiché, signalement accessible partout, motif de chaque sanction, procédure d'appel, mention des décisions automatiques, rapport de transparence possible depuis la console (comptage des décisions).

## Lutte contre la prostitution

Détection des tarifs et coordonnées (texte et images), bannissement des profils vénaux, conservation des preuves 1 an, export pour réquisition depuis la console. La lutte doit être **documentée** : chaque décision est tracée dans `admin.cases` et `admin.sanctions`.

## Accessibilité

WCAG 2.1 AA : contrastes (les tokens de `DESIGN.md` ont été choisis pour passer), taille de texte dynamique iOS respectée, cibles ≥ 44 px, VoiceOver sur tous les écrans du MVP, aucune information portée par la couleur seule.

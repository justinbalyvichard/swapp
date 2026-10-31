# 00 — Vision produit (résumé pour les agents)

Source complète : le cahier des charges fonctionnel « Cahier des charges — App libertine idéale » (Claude Docs). Ce fichier en est le résumé opérationnel. En cas de doute, le superviseur tranche et consigne dans `docs/DECISIONS.md`.

## Mission

Swapp est l'appli de rencontre de référence pour les libertins en France : couples, femmes seules, hommes seuls, personnes trans et non-binaires, débutants comme initiés. Simple, discrète, honnête sur ses prix, sans spam, sans faux profils.

## Plateformes

| Appli | Techno | Rôle |
|---|---|---|
| `apps/mobile` | Expo (React Native), iOS d'abord | Appli principale. Android plus tard, même code |
| `apps/web` | Next.js, PWA | Version web installable + site vitrine (routes publiques) |
| `apps/admin` | Next.js | Console d'administration, sous-domaine séparé |

## Non négociables (toute PR qui en viole un est refusée)

1. **Consentement d'abord** : personne ne reçoit de contenu ou de message qu'il n'a pas autorisé.
2. **Discrétion par défaut** : visibilité « Flouté » par défaut, icône et nom neutres, push au texte neutre, distance arrondie, aucune trace de consultation de profil.
3. **Vérifié ou muet** : un profil non vérifié peut regarder, pas écrire.
4. **Aucune nudité nulle part** (iOS, web, messages). Lingerie et maillot au maximum. Règles Apple 1.1.4 et 1.2.
5. **On note le comportement, jamais le physique** (Apple 1.2, « hot-or-not » interdit).
6. **Aucun faux profil, jamais**, y compris pour amorcer le lancement. Les données de test n'existent qu'en local et en staging, marquées `is_test = true`, et la production refuse toute ligne de test.
7. **Fluidité** : toute action utilisateur s'affiche comme réussie immédiatement (UI optimiste). Le serveur confirme en arrière-plan. Aucun écran de chargement plein écran.
8. **Calme** : 3 types de push seulement + messages de service, plafond 5/jour, le reste dans le digest du soir. Zéro marketing.
9. **Prix honnête** : aucun boost, super-like ou jeton payant. Un seul Premium, affiché « Gratuit pour l'instant » au lancement.
10. **Données sensibles (RGPD art. 9)** : hébergement UE, minimisation, suppression réelle, aucun traceur publicitaire.

## Navigation

4 onglets : **Découvrir**, **Soirées**, **Messages**, **Profil**. Une action principale par écran.

## Périmètre MVP

| Module | MVP | V2 (ne pas développer) |
|---|---|---|
| Inscription | Type de profil, âge 18+, ville, « Qui peut te voir ? », selfie de vérification async, charte, 3 écrans max | Vérification d'identité obligatoire |
| Profil couple | Un profil, deux identités, validation des intérêts à 1 ou à 2, profils solo liés confirmés par le partenaire | Fil privé « Entre nous » |
| Envies et limites | Grille 8 catégories Oui / Curieux / Non par membre, limites, mise en avant de 6 envies, accord visible / désaccord privé | Score de compatibilité affiché |
| Découvrir / Radar | Recherche gratuite illimitée, filtres libertins, Radars enregistrés (digest), mode Ce soir | Mode Voyage |
| Intérêt gradué | Clin d'œil, Curieux de…, Demande d'album, chat ouvert si réciproque, « Pas pour nous » | Invitation datée |
| Messagerie | Texte temps réel, photos pré-modérées, blocage, signalement, détection liens externes, pause | Messages vocaux, traduction, appel vidéo |
| Albums | Visage flouté par défaut, album privé sur demande, révocation | Filigrane invisible |
| Confidentialité | 4 niveaux de visibilité, cercle masqué, masquer une personne, PIN / Face ID, vignette floutée, distance arrondie | Bouton panique |
| Soirées | Agenda clubs et soirées privées, inscription, comptes pro vérifiés | « J'y vais » entre contacts, billetterie, avis lieux |
| Réputation | Badges Vérifié / Couple vérifié / Identité vérifiée (facultatif), « Vous vous êtes vus ? », notes 6 critères à l'aveugle, grades | Certifié par la communauté |
| Débutants | Guide des codes | Soirées découverte mises en avant |
| Ajouts | Profils mis de côté, notes privées, carnet de rencontres, disponibilités, santé sexuelle (facultatif) | — |
| Lancement | Liste d'attente, villes à seuil, codes d'invitation, site vitrine, mesure d'audience sans traceur | — |
| Premium | Paywall affiché « Gratuit pour l'instant », moments de suggestion | Paiement réel (IAP Apple + Stripe) |
| Console admin | Tout le chapitre « Console d'administration » | Rôles multiples activés |
| Modération IA | Photos (après publication, sauf messages), textes, signalements, sanctions auto, délai 24 h | Modèle sur téléphone |

## Lancement sans faux profils (cold start)

Le problème : au début, il n'y a personne. La solution n'est jamais de simuler, mais de **ne pas montrer le vide** et de **remplir avec des gens réels**.

- **Villes à seuil** : table `cities` avec `status` (`waitlist`, `open`) et seuils réglables dans la console (défaut : 150 profils vérifiés, dont ≥ 40 % couples + femmes seules). Tant qu'une ville est en `waitlist`, l'appli s'ouvre en mode « Swapp arrive à {ville} » : création du profil, vérification, envies, réglages, onglet Soirées, compteur réel « 87 / 150 profils vérifiés ». Découvrir et Messages sont verrouillés.
- **Ouverture synchronisée** : quand le seuil est atteint (ou sur décision admin), la ville passe `open` et tous ses membres reçoivent un message de service « Swapp est ouvert à {ville} ».
- **Codes d'invitation** : chaque profil vérifié a 3 codes (réglable). Les clubs partenaires ont des lots de codes. Un code fait passer devant dans la liste d'attente, rien de plus.
- **Numéro de membre** : chaque profil vérifié reçoit un numéro définitif (« Membre n° 128 »), privé par défaut, affichable s'il le souhaite. Aucun avantage attaché, pas de badge « fondateur ».
- **Soirées d'abord** : l'onglet Soirées fonctionne dans une ville en attente (contenu réel des clubs).
- **Radars enregistrés** : « On te prévient dès qu'un profil qui te correspond arrive. »
- **Rayon élastique** : si moins de 10 résultats, le rayon s'élargit automatiquement par paliers, annoncé honnêtement (« Peu de profils à 30 km, on a élargi à 60 km »).
- **Aucun compteur décourageant** : jamais « 3 profils près de toi ». En ville ouverte, pas de total affiché.
- **Interdits** : profils générés, comptes « maison », messages automatiques déguisés en membres, compteurs gonflés.

## Indicateur clé

Part des conversations qui débouchent sur une rencontre ou une soirée confirmée. Pas le temps passé dans l'appli.

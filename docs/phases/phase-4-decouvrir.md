# Phase 4 — Découvrir et Radar

**Branche** : `phase/4-decouvrir` · **Référence** : maquettes Découvrir, Radar, Fiche.

### P4-01 · dev-mobile · Découvrir
Liste selon la maquette, filtres libertins (type, âges de chaque membre, envies, expérience, lieux, reçoit ou se déplace, badges, grade minimum), préchargement des 2 pages suivantes, rayon élastique annoncé honnêtement, aucun total de profils affiché.

### P4-02 · dev-mobile · Fiche d'un profil
Selon la maquette : photos selon la relation, badges, grade, note (dès 5), envies mises en avant avec « nous deux / elle / lui », limites, distance arrondie, « actif cette semaine », actions (intérêt, mettre de côté, note privée, bloquer, signaler).
- [ ] Aucune trace de consultation créée (test)

### P4-03 · dev-mobile + dev-backend · Radars enregistrés
Création depuis les filtres, 2 gratuits (au-delà : suggestion Premium « Gratuit pour l'instant »), nouveaux profils correspondants envoyés au digest (jamais en push).

### P4-04 · dev-mobile · Mode Ce soir
Disponible 12 h, visible seulement des profils compatibles.

### P4-05 · dev-mobile · Mis de côté, notes privées, disponibilités

### P4-06 · dev-base-de-donnees · Équité et anti-aspiration
Rotation, coup de pouce des 14 premiers jours, bonus de grade plafonné, retrait des inactifs > 60 j, plafond de profils consultables par heure avec message calme.

### P4-07 · dev-web · Parité PWA

### P4-08 · testeur-qa · E2E et performance
Filtres combinés, Radar → digest, Ce soir, plafond d'aspiration, temps de réponse `discover` (< 400 ms en local sur le jeu de charge).

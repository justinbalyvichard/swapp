# Phase 6 — Soirées, rencontres, réputation, lancement par ville

**Branche** : `phase/6-soirees` · **Référence** : maquettes Soirées, Fiche soirée, Notation ; `docs/00-vision.md` section « Lancement sans faux profils ».

### P6-01 · dev-web + dev-backend · Comptes pro et soirées
Demande de compte pro (SIRET pour un club, identité pour un organisateur), création de soirée (web), statut `a_valider` jusqu'à validation dans la console (P7).

### P6-02 · dev-mobile · Onglet Soirées
Agenda filtrable (date, ville, ambiance, accepte les solos, débutants), fiche soirée, inscription et liste d'attente, rappel push la veille. **Fonctionne aussi en ville en attente.**

### P6-03 · dev-mobile · Guide des codes
Contenu pour débutants (rédigé par l'agent, validé par relecteur-design et relecteur-conformite).

### P6-04 · dev-mobile + dev-base-de-donnees · « Vous vous êtes vus ? » et carnet
Rencontre déclarée après une conversation ou une soirée, confirmation par les deux, carnet de rencontres privé.

### P6-05 · dev-mobile + dev-backend · Notes et grades
Notation 6 critères (maquette), à l'aveugle, révélation, recalcul de la réputation, badges et grade sur la fiche, « Nouveau » avant 5 notes, examen automatique si respect ≤ 2.
- [ ] Aucun critère physique, aucune note détaillée visible par le noté

### P6-06 · dev-backend + dev-base-de-donnees · Villes à seuil et invitations
Tâche d'ouverture au seuil, message de service synchronisé à toute la ville, codes d'invitation (3 par profil vérifié, lots pour les clubs), passe-droit dans la liste d'attente uniquement.

### P6-06b · dev-base-de-donnees + dev-mobile · Numéro de membre
Trigger d'attribution à la première vérification (décision D-009), affichage « Membre n° 128 » sur la carte de son propre profil, réglage « Afficher mon numéro sur mon profil » (désactivé par défaut) dans la rubrique Visibilité, affichage discret sous le pseudo si activé.
- [ ] Tests pgTAP : pas de numéro avant vérification ; numéro stable après pause, changement de pseudo ou revérification ; jamais renvoyé à un tiers si privé ; aucun numéro pour `is_test`
- [ ] Le numéro n'apparaît dans aucune URL, aucun filtre, aucun tri

### P6-07 · dev-web · Site vitrine
Accueil discret, comment ça marche, confidentialité, FAQ, liste d'attente par ville, guide des codes en articles (SEO), liens App Store et PWA, mentions légales `[À VALIDER PAR L'AVOCAT]`.

### P6-08 · testeur-qa · E2E
Ville en attente → seuil atteint → ouverture ; inscription à une soirée ; rencontre confirmée → notes croisées → grade ; code d'invitation.

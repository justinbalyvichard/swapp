# Phase 3 — Profil, photos, envies, confidentialité

**Branche** : `phase/3-profil` · **Référence** : maquettes Profil, Envies, Visibilité ; cahier des charges « Gestion du profil » (10 rubriques).

### P3-01 · dev-mobile · Onglet Profil
Bandeau du niveau de visibilité en haut (« Tu es en mode Fantôme : personne ne te voit »), 10 rubriques en listes groupées, aperçu « Voir mon profil comme… » (couple, femme, homme).

### P3-02 · dev-mobile · Identité et présentation
Pseudo (modifiable 1 fois par mois), orientation par membre, champs facultatifs, accroche (80 car.), « Qui on est », « Ce qu'on cherche », 3 questions au choix.

### P3-03 · dev-mobile + dev-backend · Photos publiques
1 à 6 photos, envoi optimiste (visible aussitôt), compression WebP et EXIF retiré, ordre par glisser-déposer, version floutée générée côté serveur, photo de vérification jamais exposée.
- [ ] Le flou couvre au minimum le visage ; au MVP, flou de l'image entière accepté (décision à consigner)

### P3-04 · dev-backend · Modération photo
Pipeline complet de `docs/04` (adaptateur Sightengine + mock), retrait avec notification et motif, gel + alerte si mineur apparent, reprise des photos bloquées, correspondance avec le selfie, empreintes perceptuelles.

### P3-05 · dev-backend + dev-mobile · Album privé
Jusqu'à 30 photos, demandes d'accès, accord, révocation immédiate, Edge Function `photo-url` (URL signées 10 min selon les droits). Alerte de capture d'écran sur iPhone.

### P3-06 · dev-mobile · Grille d'envies
Interaction de la maquette Envies : 8 catégories dépliables, Oui / Curieux / Non en un tap par membre, limites (liste + champ libre), santé sexuelle facultative, mise en avant de 6 envies, affichage « nous deux / elle / lui », désaccord visible du couple seulement.
- [ ] relecteur-conformite : libellés descriptifs, aucun vocabulaire cru

### P3-07 · dev-mobile + dev-base-de-donnees · Recherche, contact et visibilité
« Ce que je cherche », « Qui peut me contacter », « Profils ouverts à… », visibilité (4 niveaux, statut en ligne, accusés de lecture, distance et âge masquables, accès album), cercle masqué (`expo-contacts`, empreintes HMAC, aucune conservation), masquer une personne précise.

### P3-08 · dev-mobile · Réglages du couple
Validation des intérêts à 1 ou à 2, transparence ou « chacun son jardin » (modifiable seulement à deux), profils solo liés (création, confirmation par le partenaire, lien visible ou discret, grille d'envies propre), séparation.

### P3-09 · dev-mobile + dev-backend · Notifications, sécurité, compte
Réglages de push et heure du digest, liste des bloqués, double authentification, icône alternative, pause du profil (≤ 3 mois), export des données.

### P3-10 · dev-backend · Modération des textes du profil
Adaptateur `TextModerator` (Mistral UE + mock), refus avec motif clair à l'enregistrement.

### P3-11 · dev-web · Parité PWA

### P3-12 · testeur-qa · E2E
Photo conforme publiée instantanément ; photo refusée retirée avec motif ; album accordé puis révoqué ; changement de visibilité effectif immédiatement (vérifié depuis un second compte) ; cercle masqué dans les deux sens.

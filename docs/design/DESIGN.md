# DESIGN.md — Appli libertine

Direction retenue le 31 octobre 2026 : **Apple × Hôtel 70s, palette Nuit et corail**.

## Intention

La structure et la clarté d'iOS (grand titre, listes groupées, sélecteur segmenté, interrupteurs, barre d'onglets), habillées d'une ambiance d'hôtel des années 70 : bandes de couleur, porte-clés de chambre, trame d'impression. Sombre, chaleureux, discret. L'appli doit paraître native sur iPhone et ne ressembler à aucune autre appli de rencontre.

## Couleurs

| Token | Hex | Usage |
| --- | --- | --- |
| `bg` | `#121A26` | Fond de l'appli |
| `surface` | `#1C2635` | Cartes, listes groupées |
| `segment` | `#263244` | Fond du sélecteur segmenté, bouton Passer |
| `segment-on` | `#3A4A62` | Segment actif |
| `line` | `#2E3A4C` | Séparateurs de liste (0,5 px) |
| `text` | `#EAF0F7` | Texte principal |
| `muted` | `#9AA8BA` | Texte secondaire, valeurs de liste |
| `nav-muted` | `#7F8C9E` | Onglets inactifs |
| `accent` | `#F2A38A` | Action principale, onglet actif, liens, coches, porte-clés |
| `on-accent` | `#2A1510` | Texte et icônes posés sur l'accent |
| `secondary` | `#2B3A52` | Action secondaire (Clin d'œil) |
| `toggle-on` | `#E08A6E` | Interrupteur activé |
| `photo` | `#4D6178` | Fond des photos en attente |
| `photo-dot` | `#1C2635` | Trame de points des photos en attente |
| `chip` | `rgba(18,26,38,.82)` | Étiquettes posées sur une photo |
| `bar` | `rgba(18,26,38,.94)` | Barre d'onglets |

Bandes 70s (4 px chacune, de haut en bas) : `#2B4A6E`, `#4D6F95`, `#E08A6E`, `#F2C2A8`.

Règle : un seul accent corail par écran pour l'action principale. Jamais de dégradé, jamais de texte blanc sur le corail.

## Typographie

Police système d'Apple (SF Pro), sur le web `-apple-system, 'SF Pro Text', 'Helvetica Neue', sans-serif`.

| Rôle | Taille | Graisse |
| --- | --- | --- |
| Grand titre | 34 px | 700 |
| Nom de profil | 22 px | 700 |
| Texte de liste, boutons | 17 px (boutons 17 px, 600) | 400 |
| Texte courant | 15 px | 400 |
| Légendes, aides | 13 px | 400 |
| Onglets | 10 px | 500 |

## Composants

- **Bandes 70s** : 4 bandes de 4 px en haut de chaque écran, seul élément décoratif.
- **Porte-clés** : forme arrondie à gauche (rayon 19 px), carrée à droite (6 px), avec un trou rond. Sert pour le numéro de profil et la carte de grade.
- **Photo en attente** : fond `photo` + trame de points de 6 px, étiquette « Photos nettes après intérêt mutuel ».
- **Listes groupées** : fond `surface`, rayon 12–14 px, séparateurs inset de 16 px.
- **Boutons** : hauteur 50 px, rayon 12 px. Passer = icône seule sur `segment` ; Clin d'œil = `secondary` ; Curieux de… = `accent`.
- **Sélecteur segmenté** : fond `segment`, rayon 9 px, segment actif `segment-on`.
- **Interrupteur** : 51 × 31 px, `toggle-on` quand activé.
- **Barre d'onglets** : Découvrir, Soirées, Messages, Profil. Icône pleine + `accent` pour l'onglet actif, contour + `nav-muted` sinon.
- **Badge vérifié** : cercle `accent` avec coche `on-accent`.

## Espacement

Marges latérales 16 px. Espacement entre blocs 12 à 22 px. Zones tactiles d'au moins 44 px.

## À éviter

Dégradés, glassmorphism, emojis comme icônes, cartes à ombre douce partout, grilles de cartes identiques, fond crème, polices serif décoratives.

## Marque : Swapp

- **Symbole** : un S fait de deux moitiés identiques (rotation de 180°), séparées par une coupure. Moitié haute corail, moitié basse couleur du texte.
- **Sur fond sombre** : corail `#F2A38A` + clair `#EAF0F7`. **Sur fond clair** : corail profond `#D4664A` + nuit `#121A26`.
- **Logotype** : « swapp » en bas de casse géométrique dessinée (fûts droits, bols circulaires) ; le s reprend la construction du symbole.
- **Icône d'app** : symbole sur fond nuit, bandes 70s en pied (rangées de 34/1024 px).
- **Règles** : corail toujours en haut ; ne jamais refermer la coupure ; espace de protection = largeur d'une moitié ; taille mini 16 px (symbole), 80 px (horizontal).
- Fichiers : dossier `swapp-logo-kit` (SVG maîtres, icônes iOS, favicon et icônes web, planche de présentation).

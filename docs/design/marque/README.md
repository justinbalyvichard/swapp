# Swapp — pack de marque

Tout ce qu'il faut pour utiliser la marque Swapp dans l'appli iOS (Expo), la PWA (Next.js), le site vitrine et les documents.
Ouvrez `charte.html` dans un navigateur pour voir la charte complète.

## L'idée en une phrase

Le S est fait de deux moitiés identiques : on en tourne une d'un demi-tour, on obtient l'autre. C'est l'échange, dessiné dans l'initiale. Moitié haute corail, moitié basse couleur du texte.

## Contenu du pack

| Dossier | Contenu | Quand l'utiliser |
|---|---|---|
| `charte.html` | Charte de marque (logo, couleurs, icône, règles) | Référence visuelle, à partager |
| `DESIGN.md` | Direction Nuit et corail : tokens, typo, composants, section Marque | Avant de coder un écran |
| `logo/svg/` | Fichiers maîtres en couleur | Toujours partir de ces fichiers |
| `logo/png/` | Exports 1200 px (et symbole en 512 px) | Docs, slides, réseaux sociaux |
| `logo/une-couleur/` | Noir, blanc, nuit, corail profond | Impression une couleur, gravure, tampon |
| `app-ios/` | Icône d'app 1024 px et toutes les tailles iOS, icône de lancement | Expo / Xcode |
| `web/` | Favicon (ICO, SVG, PNG), icônes PWA, manifeste, extrait `<head>` | Next.js, site vitrine |
| `tokens/` | Couleurs en CSS, TypeScript et Tailwind | Code de l'appli et du site |
| `presentation/` | Planche de présentation et mises en situation | Montrer la marque |
| `source/` | Script qui régénère tous les SVG, favicon et icône masquable | Modifier la géométrie |

### Les fichiers du logo

| Fichier | Fond | Couleurs |
|---|---|---|
| `swapp-symbol.svg` | Clair | Corail profond `#D4664A` + nuit `#121A26` |
| `swapp-symbol-reversed.svg` | Sombre | Corail `#F2A38A` + clair `#EAF0F7` |
| `swapp-horizontal.svg` / `-reversed` | Clair / sombre | Symbole + « swapp » côte à côte |
| `swapp-stacked.svg` / `-reversed` | Clair / sombre | Symbole au-dessus du nom, formats carrés |
| `swapp-wordmark.svg` / `-reversed` | Clair / sombre | Le nom seul |

## Couleurs

| Nom | Hex | Rôle |
|---|---|---|
| Nuit | `#121A26` | Fond de l'appli, texte et logo sur fond clair |
| Surface | `#1C2635` | Cartes, listes groupées |
| Clair | `#EAF0F7` | Texte, moitié basse du S sur fond sombre |
| Corail | `#F2A38A` | Accent sur fond sombre, moitié haute du S |
| Corail profond | `#D4664A` | Accent sur fond clair (le corail normal est trop pâle sur du blanc) |
| Bandes 70s | `#2B4A6E` `#4D6F95` `#E08A6E` `#F2C2A8` | Haut des écrans, pied de l'icône et de l'écran de lancement, toujours dans cet ordre |

Le reste des tokens (segment, lignes, texte secondaire…) est dans `DESIGN.md` et `tokens/`.

## Intégration

### Appli iOS (Expo)

1. Copiez `app-ios/AppIcon-1024.png` et `app-ios/splash-icon.png` dans `assets/`.
2. Dans `app.json` :

```json
{
  "expo": {
    "name": "Swapp",
    "icon": "./assets/AppIcon-1024.png",
    "userInterfaceStyle": "dark",
    "backgroundColor": "#121A26",
    "plugins": [
      ["expo-splash-screen", {
        "image": "./assets/splash-icon.png",
        "imageWidth": 132,
        "backgroundColor": "#121A26"
      }]
    ]
  }
}
```

L'icône 1024 px n'a ni transparence ni coins arrondis : iOS les arrondit lui-même. Les autres tailles de `app-ios/` servent seulement pour un projet Xcode sans Expo.

### PWA et site (Next.js)

1. Copiez tout le dossier `web/` dans `public/`.
2. Avec l'App Router, ajoutez dans `app/layout.tsx` :

```ts
export const metadata = {
  title: 'Swapp',
  manifest: '/site.webmanifest',
  icons: {
    icon: [
      { url: '/favicon.ico', sizes: '48x48' },
      { url: '/favicon.svg', type: 'image/svg+xml' },
    ],
    apple: '/apple-touch-icon.png',
  },
};
export const viewport = { themeColor: '#121A26' };
```

Sans App Router, collez `web/head-snippet.html` dans le `<head>`.

Le favicon est le S sur une tuile nuit arrondie : il reste visible sur un onglet clair comme sur un onglet sombre, et lisible à 16 px. L'icône masquable (`maskable-512.png`) garde le S dans la zone de sécurité d'Android.

### Couleurs dans le code

- CSS : importez `tokens/tokens.css`, puis `background: var(--swapp-nuit)`.
- React Native : `import { colors } from './tokens'`, puis `colors.corail`.
- Tailwind : fusionnez `tokens/tailwind.colors.js` dans `theme.extend.colors`, puis `bg-swapp-nuit text-swapp-corail`.

### Le logo dans un écran

Collez directement le contenu du SVG dans un composant (Next.js : SVG inline ; React Native : `react-native-svg`). Exemple d'utilisation : en-tête de l'écran Bienvenue, 44 px de haut, version `-reversed`.

## Règles d'usage

- **Le corail est toujours en haut.** La moitié basse prend la couleur du texte : clair sur fond sombre, nuit sur fond clair.
- **Ne jamais refermer la coupure** du S, c'est elle qui porte l'idée.
- **Espace de protection** : au moins la largeur d'une moitié du S autour du logo.
- **Tailles minimales** : 16 px pour le symbole seul, 80 px de large pour la version horizontale.
- **Fonds autorisés** : nuit, surface, blanc, gris très clair. Sur une photo, poser d'abord un aplat nuit.
- **À ne pas faire** : inverser les couleurs des moitiés, déformer, ajouter ombre, contour ou dégradé, changer de couleurs.

## Modifier le logo

`source/build.py` génère tous les SVG à partir de la géométrie (deux arcs de rayon 59 et 25, coupure à 100°, rotation de 180°). Lancez `python3 build.py` dans un dossier vide, puis réexportez les PNG (`rsvg-convert -w 1024 fichier.svg -o fichier.png`).

## À faire avant le lancement

- [ ] Vérifier la marque « Swapp » à l'INPI et à l'EUIPO (classes 9, 42, 45).
- [ ] Vérifier la disponibilité de swapp.fr, swapp.com et des comptes réseaux sociaux.
- [ ] Convertir les traits du mot « swapp » en formes pleines (Figma : Outline stroke ; Illustrator : Vectoriser le contour) avant tout envoi à un imprimeur.

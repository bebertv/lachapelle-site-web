# 🏛️ Église Saint-Pierre de Lachapelle

Site web officiel de l'église Saint-Pierre de Lachapelle (Tarn-et-Garonne), monument historique classé et joyau baroque du XVIIIe siècle.

[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue?style=flat-square)](https://bebertv.github.io/lachapelle-site-web)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

## ✨ Features

- **Design élégant** - Typographie Cormorant Garamond & Outfit
- **Responsive** - Compatible mobile, tablette, desktop
- **Contenu riche** - Histoire détaillée sourcée académiquement
- **Multilingue** - Sélecteur de langue FR/EN/NL/DE/ZH
- **Gallery interactive** - Lightbox pour les images du bulletin
- **Performant** - CSS moderne avec variables et animations fluides

## 📚 Sources Académiques Intégrées

Ce site s'appuie sur des recherches historiques rigoureuses :

### 📖 Bulletin de la Société archéologique de Tarn-et-Garonne (1993)
- **Agnès Clouzet-Llorens** - *"La paroisse et l'église de Lachapelle au XVIIIe siècle"* (t. 118, pp. 17-32)
- **Jean-Claude Fabre** - *"Une querelle religieuse à Lachapelle au XIXe siècle"* (t. 118, pp. 3-16)

### 🎨 Contenu Historique
- Décor baroque par Bertrand Maraignon (1776)
- Histoire des frères Goulard, mécènes
- Querelle religieuse de l'abbé Bruitte (1840s)
- Chronologie complète du XIe siècle à nos jours

## 🚀 Déploiement

### GitHub Pages (Recommandé)

1. Allez dans **Settings** → **Pages**
2. **Branch** : `master`
3. **Folder** : `/` (root)
4. Le site sera disponible sur : `https://bebertv.github.io/lachapelle-site-web`

### Serveur Privé

```bash
# Clone le projet
git clone https://github.com/bebertv/lachapelle-site-web.git

# Serve avec Python (localhost:8000)
cd lachapelle-site-web
python -m http.server 8000
```

## 🛠️ Structure du Projet

```
lachapelle-site-web/
├── index.html          # Page principale
├── images/             # Médiathèque complète
│   ├── bulletin/       # Figures académiques
│   └── *.jpg          # Photos HD de l'église
├── README.md           # Cette documentation
└── .git/              # Versioning Git
```

## 🎨 Design System

### Couleurs
```css
--color-primary: #8b6914    /* Or baroque */
--color-accent: #c9a227     /* Doré */
--color-bg: #faf8f5         /* Fond ivoire */
--color-text: #2c2416       /* Brun profond */
```

### Typographie
- **Titres** : Cormorant Garamond (serif)
- **Corps** : Outfit (sans-serif)
- **Google Fonts** : Chargement optimisé

## 📱 Sections du Site

1. **Hero** - Introduction immersive
2. **Histoire** - Chronologie millénaire  
3. **Décor Baroque** - Trésor artistique
4. **Visites** - Carousel des highlights
5. **Querelle Religieuse** - Histoire du XIXe
6. **Horaires** - Informations pratiques
7. **Contact** - Coordination visite

## 🌐 Internationalisation

Le sélecteur de langue (FR/EN/NL/DE/ZH) est implémenté et prêt pour les traductions :

```javascript
// Dans index.html - Ligne 1540
const languageSelect = document.getElementById('language-select');
languageSelect.addEventListener('change', function() {
    // Logique de traduction à implémenter
});
```

## 🔧 Développement

### Prérequis
- Navigateur moderne (CSS Variables, ES6+)
- Git pour la versioning

### Contributions
Les contributions sont bienvenues ! Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines.

## 📜 License

MIT License - Voir [LICENSE](LICENSE) pour les détails.

## 🙏 Remerciements

- **Société archéologique de Tarn-et-Garonne** pour l'autorisation de reproduction
- **Agnès Clouzet-Llorens** pour ses recherches fondamentales
- **Communauté de Lachapelle** pour la préservation de ce patrimoine

## 📞 Contact

**Association des Amis de l'Église de Lachapelle**  
📍 82120 Lachapelle, Tarn-et-Garonne  
📞 06 12 49 23 30  
📧 contact@lachapelle82.fr  
🌐 [lachapelle82.fr](https://www.lachapelle82.fr)

---

*« Un joyau baroque du XVIIIe siècle au cœur de la Lomagne, la Toscane française »*
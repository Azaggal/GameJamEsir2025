# Swing Without Falling

## Aperçu
Swing Without Falling est un jeu de plateforme 2D développé en Python avec la bibliothèque Pygame. Le joueur navigue à travers des niveaux verticaux difficiles en grimpant, se balançant et évitant les obstacles qui tombent. Le jeu présente une mécanique d'escalade unique où les joueurs doivent chronométrer leurs mouvements correctement et gérer leur force de préhension pour progresser.

## Fonctionnalités du Jeu
- **Mécaniques d'Escalade Uniques**: Les joueurs peuvent s'agripper à des prises d'escalade et se balancer pour prendre de l'élan pour les sauts
- **Animation Dynamique des Personnages**: Animations fluides pour l'escalade et les sauts
- **Différents Types de Plateformes**: Différents types de prises incluant:
  - Prises d'escalade régulières
  - Petites prises (qui épuisent la force de préhension plus rapidement)
  - Accélérateurs de vitesse horizontale
  - Accélérateurs de vitesse verticale
  - Catapultes pour des sauts spéciaux
- **Obstacles en Chute**: Esquivez les personnages qui tombent et qui peuvent étourdir le joueur
- **Éditeur de Niveaux**: Système intégré de création et d'édition de cartes
- **Système de Sauvegarde/Chargement**: Sauvegardez votre progression ou vos cartes personnalisées

## Contrôles
- **Gauche/Droite**: Contrôle la direction du balancement en étant accroché
- **Saut**: Se libérer de la prise pour sauter
- **Gauche/Droite (en l'air)**: Ajuster le mouvement dans les airs

## Détails Techniques
Le jeu est structuré en plusieurs composants clés:

### Systèmes Principaux
- **Moteur de Jeu**: Gère les états du jeu, le rendu et la boucle principale
- **Système de Carte**: Gère le chargement, la sauvegarde et le rendu des cartes à base de tuiles
- **Physique du Joueur**: Physique personnalisée pour l'escalade, le balancement et les sauts

### Entités
- **Joueur**: Le personnage principal avec des capacités d'escalade
- **FallingCharacter**: Obstacles qui tombent d'en haut
- **Plateformes**: Différents types de prises d'escalade avec des propriétés uniques

### Fonctionnalités Techniques
- **Détection de Collision**: Collision au pixel près utilisant des masques
- **Système d'Animation**: Animation basée sur des images pour les personnages
- **Rendu de Carte à Base de Tuiles**: Rendu efficace des tuiles visibles uniquement
- **Format de Carte CSV/JSON**: Format de carte facile à éditer pour la création de niveau

## Prérequis
- Python 3.x
- Bibliothèque Pygame
- Dépendances supplémentaires (voir Installation)

## Installation
1. Clonez le dépôt
2. Installez les dépendances requises:
   ```
   pip install pygame
   ```
3. Lancez le jeu:
   ```
   python game.py
   ```

## Structure du Projet
- **assets/**: Contient tous les assets du jeu (images, sons, cartes)
  - **entities/**: Sprites des personnages et entités
  - **maps/**: Données des niveaux
  - **others/**: Éléments d'interface et images diverses
  - **tiles/**: Images des tuiles
  - **audio/**: Effets sonores et musique
- **scripts/**: Modules de code du jeu
  - **file.py**: Gère les opérations de fichiers
  - **image.py**: Chargement et traitement d'images
  - **tile.py**: Gestion des tuiles
  - **platforme.py**: Types de plateformes
  - **son.py**: Gestion audio
- **settings.py**: Configuration du jeu
- **game_config.py**: Paramètres de gameplay
- **game.py**: Point d'entrée principal du jeu
- **game_state.py**: Gestionnaire de logique de jeu
- **menu_state.py**: Système de menu

## Crédits
- Jeu développé dans le cadre d'une Game Jam (basé sur le logo affiché au démarrage)
- Musique et effets sonores inclus dans les assets

## Licence
[Vos informations de licence ici]
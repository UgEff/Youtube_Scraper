# YouTube Video Downloader and Processor

## Description

Ce projet est un script Python qui télécharge des vidéos à partir d'une chaîne YouTube, extrait l'audio en format MP3, télécharge et redimensionne les images de couverture, et crée des fichiers de métadonnées pour chaque vidéo. Le script organise les fichiers téléchargés dans des répertoires spécifiques pour faciliter leur gestion.

## Fonctionnalités

- Téléchargement des vidéos d'une chaîne YouTube.
- Extraction de l'audio au format MP3.
- Téléchargement et redimensionnement des images de couverture.
- Création d'un fichier `metadata.txt` pour chaque vidéo.
- Suppression automatique des fichiers temporaires après le traitement.

## Structure du projet

```
youtube_scrap/
├── downloads/              # Répertoire de sortie contenant les fichiers téléchargés
│   ├── NomDeLaChaine/      # Dossier principal par chaîne
│   │   ├── Prod_1/         # Dossier par vidéo
│   │   │   ├── audio/      # Dossier contenant l'audio MP3
│   │   │   ├── cover/      # Dossier contenant l'image de couverture
│   │   │   └── metadata.txt
│   │   ├── Prod_2/
│   │   └── ...
├── fonction.py             # Script Python contenant les fonctions utilitaires
├── main.py                 # Script principal pour lancer le traitement
├── picture_resize.py       # Script pour redimensionner les images
└── video_url.xlsx          # Fichier Excel contenant les URLs des chaînes YouTube
```

## Installation

1. Clonez le dépôt ou téléchargez le projet.
2. Assurez-vous d'avoir Python installé (version 3.6 ou supérieure).
3. Installez les bibliothèques nécessaires :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Remplissez le fichier `video_url.xlsx` avec les URLs des chaînes YouTube à traiter.
2. Exécutez le script principal :
   ```bash
   python main.py
   ```
3. Entrez le chemin du fichier `video_url.xlsx` lorsque le script le demande.

## Fonctionnalités des scripts

### `main.py`

- Lance le processus de téléchargement et de traitement pour chaque URL listée dans le fichier `video_url.xlsx`.

### `fonction.py`

- Contient les fonctions utilitaires pour le nettoyage des noms de fichiers, le téléchargement des vidéos, et la gestion des fichiers temporaires.

### `picture_resize.py`

- Contient la fonction de redimensionnement des images pour transformer les images de couverture en format carré.

## Avertissement

- Ce script est destiné à des fins éducatives et personnelles. Assurez-vous de respecter les conditions d'utilisation de YouTube lorsque vous téléchargez des vidéos.

## Licence

Ce projet est sous licence MIT. Vous êtes libre de le modifier et de l'utiliser, mais vous ne pouvez pas le distribuer sans mentionner l'auteur original.

## Auteur

**Idir**

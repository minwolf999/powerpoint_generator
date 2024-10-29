# Merci d'utiliser notre générateur de présentations PowerPoint ! 🎉

Ce projet est une application en Python3 permettant de créer des présentations PowerPoint via une interface graphique, développée avec `tkinter`. Elle permet d'ajouter des pages contenant du texte et des images, de sauvegarder les informations en fichier JSON pour une édition ultérieure, puis de générer le fichier PowerPoint (.ppt) à partir de ces données.

## Table des Matières
- [Fonctionnalités](#fonctionnalités)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Structure du projet](#structure-du-projet)
- [Exemples](#exemples)
- [Licence](#licence)

---

## Fonctionnalités

- **Interface graphique** : Créez et organisez vos slides facilement grâce à une interface intuitive.
- **Ajout de contenu dynamique** : Pour chaque slide, vous pouvez ajouter plusieurs blocs de texte et des images.
- **Sauvegarde et chargement des données** : Enregistre les données en JSON pour permettre une édition ultérieure.
- **Génération de PowerPoint** : Crée un fichier `.ppt` basé sur les données du fichier JSON.

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir installé les dépendances nécessaires :

- Python3
- `tkinter` (installé par défaut avec Python)
- `python-pptx` pour générer les présentations PowerPoint
- `json` (module standard de Python)

## Installation

1. Clonez ce dépôt ou téléchargez-le sous forme d'archive ZIP :
    ```bash
    git clone https://github.com/minwolf999/powerpoint_generator.git
    cd votre-projet
    ```

2. Installez les dépendances requises :
    ```bash
    pip install python-pptx
    ```

## Utilisation

1. Lancez le programme en exécutant `main.py` :
    ```bash
    python3 main.py
    ```

2. **Interface graphique** : 
   - Ajoutez des slides avec des textes et des images via l'interface `tkinter`.
   - Sauvegardez les informations en JSON pour pouvoir les modifier plus tard.

3. **Génération du PowerPoint** :
   - Une fois toutes les informations ajoutées, le programme génère un fichier `.ppt` contenant toutes les données.

## Structure du projet

    ```plaintext
    powerpoint generator/
    │
    ├── models/                 # Dossier pour les utilitaires et fonctions
    │   ├── imageClass.py       # Fichier gérant le formulaire d'ajout d'image avec tkinter dans une page
    │   ├── pageClass.py        # Fichier gérant le formulaire d'ajout d'une page avec tkinter
    │   └── textClass.py        # Fichier gérant le formulaire d'ajout d'un text avec tkinter dans une page
    |
    ├── main.py                 # Point d'entrée principal de l'application
    ├── createElem.py           # Fichier générant des éléments dans le .ppt
    ├── createPPT.py            # Fichier générant le .ppt
    |
    ├── data.json               # Fichier JSON contenant les informations rentrer dans le formulaire
    ├── powerpoint.ppt          # Le powerpoint final
    |
    └── README.md               # Documentation du projet
    ```

## Exemples

1. **Exécution de l'application**

    ```bash
    python main.py
    ```

2. **Exemples de fichiers JSON**
    Un exemple de fichier data.json pourrait ressembler à ceci pour un powerpoint ne contenant qu'une page qui elle même ne contient qu'une image et un texte :

    ```json
    {
        "Diap0": {
            "Background": {
                "Start": "d97ed9",
                "End": "56d9d9"
            },
            "Text0": {
                "Text": "text",
                "Left": 0.0,
                "Top": 2.3,
                "Width": 50.0,
                "Height": 10.0,
                "FontColor": "d98b3c",
                "FontSize": 18,
                "FontName": "Calibri",
                "Bold": true,
                "Italic": false,
                "Underline": false,
                "Align": "center"
            },
            "Image1": {
                "Path": "an/image/path",
                "Left": 0.0,
                "Top": 60.0,
                "Width": 100.0,
                "height": null
            }
        }
    }
    ```

## Licence
    Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.


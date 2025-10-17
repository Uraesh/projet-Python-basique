# Projet Python - Formation de Base

Ce dépôt contient une série d'exercices et d'exemples créés dans le cadre d'une formation Python. Les scripts couvrent divers aspects de la programmation Python, des bases aux opérations d'analyse de données avec pandas.

## Environnement de Développement

Ce projet a été développé avec **Spyder**, un environnement de développement intégré (IDE) pour Python qui inclut de nombreuses bibliothèques scientifiques préinstallées. Aucune installation externe n'est nécessaire si vous utilisez une distribution comme Anaconda qui inclut Spyder.

## Contenu du Projet

### 1. Scripts de Base

- **list.py** - Opérations de base sur les listes et calcul de somme
- **liste-tuple-ensemble.py** - Manipulation avancée des structures de données
- **Longueur-texte.py** - Comptage de mots dans un texte
- **Stat-desc-simple.py** - Calculs statistiques de base (moyenne, médiane, écart-type, etc.)
- **statAnalyze.py** - Analyse statistique avancée avec visualisation interactive

### 2. Analyse de Données avec Pandas

- **01-lecture-fichier-panda.py** - Lecture de fichiers CSV avec pandas
- **02-Analyse-données.py** - Fonctions de base d'analyse exploratoire
- **03-Sélectionner-données.py** - Techniques de sélection de données
- **04-les-filtres.py** - Application de filtres sur les données (en cours)

## Exemple d'Exécution

### Exemple avec statAnalyze.py

```
=== Programme d'Analyse Statistique ===

Entrer des nombres séparés par des espaces (ex: 10 2.5 3) : 34577 7980 654325 6789975 6886095 5368

--- Statistiques ---
Nombre d'éléments (n) : 6
Somme : 14378320.00
Moyenne : 2396386.67
Médiane : 344451.00
Maximum : 6886095.00
Minimum : 5368.00
Écart-type (population) : 3148954.32
```

**Visualisation :**
Le programme génère automatiquement des graphiques incluant :

- Un histogramme avec moyenne et médiane
- Une boîte à moustaches (box plot)
- Un graphique d'évolution des valeurs
- Un diagramme en barres des valeurs triées

![1760705173894][def]

## Fonctionnalités à Venir

- [ ] Amélioration de l'interface utilisateur
- [ ] Export des résultats en format PDF/Excel
- [ ] Tests unitaires
- [ ] Documentation avancée des fonctions

## Notes

- Les scripts sont commentés en français pour faciliter l'apprentissage
- Les données d'exemple sont fournies dans le fichier `MOCK_DATA.csv`
- Ce projet est en cours de développement dans le cadre d'une formation

## Historique des Mises à Jour

### Octobre 2025

- Création du dépôt et premiers scripts
- Implémentation des fonctionnalités de base d'analyse statistique
- Ajout des visualisations avec matplotlib
- Documentation initiale du projet

[def]: image/README/1760705173894.png

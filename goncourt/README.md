# Prix Goncourt 2026

Projet réalisé dans le cadre d'une évaluation Python.

L'application permet de gérer les différentes sélections du Prix Goncourt 2026 et les votes de la sélection finale.

## Fonctionnalités

L'application permet :

- de consulter les livres des différentes sélections ;
- d'afficher les informations détaillées des livres, auteurs, éditeurs et personnages principaux ;
- au président du jury, de renseigner les livres des deuxième et troisième sélections ;
- au président du jury, de saisir le nombre de votes obtenus par les livres finalistes ;
- d'afficher le livre gagnant en fonction des votes enregistrés.

## Architecture

Le projet utilise une architecture multicouche :

- `models` : classes représentant les entités de l'application ;
- `daos` : accès et manipulation des données en base de données ;
- `business` : logique métier de l'application ;
- `main.py` : interface console et point d'entrée de l'application ;
- `bdd` : script SQL permettant de créer et initialiser la base de données.

## Installation

### 1. Installer les dépendances

Créer et activer un environnement virtuel Python, puis installer les dépendances :

```bash
python -m pip install -r requirements.txt
```

### 2. Créer la base de données

Importer le fichier SQL présent dans :

```text
bdd/goncourt.sql
```

dans MySQL ou MariaDB.

### 3. Configurer la connexion

Créer un fichier `.env` à la racine du projet :

```text
DB_HOST=localhost
DB_USER=votre_utilisateur
DB_PASSWORD=votre_mot_de_passe
DB_NAME=votre_base_de_donnees
```

Le fichier `.env` n'est pas versionné afin de ne pas exposer les informations de connexion.

## Lancement

Lancer l'application depuis la racine du projet :

```bash
python main.py
```

## Vérification du typage

Le projet utilise `mypy` pour vérifier le typage statique :

```bash
mypy goncourt
```
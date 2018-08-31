# django-ecommerce-reporting-demo
V 0.1b - Une application de démonstration de visualisation de statistiques e-commerce à l'aide de la librairie JS plotly.js 

== Sommaire ==

1. Présentation générale
2. Prérequis
3. Installation
4. Configuration 
5. Données de démo
6. Licence et notices de copyright

## Présentation générale

Cette application est un prototype de démonstration visant à présenter un outil de visualisation de statistiques e-commerce (ou reporting).
Elle a été développée sous Python avec le Framework Django (version 2.1), sur une base de données SQL Server.
L'application utilise le framework CSS Bulma et la bibliothèque Plotly.js.

## Prérequis 

L'installation nécessite d'avoir Python version >= 3.5 installé sur son système.
Idéalement, vous aurez déjà configuré un environnement Python isolé (cf virtualenv).
Aucun autre prérequis n'est nécessaire.

## Installation

### Installation de Django

L'application a été développée sous Django 2.1 mais n'importe quelle version >= 2.0 pourra convenir.
Pour installer la dernière version de Django, placez-vous dans votre répertoire de travail à partir d'un terminal et exécutez la commande :

```sh
pip install Django
```

Par ailleurs, Django supporte nativement l'interconnexion avec plusieurs Systèmes de Gestion de Base de Données répandus mais ce n'est pas le cas avec SQL Server. Pour utiliser une base de données SQL server, il est nécessaire d'installer la librairie django-pyodbc-azure :

```sh
pip install django-pyodbc-azure
```
### Installation de l'application

Pour installer l'application, téléchargez l'archive .zip sur le repository actuel et décompressez son contenu dans le répertoire de travail que vous comptez utiliser.
Une installation en ligne de commande sera rajoutée une fois le projet sortie de phase bêta.

## Configuration

### Interconnexion à la base de données

Django repose sur un ORM faisant abstraction du système de base de données utilisé en amont.
Vous pouvez ainsi configurer l'application pour fonctionner avec votre propre système de bases de données.

Pour cela, il vous suffit de modifier le fichier reporting_demo/settings.py, section DATABASES.
Pour tout renseignement complémentaire, consultez [ce lien](https://docs.djangoproject.com/fr/2.1/topics/install/#database-installation)
Les informations présaisies sont basées sur une utilisation de SQL Server.

### Migrations d'initialisations

Afin de créer les structures de données de l'application, il est nécessaire d'effectuer les migrations qui adapteront le modèle de données utilisées. Cette opération se fait en deux étapes :

1. Saisissez la commande ci-dessous afin de préparer les données de migration.

```sh
python manage.py makemigrations reporting
```
2. Saisissez la commande ci-dessous afin de la mener à bien.

```sh
python manage.py makemigrations reporting
```

### Compte administrateur

Django propose une interface d'administration par défaut pour les applications déployées sous ce framework.
Vous avez la possibilité de créer un compte d'administrateur qui vous permettra d'y avoir accès.

En ligne de commande, saisissez la commande :

```sh
python manage.py createsuperuser
```

## Données de démo

Afin de fonctionner correctement, l'application a besoin de données sur lesquelles travailler.
Les modèles utilisés dans l'application sont les suivants :
* User : clients de la base site e-commerce
* Product : produits de la base e-commerce
* Category : catégories de produits 
* Order : commandes de la base e-commerce
* OrderStatus : status possibles pour une commande
* Shipping : modes d'expédition proposés
* OrderCart : paniers de commande (détaillant les produits associés à une commande)

Les données des modèles User, Product, Category, Shipping et OrderStatus peuvent être créés manuellement par le biais de l'interface d'administration de l'application ou importés directement par le biais des fichiers csv à la racine (encodage UTF-8, délimitateurs double quotes ", séparateurs point-virgule ;).

Un script permet de générer ensuite les données des modèles Order et OrderCart.
Pour générer ces données, lancez le shell de l'interpréteur Django par le biais de la commande python manage.py shell.

Dans la nouvelle interface, saisissez les commandes suivantes :

```sh
import setupdata
setupdata.generate_database_step1(nb_comm) 
setupdata.generate_database_step2() 
```
Où nb_comm est le nombre de commandes que vous souhaitez générer en base. L'application a été testée avec nb_comm=500.
Par souci de commodité, les commandes générées ne disposent que d'un nombre limité de produits, sont toutes au statut Expédié et ont été passées entre Avril et Août 2018.

## Licence et notices de copyright 

Cette application est Copyright 2018 Florent Roux. Le code est publié sous [licence MIT](https://github.com/FloRoux/django-ecommerce-reporting-demo/blob/master/LICENSE).

Le framework CSS [bulma](https://github.com/jgthms/bulma/) est Copyright (c) 2018 Jeremy Thomas.
La librairie [Plotly.js](https://github.com/plotly/plotly.js/) est Copyright (c) 2018 Plotly, Inc.




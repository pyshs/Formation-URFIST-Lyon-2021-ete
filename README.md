## Préparer la séance

### Rapide panorama

Python est un langage interprété qui nécessite un environnement. 

Il existe plusieurs manières de l'utiliser :
- Sur votre ordinateur, avec Anaconda (ci-dessous)
- Sur le Cloud, avec différentes solutions, par exemple Google colab https://colab.research.google.com/

Le Cloud est une solution souple qui évite l'installation mais rend plus difficile l'importation de données.


### Installation d'Anaconda

Anaconda est un environnement qui fournit l'ensemble des éléments nécessaires pour exécuter du code python. Il permet de construire des environnements (une version du langage et de librairies spécifiques) et de travailler au sein de ces environnements permettant d'en avoir plusieurs (par exemple, pour tester des versions différentes de librairies, etc.)

- Télécharger Anaconda pour votre OS : https://www.anaconda.com/distribution/
- Installer (suivant que vous soyez sous Windows, Linux ou Mac, la procédure va changer)
- Lancer Anaconda pour créer un environnement de travail
  - Sur windows : Aller dans environnements > Create > donner un nom (ex. p39) et une version de python 3.9 (__Attention bien installer la version 3.7 ou plus de Python __)
  - Sur linux/mac : Ouvrir un terminal, puis créer un environnement en tappant la commande : conda create --name p39 python=3.9 (pour toute information sur les commandes conda : https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- Lancer python (sur windows en lançant Anaconda ; sous linux/mac en tapant la commande source activate p37 dans un terminal)
- lancez un terminal (vous pouvez le faire sous le logiciel Anaconda) et vérifiez que ipython est bien installé en tapant ipython de manière similaire, lancez Jupyter notebook en tapant jupyter notebook


Autres logiciels

Vous pouvez installer Sublime text : https://www.sublimetext.com/ (pour visualiser des documents textes)

# THE BIG FARMER
We are the biggest farmer's you never seen !

## I - Mise en place des tests -

### 1. Intaller pytest sur votre machine

#### a. Travailler sur l'environnement virtuel :
ATTENTION ! Veillez à bien activer l'envrionnement virtuel (venv)

    * Windows : `venv\Scripts\activate.bat`
    * Unix/MacOS : `source venv/bin/activate`

#### b. Installation de pytest :
```
pip install -u pytest
```

#### c. Tests avec pytest :
Se rendre dans le répertoire sur lequel effectuer les tests avec le terminal et éxecuter la ligne suivante
```
pytest
```

## II - Mesurer la couverture de code -

### 1. Intaller pytest + plugin coverage sur votre machine

#### a. Travailler sur l'environnement virtuel :
ATTENTION ! Veillez à bien activer l'envrionnement virtuel (venv)

    * Windows : `venv\Scripts\Activate.ps1`
    * Unix/MacOS : `source venv/bin/activate`

#### b. Installation de pytest + plugin coverage :
```
pip install pytest-cov
```
#### c. Prise en charge des tests distribués :
Pour cela il est nécessaire d'isntaller `-xdist`
```
pip install pytest -xdist
```

#### c. Tests avec pytest-cov :
Se rendre dans le répertoire sur lequel effectuer les tests avec le terminal et éxecuter la ligne suivante
```
pytest --cov
```
Produirait un rapport comme :

```
-------------------- couverture: ... ---------------------
Nom Stmts Miss Cover
----------------------------------------
monproj/__init__ 2 0 100%
monproj/monproj 257 13 94%
monproj/fonctionnalité4286 94 7 92%
----------------------------------------
TOTAL 353 20 94%
```

# = AIDE LANCEMENT DU JEU =

### - Connexion au serveur :
Dans un premier terminal de commande entrer la ligne suivante
```
python3 -m chronobio.game.server -p $port
```
Remplacer $port par un numéro de serveur > 1024

### - Démarrage du fichier jeu :
Dans un deuxième terminal entrer la ligne suivante
```
python3 name_game_file.py -p $port -u THE_BIG_FARMER
```
Remplacer $port par le même numéro de serveur que précédement en respectant la condition > 1024

### : Partie graphique :
### 1A - Création de l'espace virtuel WINDOWS
```
python3 -m venv venv
```
### 1B - Création de l'espace virtuel UBUNTU
```
sudo apt install python3-venv
python3 -m venv my-project-env
```
### 2A - Activation de l'espace virtuel WINDOWS
```
venv\Scripts\Activate.ps1
```
### 2B - Activation de l'espace virtuel UBUNTU
```
source my-project-env/bin/activate
$ source my-project-env/bin/activate (my-project-env) $
```
### 3 - Démarrer le jeu - graphique
```
python -m chronobio.viewer -p $port
```
Remplacer $port par le même numéro de serveur que précédement en respectant la condition > 1024

/!\ Il faut garder les terminaux ouverts /!\

# = PRE-COMMIT =

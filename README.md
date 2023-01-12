# The-Big-Farmer
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

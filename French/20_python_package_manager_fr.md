<div align="center">
  <h1> 30 Jours de Python : Jour 20 - PIP </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Auteur :
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Deuxième édition : juillet 2021</small>
</sub>
</div>

[<< Jour 19](./19_file_handling_fr.md) | [Jour 21 >>](./21_classes_and_objects_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 20](#-jour-20)
  - [Python PIP - Gestionnaire de paquets Python](#python-pip---gestionnaire-de-paquets-python)
    - [Qu'est-ce que PIP ?](#quest-ce-que-pip-)
    - [Installer PIP](#installer-pip)
    - [Installer des paquets avec pip](#installer-des-paquets-avec-pip)
    - [Désinstaller des paquets](#désinstaller-des-paquets)
    - [Liste des paquets](#liste-des-paquets)
    - [Afficher un paquet](#afficher-un-paquet)
    - [PIP Freeze](#pip-freeze)
    - [Lecture depuis une URL](#lecture-depuis-une-url)
    - [Créer un paquet](#créer-un-paquet)
    - [Plus d'informations sur les paquets](#plus-dinformations-sur-les-paquets)
  - [Exercices : Jour 20](#exercices-jour-20)

# 📘 Jour 20

## Python PIP - Gestionnaire de paquets Python

### Qu'est-ce que PIP ?

PIP signifie Preferred Installer Program (Programme d'installation préféré). Nous utilisons _pip_ pour installer différents paquets Python.
Un paquet est un module Python qui peut contenir un ou plusieurs modules ou d'autres paquets. Un module ou des modules que nous pouvons installer dans notre application est un paquet.
En programmation, nous n'avons pas à écrire chaque programme utilitaire, nous installons plutôt des paquets et les importons dans nos applications.

### Installer PIP

Si vous n'avez pas installé pip, installons-le maintenant. Allez dans votre terminal ou invite de commande et copiez-collez ceci :

```sh
asabeneh@Asabeneh:~$ pip install pip
```

Vérifiez si pip est installé en tapant :

```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

Comme vous pouvez le voir, j'utilise pip version 21.1.3. Si vous voyez un numéro légèrement inférieur ou supérieur, cela signifie que pip est installé.

Examinons quelques-uns des paquets utilisés dans la communauté Python à différentes fins. Juste pour vous informer qu'il existe de nombreux paquets disponibles pour différentes applications.

### Installer des paquets avec pip

Essayons d'installer _numpy_, appelé numeric python. C'est l'un des paquets les plus populaires dans la communauté du machine learning et de la data science.

- NumPy est le paquet fondamental pour le calcul scientifique avec Python. Il contient entre autres :
  - un puissant objet tableau N-dimensionnel
  - des fonctions sophistiquées de diffusion (broadcasting)
  - des outils pour intégrer du code C/C++ et Fortran
  - des fonctionnalités utiles d'algèbre linéaire, de transformée de Fourier et de nombres aléatoires

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

Commençons à utiliser numpy. Ouvrez votre interpréteur Python interactif, tapez python puis importez numpy comme suit :

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>
```

Pandas est une bibliothèque open source sous licence BSD qui fournit des structures de données haute performance et faciles à utiliser ainsi que des outils d'analyse de données pour le langage de programmation Python. Installons le grand frère de numpy, _pandas_ :

```sh
asabeneh@Asabeneh:~$ pip install pandas
```

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

Cette section ne porte pas sur numpy ni pandas, ici nous essayons d'apprendre comment installer des paquets et comment les importer. Si besoin, nous parlerons de différents paquets dans d'autres sections.

Importons un module de navigateur web, qui peut nous aider à ouvrir n'importe quel site. Nous n'avons pas besoin d'installer ce module, il est déjà installé par défaut avec Python 3. Par exemple, si vous aimez ouvrir un certain nombre de sites web à n'importe quel moment ou si vous aimez planifier quelque chose, ce module _webbrowser_ peut être utilisé.

```py
import webbrowser # module navigateur web pour ouvrir des sites

# liste d'urls : python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# ouvre la liste de sites ci-dessus dans un onglet différent
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### Désinstaller des paquets

Si vous ne souhaitez pas conserver les paquets installés, vous pouvez les supprimer en utilisant la commande suivante.

```sh
pip uninstall nom_paquet
```

### Liste des paquets

Pour voir les paquets installés sur notre machine, nous pouvons utiliser pip suivi de list.

```sh
pip list
```

### Afficher un paquet

Pour afficher des informations sur un paquet :

```sh
pip show nom_paquet
```

```sh
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

Si nous voulons encore plus de détails, ajoutez --verbose :

```sh
asabeneh@Asabeneh:~$ pip show --verbose pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

Génère une liste des paquets Python installés avec leur version, et la sortie convient pour l'utiliser dans un fichier requirements. Un fichier requirements.txt est un fichier qui devrait contenir tous les paquets Python installés dans un projet Python.

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

La commande pip freeze nous a donné les paquets utilisés, installés et leur version. Nous l'utilisons avec le fichier requirements.txt pour le déploiement.

### Lecture depuis une URL

Maintenant, vous êtes familier avec la façon de lire ou d'écrire sur un fichier situé sur votre machine locale. Parfois, nous aimerions lire depuis un site web en utilisant une URL ou depuis une API.
API signifie Application Program Interface (Interface de programmation d'application). C'est un moyen d'échanger des données structurées entre serveurs, principalement sous forme de données json. Pour ouvrir une connexion réseau, nous avons besoin d'un paquet appelé _requests_ - il permet d'ouvrir une connexion réseau et d'implémenter les opérations CRUD (create, read, update, delete). Dans cette section, nous ne couvrirons que la partie lecture (ou "get") du CRUD.

Installons _requests_ :

```py
asabeneh@Asabeneh:~$ pip install requests
```

Nous verrons les méthodes _get_, _status_code_, _headers_, _text_ et _json_ dans le module _requests_ :
  - _get()_ : pour ouvrir une connexion réseau et récupérer des données depuis une URL - retourne un objet réponse
  - _status_code_ : après avoir récupéré les données, nous pouvons vérifier le statut de l'opération (succès, erreur, etc.)
  - _headers_ : pour vérifier les types d'en-têtes
  - _text_ : pour extraire le texte de l'objet réponse récupéré
  - _json_ : pour extraire des données json
Lisons un fichier txt depuis ce site : https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # importation du module requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # texte depuis un site web

response = requests.get(url) # ouverture d'une connexion réseau et récupération de données
print(response)
print(response.status_code) # code de statut, succès : 200
print(response.headers)     # informations d'en-tête
print(response.text) # donne tout le texte de la page
```

```sh
<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

- Lisons depuis une API. API signifie Application Program Interface. C'est un moyen d'échanger des données structurées entre serveurs, principalement sous forme de données json. Un exemple d'API : https://restcountries.eu/rest/v2/all. Lisons cette API en utilisant le module _requests_.

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # api des pays
response = requests.get(url)  # ouverture d'une connexion réseau et récupération de données
print(response) # objet réponse
print(response.status_code)  # code de statut, succès : 200
countries = response.json()
print(countries[:1])  # nous n'avons pris que le premier pays, retirez le slicing pour voir tous les pays
```

```sh
<Response [200]>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
```

Nous utilisons la méthode _json()_ de l'objet réponse, si nous récupérons des données JSON. Pour txt, html, xml et autres formats de fichiers, nous pouvons utiliser _text_.

### Créer un paquet

Nous organisons un grand nombre de fichiers dans différents dossiers et sous-dossiers selon certains critères, afin de pouvoir les trouver et les gérer facilement. Comme vous le savez, un module peut contenir plusieurs objets, tels que des classes, des fonctions, etc. Un paquet peut contenir un ou plusieurs modules pertinents. Un paquet est en fait un dossier contenant un ou plusieurs fichiers de modules. Créons un paquet nommé mypackage, en suivant les étapes suivantes :

Créez un nouveau dossier nommé mypackage dans le dossier 30DaysOfPython
Créez un fichier **__init__**.py vide dans le dossier mypackage.
Créez les modules arithmetic.py et greet.py avec le code suivant :

```py
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
```

```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, bienvenue au défi 30DaysOfPython !'
```

La structure de dossiers de votre paquet devrait ressembler à ceci :

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

Ouvrons maintenant l'interpréteur Python interactif et essayons le paquet que nous avons créé :

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Asabeneh', 'Yetayeh')
'Asabeneh Yetayeh, bienvenue au défi 30DaysOfPython !'
>>>
```

Comme vous pouvez le voir, notre paquet fonctionne parfaitement. Le dossier du paquet contient un fichier spécial appelé **__init__**.py - il stocke le contenu du paquet. Si nous mettons **__init__**.py dans le dossier du paquet, Python le reconnaît comme un paquet.
Le fichier **__init__**.py expose les ressources spécifiées de ses modules pour être importées dans d'autres fichiers Python. Un fichier **__init__**.py vide rend toutes les fonctions disponibles lorsqu'un paquet est importé. Le fichier **__init__**.py est essentiel pour que le dossier soit reconnu par Python comme un paquet.

### Plus d'informations sur les paquets

- Base de données
  - SQLAlchemy ou SQLObject - Accès orienté objet à plusieurs systèmes de bases de données différents
    - _pip install SQLAlchemy_
- Développement Web
  - Django - Framework web haut niveau.
    - _pip install django_
  - Flask - Micro-framework Python basé sur Werkzeug, Jinja 2. (Sous licence BSD)
    - _pip install flask_
- Analyse HTML
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Analyseur HTML/XML conçu pour des projets à évolution rapide comme le scraping, accepte les balises incorrectes.
    - _pip install beautifulsoup4_
  - PyQuery - implémente jQuery en Python ; plus rapide que BeautifulSoup, apparemment.

- Traitement XML
  - ElementTree - Le type Element est un conteneur simple mais flexible, conçu pour stocker des structures de données hiérarchiques, comme des ensembles d'informations XML simplifiés, en mémoire. --Note : Python 2.5 et supérieur inclut ElementTree dans la bibliothèque standard.
- GUI
  - PyQt - Liaisons pour le framework Qt multiplateforme.
  - TkInter - La boîte à outils d'interface utilisateur Python traditionnelle.
- Analyse de données, Data Science et Machine Learning
  - Numpy : Numpy (numeric python) est connu comme l'une des bibliothèques de machine learning les plus populaires en Python.
  - Pandas : est une bibliothèque d'analyse de données, de data science et de machine learning en Python qui fournit des structures de données haut niveau et une grande variété d'outils d'analyse.
  - SciPy : SciPy est une bibliothèque de machine learning pour les développeurs d'applications et les ingénieurs. La bibliothèque SciPy contient des modules pour l'optimisation, l'algèbre linéaire, l'intégration, le traitement d'images et les statistiques.
  - Scikit-Learn : est basé sur NumPy et SciPy. Il est considéré comme l'une des meilleures bibliothèques pour travailler avec des données complexes.
  - TensorFlow : est une bibliothèque de machine learning construite par Google.
  - Keras : est considérée comme l'une des bibliothèques de machine learning les plus cool en Python. Elle fournit un mécanisme plus facile pour exprimer les réseaux de neurones. Keras fournit également certaines des meilleures utilitaires pour compiler des modèles, traiter des ensembles de données, visualiser des graphiques et bien plus encore.
- Réseau :
  - requests : est un paquet que nous pouvons utiliser pour envoyer des requêtes à un serveur (GET, POST, DELETE, PUT)
    - _pip install requests_

🌕 Vous progressez toujours et vous êtes à 20 pas de votre chemin vers la grandeur. Maintenant, faites quelques exercices pour votre cerveau et vos muscles.

## Exercices : Jour 20

1. Lisez cette url et trouvez les 10 mots les plus fréquents. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
2. Lisez l'API des chats : cats_api = 'https://api.thecatapi.com/v1/breeds' et trouvez :
   1. le min, max, moyenne, médiane, écart type du poids des chats en unités métriques.
   2. le min, max, moyenne, médiane, écart type de l'espérance de vie des chats en années.
   3. Créez un tableau de fréquences des pays et des races de chats.
3. Lisez l'[API des pays](https://restcountries.eu/rest/v2/all) et trouvez :
   1. les 10 plus grands pays
   2. les 10 langues les plus parlées
   3. le nombre total de langues dans l'API des pays
4. UCI est l'un des endroits les plus courants pour obtenir des ensembles de données pour la data science et le machine learning. Lisez le contenu de UCL (https://archive.ics.uci.edu/ml/datasets.php). Sans bibliothèques supplémentaires, ce sera difficile, vous pouvez donc essayer avec BeautifulSoup4.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 19](./19_file_handling_fr.md) | [Jour 21 >>](./21_classes_and_objects_fr.md)

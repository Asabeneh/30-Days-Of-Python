<div align="center">
  <h1> 30 Jours de Python : Jour 19 - Gestion de fichiers </h1>
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

[<< Jour 18](./18_regular_expressions_fr.md) | [Jour 20 >>](./20_python_package_manager_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 19](#-jour-19)
  - [Gestion de fichiers](#gestion-de-fichiers)
    - [Ouverture de fichiers en lecture](#ouverture-de-fichiers-en-lecture)
    - [Ouverture de fichiers en écriture et mise à jour](#ouverture-de-fichiers-en-écriture-et-mise-à-jour)
    - [Suppression de fichiers](#suppression-de-fichiers)
  - [Types de fichiers](#types-de-fichiers)
    - [Fichier avec l'extension txt](#fichier-avec-lextension-txt)
    - [Fichier avec l'extension json](#fichier-avec-lextension-json)
    - [Convertir du JSON en dictionnaire](#convertir-du-json-en-dictionnaire)
    - [Convertir un dictionnaire en JSON](#convertir-un-dictionnaire-en-json)
    - [Sauvegarder au format JSON](#sauvegarder-au-format-json)
    - [Fichier avec l'extension csv](#fichier-avec-lextension-csv)
    - [Fichier avec l'extension xlsx](#fichier-avec-lextension-xlsx)
    - [Fichier avec l'extension xml](#fichier-avec-lextension-xml)
  - [💻 Exercices : Jour 19](#-exercices-jour-19)
    - [Exercices : Niveau 1](#exercices-niveau-1)
    - [Exercices : Niveau 2](#exercices-niveau-2)
    - [Exercices : Niveau 3](#exercices-niveau-3)

# 📘 Jour 19

## Gestion de fichiers

Jusqu'à présent, nous avons vu différents types de données Python. Nous stockons généralement nos données dans différents formats de fichiers. En plus de la gestion des fichiers, nous verrons également différents formats de fichiers (.txt, .json, .xml, .csv, .tsv, .excel) dans cette section. Commençons par nous familiariser avec la gestion des fichiers au format courant (.txt).

La gestion des fichiers est une partie importante de la programmation qui nous permet de créer, lire, mettre à jour et supprimer des fichiers. En Python, pour manipuler des données, nous utilisons la fonction intégrée _open()_.

```py
# Syntaxe
open('fichier', mode) # mode(r, a, w, x, t, b) peut être lecture, écriture, mise à jour
```

- "r" - Lecture (Read) - Valeur par défaut. Ouvre un fichier en lecture, retourne une erreur si le fichier n'existe pas
- "a" - Ajout (Append) - Ouvre un fichier pour ajout, crée le fichier s'il n'existe pas
- "w" - Écriture (Write) - Ouvre un fichier en écriture, crée le fichier s'il n'existe pas
- "x" - Création (Create) - Crée le fichier spécifié, retourne une erreur si le fichier existe
- "t" - Texte (Text) - Valeur par défaut. Mode texte
- "b" - Binaire (Binary) - Mode binaire (ex. images)

### Ouverture de fichiers en lecture

Le mode par défaut de _open_ est la lecture, donc nous n'avons pas à spécifier 'r' ou 'rt'. J'ai créé et sauvegardé un fichier nommé reading_file_example.txt dans le dossier files. Voyons comment cela se fait :

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

Comme vous pouvez le voir dans l'exemple ci-dessus, j'ai affiché le fichier ouvert et il a donné quelques informations à son sujet. Un fichier ouvert dispose de différentes méthodes de lecture : _read()_, _readline_, _readlines_. Un fichier ouvert doit être fermé avec la méthode _close()_.

- _read()_ : lit tout le texte sous forme de chaîne. Si nous voulons limiter le nombre de caractères à lire, nous pouvons le limiter en passant une valeur entière à la méthode *read(nombre)*.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# sortie
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

Au lieu d'afficher tout le texte, affichons les 10 premiers caractères du fichier texte.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# sortie
<class 'str'>
This is an
```

- _readline()_ : lit uniquement la première ligne

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# sortie
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_ : lit tout le texte ligne par ligne et retourne une liste de lignes

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# sortie
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Une autre façon d'obtenir toutes les lignes sous forme de liste est d'utiliser _splitlines()_ :

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# sortie
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

Après avoir ouvert un fichier, nous devrions le fermer. Il y a une forte tendance à oublier de les fermer. Il existe une nouvelle façon d'ouvrir les fichiers en utilisant _with_ - il ferme les fichiers tout seul. Réécrivons l'exemple précédent avec la méthode _with_ :

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# sortie
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Ouverture de fichiers en écriture et mise à jour

Pour écrire dans un fichier existant, nous devons ajouter un mode comme paramètre à la fonction _open()_ :

- "a" - ajout (append) - ajoute à la fin du fichier, si le fichier n'existe pas, il en crée un nouveau.
- "w" - écriture (write) - écrase tout contenu existant, si le fichier n'existe pas, il le crée.

Ajoutons du texte au fichier que nous lisions :

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

La méthode ci-dessous crée un nouveau fichier, si le fichier n'existe pas :

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### Suppression de fichiers

Nous avons vu dans la section précédente comment créer et supprimer un répertoire en utilisant le module _os_. Maintenant, si nous voulons supprimer un fichier, nous utilisons le module _os_.

```py
import os
os.remove('./files/example.txt')

```

Si le fichier n'existe pas, la méthode remove lèvera une erreur, il est donc bon d'utiliser une condition comme celle-ci :

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('Le fichier n\'existe pas')
```

## Types de fichiers

### Fichier avec l'extension txt

Le fichier avec l'extension _txt_ est une forme de données très courante et nous l'avons couvert dans la section précédente. Passons au fichier JSON.

### Fichier avec l'extension json

JSON signifie JavaScript Object Notation. En réalité, c'est un objet JavaScript ou un dictionnaire Python converti en chaîne de caractères.

_Exemple :_

```py
# dictionnaire
personne_dct = {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON : une chaîne représentant un dictionnaire
personne_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# nous utilisons trois guillemets et plusieurs lignes pour le rendre plus lisible
personne_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### Convertir du JSON en dictionnaire

Pour convertir du JSON en dictionnaire, nous importons d'abord le module json, puis nous utilisons la méthode _loads_.

```py
import json
# JSON
personne_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# convertissons JSON en dictionnaire
personne_dct = json.loads(personne_json)
print(type(personne_dct))
print(personne_dct)
print(personne_dct['name'])
```

```sh
# sortie
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### Convertir un dictionnaire en JSON

Pour convertir un dictionnaire en JSON, nous utilisons la méthode _dumps_ du module json.

```py
import json
# dictionnaire python
personne = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# convertissons-le en json
personne_json = json.dumps(personne, indent=4) # indent peut être 2, 4, 8. Il embellit le json
print(type(personne_json))
print(personne_json)
```

```sh
# sortie
# quand vous l'affichez, il n'a pas de guillemets, mais en réalité c'est une chaîne
# JSON n'a pas de type, c'est un type chaîne
<class 'str'>
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
```

### Sauvegarder au format JSON

Nous pouvons également sauvegarder nos données sous forme de fichier json. Sauvegardons-le en utilisant les étapes suivantes. Pour écrire un fichier json, nous utilisons la méthode json.dump(), elle peut prendre un dictionnaire, un fichier de sortie, ensure_ascii et indent.

```py
import json
# dictionnaire python
personne = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(personne, f, ensure_ascii=False, indent=4)
```

Dans le code ci-dessus, nous utilisons l'encodage et l'indentation. L'indentation rend le fichier json facile à lire.

### Fichier avec l'extension csv

CSV signifie Comma Separated Values (valeurs séparées par des virgules). CSV est un format de fichier simple utilisé pour stocker des données tabulaires, comme un tableur ou une base de données. CSV est un format de données très courant en science des données.

**Exemple :**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**Exemple :**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # nous utilisons la méthode reader pour lire le csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Noms des colonnes : {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} est un enseignant. Il vit à {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Nombre de lignes : {line_count}')
```

```sh
# sortie :
Noms des colonnes : name, country, city, skills
Nombre de lignes : 1
        Asabeneh est un enseignant. Il vit à Finland, Helsinki.
Nombre de lignes : 2
```

### Fichier avec l'extension xlsx

Pour lire des fichiers Excel, nous devons installer le paquet _xlrd_. Nous aborderons cela après avoir couvert l'installation de paquets avec pip.

```py
import xlrd
classeur_excel = xlrd.open_workbook('sample.xls')
print(classeur_excel.nsheets)
print(classeur_excel.sheet_names)
```

### Fichier avec l'extension xml

XML est un autre format de données structurées qui ressemble à HTML. En XML, les balises ne sont pas prédéfinies. La première ligne est une déclaration XML. La balise person est la racine du XML. La personne a un attribut gender.

**Exemple : XML**

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

Pour plus d'informations sur la lecture d'un fichier XML, consultez la [documentation](https://docs.python.org/2/library/xml.etree.elementtree.html).

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Balise racine :', root.tag)
print('Attribut :', root.attrib)
for child in root:
    print('champ : ', child.tag)
```

```sh
# sortie
Balise racine : person
Attribut : {'gender': 'male'}
champ : name
champ : country
champ : city
champ : skills
```

🌕 Vous faites de grands progrès. Gardez votre élan, continuez votre bon travail. Maintenant, faites quelques exercices pour votre cerveau et vos muscles.

## 💻 Exercices : Jour 19

### Exercices : Niveau 1

1. Écrivez une fonction qui compte le nombre de lignes et le nombre de mots dans un texte. Tous les fichiers sont dans le dossier data :
   1) Lisez le fichier obama_speech.txt et comptez le nombre de lignes et de mots
   2) Lisez le fichier michelle_obama_speech.txt et comptez le nombre de lignes et de mots
   3) Lisez le fichier donald_speech.txt et comptez le nombre de lignes et de mots
   4) Lisez le fichier melina_trump_speech.txt et comptez le nombre de lignes et de mots
2. Lisez le fichier de données countries_data.json dans le dossier data, créez une fonction qui trouve les dix langues les plus parlées

   ```py
   # Votre sortie devrait ressembler à ceci
   print(most_spoken_languages(filename='./data/countries_data.json', 10))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic'),
   (24, 'Spanish'),
   (9, 'Russian'),
   (9, 'Portuguese'),
   (8, 'Dutch'),
   (7, 'German'),
   (5, 'Chinese'),
   (4, 'Swahili'),
   (4, 'Serbian')]

   # Votre sortie devrait ressembler à ceci
   print(most_spoken_languages(filename='./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. Lisez le fichier de données countries_data.json dans le dossier data, créez une fonction qui crée une liste des dix pays les plus peuplés

   ```py
   # Votre sortie devrait ressembler à ceci
   print(most_populated_countries(filename='./data/countries_data.json', 10))

   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000},
   {'country': 'Indonesia', 'population': 258705000},
   {'country': 'Brazil', 'population': 206135893},
   {'country': 'Pakistan', 'population': 194125062},
   {'country': 'Nigeria', 'population': 186988000},
   {'country': 'Bangladesh', 'population': 161006790},
   {'country': 'Russian Federation', 'population': 146599183},
   {'country': 'Japan', 'population': 126960000}
   ]

   # Votre sortie devrait ressembler à ceci

   print(most_populated_countries(filename='./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

### Exercices : Niveau 2

1. Extrayez toutes les adresses e-mail entrantes sous forme de liste à partir du fichier email_exchange_big.txt.
2. Trouvez les mots les plus courants dans la langue anglaise. Appelez votre fonction find_most_common_words, elle prendra deux paramètres - une chaîne ou un fichier et un entier positif, indiquant le nombre de mots. Votre fonction retournera un tableau de tuples en ordre décroissant. Vérifiez la sortie.

```py
    # Votre sortie devrait ressembler à ceci
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Votre sortie devrait ressembler à ceci
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. Utilisez la fonction find_most_frequent_words pour trouver :
   1) Les dix mots les plus fréquents utilisés dans le discours d'[Obama](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   2) Les dix mots les plus fréquents utilisés dans le discours de [Michelle](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   3) Les dix mots les plus fréquents utilisés dans le discours de [Trump](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   4) Les dix mots les plus fréquents utilisés dans le discours de [Melina](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
4. Écrivez une application Python qui vérifie la similarité entre deux textes. Elle prend un fichier ou une chaîne comme paramètre et évaluera la similarité des deux textes. Par exemple, vérifiez la similarité entre les transcriptions du discours de [Michelle](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) et de [Melina](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt). Vous aurez besoin de quelques fonctions : une fonction pour nettoyer le texte (clean_text), une fonction pour supprimer les mots vides (remove_support_words) et enfin pour vérifier la similarité (check_text_similarity). La liste des [mots vides](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) se trouve dans le dossier data.
5. Trouvez les 10 mots les plus répétés dans le fichier romeo_and_juliet.txt
6. Lisez le fichier [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) et trouvez :
   1) Comptez le nombre de lignes contenant python ou Python
   2) Comptez le nombre de lignes contenant JavaScript, javascript ou Javascript
   3) Comptez le nombre de lignes contenant Java et pas JavaScript

🎉 FÉLICITATIONS ! 🎉

[<< Jour 18](./18_regular_expressions_fr.md) | [Jour 20 >>](./20_python_package_manager_fr.md)

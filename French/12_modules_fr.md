<div align="center">
  <h1> 30 Jours de Python : Jour 12 - Modules</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Auteur :
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Deuxième édition : juillet 2021</small>
</sub>


</div>

[<< Jour 11](./11_functions_fr.md) | [Jour 13 >>](./13_list_comprehension_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 12](#-jour-12)
  - [Modules](#modules)
    - [Qu'est-ce qu'un module](#quest-ce-quun-module)
    - [Créer un module](#créer-un-module)
    - [Importer un module](#importer-un-module)
    - [Importer des fonctions depuis un module](#importer-des-fonctions-depuis-un-module)
    - [Importer des fonctions depuis un module et les renommer](#importer-des-fonctions-depuis-un-module-et-les-renommer)
  - [Importer des modules intégrés](#importer-des-modules-intégrés)
    - [Module OS](#module-os)
    - [Module Sys](#module-sys)
    - [Module Statistics](#module-statistics)
    - [Module Math](#module-math)
    - [Module String](#module-string)
    - [Module Random](#module-random)
  - [💻 Exercices : Jour 12](#-exercices--jour-12)
    - [Exercices : Niveau 1](#exercices--niveau-1)
    - [Exercices : Niveau 2](#exercices--niveau-2)
    - [Exercices : Niveau 3](#exercices--niveau-3)

# 📘 Jour 12

## Modules

### Qu'est-ce qu'un module

Un module est un fichier contenant un ensemble de code ou de fonctions qui peuvent être inclus dans une application. Un module peut être un fichier contenant une seule variable, une fonction ou une grande base de code.

### Créer un module

Pour créer un module, nous écrivons notre code dans un script Python et nous le sauvegardons avec l'extension .py. Créez un fichier nommé mymodule.py dans votre dossier de projet. Écrivons du code dans ce fichier.

```py
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

Créez un fichier main.py dans votre répertoire de projet et importez le fichier mymodule.py.

### Importer un module

Pour importer le fichier, nous utilisons le mot-clé _import_ et uniquement le nom du fichier.

```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### Importer des fonctions depuis un module

Nous pouvons avoir plusieurs fonctions dans un fichier et nous pouvons les importer de différentes manières.

```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Importer des fonctions depuis un module et les renommer

Lors de l'importation, nous pouvons renommer le module.

```py
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Importer des modules intégrés

Comme dans d'autres langages de programmation, nous pouvons importer des modules en utilisant le mot-clé _import_. Importons les modules courants que nous utiliserons la plupart du temps. Voici quelques modules intégrés courants : _math_, _datetime_, _os_, _sys_, _random_, _statistics_, _collections_, _json_, _re_.

### Module OS

En utilisant le module _os_ de Python, il est possible d'effectuer automatiquement de nombreuses tâches du système d'exploitation. Le module OS en Python fournit des fonctions pour créer un répertoire, changer de répertoire de travail, supprimer un répertoire (dossier), récupérer son contenu, et identifier le répertoire courant.

```py
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

### Module Sys

Le module sys fournit des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution Python. La fonction sys.argv retourne une liste des arguments de ligne de commande passés à un script Python. L'élément à l'indice 0 de cette liste est toujours le nom du script, à l'indice 1 se trouve l'argument passé depuis la ligne de commande.

Exemple d'un fichier script.py :

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # cette ligne afficherait : nom_du_fichier argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

Pour vérifier le fonctionnement de ce script, j'ai écrit dans la ligne de commande :

```sh
python script.py Asabeneh 30DaysOfPython
```

Le résultat :

```sh
Welcome Asabeneh. Enjoy 30DaysOfPython challenge! 
```

Quelques commandes sys utiles :

```py
# pour quitter sys
sys.exit()
# Pour connaître le plus grand entier qu'il peut prendre
sys.maxsize
# Pour connaître le chemin d'environnement
sys.path
# Pour connaître la version de Python utilisée
sys.version
```

### Module Statistics

Le module statistics fournit des fonctions pour les statistiques mathématiques de données numériques. Les fonctions statistiques populaires définies dans ce module : _mean_, _median_, _mode_, _stdev_, etc.

```py
from statistics import * # importe toutes les fonctions du module statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Module Math

Module contenant de nombreuses opérations et constantes mathématiques.

```py
import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, racine carrée
print(math.pow(2, 3))    # 8.0, fonction exponentielle
print(math.floor(9.81))  # 9, arrondi à l'inférieur
print(math.ceil(9.81))   # 10, arrondi au supérieur
print(math.log10(100))   # 2, logarithme en base 10
```

Nous avons maintenant importé le module *math* qui contient de nombreuses fonctions pour effectuer des calculs mathématiques. Pour voir les fonctions disponibles dans le module, nous pouvons utiliser _help(math)_ ou _dir(math)_. Cela affichera les fonctions disponibles dans le module. Si nous voulons importer seulement une fonction spécifique du module, nous l'importons comme suit :

```py
from math import pi
print(pi)
```

Il est également possible d'importer plusieurs fonctions à la fois :

```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

Mais si nous voulons importer toutes les fonctions du module math, nous pouvons utiliser \* .

```py
from math import *
print(pi)                  # 3.141592653589793, constante pi
print(sqrt(2))             # 1.4142135623730951, racine carrée
print(pow(2, 3))           # 8.0, exponentielle
print(floor(9.81))         # 9, arrondi à l'inférieur
print(ceil(9.81))          # 10, arrondi au supérieur
print(math.log10(100))     # 2
```

Lors de l'importation, nous pouvons aussi renommer la fonction.

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### Module String

Le module string est un module utile à plusieurs fins. L'exemple ci-dessous montre quelques utilisations du module string.

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Module Random

Vous êtes maintenant familier avec l'importation de modules. Faisons une importation de plus pour bien nous familiariser. Importons le module _random_ qui nous donne un nombre aléatoire entre 0 et 0,9999.... Le module _random_ a de nombreuses fonctions, mais dans cette section, nous n'utiliserons que _random_ et _randint_.

```py
from random import random, randint
print(random())   # ne prend aucun argument ; retourne une valeur entre 0 et 0,9999
print(randint(5, 20)) # retourne un entier aléatoire entre [5, 20] inclus
```

🌕 Vous allez loin. Continuez ainsi ! Vous venez de terminer les défis du jour 12 et vous êtes 12 étapes plus loin vers l'excellence. Entraînez votre cerveau et vos muscles avec les exercices suivants.

## 💻 Exercices : Jour 12

### Exercices : Niveau 1

1. Écrivez une fonction qui génère un random_user_id de six chiffres/caractères.
   ```py
     print(random_user_id()) 
     '1ee33d'
   ```
2. Modifiez la tâche précédente. Déclarez une fonction nommée user_id_gen_by_user. Elle ne prend aucun paramètre mais prend deux entrées avec input(). La première entrée est le nombre de caractères et la seconde est le nombre d'ID à générer.
   
```py
print(user_id_gen_by_user()) # saisie utilisateur : 5 5
#sortie :
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. Écrivez une fonction nommée rgb_color_gen. Elle générera des couleurs rgb (3 valeurs comprises entre 0 et 255 chacune).
   
```py
print(rgb_color_gen())
# rgb(125,244,255) - la sortie doit être sous cette forme
```

### Exercices : Niveau 2

1. Écrivez une fonction list_of_hexa_colors qui retourne un nombre quelconque de couleurs hexadécimales dans un tableau (six chiffres hexadécimaux écrits après #. Le système de numération hexadécimal est composé de 16 symboles : 0-9 et les 6 premières lettres de l'alphabet, a-f.)
2. Écrivez une fonction list_of_rgb_colors qui retourne un nombre quelconque de couleurs RVB dans un tableau.
3. Écrivez une fonction generate_colors qui peut générer un nombre quelconque de couleurs hexa ou rgb.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

### Exercices : Niveau 3

1. Appelez votre fonction shuffle_list, elle prend une liste en paramètre et retourne une liste mélangée.
2. Écrivez une fonction qui retourne un tableau de sept nombres aléatoires dans un intervalle de 0 à 9. Tous les nombres doivent être uniques.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 11](./11_functions_fr.md) | [Jour 13 >>](./13_list_comprehension_fr.md)

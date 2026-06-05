<div align="center">
  <h1> 30 Jours de Python : Jour 14 - Fonctions d'ordre supérieur</h1>
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

[<< Jour 13](./13_list_comprehension_fr.md) | [Jour 15 >>](./15_python_type_errors_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 14](#-jour-14)
  - [Fonctions d'ordre supérieur](#fonctions-dordre-supérieur)
    - [Fonction comme paramètre](#fonction-comme-paramètre)
    - [Fonction comme valeur de retour](#fonction-comme-valeur-de-retour)
  - [Fermetures Python](#fermetures-python)
  - [Décorateurs Python](#décorateurs-python)
    - [Créer des décorateurs](#créer-des-décorateurs)
    - [Appliquer plusieurs décorateurs à une seule fonction](#appliquer-plusieurs-décorateurs-à-une-seule-fonction)
    - [Accepter des paramètres dans les fonctions décoratrices](#accepter-des-paramètres-dans-les-fonctions-décoratrices)
  - [Fonctions d'ordre supérieur intégrées](#fonctions-dordre-supérieur-intégrées)
    - [Python - Fonction Map](#python---fonction-map)
    - [Python - Fonction Filter](#python---fonction-filter)
    - [Python - Fonction Reduce](#python---fonction-reduce)
  - [💻 Exercices : Jour 14](#-exercices--jour-14)
    - [Exercices : Niveau 1](#exercices--niveau-1)
    - [Exercices : Niveau 2](#exercices--niveau-2)
    - [Exercices : Niveau 3](#exercices--niveau-3)

# 📘 Jour 14

## Fonctions d'ordre supérieur

En Python, les fonctions sont traitées comme des citoyens de première classe, ce qui permet d'effectuer les opérations suivantes sur les fonctions :

- Une fonction peut prendre une ou plusieurs fonctions comme paramètres
- Une fonction peut être retournée comme résultat d'une autre fonction
- Une fonction peut être modifiée
- Une fonction peut être assignée à une variable

Dans cette section, nous aborderons :

1. La manipulation des fonctions comme paramètres
2. Le retour de fonctions comme valeur de retour depuis d'autres fonctions
3. L'utilisation des fermetures et décorateurs Python

### Fonction comme paramètre

```py
def sum_numbers(nums):  # fonction normale
    return sum(nums)    # une fonction simple utilisant la fonction intégrée sum

def higher_order_function(f, lst):  # fonction comme paramètre
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Fonction comme valeur de retour

```py
def square(x):          # une fonction carré
    return x ** 2

def cube(x):            # une fonction cube
    return x ** 3

def absolute(x):        # une fonction valeur absolue
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # une fonction d'ordre supérieur retournant une fonction
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

Vous pouvez voir dans l'exemple ci-dessus que la fonction d'ordre supérieur retourne différentes fonctions selon le paramètre passé.

## Fermetures Python

Python permet à une fonction imbriquée d'accéder à la portée externe de la fonction englobante. C'est ce qu'on appelle une fermeture (closure). Voyons comment les fermetures fonctionnent en Python. En Python, une fermeture est créée en imbriquant une fonction à l'intérieur d'une autre fonction encapsulante, puis en retournant la fonction interne. Voir l'exemple ci-dessous.

**Exemple :**

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Décorateurs Python

Un décorateur est un patron de conception en Python qui permet d'ajouter de nouvelles fonctionnalités à un objet existant sans modifier sa structure. Les décorateurs sont généralement appelés avant la définition de la fonction que vous souhaitez décorer.

### Créer des décorateurs

Pour créer une fonction décoratrice, nous avons besoin d'une fonction externe avec une fonction wrapper interne.

**Exemple :**

```py
# Fonction normale
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Implémentons l'exemple ci-dessus avec un décorateur

'''Cette fonction décoratrice est une fonction d'ordre supérieur
qui prend une fonction comme paramètre'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

### Appliquer plusieurs décorateurs à une seule fonction

```py

'''Ces fonctions décoratrices sont des fonctions d'ordre supérieur
qui prennent des fonctions comme paramètres'''

# Premier décorateur
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Deuxième décorateur
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

# Les décorateurs sont exécutés de bas en haut
@split_string_decorator
@uppercase_decorator     # l'ordre des décorateurs est important dans ce cas - .upper() ne fonctionne pas avec les listes
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### Accepter des paramètres dans les fonctions décoratrices

La plupart du temps, nous avons besoin que nos fonctions prennent des paramètres, nous devons donc définir un décorateur qui accepte des paramètres.

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## Fonctions d'ordre supérieur intégrées

Parmi les fonctions d'ordre supérieur intégrées que nous abordons dans cette partie, on trouve _map()_, _filter_ et _reduce_.
Une fonction lambda peut être passée comme paramètre et le meilleur cas d'utilisation des fonctions lambda est dans des fonctions comme map, filter et reduce.

### Python - Fonction Map

La fonction map() est une fonction intégrée qui prend une fonction et un itérable comme paramètres.

```py
    # syntax
    map(function, iterable)
```

**Exemple 1 :**

```py
numbers = [1, 2, 3, 4, 5] # itérable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Appliquons-la avec une fonction lambda
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Exemple 2 :**

```py
numbers_str = ['1', '2', '3', '4', '5']  # itérable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Exemple 3 :**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # itérable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Appliquons-la avec une fonction lambda
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

Ce que fait réellement map, c'est itérer sur une liste. Par exemple, elle met les noms en majuscules et retourne une nouvelle liste.

### Python - Fonction Filter

La fonction filter() appelle la fonction spécifiée qui retourne un booléen pour chaque élément de l'itérable spécifié (liste). Elle filtre les éléments qui satisfont les critères de filtrage.

```py
    # syntax
    filter(function, iterable)
```

**Exemple 1 :**

```py
# Filtrons uniquement les nombres pairs
numbers = [1, 2, 3, 4, 5]  # itérable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Exemple 2 :**

```py
numbers = [1, 2, 3, 4, 5]  # itérable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# Filtrer les noms longs
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # itérable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python - Fonction Reduce

La fonction _reduce()_ est définie dans le module functools et nous devons l'importer depuis ce module. Comme map et filter, elle prend deux paramètres : une fonction et un itérable. Cependant, elle ne retourne pas un autre itérable, mais une valeur unique.

**Exemple 1 :**

```py
numbers_str = ['1', '2', '3', '4', '5']  # itérable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Exercices : Jour 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Exercices : Niveau 1

1. Expliquez la différence entre map, filter et reduce.
2. Expliquez la différence entre fonction d'ordre supérieur, fermeture et décorateur.
3. Définissez une fonction d'appel avant map, filter ou reduce, voir les exemples.
4. Utilisez une boucle for pour afficher chaque pays dans la liste countries.
5. Utilisez une boucle for pour afficher chaque nom dans la liste names.
6. Utilisez une boucle for pour afficher chaque nombre dans la liste numbers.

### Exercices : Niveau 2

1. Utilisez map pour créer une nouvelle liste en mettant chaque pays en majuscules dans la liste countries.
2. Utilisez map pour créer une nouvelle liste en convertissant chaque nombre en son carré dans la liste numbers.
3. Utilisez map pour mettre chaque nom en majuscules dans la liste names.
4. Utilisez filter pour filtrer les pays contenant 'land'.
5. Utilisez filter pour filtrer les pays ayant exactement six caractères.
6. Utilisez filter pour filtrer les pays contenant six lettres ou plus dans la liste countries.
7. Utilisez filter pour filtrer les pays commençant par 'E'.
8. Enchaînez deux itérateurs de liste ou plus (ex. arr.map(callback).filter(callback).reduce(callback)).
9. Déclarez une fonction appelée get_string_lists qui prend une liste en paramètre et retourne une liste contenant uniquement les éléments de type chaîne.
10. Utilisez reduce pour additionner tous les nombres de la liste numbers.
11. Utilisez reduce pour concaténer tous les pays et produire cette phrase : Estonie, Finlande, Suède, Danemark, Norvège et Islande sont des pays d'Europe du Nord.
12. Déclarez une fonction appelée categorize_countries qui retourne une liste de pays ayant un motif commun (vous pouvez trouver la [liste des pays](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) dans ce dépôt sous countries.js (ex. 'land', 'ia', 'island', 'stan')).
13. Créez une fonction retournant un dictionnaire, où les clés représentent les lettres de début des pays et les valeurs sont le nombre de noms de pays commençant par cette lettre.
14. Déclarez une fonction get_first_ten_countries - elle retourne une liste des dix premiers pays de la liste countries.js dans le dossier data.
15. Déclarez une fonction get_last_ten_countries qui retourne les dix derniers pays de la liste countries.

### Exercices : Niveau 3

1. Utilisez le fichier countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) et suivez les tâches ci-dessous :
   - Triez les pays par nom, par capitale, par population.
   - Triez les dix langues les plus parlées par emplacement.
   - Triez les dix pays les plus peuplés.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 13](./13_list_comprehension_fr.md) | [Jour 15 >>](./15_python_type_errors_fr.md)

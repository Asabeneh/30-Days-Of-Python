<div align="center">
  <h1> 30 Jours de Python : Jour 13 - Compréhension de listes</h1>
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

[<< Jour 12](./12_modules_fr.md) | [Jour 14 >>](./14_higher_order_functions_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 13](#-jour-13)
  - [Compréhension de listes](#compréhension-de-listes)
  - [Fonction Lambda](#fonction-lambda)
    - [Créer une fonction Lambda](#créer-une-fonction-lambda)
    - [Fonction Lambda dans une autre fonction](#fonction-lambda-dans-une-autre-fonction)
  - [💻 Exercices : Jour 13](#-exercices--jour-13)

# 📘 Jour 13

## Compréhension de listes

La compréhension de listes en Python est une façon compacte de créer une liste à partir d'une séquence. C'est une manière concise de créer une nouvelle liste. La compréhension de listes est considérablement plus rapide que le traitement d'une liste avec une boucle _for_.

```py
# syntax
[i for i in iterable if condition]
```

**Exemple 1 :**

Par exemple, si vous voulez convertir une chaîne en une liste de caractères. Vous pouvez utiliser plusieurs méthodes. Voyons-en quelques-unes :

```py
# Une façon
language = 'Python'
lst = list(language) # conversion de la chaîne en liste
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Deuxième façon : compréhension de listes
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**Exemple 2 :**

Par exemple, si vous voulez générer une liste de nombres

```py
# Génération de nombres
numbers = [i for i in range(11)]  # pour générer les nombres de 0 à 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Il est possible d'effectuer des opérations mathématiques pendant l'itération
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Il est aussi possible de créer une liste de tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**Exemple 3 :**

La compréhension de listes peut être combinée avec une expression if


```py
# Génération de nombres pairs
even_numbers = [i for i in range(21) if i % 2 == 0]  # pour générer une liste de nombres pairs de 0 à 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Génération de nombres impairs
odd_numbers = [i for i in range(21) if i % 2 != 0]  # pour générer les nombres impairs de 0 à 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filtrage de nombres : filtrons les nombres pairs positifs de la liste ci-dessous
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [4, 6, 8, 10]

# Aplatissement d'un tableau à deux dimensions
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Fonction Lambda

Une fonction lambda est une petite fonction anonyme sans nom. Elle peut prendre n'importe quel nombre d'arguments, mais ne peut avoir qu'une seule expression. La fonction lambda est similaire aux fonctions anonymes en JavaScript. Nous en avons besoin lorsque nous voulons écrire une fonction anonyme à l'intérieur d'une autre fonction.

### Créer une fonction Lambda

Pour créer une fonction lambda, nous utilisons le mot-clé _lambda_ suivi d'un ou plusieurs paramètres, puis d'une expression. Voir la syntaxe et l'exemple ci-dessous. La fonction lambda n'utilise pas return mais retourne explicitement l'expression.

```py
# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

**Exemple :**

```py
# Fonction nommée
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Transformons la fonction ci-dessus en une fonction lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Fonction lambda auto-invoquée
(lambda a, b: a + b)(2,3) # 5 - nécessite d'être encapsulée dans print() pour voir le résultat dans la console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Variables multiples
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### Fonction Lambda dans une autre fonction

Utiliser une fonction lambda à l'intérieur d'une autre fonction.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # la fonction power a maintenant besoin de 2 arguments pour s'exécuter, dans des parenthèses séparées
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

🌕 Continuez votre bon travail. Gardez votre élan, le ciel est la limite ! Vous venez de terminer les défis du jour 13 et vous êtes 13 étapes plus loin vers l'excellence. Entraînez votre cerveau et vos muscles avec les exercices suivants.

## 💻 Exercices : Jour 13

1. Filtrez uniquement les nombres négatifs et zéro dans la liste en utilisant la compréhension de listes.
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. Aplatissez la liste de listes suivante en une liste unidimensionnelle :

   ```py
   list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. En utilisant la compréhension de listes, créez la liste de tuples suivante :
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. Aplatissez la liste suivante en une nouvelle liste :
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
5. Convertissez la liste suivante en une liste de dictionnaires :
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
6. Convertissez la liste de listes suivante en une liste de chaînes concaténées :
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
7. Écrivez une fonction lambda qui peut calculer la pente ou l'ordonnée à l'origine de fonctions linéaires.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 12](./12_modules_fr.md) | [Jour 14 >>](./14_higher_order_functions_fr.md)

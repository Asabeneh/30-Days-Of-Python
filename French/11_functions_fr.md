<div align="center">
  <h1> 30 Jours de Python : Jour 11 - Fonctions</h1>
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

[<< Jour 10](./10_loops_fr.md) | [Jour 12 >>](./12_modules_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 11](#-jour-11)
  - [Fonctions](#fonctions)
    - [Définir une fonction](#définir-une-fonction)
    - [Déclarer et appeler une fonction](#déclarer-et-appeler-une-fonction)
    - [Fonction sans paramètres](#fonction-sans-paramètres)
    - [Fonction retournant une valeur - Partie 1](#fonction-retournant-une-valeur---partie-1)
    - [Fonction avec paramètres](#fonction-avec-paramètres)
    - [Passer des arguments avec clé et valeur](#passer-des-arguments-avec-clé-et-valeur)
    - [Fonction retournant une valeur - Partie 2](#fonction-retournant-une-valeur---partie-2)
    - [Fonction avec paramètres par défaut](#fonction-avec-paramètres-par-défaut)
    - [Nombre arbitraire d'arguments](#nombre-arbitraire-darguments)
    - [Paramètres par défaut et nombre arbitraire dans les fonctions](#paramètres-par-défaut-et-nombre-arbitraire-dans-les-fonctions)
    - [Fonction comme paramètre d'une autre fonction](#fonction-comme-paramètre-dune-autre-fonction)
  - [Témoignage](#témoignage)
  - [💻 Exercices : Jour 11](#-exercices--jour-11)
    - [Exercices : Niveau 1](#exercices--niveau-1)
    - [Exercices : Niveau 2](#exercices--niveau-2)
    - [Exercices : Niveau 3](#exercices--niveau-3)

# 📘 Jour 11

## Fonctions

Jusqu'à présent, nous avons vu de nombreuses fonctions intégrées de Python. Dans cette section, nous allons nous concentrer sur les fonctions personnalisées. Qu'est-ce qu'une fonction ? Avant de commencer à créer des fonctions, découvrons ce qu'est une fonction et pourquoi nous en avons besoin.

### Définir une fonction

Une fonction est un bloc de code réutilisable conçu pour effectuer une tâche spécifique. Pour définir ou déclarer une fonction, Python fournit le mot-clé _def_. Voici la syntaxe pour définir une fonction. Le bloc de code de la fonction n'est exécuté que si la fonction est appelée ou invoquée.

### Déclarer et appeler une fonction

Lorsque nous créons une fonction, on appelle cela déclarer une fonction. Lorsque nous commençons à l'utiliser, on appelle cela _appeler_ ou _invoquer_ une fonction. Les fonctions peuvent être déclarées avec ou sans paramètres.

```py
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
```

### Fonction sans paramètres

Une fonction peut être déclarée sans paramètres.

**Exemple :**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # appel d'une fonction

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Fonction retournant une valeur - Partie 1

Les fonctions retournent des valeurs à l'aide de l'instruction _return_. Si une fonction n'a pas d'instruction return, elle retourne None. Réécrivons les fonctions ci-dessus en utilisant return. Désormais, nous obtenons une valeur d'une fonction lorsque nous l'appelons et l'affichons.

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Fonction avec paramètres

Dans une fonction, nous pouvons passer différents types de données (number, string, boolean, list, tuple, dictionary ou set) comme paramètres.

- Paramètre unique : si notre fonction prend un paramètre, nous devons l'appeler avec un argument

```py
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
```

**Exemple :**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Deux paramètres : une fonction peut avoir ou non un ou plusieurs paramètres. Une fonction peut aussi avoir deux paramètres ou plus. Si notre fonction prend des paramètres, nous devons l'appeler avec des arguments. Regardons une fonction avec deux paramètres :

```py
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
```

**Exemple :**

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # la valeur doit d'abord être convertie en chaîne
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Passer des arguments avec clé et valeur

Si nous passons les arguments avec clé et valeur, l'ordre des arguments n'a pas d'importance.

```py
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # l'ordre des arguments n'a pas d'importance ici
```

**Exemple :**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # l'ordre n'a pas d'importance
```

### Fonction retournant une valeur - Partie 2

Si nous ne retournons pas de valeur avec une fonction, alors notre fonction retourne _None_ par défaut. Pour retourner une valeur avec une fonction, nous utilisons le mot-clé _return_ suivi de la variable que nous retournons. Nous pouvons retourner n'importe quel type de données depuis une fonction.

- Retourner une chaîne :
**Exemple :**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- Retourner un nombre :

**Exemple :**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))
```

- Retourner un booléen :
  **Exemple :**

```py
def is_even (n):
    if n % 2 == 0:
        return True    # return arrête l'exécution de la fonction, similaire à break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Retourner une liste :
  **Exemple :**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Fonction avec paramètres par défaut

Parfois, nous passons des valeurs par défaut aux paramètres lorsque nous invoquons la fonction. Si nous ne passons pas d'arguments lors de l'appel de la fonction, leurs valeurs par défaut seront utilisées.

```py
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

**Exemple :**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # la valeur doit d'abord être convertie en chaîne
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - gravité moyenne à la surface de la Terre
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravité à la surface de la Lune
```

### Nombre arbitraire d'arguments

Si nous ne connaissons pas le nombre d'arguments que nous passons à notre fonction, nous pouvons créer une fonction qui peut prendre un nombre arbitraire d'arguments en ajoutant \* avant le nom du paramètre.

```py
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

**Exemple :**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # équivaut à total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Paramètres par défaut et nombre arbitraire dans les fonctions

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

### Dépaquetage de dictionnaire

Vous pouvez appeler une fonction qui a des arguments nommés en utilisant un dictionnaire avec des noms de clés correspondants. Pour ce faire, utilisez ``**``.

```py
# Définissez une fonction qui prend deux arguments : 'name' et 'location'
def greet(name, location):
    # Affiche un message de salutation utilisant les arguments fournis
    print("Hi there", name, "how is the weather in", location)

# Appelez la fonction en utilisant des arguments nommés
greet(name="Alice", location="New York")  
# Sortie : Hi there Alice how is the weather in New York

# Créez un dictionnaire avec des clés correspondant aux noms des paramètres de la fonction
my_dict = {"name": "Alice", "location": "New York"}

# Appelez la fonction en utilisant le dépaquetage de dictionnaire
greet(**my_dict)  
# L'opérateur ** dépaquette le dictionnaire, passant ses paires clé-valeur
# comme arguments nommés à la fonction.
# Sortie : Hi there Alice how is the weather in New York
```

### Nombre arbitraire d'arguments nommés

Vous pouvez également définir une fonction pour accepter un nombre arbitraire d'arguments nommés.

```py
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
```

Évitez généralement cela sauf si nécessaire, car cela rend plus difficile la compréhension de ce que la fonction accepte et fait.

### Fonction comme paramètre d'une autre fonction

```py
# Vous pouvez passer des fonctions comme paramètres
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 Vous avez accompli pas mal de choses jusqu'à présent. Continuez ainsi ! Vous venez de terminer les défis du jour 11 et vous êtes 11 étapes plus loin vers l'excellence. Entraînez votre cerveau et vos muscles avec les exercices suivants.

## Témoignage

Il est maintenant temps d'exprimer votre opinion sur l'auteur et 30DaysOfPython. Vous pouvez laisser votre témoignage sur ce [lien](https://testimonial-s3sw.onrender.com/).

## 💻 Exercices : Jour 11

### Exercices : Niveau 1

1. Déclarez une fonction _add_two_numbers_. Elle prend deux paramètres et retourne une somme.
2. L'aire d'un cercle se calcule ainsi : aire = π x r x r. Écrivez une fonction qui calcule _area_of_circle_.
3. Écrivez une fonction appelée add_all_nums qui prend un nombre arbitraire d'arguments et les additionne. Vérifiez si tous les éléments de la liste sont de type numérique. Sinon, donnez un retour approprié.
4. La température en °C peut être convertie en °F avec cette formule : °F = (°C x 9/5) + 32. Écrivez une fonction qui convertit °C en °F, _convert_celsius_to_fahrenheit_.
5. Écrivez une fonction appelée check_season, elle prend un paramètre month et retourne la saison : Automne, Hiver, Printemps ou Été.
6. Écrivez une fonction appelée calculate_slope qui retourne la pente d'une équation linéaire.
7. L'équation quadratique se calcule ainsi : ax² + bx + c = 0. Écrivez une fonction qui calcule l'ensemble des solutions d'une équation quadratique, _solve_quadratic_eqn_.
8. Déclarez une fonction nommée print_list. Elle prend une liste en paramètre et affiche chaque élément de la liste.
9. Déclarez une fonction nommée reverse_list. Elle prend un tableau en paramètre et retourne le tableau inversé (utilisez des boucles).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
```

10. Déclarez une fonction nommée capitalize_list_items. Elle prend une liste en paramètre et retourne une liste d'éléments en majuscules.
11. Déclarez une fonction nommée add_item. Elle prend une liste et un élément en paramètres. Elle retourne une liste avec l'élément ajouté à la fin.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. Déclarez une fonction nommée remove_item. Elle prend une liste et un élément en paramètres. Elle retourne une liste avec l'élément supprimé.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Déclarez une fonction nommée sum_of_numbers. Elle prend un paramètre number et additionne tous les nombres dans cet intervalle.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. Déclarez une fonction nommée sum_of_odds. Elle prend un paramètre number et additionne tous les nombres impairs dans cet intervalle.
15. Déclarez une fonction nommée sum_of_even. Elle prend un paramètre number et additionne tous les nombres pairs dans cet intervalle.

### Exercices : Niveau 2

1. Déclarez une fonction nommée evens_and_odds. Elle prend un entier positif en paramètre et compte le nombre de pairs et d'impairs dans le nombre.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

2. Appelez votre fonction factorial, elle prend un nombre entier en paramètre et retourne la factorielle de ce nombre.
3. Appelez votre fonction _is_empty_, elle prend un paramètre et vérifie s'il est vide ou non.
4. Écrivez différentes fonctions qui prennent des listes. Elles doivent calculer calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (écart type).
5. Écrivez une fonction appelée _greet_ qui prend un argument par défaut, _name_. Si aucun argument n'est fourni, elle doit afficher "Hello, Guest!", sinon elle doit saluer la personne par son nom.

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```

6. Créez une fonction appelée _show_args_ pour prendre un nombre arbitraire d'arguments nommés et afficher leurs noms et valeurs.

   ```py
   show_args(name="Alice", age=30, city="New York")
   # Received: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```

### Exercices : Niveau 3

1. Écrivez une fonction appelée is_prime qui vérifie si un nombre est premier.
2. Écrivez une fonction qui vérifie si tous les éléments de la liste sont uniques.
3. Écrivez une fonction qui vérifie si tous les éléments de la liste sont du même type de données.
4. Écrivez une fonction qui vérifie si une variable fournie est une variable Python valide.
5. Allez dans le dossier data et accédez au fichier countries-data.py.

   - Créez une fonction appelée most_spoken_languages in the world. Elle doit retourner les 10 ou 20 langues les plus parlées dans le monde par ordre décroissant.
   - Créez une fonction appelée most_populated_countries. Elle doit retourner les 10 ou 20 pays les plus peuplés par ordre décroissant.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 10](./10_loops_fr.md) | [Jour 12 >>](./12_modules_fr.md)

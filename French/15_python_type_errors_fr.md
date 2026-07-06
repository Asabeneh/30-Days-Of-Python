<div align="center">
  <h1> 30 Jours de Python : Jour 15 - Erreurs de type en Python</h1>
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

[<< Jour 14](./14_higher_order_functions_fr.md) | [Jour 16 >>](./16_python_datetime_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Jour 15](#-jour-15)
  - [Types d'erreurs Python](#types-derreurs-python)
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexerror)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)
  - [💻 Exercices : Jour 15](#-exercices--jour-15)

# 📘 Jour 15

## Types d'erreurs Python

Quand on écrit du code, il est courant de faire une faute de frappe ou une autre erreur fréquente. Si notre code ne s'exécute pas, l'interpréteur Python affiche un message contenant des informations sur l'endroit où le problème se produit et le type d'erreur. Il nous donne aussi parfois des suggestions de correction. Comprendre les différents types d'erreurs dans les langages de programmation nous aide à déboguer notre code rapidement et nous rend meilleurs dans ce que nous faisons.

Voyons les types d'erreurs les plus courants un par un. Commençons par ouvrir notre terminal interactif Python. Allez dans votre terminal et tapez 'python'. Le terminal interactif Python s'ouvrira.

### SyntaxError

**Exemple 1 : SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

Comme vous pouvez le voir, nous avons fait une erreur de syntaxe car nous avons oublié d'entourer la chaîne de parenthèses, et Python nous suggère déjà la solution. Corrigeons-la.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

L'erreur était une _SyntaxError_. Après la correction, notre code s'est exécuté sans problème. Voyons d'autres types d'erreurs.

### NameError

**Exemple 1 : NameError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

Comme vous pouvez le voir dans le message ci-dessus, le nom age n'est pas défini. Oui, c'est vrai, nous n'avons pas défini de variable age mais nous essayions de l'afficher comme si nous l'avions déclarée. Corrigeons cela en la déclarant et en lui assignant une valeur.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

Le type d'erreur était une _NameError_. Nous avons débogué l'erreur en définissant le nom de la variable.

### IndexError

**Exemple 1 : IndexError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

Dans l'exemple ci-dessus, Python a levé une _IndexError_, car la liste n'a que des index de 0 à 4, donc il était hors limites.

### ModuleNotFoundError

**Exemple 1 : ModuleNotFoundError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

Dans l'exemple ci-dessus, j'ai délibérément ajouté un s supplémentaire à math et _ModuleNotFoundError_ a été levée. Corrigeons cela en retirant le s supplémentaire de math.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

Nous avons corrigé, utilisons donc quelques fonctions du module math.

### AttributeError

**Exemple 1 : AttributeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

Comme vous pouvez le voir, j'ai encore fait une erreur ! Au lieu de pi, j'ai essayé d'appeler une constante PI du module math. Cela a levé une AttributeError, ce qui signifie que l'attribut n'existe pas dans le module. Corrigeons en changeant PI en pi.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

Maintenant, en appelant pi depuis le module math, nous avons obtenu le résultat.

### KeyError

**Exemple 1 : KeyError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

Comme vous pouvez le voir, il y avait une faute de frappe dans la clé utilisée pour obtenir la valeur du dictionnaire. C'est donc une KeyError et la correction est assez simple. Faisons cela !

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

Nous avons débogué l'erreur, notre code s'est exécuté et nous avons obtenu la valeur.

### TypeError

**Exemple 1 : TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

Dans l'exemple ci-dessus, une TypeError est levée car nous ne pouvons pas additionner un nombre à une chaîne. La première solution serait de convertir la chaîne en int ou float. Une autre solution serait de convertir le nombre en chaîne (le résultat serait alors '43'). Suivons la première correction.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

L'erreur a été supprimée et nous avons obtenu le résultat attendu.

### ImportError

**Exemple 1 : ImportError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

Il n'y a pas de fonction appelée power dans le module math, elle porte un nom différent : _pow_. Corrigeons cela :

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### ValueError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

Dans ce cas, nous ne pouvons pas convertir la chaîne donnée en nombre à cause de la lettre 'a' qu'elle contient.

### ZeroDivisionError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

Nous ne pouvons pas diviser un nombre par zéro.

Nous avons couvert certains des types d'erreurs Python ; si vous voulez en savoir plus, consultez la documentation Python sur les types d'erreurs.
Si vous êtes capable de lire les types d'erreurs, vous pourrez corriger vos bugs rapidement et vous deviendrez également un meilleur programmeur.

🌕 Vous excellez. Vous êtes à mi-chemin de la grandeur. Faites maintenant quelques exercices pour votre cerveau et pour vos muscles.

## 💻 Exercices : Jour 15

1. Ouvrez votre terminal interactif Python et essayez tous les exemples abordés dans cette section.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 14](./14_higher_order_functions_fr.md) | [Jour 16 >>](./16_python_datetime_fr.md)

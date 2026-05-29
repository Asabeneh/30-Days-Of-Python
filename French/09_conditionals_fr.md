<div align="center">
  <h1> 30 Jours de Python : Jour 9 - Conditionnels</h1>
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

[<< Jour 8](./08_dictionaries_fr.md) | [Jour 10 >>](./10_loops_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 9](#-jour-9)
  - [Conditionnels](#conditionnels)
    - [Condition If](#condition-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Format raccourci](#format-raccourci)
    - [Conditions imbriquées](#conditions-imbriquées)
    - [Condition If et opérateurs logiques](#condition-if-et-opérateurs-logiques)
    - [If et opérateur logique Or](#if-et-opérateur-logique-or)
  - [💻 Exercices : Jour 9](#-exercices--jour-9)
    - [Exercices : Niveau 1](#exercices--niveau-1)
    - [Exercices : Niveau 2](#exercices--niveau-2)
    - [Exercices : Niveau 3](#exercices--niveau-3)

# 📘 Jour 9

## Conditionnels

Par défaut, les instructions dans un script Python sont exécutées séquentiellement de haut en bas. Si la logique du programme l'exige, l'ordre d'exécution peut être modifié de deux manières :

- **Exécution conditionnelle** : un bloc d'une ou plusieurs instructions s'exécute si une expression est vraie.
- **Exécution répétitive** : un bloc d'une ou plusieurs instructions s'exécute de manière répétitive tant qu'une expression est vraie.

Dans cette section, nous aborderons les instructions _if_, _else_, _elif_. Les opérateurs de comparaison et logiques que nous avons appris dans les sections précédentes seront utiles ici.

### Condition If

En Python et dans d'autres langages de programmation, le mot-clé _if_ est utilisé pour vérifier si une condition est vraie et exécuter le bloc de code. N'oubliez pas l'indentation après les deux-points.

```py
# syntax
if condition:
    this part of code runs for truthy conditions
```

**Exemple 1 :**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

Comme vous pouvez le voir dans l'exemple ci-dessus, 3 est plus grand que 0. La condition était vraie et le bloc de code a été exécuté. Cependant, si la condition est fausse, nous ne voyons pas le résultat. Pour voir le résultat quand la condition est fausse, il faut un autre bloc, qui sera _else_.

### If Else

Si la condition est vraie, le premier bloc s'exécute ; sinon, c'est le bloc else qui s'exécute.

```py
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**Exemple :**

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

La condition ci-dessus est fausse, donc le bloc else s'exécute. Et si notre condition a plus de deux cas ? Nous pourrions utiliser _elif_.

### If Elif Else

Dans notre vie quotidienne, nous prenons des décisions chaque jour. Nous ne prenons pas nos décisions en vérifiant une ou deux conditions, mais bien plusieurs. Comme dans la vie, la programmation est également pleine de conditions. Nous utilisons _elif_ lorsque nous avons plusieurs conditions.

```py
# syntax
if condition:
    code
elif condition:
    code
else:
    code

```

**Exemple :**

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### Format raccourci

```py
# syntax
code if condition else code
```

**Exemple :**

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # première condition satisfaite, 'A is positive' sera affiché
```

### Conditions imbriquées

Les conditions peuvent être imbriquées.

```py
# syntax
if condition:
    code
    if condition:
    code
```

**Exemple :**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

```

Nous pouvons éviter d'écrire des conditions imbriquées en utilisant l'opérateur logique _and_.

### Condition If et opérateurs logiques

```py
# syntax
if condition and condition:
    code
```

**Exemple :**

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

### If et opérateur logique Or

```py
# syntax
if condition or condition:
    code
```

**Exemple :**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

🌕 Vous faites un excellent travail. N'abandonnez jamais, car les grandes choses prennent du temps. Vous venez de terminer les défis du jour 9 et vous êtes 9 étapes plus loin vers l'excellence. Entraînez votre cerveau et vos muscles avec les exercices suivants.

## 💻 Exercices : Jour 9

### Exercices : Niveau 1

1. Obtenez une entrée utilisateur avec input("Entrez votre âge : "). Si l'utilisateur a 18 ans ou plus, retournez : Vous êtes assez âgé pour conduire. Si moins de 18 ans, indiquez le nombre d'années restantes. Sortie :

    ```sh
    Entrez votre âge : 30
    Vous êtes assez âgé pour apprendre à conduire.

    Entrez votre âge : 15
    Il vous reste 3 ans à attendre pour apprendre à conduire.
    ```

2. Comparez les valeurs de my_age et your_age en utilisant if … else. Qui est le plus âgé (moi ou vous) ? Utilisez input("Entrez votre âge : ") pour obtenir l'âge. Vous pouvez utiliser une condition imbriquée pour afficher 'an' pour 1 an de différence, 'ans' pour des différences plus grandes, et un texte personnalisé si my_age = your_age. Sortie :

    ```sh
    Entrez votre âge : 30
    Vous avez 5 ans de plus que moi.
    ```

3. Obtenez deux nombres de l'utilisateur via input. Si a est plus grand que b, retournez a est plus grand que b, si a est plus petit que b, retournez a est plus petit que b, sinon a est égal à b. Sortie :

```sh
Entrez le nombre un : 4
Entrez le nombre deux : 3
4 est plus grand que 3
```

### Exercices : Niveau 2

1. Écrivez un code qui attribue une note aux élèves selon leurs scores :

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

2. Obtenez le mois de l'utilisateur, puis vérifiez si la saison est Automne, Hiver, Printemps ou Été. Si l'utilisateur saisit :
    Septembre, Octobre ou Novembre, la saison est l'Automne.
    Décembre, Janvier ou Février, la saison est l'Hiver.
    Mars, Avril ou Mai, la saison est le Printemps.
    Juin, Juillet ou Août, la saison est l'Été.

3. La liste suivante contient des fruits :

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    Si un fruit n'existe pas dans la liste, ajoutez le fruit à la liste et affichez la liste modifiée. Si le fruit existe, affichez 'Ce fruit existe déjà dans la liste' avec print().

### Exercices : Niveau 3

1. Voici un dictionnaire person. N'hésitez pas à le modifier !

```py
    person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

    * Vérifiez si le dictionnaire person a une clé skills, si oui, affichez la compétence du milieu dans la liste skills.
    * Vérifiez si le dictionnaire person a une clé skills, si oui, vérifiez si la personne a la compétence 'Python' et affichez le résultat.
    * Si la personne n'a que JavaScript et React dans ses compétences, affichez 'He is a front end developer' avec print(), si la personne a Node, Python, MongoDB, affichez 'He is a backend developer' avec print(), si la personne a React, Node et MongoDB, affichez 'He is a fullstack developer' avec print(), sinon affichez 'unknown title' avec print() - pour des résultats plus précis, vous pouvez imbriquer davantage de conditions !
    * Si la personne est mariée et vit en Finlande, affichez les informations au format suivant :

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 FÉLICITATIONS ! 🎉

[<< Jour 8](./08_dictionaries_fr.md) | [Jour 10 >>](./10_loops_fr.md)

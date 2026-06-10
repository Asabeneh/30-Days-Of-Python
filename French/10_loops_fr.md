<div align="center">
  <h1> 30 Jours de Python : Jour 10 - Boucles</h1>
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

[<< Jour 9](./09_conditionals_fr.md) | [Jour 11 >>](./11_functions_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 10](#-jour-10)
  - [Boucles](#boucles)
    - [Boucle While](#boucle-while)
    - [Break et Continue - Partie 1](#break-et-continue---partie-1)
    - [Boucle For](#boucle-for)
    - [Break et Continue - Partie 2](#break-et-continue---partie-2)
    - [La Fonction Range](#la-fonction-range)
    - [Boucle For Imbriquée](#boucle-for-imbriquée)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [💻 Exercices : Jour 10](#-exercices--jour-10)
    - [Exercices : Niveau 1](#exercices--niveau-1)
    - [Exercices : Niveau 2](#exercices--niveau-2)
    - [Exercices : Niveau 3](#exercices--niveau-3)

# 📘 Jour 10

## Boucles

La vie est faite de routines. En programmation, nous effectuons aussi beaucoup de tâches répétitives. Pour gérer ces tâches répétitives, les langages de programmation utilisent des boucles. Python propose également les deux types de boucles suivants :

1. while
2. for

### Boucle While

Nous utilisons le mot réservé _while_ pour créer une boucle while. Elle est utilisée pour exécuter un bloc d'instructions de manière répétée jusqu'à ce que la condition soit vraie. Lorsque la condition devient fausse, les lignes de code après la boucle continuent de s'exécuter.

```py
  # syntax
while condition:
    code goes here
```

**Exemple :**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
# affiche de 0 à 4
```

Dans la boucle while ci-dessus, la condition devient fausse lorsque count vaut 5. C'est à ce moment que la boucle s'arrête.
Si nous souhaitons exécuter un bloc de code une fois la condition devenue fausse, nous pouvons utiliser _else_.

```py
  # syntax
while condition:
    code goes here
else:
    code goes here
```

**Exemple :**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

La condition de la boucle ci-dessus devient fausse lorsque count vaut 5 et la boucle s'arrête, puis l'exécution passe à l'instruction else. Par conséquent, 5 sera affiché.

### Break et Continue - Partie 1

- Break : Nous utilisons break lorsque nous voulons sortir de la boucle ou l'arrêter.

```py
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

**Exemple :**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

La boucle while ci-dessus n'affiche que 0, 1, 2, mais lorsqu'elle atteint 3, elle s'arrête.

- Continue : Avec l'instruction continue, nous pouvons sauter l'itération en cours et continuer avec la suivante :

```py
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

**Exemple :**

```py
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

La boucle while ci-dessus n'affiche que 0, 1, 2 et 4 (saute 3).

### Boucle For

Le mot-clé _for_ est utilisé pour créer une boucle for, similaire à d'autres langages de programmation, mais avec quelques différences de syntaxe. La boucle est utilisée pour itérer sur une séquence (liste, tuple, dictionnaire, ensemble ou chaîne de caractères).

- Boucle For sur une liste

```py
# syntax
for iterator in lst:
    code goes here
```

**Exemple :**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number est un nom temporaire pour référer aux éléments de la liste, valable uniquement dans cette boucle
    print(number)       # les nombres seront affichés ligne par ligne, de 0 à 5
```

- Boucle For sur une chaîne de caractères

```py
# syntax
for iterator in string:
    code goes here
```

**Exemple :**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- Boucle For sur un tuple

```py
# syntax
for iterator in tpl:
    code goes here
```

**Exemple :**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- Boucle For avec un dictionnaire
  Itérer sur un dictionnaire avec une boucle donne les clés du dictionnaire.

```py
  # syntax
for iterator in dct:
    code goes here
```

**Exemple :**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # de cette façon, nous obtenons à la fois les clés et les valeurs
```

- Boucle For sur un ensemble

```py
# syntax
for iterator in st:
    code goes here
```

**Exemple :**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break et Continue - Partie 2

Petit rappel :
_Break_ : Nous utilisons break lorsque nous voulons arrêter notre boucle avant qu'elle ne soit terminée.

```py
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

**Exemple :**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

Dans l'exemple ci-dessus, la boucle s'arrête lorsqu'elle atteint 3.

Continue : Nous utilisons continue lorsque nous voulons sauter certaines étapes dans l'itération de la boucle.

```py
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**Exemple :**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Le nombre suivant devrait être ', number + 1) if number != 5 else print("fin de la boucle") # pour le format raccourci, les instructions if et else sont toutes deux nécessaires
print('en dehors de la boucle')
```

Dans l'exemple ci-dessus, si le nombre est égal à 3, l'étape _après_ la condition (mais à l'intérieur de la boucle) est sautée et l'exécution de la boucle continue s'il reste des itérations.

### La Fonction Range

La fonction _range()_ est utilisée pour générer une séquence de nombres. _range(start, end, step)_ prend trois paramètres : le début, la fin et l'incrément. Par défaut, elle commence à 0 et l'incrément est de 1. La séquence range nécessite au moins 1 argument (end).
Créer des séquences avec range

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indiquent le début et la fin de la séquence, le pas est fixé à 1 par défaut
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# pour un parcours inversé
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

```py
# syntax
for iterator in range(start, end, step):
```

**Exemple :**

```py
for number in range(11):
    print(number)   # affiche de 0 à 10, 11 non inclus
```

### Boucle For Imbriquée

Nous pouvons écrire des boucles à l'intérieur d'une boucle.

```py
# syntax
for x in y:
    for t in x:
        print(t)
```

**Exemple :**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

Si nous voulons afficher un message lorsque la boucle se termine, nous utilisons else.

```py
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('La boucle est terminée')
```

**Exemple :**

```py
for number in range(11):
    print(number)   # affiche de 0 à 10, 11 non inclus
else:
    print('La boucle s\'arrête à', number)
```

### Pass

En Python, lorsqu'une instruction est requise (après les deux-points), mais que nous ne souhaitons pas y exécuter de code, nous pouvons écrire le mot _pass_ pour éviter les erreurs. Nous pouvons aussi l'utiliser comme un espace réservé pour de futures instructions.

**Exemple :**

```py
for number in range(6):
    pass
```

🌕 Vous avez franchi une grande étape, vous êtes imbattable. Continuez ainsi ! Vous venez de terminer les défis du jour 10 et vous êtes 10 étapes plus loin vers l'excellence. Entraînez votre cerveau et vos muscles avec les exercices suivants.

## 💻 Exercices : Jour 10

### Exercices : Niveau 1

1. Itérez de 0 à 10 avec une boucle for, puis faites de même avec une boucle while.
2. Itérez de 10 à 0 avec une boucle for, puis faites de même avec une boucle while.
3. Écrivez une boucle qui effectue sept appels à print() pour obtenir le triangle suivant :

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Utilisez des boucles imbriquées pour créer le motif suivant :

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. Affichez le motif suivant :

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. Parcourez la liste ['Python', 'Numpy','Pandas','Django', 'Flask'] avec une boucle for et affichez chaque élément.
7. Utilisez une boucle for pour itérer de 0 à 100 et n'affichez que les nombres pairs.
8. Utilisez une boucle for pour itérer de 0 à 100 et n'affichez que les nombres impairs.

### Exercices : Niveau 2

1.  Utilisez une boucle for pour itérer de 0 à 100 et affichez la somme de tous les nombres.

```sh
The sum of all numbers is 5050.
```

2. Utilisez une boucle for pour itérer de 0 à 100 et affichez la somme de tous les nombres pairs et la somme de tous les nombres impairs.

   ```sh
   The sum of all evens is 2550. And the sum of all odds is 2500.
   ```

### Exercices : Niveau 3

1. Allez dans le dossier data et utilisez le fichier [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py). Parcourez les pays et extrayez tous ceux contenant le mot _land_.
2. Voici une liste de fruits, ['banana', 'orange', 'mango', 'lemon']. Inversez l'ordre en utilisant une boucle.
3. Allez dans le dossier data et utilisez le fichier [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
   1. Quel est le nombre total de langues dans les données ?
   2. Trouvez les dix langues les plus parlées dans les données.
   3. Trouvez les 10 pays les plus peuplés du monde.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 9](./09_conditionals_fr.md) | [Jour 11 >>](./11_functions_fr.md)

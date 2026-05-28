<div align="center">
  <h1> 30 Jours de Python : Jour 7 - Ensembles</h1>
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

[<< Jour 6](./06_tuples_fr.md) | [Jour 8 >>](./08_dictionaries_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 7](#-jour-7)
  - [Ensembles](#ensembles)
    - [Créer un ensemble](#créer-un-ensemble)
    - [Obtenir la longueur d'un ensemble](#obtenir-la-longueur-dun-ensemble)
    - [Accéder aux éléments d'un ensemble](#accéder-aux-éléments-dun-ensemble)
    - [Vérifier un élément](#vérifier-un-élément)
    - [Ajouter des éléments à un ensemble](#ajouter-des-éléments-à-un-ensemble)
    - [Supprimer des éléments d'un ensemble](#supprimer-des-éléments-dun-ensemble)
    - [Vider un ensemble](#vider-un-ensemble)
    - [Supprimer un ensemble](#supprimer-un-ensemble)
    - [Convertir une liste en ensemble](#convertir-une-liste-en-ensemble)
    - [Joindre des ensembles](#joindre-des-ensembles)
    - [Trouver les éléments d'intersection](#trouver-les-éléments-dintersection)
    - [Vérifier les sous-ensembles et sur-ensembles](#vérifier-les-sous-ensembles-et-sur-ensembles)
    - [Vérifier la différence entre deux ensembles](#vérifier-la-différence-entre-deux-ensembles)
    - [Trouver la différence symétrique entre deux ensembles](#trouver-la-différence-symétrique-entre-deux-ensembles)
    - [Joindre des ensembles](#joindre-des-ensembles-1)
  - [💻 Exercices : Jour 7](#-exercices--jour-7)
    - [Exercices : Niveau 1](#exercices--niveau-1)
    - [Exercices : Niveau 2](#exercices--niveau-2)
    - [Exercices : Niveau 3](#exercices--niveau-3)

# 📘 Jour 7

## Ensembles

Un ensemble est une collection d'éléments. Revenons à vos cours de mathématiques à l'école primaire ou secondaire. La définition mathématique d'un ensemble peut également s'appliquer en Python. Un ensemble est une collection d'éléments distincts, non ordonnés et non indexés. En Python, un ensemble est utilisé pour stocker des éléments uniques, et il est possible de trouver l'_union_, l'_intersection_, la _différence_, la _différence symétrique_, le _sous-ensemble_, le _sur-ensemble_ ainsi que les _ensembles conjoints_ et _disjoints_.

### Créer un ensemble

Pour créer un ensemble vide, nous utilisons la fonction set(). Des accolades vides {} créeront un dictionnaire.

- Créer un ensemble vide

```py
# syntax
st = set()
```

- Créer un ensemble avec des éléments initiaux

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

**Exemple :**

```py
# syntax
fruits = {'banane', 'orange', 'mangue', 'citron'}
```

### Obtenir la longueur d'un ensemble

Nous utilisons la méthode **len()** pour connaître la taille d'un ensemble.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
len(fruits)
```

### Accéder aux éléments d'un ensemble

Nous utilisons des boucles pour accéder aux éléments. Nous verrons cela dans la section sur les boucles.

### Vérifier un élément

Pour vérifier si un élément existe dans un ensemble, nous utilisons l'opérateur d'appartenance _in_.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Est-ce que l'ensemble st contient item3 ? ", 'item3' in st) # Est-ce que l'ensemble st contient item3 ? True
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
print('mangue' in fruits ) # True
```

### Ajouter des éléments à un ensemble

Une fois qu'un ensemble est créé, nous ne pouvons pas modifier ses éléments, mais nous pouvons en ajouter de nouveaux.

- Ajouter un élément avec _add()_

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
fruits.add('lime')
```

- Ajouter plusieurs éléments avec _update()_
  La méthode _update()_ permet d'ajouter plusieurs éléments à un ensemble. _update()_ prend une liste en argument.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
legumes = ('tomate', 'pomme de terre', 'chou', 'oignon', 'carotte')
fruits.update(legumes)
```

### Supprimer des éléments d'un ensemble

Nous pouvons supprimer un élément d'un ensemble en utilisant la méthode _remove()_. Si l'élément n'est pas trouvé, la méthode _remove()_ générera une erreur, il est donc préférable de vérifier si l'élément existe dans l'ensemble. Cependant, la méthode _discard()_ ne génère aucune erreur.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

La méthode pop() retire un élément aléatoire d'un ensemble et retourne l'élément retiré.

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
fruits.pop()  # retire un élément aléatoire de l'ensemble

```

Si nous souhaitons récupérer l'élément retiré.

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
element_retire = fruits.pop() 
```

### Vider un ensemble

Si nous voulons vider un ensemble, nous utilisons la méthode _clear_.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
fruits.clear()
print(fruits) # set()
```

### Supprimer un ensemble

Si nous voulons supprimer l'ensemble lui-même, nous utilisons l'opérateur _del_.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
del fruits
```

### Convertir une liste en ensemble

Nous pouvons convertir une liste en ensemble et un ensemble en liste. Convertir une liste en ensemble supprime les doublons et seuls les éléments uniques sont conservés.

```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - l'ordre est aléatoire, car les ensembles ne sont pas ordonnés par nature
```

**Exemple :**

```py
fruits = ['banane', 'orange', 'mangue', 'citron', 'orange', 'banane']
fruits = set(fruits) # {'mangue', 'citron', 'banane', 'orange'}
```

### Joindre des ensembles

Nous pouvons joindre deux ensembles en utilisant la méthode _union()_, _update()_ ou le symbole _|_.

- Union
  Cette méthode retourne un nouvel ensemble

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
legumes = {'tomate', 'pomme de terre', 'chou', 'oignon', 'carotte'}
print(fruits.union(legumes)) # {'citron', 'carotte', 'tomate', 'banane', 'mangue', 'orange', 'chou', 'pomme de terre', 'oignon'}
# ou en utilisant : print(fruits | legumes)
```

- Mise à jour
  Cette méthode insère un ensemble dans un autre ensemble

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # le contenu de st2 est ajouté à st1
```

**Exemple :**

```py
fruits = {'banane', 'orange', 'mangue', 'citron'}
legumes = {'tomate', 'pomme de terre', 'chou', 'oignon', 'carotte'}
fruits.update(legumes)
print(fruits) # {'citron', 'carotte', 'tomate', 'banane', 'mangue', 'orange', 'chou', 'pomme de terre', 'oignon'}
```

### Trouver les éléments d'intersection

L'intersection retourne un ensemble d'éléments qui sont présents dans les deux ensembles, ou en utilisant le symbole _&_. Voir l'exemple

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# ou en utilisant : st1 & st2
```

**Exemple :**

```py
nombres_entiers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
nombres_pairs = {0, 2, 4, 6, 8, 10}
nombres_entiers.intersection(nombres_pairs) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon
```

### Vérifier les sous-ensembles et sur-ensembles

Un ensemble peut être un sous-ensemble ou un sur-ensemble d'autres ensembles :

- Sous-ensemble : _issubset()_
- Sur-ensemble : _issuperset()_

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**Exemple :**

```py
nombres_entiers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
nombres_pairs = {0, 2, 4, 6, 8, 10}
nombres_entiers.issubset(nombres_pairs) # False, car c'est un sur-ensemble
nombres_entiers.issuperset(nombres_pairs) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### Vérifier la différence entre deux ensembles

Elle retourne la différence entre deux ensembles, ou en utilisant le symbole _-_ .

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2 : st2 - st1
```

**Exemple :**

```py
nombres_entiers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
nombres_pairs = {0, 2, 4, 6, 8, 10}
nombres_entiers.difference(nombres_pairs) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - le résultat n'est pas ordonné (caractéristique des ensembles)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python
```

### Trouver la différence symétrique entre deux ensembles

Elle retourne la différence symétrique entre deux ensembles. Cela signifie qu'elle retourne un ensemble contenant tous les éléments des deux ensembles, à l'exception des éléments communs aux deux ensembles, mathématiquement : (A\B) ∪ (B\A)

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# cela signifie (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
```

**Exemple :**

```py
nombres_entiers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
certains_nombres = {1, 2, 3, 4, 5}
nombres_entiers.symmetric_difference(certains_nombres) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon
```

### Joindre des ensembles

Si deux ensembles n'ont aucun élément commun, on les appelle des ensembles disjoints. Nous pouvons vérifier si deux ensembles sont conjoints ou disjoints en utilisant la méthode _isdisjoint()_.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

**Exemple :**

```py
nombres_pairs = {0, 2, 4, 6, 8}
nombres_impairs = {1, 3, 5, 7, 9}
nombres_pairs.isdisjoint(nombres_impairs) # True, car aucun élément commun

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, il y a des éléments communs {'o', 'n'}
```

🌕 Vous êtes une étoile montante. Vous venez de terminer les défis du jour 7 et vous êtes 7 étapes plus loin vers l'excellence. Entraînez votre cerveau et vos muscles avec les exercices suivants.

## 💻 Exercices : Jour 7

```py
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Exercices : Niveau 1

1. Trouvez la longueur de l'ensemble it_companies
2. Ajoutez 'Twitter' à it_companies
3. Insérez plusieurs entreprises informatiques à la fois dans l'ensemble it_companies
4. Supprimez l'une des entreprises de l'ensemble it_companies
5. Quelle est la différence entre remove et discard

### Exercices : Niveau 2

1. Joignez A et B
2. Trouvez l'intersection de A et B
3. A est-il un sous-ensemble de B
4. A et B sont-ils des ensembles disjoints
5. Joignez A avec B et B avec A
6. Quelle est la différence symétrique entre A et B
7. Supprimez complètement les ensembles

### Exercices : Niveau 3

1. Convertissez les âges en un ensemble et comparez la longueur de la liste et celle de l'ensemble. Laquelle est plus grande ?
2. Expliquez la différence entre les types de données suivants : string, list, tuple et set
3. _I am a teacher and I love to inspire and teach people._ Combien de mots uniques ont été utilisés dans cette phrase ? Utilisez les méthodes split et set pour obtenir les mots uniques.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 6](./06_tuples_fr.md) | [Jour 8 >>](./08_dictionaries_fr.md)

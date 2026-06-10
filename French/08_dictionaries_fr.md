<div align="center">
  <h1> 30 Jours de Python : Jour 8 - Dictionnaires</h1>
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

[<< Jour 7](./07_sets_fr.md) | [Jour 9 >>](./09_conditionals_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 8](#-jour-8)
  - [Dictionnaires](#dictionnaires)
    - [Créer un dictionnaire](#créer-un-dictionnaire)
    - [Longueur d'un dictionnaire](#longueur-dun-dictionnaire)
    - [Accéder aux éléments d'un dictionnaire](#accéder-aux-éléments-dun-dictionnaire)
    - [Ajouter des éléments à un dictionnaire](#ajouter-des-éléments-à-un-dictionnaire)
    - [Modifier des éléments dans un dictionnaire](#modifier-des-éléments-dans-un-dictionnaire)
    - [Vérifier les clés dans un dictionnaire](#vérifier-les-clés-dans-un-dictionnaire)
    - [Supprimer des paires clé-valeur d'un dictionnaire](#supprimer-des-paires-clé-valeur-dun-dictionnaire)
    - [Convertir un dictionnaire en une liste d'éléments](#convertir-un-dictionnaire-en-une-liste-déléments)
    - [Vider un dictionnaire](#vider-un-dictionnaire)
    - [Supprimer un dictionnaire](#supprimer-un-dictionnaire)
    - [Copier un dictionnaire](#copier-un-dictionnaire)
    - [Obtenir les clés d'un dictionnaire sous forme de liste](#obtenir-les-clés-dun-dictionnaire-sous-forme-de-liste)
    - [Obtenir les valeurs d'un dictionnaire sous forme de liste](#obtenir-les-valeurs-dun-dictionnaire-sous-forme-de-liste)
  - [💻 Exercices : Jour 8](#-exercices--jour-8)

# 📘 Jour 8

## Dictionnaires

Un dictionnaire est une collection de données non ordonnées, modifiables (mutable), sous forme de paires (clé : valeur).

### Créer un dictionnaire

Pour créer un dictionnaire, nous utilisons des accolades {} ou la fonction intégrée *dict()*.

```py
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
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
```

Le dictionnaire ci-dessus montre qu'une valeur peut être de n'importe quel type de données : chaîne, booléen, liste, tuple, ensemble ou un dictionnaire.

### Longueur d'un dictionnaire

Il vérifie le nombre de paires 'clé : valeur' dans le dictionnaire.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Exemple :**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

```

### Accéder aux éléments d'un dictionnaire

Nous pouvons accéder aux éléments d'un dictionnaire par son nom de clé.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
```

Accéder à un élément par son nom de clé génère une erreur si la clé n'existe pas. Pour éviter cette erreur, nous devons d'abord vérifier si une clé existe, ou nous pouvons utiliser la méthode _get_. La méthode get retourne None, qui est un objet de type NoneType, si la clé n'existe pas.

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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### Ajouter des éléments à un dictionnaire

Nous pouvons ajouter de nouvelles paires clé-valeur à un dictionnaire.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

### Modifier des éléments dans un dictionnaire

Nous pouvons modifier des éléments dans un dictionnaire.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### Vérifier les clés dans un dictionnaire

Nous utilisons l'opérateur _in_ pour vérifier si une clé existe dans un dictionnaire.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Supprimer des paires clé-valeur d'un dictionnaire

- _pop(key)_ : supprime l'élément avec le nom de clé spécifié.
- _popitem()_ : supprime le dernier élément.
- _del_ : supprime un élément avec le nom de clé spécifié.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # supprime l'élément key1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # supprime le dernier élément
del dct['key2'] # supprime l'élément key2
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
person.pop('first_name')        # Supprime l'élément first_name
person.popitem()                # Supprime l'élément address
del person['is_marred']        # Supprime l'élément is_marred
```

### Convertir un dictionnaire en une liste d'éléments

La méthode _items()_ transforme un dictionnaire en une liste de tuples.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Vider un dictionnaire

Si nous souhaitons vider un dictionnaire, nous pouvons utiliser la méthode _clear()_.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Supprimer un dictionnaire

Si nous n'utilisons plus le dictionnaire, nous pouvons le supprimer complètement.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copier un dictionnaire

Nous pouvons copier un dictionnaire en utilisant la méthode _copy()_. Utiliser copy nous évite de muter le dictionnaire d'origine.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Obtenir les clés d'un dictionnaire sous forme de liste

La méthode _keys()_ nous donne toutes les clés d'un dictionnaire sous forme de liste.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Obtenir les valeurs d'un dictionnaire sous forme de liste

La méthode _values()_ nous donne toutes les valeurs d'un dictionnaire sous forme de liste.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 Vous êtes incroyable. Vous voilà paré du pouvoir des dictionnaires. Vous venez de terminer les défis du jour 8 et vous êtes 8 étapes plus loin vers l'excellence. Entraînez votre cerveau et vos muscles avec les exercices suivants.

## 💻 Exercices : Jour 8

1. Créez un dictionnaire vide appelé dog
2. Ajoutez les clés name, color, breed, legs, age au dictionnaire dog
3. Créez un dictionnaire student et ajoutez first_name, last_name, gender, age, marital status, skills, country, city et address comme clés du dictionnaire
4. Obtenez la longueur du dictionnaire student
5. Obtenez la valeur de skills et vérifiez le type de données, il devrait s'agir d'une liste
6. Modifiez les valeurs de skills en ajoutant une ou deux compétences
7. Obtenez les clés du dictionnaire sous forme de liste
8. Obtenez les valeurs du dictionnaire sous forme de liste
9. Convertissez le dictionnaire en une liste de tuples avec la méthode _items()_
10. Supprimez l'un des éléments du dictionnaire
11. Supprimez l'un des dictionnaires

🎉 FÉLICITATIONS ! 🎉

[<< Jour 7](./07_sets_fr.md) | [Jour 9 >>](./09_conditionals_fr.md)

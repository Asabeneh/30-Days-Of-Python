<div align="center">
  <h1> 30 Jours de Python : Jour 21 - Classes et Objets</h1>
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

[<< Jour 20](./20_python_package_manager_fr.md) | [Jour 22 >>](./22_web_scraping_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 21](#-jour-21)
  - [Classes et Objets](#classes-et-objets)
    - [Créer une classe](#créer-une-classe)
    - [Créer un objet](#créer-un-objet)
    - [Constructeur de classe](#constructeur-de-classe)
    - [Méthodes d'objet](#méthodes-dobjet)
    - [Méthodes par défaut d'un objet](#méthodes-par-défaut-dun-objet)
    - [Méthode pour modifier les valeurs par défaut d'une classe](#méthode-pour-modifier-les-valeurs-par-défaut-dune-classe)
    - [Héritage](#héritage)
    - [Surcharge de la méthode parente](#surcharge-de-la-méthode-parente)
  - [💻 Exercices : Jour 21](#-exercices-jour-21)
    - [Exercices : Niveau 1](#exercices-niveau-1)
    - [Exercices : Niveau 2](#exercices-niveau-2)
    - [Exercices : Niveau 3](#exercices-niveau-3)

# 📘 Jour 21

## Classes et Objets

Python est un langage de programmation orientée objet. Tout en Python est un objet, avec ses propriétés et ses méthodes. Un nombre, une chaîne, une liste, un dictionnaire, un tuple, un ensemble, etc. utilisés dans un programme sont des objets d'une classe intégrée correspondante. Nous créons une classe pour créer un objet. Une classe est comme un constructeur d'objet, ou un « plan » pour créer des objets. Nous instancions une classe pour créer un objet. La classe définit les attributs et le comportement de l'objet, tandis que l'objet, quant à lui, représente la classe.

Nous avons travaillé avec des classes et des objets depuis le début de ce défi sans le savoir. Chaque élément d'un programme Python est un objet d'une classe.
Vérifions si tout en Python est une classe :

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### Créer une classe

Pour créer une classe, nous avons besoin du mot-clé **class** suivi du nom et de deux-points. Le nom de la classe doit être en **CamelCase**.

```sh
# syntaxe
class NomClasse:
  le code va ici
```

**Exemple :**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### Créer un objet

Nous pouvons créer un objet en appelant la classe.

```py
p = Person()
print(p)
```

### Constructeur de classe

Dans les exemples ci-dessus, nous avons créé un objet à partir de la classe Person. Cependant, une classe sans constructeur n'est pas vraiment utile dans les applications réelles. Utilisons une fonction constructeur pour rendre notre classe plus utile. Comme la fonction constructeur en Java ou JavaScript, Python a aussi une fonction constructeur intégrée **__init__**(). La fonction constructeur **__init__** a un paramètre self qui est une référence à l'instance actuelle de la classe.

**Exemples :**

```py
class Person:
      def __init__ (self, name):
        # self permet d'attacher un paramètre à la classe
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# sortie
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

Ajoutons plus de paramètres à la fonction constructeur.

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# sortie
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### Méthodes d'objet

Les objets peuvent avoir des méthodes. Les méthodes sont des fonctions qui appartiennent à l'objet.

**Exemple :**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} a {self.age} ans. Il habite à {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# sortie
Asabeneh Yetayeh a 250 ans. Il habite à Helsinki, Finland
```

### Méthodes par défaut d'un objet

Parfois, vous pouvez vouloir avoir des valeurs par défaut pour les méthodes de votre objet. Si nous donnons des valeurs par défaut aux paramètres du constructeur, nous pouvons éviter les erreurs lorsque nous appelons ou instancions notre classe sans paramètres. Voyons à quoi cela ressemble :

**Exemple :**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} a {self.age} ans. Il habite à {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# sortie
Asabeneh Yetayeh a 250 ans. Il habite à Helsinki, Finland.
John Doe a 30 ans. Il habite à Noman city, Nomanland.
```

### Méthode pour modifier les valeurs par défaut d'une classe

Dans l'exemple ci-dessous, la classe Person a toutes les valeurs par défaut pour les paramètres du constructeur. En plus de cela, nous avons un paramètre skills, auquel nous pouvons accéder via une méthode. Créons une méthode add_skill pour ajouter des compétences à la liste skills.

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} a {self.age} ans. Il habite à {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# sortie
Asabeneh Yetayeh a 250 ans. Il habite à Helsinki, Finland.
John Doe a 30 ans. Il habite à Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Héritage

Grâce à l'héritage, nous pouvons réutiliser le code de la classe parente. L'héritage nous permet de définir une classe qui hérite de toutes les méthodes et propriétés de la classe parente. La classe parente, superclasse ou classe de base est la classe qui fournit toutes les méthodes et propriétés. La classe enfant est la classe qui hérite d'une autre classe ou d'une classe parente.
Créons une classe Student en héritant de la classe Person.

```py
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

```sh
sortie
Eyob Yetayeh a 30 ans. Il habite à Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam a 28 ans. Il habite à Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Nous n'avons pas appelé le constructeur **__init__**() dans la classe enfant. Si nous ne l'appelons pas, nous pouvons toujours accéder à toutes les propriétés du parent. Mais si nous appelons le constructeur, nous pouvons accéder aux propriétés du parent en appelant _super_.
Nous pouvons ajouter une nouvelle méthode à l'enfant ou nous pouvons surcharger les méthodes de la classe parente en créant le même nom de méthode dans la classe enfant. Lorsque nous ajoutons la fonction **__init__**(), la classe enfant n'héritera plus de la fonction **__init__**() du parent.

### Surcharge de la méthode parente

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'Il' if self.gender == 'male' else 'Elle'
        return f'{self.firstname} {self.lastname} a {self.age} ans. {gender} habite à {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
Eyob Yetayeh a 30 ans. Il habite à Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam a 28 ans. Elle habite à Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Nous pouvons utiliser la fonction intégrée super() ou le nom du parent Person pour hériter automatiquement des méthodes et propriétés de son parent. Dans l'exemple ci-dessus, nous avons surchargé la méthode parente. La méthode enfant a une fonctionnalité différente, elle peut identifier si le genre est masculin ou féminin et assigner le pronom approprié (Il/Elle).

🌕 Maintenant, vous êtes pleinement chargé d'un super pouvoir de programmation. Faites maintenant quelques exercices pour votre cerveau et vos muscles.

## 💻 Exercices : Jour 21

### Exercices : Niveau 1

1. Python a un module appelé _statistics_ et nous pouvons utiliser ce module pour faire tous les calculs statistiques. Cependant, pour apprendre à créer des fonctions et à les réutiliser, essayons de développer un programme qui calcule les mesures de tendance centrale d'un échantillon (moyenne, médiane, mode) et les mesures de variabilité (étendue, variance, écart type). En plus de ces mesures, trouvez le min, max, count, percentile et la distribution de fréquence de l'échantillon. Vous pouvez créer une classe appelée Statistics et créer toutes les fonctions qui effectuent les calculs statistiques en tant que méthodes de la classe Statistics. Vérifiez la sortie ci-dessous.

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# votre sortie devrait ressembler à ceci
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### Exercices : Niveau 2

1. Créez une classe appelée PersonAccount. Elle a les propriétés firstname, lastname, incomes, expenses et les méthodes total_income, total_expense, account_info, add_income, add_expense et account_balance. Incomes est un ensemble de revenus et leurs descriptions. Il en va de même pour expenses.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 20](./20_python_package_manager_fr.md) | [Jour 22 >>](./22_web_scraping_fr.md)

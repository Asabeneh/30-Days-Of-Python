<div align="center">
  <h1> 30 Days Of Python: День 21 - Классы и объекты</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Второе издание: июль 2021</small>
</sub>

</div>

[<< День 20](./20_python_package_manager_ru.md) | [День 22 >>](./22_web_scraping_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 21](#-день-21)
  - [Классы и объекты](#классы-и-объекты)
    - [Создание класса](#создание-класса)
    - [Создание объекта](#создание-объекта)
    - [Конструктор класса](#конструктор-класса)
    - [Методы объекта](#методы-объекта)
    - [Методы объекта по умолчанию](#методы-объекта-по-умолчанию)
    - [Метод для изменения значений класса по умолчанию](#метод-для-изменения-значений-класса-по-умолчанию)
    - [Наследование](#наследование)
    - [Переопределение метода родителя](#переопределение-метода-родителя)
  - [💻 Упражнения: День 21](#-упражнения-день-21)
    - [Упражнения: Уровень 1](#упражнения-уровень-1)
    - [Упражнения: Уровень 2](#упражнения-уровень-2)
    - [Упражнения: Уровень 3](#упражнения-уровень-3)

# 📘 День 21

## Классы и объекты

Python — объектно-ориентированный язык программирования. Всё в Python является объектом со своими свойствами и методами. Число, строка, список, словарь, кортеж, множество и т. д., используемые в программе, являются объектом соответствующего встроенного класса. Мы создаём класс, чтобы создать объект. Класс похож на конструктор объектов или «чертёж» для создания объектов. Мы создаём экземпляр класса, чтобы создать объект. Класс определяет атрибуты и поведение объекта, а объект, в свою очередь, представляет класс.

Мы работали с классами и объектами с самого начала этого испытания, сами того не зная. Каждый элемент в программе на Python является объектом класса.
Давайте проверим, всё ли в Python является классом:

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

### Создание класса

Чтобы создать класс, нам нужно ключевое слово **class**, за которым следуют имя и двоеточие. Имя класса должно быть в **CamelCase**.

```sh
# синтаксис
class ClassName:
  здесь код
```

**Пример:**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### Создание объекта

Мы можем создать объект, вызвав класс.

```py
p = Person()
print(p)
```

### Конструктор класса

В примерах выше мы создали объект из класса Person. Однако класс без конструктора не очень полезен в реальных приложениях. Давайте используем функцию-конструктор, чтобы сделать наш класс более полезным. Как и функция-конструктор в Java или JavaScript, в Python тоже есть встроенная функция-конструктор **__init__**(). У функции-конструктора **__init__** есть параметр self, который является ссылкой на текущий экземпляр класса
**Примеры:**

```py
class Person:
      def __init__ (self, name):
        # self позволяет прикрепить параметр к классу
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# вывод
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

Давайте добавим больше параметров в функцию-конструктор.

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
# вывод
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### Методы объекта

Объекты могут иметь методы. Методы — это функции, которые принадлежат объекту.

**Пример:**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# вывод
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

### Методы объекта по умолчанию

Иногда вам может понадобиться иметь значения по умолчанию для методов объекта. Если мы зададим значения по умолчанию для параметров в конструкторе, мы сможем избежать ошибок, когда вызываем или создаём экземпляр нашего класса без параметров. Давайте посмотрим, как это выглядит:

**Пример:**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# вывод
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

### Метод для изменения значений класса по умолчанию

В примере ниже в классе person все параметры конструктора имеют значения по умолчанию. Кроме того, у нас есть параметр skills, к которому мы можем получить доступ с помощью метода. Давайте создадим метод add_skill, чтобы добавлять навыки в список skills.

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
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
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
# вывод
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Наследование

Используя наследование, мы можем повторно использовать код родительского класса. Наследование позволяет нам определить класс, который наследует все методы и свойства от родительского класса. Родительский класс, или суперкласс, или базовый класс — это класс, который предоставляет все методы и свойства. Дочерний класс — это класс, который наследует от другого или родительского класса.
Давайте создадим класс student, унаследовав его от класса person.

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
вывод
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Мы не вызывали конструктор **__init__**() в дочернем классе. Если мы его не вызывали, то всё равно можем получить доступ ко всем свойствам родителя. Но если мы вызываем конструктор, мы можем получить доступ к свойствам родителя, вызвав _super_.  
Мы можем добавить новый метод в дочерний класс или переопределить методы родительского класса, создав метод с тем же именем в дочернем классе. Когда мы добавляем функцию **__init__**(), дочерний класс больше не наследует функцию **__init__**() родителя.

### Переопределение метода родителя

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

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
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Мы можем использовать встроенную функцию super() или имя родителя Person, чтобы автоматически наследовать методы и свойства от его родителя. В примере выше мы переопределяем метод родителя. Дочерний метод имеет другую особенность: он может определить, является ли пол мужским или женским, и назначить подходящее местоимение (He/She).

🌕 Теперь вы полностью заряжены суперспособностью программирования. Теперь сделайте несколько упражнений для мозга и мышц.

## 💻 Упражнения: День 21

### Упражнения: Уровень 1

1. В Python есть модуль _statistics_, и мы можем использовать этот модуль для всех статистических вычислений. Однако, чтобы научиться создавать функции и повторно использовать функции, давайте попробуем разработать программу, которая вычисляет меры центральной тенденции выборки (среднее, медиану, моду) и меры разброса (размах, дисперсию, стандартное отклонение). В дополнение к этим мерам найдите минимум, максимум, количество, процентиль и распределение частот выборки. Вы можете создать класс Statistics и создать все функции, выполняющие статистические вычисления, как методы класса Statistics. Проверьте вывод ниже.

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
# ваш вывод должен выглядеть так
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

### Упражнения: Уровень 2

1. Создайте класс с именем PersonAccount. У него есть свойства firstname, lastname, incomes, expenses и методы total_income, total_expense, account_info, add_income, add_expense и account_balance. Incomes — это набор доходов и их описаний. То же самое касается расходов.

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 20](./20_python_package_manager_ru.md) | [День 22 >>](./22_web_scraping_ru.md)

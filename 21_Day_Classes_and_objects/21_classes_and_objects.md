<div align="center">
  <h1> 30 Days Of Python: Day 21 - Classes and Objects</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 20](../20_Day_Python_package_manager/20_python_package_manager.md) | [Day 22 >>](../22_Day_Web_scraping/22_web_scraping.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 21](#-day-21)
  - [Classes and Objects](#classes-and-objects)
    - [Creating a Class](#creating-a-class)
    - [បង្កើត object](#បង្កើត-object)
    - [Class Constructor](#class-constructor)
    - [Object Methods](#object-methods)
    - [Object Default Methods](#object-default-methods)
    - [វិធីសាស្ត្រដើម្បីកែប្រែតម្លៃ default របស់ class](#វិធីសាស្ត្រដើម្បីកែប្រែតម្លៃ-default-របស់-class)
    - [Inheritance](#inheritance)
    - [Overriding parent method](#overriding-parent-method)

# 📘 Day 21

## Classes and Objects
Python គឺជា ភាសា កម្មវិធី ដែល មាន គោលដៅ ទៅលើ object ។ គ្រប់យ៉ាងនៅក្នុង Python គឺជាobjectមួយ ដែលមានលក្ខណៈសម្បត្តិ និងវិធីសាស្ត្ររបស់ខ្លួន។ ចំនួន, string, list, dictionary, tuple, set ជាដើម ដែលប្រើនៅក្នុងកម្មវិធី គឺជា object របស់ class ដែលបានបង្កើតឡើង។ យើងបង្កើត class ដើម្បីបង្កើត object កម្រិត គឺដូចជា object constructor ឬ " blueprint" សម្រាប់បង្កើត object ។ យើងបង្កើត class ដើម្បីបង្កើត object កម្រិតកំណត់លក្ខណៈសម្បត្តិ និងអាកប្បកិរិយារបស់វត្ថុ ខណៈដែលobjectវិញតំណាងឱ្យកម្រិត។

យើងបានធ្វើការជាមួយថ្នាក់ និងវត្ថុ តាំងពីដើមនៃការប្រឈមនេះ ដោយមិនដឹងខ្លួន គ្រប់អេឡិចត្រូនិកនៅក្នុងកម្មវិធី Python គឺជាអាវយឺតនៃថ្នាក់។
សូមយើងពិនិត្យមើលថាតើអ្វីគ្រប់យ៉ាងនៅក្នុង Python គឺជា class ឬទេ:
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

### Creating a Class

ដើម្បីបង្កើត class យើងត្រូវការពាក្យ Keyword **class** តាមក្រោយឈ្មោះ និង colon ។ ឈ្មោះថ្នាក់រៀនគួរជា **CamelCase**។

```sh
# syntax
class ClassName:
  code goes here
```

**Example:**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### បង្កើត object

យើងអាចបង្កើត object ដោយហៅ class

```py
p = Person()
print(p)
```

### Class Constructor

នៅក្នុងឧទាហរណ៍ខាងលើនេះ យើងបានបង្កើត object ពី class Person ។ ទោះបីជាយ៉ាងណាក៏ដោយ, កម្រិតដែលគ្មាន constructor មិនសូវមានប្រយោជន៍នៅក្នុងកម្មវិធីពិតទេ។ យើងត្រូវប្រើកម្រិត constructor ដើម្បីធ្វើឱ្យ class របស់យើងមានប្រសិទ្ធភាព។ ដូច Function constructor ក្នុង Java ឬ JavaScript Python ក៏មាន Function constructor ****init****() ដែលត្រូវបានបង្កើតឡើងផងដែរ ។ តួនាទី constructor ****init**** មាន self parameter ដែលជាការអត្ថាធិប្បាយទៅនឹងករណីបច្ចុប្បន្ននៃថ្នាក់

**Examples:**

```py
class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# output
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

សូមយើងបន្ថែម parameter បន្ថែមទៀតទៅលើ function constructor ។
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
# output
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### Object Methods

វត្ថុអាចមានវិធីសាស្ត្រ។ វិធីសាស្រ្ត គឺជាមុខងារដែលជារបស់វត្ថុ។

**Example:**

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
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

### Object Default Methods

ពេលខ្លះ, អ្នកប្រហែលជាចង់មានតម្លៃ default សម្រាប់វិធីសាស្រ្តរបស់ object របស់អ្នក។ ប្រសិន បើ យើង ផ្តល់ តម្លៃ ជា ធម្មតា សម្រាប់ Parameters ក្នុង constructor យើង អាច ជៀសវាង កំហុស នៅពេល ដែល យើង ហៅ ឬ បង្កើត instance របស់ class ដោយ គ្មាន Parameters ។ សូមមើលថាវាមើលទៅដូចម្ដេច:

**Example:**

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
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

### វិធីសាស្ត្រដើម្បីកែប្រែតម្លៃ default របស់ class

នៅក្នុងឧទាហរណ៍ខាងក្រោម, មនុស្សថ្នាក់, គ្រប់គំរូ constructor មានតម្លៃជាមុនសិន។ ក្រៅពីនេះយើងមានសមត្ថភាពដែលយើងអាចចូលទៅកាន់ដោយប្រើវិធីសាស្ត្រ។ សូមយើងបង្កើត add_skill method ដើម្បីបន្ថែម skills ទៅក្នុងបញ្ជី skills

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
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Inheritance

ដោយប្រើ inheritance យើងអាចប្រើឡើងវិញកូដថ្នាក់ឪពុក ការទទួលកេរដំណែលអនុញ្ញាតឱ្យយើងកំណត់លំដាប់ដែលទទួលកេរដំណែលគ្រប់មធ្យោបាយ និងលក្ខណៈសម្បត្តិពីលំដាប់ឪពុកម្តាយ។ កម្រិតមេ ឬ super ឬ base class គឺជាកម្រិតដែលផ្តល់នូវវិធីសាស្ត្រ និងលក្ខណៈសម្បត្តិទាំងអស់។ Child class គឺជា class ដែលទទួលយកពី class ផ្សេង ឬ parent class ។
សូមយើងបង្កើតclassសិស្ស ដោយទទួលយកពីclassមនុស្ស។

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
output
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

យើងមិនបានហៅ constructor ****init****( នៅក្នុង child class ទេ បើសិនជាយើងមិនហៅវាទេ យើងនៅតែអាចចូលទៅកាន់លក្ខណៈសម្បត្តិទាំងអស់parent class។ ប៉ុន្តែបើយើងហៅ constructor យើងអាចចូលទៅកាន់ properties parent ដោយហៅ _super_
យើងអាចបន្ថែមមធ្យោបាយថ្មីទៅលើកូន ឬយើងអាច override មធ្យោបាយថ្នាក់មេ ដោយបង្កើតឈ្មោះមធ្យោបាយដូចគ្នានៅក្នុងថ្នាក់កូន។ When we add the ****init****() function, the child class will no longer inherit the parent's ****init****() function.

### Overriding parent method

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
យើងអាចប្រើ super() built-in function ឬឈ្មោះឪពុកម្តាយ Person ដើម្បីទទួលយកលក្ខណៈសម្បត្តិ និងវិធីសាស្ត្រពីparentរបស់វា។ នៅក្នុងឧទាហរណ៍ខាងលើយើង override វិធីសាស្ត្រparent។ វិធីសាស្ត្រកូនមានលក្ខណៈខុសគ្នាវាអាចកំណត់ថា តើភេទជាប្រុសឬស្រី ហើយកំណត់ពាក្យចាត់ទុកដែលសមរម្យ (He/She) ។




🎉 CONGRATULATIONS ! 🎉

[<< Day 20](../20_Day_Python_package_manager/20_python_package_manager.md) | [Day 22 >>](../22_Day_Web_scraping/22_web_scraping.md)

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
  <small> First Edition: Nov 22 - Dec 22, 2019</small>
  </sub>
</div>
</div>

[<< Day 20](../20_Day/20_python_package_manager.md) | [Day 22 >>](../22_Day/22_web_scraping.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 21](#%f0%9f%93%98-day-21)
  - [Classes and Objects](#classes-and-objects)
    - [Creating a Class](#creating-a-class)
    - [Creating an Object](#creating-an-object)
    - [Class Constructor](#class-constructor)
    - [Object Methods](#object-methods)
    - [Object default methods](#object-default-methods)
    - [Method to modify class default values](#method-to-modify-class-default-values)
    - [Inheritance](#inheritance)
    - [Overriding parent method](#overriding-parent-method)
  - [💻 Exercises: Day 21](#%f0%9f%92%bb-exercises-day-21)

# 📘 Day 21

## Classes and Objects

Python is an object oriented programming language. Everything in Python is an object, with its properties and methods. A number, string, list, dictionary,tuple, set etc. used in a program is an object of a corresponding built-in class. We create class to create an object. A Class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.

We have been working with classes and objects right from the beginning of these challenge unknowingly. Every element in a Python program is an object of a class.
Let's check if everything in python is class:

```py
Last login: Tue Dec 10 09:35:28 on console
asabeneh@Asabeneh:~$ pyhton
-bash: pyhton: command not found
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
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

To create a class we need the key word **class** followed by colon. Class name should be **CamelCase**.

```sh
# syntax
class ClassName:
  code goes here
```

**Example:**

```py
class Person:
  pass
```

```sh
<__main__.Person object at 0x10804e510>
```

### Creating an Object

We can create an object by calling the class.

```py
p = Person()
print(p)
```

### Class Constructor

In the above examples, we have created an object from the Person class. However, Class without a constructor is not really useful in real applications. Let's use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, python has also a builtin _**init**()_ constructor function. The _**init**_ constructor function has self parameter which is a reference to the current instance of the class
**Examples:**

```py
class Person:
      def __init__ (self, name):
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# output
Asabeneh
```

Let's add more parameter to the constructor function.

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

Objects can have methods. The methods are functions which are belongs to the object.
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
        return f'{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}, {self.country}'


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# output
Asabeneh Yetayeh is 250 year old. He lives in Helsinki, Finland
```

### Object default methods

Sometimes, you may want to have a default values for you object methods. If we give a default values for the parameters in the constructor, we can avoid error when we call or instantiate our class without parameters. Let's see how it looks using example.

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
        return f'{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# output
Asabeneh Yetayeh is 250 year old. He lives in Helsinki, Finland.
John Doe is 30 year old. He lives in Noman city, Nomanland.
```

### Method to modify class default values

In the example below, the person class, all the constructor parameters have default values and in addition to that we have a skills default value which we can access it using method. Let's create add_skill method to add skill to the skills list.

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
        return f'{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}, {self.country}.'
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
Asabeneh Yetayeh is 250 year old. He lives in Helsinki, Finland.
John Doe is 30 year old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Inheritance

Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from another class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class the inherits from another class.
Let's see create a student class by inheriting from person class.

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
Eyob Yetayeh is 30 year old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 year old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

We didn't call the _**init**()_ constructor in the child class. If we didn't call it we can access all the properties but if we call it once we access the parent properties by calling _super_.  
We can write add a new method to the child or we can overwrite the parent class by creating the same method name in the child class. When we add the **init**() function, the child class will no longer inherit the parent's **init**() function.

### Overriding parent method

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} year old. {gender} lives in {self.city}, {self.country}.'

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
Eyob Yetayeh is 30 year old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 year old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

We can use super() function or the parent name Person to automatically inherit the methods and properties from its parent. In the above example, we override the parant method. The child method has a different feature, it can identify if the gender is male or female and assign the proper pronoun(He/She).

## 💻 Exercises: Day 21

1. Python has the module called _statistics_ and we can use this module to do all the statistical caluculations. Hower to challlenge ourselves, let's try to develop a program which calculate measure of central tendency of a sample(mean, median, mode) and measure of variability(range, variance, standard deviation). In addition to those measures find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions which do statistical calculations as method for the Statistics class. Check the output below.

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ',data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Variance: ',data.var()) # 17.5
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ',data.var()) # 17.5
print('Frequency Distribution: ',data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# you output should look like this
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
1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info,add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description and the same goes for expenses.
   

🎉 CONGRATULATIONS ! 🎉

[<< Day 20](../20_Day/20_python_package_manager.md) | [Day 22 >>](../22_Day/22_web_scraping.md)
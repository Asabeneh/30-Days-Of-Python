# 30天Python编程挑战：第21天 - 类和对象

- [第21天](#-第21天)
  - [类和对象](#类和对象)
    - [创建类](#创建类)
    - [创建对象](#创建对象)
    - [类构造函数](#类构造函数)
    - [对象方法](#对象方法)
    - [对象默认方法](#对象默认方法)
    - [修改类默认值的方法](#修改类默认值的方法)
    - [继承](#继承)
    - [覆盖父类方法](#覆盖父类方法)
  - [💻 练习：第21天](#-练习第21天)
    - [练习：级别1](#练习级别1)
    - [练习：级别2](#练习级别2)
    - [练习：级别3](#练习级别3)

# 📘 第21天

## 类和对象

Python是一种面向对象的编程语言。在Python中，一切都是对象，都有其属性和方法。在程序中使用的数字、字符串、列表、字典、元组、集合等都是相应内置类的对象。我们创建类来创建对象。类就像一个对象构造器，或者说是创建对象的"蓝图"。我们实例化一个类来创建一个对象。类定义了对象的属性和行为，而对象则代表了类。

从这个挑战的开始，我们就一直在不知不觉地使用类和对象。Python程序中的每个元素都是某个类的对象。
让我们检查一下Python中的一切是否都是类：

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

### 创建类

要创建一个类，我们需要关键字**class**，后跟类名和冒号。类名应该使用**驼峰命名法（CamelCase）**。

```sh
# 语法
class 类名:
  代码放在这里
```

**示例：**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### 创建对象

我们可以通过调用类来创建对象。

```py
p = Person()
print(p)
```

### 类构造函数

在上面的例子中，我们已经从Person类创建了一个对象。然而，没有构造函数的类在实际应用中并不真正有用。让我们使用构造函数使我们的类更有用。与Java或JavaScript中的构造函数一样，Python也有一个内置的**__init__**()构造函数。**__init__**构造函数有一个self参数，它是当前类实例的引用。
**示例：**

```py
class Person:
      def __init__ (self, name):
        # self允许将参数附加到类
          self.name = name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# 输出
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

让我们向构造函数添加更多参数。

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
# 输出
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### 对象方法

对象可以有方法。方法是属于对象的函数。

**示例：**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# 输出
Asabeneh Yetayeh今年250岁。他住在Finland的Helsinki。
```

### 对象默认方法

有时，你可能希望为对象方法提供默认值。如果我们为构造函数中的参数提供默认值，可以避免在不带参数调用或实例化类时出现错误。让我们看看这是什么样子：

**示例：**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# 输出
Asabeneh Yetayeh今年250岁。他住在Finland的Helsinki。
John Doe今年30岁。他住在Nomanland的Noman city。
```

### 修改类默认值的方法

在下面的例子中，person类的所有构造函数参数都有默认值。此外，我们还有一个skills参数，可以通过方法访问。让我们创建一个add_skill方法，向skills列表添加技能。

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
        return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'
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
# 输出
Asabeneh Yetayeh今年250岁。他住在Finland的Helsinki。
John Doe今年30岁。他住在Nomanland的Noman city。
['HTML', 'CSS', 'JavaScript']
[]
```

### 继承

继承允许我们定义一个继承父类所有功能的类。它使代码可重用。

```py
# 语法
class 子类名(父类名):
    代码放在这里
```

让我们通过实际例子来看看继承的含义：

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
# 输出
Eyob Yetayeh今年30岁。他住在Finland的Helsinki。
['JavaScript', 'React', 'Python']
Lidiya Teklemariam今年28岁。他住在Finland的Espoo。
['Organizing', 'Marketing', 'Digital Marketing']
```

我们没有在Student类中调用任何方法，但我们能够访问来自Parent类的所有方法。Student类继承了Person类的__init__构造函数和person_info方法。如果我们想要向子类添加一个特定于子类的新方法，我们必须编写子类并在子类中创建新的方法。

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = '他' if self.gender =='male' else '她'
        return f'{self.firstname} {self.lastname}今年{self.age}岁。{gender}住在{self.country}的{self.city}。'


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
# 输出
Eyob Yetayeh今年30岁。他住在Finland的Helsinki。
['JavaScript', 'React', 'Python']
Lidiya Teklemariam今年28岁。她住在Finland的Espoo。
['Organizing', 'Marketing', 'Digital Marketing']
```

我们可以使用super()函数或父类名Person来自动继承父类的方法和属性。在上面的例子中，我们覆盖了父类方法。子类的person_info方法有不同的实现，即使方法名称与父类相同。

### 覆盖父类方法

如上所示，我们可以通过创建与父类方法名称相同的子类方法来覆盖父类方法。

## 💻 练习：第21天

### 练习：级别1

1. Python有一个名为_statistics_的模块，我们可以使用这个模块来计算统计数据。但是，让我们尝试开发一个可以计算均值、中位数、众数、标准差等统计数据的类。
  
```py
class Statistics:
    def __init__(self, data=[]):
        self.data = data

    def count(self):
        # 你自己的实现
        pass
    
    def sum(self):
        # 你自己的实现
        pass
    
    def min(self):
        # 你自己的实现
        pass
    
    def max(self):
        # 你自己的实现
        pass
    
    def range(self):
        # 你自己的实现
        pass
    
    def mean(self):
        # 你自己的实现
        pass
    
    def median(self):
        # 你自己的实现
        pass
    
    def mode(self):
        # 你自己的实现
        pass
    
    def standard_deviation(self):
        # 你自己的实现
        pass
    
    def variance(self):
        # 你自己的实现
        pass
    
    def frequency_distribution(self):
        # 你自己的实现
        pass
    
    def describe(self):
        # 你自己的实现
        pass
```

```py
# 测试代码
data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
statistics = Statistics(data)
print('Count:', statistics.count()) # 25
print('Sum: ', statistics.sum()) # 730
print('Min: ', statistics.min()) # 24
print('Max: ', statistics.max()) # 38
print('Range: ', statistics.range()) # 14
print('Mean: ', statistics.mean()) # 29.2
print('Median: ', statistics.median()) # 27
print('Mode: ', statistics.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', statistics.standard_deviation()) # 4.2
print('Variance: ', statistics.variance()) # 17.5
print('Frequency Distribution: ', statistics.frequency_distribution()) # [(24, 2), (25, 1), (26, 5), (27, 4), (29, 1), (31, 2), (32, 3), (33, 2), (34, 2), (37, 2), (38, 1)]
```

### 练习：级别2

1. 创建一个名为PersonAccount的类。它有firstname、lastname、incomes、expenses属性和添加收入、添加支出以及账户余额方法。

### 练习：级别3

1. 以下是使用函数的方法。让我们将其转换为类
   
```python
def print_products(*args, **kwargs):
    for product in args:
        print(product)
    print(kwargs)
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

print_products("apple", "banana", "orange", vegetable="tomato", juice="orange")
```

```sh
apple
banana
orange
{'vegetable': 'tomato', 'juice': 'orange'}
vegetable: tomato
juice: orange
```

1. 在一个名为PersonAccount的类中，我们有属性：firstname、lastname、incomes、expenses。设计一个类，用于计算一个人的净收入。

🎉 恭喜！🎉

[<< 第 20 天](./20_python_package_manager_cn.md) | [第 22 天 >>](./22_web_scraping_cn.md) 
<div align="center">
  <h1> 30 Days Of Python: Day 14 - Higher Order Functions</h1>
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
</div>

[<< Day 13](../13_Day_List_comprehension/13_list_comprehension.md) | [Day 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 14](#-day-14)
  - [Higher Order Functions](#higher-order-functions)
    - [Function as a Parameter](#function-as-a-parameter)
    - [Function as a Return Value](#function-as-a-return-value)
  - [Python Closures](#python-closures)
  - [Python Decorators](#python-decorators)
    - [Creating Decorators](#creating-decorators)
    - [Applying Multiple Decorators to a Single Function](#applying-multiple-decorators-to-a-single-function)
    - [Accepting Parameters in Decorator Functions](#accepting-parameters-in-decorator-functions)
  - [Built-in Higher Order Functions](#built-in-higher-order-functions)
    - [Python - Map Function](#python---map-function)
    - [Python - Filter Function](#python---filter-function)
    - [Python - Reduce Function](#python---reduce-function)

# 📘 Day 14

## Higher Order Functions

ក្នុង Python function ត្រូវបានគេចាត់ទុកថាជាពលរដ្ឋជាន់ខ្ពស់, ដែលអនុញ្ញាតឱ្យអ្នកធ្វើការប្រតិបត្តិការដូចខាងក្រោមនេះនៅលើ function:

- function អាចយកមួយឬច្រើន function ជា parameters
- function អាចត្រូវបានត្រឡប់មកវិញជាលទ្ធផលនៃ function
- function អាចនឹង modified
- function អាចត្រូវបានកំណត់ឱ្យ variable

នៅក្នុងផ្នែកនេះ យើងនឹងពិភាក្សាអំពី:

1. ការគ្រប់គ្រង functions ជា parameters
2. ត្រឡប់មកវិញ functions ជាតម្លៃមកពី functions ​មួយទៀត
3. ប្រើ Python closures និង decorators

### Function as a Parameter

```py
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Function as a Return Value

```py
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

អ្នកអាចមើលឃើញពីឧទាហរណ៍ខាងលើនេះថា higher order function កំពុងត្រឡប់មកវិញ function​ ខុសៗ​គ្នាដោយអាស្រ័យទៅលើ parameter។

## Python Closures

ython អនុញ្ញាតអោយ function​ ក្នុង function​ មួយទៀត អាចប្រើអ្វីៗរបស់ function​ នៅខាងលើ។ នេះត្រូវបានគេស្គាល់ថាជា Closure។ សូមយើងមើលថា closures ប្រើម្តេខក្នុង Python។ ក្នុង Python, closure បង្កើតដោយដាក់ function​​ ក្នុង function​ មួយទៀតហើយត្រទ្បប់មកវិញ​ function ខាងក្នុង។ សូមមើលឧទាហរណ៍ខាងក្រោម។

**Example:**

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Python Decorators

Decorator គឺជា design pattern ក្នុង Python​ ដែលអនុញ្ញាតឱ្យអ្នកប្រើប្រាស់បន្ថែមមុខងារថ្មី ទៅនឹង object ដោយមិនចាំបាច់កែប្រែលក្ខណៈសម្បត្តិរបស់វាទេ។ Decorators ជាទូទៅត្រូវបានហៅមុនការកំណត់នៃ function​​ ដែលអ្នកចង់ decorate ។

### Creating Decorators

ដើម្បីបង្កើត decorator function,យើងត្រូវការ function ខាងក្រៅ ជាមួយនឹង wrapper function ខាងក្នុង។
**Example:**

```py
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

### Applying Multiple Decorators to a Single Function

```py

'''This decorator function is a higher order function
that takes a function as a parameter'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
```

### Accepting Parameters in Decorator Functions

ភាគច្រើនពេលយើងត្រូវការ functions យក parameters, ដូច្នេះយើងអាចត្រូវកំណត់ decorator ដែលទទួលយក parameters។

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## Built-in Higher Order Functions

មួយចំនួននៃ built-in higher order functions ដែលយើងបានពិភាក្សានៅក្នុងផ្នែកនេះគឺ _map()_, _filter_, and _reduce_​។
Lambda function អាចត្រូវបានដាក់ជា parameter និងករណីប្រើប្រាស់ល្អបំផុតនៃ lambda functions គឺក្នុង functions ដូចជា map, filter និង reduce។

### Python - Map Function

map() function គឺជា built-in function ដែលយក function និង iterable ជា parameters.

```py
    # syntax
    map(function, iterable)
```

**Example:1**

```py
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Example:2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Example:3**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

អ្វីដែល Map ធ្វើគឺធ្វើ iteration លើ list មួយ។ ឧទាហរណ៍វាផ្លាស់ប្តូរឈ្មោះទៅជាអក្សរធំ និងត្រឡប់មក list ថ្មី។

### Python - Filter Function

filter() function ហៅ function ដែលបានកំណត់​ ដែលត្រឡប់មកវិញ boolean សម្រាប់ item នៃ​ iterable (list)។ វាយកចេញ item​​​ ដែលលក្ខខណ្ឌ។
```py
    # syntax
    filter(function, iterable)
```

**Example:1**

```py
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Example:2**

```py
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python - Reduce Function

_reduce()_ function ត្រូវបានកំណត់នៅក្នុង Functools Module ហើយយើងត្រូវ import ពឺ module នេះ។ ដូច map និង filter 
វាត្រូវការពីរ parameters,​ function មួយ និង iterable​ មួយ។ ប៉ុន្តែវាមិនត្រឡប់មកវិញ iterable​ មួយទៀត, វាត្រឡប់មកតម្លៃតែមួយ។
**Example:1**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Exercises: Day 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

[<< Day 13](../13_Day_List_comprehension/13_list_comprehension.md) | [Day 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)
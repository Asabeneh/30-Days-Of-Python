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
  <small> First Edition: Nov 22 - Dec 22, 2019</small>
  </sub>
</div>
</div>

[<< Day 13](../13_Day/13_list_comprehension.md) | [Day 15>>](../15_Day/15_python_type_error.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 14](#%f0%9f%93%98-day-14)
  - [Higher Order Functions](#higher-order-functions)
    - [Function as a parameter](#function-as-a-parameter)
    - [Function as a return value](#function-as-a-return-value)
  - [Python closures](#python-closures)
  - [Python decorators](#python-decorators)
    - [Creating Decorators](#creating-decorators)
    - [Applying Multiple Decorators to a Single Function](#applying-multiple-decorators-to-a-single-function)
    - [Accepting parameters in Decorator Functions](#accepting-parameters-in-decorator-functions)
  - [Built-in Higher Order Functions](#built-in-higher-order-functions)
    - [Python - Map Function](#python---map-function)
    - [Python - Filter Function](#python---filter-function)
    - [Python - Reduce Function](#python---reduce-function)
  - [💻 Exercises: Day 14](#%f0%9f%92%bb-exercises-day-14)

# 📘 Day 14

## Higher Order Functions

In python functions are treated as first class citizens, allowing you to perform the following operations on functions:

- A function can take one or more functions as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

In this section, we will cover:

1. Handling functions as parameters
2. Returning functions as return value from other functions
3. Using python closures and decorators

### Function as a parameter

```py
def sum_numbers(nums):  # normal function
    return sum(nums)

def higher_order_function(f, *args):  # function as a parameter
    summation = f(*args)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Function as a return value

```py
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x == 0:
        return x
    elif x < 1:
        return -(x)
    else:
        return x

def higher_order_function(type): # a higher order function returning function
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

You can see from the above example that the higher order function is returning different functions depending on the passed parameter

## Python closures

Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let’s have a look at how closures works in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.

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

## Python decorators

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

### Creating Decorators

To create a decorator function, we need an outer function, inner wrapper function.

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

## Lets implement the above to a decorator

'''This decorator function is a higher order
which is take function as a parameter'''
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

'''These decorator functions are higher order functions
which take function as parameters'''

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

@uppercase_decorator
@split_string_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

### Accepting parameters in Decorator Functions

Most of the time we need our functions to take parameters, so we might need to define a decorator that accepts parameters.

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love teaching".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## Built-in Higher Order Functions

Some of the builtin higher order function which we cover in the part are _map()_, _filter_, and _reduce_.
Lambda function can be passed a parameter and the best use case of lambda function is in function like map, filter and reduce.

### Python - Map Function

The map() function is a built-in function which takes a function and iterable as parameter.

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

# Lets apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

What actually map do is mapping a list. For instance it changes the names to upper case and return a new list.

### Python - Filter Function

The filter() function calls the specified function which returns boolean for each item of the specified iterable (list). It filters the items which the satisfied with the filtering criteria.

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

The _reduce()_ function is defined in the functools module and we should import it from this module.Like map and filter it takes two parameters, a function and an iterable. However, it doesn't return another iterable, instead it returns a single value.

**Example:2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add(x, y):
    return int(x) + int(y)

total = reduce(add_two, numbers_str)
print(total)    # 15
```

## 💻 Exercises: Day 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

1. Explain the difference between map, filter, and reduce.
1. Explain the difference between higher order function, closure and decorator
1. Define a call function before map, filter or reduce, see examples.
1. Use for loop to print each country in the countries list.
1. Use for to print each name in the names list.
1. Use for to print each number in the numbers list.
1. Use map to create a new list by changing each country to uppercase in the countries list
1. Use map to create a new list by changing each number to square in the numbers list
1. Use map to change to each name to uppercase in the names list
1. Use filter to filter out countries containing land.
1. Use filter to filter out countries having six character.
1. Use filter to filter out countries containing six letters and more in the country list.
1. Use filter to filter out country start with 'E'
1. Chain two or more list iterators(eg. arr.map(callback).filter(callback).reduce(callback))
1. Declare a function called get_string_lists which takes an list as a parameter and then returns an list only with string items.
1. Use reduce to sum all the numbers in the numbers list.
1. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and IceLand are north European countries
1. Declare a function called categorize_countries which returns an list of countries which have some common pattern(you find the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
1. Create a function which return a list of dictionary, which is the letter and the number of times the letter used to start a name of a country.
1. Declare a get_first_ten_countries function and return an list of ten countries from the countries.js list in the data folder.
1. Declare a get_last_ten_countries function which which returns the last ten countries in the countries list.
1. Find out which letter is used many times as initial for a country name from the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py)(eg. Finland, Fiji, France etc)
1. Use the countries_data.py file information, in the data folder.
   - Sort countries by name, by capital, by population
   - Sort out the ten most spoken languages by location.
   - Sort out the ten most populated countries.

🎉 CONGRATULATIONS ! 🎉

[<< Day 13](../13_Day/13_list_comprehension.md) | [Day 15>>](../15_Day/15_python_type_error.md)
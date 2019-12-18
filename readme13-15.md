![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

🧳 [Part 1: Day 1 - 3](https://github.com/Asabeneh/30-Days-Of-Python)  
🧳 [Part 2: Day 4 - 6](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)  
🧳 [Part 3: Day 7 - 9](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)  
🧳 [Part 4: Day 10 - 12](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)  
🧳 [Part 5: Day 13 - 15](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)  
🧳 [Part 6: Day 16 - 18](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)  
🧳 [Part 7: Day 19 - 21](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)  
🧳 [Part 8: Day 22 - 24](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme22-24.md)  
🧳 [Part 9: Day 25 - 27](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme25-27.md)  
🧳 [Part 10: Day 28 - 30](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme28-30.md)  

---

- [📘 Day 13](#%f0%9f%93%98-day-13)
  - [List Comprehension](#list-comprehension)
  - [Lambda Function](#lambda-function)
    - [Creating a lambda function](#creating-a-lambda-function)
    - [Lambda function inside other function](#lambda-function-inside-other-function)
  - [💻 Exercises: Day 13](#%f0%9f%92%bb-exercises-day-13)
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
- [📘 Day 15](#%f0%9f%93%98-day-15)
  - [Python Error Types](#python-error-types)
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexerror)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)
  - [💻 Exercises: Day 15](#%f0%9f%92%bb-exercises-day-15)
GIVE FEEDBACK: http://thirtydayofpython-api.herokuapp.com/feedback
# 📘 Day 13

## List Comprehension

List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

```py
# syntax
[i for i in iterable if expression]
```

**Example:1**

For instance if you want to change a string to a list of characters. You can use a couple methods. Let's see some of them

```py
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**Example:2**

For instance if you want to generate a list of numbers

```py
# Generating numbers
numbers = [i for i in range(11)]  # to generate number from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operation during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is possible to do mathematical operation during iteration
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**Example:2**
List compression can be combined with if expression

```py
# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even number between 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd number between 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter positive and even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_event_numbers = [i for i in range(21) if i % 2 == 0 and i > )]
print(positive_event_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening two dimensional array
two_dimen_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in two_dimen_list for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Lambda Function

Lambda function is a small anonymous function without name.A lambda function can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous function in JavaScript. We need lambda function when we want to write an anonymous function inside another function.

### Creating a lambda function

To create a lambda function we use _lambda_ keyword followed by parameter, followed by expression. See the syntax and the example below. Lambda function do not use return but it explicitly return the expression.

```py
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

**Example:**

```py
# Named function
def add_two_nums(a, b):
    return a + b

print(2, 3)     # 3
# Lets change the above function to lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))
```

### Lambda function inside other function

Using lambda function inside another function.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3) # 8
two_power_of_five = power(2)(5) # 32
```

## 💻 Exercises: Day 13

1. Filter only negative or zero in the list using list comprehension
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
1. Flatten the following list of lists of lists to a one dimensional list :

   ```py
   list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

1. Using list comprehension create the following list of tuples:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
1. Change the following list to a flatten list:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   ['FINLAND', 'HELSINKI', 'SWEDEN', 'STOCKHOLM', 'NORWAY', 'OSLO']
   ```
1. Change the following list to a list of dictionaries:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
1. Change the following list of lists to flat list:
   ```py
   names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
1. Write a lambda function which can solve slope or y-intercept.

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

# 📘 Day 15

## Python Error Types

When we write code it common that we make a typo or other common errors. Based on the type of error we make python raise a kind of error which suggests us to fix it by reading the feedback. Understanding different types of errors in a certain programming language can help us to debug our code quick and in return it makes us a better programmer.

Let's see the most common error types step by step by open our python interactive shell. Go to your you computer terminal and write, python, the python interactive shell will be opened.

### SyntaxError

**Example 1: SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

As you can see we made a syntax error because we forgot to enclose the string with parenthesis and python is already suggested us to fix. Let's fix it.

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

The error was a _SyntaxError_ and we fixed and our code executed. Let see more error types.

### NameError

**Example 1: NameError**

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

As you can see from the above error, it says that name age is not defined. Yes, it is true. We did define an age variable but we were trying to print it as if we declare it. Now, lets fix this by declaring age variable and assigning with a value.

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

The type of error was a _NameError_. We debugged the error by defining the variable name.

### IndexError

**Example 1: IndexError**

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

In the above example, python raised an _IndexError_ because the list has only 0 to 4 indexes, so it was out of range.

### ModuleNotFoundError

**Example 1: ModuleNotFoundError**

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

In the above example, I added extra s to math deliberately and _ModuleNotFoundError_ was raised. Lets fix the error by removing the extra added s from math.

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

We fixed the error by removing the extra s. Now let's use some of the function from math module.

### AttributeError

**Example 1: AttributeError**

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

As you can see, now again I made a mistake instead of pi, I tried to call a PI function from maths module that raise an attribute error, it means the function does not exist in the module. Lets fix it by change from PI to pi.

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

Now, when we call pi from the math module we got the result.

### KeyError

**Example 1: KeyError**

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

As you can see, there was a typo in the key used to get the dictionary value. so, this is a key error and it is straight forward what to fix. Lets fix this.

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

We debug our error and our code ran and we got the value.

### TypeError

**Example 1: TypeError**

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

In the above example, a TypeError is raised because we can not add number and string. First, we should convert the string to int or float. Let's fix this error.

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

The remove the error and our and we got the result we expected.

### ImportError

**Example 1: TypeError**

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

There is no function called power in the math module instead we have _pow_. Lets correct it

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### ValueError

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

We can not change string to a number.

### ZeroDivisionError

```py
Last login: Tue Dec  3 15:20:41 on ttys002
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

We can not divide a number by zero.

We have covered some of the python error types, if you want to check more about it check the python documentation about python error types.
If you are good at reading the error types then you will be able to fix your bugs fast and you will be also a better programmer.

## 💻 Exercises: Day 15

1. Open you python interactive shell and try all the examples covered in this section.

[<< Part 4 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md) | [Part 6 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)

---

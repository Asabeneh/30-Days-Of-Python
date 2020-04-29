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

- [📘 Day 1](#%f0%9f%93%98-day-1)
  - [Welcome](#welcome)
  - [Introduction](#introduction)
  - [Why Python ?](#why-python)
  - [Environment Setup](#environment-setup)
    - [Installing Python](#installing-python)
    - [Python Shell](#python-shell)
    - [Installing Visual Studio Code](#installing-visual-studio-code)
      - [How to use visual studio code](#how-to-use-visual-studio-code)
  - [Basic Python](#basic-python)
    - [Python Syntax](#python-syntax)
    - [Python Indentation](#python-indentation)
    - [Comment](#comment)
    - [Data types](#data-types)
      - [Number](#number)
      - [String](#string)
      - [Booleans](#booleans)
      - [List](#list)
      - [Dictionary](#dictionary)
      - [Tuple](#tuple)
      - [Set](#set)
    - [Checking Data types](#checking-data-types)
    - [Python File](#python-file)
  - [💻 Exercises - Day 1](#%f0%9f%92%bb-exercises---day-1)
- [📘 Day 2](#%f0%9f%93%98-day-2)
  - [Built in functions](#built-in-functions)
  - [Variables](#variables)
  - [Data Types](#data-types-1)
  - [Checking Data types and Casting](#checking-data-types-and-casting)
  - [Number](#number-1)
  - [💻 Exercises - Day 2](#%f0%9f%92%bb-exercises---day-2)
- [📘 Day 3](#%f0%9f%93%98-day-3)
  - [Boolean](#boolean)
  - [Operators:](#operators)
    - [Assignment Operators:](#assignment-operators)
    - [Arithmetic Operators:](#arithmetic-operators)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
  - [💻 Exercises - Day 3](#%f0%9f%92%bb-exercises---day-3)

# 📘 Day 1

## Welcome

**Congratulations** for deciding to participate in a **_30 days of Python_** programming challenge . In this challenge you will learn everything you need to be a python programmer and the whole concepts of programming. In the end of the challenge you will get a **_30DaysOfPython_** programming challenge certificate.

[Join the telegram channel to get help](https://t.me/ThirtyDaysOfPython)

## Introduction

Python is a high-level programming language for general-purpose programming. It is an open source. This 30 days python challenge will help you learn the latest version of Python, Python 3 step by step. The topics are broken down into 30 days, where each days contains several topics with easy-to-understand explanations, real-world examples and many hands on exercises.

This challenge is designed for beginners and professionals who want to learn python programming language.

## Why Python ?

It is a programming language which is very close to human language and because of that it is easy to learn and easy to use.
Python used in varies industries including Google. It has been used to develop web applications, desktop applications, system adminstration, and machine learning libraries. Python is highly embraced language in the data science and machine learning community. I hope this is enough to convince you to start learning python. Python is eating the world and you are killing it before it eats you.

## Environment Setup

### Installing Python

To run python script you need to install python. Let's [download](https://www.python.org/) python.
If your are a windows user. Click the button encircled in red.

[![installing on Windows](./images/installing_on_windows.png)](https://www.python.org/)

If you are a macOS user. Click the button encircled in red.

[![installing on Windows](./images/installing_on_macOS.png)](https://www.python.org/)

To check if python is installed write the following command on your device terminal.

```shell
python --version
```

![Python Version](./images/python_versio.png)

As you can see from the terminal, I am using _python 3.7.5_ version at the moment. If you mange to see the python version, well done. Python has been installed on your machine. Continue to the next section.

### Python Shell

Python is an interpreted scripting language,so it doesn't need to be compiled. It means it executes the code line by line. Python comes with a _Python Shell (Python Interactive Shell)_. It is used to execute a single python command and get the result.

Python Shell waits for the python code from the user. When you enter the code, it interprets the code and shows the result in the next line.
Open your terminal or command prompt(cmd) and write:

```shell
python
```

![Python Scripting Shell](images/opening_python_shell.png)

The python interactive shell is opened and it is waiting for you to write python code. You will write your python script next to this symbol >>> and then click Enter.
Lets write our very first script on the python scripting shell.

![Python script on python shell](images/adding_on_python_shell.png)

Well done, you wrote your first python script on python interactive shell. How do we close this shell ?
To close the shell, next to this symbol >> write **exit()** command and press Enter.

![Exit from python shell](images/exit_from_shell.png)

Now, you knew how to open the python interactive shell and how to exit from it.

Python can give you result if you write scripts what python understands if not it returns errors. Let's make a deliberate mistake and see what python will return.

![Invalid Syntax Error](./images/invalid_syntax_error.png)

As you can see from the returned error, python is so clever that it knows the mistake we made and which was _Syntax Error: invalid syntax_. Using x as multiplication in python is a syntax error because (x) is not a valid syntax in python. Instead of (**x**) we use asterisk (*) for multiplication. The returned error clearly shows what to fix.
The process of identifying and removing errors from a program is called *debugging*. Let's debug it by replacing * in place of **x**.

![Fixing Syntax Error](./images/fixing_syntax_error.png)

Our bug was fixed and the code run and we got a result we were expecting. As a programmer you will see such kind of errors on daily basis. It is good to know how to debug. To be good at debugging you should understand what kind of errors you are facing:SyntaxError, IndexError, ModuleNotFoundError, KeyError, ImportError etc. We will see more about different python **_error types_** in later section .

Let's practice more , how to use python interactive shell. Go to your terminal or command prompt and write the word **python**.

![Python Scripting Shell](images/opening_python_shell.png)

The python interactive shell is open and lets do some basic mathematics operations(addition, subtraction, multiplication, division, modulus, exponential).
Lets do some maths first before we write any python code:

- 2 + 3 = 5
- 3 - 2 = 1
- 3 \* 2 = 6
- 3 / 2 = 1.5
- 3 ^ 2 = 3 x 3 = 9

In python we have the following additional operations:

- 3 % 2 = 1 => which means finding the remainder
- 3 // 2 = 1 => which means removing the remainder

Lets change the above mathematical expressions to code. The python shell has been opened and lets write a comment at the very beginning of the shell.
A _comment_ is a part of the code which is not executed by python. So we can leave some text in our code to make our code more readable. Python does not run the comment part. A comment in python starts with hash(#) symbol.
This is a how you write comment in python

```shell
 # comment starts with hash
 # this is a python comment itself because it starts with a (#) symbol
```

![Maths on python shell](./images/maths_on_python_shell.png)

Before we move on to the next section, lets practice more on the python interactive shell. Close the opened shell by writing _exit()_ on the shell and open it again and let's practice how to write text on the python shell.

![Writing String on python shell](images/writing_string_on_shell.png)

### Installing Visual Studio Code

The python interactive shell is good to try and test small script codes but it won't be for a big project. In real work environment, developers use different code editors to write codes. In this 30 days of python programming challenge we will use visual studio code. Visual studio code is a very popular open source text editor. I am a fan of vscode and I would recommend to [download](https://code.visualstudio.com/) visual studio code, but if you are in favor of other editors, feel free to follow with what you have.

[![Visual Studio Code](./images/vscode.png)](https://code.visualstudio.com/)

If you installed visual studio code, let's see how to use it.

#### How to use visual studio code

Open the visual studio code by double clicking the visual studio icon. When you open it you will get this kind of interface. Try to interact with the labelled icons.

![Visual studio Code](images/vscode_ui.png)

Create a folder name 30DaysOfPython on your desktop. Then open it using visual studio code.

![Opening Project on Visual studio](./images/how_to_open_project_on_vscode.png)

![Opening a project](./images/opening_project.png)

After you opened you can create file and folder inside the your project directory which is 30DaysOfPython. As you can see below, I have created the very first file, helloworld.py. You can do the same.

![Creating a python file](./images/helloworld.png)

After a long day of coding, you want to close your code editor, right ?. This is how you will close the opened project.

![Closing project](./images/closing_opened_project.png)

Congratulations, you have finished setting up the development environment. Let's start coding.

## Basic Python

### Python Syntax

A python script can be written on python interactive shell or on code editor. A python file has an extension .py.

### Python Indentation

An indentation is a white space in a text. Indentation in many languages used to increase code readability, however python uses indentation to create block of codes. In other programming languages curly bracket used to create block of codes instead of indentation. One of the common bug when you write a python code will be wrong indentation.

![Indentation Error](images/indentation.png)

### Comment

Comment is very important to make code more readable and to leave to remark in our code. Python doesn't run comment part of our code.
Any text starts with hash(#) in python is a comment.

**Example: Single Line Comment**

```shell
    # This is the first comment
    # This is the second comment
    # Python is eating the world
```

**Example: Multiline Comment**

Triple quote can be use for multiline comment if it is not assigned to a variable

```shell
"""This is multiline comment
multiline comment take multiple lines.
python is eating the world
"""
```

### Data types

In python there are several types of data types. We will get started with the most common ones.

#### Number

    - Integer: Integer(negative, zero and positive) numbers
        Example:
        ... -3, -2, -1, 0, 1, 2, 3 ...
    - Float: Decimal number
        Example
        ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
    - Complex
        Example
        1 + j, 2 + 4j

#### String

A collection of one or more characters under a single or double quote. If a string is more than one sentence we use triple quote.

**Example:**

```py
'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day'
```

#### Booleans

A boolean data type is either a True or False value.

**Example:**

```python
    True  #  if the light on, if it is on the value is True
    False # if the light off, if it is off the value is False
```

#### List

Python list is an ordered collection which allows to store of different data type items. A list is similar to an array in JavaScript.

**Example:**

```py
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data type in the list
['Banana', 10, False, 9.81] # different data types in the list
```

#### Dictionary

A python dictionary object is an unordered collection of data in a key:value pair.

**Example:**

```py
{'name':'Asabeneh', 'country':'Finland', age:250, 'is_married':True}
```

#### Tuple

A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

**Example**

```py
('Asabeneh', 'Brook', 'Abraham', 'Lidiya')
```

#### Set

A set is a collection data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in mathematics, set in python store only unique items.

In later sections, we will go in detail in each and every python data types.

**Example:**

```py
{3.14, 9.81, 2.7} # order is not important in set
```

### Checking Data types

To check the data type of a certain data type we use the **type** function. In the following terminal you will see the different python data types:

![Checking Data types](./images/checking_data_types.png)

### Python File

First open your project folder, 30DaysOfPython. If you don't have this folder,create a folder name called 30DaysOfPython. Inside this folder, create a file called helloworld.py. Now, let's do what we did on python interactive shell using visual studio code.
The python interactive shell was printing without using **print** but on visual studio code to see our result we should use a built in function **print(some data to print)**.

**Example:**
helloworld.py

```py
# Day 1 - 30DaysOfPython Challenge
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
```

![Running python script](./images/running_python_script.png)

🌕  You are amazing. You have just completed day 1 challenge and you are in your way to greatness. Now do some exercises for your brain and for your muscle.

## 💻 Exercises - Day 1

1. Check the python version you are using
2. Open the python interactive shell and do the following operations. The operands are 3 and 4. Check the example above
   - addition(+)
   - subtraction(-)
   - multiplication(\*)
   - modulus(%)
   - division(/)
   - exponential(\*\*)
   - floor division operator(//)
3. Write strings on the python interactive shell. The strings are the following:
   - Your name
   - Your family name
   - Your country
   - I am enjoying 30 days of python
4. Check the data types of the following data:
   - 10
   - 9.8
   - 3.14
   - 4 - 4j
   - ['Asabeneh', 'Python', 'Finland']
   - Your name
   - Your family name
   - Your country
5. Create a folder name day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a file python file helloword.py and repeat question 1, 2, 3 and 4. Remember to use _print()_ when you are working on a python file. Navigate to the directory where you saved your file, and run it.

# 📘 Day 2

## Built in functions

In python we have lots of built in functions. Built-in functions are globally available for your use. Some of the most commonly used python built-in functions are the following: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, and _dir()_. In the following table you will see an exhaustive list of python built in functions taken from [python documentation](https://docs.python.org/2/library/functions.html).

![Built in Functions](images/builtin-functions.png)

Let's open the python shell and start using some of the most common built in functions.

![Built in functions](images/builtin-functions_practice.png)

Let's practice more by using different built-in functions

![Help and Dir Built in Functions](/images/help_and_dir_builtin.png)

As you can see from the above terminal, python has reserved words. We do not use reserved words to declare variables or functions. We will cover variables in the next section.

I believe, by now you are familiar with built-in functions. Let's do one more practice of built-in functions and we will move on to the next section

![Min Max Sum](images/builtin-functional-final.png)

## Variables

Variables store data in a computer memory. Mnemonic variables are recommend to use in many programming languages. A variable refers to an a memory address in which a data is stored.
Number at the beginning, special character, hyphen are not allowed. A variable can have a short name (like x,y,z) but a more descriptive name (firstname, lastname, age, country) is highly recommended .
Python Variable Name Rules

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and \_ )
- Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME are different variables)

Valid variable names

```shell
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2019
year2019
current_year_2019
num1
num2
```

Invalid variables names

```shell
first-name
num-1
1num
```

We will use standard python variable naming style which has been adopted by many python developers. The example below is an example of standard naming of variables, underscore when the variable name is long.

When we assign a certain data type to a variable is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable.

_Example:_

```py
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

Let's use _print()_ and _len()_ built in functions. Print function will take multiple arguments. An argument is a value which we pass or put inside the function parenthesis, see the example below.

**Example:**

```py
print('Hello, World!')
print('Hello',',', 'World','!') # it can take multiple arguments
print(len('Hello, World!')) # it takes only one argument
```

Let's print and also find the length of the variables declared at the top:

**Example:**

```py
# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

Variable can also be declared in one line:

**Example:**

```py
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

Getting user input using the _input()_ built-in function. Let's assign the data we get from a user into first_name and age variables.
**Example:**

```py
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

## Data Types

There are several data types in python. To identify the data type we use the _type_ builtin function. I like you to focus understanding different data types very well. When it comes to programming it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

## Checking Data types and Casting

- Check Data types: To check the data type of a certain data type we use the _type_
  **Example:**

```py
# Different python data types
# Let's declare different data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2,3,4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
```

- Casting: Converting one data type to another data type. We use _int()_, _float()_, _str()_, _list_
  When we do arithmetic operations string numbers should be first converted to int or float if not it returns an error. If we concatenate a number with string, the number should be first converted to a string. We will talk about concatenation in String section.
  **Example:**

```py
# int to float

num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first = 'Asabeneh'
print(first_name)
print(first_name)                    # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

## Number

Numbers are python data types.

1. Integers: Integer(negative, zero and positive) numbers
    Example:
        ... -3, -2, -1, 0, 1, 2, 3 ...

2. Floating Numbers(Decimal numbers)
    Example:
        ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. Complex Numbers
    Example:
        1 + j, 2 + 4j, 1 - 1j

## 💻 Exercises - Day 2

1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file name called variables.py
2. Writ a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable is_true and assign a value to it
12. Declare a variable is_light_on and assign a value to it
13. Declare multiple variable on one line
14. Check the data type of all your variables using type() built in function
15. Using the _len()_ built-in function find the length of your first name
16. Compare the length of your first name and your last name
17. Declare 5 as num_one and 4 as num_two
    1. Add num_one and num_two and assign the value to a variable _total_
    2. Subtract num_two from num_one and assign the value to a variable _diff_
    3. Multiply num_two and num_one and assign the value to a variable _product_
    4. Divide num_one by num_two and assign the value to a variable _division_
    5. Use modulus division to find num_two divided by num_one and assign the value to a variable _remainder_
    6. Calculate num_one the power of num_two and assign the value to a variable _exp_
    7. Find floor division of num_one by num_two and assign the value to a variable _floor_division_
18. The radius of a circle is 30 meters.
    1. Calculate the area of a circle and assign the value to a variable _area_of_circle_
    2. Calculate the circumference of a circle and assign the value to a variable _circum_of_circle_
    3. Take radius as user input and calculate the area.
19. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
20. Run help('keywords') on python shell or in your file check the reserved words

# 📘 Day 3

## Boolean

A boolean data type represents one of the two values:_True_ or _False_. The use of these data types will be clear when you start the comparison operator. The first letter **T** for True and **F** for False should be capital unlike JavaScript.
**Example: Boolean Values**

```py
print(True)
print(False)
```

## Operators:

Python language supports several types of operators. In this section, we will focus on few of them.

### Assignment Operators:

Assignment operators are used to assign values to variables. Let's take = as an example. Equal sign in mathematics shows that two values are equal, however in python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable. The table below shows the different types of python assignment operators, taken from [w3school](https://www.w3schools.com/python/python_operators.asp).

![Assignment Operators](images/assignment_operators.png)

### Arithmetic Operators:

- Addition(+): a + b
- Subtraction(-): a -b
- Multiplication(_):a _ b
- Division(/): a / b
- Modulus(%):a % b
- Floor division(//): a // b
- Exponential(**):a ** b

![Arithmetic Operators](./images/arithmetic_operators.png)

**Example:Integers**

```py
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ',7 // 3)
print('Exponential: ', 3 ** 2)                      # it means 3 * 3
```

**Example:Floats**

```py
# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)
```

**Example:Complex numbers**

```py
# Complex numbers
print('Complex number: ', 1+1j)
print('Multiplying complex number: ',(1+1j) * (1-1j))
```

Let's declare a variable and assign a number data type. I am going to use single character variable but remember do not develop a habit of declaring such types of variable. Variable names should be all the time mnemonic.

**Example:**

```python
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
```

**Example:**

```py
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
```

Let's start start connecting the dots and start making use of what we knew to calculate(area, volume, weight, perimeter, distance, force)

**Example:**

```py
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_width)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight
```

### Comparison Operators

In programming we compare values, we use comparison operators to compare two values. We check if a value is greater or less or equal to other value. The following table shows python comparison operators which was taken from [w3shool](https://www.w3schools.com/python/python_operators.asp).

![Comparison Operators](./images/comparison_operators.png)
**Example: Comparison Operators**

```py
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something give either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

```

In addition to the above comparison operator python uses:

- _is_: Returns true if both variables are the same object(x is y)
- _is not_: Returns true if both variables are not the same object(x is not y)
- _in_: Returns True if a list with the a certain item(x in y)
- _not in_: Returns True if a list doesn't have the a certain item(x in y)

```py
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 **2)   # True
```

### Logical Operators

Unlike other programming languages python uses the key word _and_, _or_ and _not_ for logical operator. Logical operators are used to combine conditional statements:

![Logical Operators](./images/logical_operators.png)

```py
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
```

## 💻 Exercises - Day 3

1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a complex number variable
4. Write a script that prompt the user to enter base and height of the triangle and calculate an area of a triangle (area = 0.5 x b x h).

```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 50
```

5. Write a script that prompt the user to enter side a, side b, and side c of the triangle and and calculate the perimeter of triangle (perimeter = a + b + c)

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

6. Get length and width using prompt and calculate an area of rectangle (area = length x width and the perimeter of rectangle (perimeter = 2 x (length + width))
7. Get radius using prompt and calculate the area of a circle (area = pi x r x r) and circumference of a circle(c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point(6,10)
10. Compare the slope of q10 and 11
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
12. Find the length of python and jargon and make a falsy comparison statement.
13. Use _and_ operator to check if 'on' is found in both python and jargon
14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text _python_ and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. The floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to 10
20. Check if int('9.8') is equal to 10
21. Writ a script that prompt a user to enters hours and rate per hour. Calculate pay of the person?

```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

22. Write a script that prompt the user to enter number of years. Calculate the number of seconds a person can live. Assume some one lives just hundred years

```py
Enter number of yours you live: 100
You lived 3153600000 seconds.
```

23. Write a python script that display the following table

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

[Part 2 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)

![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)
- [Day 1](#day-1)
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
  - [Exercises - Day 1](#exercises---day-1)
- [Day 2](#day-2)
  - [Built in functions](#built-in-functions)
  - [Variables](#variables)
  - [Data Types](#data-types)
  - [Checking Data types and Casting](#checking-data-types-and-casting)
  - [Number](#number-1)
  - [Exercises - Day 2](#exercises---day-2)
- [Day 3](#day-3)
  - [Boolean](#boolean)
  - [Operators:](#operators)
    - [Assignment Operators:](#assignment-operators)
    - [Arithmetic Operators:](#arithmetic-operators)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
  - [Exercises - Day 3](#exercises---day-3)
- [Day 4](#day-4)
  - [String](#string-1)
    - [Creating a string](#creating-a-string)
    - [String Concatenation](#string-concatenation)
    - [Escape Sequences in string](#escape-sequences-in-string)
    - [String formating](#string-formating)
      - [Old Style String Formatting (% Operator)](#old-style-string-formatting--operator)
      - [New Style String Formatting (str.format)](#new-style-string-formatting-strformat)
      - [String Interpolation / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
    - [Python strings as sequences of characters](#python-strings-as-sequences-of-characters)
      - [Unpacking characters](#unpacking-characters)
      - [Accessing characters in strings by index](#accessing-characters-in-strings-by-index)
      - [Slicing Python Strings](#slicing-python-strings)
      - [Reversing a string](#reversing-a-string)
      - [Skipping characters while slicing](#skipping-characters-while-slicing)
    - [String Methods](#string-methods)
  - [Exercises - Day 4](#exercises---day-4)
- [Day 5](#day-5)
  - [Lists](#lists)
    - [How to create a list](#how-to-create-a-list)
    - [Accessing list items using positive indexing](#accessing-list-items-using-positive-indexing)
    - [Accessing list items using negative indexing](#accessing-list-items-using-negative-indexing)
    - [Unpacking list items](#unpacking-list-items)
    - [Slicing items from list](#slicing-items-from-list)
    - [Modifying list](#modifying-list)
    - [Check items in a list](#check-items-in-a-list)
    - [Adding item in a list](#adding-item-in-a-list)
    - [Inserting item in to a list](#inserting-item-in-to-a-list)
    - [Removing item from list](#removing-item-from-list)
    - [Removing item using pop](#removing-item-using-pop)
    - [Removing item using del](#removing-item-using-del)
    - [Clearing list items](#clearing-list-items)
    - [Copying a list](#copying-a-list)
    - [Joining lists](#joining-lists)
    - [Counting Items in a list](#counting-items-in-a-list)
    - [Finding index of an item](#finding-index-of-an-item)
    - [Reversing a list](#reversing-a-list)
    - [Sorting list items](#sorting-list-items)
  - [Exercises: Day 5](#exercises-day-5)
- [Day 6:](#day-6)
  - [Tuple](#tuple-1)
    - [Creating Tuple](#creating-tuple)
    - [Tuple length](#tuple-length)
    - [Accessing tuple items](#accessing-tuple-items)
    - [Slicing tuples](#slicing-tuples)
    - [Changing tuples to list](#changing-tuples-to-list)
    - [Checking an item in a list](#checking-an-item-in-a-list)
    - [Joining tuples](#joining-tuples)
    - [Deleting tuple](#deleting-tuple)
  - [Exercises: Day 6](#exercises-day-6)

# Day 1
## Welcome
**Congratulations** for deciding to participate in a ***30 days of Python*** programming challenge . In this challenge you will learn everything you need to be a python programmer and the whole concepts of programming. In the end of the challenge you will get a ***30DaysOfPython*** programming challenge certificate. [Join the telegram channel](https://t.me/ThirtyDaysOfPython)
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

If you are a  macOS user. Click the button encircled in red.

[![installing on Windows](./images/installing_on_macOS.png)](https://www.python.org/)

To check if python is installed write the following command on your device terminal.
```shell
python --version
```
![Python Version](./images/python_versio.png)


As you can see from the terminal, I am using *python 3.7.5* version at the moment. If you mange to see the python version, well done. Python has been installed on your machine. Continue to the next section.  

### Python Shell
Python is an interpreted scripting language,o it doesn't need to be compiled. It means it executes the code line by line. Python comes with  a *Python Shell (Python Interactive Shell)*. It is used to execute a single python command and get the result.

Python Shell waits for the python code from the user. When you enter the code, it interprets the code and shows the result in the next line.
Open your terminal or cmd and write:
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

As you can see from the returned error, python is so clever that it knows the mistake we made and which was *Syntax Error: invalid syntax*. Using x as multiplication in python is a syntax error because (x) is not a valid syntax in python. Instead  of  (**x**)  we use asterisk (*) for multiplication. The returned error clearly shows what to fix. 
The process of identifying and removing errors from a program is called *debugging*. Let's debug it by replacing * in place of **x**. 

![Fixing Syntax Error](./images/fixing_syntax_error.png)

Our bug was fixed and the code run and we got a result we were expecting. As a programmer you will see such kind of errors on daily basis. It is good to know how to debug. To be good at debugging you should understand what kind of errors you are facing:SyntaxError, IndexError, ModuleNotFoundError, KeyError, ImportError etc. We will see more about different python ***error types*** in later section .

Let's practice more , how to use python interactive shell. Go to your terminal or command prompt and write the word **python**.

![Python Scripting Shell](images/opening_python_shell.png)

The python interactive shell is open and lets do some basic mathematics operations(addition, subtraction, multiplication, division, modulus, exponential). 
Lets do some maths first before we write any python code:
- 2 + 3 = 5
- 3 - 2 = 1
- 3 * 2 = 6
- 3 / 2 = 1.5
- 3 ^ 2 = 3 x 3 = 9

In python we have the following additional operations:
- 3 % 2 = 1  => which means finding the remainder
- 3 // 2 = 1 => which means removing the remainder

Lets change the above mathematical expressions to code. The python shell has opened and lets write a comment at the very beginning of the shell.
A *comment* is a part of the code which is not executed by python. So we can leave some text in our code to make our code more readable. Python does not run the comment part. A comment in python starts with hash(#) symbol.
This is a how you write comment in python
```shell
 # comment starts with hash
 # this is a python comment itself because it starts with a (#) symbol
```

![Maths on python shell](./images/maths_on_python_shell.png)

Before we move on to the next section, lets practice more on the python interactive shell. Close the opened shell by writing *exit()* on the shell and open it again and lets practice how to write text on the python shell.

![Writing String on python shell](images/writing_string_on_shell.png)

### Installing Visual Studio Code
The python interactive shell is good to try and test small script codes but it won't be for a big  project. In real work environment, developers use different code editors to write codes. In this 30 days python programming challenge we will use visual studio code. Visual studio code is a very popular open source text editor. I am a fun of vscode and I would recommend to [download](https://code.visualstudio.com/) visual studio code, but if you are in favor of other editors, feel free to follow with what you have.

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
A python  dictionary object is an unordered collection of data in a key:value pair.

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
print(type({9.8, 3.14, 2.7}))    # Tuple
```
![Running python script](./images/running_python_script.png)


## Exercises - Day 1
  1. Check the python version you are using
  2. Open the python interactive shell and do  the following operations. The operands are 3 and 4. Check the example above
     - addition(+)
     - subtraction(-)
     - multiplication(*)
     - modulus(%)
     - division(/)
     - exponential(**)
     - floor division operator(//)
 1. Write strings on the python interactive shell. The strings are the following:
     - Your name 
     - Your family name
     - Your country
     - I am enjoying 30 days of python
 2. Check the data types of the following data:
    - 10
    - 9.8
    - 3.14
    - 4 - 4j
    - ['Asabeneh', 'Python', 'Finland']
    - Your name
    - Your family name
    - Your country
 3. Create a folder name day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a file python file helloword.py and repeat question 1, 2, 3 and 4. Remember to use *print()* when you are working on a python file. Navigate to the directory where you saved your file, and run it.

# Day 2
## Built in functions
In python we have lots of built in functions. Built-in functions are globally available for your use. Some  of the most commonly used python built-in functions are the following: *print()*,  *len()*,  *type()*,  *int()*,  *float()*,  *str()*,  *input()*,  *list()*,  *dict()*,  *min()*,  *max()*,  *sum()*,  *sorted()*,  *open()*,  *file()*,  *help()*, and *dir()*.  In the following table you will see an exhaustive list of python built in functions taken from [python documentation](https://docs.python.org/2/library/functions.html).

![Built in Functions](images/builtin-functions.png)

Let's open the python shell and start using some of the most common built in functions. 

![Built in functions](images/builtin-functions_practice.png)

Let's practice more by using different built-in functions

![Help and Dir Built in Functions](/images/help_and_dir_builtin.png)

As you can see from the above terminal, python has reserved words. We do not use reserved words to declare variables or functions. We will cover variables in the next section.

I believe,  by now you are familiar with built-in functions.  Let's do one more practice of built-in functions and we will move on to the next section

![Min Max Sum](images/builtin-functional-final.png)


## Variables
Variables store data in a computer memory.  Mnemonic variables are recommend to use in many programming languages.  A variable refers to an a memory address in which a data is stored.
Number at the beginning,  special character,  hyphen are not allowed.  A variable can have a short name (like x,y,z) but a more descriptive name (firstname,  lastname,  age,  country) is highly recommended .

 Python Variable Name Rules
   - A variable name must start with a letter or the underscore character
   - A variable name cannot start with a number
   - A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
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

 *Example:*

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
 Let's use *print()* and *len()* built in functions. Print function will take multiple arguments. An argument is a value which we pass or put inside the function parenthesis, see the example below.

 **Example:**
 ```py
 print('Hello, World!')
 print('Hello',',', 'World','!') # it can take multiple arguments
 print(len('Hello, World!')) # it takes only one argument
 ```

 Let's print and also find  the length of the variables declared at the top:

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
 Getting user input using the *input()* built-in function. Let's assign the data we get from a user into first_name and age variables.
 **Example:**
 ```py
 first_name = input('What is your name: ')
 age = input('How old are you? ')
 print(first_name)
 print(age)
 ```

 ## Data Types
 There are several data types in python. To identify the data type we use the *type* builtin function. I like you to focus understanding different data types very well. When it comes to programming it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.
## Checking Data types and Casting
* Check Data types: To check the data type of a certain data type we use the *type*
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
* Casting: Converting one data type to another data type. We use *int()*, *float()*, *str()*, *list*
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

## Exercises - Day 2
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
15. Using the *len()* built-in function find the length of your first name
16. Compare the length of your first name and your last name
17. Declare 5 as num_one and 4 as num_two
    1.  Add num_one and num_two and assign the value to a variable *total*
    2.  Subtract num_two from num_one and assign the value to a variable *diff*
    3.  Multiply num_two and num_one and assign the value to a variable *product*
    4.  Divide num_one by num_two and assign the value to a variable *division*
    5.  Use modulus division to find num_two divided by  num_one and assign the value to a variable *remainder*
    6.  Calculate num_one the  power of num_two and assign the value to a variable *exp*
    7.  Find floor division of num_one by num_two and assign the value to a variable *floor_division*
18. The radius of a circle is 30 meters.
    1.  Calculate the area of a circle and assign the value to a variable *area_of_circle*
    2.  Calculate the circumference of a circle and assign the value to a variable *circum_of_circle*
    3.  Take radius as user input and calculate the area. 
19. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
20. Run help('keywords') on python shell or in your file check the reserved words

# Day 3
## Boolean

A boolean data type represents one of the two values:*True* or *False*. The use of these data types will be clear when you start the comparison operator. The first letter **T** for True and **F** for False should be capital unlike JavaScript.
**Example: Boolean Values**
```py
print(True)
print(False)
```
## Operators:
Python language supports several types of  operators. In this section, we will focus on few of them.
### Assignment Operators:
Assignment operators are used to assign values to variables. Let's take = as an example. Equal sign in mathematics shows that two values are equal, however in python it means we are storing a value in a certain variable and we call it assignment or a assigning value to a variable.  The table below shows the different types of python assignment operators, taken from [w3school](https://www.w3schools.com/python/python_operators.asp).

![Assignment Operators](images/assignment_operators.png)

### Arithmetic Operators:
* Addition(+): a + b 
* Subtraction(-): a -b 
* Multiplication(*):a * b
* Division(/): a / b
* Modulus(%):a % b
* Floor division(//): a // b
* Exponential(**):a ** b

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
* *is*: Returns true if both variables are the same object(x is y)
* *is not*: Returns true if both variables are not the same object(x is not y)
* *in*: Returns True if a list with the a certain item(x in y)
* *not in*: Returns True if a list doesn't have  the a certain item(x in y)

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
Unlike other programming languages python uses the key word *and*, *or* and *not* for logical operator. Logical operators are used to combine conditional statements:

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

## Exercises - Day 3
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a complex number variable
4.  Write a script that prompt the user to enter base and height of the triangle and calculate an area of a triangle (area = 0.5 x b x h).
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
6. Get length and width using prompt and calculate an area of rectangle (area = length x width  and the perimeter of rectangle (perimeter = 2 x (length + width))
7. Get radius using prompt and calculate the area of a circle (area = pi x r x r) and circumference of a circle(c = 2 x pi x r) where pi = 3.14.
8.  Calculate the slope, x-intercept and y-intercept of y = 2x -2
9.  Slope is (m = y2-y1/x2-x1). Find the slope between point (2, 2) and point(6,10)
10. Compare the slope of q10 and 11
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
12. Find the length of python and jargon and make a falsy comparison statement.
13. Use *and* operator to check if 'on' is found in both python and jargon
14. *I hope this course is not full of jargon*. Use *in* operator to check if *jargon* is in the sentence.
15. There is no 'on' in both  dragon and python
16. Find the length of the text *python* and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. The  floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to 10
20. Check if int('9.8') is equal to 10
21. Writ a script that prompt a user to enters hours and rate per hour. Calculate pay of the person? 
```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```
22. Write a script that prompt the user to enter number of years.  Calculate the number of seconds a person can live. Assume some one lives just hundred years
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

# Day 4
## String
Text is a string data type. Any data type written as text is a string. Any data under single or double quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

### Creating a string
```py
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

```
Multiline string is created by using triple ''' or  quotes.See the example below.
```py
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```
### String Concatenation
We can connect to strings together. Merging or connecting to strings together is called concatenation.See the example below
```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15
```
### Escape Sequences in string
In python and other programming language \ followed by a character. Let's see the most common escape characters:
* \n: new line
* \t: Tab means(8 spaces)
* \\\\: Back slash
* \\': Single quote (')
* \\":Double quote (")
```py
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"') 

# output
I hope every one enjoying the python challenge.
Do you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a back slash  symbol (\)
In every programming language it starts with "Hello, World!"

```
### String formating
#### Old Style String Formatting (% Operator)
In python there many ways of formating string. In this section we will cover some of them.
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s",  "%d", "%f", "%.<number of digits>f". 
* %s - String (or any object with a string representation, like numbers)
* %d - Integers
* %f - Floating point numbers
* %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

```py
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formatted_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formatted_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formatted_string = 'The following are python libraries:' % python_libraries
print(formatted_string) # "The following are python libraries:['Django', 'Flask', 'Numpy', 'Pandas']"
```
#### New Style String Formatting (str.format)
This is formating is introduced in python version 3. 

```py

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formatted_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formatted_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formatted_string)

```
####  String Interpolation / f-Strings (Python 3.6+)
Another new string formatting is string interpolation, f-strings. String started with f and we can inject the data in their corresponding positions.
```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}') 
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

### Python strings as sequences of characters
Python strings are sequences of  characters, and share their basic methods of access with those other Python sequences – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.
#### Unpacking characters 
```
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n
```
#### Accessing characters in strings by index
  In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.

  ![String index](./images/string_index.png)
  
```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```
If we want to start from right end we can use negative indexing. -1 is the last index.
```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
  ```
#### Slicing Python Strings
    In python we can slice substrings from a string.
```py
language = 'Python'
first_three = language[0,3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```
#### Reversing a string
We can easily reverse string in python.
```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

#### Skipping characters while slicing
It is possible to skip characters while slicing by passing step argument to slice method.
```py
language = 'Python'
pto = language[0,6:2] # 
print(pto) # pto
```

### String Methods
There are many string methods which allow us to format strings. See some of the string methods in the following example:

* capitalize(): Converts the first character the string to Capital Letter
```py
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```
* count(): returns occurrences of substring in string, count(substring, start=.., end=..)
```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`
```
* endswith(): Checks if a string ends with a specified ending
```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```
* expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```
* find(): Returns the index of first occurrence of substring
```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```
* format()	formats string into nicer output    
    More about string formating check this [link](https://www.programiz.com/python-programming/methods/string/format)
```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0
```
* index(): Returns the index of substring
```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```
* isalnum(): Checks alphanumeric character
```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```
* isalpha(): Checks if all characters are alphabets
```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```
* isdecimal(): Checks Decimal Characters
```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```
* isdigit(): Checks Digit Characters
```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.digit())   # True
```
* isdecimal():Checks decimal characters
```py
num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False
```

* isidentifier():Checks for valid identifier means it check if a string is a valid variable name
```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

* islower():Checks if all alphabets in a string are lowercase
```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```
* isupper(): returns if all characters are uppercase characters
```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

* isnumeric():Checks numeric characters
```py
num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False
```
* join(): Returns a concatenated string
```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```
* strip(): Removes both leading and trailing characters
```py
challenge = ' thirty days of python '
print(challenge.strip('y')) # 5
```
* replace(): Replaces substring inside
```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```
* split():Splits String from Left
```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
```
* title(): Returns a Title Cased String
```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```
* swapcase(): Checks if String Starts with the Specified String
  The string swapcase() method converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.
```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```
* startswith(): Checks if String Starts with the Specified String
```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```

## Exercises - Day 4
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
3. Declare a variable name company and assign it to an initial value "Coding For All.
4. Print company using *print()*
5. Print the length of the company string using *len()* method and *print()*
6. Change all the characters to capital letters using *upper()* method
7. Change all the characters to lowercase letters using *lower()* method
8. Use capitalize(), title(), swapcase() methods to format the value the string *Coding For All*.
9.  Cut(slice) out the first word of *Coding For All* string
10. Check if *Coding For All* string contains a word Coding using the method index, find or other methods.
11. Replace the word coding in the string 'Coding For All' to Python.
12. Change Python for Everyone to Python for All using the replace method or other methods
13. Split the string 'Coding For All' at the space using split() method
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
15. What is character at index 0 in the string *Coding For All*.
16. What is the last index of the string *Coding For All*
17. What character is at index 10 in "Coding For All" string.
18. Create an acronym or an abbreviation for the name 'Python For Everyone'
19. Create an acronym or an abbreviation for the name 'Coding For All'
20. Use index to determine the position of the first occurrence of C in Coding For All.
21. Use index to determine the position of the first occurrence of F in Coding For All
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
23. Use index or find to find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
24. Use rindex to find the position of the last occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
25. Slice out the phrase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
26. Find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
27. Slice out the phase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
28. Does Coding For All starts with a substring *Coding*?
29. Does Coding For All ends with a substring *coding*?
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;,    remove the left and right trailing spaces in the given string.
31. Which one of the following variable return True when we use the method isidentifier()
    * 30DaysOfPython
    * thirty_days_of_python
32. The following are some of python libraries list: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string. 
33. Use new line escape sequence to writ the following sentence.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. Use a tab escape sequence to writ the following sentence.
    ```py
    Name      Age     Country
    Asabeneh  250     Finland
    ```
35. Use string formatting method to display the following:
```sh
radius = 10
area = 3.14 * radius ** 2
The area of radius 10 is 314 meters squares. 
```
36. Make the following using string formatting methods:
```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```
# Day 5
## Lists
The are four collection data types in python :
* List:  is a collection which is ordered and changeable(modifiable). Allows duplicate members.
* Tuple:  is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
* Set:  is a collection which is unordered and unindexed. No duplicate members.
* Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items or items
### How to create a list
In python we can create list in two ways:
* Using list builtin function
```py
# syntax
lst = list()
```
```py
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```
* Using square brackets, []
```py
# syntax
lst = []
```
```py
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

List with initial values. We use *len()* to find the length of a list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```
```sh
output
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```
* List can have items of different data types
```py
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
```
### Accessing list items using positive indexing
We access each item in a list using their index. A list index start from 0. The picture below show clearly where the index starts
![List index](./images/list_index.png)
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```
### Accessing list items using negative indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.

![List negative indexing](./images/list_negative_indexing.png)
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```
### Unpacking list items
```py
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item1
print(third_item)     # item2
print(rest)           # ['item4', 'item5']

```
```py
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```
### Slicing  items from list
* Positive Indexing: We can specify a range of positive indexes by specifying the starting  and the ending, the return value will be a new list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]
```
* Negative Indexing:  We can specify a range of negative indexes by specifying the starting  and the ending, the return value will be a new list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]
```
### Modifying list
List is a mutable or modifiable ordered collection of items or items. Lets modify the fruit list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits)
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```
### Check items in a list
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```
### Adding item in a list
To add item to the end of an existing list we use the method
```py
# syntax
lst = list()
lst.append(item)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```
### Inserting item in to a list
Use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right.
```py
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon']
print(fruits)
```
### Removing item from list
The remove method remove a specified item from a list
```py
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']
```
### Removing item using pop
The pop() method removes the specified index, (or the last item if index is not specified):
```py
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.remove(0)     
print(fruits)       # ['orange', 'mango']    
```
### Removing item using del
The del keyword removes the specified index and it can be also use to delete the list completely

```py
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```
### Clearing list items
The clear() method empties the list:
```py
# syntax
lst = ['item1', 'item2']
lst.clear()
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []   
```
### Copying  a list
It is possible to copy a list by reassigning to a new variable in the  following way list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list2. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way avoid the above problem is using *copy()*.
```py
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```
### Joining lists
There are several ways to join, or concatenate, two or more lists in Python. 

* Plus Operator (+)
```py
# syntax
list3 = list1 +list2
```
```py
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

```
```py
# output
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```
  * Joining using extend() method

```py
# syntax
lst1 = ['item1', 'item2']
lst2 = ['item3', 'item4','item5']
list1.extend(list2)
```
```py
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

```
```py
Numbers: [0, 1, 2, 3, 4, 5, 6]
Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### Counting Items in a list
The count() method returns the number of times an item appears in a list:
```py
# syntax
lst = ['item1', 'item2']
lst.count(item) 
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```
### Finding index of an item
The count() method returns the index of an item in the list:
```py
# syntax
lst = ['item1', 'item2']
lst.index(item) 
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```
### Reversing a list
The reverse() method reverse the order of a list.
```py
# syntax
lst = ['item1', 'item2']
lst.reverse() 

```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())         
```
```py
['lemon', 'mango', 'orange', 'banana']
[24, 25, 24, 26, 25, 24, 19, 22]
```
### Sorting list items
The sort() method reorder the list items in ascending order. If a reverse is equal to true it arrange in descending order.
```py
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages)           
```
```sh
['banana', 'lemon', 'mango', 'orange']
['orange', 'mango', 'lemon', 'banana']
[19, 22, 24, 24, 24, 25, 25, 26]
[26, 25, 25, 24, 24, 24, 22, 19]
```
  
## Exercises: Day 5
1. Declare an empty list
2. Declare a list with more than 5 number of items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types,put your(name, age, height, marital status, address)
6. Declare a list variable name it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using *print()*
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print modify any of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies item to uppercase
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list. 
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies item
25. Destroy the IT companies list
26. Join the following lists:
    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
27. After joining the lists in question 26. Copy the joined list and assigned it to a variable full_stack. Then insert, Python and SQL after Redux.
28. The following is a list of 10 students ages:
```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```
  * Sort the list and find the min and max age
  * Add the min age and the max age
  * Find the median age(one middle item or two middle items divided by two)
  * Find the average age(all items divided by number of items)
  * Find the range of the ages(max minus min)
  * Compare the value of (min - average) and (max - average), use *abs()* method
29. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
30. Divide the countries list into two equal lists if it is even if not one more country for the first half.
31. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

# Day 6:
## Tuple
A tuple is a collection of different data types which is ordered and unchangeable(immutable). Tuples are written with round brackets,(). Once a tuple is created, we can not change its values. We can not add, insert, remove a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuple:
* tuple(): to create an empty tuple
* count(): to count the number of a specified item in a tuple
* index(): to find the index of a specified item in a tuple
* + operator: to join two or more tuples and to create new tuple
### Creating Tuple

* Empty tuple: Creating an empty tuple
```py
# syntax
empty_tuple = () 
# or using the tuple constructor
empty_tuple = tuple()
```
* Tuple with initial values
```py
# syntax
tpl = ('item1', 'item2','item3')
```
* 
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
```
### Tuple length
We use the *len()* method to get the length of a tuple.
```py
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```
### Accessing tuple items
* Positive Indexing
Similar to the list data type we use positive or negative indexing to access tuple items.
![Accessing tuple items](images/tuples_index.png)

```py
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[las_index]
```
* Negative indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list length refers to the first item.
![Tuple Negative indexing](images/tuple_negative_indexing.png)
```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
```
### Slicing tuples
We can slice out a sub tuple by  specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

* Range of Positive Indexes

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
```

* Range of Negative Indexes

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
```
### Changing tuples to list
We can change tuples to list and list to tuple. Tuple is immutable if we want to modify a tuple we should change to a list.
```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```
### Checking an item in a list
We can check an item if it exists in a list or not using *in*, it returns boolean.
```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')
'orange' in fruits # True
'apple' in fruits # False
fruits[0] = 'apple'
```
### Joining tuples
We can join two or more tuples using + operator
```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```
```py
fruits = ('banana', 'orange', 'mango', 'lemon')                    
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables 
```
### Deleting tuple
It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using *del*.
```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

```
```py
fruits = ('banana', 'orange', 'mango', 'lemon') 
del fruits                  
```


## Exercises: Day 6
1. Create an empty tuple
2. Create a tuple containing name of your sisters and your brothers
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have ?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
6. Unpack siblings and parents from family_members
7. Create a fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff. 
8. Slice out the middle item or items from the food_staff list
9. Slice out the first three items and the last three items from food_staff list
10. Delete the food_staff list completely
11. Check if an item exist in a tuple:
* Check if 'Estonia' is a nordic country
* Check if 'Iceland' is a nordic country
  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```





 








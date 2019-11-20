

![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)
- [Day 1](#day-1)
  - [Welcome](#welcome)
  - [Introduction](#introduction)
  - [Why Python ?](#why-python)
  - [Environment Setup](#environment-setup)
    - [Installing Python](#installing-python)
    - [Python Shell](#python-shell)
    - [Installing Visual Studio Code](#installing-visual-studio-code)
      - [How to visual studio code](#how-to-visual-studio-code)
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
    - [Number](#number-1)
  - [String](#string-1)
  - [Boolean](#boolean)
  - [Exercises - Day 1](#exercises---day-1-1)

# Day 1
## Welcome
**Congratulations** for deciding to participate in a ***30 days of Python*** programming challenge . In this challenge you will learn everything you need to be a python programmer and the whole concepts of programming. In the end of the challenge you will get a ***30DaysOfPython*** programming challenge certificate. [Join the telegram channel](https://t.me/ThirtyDaysOfPython)
## Introduction
Python is a high-level programming language. It is an open source. This 30 days python challenge will help you learn the latest version of Python, Python 3 step by step. The topics are broken down into 30 days, where each days contains several topics with easy-to-understand explanations, real-world examples and many hands on exercises.

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
![Pyhton Version](./images/python_versio.png)


As you can see from the terminal, I am using *python 3.7.5* version at the moment. If you mange to see the python version, well done. Python has been installed on your machine. Continue to the next section.  

### Python Shell
Python is an interpreter scripting language. It means it executes the code line by line. Python comes with  a *Python Shell (Python Interactive Shell)*. It is used to execute a single python command and get the result.

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
#### How to visual studio code
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
Indentation in many languages used to increase code readability, however python uses indentation to create block of codes. In other programming languages curly bracket used instead of indentation. One of the common bug when you write a python code will be wrong indentation.

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
 A collection of one or more characters under in single or double quote. If a string is more than one sentence we use triple quote.

 **Example:**
```py
'Asabeneh'
'Finland'
"Python"
"I love teaching"
"I hope you are enjoying the first day"
```
#### Booleans
A boolean data type is either True or False value.

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
{"name":"Asabeneh", "country":"Finland", age:250, "is_married":True}
```
#### Tuple
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

 **Example**
```py
    ('Asabeneh', 'Brook', 'Abraham', 'Lidiya')
```
#### Set
A set is a collection data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in mathematics, set in python store only unique elements.

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
    print(2 + 3)   # addition(+)
    print(3 - 1)   # subtraction(-)
    print(2 * 3)   # multiplication(*)
    print(3 / 2)   # division(/)
    print(3 ** 2)  # exponential(**)
    print(3 % 2)   # modulus(%)
    print(3 // 2)  # Floor division operator(//)
    # Checking data types
    print(type(10))                  # Int 
    print(type(3.14))                # Float 
    print(type(1 + 3j))              # Complex number
    print(type('Asabeneh'))          # String 
    print(type([1, 2, 3]))           # List 
    print(type({'name':'Asabeneh'})) #Dictionary
    print(type({9.8, 3.14, 2.7}))    #Tuple
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
     - exponential
     - floor division operator(//).
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
In python we have lots of built in functions. Built-in functions are globally available for your use. Some of the built in functions used frequently in python such as: *print()*, *len()*, *type()*, *int()*, *float()*, *str()*, *input()*, *list()*, *dict()*, *min()*, *max()*, *sum()*,*sorted*, *open*,*file*, *help()*, *dir*. In the following table you will see an exhaustive list of python built in functions taken from [python documentation](https://docs.python.org/2/library/functions.html).

![Built in Functions](images/builtin-functions.png)
Let's open the python shell and start using the some of the most common built in functions. 
![Built in functions](images/builtin-functions_practice.png)

Let's practice more by using different built-in functions

![Help and Dir Built in Functions](/images/help_and_dir_builtin.png)

As you can see from the above terminal, python has reserved words. We do not use reserved words to declare variables or functions. We will cover variables in the next section.

I believe, by now you are familiar with built-in functions. Let's do one more practice of built-in functions and we will move on to the next section
![Min Max Sum](images/builtin-functional-final.png)


## Variables
Variables are store data in a computer memory. Mnemonic variables recommend to use in many programming languages. A variable refers to an address in which a data is stored.
Number at the beginning, special character, hyphen are not allowed. A variable can have a short name (like x,y,z) or a more descriptive name (firstname, lastname, age, country).

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
_if # if we want to use reservered word as a variable
first_name
year_2019
year2019
current_year_2019
num1
num2
```
Invalid varaible names
```shell
first-name
num-1
1num
```
 We will use standard python variable naming style which has been adopted by many python developers. The example below is an example of standard naming of variables, underscore when the variable name is long.

 When we assign a certain data type to a variable is called variable declaration. For instance in the example below the my first name is assigned to a variable first_name. The equal sign is an assignment operator.Assigning means storing data in the variable.
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
 Example
 ```py
 print('Hello, World!')
 print('Hello',',', 'World','!') # it can take multiple arguments
 print(len('Hello, World!')) # it takes only on argument
 ```

 Let's print and also find  the length of the variables declared at the top:
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
 ```py
 first_name = input('What is your name: ')
 age = input('How old are you? ')
 print(first_name)
 print(age)
 ```

 ## Data Types
 Different data types in python. There are different data type in python programming. To identify the data tpe we use the type method. In this section, we will see data types in detail.
 ```py
 # Different python data types
# Let's declare different data types

first_name = 'Asabeneh' # String
last_name = 'Yetayeh' # String
country = 'Finland' # String
city= 'Helsinki'
age = 250 # Number, it is not my real age, don't worry about it

print(type('Asabeneh'))
print(type(first_name))
print(type(10))
print(type(3.14))
print(type(1 + 1j))
print(type(True))
print(type([1, 2,3,4]))
print(type({"name":"Asabeneh","age":250, "is_married":250}))
print(type((1,2)))
print(type(zip([1,2],[3,4])))
 ``` 
 ### Number
  1. Integers
  2. Floating Numbers
  3. Complex Numbers

 Numbers are python data types. Arithmetic Operators: +, -, *, /
 ```py
 # Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2) # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2) # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)
print ('Division without the remainder: ',7 // 3)
print('Exponential: ', 3 ** 2)
# Floating numbers
print('Floating Number', 3.14)
# Complex numbers
print('Complex number: ', 1+1j)
print('Multiplying complex number: ',(1+1j) * (1-1j))


print('== Addition, Subtraction, Multiplication, Division, Modules ==')

num_one = 3
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

print('sum: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

mass = 75
gravity = 9.81
# Calculate the weight of the object on planet earth
weight = mass * gravity

print(weight, 'N')
 ```

## String
## Boolean

## Exercises - Day 1
1. Create a folder called day_2. Inside this folder create a file name called variables.py
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
    1.  Add num_one and num_two and assign the value to a variable *add*
    2.  Subtract num_two from num_one and assign the value to a variable *dif*
    3.  Multiply num_two and num_one and assign the value to a variable *mul*
    4.  Divide num_one by num_two and assign the value to a variable *div*
    5.  Use modulus division to find num_two divided by  num_one and assign the value to a variable *remainder*
    6.  Calculate num_one the  power of num_two and assign the value to a variable *exp*
    7.  Find floor division of num_one by num_two and assign the value to a variable *floor_div*
18. The radius of a circle is 30 meters.
    1.  Calculate the area of a circle and assign the value to a variable *area_of_circle*
    2.  Calculate the circumference of a circle and assign the value to a variable *circum_of_circle*
    3.  Take radius as user input and calculate the area. 
19. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
20. Run help('keywords') on python shell or in your file check the reserved words





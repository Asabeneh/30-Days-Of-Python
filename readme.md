

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
  - [Variables](#variables)

# Day 1
## Welcome
**Congratulations** for deciding to participate in a 30 days of Python programming challenge . In this challenge you will learn everything you need to be a python programmer and the whole concept of programming. In the end of the challenge you will get a 30DaysOfPython programming challenge certificate.
## Introduction
Python is a high-level programming language. It is an open source. This 30 days challenge will help you learn the latest version of Python, Python 3 step by step. The topics are broken down into 30 days, where each days contains several topics with easy-to-understand explanations, real-world examples and many hands on exercise.

This challenge is designed for beginners and professionals who want to learn Python programming language.
## Why Python ?
It is a programming language which is very close to human language and because of that it is easy to learn and easy to use. 
Python used in varies industries including Google. It has been used to develop web application, desktop application, machine learning libraries. Python is highly embraced language in the data science and machine learning community. I hope this is enough to convince you to start learning python. Python is eating the world and you are killing it before it eats you.

## Environment Setup

### Installing Python
To run python script you need to install python. Let's [download](https://www.python.org/) python.
If your are a windows user. Click the button encircled in red.

[![installing on Windows](./images/installing_on_windows.png)](https://www.python.org/)

If you are a  macOS user. Click the button encircled in red.

[![installing on Windows](./images/installing_on_macOS.png)](https://www.python.org/)

To check if python is installed write the following command on your device terminal
```shell
python --version
```
![Pyhton Version](./images/python_versio.png)

As you can see from the terminal, I am using python 3.7.5 version at the moment. If you mange to see the python version, well done. Python has been installed to you machine. Continue to the next section.  

### Python Shell
Python is an interpreter scripting language. It means it executes the code line by line. Python comes with  a Python Shell (Python Interactive Shell). It is used to execute a single Python command and get the result.

Python Shell waits for the python code from the user. When you enter the code, it interprets the code and shows the result.
Open your terminal or cmd and write:
```shell
python
```
![Python Scripting Shell](images/opening_python_shell.png)

The python interactive shell is opened and it is waiting for you to write python code. You will write your python script next to this symbol >>> and then click Enter.
Lets write our very first script on the python scripting shell.

![Python script on python shell](images/adding_on_python_shell.png)

Well done, you wrote your first python script on python interactive shell. How do we close this shell ?
To close the shell, next to >> write **exit()** command and press Enter

![Exit from python shell](images/exit_from_shell.png)
Now, you knew how to open the python interactive shell and how exit from it. 

Python can do give you result if write script what python understands if not it returns errors. Let's make a deliberate mistake and see what python will return

![Invalid Syntax Error](./images/invalid_syntax_error.png)

As you can see from the returned error, python is so clever that it knows the mistake we made and which was invalid syntax. Using X as multiplication in python is not (**x**) a valid instead  we use asterisk (*). The returned error clearly shows what to fix. 
The process of identifying and removing errors from a program is called debugging. Lets debug it by using * instead of **x**. 

![Fixing Syntax Error](./images/fixing_syntax_error.png)

Our bug was fixed and the code run and we got a result. As a programmer you will see such kind of errors on daily basis. It is good to know how to debug. To be good at debugging you should understand what kind of errors you are facing:SyntaxError, IndexError, ModuleNotFoundError, KeyError, ImportError etc. We will see more about different python ***error types*** in later section .

Let's practice more , how to use python interactive shell. Go to your terminal or command prompt and write the word **pyhton**

![Python Scripting Shell](images/opening_python_shell.png)

The python interactive shell is open and lets do some basic maths(addition, subtraction, multiplication, division, modulus, exponential). 
Lets do some maths first before we write any python code:
- 2 + 3 = 5
- 3 - 2 = 1
- 3 * 2 = 6
- 3 / 2 = 1.5
- 3 ^ 2 = 3 x 3 = 9

In python we have the following additional operations:
- 3 % 2 = 1  => which means finding the remainder
- 3 // 2 = 1 => which means removing the remainder

Lets change all what we wrote to code. The python shell has opened and lets write a comment at the very beginning of the shell.
Python does not run the comment part. So we can leave some text in our code to make our code more readable 
This is a how you write comment in python
```shell
 # comment starts with hash,
 # this is a python comment itself because it starts with a (#) symbol
```

![Maths on python shell](./images/maths_on_python_shell.png)

Before we move on to the next section, lets practice more on the python interactive shell. Close the opened shell by writing **exit()** on the shell and open it again and lets practice how to write text on the python shell.
![Writng String on python shell](images/writing_string_on_shell.png)

### Installing Visual Studio Code
The python interactive shell is good to try and test small script codes but it won't be for a big  project. In real work environment, developers use different coding editors to write code. In this 30 days python programming challenge we will use visual studio code. Visual studio code is a very popular open source text editor. I am a fn of vscode and I would recommend to [download](https://code.visualstudio.com/) visual studio code, but if you are in favor of other editors, feel free to follow with what you have.

[![Visual Studio Code](./images/vscode.png)](https://code.visualstudio.com/)
If you installed visual studio code, lets see how to use it.
#### How to visual studio code
Open the visual studio code by double click the visual studio icon. When you open it you will get this kind of interface. Try to interact with the labelled icons.
![Visual studio Code](images/vscode_ui.png)

Create a folder name 30DaysOfPython on your desktop. Then open it using visual studio code.

![Opening Project on Visual studio](./images/how_to_open_project_on_vscode.png)
![Opening a project](./images/opening_project.png)

After you opened you can create file and folder inside the your project directory which is 30DaysOfPython. As you can see bellow, I have created the very first file, helloworld.py. You can do the same.
![Creating a python file](./images/helloworld.png)

After a long day of coding, this is it, you will close the project.
![Closing project](./images/closing_opened_project.png)
Congratulations, you have finished setting up the development environment. Let's start coding.

## Basic Python 
### Comment
Comment is very important to make code more readable and to leave to remark in our code. Python doesn't run comment part of our code.
Any text starts with hash(#) in python is a comment.
Example
```shell
# This is the first comment
# This is the second comment
# Python is eating the world
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
    Example:
    'Asabeneh'
    'Finland'
    "Python"
    "I love teaching"
    "I hope you are enjoying the first day"
#### Booleans
A boolean data type is either True or False value.
    Example: 
    True -> if the light is on, if it is on the value is True
    ,False -> if the light is off,then the value is False
#### List
Python list is an ordered collection which allows to store of different data type items. A list is similar to an array in JavaScript
    Example:
        ['Banana', 'Orange', 'Mango', 'Avocado'] -> all the same data type in the list
        ['Banana', 10, False, 9.81] => different data types in the list

#### Dictionary
A python  dictionary object is an unordered collection of data in a key:value pair.

    Example: 
    {"name":"Asabeneh", "country":"Finland", age:250, "is_married":True}
#### Tuple
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.
    Example
    ('Asabeneh', 'Brook', 'Abraham', 'Lidiya')
#### Set
A set is a collection data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in mathematics, set in python store only unique elements.
    Example
    {3.14, 9.81, 2.7} -> order is not important in set
### Checking Data types
To check the data type of a certain data type we use the **type**
### Python File
First open your project folder, 30DaysOfPython. If you don't have this folder,create a folder name called 30DaysOfPython. In side this folder, create a file called helloworld.py. Now, let's do what we did on python interactive shell on visual studio code.
The python interactive shell was printing with using **print** but on visual studio code to see our result we should use a built in function **print**.

![Checking Data types](./images/checking_data_types.png)

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
    print(type(1 + 3j))              # Complex
    print(type('Asabeneh'))          # String
    print(type([1, 2, 3]))           # List
    print(type({'name':'Asabeneh'})) #Dictionary
    print(type({9.8, 3.14, 2.7}))    #Tuple)
```
![Running python script](./images/running_python_script.png)


## Exercises - Day 1
  1. Check the python version you are using
  1. Open the python interactive shell and do  the following operations. The operands are 3 and 4. Check the example above
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
 1. Check the data types of the following data:
    - 10
    - 9.8
    - 3.14
    - 4 - 4j
    - ['Asabeneh', 'Python', 'Finland']
    - Your name
    - Your family name
    - Your country
 1. Create python file day_1.py and repeat question 1, 2, 3 and 4. Remember to use print when you are working on a python file. Then run the file.


# Day 2
## Variables




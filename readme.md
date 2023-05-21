# 🐍 30 Days Of Python 

|# Day | Topics                                                    |
|------|:---------------------------------------------------------:|
| 01  |  [Introduction](./readme.md)|
| 02  |  [Variables, Built-in Functions](./02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)|
| 03  |  [Operators](./03_Day_Operators/03_operators.md)|
| 04  |  [Strings](./04_Day_Strings/04_strings.md)|
| 05  |  [Lists](./05_Day_Lists/05_lists.md)|
| 06  |  [Tuples](./06_Day_Tuples/06_tuples.md)|
| 07  |  [Sets](./07_Day_Sets/07_sets.md)|
| 08  |  [Dictionaries](./08_Day_Dictionaries/08_dictionaries.md)|
| 09  |  [Conditionals](./09_Day_Conditionals/09_conditionals.md)|
| 10  |  [Loops](./10_Day_Loops/10_loops.md)|
| 11  |  [Functions](./11_Day_Functions/11_functions.md)|
| 12  |  [Modules](./12_Day_Modules/12_modules.md)|
| 13  |  [List Comprehension](./13_Day_List_comprehension/13_list_comprehension.md)|
| 14  |  [Higher Order Functions](./14_Day_Higher_order_functions/14_higher_order_functions.md)|     
| 15  |  [Python Type Errors](./15_Day_Python_type_errors/15_python_type_errors.md)| 
| 16 |  [Python Date time](./16_Day_Python_date_time/16_python_datetime.md) |     
| 17 |  [Exception Handling](./17_Day_Exception_handling/17_exception_handling.md)|    
| 18 |  [Regular Expressions](./18_Day_Regular_expressions/18_regular_expressions.md)|    
| 19 |  [File Handling](./19_Day_File_handling/19_file_handling.md)|
| 20 |  [Python Package Manager](./20_Day_Python_package_manager/20_python_package_manager.md)|
| 21 |  [Classes and Objects](./21_Day_Classes_and_objects/21_classes_and_objects.md)|
| 22 |  [Web Scraping](./22_Day_Web_scraping/22_web_scraping.md)|
| 23 |  [Virtual Environment](./23_Day_Virtual_environment/23_virtual_environment.md)|
| 24 |  [Statistics](./24_Day_Statistics/24_statistics.md)|
| 25 |  [Pandas](./25_Day_Pandas/25_pandas.md)|
| 26 |  [Python web](./26_Day_Python_web/26_python_web.md)|
| 27 |  [Python with MongoDB](./27_Day_Python_with_mongodb/27_python_with_mongodb.md)|
| 28 |  [API](./28_Day_API/28_API.md)|
| 29 |  [Building API](./29_Day_Building_API/29_building_API.md)|
| 30 |  [Conclusions](./30_Day_Conclusions/30_conclusions.md)|

🧡🧡🧡 HAPPY CODING 🧡🧡🧡


<div align="center">
  <h1> Python за 30 дней: День 1 - Знакомство с Python</h1>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Второе издание: июль, 2021</small>
  </sub>
</div>


[День 2 >>](./02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)

![Python за 30 дней](./images/30DaysOfPython_banner3@2x.png)

- [🐍 Python за 30 дней](#-30-days-of-python)
- [📘 День 1](#-day-1)
  - [Приветствие](#welcome)
  - [Знакомство с Python](#introduction)
  - [Почему Python?](#why-python-)
  - [Установка среды](#environment-setup)
    - [Установка Python](#installing-python)
    - [Python Shell](#python-shell)
    - [Установка Visual Studio Code](#installing-visual-studio-code)
      - [Как пользоваться visual studio code?](#how-to-use-visual-studio-code)
  - [Основы Python](#basic-python)
    - [Синтаксис Python](#python-syntax)
    - [Отступы в Python](#python-indentation)
    - [Комментарии](#comments)
    - [Типы данных](#data-types)
      - [Числа](#number)
      - [Строки](#string)
      - [Булевый тип данных](#booleans)
      - [Список](#list)
      - [Словарь](#dictionary)
      - [Кортеж](#tuple)
      - [Множество](#set)
    - [Определение типа данных](#checking-data-types)
    - [Файл Python](#python-file)
  - [💻 Упражнения - День 1](#-exercises---day-1)
    - [Упражнения: Уровень 1](#exercise-level-1)
    - [Упражнения: Уровень 2](#exercise-level-2)
    - [Упражнения: Уровень 3](#exercise-level-3)

# 📘 День 1

## Приветствие

**Поздравляем и добро пожаловать!** Раз вы здесь, значит вы решились бросить себе вызов и присоединиться к нам в изучении _Python за 30 дней_ . Из наших уроков вы узнаете всё необходимое, чтобы программировать на python, и поймете, что вообще программирование из себя предсталвяет. После успешного выполнения программы вы получите сертификат _30DaysOfPython_ .

Для активного участия при желании можете вступить в чат в telegram: [30DaysOfPython challenge](https://t.me/ThirtyDaysOfPython).  

## Знакомство с Python

Python - это высокоуровневый язык программирования общего назначения. Python - язык open source (с открытым исходным кодом), а также интерпретируемый и объектно-ориентированный. Создатель Python - Гвидо ван Россум, нидерландский программист. Название данного языка программирования заимствовано из британского комедийного скетч-сериала, *Летающий цирк Монти Пайтона*. Первая версия вышла 20 февраля 1991 года. Челлендж **Python за 30 дней** постепенно познакомит вас с последней версией Python - Python 3. Темы разделены на 30 блоков на 30 дней соответственно. В каждом из них вы найдете объяснение темы доступным языком, реальные примеры и множество упражнений для практики.

Данный челлендж предназначен для интересующихся языком программирования python: от начинающих до профессионалов. Его изучение может занять у вас от 30 до 100 дней. Активные участники чата в telegram имеют все шансы справиться успешно.

Материал написан простым языком. **Python за 30 дней** поможет вам активно влиться в процесс изучения и поддерживать мотивацию, однако без ваших стараний не обойтись. Вам потребуется отвести на занятия много времени, чтобы успешно освоить программу. Тем, кто предпочитает воспринимать информацию визуально, рекомендуем обратить внимание на видео-уроки на YouTube-канале <a href="https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw"> Washera</a>. Для начала посмотрите видео [Python for Absolute Beginners video](https://youtu.be/OCCWZheOesI). Подписывайтесь на канал, оставляйте комментарии и задавайте вопросы. Автор обязательно заметит вашу активность.

Автору важно знать ваше мнение. Вы можете оставить отзыв здесь: [ссылка](https://testimonial-vdzd.onrender.com/)

## Почему Python?

Это язык программирования, очень близкий к языку человеческому. За счет этого понимать его и работать с ним довольно просто.
Python используется в работе крупных компаний(включая Google). Он применяется для разработки веб-приложений, десктопных приложений, а также для системного администрирования и машинного обучения. Python широко распространен среди датасаентистов и специалистов по машинному обучению. Надеемся, этого достаточно, чтоб убедить вас начать свой путь в изучении Python. Python захватывает мир: либо вы укротите его, либо он вас.

## Установка среды

### Установка Python

Для запуска кода на python вам необходимо его установить: [ссылка](https://www.python.org/).

Пользователям windows: нажмите на кнопку, обведенную красной рамкой.

[![установка на Windows](./images/installing_on_windows.png)](https://www.python.org/)

Пользователям macOS: нажмите на кнопку, обведенную красной рамкой.

[![установка на macOS](./images/installing_on_macOS.png)](https://www.python.org/)

Проверьте, что python установлен: введите в терминал следующую команду:

```shell
python --version
```

![Python Version](./images/python_versio.png)

Мы сейчас используем версию _Python 3.7.5_, согласно терминалу. У вас может быть установлена другая версия, но не ниже 3.6. Если вы видите у себя в терминале версию python, значит всё отлично. Python установлен на ваше устройство. Двигаемся дальше.

### Python Shell

Python - интерпретируемый скриптовый язык, он не требует компиляции. Это означает, что код выполняется строка за строкой. Python работает при помощи _Python Shell (Python Interactive Shell)_: выполняются команды, написанные на python, и мы получаем результат.

Для работы Python Shell нужен код на языке Python от пользователя. Вы вводите код, он интерпретируется, и в следующей строке появляется результат.
Откройте свой терминал или командную строку и введите:

```shell
python
```

![Python Scripting Shell](./images/opening_python_shell.png)

Python Shell готов к работе, осталось лишь написать код. После символа >>> вводите свой код и нажимайте Enter.
Время написать наш первый код!

![Python script on Python shell](./images/adding_on_python_shell.png)

Поздравляем, вы написали свой первый код на языке Python в Python Shell. Как же теперь его закрыть?
После символа >> введите команду **exit()** и нажмите Enter.

![Exit from python shell](./images/exit_from_shell.png)

Теперь вы умеете открывать и закрывать Python Shell.

Python выдаст вам результат только в случае отсутствия ошибок, то есть если Python понимает ваш код. Давайте специально допустим ошибку и посмотрим, что вернет нам Python.

![Invalid Syntax Error](./images/invalid_syntax_error.png)

Как видите, Python настолько умный, что он сам понимает, какую ошибку мы допустили: _Syntax Error: invalid syntax_. Использовать символ x для перемножения в Python неправильно, это синтаксическая ошибка. Вместо символа (**x**) для перемножения используется звездочка (*). Ошибка, которую вернул нам Python, четко дает понять, что именно нужно исправить.

Процесс обнаружения и устранения ошибок в программе назывется *отладкой*. Давйте исправим ошибку, поставив звездочку * на место символа **x**.

![Fixing Syntax Error](./images/fixing_syntax_error.png)

Ошибка устранена, код работает и приводит к нужному результату. При работе программистом вы будете встречаться с подобными ошибками постоянно. Важно знать, как их исправлять. Для этого необходимо научиться понимать, с какими ошибками вы сталкиваетесь. Например, вот такие ошибки вы можете встретить в случае с Python: *SyntaxError*, *IndexError*, *NameError*, *ModuleNotFoundError*, *KeyError*, *ImportError*, *AttributeError*, *TypeError*, *ValueError*, *ZeroDivisionError* и др. Больше различных **_видов ошибок_** в Python мы рассмотрим в следующих разделах.

Время ещё попрактиковаться в использовании Python Shell! Откройте терминал или командную строку и введите слово **python**.

![Python Scripting Shell](./images/opening_python_shell.png)

Вы открыли Python Shell. Давайте попробуем выполнить простые математические операции (сложение, вычитание, умножение, деление, нахождение остатка от деления, возведение в степень).

Прежде чем начать писать код, для начала вспомним немного математики:

- 2 + 3 = 5
- 3 - 2 = 1
- 3 \* 2 = 6
- 3 / 2 = 1.5
- 3 ^ 2 = 3 x 3 = 9

В python есть дополнительные операции:

- 3 % 2 = 1 => для нахождения остатка от деления
- 3 // 2 = 1 => для нахождения целой части от деления

Теперь превратим математические выражения в код на Python. Напишем комментарий в самом начале Python Shell. 

_Комментарий_ - это часть кода, которую python не выполняет. Так что мы можем добавить в наш код текст, чтобы сделать его более читаемым. Комментарии в python начинаются со знака решетки (#).
Вот так пишутся комментарии в python:

```shell
 # комментарий начинается со знака решетки
 # это комментарий, т.к. он начинается со знака решетки (#)
```

![Maths on python shell](./images/maths_on_python_shell.png)

Прежде чем перейти к следующему разделу, давайте еще потренируемся работать с Python Shell. Введите команду _exit()_ и закройте Python shell, затем откройте заново и приступайте к практике. 

![Writing String on python shell](./images/writing_string_on_shell.png)

### Установка Visual Studio Code

The Python interactive shell is good to try and test small script codes but it will not be for a big project. In real work environment, developers use different code editors to write codes. In this 30 days of Python programming challenge we will use visual studio code. Visual studio code is a very popular open source text editor. I am a fan of vscode and I would recommend to [download](https://code.visualstudio.com/) visual studio code, but if you are in favor of other editors, feel free to follow with what you have.

[![Visual Studio Code](./images/vscode.png)](https://code.visualstudio.com/)

If you installed visual studio code, let us see how to use it.
If you prefer a video, you can follow this Visual Studio Code for Python [Video tutorial](https://www.youtube.com/watch?v=bn7Cx4z-vSo)

#### How to use visual studio code

Open the visual studio code by double clicking the visual studio icon. When you open it you will get this kind of interface. Try to interact with the labeled icons.

![Visual studio Code](./images/vscode_ui.png)

Create a folder named 30DaysOfPython on your desktop. Then open it using visual studio code.

![Opening Project on Visual studio](./images/how_to_open_project_on_vscode.png)

![Opening a project](./images/opening_project.png)

After opening it you will see shortcuts for creating files and folders inside of 30DaysOfPython project's directory. As you can see below, I have created the very first file, helloworld.py. You can do the same.

![Creating a python file](./images/helloworld.png)

After a long day of coding, you want to close your code editor, right? This is how you will close the opened project.

![Closing project](./images/closing_opened_project.png)

Congratulations, you have finished setting up the development environment. Let us start coding.

## Basic Python

### Python Syntax

A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

### Python Indentation

An indentation is a white space in a text. Indentation in many languages is used to increase code readability, however Python uses indentation to create block of codes. In other programming languages curly brackets are used to create blocks of codes instead of indentation. One of the common bugs when writing python code is wrong indentation.

![Indentation Error](./images/indentation.png)

### Comments

Comments are very important to make the code more readable and to leave remarks in our code. Python does not run comment parts of our code.
Any text starting with hash(#) in Python is a comment.

**Example: Single Line Comment**

```shell
    # This is the first comment
    # This is the second comment
    # Python is eating the world
```

**Example: Multiline Comment**

Triple quote can be used for multiline comment if it is not assigned to a variable

```shell
"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""
```

### Data types

In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

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

A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

**Example:**

```py
'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
```

#### Booleans

A boolean data type is either a True or False value. T and F should be always uppercase.

**Example:**

```python
    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False
```

#### List

Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

**Example:**

```py
[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float
```

#### Dictionary

A Python dictionary object is an unordered collection of data in a key value pair format. 

**Example:**

```py
{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
```

#### Tuple

A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

**Example:**

```py
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
```

```py
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets
```

#### Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

**Example:**

```py
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set
```

### Checking Data types

To check the data type of certain data/variable we use the **type** function. In the following terminal you will see different python data types:

![Checking Data types](./images/checking_data_types.png)

### Python File

First open your project folder, 30DaysOfPython. If you don't have this folder, create a folder name called 30DaysOfPython. Inside this folder, create a file called helloworld.py. Now, let's do what we did on python interactive shell using visual studio code.

The Python interactive shell was printing without using **print** but on visual studio code to see our result we should use a built in function *print(). The *print()* built-in function takes one or more arguments as follows *print('arument1', 'argument2', 'argument3')*. See the examples below.

**Example:**

The file name is helloworld.py

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

To run the python file check the image below. You can run the python file either by running the green button on Visual Studio Code or by typing *python helloworld.py* in the terminal .

![Running python script](./images/running_python_script.png)

🌕  You are amazing. You have just completed day 1 challenge and you are on your way to greatness. Now do some exercises for your brain and muscles.

## 💻 Exercises - Day 1

### Exercise: Level 1

1. Check the python version you are using
2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
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

### Exercise: Level 2

1. Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use _print()_ when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

### Exercise: Level 3

1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
2. Find an [Euclidian distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between (2, 3) and (10, 8)

🎉 CONGRATULATIONS ! 🎉

[Day 2 >>](./02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)

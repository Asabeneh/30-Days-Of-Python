# 🐍 30 днів з Python 

| № дня |                                                  Теми                                                   |
|-------|:-------------------------------------------------------------------------------------------------------:|
| 01    |                                          [Вступ](../readme.md)                                           |
| 02    | [Variables, Built-in Functions](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) |
| 03    |                             [Operators](../03_Day_Operators/03_operators.md)                             |
| 04    |                                [Strings](../04_Day_Strings/04_strings.md)                                |
| 05    |                                   [Lists](../05_Day_Lists/05_lists.md)                                   |
| 06    |                                 [Tuples](../06_Day_Tuples/06_tuples.md)                                  |
| 07    |                                    [Sets](../07_Day_Sets/07_sets.md)                                     |
| 08    |                        [Dictionaries](../08_Day_Dictionaries/08_dictionaries.md)                         |
| 09    |                        [Conditionals](../09_Day_Conditionals/09_conditionals.md)                         |
| 10    |                                   [Loops](../10_Day_Loops/10_loops.md)                                   |
| 11    |                             [Functions](../11_Day_Functions/11_functions.md)                             |
| 12    |                                [Modules](../12_Day_Modules/12_modules.md)                                |
| 13    |               [List Comprehension](../13_Day_List_comprehension/13_list_comprehension.md)                |
| 14    |         [Higher Order Functions](../14_Day_Higher_order_functions/14_higher_order_functions.md)          |     
| 15    |               [Python Type Errors](../15_Day_Python_type_errors/15_python_type_errors.md)                | 
| 16    |                   [Python Date time](../16_Day_Python_date_time/16_python_datetime.md)                   |     
| 17    |               [Exception Handling](../17_Day_Exception_handling/17_exception_handling.md)                |    
| 18    |              [Regular Expressions](../18_Day_Regular_expressions/18_regular_expressions.md)              |    
| 19    |                       [File Handling](../19_Day_File_handling/19_file_handling.md)                       |
| 20    |         [Python Package Manager](../20_Day_Python_package_manager/20_python_package_manager.md)          |
| 21    |              [Classes and Objects](../21_Day_Classes_and_objects/21_classes_and_objects.md)              |
| 22    |                        [Web Scraping](../22_Day_Web_scraping/22_web_scraping.md)                         |
| 23    |              [Virtual Environment](../23_Day_Virtual_environment/23_virtual_environment.md)              |
| 24    |                           [Statistics](../24_Day_Statistics/24_statistics.md)                            |
| 25    |                                 [Pandas](../25_Day_Pandas/25_pandas.md)                                  |
| 26    |                           [Python web](../26_Day_Python_web/26_python_web.md)                            |
| 27    |              [Python with MongoDB](../27_Day_Python_with_mongodb/27_python_with_mongodb.md)              |
| 28    |                                      [API](../28_Day_API/28_API.md)                                      |
| 29    |                        [Building API](../29_Day_Building_API/29_building_API.md)                         |
| 30    |                          [Conclusions](../30_Day_Conclusions/30_conclusions.md)                          |

🧡🧡🧡 ЩАСЛИВОГО ПРОГРАМУВАННЯ 🧡🧡🧡

<div>
<small>Підтримайте <strong>автора</strong>, щобм він створював більше навчальних матеріалів</small> <br />  
<a href = "https://www.paypal.me/asabeneh"><img src='../images/paypal_lg.png' alt='Paypal Logo' style="width:10%"/></a>
</div>

<div align="center">
  <h1> 30 днів Python: День 1 - Вступ</h1>  
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social" alt="">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Друге видання: Липень, 2021</small>
  </sub>
</div>


[День 2 >>](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)

![30 днів з Python](../images/30DaysOfPython_banner3@2x.png)

- [🐍 30 днів Python](#-30-days-of-python)
- [📘 День 1](#-day-1)
  - [Ласкаво просимо](#ласкаво-просимо)
  - [Вступ](#вступ)
  - [Чому Python ?](#чому-python-)
  - [Налаштування середовища](#налаштування-середовища)
    - [Установлення Python](#установлення-python)
    - [Оболонка Python](#оболонка-python)
    - [Установлення Visual Studio Code](#установлення-visual-studio-code)
      - [Як використовувати Visual studio code](#як-використовувати-visual-studio-code)
  - [Початковий Python](#початковий-python)
    - [Синтаксис у Python](#синтаксис-у-python)
    - [Відступи у Python](#відступи-у-python)
    - [Коментарі](#коментарі)
    - [Типи даних](#типи-даних)
      - [Number (числовий)](#number)
      - [String (рядок)](#string)
      - [Booleans (логічний двійковий)](#booleans)
      - [List (список)](#list)
      - [Dictionary (словник)](#dictionary)
      - [Tuple (кортеж)](#tuple)
      - [Set (набір)](#set)
    - [Перевірка типів даних](#перевірка-типів-даних)
    - [Файл Python](#файл-python)
  - [💻 Вправи - День 1](#вправи--день-1)
    - [Вправи: Рівень 1](#вправи--рівень-1)
    - [Вправи: Рівень 2](#вправи--рівень-2)
    - [Вправи: Рівень 3](#вправи--рівень-3)

# 📘 День 1

## Ласкаво просимо

**Вітаємо** за прийняття рішення про участь у 30-денному виклику з програмування на Python. У цьому виклику ви дізнаєтеся все, що вам потрібно для того, щоб стати програмістом на python, і всю концепцію програмування. У кінці цього виклику ви отримаєте сертифікат про проходження виклику з програмування _30DaysOfPython_.

Якщо ви бажаєте активно долучитися до виклику, ви можете приєднатися до групи у Telegram [30DaysOfPython challenge](https://t.me/ThirtyDaysOfPython).  

## Вступ

Python - це мова програмування високого рівня для програмування загального призначення. Це об'єктно-орієнтована мова програмування з відкритим вихідним кодом, що інтерпретується. Python була створена голландським програмістом Гвідо ван Россумом. Назва мови програмування Python походить від британського скетч-комедійного серіалу "Летючий цирк Монті Пайтона".  Перша версія була випущена 20 лютого 1991 року. Цей 30-денний челендж з Python допоможе вам крок за кроком вивчити останню версію Python, Python 3. Теми розбиті на 30 днів, де кожен день містить кілька тем з простими для розуміння поясненнями, реальними прикладами, безліччю практичних вправ і проектів.

Цей челендж призначений для початківців та професіоналів, які хочуть вивчити мову програмування python. На проходження челенджу може знадобитися від 30 до 100 днів, люди, які беруть активну участь у телеграм-групі, мають високу ймовірність завершити челендж.
Якщо ви навчаєтесь з використанням візуальних засобів або віддаєте перевагу відео, ви можете почати з цього [відео з Python для абсолютних новачків (англійською)](https://www.youtube.com/watch?v=11OYpBrhdyM).

## Чому Python ?

Це мова програмування, яка дуже близька до людської мови, і тому її легко вивчати та використовувати.
Python використовується різними галузями та компаніями (включаючи Google). Її використовують для розробки веб-застосунків, настільних застосунків, системного адміністрування та бібліотек машинного навчання. Python дуже популярна мова у спільноті, що займається наукою про дані та машинним навчанням. Сподіваюся, цього достатньо, щоби переконати вас почати вивчати Python. Python поглинає світ, а ви вбиваєте його до того, як він з'їсть вас.

## Налаштування середовища

### Установлення Python

Для запуску скрипту на python, вам потрібно встановити python. Нумо [завантажимо](https://www.python.org/) Python.
Якщо ви є користувачем Windows. Натисніть кнопку, обведену червоним кольором.

[![установлення на Windows](../images/installing_on_windows.png)](https://www.python.org/)

Якщо ви є користувачем MacOS. Натисніть кнопку, обведену червоним кольором.

[![установлення на Windows](../images/installing_on_macOS.png)](https://www.python.org/)

Щоб перевірити, чи встановлено Python, напишіть наступну команду у терміналі вашого пристрою.

```shell
python --version
```

![Версія Python](../images/python_versio.png)

Як ви можете бачити з терміналу, я використовую версію _Python 3.7.5_ на даний момент. Ваша версія Python може відрізнятися від моєї, але вона має бути 3.6 або вище. Вам вдалося побачити версію python? Чудова робота, Python встановлено на вашому комп'ютері. Перейдіть до наступного розділу.

### Оболонка Python

Python - це інтерпретована скриптова мова, тому її не потрібно компілювати. Це означає, що вона виконує код рядок за рядком. Python постачається з _Python Shell (Python Interactive Shell)_. Вона використовується для виконання однієї команди python і отримання результату.

Python Shell чекає на код Python від користувача. Коли ви вводите код, вона інтерпретує його і показує результат у наступному рядку.
Відкрийте термінал або командний рядок (cmd) і напишіть:

```shell
python
```

![Скриптова оболонка Python](../images/opening_python_shell.png)

Відкриється інтерактивна оболонка Python, яка чекає на написання коду на Python (скрипт Python). Ви напишете свій скрипт Python поруч з цими символами >>>, а потім натиснете Enter.
Гайда напишемо наш перший скрипт у скриптовій оболонці Python.

![Python script on Python shell](../images/adding_on_python_shell.png)

Чудово, ви написали свій перший Python-скрипт в інтерактивній оболонці Python. Як закрити інтерактивну оболонку Python?
Щоби закрити оболонку, поруч з цим символом >> напишіть команду **exit()** і натисніть Enter.

![Вихід з оболонки Python](../images/exit_from_shell.png)

Now, you know how to open the Python interactive shell and how to exit from it.

Python will give you results if you write scripts that Python understands, if not it returns errors. Let's make a deliberate mistake and see what Python will return.

![Неправильний синтаксис](../images/invalid_syntax_error.png)

As you can see from the returned error, Python is so clever that it knows the mistake we made and which was _Syntax Error: invalid syntax_. Using x as multiplication in Python is a syntax error because (x) is not a valid syntax in Python. Instead of (**x**) we use asterisk (*) for multiplication. The returned error clearly shows what to fix.

Процес виявлення та усунення помилок у програмі називається *зневадженням (англ. debugging)*. Гайда розберемось з помилками, підставивши * замість **x**.

![Виправлення синтаксичної помилки](../images/fixing_syntax_error.png)

Our bug was fixed, the code ran and we got a result we were expecting. As a programmer you will see such kind of errors on daily basis. It is good to know how to debug. To be good at debugging you should understand what kind of errors you are facing. Some of the Python errors you may encounter are *SyntaxError*, *IndexError*, *NameError*, *ModuleNotFoundError*, *KeyError*, *ImportError*, *AttributeError*, *TypeError*, *ValueError*, *ZeroDivisionError* etc. We will see more about different Python **_error types_** in later sections.

Let us practice more how to use Python interactive shell. Go to your terminal or command prompt and write the word **python**.

![Скриптова оболонка Python](../images/opening_python_shell.png)

The Python interactive shell is opened. Let us do some basic mathematical operations (addition, subtraction, multiplication, division, modulus,  exponential).

Let us do some maths first before we write any Python code:

- 2 + 3 = 5
- 3 - 2 = 1
- 3 \* 2 = 6
- 3 / 2 = 1.5
- 3 ^ 2 = 3 x 3 = 9

In python we have the following additional operations:

- 3 % 2 = 1 => which means finding the remainder
- 3 // 2 = 1 => which means removing the remainder

Let us change the above mathematical expressions to Python code. The Python shell has been opened and let us write a comment at the very beginning of the shell.

A _comment_ is a part of the code which is not executed by python. So we can leave some text in our code to make our code more readable. Python does not run the comment part. A comment in python starts with hash(#) symbol.
This is how you write a comment in python

```shell
 # comment starts with hash
 # this is a python comment, because it starts with a (#) symbol
```

![Maths on python shell](../images/maths_on_python_shell.png)

Before we move on to the next section, let us practice more on the Python interactive shell. Close the opened shell by writing _exit()_ on the shell and open it again and let us practice how to write text on the Python shell.

![Writing String on python shell](../images/writing_string_on_shell.png)

### Установлення Visual Studio Code

Інтерактивна оболонка Python добре підходить для тестування невеликих скриптових кодів, але вона не підійде для великого проєкту. У реальному робочому середовищі розробники використовують різні редактори коду для написання коду. У цьому 30-денному виклику з програмування на Python ми будемо використовувати Visual Studio Code. Visual Studio Code - це дуже популярний текстовий редактор з відкритим вихідним кодом. Я є прихильником vscode і рекомендую [завантажити](https://code.visualstudio.com/) Visual Studio Code, але якщо ви віддаєте перевагу іншим редакторам, не соромтеся користуватися тим, що у вас є.

[![Visual Studio Code](../images/vscode.png)](https://code.visualstudio.com/)

Якщо ви встановили код Visual Studio, подивімося, як ним користуватися.
Якщо ви віддаєте перевагу відео, ви можете слідувати за цим [відео-посібнком](https://www.youtube.com/watch?v=bn7Cx4z-vSo)

#### Як використовувати Visual Studio Code

Open the visual studio code by double clicking the visual studio icon. When you open it you will get this kind of interface. Try to interact with the labeled icons.

![Visual Studio Code](../images/vscode_ui.png)

Створіть теку з назваю 30DaysOfPython на вашому робочому столі. Потім відкрийте її за допомогою Visual Studio Code.

![Відкриття проєкту у Visual studio](../images/how_to_open_project_on_vscode.png)

![Відкриття проєкту](../images/opening_project.png)

After opening it you will see shortcuts for creating files and folders inside of 30DaysOfPython project's directory. As you can see below, I have created the very first file, helloworld.py. You can do the same.

![Створення python-файлу](../images/helloworld.png)

After a long day of coding, you want to close your code editor, right? This is how you will close the opened project.

![Закриття проєкту](../images/closing_opened_project.png)

Congratulations, you have finished setting up the development environment. Let us start coding.

## Початковий Python

### Синтаксис Python

A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

### Відступи у Python

An indentation is a white space in a text. Indentation in many languages is used to increase code readability, however Python uses indentation to create block of codes. In other programming languages curly brackets are used to create blocks of codes instead of indentation. One of the common bugs when writing python code is wrong indentation.

![Indentation Error](../images/indentation.png)

### Коментарі

Comments are very important to make the code more readable and to leave remarks in our code. Python does not run comment parts of our code.
Any text starting with hash(#) in Python is a comment.

**Приклад: Single Line Comment**

```shell
    # This is the first comment
    # This is the second comment
    # Python is eating the world
```

**Приклад: Multiline Comment**

Triple quote can be used for multiline comment if it is not assigned to a variable

```shell
"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""
```

### Типи даних
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

**Приклад:**

```py
'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
```

#### Booleans

A boolean data type is either a True or False value. T and F should be always uppercase.

**Приклад:**

```python
    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False
```

#### List

Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

**Приклад:**

```py
[0, 1, 2, 3, 4, 5]  # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float
```

#### Dictionary (словник)

A Python dictionary object is an unordered collection of data in a key value pair format. 

**Приклад:**

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

**Приклад:**

```py
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
```

```py
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets
```

#### Set

A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

In later sections, we will go in detail about each and every Python data type.

**Приклад:**

```py
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set
```

### Перевірка типів даних

Для перевірки типу даних певних даних/змінних ми використовуємо функцію **type**. У наведеному нижче терміналі ви побачите різні типи даних python:

![Перевірка типів даних](../images/checking_data_types.png)

### Файл Python

По-перше, відкрийте свою теку з проєктому 30DaysOfPython. Якщо ви не маєте цієї теки, то створіть її з назвою 30DaysOfPython. Усередині цієї теки, створіть файл з назвою helloworld.py. Тепер зробімо те, що ми робили в інтерактивній оболонці python, використовуючи Visual Studio Code.

The Python interactive shell was printing without using **print** but on visual studio code to see our result we should use a built in function *print(). The *print()* built-in function takes one or more arguments as follows *print('arument1', 'argument2', 'argument3')*. See the examples below.

**Приклад:**

Назва файлу: helloworld.py

```py
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)             # додавання(+)
print(3 - 1)             # віднімання(-)
print(2 * 3)             # множення(*)
print(3 / 2)             # ділення(/)
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

Для запуску python-файл перевірте зображення нижче. Ви можете запустити файл python, натиснувши зелену кнопку на Visual Studio Code або ввівши *python helloworld.py* в терміналі.

![Запуск python-скриптк](../images/running_python_script.png)

🌕  Ви дивовижні. Ви щойно виконали завдання першого дня і вже на шляху до величі. Тепер виконайте кілька вправ для мозку та м'язів.

## 💻 Вправи - день 1

### Вправи: рівень 1

1. Перевірте версію python, яку ви використовуєте
2. Відкрийте інтерактивну оболонку python і виконайте наступні дії. Параметрами є числа 3 та 4.
   - додавання(+)
   - віднімання(-)
   - множення(\*)
   - залишок від числа(%)
   - ділення(/)
   - показник(\*\*)
   - ціла частина від числа(//)
3. Напишіть рядки в інтерактивній оболонці python. Рядки подано наступним чином:
   - Ваше ім'я
   - Ваше прізвище
   - Ваша країна
   - Я насолоджуюся 30 днями з python
4. Перевірте типи наступних даних:
   - 10
   - 9.8
   - 3.14
   - 4 - 4j
   - ['Asabeneh', 'Python', 'Finland']
   - Ваше ім'я
   - Ваше прізвище
   - Ваша країна

### Вправи: рівень 2

1. Створіть теку з назвою day_1 всередині теки 30DaysOfPython. Усередині теки day_1, створити python-файл helloworld.py і повторіть питання 1, 2, 3 та 4. Пам'ятайте використовувати _print()_ коли ви працюєте над python-файлом. Перейдіть до теки, куди ви зберегли файл, і запустіть його.

### Вправи: рівень 3

1. Напишіть приклад для різних типів даних Python, як-от Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set та Dictionary.
2. Знайдіть [Евклідову відстань](https://uk.wikipedia.org/wiki/%D0%95%D0%B2%D0%BA%D0%BB%D1%96%D0%B4%D0%BE%D0%B2%D0%B0_%D0%B2%D1%96%D0%B4%D1%81%D1%82%D0%B0%D0%BD%D1%8C) між (2, 3) та (10, 8)

🎉 ВІТАННЯ ! 🎉

[День 2 >>](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)
<div align="center">
  <h1> 30 Дней Python: День 15 - Типы ошибок в Python </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Второе издание: Июль, 2021</small>
  </sub>
</div>
</div>

[<< День 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [День 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 День 15](#-день-15)
  - [Типы ошибок в Python](#типы-ошибок-в-python)
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
  - [💻 Упражнения: День 15](#-упражнения-день-15)

# 📘 День 15

## Типы ошибок в Python

Во время написания кода очень легко опечататься или допустить одну из частых ошибок. Если наш код не может выполниться, интерпретатор Python покажет сообщение с информацией о том, где произошла ошибка и ее тип. Также иногда он может предположить, как ее можно исправить. Понимание разных типов ошибок в языках программирования поможет в быстрой отладке кода и улучшении навыков программирования.

Давайте рассмотрим наиболее частые типы ошибок. Сперва откройте интерактивную оболочку Python interactive shell. Откройте на компьютере терминал и наберите 'python'. Это откроет интерактивную оболочку python.

### SyntaxError

**Example 1: SyntaxError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>
```

Как видите, мы допустили синтаксическую ошибку, потому что забыли взять строку в круглые скобки и Python уже предлагает решение. Давайте это исправим.

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('hello world')
hello world
>>>
```

Эта ошибка называется _SyntaxError_. После исправления код был выполнен. Давайте познакомимся с еще несколькими типами ошибок.

### NameError

**Пример 1: NameError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

Как видно в сообщении выше, переменная age не определена. Это так, мы действительно не объявили переменную age, но при этом пытались вывести ее на печать, как будто объявили. Теперь давайте это исправим, объявив переменную и присвоим ей значение.

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
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

Этот тип ошибки называется _NameError_. Мы исправили эту ошибку, задав имя переменной.

### IndexError

**Пример 1: IndexError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

В примере выше Python вызвал исключение _IndexError_, потому что в списке есть только индексы от 0 до 4, поэтому индекс 5 был вне диапазона.

### ModuleNotFoundError

**Пример 1: ModuleNotFoundError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

В примере выше я умышленно добавил лишнюю s к названию модуля math и исключение _ModuleNotFoundError_ было вызвано. Давайте это исправим, убрав лишнюю s из math.

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

Мы исправили ошибку, так что давайте используем несколько функций из модуля math.

### AttributeError

**Пример 1: AttributeError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>>
```

Как видите, я снова допустил ошибку! Вместо pi я пытался вызвать функцию PI из модуля maths. Это вызвало исключение attribute error, это означает, что функция отсутствует в модуле. Давайте исправим ошибку, изменив PI на pi.

```py
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793
>>>
```

Теперь когда мы вызываем pi из модуля math мы получаем результат.

### KeyError

**Пример 1: KeyError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'имя':'Иван', 'возраст':250, 'страна':'Россия'}
>>> users['имя']
'Иван'
>>> users['стрна']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'стрна'
>>>
```

Как вы можете видеть, при попытке получить значение словаря по ключу была допущена ошибка. Поэтому это исключение key error и его исправление весьма очевидно. Давайте это сделаем!

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'имя':'Иван', 'возраст':250, 'страна':'Россия'}
>>> users['имя']
'Иван'
>>> users['стрна']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'стрна'
>>> users['страна']
'Россия'
>>>
```

Мы исправили ошибку, наш код был выполнен, и мы получили значение.

### TypeError

**Пример 1: TypeError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

В примере выше было вызвано исключение TypeError, потому что нельзя прибавлять строку к числу. Первый вариант решения это привести строку к числу типа int или float. Другой вариант привести число к строковому типу (тогда результат будет '43'). Давайте пойдем по первому пути.

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
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

Ошибка исправлена, и мы получили ожидаемый результат.

### ImportError

**Пример 1: TypeError**

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>>
```

В модуле math нет функции power, она называется _pow_. Давайте исправим это:

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### ValueError

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

В данном случае мы не можем привести строку к числу из-за буквы 'a' в ней.

### ZeroDivisionError

```py
PS C:\Projects\30-Days-Of-Python> python
Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

Мы не можем делить число на ноль.

Мы рассмотрели несколько типов ошибок в python, при желании вы можете узнать больше о типах ошибок в документации python.
Если вы научитесь читать ошибки разных типов, вы сможете быстро отлаживать код и станете более успешным как разработчик.

🌕 Вы достигли выдающихся результатов. Вы уже на пол пути к успеху. Теперь выполните несколько упражнений для мозга и мускулов.

## 💻 Упражнения: День 15

1. Откройте интерактивную оболочку python и попробуйте повторить все примеры, приведенные в этом разделе.

🎉 ПОЗДРАВЛЯЮ ! 🎉

[<< День 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [День 16 >>](../16_Day_Python_date_time/16_python_datetime.md)
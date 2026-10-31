<div align="center">
  <h1> 30 дней Python: День 15 - Ошибки типов Python</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Асабенех Йетаех</a><br>
  <small> Второе издание: июль 2021</small>
  </sub>

</div>

[<< День 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [День 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)
- [📘 День 15](#-день-15)
  - [Типы ошибок Python](#типы-ошибок-python)
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

## Типы ошибок Python

При написании кода часто случается опечатка или другая распространённая ошибка. Если наш код не запускается, интерпретатор Python выводит сообщение, содержащее обратную связь с информацией о том, где возникает проблема и какой тип ошибки. Иногда он также даёт нам подсказки о возможном исправлении. Понимание различных типов ошибок в языках программирования поможет нам быстро отлаживать наш код, а также сделает нас лучше в том, что мы делаем.

Давайте рассмотрим наиболее распространённые типы ошибок по очереди. Сначала откроем нашу интерактивную оболочку Python. Перейдите в терминал вашего компьютера и напишите 'python'. Откроется интерактивная оболочка Python.

### SyntaxError

**Пример 1: SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

Как вы можете видеть, мы допустили синтаксическую ошибку, потому что забыли заключить строку в скобки, и Python уже предлагает решение. Давайте исправим её.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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

Ошибка была _SyntaxError_. После исправления наш код выполнился без проблем. Давайте рассмотрим больше типов ошибок.

### NameError

**Пример 1: NameError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

Как вы видите из сообщения выше, имя age не определено. Да, это правда, что мы не определили переменную age, но мы пытались вывести её так, как будто объявили её. Теперь давайте исправим это, объявив её и присвоив ей значение.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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

Тип ошибки был _NameError_. Мы устранили ошибку, определив имя переменной.

### IndexError

**Пример 1: IndexError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

В приведённом выше примере Python вызвал _IndexError_, потому что список имеет только индексы от 0 до 4, поэтому он вышел за пределы диапазона.

### ModuleNotFoundError

**Пример 1: ModuleNotFoundError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

В приведённом выше примере я намеренно добавил лишнюю s в math, и была вызвана _ModuleNotFoundError_. Давайте исправим это, убрав лишнюю s из math.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

Мы исправили это, так что давайте воспользуемся некоторыми функциями из модуля math.

### AttributeError

**Пример 1: AttributeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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

Как видите, я снова ошибся! Вместо pi я попытался вызвать константу PI из модуля maths. Это вызвало ошибку атрибута, что означает, что такого атрибута не существует в модуле. Давайте исправим это, изменив PI на pi.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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

Теперь, когда мы вызываем pi из модуля math, мы получаем результат.

### KeyError

**Пример 1: KeyError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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

Как видите, в ключе, использованном для получения значения словаря, была опечатка. Итак, это ошибка ключа, и исправление довольно простое. Давайте сделаем это!

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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

Мы устранили ошибку, наш код выполнился, и мы получили значение.

### TypeError

**Пример 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

В приведённом выше примере возникает TypeError, потому что мы не можем сложить число со строкой. Первым решением было бы преобразовать строку в int или float. Другим решением было бы преобразовать число в строку (тогда результат был бы '43'). Давайте последуем первому исправлению.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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

Ошибка устранена, и мы получили ожидаемый результат.

### ImportError

**Пример 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

В модуле math нет функции с именем power, она называется иначе: _pow_. Давайте исправим это:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
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
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

В этом случае мы не можем преобразовать заданную строку в число из-за буквы 'a' в ней.

### ZeroDivisionError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

Мы не можем разделить число на ноль.

Мы рассмотрели некоторые типы ошибок Python; если вы хотите узнать больше, посмотрите документацию Python о типах ошибок.
Если вы хорошо умеете читать типы ошибок, вы сможете быстро исправлять свои баги, а также станете лучшим программистом.

🌕 Ты преуспеваешь. Ты прошёл половину пути к величию. Теперь выполни несколько упражнений для своего мозга и мышц.

## 💻 Упражнения: День 15

1. Открой интерактивную оболочку Python и попробуй все примеры, рассмотренные в этом разделе.

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [День 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

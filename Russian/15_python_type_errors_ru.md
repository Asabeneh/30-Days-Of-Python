<div align="center">
  <h1> 30 дней Python: День 15 - Типы ошибок в Python </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Второе издание: июль 2021</small>
  </sub>

</div>

[<< День 14](./14_higher_order_functions_ru.md) | [День 16 >>](./16_python_datetime_ru.md)

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

Когда мы пишем код, мы часто делаем опечатки или другие распространённые ошибки. Если наш код не запускается, интерпретатор Python выводит сообщение с обратной связью о том, где возникла проблема и какой тип ошибки. Иногда он также предлагает возможное исправление. Понимание различных типов ошибок в языках программирования поможет нам быстро отлаживать код и делает нас лучше в том, что мы делаем.

Давайте рассмотрим наиболее распространённые типы ошибок по очереди. Сначала откроем интерактивную оболочку Python. Перейдите в терминал вашего компьютера и введите 'python'. Откроется интерактивная оболочка Python.

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

Как видите, мы допустили синтаксическую ошибку, потому что забыли заключить строку в скобки, и Python уже предлагает решение. Давайте исправим это.

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

Ошибкой была _SyntaxError_. После исправления наш код выполнился без сучка и задоринки. Рассмотрим другие типы ошибок.

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

Как видно из сообщения выше, имя age не определено. Да, верно, мы не определили переменную age, но пытались её вывести так, будто объявили её. Теперь давайте исправим это, объявив её и присвоив значение.

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

Типом ошибки была _NameError_. Мы отладили ошибку, определив имя переменной.

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

В приведённом выше примере Python вызвал _IndexError_, потому что в списке есть индексы только от 0 до 4, поэтому индекс оказался вне диапазона.

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

В примере выше я намеренно добавил лишнюю s к math, и была вызвана _ModuleNotFoundError_. Давайте исправим это, убрав лишнюю s из math.

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

Мы исправили это, так что давайте использовать некоторые функции из модуля math.

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

Как видите, я снова ошибся! Вместо pi я попытался вызвать константу PI из модуля math. Это вызвало ошибку атрибута, что означает, что такого атрибута в модуле нет. Давайте исправим это, заменив PI на pi.

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

Теперь, когда мы вызываем pi из модуля math, мы получили результат.

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

Как видите, в ключе, использованном для получения значения словаря, была опечатка. Итак, это ошибка ключа, и исправление довольно очевидное. Давайте сделаем это!

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

Мы отладили ошибку, наш код выполнился, и мы получили значение.

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

В примере выше возникает TypeError, потому что мы не можем сложить число со строкой. Первым решением было бы преобразовать строку в int или float. Другим решением было бы преобразовать число в строку (тогда результатом было бы '43'). Давайте последуем первому исправлению.

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

В модуле math нет функции power, она называется иначе: _pow_. Давайте исправим:

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

В этом случае мы не можем преобразовать данную строку в число из-за буквы 'a' в ней.

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

Мы не можем делить число на ноль.

Мы рассмотрели некоторые типы ошибок Python; если хотите узнать больше, обратитесь к документации Python по типам ошибок.
Если вы хорошо разбираетесь в чтении типов ошибок, вы сможете быстро исправлять свои баги и станете лучшим программистом.

🌕 Вы отлично справляетесь. Вы прошли половину пути к величию. Теперь сделайте несколько упражнений для ума и мышц.

## 💻 Упражнения: День 15

1. Откройте интерактивную оболочку Python и попробуйте все примеры, рассмотренные в этом разделе.

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 14](./14_higher_order_functions_ru.md) | [День 16 >>](./16_python_datetime_ru.md)

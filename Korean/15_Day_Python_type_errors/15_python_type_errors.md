<div align="center">
  <h1> 30 Days Of Python: Day 15 - Python Type Errors </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Second Edition: July, 2021</small>
  </sub>

</div>

[<< Day 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Day 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 15](#-day-15)
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
  - [💻 Exercises: Day 15](#-exercises-day-15)

# 📘 Day 15

## Python Error Types

코드를 작성할 때 오타나 다른 일반적인 오류를 만드는 것은 흔한 일입니다. 코드가 실행되지 않으면 파이썬 인터프리터는 문제가 발생한 위치와 오류 유형에 대한 정보를 포함하는 메시지를 표시합니다. 때때로 가능한 수정 사항에 대한 제안도 제공합니다. 프로그래밍 언어에서 다양한 유형의 오류를 이해하면 코드를 빠르게 디버그하는 데 도움이 되며 더 나은 개발자가 될 수 있습니다.

가장 일반적인 오류 유형을 하나씩 살펴봅시다. 먼저 파이썬 대화형 셸을 열어봅시다. 컴퓨터 터미널로 이동하여 'python'을 입력합니다. 파이썬 대화형 셸이 열립니다.

### SyntaxError

**Example 1: SyntaxError**

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

보시다시피 문자열을 괄호로 감싸는 것을 잊어서 구문 오류가 발생했습니다. 파이썬은 이미 해결 방법을 제안하고 있습니다. 수정해봅시다.

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

오류는 _SyntaxError_ 였습니다. 수정 후 코드는 문제없이 실행되었습니다. 더 많은 오류 유형을 살펴봅시다.

### NameError

**Example 1: NameError**

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

위의 메시지에서 볼 수 있듯이 name age is not defined라고 합니다. 맞습니다, 실제로 age 변수를 정의하지 않았지만 선언한 것처럼 출력하려고 했습니다. 이제 변수를 선언하고 값을 할당하여 수정해봅시다.

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

오류 유형은 _NameError_ 였습니다. 변수 이름을 정의하여 오류를 디버그했습니다.

### IndexError

**Example 1: IndexError**

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

위의 예에서 파이썬은 _IndexError_ 를 발생시켰습니다. 리스트의 인덱스는 0에서 4까지만 있으므로 범위를 벗어났기 때문입니다.

### ModuleNotFoundError

**Example 1: ModuleNotFoundError**

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

위의 예에서 의도적으로 math에 s를 추가했고 _ModuleNotFoundError_ 가 발생했습니다. math에서 추가된 s를 제거하여 수정해봅시다.

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

수정했으니 이제 math 모듈의 일부 함수를 사용해봅시다.

### AttributeError

**Example 1: AttributeError**

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

보시다시피 또 실수를 했습니다! pi 대신 maths 모듈에서 PI 상수를 호출하려고 했습니다. 속성 오류가 발생했는데, 이는 해당 속성이 모듈에 존재하지 않는다는 것을 의미합니다. PI를 pi로 변경하여 수정해봅시다.

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

이제 math 모듈에서 pi를 호출하면 결과를 얻을 수 있습니다.

### KeyError

**Example 1: KeyError**

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

보시다시피 딕셔너리 값을 가져오는 데 사용된 키에 오타가 있었습니다. 이것은 키 오류이며 수정은 매우 간단합니다. 해봅시다!

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

오류를 디버그하고 코드가 실행되어 값을 얻었습니다.

### TypeError

**Example 1: TypeError**

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

위의 예에서 숫자와 문자열을 더할 수 없기 때문에 TypeError가 발생했습니다. 첫 번째 해결 방법은 문자열을 int 또는 float으로 변환하는 것입니다. 또 다른 해결 방법은 숫자를 문자열로 변환하는 것입니다 (결과는 '43'이 됩니다). 첫 번째 수정 방법을 따라해봅시다.

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

오류가 제거되고 예상했던 결과를 얻었습니다.

### ImportError

**Example 1: TypeError**

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

math 모듈에는 power라는 함수가 없으며 다른 이름 _pow_ 를 사용합니다. 수정해봅시다:

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

이 경우 'a' 문자가 있기 때문에 주어진 문자열을 숫자로 변환할 수 없습니다.

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

숫자를 0으로 나눌 수 없습니다.

파이썬 오류 유형 중 일부를 다루었습니다. 더 자세히 알고 싶다면 파이썬 오류 유형에 대한 파이썬 문서를 확인하세요.
오류 유형을 잘 읽을 수 있다면 버그를 빠르게 수정할 수 있고 더 나은 프로그래머가 될 수 있습니다.

🌕 뛰어나게 잘하고 있습니다. 위대함을 향한 길의 절반에 도달했습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 Exercises: Day 15

1. 파이썬 대화형 셸을 열고 이 섹션에서 다룬 모든 예제를 시도해보세요.

🎉 CONGRATULATIONS ! 🎉

[<< Day 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Day 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

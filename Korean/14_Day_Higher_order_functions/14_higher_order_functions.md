<div align="center">
  <h1> 30 Days Of Python: Day 14 - Higher Order Functions</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>Second Edition: July, 2021</small>
  </sub>

</div> 

[<< Day 13](../13_Day_List_comprehension/13_list_comprehension.md) | [Day 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 14](#-day-14)
  - [Higher Order Functions](#higher-order-functions)
    - [Function as a Parameter](#function-as-a-parameter)
    - [Function as a Return Value](#function-as-a-return-value)
  - [Python Closures](#python-closures)
  - [Python Decorators](#python-decorators)
    - [Creating Decorators](#creating-decorators)
    - [Applying Multiple Decorators to a Single Function](#applying-multiple-decorators-to-a-single-function)
    - [Accepting Parameters in Decorator Functions](#accepting-parameters-in-decorator-functions)
  - [Built-in Higher Order Functions](#built-in-higher-order-functions)
    - [Python - Map Function](#python---map-function)
    - [Python - Filter Function](#python---filter-function)
    - [Python - Reduce Function](#python---reduce-function)
  - [💻 Exercises: Day 14](#-exercises-day-14)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 14

## Higher Order Functions

파이썬에서 함수는 일급 시민으로 취급되며, 함수에 대해 다음과 같은 작업을 수행할 수 있습니다:

- 함수는 하나 이상의 함수를 매개변수로 받을 수 있습니다
- 함수는 다른 함수의 결과로 반환될 수 있습니다
- 함수는 수정될 수 있습니다
- 함수는 변수에 할당될 수 있습니다

이 섹션에서는 다음을 다룹니다:

1. 함수를 매개변수로 처리하기
2. 다른 함수에서 반환 값으로 함수 반환하기
3. 파이썬 클로저와 데코레이터 사용하기

### Function as a Parameter

```py
def sum_numbers(nums):  # 일반 함수
    return sum(nums)    # 내장 sum 함수를 남용하는 슬픈 함수 :<

def higher_order_function(f, lst):  # 매개변수로서의 함수
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Function as a Return Value

```py
def square(x):          # 제곱 함수
    return x ** 2

def cube(x):            # 세제곱 함수
    return x ** 3

def absolute(x):        # 절대값 함수
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # 함수를 반환하는 고차 함수
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

위의 예에서 볼 수 있듯이 고차 함수는 전달된 매개변수에 따라 다른 함수를 반환합니다.

## Python Closures

파이썬에서는 중첩된 함수가 둘러싸는 함수의 외부 스코프에 접근할 수 있습니다. 이를 클로저라고 합니다. 파이썬에서 클로저가 어떻게 작동하는지 살펴봅시다. 파이썬에서 클로저는 다른 캡슐화 함수 안에 함수를 중첩시킨 다음 내부 함수를 반환하여 생성됩니다. 아래 예제를 참조하세요.

**Example:**

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Python Decorators

데코레이터는 파이썬의 디자인 패턴으로, 사용자가 기존 객체의 구조를 수정하지 않고 새로운 기능을 추가할 수 있게 합니다. 데코레이터는 일반적으로 데코레이트하려는 함수의 정의 전에 호출됩니다.

### Creating Decorators

데코레이터 함수를 만들려면 내부 래퍼 함수가 있는 외부 함수가 필요합니다.

**Example:**

```py
# 일반 함수
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## 위의 예제를 데코레이터로 구현해봅시다

'''이 데코레이터 함수는 함수를 매개변수로 받는
고차 함수입니다'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

### Applying Multiple Decorators to a Single Function

```py

'''이 데코레이터 함수들은 함수를 매개변수로 받는
고차 함수입니다'''

# 첫 번째 데코레이터
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# 두 번째 데코레이터
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

# 데코레이터는 아래에서 위로 실행됩니다
@split_string_decorator
@uppercase_decorator     # 이 경우 데코레이터의 순서가 중요합니다 - .upper() 함수는 리스트에서 작동하지 않습니다
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### Accepting Parameters in Decorator Functions

대부분의 경우 함수가 매개변수를 받아야 하므로 매개변수를 받는 데코레이터를 정의해야 할 수 있습니다.

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## Built-in Higher Order Functions

이 부분에서 다루는 일부 내장 고차 함수는 _map()_, _filter_, _reduce_ 입니다.
Lambda 함수는 매개변수로 전달될 수 있으며 lambda 함수의 가장 좋은 사용 사례는 map, filter, reduce와 같은 함수입니다.

### Python - Map Function

map() 함수는 함수와 iterable을 매개변수로 받는 내장 함수입니다.

```py
    # syntax
    map(function, iterable)
```

**Example:1**

```py
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# lambda 함수로 적용해봅시다
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Example:2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Example:3**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# lambda 함수로 적용해봅시다
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

map이 실제로 하는 것은 리스트를 반복하는 것입니다. 예를 들어 이름을 대문자로 변경하고 새 리스트를 반환합니다.

### Python - Filter Function

filter() 함수는 지정된 iterable(리스트)의 각 아이템에 대해 불리언을 반환하는 지정된 함수를 호출합니다. 필터링 기준을 충족하는 아이템을 필터링합니다.

```py
    # syntax
    filter(function, iterable)
```

**Example:1**

```py
# 짝수만 필터링해봅시다
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Example:2**

```py
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# 긴 이름 필터링
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python - Reduce Function

_reduce()_ 함수는 functools 모듈에 정의되어 있으며 이 모듈에서 임포트해야 합니다. map과 filter처럼 두 개의 매개변수(함수와 iterable)를 받습니다. 그러나 다른 iterable을 반환하지 않고 단일 값을 반환합니다.
**Example:1**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Exercises: Day 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Exercises: Level 1

1. map, filter, reduce의 차이점을 설명합니다.
2. 고차 함수, 클로저, 데코레이터의 차이점을 설명합니다.
3. map, filter 또는 reduce 전에 호출 함수를 정의합니다. 예제를 참조하세요.
4. for 루프를 사용하여 countries 리스트의 각 나라를 출력합니다.
5. for를 사용하여 names 리스트의 각 이름을 출력합니다.
6. for를 사용하여 numbers 리스트의 각 숫자를 출력합니다.

### Exercises: Level 2

1. map을 사용하여 countries 리스트의 각 나라를 대문자로 변경한 새 리스트를 만듭니다.
1. map을 사용하여 numbers 리스트의 각 숫자를 제곱으로 변경한 새 리스트를 만듭니다.
1. map을 사용하여 names 리스트의 각 이름을 대문자로 변경합니다.
1. filter를 사용하여 'land'를 포함하는 나라를 필터링합니다.
1. filter를 사용하여 정확히 6자인 나라를 필터링합니다.
1. filter를 사용하여 6글자 이상인 나라를 필터링합니다.
1. filter를 사용하여 'E'로 시작하는 나라를 필터링합니다.
1. 두 개 이상의 리스트 이터레이터를 체이닝합니다 (예: arr.map(callback).filter(callback).reduce(callback))
1. 리스트를 매개변수로 받아 문자열 아이템만 포함하는 리스트를 반환하는 get_string_lists 함수를 선언합니다.
1. reduce를 사용하여 numbers 리스트의 모든 숫자를 합산합니다.
1. reduce를 사용하여 모든 나라를 연결하여 다음 문장을 만듭니다: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
1. 공통 패턴을 가진 나라 리스트를 반환하는 categorize_countries 함수를 선언합니다 (이 저장소에서 [countries list](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py)를 찾을 수 있습니다. 예: 'land', 'ia', 'island', 'stan').
1. 나라의 시작 글자를 키로, 해당 글자로 시작하는 나라 이름의 수를 값으로 하는 딕셔너리를 반환하는 함수를 만듭니다.
2. data 폴더의 countries.js 리스트에서 처음 10개 나라를 반환하는 get_first_ten_countries 함수를 선언합니다.
1. countries 리스트에서 마지막 10개 나라를 반환하는 get_last_ten_countries 함수를 선언합니다.

### Exercises: Level 3

1. countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 파일을 사용하여 다음 과제를 수행합니다:
   - 이름, 수도, 인구별로 나라를 정렬합니다
   - 위치별로 가장 많이 사용되는 10개 언어를 정렬합니다.
   - 가장 인구가 많은 10개 나라를 정렬합니다.

🎉 CONGRATULATIONS ! 🎉

[<< Day 13](../13_Day_List_comprehension/13_list_comprehension.md) | [Day 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)

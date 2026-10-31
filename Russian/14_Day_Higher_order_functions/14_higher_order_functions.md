<div align="center">
  <h1> 30 дней Python: День 14 - Функции высшего порядка</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Асабенех Йетаех</a><br>
  <small>Второе издание: июль 2021</small>
  </sub>

</div> 

[<< День 13](../13_Day_List_comprehension/13_list_comprehension.md) | [День 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)
- [📘 День 14](#-день-14)
  - [Функции высшего порядка](#функции-высшего-порядка)
    - [Функция как параметр](#функция-как-параметр)
    - [Функция как возвращаемое значение](#функция-как-возвращаемое-значение)
  - [Замыкания Python](#замыкания-python)
  - [Декораторы Python](#декораторы-python)
    - [Создание декораторов](#создание-декораторов)
    - [Применение нескольких декораторов к одной функции](#применение-нескольких-декораторов-к-одной-функции)
    - [Приём параметров в функциях-декораторах](#приём-параметров-в-функциях-декораторах)
  - [Встроенные функции высшего порядка](#встроенные-функции-высшего-порядка)
    - [Python - функция Map](#python--функция-map)
    - [Python - функция Filter](#python--функция-filter)
    - [Python - функция Reduce](#python--функция-reduce)
  - [💻 Упражнения: День 14](#-упражнения-день-14)
    - [Упражнения: Уровень 1](#упражнения-уровень-1)
    - [Упражнения: Уровень 2](#упражнения-уровень-2)
    - [Упражнения: Уровень 3](#упражнения-уровень-3)

# 📘 День 14

## Функции высшего порядка

В Python функции рассматриваются как объекты первого класса, что позволяет выполнять над функциями следующие операции:

- Функция может принимать одну или несколько функций в качестве параметров
- Функция может быть возвращена как результат другой функции
- Функция может быть изменена
- Функция может быть присвоена переменной

В этом разделе мы рассмотрим:

1. Обработку функций как параметров
2. Возврат функций как возвращаемого значения из других функций
3. Использование замыканий и декораторов Python

### Функция как параметр

```py
def sum_numbers(nums):  # обычная функция
    return sum(nums)    # грустная функция, злоупотребляющая встроенной функцией sum :<

def higher_order_function(f, lst):  # функция как параметр
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Функция как возвращаемое значение

```py
def square(x):          # функция возведения в квадрат
    return x ** 2

def cube(x):            # функция возведения в куб
    return x ** 3

def absolute(x):        # функция абсолютного значения
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # функция высшего порядка, возвращающая функцию
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

Из приведённого выше примера видно, что функция высшего порядка возвращает разные функции в зависимости от переданного параметра.

## Замыкания Python

Python позволяет вложенной функции обращаться к внешней области видимости охватывающей функции. Это называется Замыканием. Давайте посмотрим, как работают замыкания в Python. В Python замыкание создаётся путём вложения функции внутрь другой инкапсулирующей функции и последующего возврата внутренней функции. Смотрите пример ниже.

**Пример:**

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

## Декораторы Python

Декоратор - это шаблон проектирования в Python, который позволяет пользователю добавлять новую функциональность к существующему объекту без изменения его структуры. Декораторы обычно вызываются перед определением функции, которую вы хотите декорировать.

### Создание декораторов

Чтобы создать функцию-декоратор, нам нужна внешняя функция с внутренней функцией-обёрткой.

**Пример:**

```py
# Обычная функция
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

## Давайте реализуем приведённый выше пример с декоратором

'''Эта функция-декоратор является функцией высшего порядка,
которая принимает функцию в качестве параметра'''
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

### Применение нескольких декораторов к одной функции

```py

'''Эти функции-декораторы являются функциями высшего порядка,
которые принимают функции в качестве параметров'''

# Первый декоратор
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Второй декоратор
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Декораторы будут выполняться снизу вверх
@split_string_decorator
@uppercase_decorator     # порядок с декораторами важен в этом случае - функция .upper() не работает со списками
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### Приём параметров в функциях-декораторах

В большинстве случаев нам нужно, чтобы наши функции принимали параметры, поэтому нам может потребоваться определить декоратор, который принимает параметры.

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

## Встроенные функции высшего порядка

Некоторые из встроенных функций высшего порядка, которые мы рассмотрим в этой части: _map()_, _filter_ и _reduce_.
Лямбда-функция может быть передана как параметр, и лучшее применение лямбда-функций - в таких функциях, как map, filter и reduce.

### Python - функция Map

Функция map() - это встроенная функция, которая принимает функцию и итерируемый объект в качестве параметров.

```py
    # синтаксис
    map(function, iterable)
```

**Пример:1**

```py
numbers = [1, 2, 3, 4, 5] # итерируемый объект
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Давайте применим её с лямбда-функцией
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Пример:2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # итерируемый объект
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Пример:3**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # итерируемый объект

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Давайте применим её с лямбда-функцией
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

Что на самом деле делает map - это итерация по списку. Например, она изменяет имена на верхний регистр и возвращает новый список.

### Python - функция Filter

Функция filter() вызывает указанную функцию, которая возвращает логическое значение для каждого элемента указанного итерируемого объекта (списка). Она отфильтровывает элементы, удовлетворяющие критериям фильтрации.

```py
    # синтаксис
    filter(function, iterable)
```

**Пример:1**

```py
# Давайте отфильтруем только чётные числа
numbers = [1, 2, 3, 4, 5]  # итерируемый объект

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Пример:2**

```py
numbers = [1, 2, 3, 4, 5]  # итерируемый объект

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# Фильтрация длинных имён
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # итерируемый объект
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python - функция Reduce

Функция _reduce()_ определена в модуле functools, и мы должны импортировать её из этого модуля. Как и map и filter, она принимает два параметра: функцию и итерируемый объект. Однако она не возвращает другой итерируемый объект, а возвращает одно значение.
**Пример:1**

```py
numbers_str = ['1', '2', '3', '4', '5']  # итерируемый объект
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Упражнения: День 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Упражнения: Уровень 1

1. Объясни разницу между map, filter и reduce.
2. Объясни разницу между функцией высшего порядка, замыканием и декоратором
3. Определи вызывающую функцию перед map, filter или reduce, смотри примеры.
4. Используй цикл for для вывода каждой страны в списке countries.
5. Используй for для вывода каждого имени в списке names.
6. Используй for для вывода каждого числа в списке numbers.

### Упражнения: Уровень 2

1. Используй map для создания нового списка, изменив каждую страну на верхний регистр в списке countries
1. Используй map для создания нового списка, изменив каждое число на его квадрат в списке numbers
1. Используй map для изменения каждого имени на верхний регистр в списке names
1. Используй filter для отфильтровывания стран, содержащих 'land'.
1. Используй filter для отфильтровывания стран, содержащих ровно шесть символов.
1. Используй filter для отфильтровывания стран, содержащих шесть букв и более, в списке стран.
1. Используй filter для отфильтровывания стран, начинающихся с 'E'
1. Соедини два или более итераторов списков (например, arr.map(callback).filter(callback).reduce(callback))
1. Объяви функцию get_string_lists, которая принимает список в качестве параметра и возвращает список, содержащий только строковые элементы.
1. Используй reduce для суммирования всех чисел в списке numbers.
1. Используй reduce для объединения всех стран и создания следующего предложения: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
1. Объяви функцию categorize_countries, которая возвращает список стран с некоторым общим шаблоном (вы можете найти [список стран](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) в этом репозитории как countries.js (например, 'land', 'ia', 'island', 'stan')).
1. Создай функцию, возвращающую словарь, где ключи - начальные буквы стран, а значения - количество названий стран, начинающихся с этой буквы.
2. Объяви функцию get_first_ten_countries - она возвращает список первых десяти стран из списка countries.js в папке data.
1. Объяви функцию get_last_ten_countries, которая возвращает последние десять стран в списке countries.

### Упражнения: Уровень 3

1. Используй файл countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) и выполни следующие задания:
   - Отсортируй страны по названию, по столице, по населению
   - Отсортируй десять самых распространённых языков по местоположению.
   - Отсортируй десять самых населённых стран.

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 13](../13_Day_List_comprehension/13_list_comprehension.md) | [День 15>>](../15_Day_Python_type_errors/15_python_type_errors.md)

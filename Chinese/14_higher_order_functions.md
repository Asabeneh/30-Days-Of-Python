<div align="center">
  <h1> 30天Python：第14天 - 高阶函数</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>第二版：2021 年 7 月</small>
</sub>

</div>

[<< 第 13 天](./13_list_comprehension.md) | [第 15 天 >>](./15_python_type_errors_cn.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 14 天](#-第14天)
  - [高阶函数](#高阶函数)
    - [函数作为参数](#函数作为参数)
    - [函数作为返回值](#函数作为返回值)
  - [Python 闭包](#python闭包)
  - [Python 装饰器](#python装饰器)
    - [创建装饰器](#创建装饰器)
    - [将多个装饰器应用于单个函数](#将多个装饰器应用于单个函数)
    - [在装饰器函数中接受参数](#在装饰器函数中接受参数)
  - [内置高阶函数](#内置高阶函数)
    - [Python - Map 函数](#python---map函数)
    - [Python - Filter 函数](#python---filter函数)
    - [Python - Reduce 函数](#python---reduce函数)
  - [💻 练习：第 14 天](#-练习-第14天)
    - [练习：简单](#练习-简单)
    - [练习：中等](#练习-中等)
    - [练习：高级](#练习-高级)

# 📘 第 14 天

## 高阶函数

在 Python 中，函数被视为第一类公民，可以对函数执行以下操作：

- 一个函数可以接收一个或多个函数作为参数
- 一个函数可以作为另一个函数的返回值
- 一个函数可以被修改
- 一个函数可以被赋值给变量

在本节中，我们将讨论：

1. 将函数作为参数传递
2. 将函数作为返回值返回
3. 使用 Python 闭包和装饰器

### 函数作为参数

```py
def sum_numbers(nums):  # 普通函数
    return sum(nums)    # 使用内置函数sum的函数

def higher_order_function(f, lst):  # 将函数作为参数
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### 函数作为返回值

```py
def square(x):          # 求平方函数
    return x ** 2

def cube(x):            # 求立方函数
    return x ** 3

def absolute(x):        # 求绝对值函数
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # 返回一个函数的高阶函数
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

从上述示例中可以看到，高阶函数根据传入的参数来返回不同的函数。

## Python 闭包

Python 允许嵌套函数访问外部封闭函数的作用域。 这称为闭包。 让我们看看闭包在 Python 中的工作原理。在 Python 中，闭包是通过在另一个封装函数内部嵌套函数，然后返回内部函数来创建的。请看下面的例子。

**示例：**

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

## Python 装饰器

装饰器是一种设计模式，允许用户在不修改对象结构的情况下为其添加新功能。装饰器通常在你想要装饰的函数定义之前调用。

### 创建装饰器

要创建装饰器函数，我们需要一个带有内部包装器函数的外部函数。

**示例：**

```py
# 普通函数
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

# 使用装饰器实现上面的示例

'''这个装饰器函数是一个高阶函数，接收一个函数作为参数'''
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

### 将多个装饰器应用于单个函数

```py

'''这些装饰器函数是高阶函数，接收函数作为参数'''

# 第一个装饰器
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# 第二个装饰器
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # 在此情况下，装饰器的顺序很重要 - .upper()函数不适用于列表
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### 在装饰器函数中接受参数

大多数时候我们需要我们的函数接受参数，所以我们可能需要定义一个接受参数的装饰器。

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## 内置高阶函数

在本部分中，我们将讨论一些内置的高阶函数，如*map()*, *filter*和*reduce*。
Lambda 函数可以作为参数传递，其最佳使用案例是在地图、过滤和减少等功能中。

### Python - Map 函数

map()函数是一个内置函数，接收一个函数和可迭代对象作为参数。

```py
    # 语法
    map(function, iterable)
```

**示例：1**

```py
numbers = [1, 2, 3, 4, 5] # 可迭代对象
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# 让我们应用lambda函数
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**示例：2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # 可迭代对象
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**示例：3**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # 可迭代对象

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# 让我们应用lambda函数
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

map 函数实际上是迭代列表。例如，它将名称更改为大写并返回一个新列表。

### Python - Filter 函数

filter()函数调用指定函数，该函数对指定的可迭代对象（列表）中的每个项目返回布尔值。它过滤出满足过滤条件的项目。

```py
    # 语法
    filter(function, iterable)
```

**示例：1**

```py
# 让我们只过滤偶数
numbers = [1, 2, 3, 4, 5]  # 可迭代对象

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**示例：2**

```py
numbers = [1, 2, 3, 4, 5]  # 可迭代对象

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# 过滤长名称
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # 可迭代对象
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python - Reduce 函数

*reduce()*函数定义在 functools 模块中，我们需要从这个模块中导入它。像 map 和 filter 一样，它接收两个参数，一个函数和一个可迭代对象。然而，它不返回另一个可迭代对象，而是返回一个单一的值。
**示例：1**

```py
numbers_str = ['1', '2', '3', '4', '5']  # 可迭代对象
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 练习：第 14 天

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### 练习：简单

1. 解释 map、filter 和 reduce 的区别。
2. 解释高阶函数、闭包和装饰器的区别。
3. 定义调用函数，见示例。
4. 使用 for 循环打印 countries 列表中的每个国家。
5. 使用 for 循环打印 names 列表中的每个名称。
6. 使用 for 循环打印 numbers 列表中的每个数字。

### 练习：中等

1. 使用 map 将 countries 列表中的每个国家更改为大写，生成一个新列表。
2. 使用 map 将 numbers 列表中的每个数字更改为平方，生成一个新列表。
3. 使用 map 将 names 列表中的每个名称更改为大写，生成一个新列表。
4. 使用 filter 过滤出包含“land”的国家。
5. 使用 filter 过滤出正好六个字符的国家。
6. 使用 filter 过滤出包含六个字母及以上的国家。
7. 使用 filter 过滤出以'E'开头的国家。
8. 链接两个或多个列表迭代器（例如 arr.map(callback).filter(callback).reduce(callback)）。
9. 声明一个函数 get_string_lists，它接收一个列表作为参数并返回一个仅包含字符串项的列表。
10. 使用 reduce 对 numbers 列表中的所有数字求和。
11. 使用 reduce 将所有国家连接起来，生成句子：Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries。
12. 声明一个函数 categorize_countries，返回一个包含某种通用模式的国家列表（可以在本仓库的 countries.js 文件中找到国家列表，例如 'land', 'ia', 'island', 'stan'）。
13. 创建一个返回字典的函数，其中键表示国家名称的首字母，值表示以该字母开头的国家数。
14. 声明一个 get_first_ten_countries 函数 - 它返回数据文件夹中 countries.js 列表中的前十个国家。
15. 声明一个 get_last_ten_countries 函数 - 它返回国家列表中的最后十个国家。

### 练习：高级

1. 使用 countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 文件，完成以下任务：
   - 按国家名称、首都和人口排序国家
   - 按位置排序出前十个最常用语言。
   - 排序出前十个人口最多的国家。

🎉 恭喜你！ 🎉

[<< 第 13 天](./13_list_comprehension.md) | [第 15 天 >>](./15_python_type_errors_cn.md)

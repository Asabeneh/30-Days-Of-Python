<div align="center">
  <h1> 30 天 Python 挑战: 第 11 天 - 函数</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> 第二版: 2021 年 7 月</small>
</sub>

</div>

[<< 第 10 天](../10_Day_Loops/10_loops.md) | [第 12 天 >>](../12_Day_Modules/12_modules.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 11 天](#-day-11)
  - [函数](#functions)
    - [定义函数](#defining-a-function)
    - [声明和调用函数](#declaring-and-calling-a-function)
    - [无参数的函数](#function-without-parameters)
    - [返回值的函数 - 第 1 部分](#function-returning-a-value---part-1)
    - [有参数的函数](#function-with-parameters)
    - [使用键值对传递参数](#passing-arguments-with-key-and-value)
    - [返回值的函数 - 第 2 部分](#function-returning-a-value---part-2)
    - [带默认参数的函数](#function-with-default-parameters)
    - [不定数量的参数](#arbitrary-number-of-arguments)
    - [函数中的默认和不定数量的参数](#default-and-arbitrary-number-of-parameters-in-functions)
    - [作为另一个函数参数的函数](#function-as-a-parameter-of-another-function)
  - [💻 练习: 第 11 天](#-exercises-day-11)
    - [练习: Level 1](#exercises-level-1)
    - [练习: Level 2](#exercises-level-2)
    - [练习: Level 3](#exercises-level-3)

# 📘 第 11 天

## 函数

到目前为止，我们已经学习了很多内置的 Python 函数。在这一节中，我们将重点关注自定义函数。什么是函数？在开始创建函数之前，让我们先了解一下什么是函数以及为什么需要它们。

### 定义函数

函数是一块可重复使用的代码块或编程语句，用于执行某些任务。要定义或声明一个函数，Python 提供了 _def_ 关键字。下面是定义函数的语法。只有在调用或触发函数时，这段函数代码才会执行。

### 声明和调用函数

当我们创建一个函数时，我们称其为声明一个函数。当我们开始使用它时，我们称其为调用或触发一个函数。函数可以带参数也可以不带参数。

```py
# 语法
# 声明一个函数
def function_name():
    codes
    codes
# 调用一个函数
function_name()
```

### 无参数的函数

函数可以在没有参数的情况下声明。

**示例:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # 调用一个函数

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### 返回值的函数 - 第 1 部分

函数也可以返回值，如果一个函数没有 return 语句，那么函数的返回值为 None。让我们使用 return 重写上述函数。从现在开始，当我们调用函数并打印时，我们会得到一个值。

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### 有参数的函数

在一个函数中，我们可以传递不同的数据类型（数字、字符串、布尔值、列表、元组、字典或集合）作为参数。

- 单个参数：如果我们的函数需要一个参数，我们应该用一个实参调用它。

```py
  # 语法
  # 声明一个函数
  def function_name(parameter):
    codes
    codes
  # 调用函数
  print(function_name(argument))
```

**示例:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- 两个参数：一个函数可以没有参数，也可以有一个或多个参数。如果我们的函数需要两个参数，我们应该用两个实参调用它。让我们看看一个带有两个参数的函数：

```py
  # 语法
  # 声明一个函数
  def function_name(para1, para2):
    codes
    codes
  # 调用函数
  print(function_name(arg1, arg2))
```

**示例:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # 值需要先转换为字符串
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### 使用键值对传递参数

如果我们使用键值对传递参数，参数的顺序就无关紧要了。

```py
# 语法
# 声明一个函数
def function_name(para1, para2):
    codes
    codes
# 调用函数
print(function_name(para1 = 'John', para2 = 'Doe')) # 参数的顺序在这里无关紧要
```

**示例:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # 顺序无关紧要
```

### 返回值的函数 - 第 2 部分

如果我们不在函数中返回一个值，那么我们的函数默认返回 _None_。要用函数返回一个值，我们使用关键字 _return_，后面跟上我们要返回的变量。我们可以从一个函数返回任何类型的数据。

- 返回字符串:
  **示例:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- 返回数字:

**示例:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
```

- 返回布尔值:
  **示例:**

```py
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return 语句会停止函数的进一步执行，类似于 break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- 返回列表:
  **示例:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### 带默认参数的函数

有时我们在调用函数时会传递默认值给参数。如果我们在调用函数时没有传递实参，参数的默认值将会被使用。

```py
# 语法
# 声明一个函数
def function_name(param = value):
    codes
    codes
# 调用函数
function_name()
function_name(arg)
```

**示例:**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # 值需要先转换为字符串
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - 地球表面的平均重力
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # 月球表面的重力
```

### 不定数量的参数

如果我们不知道传递给函数的参数数量，可以通过在参数名前加上 \* 来创建一个可以接受不定数量参数的函数。

```py
# 语法
# 声明一个函数
def function_name(*args):
    codes
    codes
# 调用函数
function_name(param1, param2, param3,..)
```

**示例:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # 相当于 total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### 函数中的默认和不定数量的参数

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
```

### 作为另一个函数参数的函数

```py
# 你可以将函数作为参数传递
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 你已经完成了很多。继续加油！你已经完成了第 11 天的挑战，你在走向成功的道路上已经迈出了 11 步。现在做一些锻炼脑力和肌肉的练习。

## 见证

现在是时候表达你对作者和 30DaysOfPython 的看法了。你可以在这个[链接](https://testimonify.herokuapp.com/)留下你的见证。

## 💻 练习: 第 11 天

### 练习: Level 1

1. 声明一个函数 _add_two_numbers_。它接受两个参数并返回它们的和。
2. 圆的面积计算公式为：area = π x r x r。编写一个函数计算 _area_of_circle_。
3. 编写一个名为 add_all_nums 的函数，它接受不定数量的参数并求和所有参数。检查所有列表项是否都是数字类型。如果不是，给予合理的反馈。
4. 摄氏温度（°C）可以使用以下公式转换为华氏温度（°F）：°F = (°C x 9/5) + 32。编写一个函数将 °C 转换为 °F，_convert_celsius_to_fahrenheit_。
5. 编写一个名为 check-season 的函数，它接受一个月份作为参数并返回季节：秋季、冬季、春季或夏季。
6. 编写一个名为 calculate_slope 的函数，它返回线性方程的斜率。
7. 二次方程按以下公式计算：ax² + bx + c = 0。编写一个函数计算二次方程的解集，_solve_quadratic_eqn_。
8. 声明一个名为 print_list 的函数。它接受一个列表作为参数，并打印列表的每个元素。
9. 声明一个名为 reverse_list 的函数。它接受一个数组作为参数，并返回数组的反转（使用循环）。

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
```

10. 声明一个名为 capitalize_list_items 的函数。它接受一个列表作为参数，并返回一个大写的列表项。
11. 声明一个名为 add_item 的函数。它接受一个列表和一个项作为参数。它返回在末尾添加项的列表。

```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
```

12. 声明一个名为 remove_item 的函数。它接受一个列表和一个项作为参数。它返回移除该项后的列表。

```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. 声明一个名为 sum_of_numbers 的函数。它接受一个数字参数并将范围内的所有数字相加。

```py
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
```

14. 声明一个名为 sum_of_odds 的函数。它接受一个数字参数并将范围内的所有奇数相加。
15. 声明一个名为 sum_of_even 的函数。它接受一个数字参数并将范围内的所有偶数相加。

### 练习: Level 2

1. 声明一个名为 evens_and_odds 的函数。它接受一个正整数作为参数并计算该数内偶数和奇数的数量。

```py
    print(evens_and_odds(100))
    # 偶数的数量是 50。
    # 奇数的数量是 51。
```

1. 调用你的函数 factorial，它接受一个整数作为参数并返回该数的阶乘。
1. 调用你的函数 _is_empty_，它接受一个参数并检查它是否为空。
1. 编写不同的函数，它们接受列表。它们应该计算平均值、计算中位数、计算众数、计算范围、计算方差、计算标准差。

### 练习: Level 3

1. 编写一个名为 is_prime 的函数，检查一个数是否是质数。
1. 编写一个函数检查列表中的所有项是否都是唯一的。
1. 编写一个函数检查列表中的所有项是否都是相同的数据类型。
1. 编写一个函数检查提供的变量是否是一个有效的 python 变量。
1. 访问数据文件并访问 countries-data.py 文件。

- 创建一个名为 the most_spoken_languages 的函数。它返回世界上使用最多的 10 或 20 种语言，按降序排列。
- 创建一个名为 the most_populated_countries 的函数。它返回世界上人口最多的 10 或 20 个国家，按降序排列。

🎉 恭喜! 🎉

[<< 第 10 天](../10_Day_Loops/10_loops.md) | [第 12 天 >>](../12_Day_Modules/12_modules.md)

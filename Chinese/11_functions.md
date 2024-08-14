<div align="center">
  <h1> 30 天学会 Python: 第十一天 - 函数</h1>
  <h2> 30 Days Of Python: Day 11 - Functions</h2>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
本章译者：
<a href="https://github.com/shenxianovo" target="_blank">shenxianovo</a><br>
<small> 第二版：2021 年 7 月</small>
</sub>

</div>

[<< 第十天](../Chinese/10_loops.md) | [第十二天 >>](../Chinese/12_modules.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 第十一天](#-第十一天)
  - [函数](#函数)
    - [函数：定义](#函数定义)
    - [函数：声明与调用](#函数声明与调用)
    - [函数：无参数](#函数无参数)
    - [函数：返回值 - 第一部分](#函数返回值---第一部分)
    - [函数：带参数](#函数带参数)
    - [通过关键字传参](#通过关键字传参)
    - [函数：返回值 - 第二部分](#函数返回值---第二部分)
    - [函数：默认参数](#函数默认参数)
    - [任意数量的参数](#任意数量的参数)
    - [普通参数与星号参数混用](#普通参数与星号参数混用)
    - [将函数作为参数](#将函数作为参数)
  - [留下你的想法吧](#留下你的想法吧)
  - [💻 练习：第十一天](#-练习第十一天)
    - [练习：难度1](#练习难度1)
    - [练习：难度2](#练习难度2)
    - [练习：难度3](#练习难度3)

# 📘 第十一天

## 函数

到教程的现在，我们已经见过许多Python内置函数。在这一部分，我们将集中精力去看看用户自定义函数。首先，请你思考：函数是什么呢？在开始上手写一个函数之前，也许你应该来看看：函数到底是个什么东西？我们为什么需要它？


### 函数：定义

函数，是为了执行特定任务编写的，可重用的代码块或编程语句。如何定义（*define*）或声明（*declare*）函数呢？Python为我们提供了`def`关键字。下面就是函数定义的语法。当一个函数被调用（*called*）时，函数体内部的代码才会被执行。

### 函数：声明与调用

我们将函数的创建称为声明（*declare*）一个函数。将函数的使用称为调用（*call* or *invoke*）。创建函数时，既可以带参数（*parameters*），也可以不带参


```py
# syntax 语法
# Declaring a function 定义一个函数
    ## 译者注：作者使用了Declare（声明）这个单词。
    ## 在Python中，函数声明与定义同时完成，二者几乎同义
    ## 但在其他编程语言（如C/C++）定义和声明的语义有所区别
def function_name():
    codes # 这些是函数体内的代码
    codes
# Calling a function 调用一个函数
function_name()
```

### 函数：无参数

函数声明时可以不带参数。

**例:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # 函数调用
# 输出：Asabeneh Yetayeh（作者的名字）

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
# 输出：5
```

### 函数：返回值 - 第一部分

函数也可以返回（*return*）一个值，如果函数没有返回语句，那么它的返回值是`None`。让我们用`return`语句重写上面的函数，然后打印出函数的返回值

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
# 输出：Asabeneh Yetayeh

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
# 输出：5
```

### 函数：带参数

我们可以给函数传递不同类型的数据（数字，字符串，布尔值，列表，元组，字典，集合等等...），传递给函数的这些数据称为参数。


- 单一参数: 如果我们的函数需要接受一个参数（*parameter*），那么在调用它时，我们也需要提供一个参数（*argument*）。 
  - *译者注：parameter：形参，argument：实参*

```py
  # 语法
  # 定义一个函数
  def function_name(parameter):
    codes
    codes
  # 调用函数
  print(function_name(argument))
```

**例:**

```py
def greetings (name):
    message = name + '，欢迎来到Python的世界!'
    return message

print(greetings('屏幕前的你'))
# 输出：屏幕前的你，欢迎来到Python的世界!

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))
# 输出：100

def square_number(x):
    return x * x
print(square_number(2))
# 输出：4

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

- 多个参数: 函数也许没有参数，也许有很多参数。总而言之，函数需要多少参数，我们就要喂给它多少参数。

```py
  # 语法
  # 函数定义
  def function_name(para1, para2):
    codes
    codes
  # 函数调用
  print(function_name(arg1, arg2))
```

**例:**

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
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### 通过关键字传参

如果我们用键（*key*）和值（*value*）来传参，那么参数的顺序就变得不再重要。

```py
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # 关键字参数顺序不再重要
# print(function_name(para2 = 'Doe', para1 = 'John')) # 这样与上面效果等同
```

**例:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

### 函数：返回值 - 第二部分

如果函数不返回一个值，那么它将会返回默认的`None`。要让函数返回一个值，我们需要用到关键字`return`。返回值可以是任意类型的数据。

- 返回一个字符串:
**例:**

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

- 返回一个数字:

**例:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))
```

- 返回一个布尔值:
  **Example:**

```py
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return后，下方代码将不会执行，效果类似于 break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- 返回一个列表:
  **例:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### 函数：默认参数

有时我们可以给函数设置一个默认参数，这样当我们调用该函数时，它将会使用默认值

```py
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name() # 调用：默认参数
function_name(arg) # 调用：传递参数
```

**例:**

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
    return age
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # 转换为字符串以供下面打印
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - 地球表面的重量
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # 月球表面的重量
```

### 任意数量的参数

如果我们不知道参数的数量，我们可以在形参名前面加上\*（星号）来表示该形参可以接受任意数量的实参

```py
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

**例:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### 普通参数与星号参数混用

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
```

### 将函数作为参数

```py
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 恭喜喵~ 你距离学会Python又进了一步~，继续加油喵 OωO - 你已经完成了第11天的挑战，已经在通往卓越的道路上迈出了11步！现在来做一些小练习吧(๑乛◡乛๑)

## 留下你的想法吧
你已经完成了“30天Python挑战”的三分之一！如果你觉得本书对你有帮助，请将它分享给更多的人(๑•̀ㅂ•́)و✧

也可以在这个链接上分享你的经历或者留下你的想法。[link](https://testimonify.herokuapp.com/)

## 💻 练习：第十一天

### 练习：难度1

1. 定义一个名为`add_two_numbers`的函数，它接受两个参数，返回两个参数之和。
2. 圆形面积公式： `面积 = π x r x r`. 编写名为`area_of_circle`的函数计算圆的面积.
3. 编写名为`add_all_nums`的函数。它接受任意数量参数，并返回所有参数之和。检查列表中的所有项目是否都是数字类型。如果不是，请给出合理的反馈。
4. 摄氏度°C与华氏度°F的换算公式：`°F = (°C x 9/5) + 32`。编写一个将摄氏度转换为华氏度的函数。
5. 编写名为`check_season`的函数，它接受一个月份参数，返回对应的季节：春，夏，秋，冬 （Spring, Summer, Autumn or Winter）
6. 编写名为`calculate_slope`的函数，它返回一个线性方程（直线方程）的斜率。
7. 一元二次方程：`ax² + bx + c = 0`。编写一个函数来计算二次方程的解。
8. 编写名为`print_list`的函数。它接收一个列表参数，然后打印出列表中每一个元素。
9. 编写名为`reverse_list`的函数。它接收一个列表，并返回该列表的逆序（使用循环）。

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
```

10.  编写名为`capitalize_list_items`的函数。它接收一个列表，将列表中元素的字母全部转换为大写，然后返回列表。
11.  编写名为`add_item`的函数。它接收一个列表与一个项。将项添加到列表尾部后返回列表。

```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
```

12.  编写名为`remove_item`的函数。它接收一个列表与一个项。返回一个没有该项的列表。

```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13.  编写名为`sum_of_numbers`的函数。返回从1一直加到该数字的和。

```py
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050
```

14. 编写名为`sum_of_odds`的函数。返回从1到该数字的所有奇数的加和。
15. 编写名为`sum_of_even`的函数。返回从1到该数字的所有偶数的加和。

### 练习：难度2

1.  编写名为`evens_and_odds`和函数。统计从1到该数之间奇数和偶数的个数。

```py
    print(evens_and_odds(100))
    # 奇数的个数是 50.
    # 偶数的个数是 51.
```

2. 编写名为`factorial`的函数，它接受一个整数作为参数，并返回该数的阶乘。
3. 编写名为`_is_empty_`的函数，它接受一个参数并检查该参数是否为空。
4. 编写一组函数，他们都接收一个列表，分别计算平均值、中位数、众数、极差、方差和标准差。名称分别为`calculate_mean`, `calculate_median`, `calculate_mode`, `calculate_range`,` calculate_variance`, `calculate_std`）。

### 练习：难度3

1. 编写名为`is_prime`的函数，检查一个数是否是质数（素数）。
2. 编写一个函数，检查列表中的所有项目是否唯一
3. 编写一个函数，检查列表中的所有项目是否具有相同的数据类型。
4. 编写一个函数，检查提供的变量是否是有效的Python变量。
5. 进入`data`文件夹，找到 countries-data.py 文件。根据文件内容完成下面的任务：
   - 编写名为`the_most_spoken_languages_in_the_world`的函数，返回世界上使用人数最多的10或20种语言，并按降序排列。
   - 编写名为`the_most_populated_countries`的函数，应该返回世界上人口最多的10或20个国家，并按降序排列。

🎉 恭喜 ! 🎉

[<< Day 10](../Chinese/10_loops.md) | [Day 12 >>](../12_Day_Modules/12_modules.md)

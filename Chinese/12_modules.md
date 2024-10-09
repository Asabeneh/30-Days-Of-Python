<div align="center">
  <h1> 30 天 Python ：第 12 天 - 模块 </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>第二版: 2021 年 7 月</small>
</sub>

</div>
</div>

[<< 第 11 天](../11_Day_Functions/11_functions.md) | [第 13 天>>](../13_Day_List_comprehension/13_list_comprehension.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 12 天](#-第12天)
  - [模块](#模块)
    - [什么是模块](#什么是模块)
    - [创建模块](#创建模块)
    - [导入模块](#导入模块)
    - [从模块中导入函数](#从模块中导入函数)
    - [从模块中导入函数并重命名](#从模块中导入函数并重命名)
  - [导入内置模块](#导入内置模块)
    - [OS 模块](#os-模块)
    - [Sys 模块](#sys-模块)
    - [统计模块](#统计模块)
    - [数学模块](#数学模块)
    - [字符串模块](#字符串模块)
    - [随机模块](#随机模块)
  - [💻 练习：第 12 天](#-练习-第12天)
    - [练习：级别 1](#练习-级别-1)
    - [练习：级别 2](#练习-级别-2)
    - [练习：级别 3](#练习-级别-3)

# 📘 第 12 天

## 模块

### 什么是模块

模块是包含一组代码或一组函数的文件，可以包含在一个应用程序中。一个模块可以是包含单个变量、函数或大规模代码库的文件。

### 创建模块

要创建模块，我们在一个 Python 脚本中编写代码并保存为 .py 文件。 在项目文件夹中创建一个名为 mymodule.py 的文件。让我们在此文件中编写一些代码。

```py
# mymodule.py 文件
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

在项目目录中创建 main.py 文件并导入 mymodule.py 文件。

### 导入模块

要导入文件，我们使用 _import_ 关键字和文件名。

```py
# main.py 文件
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### 从模块中导入函数

我们可以在一个文件中有很多函数，并且我们可以分别导入所有函数。

```py
# main.py 文件
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### 从模块中导入函数并重命名

在导入过程中，我们可以重命名模块名称。

```py
# main.py 文件
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## 导入内置模块

像其他编程语言一样，我们也可以通过使用关键字 _import_ 导入文件/函数来导入模块。让我们导入我们大多数时候会使用的常见模块。一些常见的内置模块：_math_、_datetime_、_os_、_sys_、_random_、_statistics_、_collections_、_json_、_re_

### OS 模块

使用 Python _os_ 模块可以自动执行许多操作系统任务。Python 中的 OS 模块提供了创建、更改当前工作目录和删除目录（文件夹）、获取其内容、更改和识别当前目录的函数。

```py
# 导入模块
import os
# 创建目录
os.mkdir('directory_name')
# 更改当前目录
os.chdir('path')
# 获取当前工作目录
os.getcwd()
# 删除目录
os.rmdir()
```

### Sys 模块

sys 模块提供用于操作 Python 运行时环境不同部分的函数和变量。函数 sys.argv 返回传递给 Python 脚本的命令行参数列表。此列表中索引 0 处的项始终是脚本的名称，索引 1 处是从命令行传递的参数。

示例 script.py 文件：

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # 这一行会打印出来：文件名 argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

现在要查看这个脚本的工作效果，我在命令行中写：

```sh
python script.py Asabeneh 30DaysOfPython
```

结果：

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge!
```

一些有用的 sys 命令：

```py
# 退出 sys
sys.exit()
# 知道最大整数变量
sys.maxsize
# 知道环境路径
sys.path
# 知道使用的 Python 版本
sys.version
```

### 统计模块

统计模块提供用于数值数据的数学统计的函数。这个模块中定义的流行统计函数：_mean_、_median_、_mode_、_stdev_ 等。

```py
from statistics import * # 导入所有统计模块
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### 数学模块

包含许多数学运算和常数的模块。

```py
import math
print(math.pi)           # 3.141592653589793, pi 常数
print(math.sqrt(2))      # 1.4142135623730951, 平方根
print(math.pow(2, 3))    # 8.0, 指数函数
print(math.floor(9.81))  # 9, 向下取整
print(math.ceil(9.81))   # 10, 向上取整
print(math.log10(100))   # 2, 以 10 为底的对数
```

现在，我们已经导入了包含大量函数的 _math_ 模块，可以帮助我们进行数学计算。要检查模块中包含哪些函数，我们可以使用 _help(math)_ 或 _dir(math)_。这将显示模块中的可用函数。如果我们只想从模块中导入特定的函数，我们可以这样导入：

```py
from math import pi
print(pi)
```

也可以一次导入多个函数

```py
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
```

但如果我们想要导入数学模块中的所有函数，可以使用 \* .

```py
from math import *
print(pi)                  # 3.141592653589793, pi 常数
print(sqrt(2))             # 1.4142135623730951, 平方根
print(pow(2, 3))           # 8.0, 指数
print(floor(9.81))         # 9, 向下取整
print(ceil(9.81))          # 10, 向上取整
print(math.log10(100))     # 2
```

当我们导入时，我们也可以重命名函数名称。

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### 字符串模块

字符串模块是一个很有用的模块。下面的例子展示了字符串模块的一些用法。

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### 随机模块

现在你已经熟悉了导入模块。让我们再进行一次导入以熟悉它。让我们导入 _random_ 模块，它会给我们一个 0 到 0.9999 之间的随机数。_random_ 模块有很多函数，但在本节中，我们将只使用 _random_ 和 _randint_。

```py
from random import random, randint
print(random())   # 它不需要任何参数；它返回一个介于 0 和 0.9999 之间的值
print(randint(5, 20)) # 它返回一个介于 [5, 20] 之间的随机整数（含边界）
```

🌕 你走得很远了。继续努力！你刚刚完成第 12 天的挑战，现在你已经在通往伟大的路上迈出了 12 步。现在为你的大脑和肌肉做一些练习。

## 💻 练习：第 12 天

### 练习：级别 1

1. 编写一个生成六位数/字符 random_user_id 的函数。
   ```py
     print(random_user_id());
     '1ee33d'
   ```
2. 修改上一个任务。声明一个名为 user_id_gen_by_user 的函数。它不接受任何参数，但接受两个输入。一个输入是字符的数量，另一个输入是应生成的 ID 数量。

```py
print(user_id_gen_by_user()) # 用户输入：5 5
#输出：
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. 编写一个名为 rgb_color_gen 的函数。它将生成 RGB 颜色（每个值范围从 0 到 255）。

```py
print(rgb_color_gen())
# rgb(125,244,255) - 输出应该是这种形式
```

### 练习：级别 2

1. 编写一个函数 list_of_hexa_colors，它返回一个数组中的任意数量的十六进制颜色（六个十六进制数写在 # 后面。十六进制数字系统由 16 个符号组成，0-9 和 前 6 个字母 a-f。查看任务 6 的输出示例）。
2. 编写一个函数 list_of_rgb_colors，它返回一个数组中的任意数量的 RGB 颜色。
3. 编写一个函数 generate_colors，它可以生成任意数量的十六进制或 RGB 颜色。

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
```

### 练习：级别 3

1. 调用你的函数 shuffle_list，它接受一个列表作为参数并返回一个打乱的列表。
2. 编写一个函数，它在 0-9 的范围内返回七个随机数的数组。所有数字必须是唯一的。

🎉 恭喜！ 🎉

[<< 第 11 天](../11_Day_Functions/11_functions.md) | [第 13 天>>](../13_Day_List_comprehension/13_list_comprehension.md)

<div align="center">
  <h1> 30 Days Of Python: Day 12 - Modules </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> 第二版：2021 年 7 月</small>
</sub>

</div>
</div>

[<< 第十一天](../11_functions.md) | [第十三天>>](../13_list_comprehension.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

阅读大约需要：10m

-   [📘 第十二天](#-第十二天)
    -   [模块](#模块)
        -   [什么是模块](#什么是模块)
        -   [创建模块](#创建模块)
        -   [导入模块](#导入模块)
        -   [从模块导入函数](#从模块导入函数)
        -   [从模块导入函数并重命名](#从模块导入函数并重命名)
    -   [导入内置模块](#导入内置模块)
        -   [OS 模块](#os-模块)
        -   [Sys 模块](#sys-模块)
        -   [Statistics 模块](#statistics-模块)
        -   [Math 模块](#math-模块)
        -   [String 模块](#string-模块)
        -   [Random 模块](#random-模块)
    -   [💻 练习 - 第十二天](#-练习---第十二天)
        -   [练习： 1 级](#练习-1-级)
        -   [练习： 2 级](#练习-2-级)
        -   [练习： 3 级](#练习-3-级)

# 📘 第十二天

## 模块

### 什么是模块

模块是一个包含一组代码或一组函数的文件，可以包含到应用程序中。模块可以是包含单个变量、函数或大量代码的文件。

### 创建模块

要创建一个模块，我们在一个 Python 脚本中编写代码，并将其保存为 .py 文件。在项目文件夹中创建一个名为 mymodule.py 的文件。让我们在这个文件中编写一些代码。

```py
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

在项目目录中创建 main.py 文件，并导入 mymodule.py 文件。

### 导入模块

要导入文件，我们仅需要使用 _import_ 关键字和文件的名称。

```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### 从模块导入函数

我们可以在一个文件中写许多函数，并且可以以不同的方式导入所有函数。

```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### 从模块导入函数并重命名

在导入时，我们可以重命名模块的名称。

```py
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## 导入内置模块

与其他编程语言一样，我们也可以通过使用 _import_ 关键字导入文件/函数来导入模块。下面我们导入一些常用的模块。常用的内置模块有：_math_、_datetime_、_os_、_sys_、_random_、_statistics_、_collections_、_json_、_re_

### OS 模块

使用 python _os_ 模块可以自动执行许多操作系统任务。Python 的 OS 模块提供了创建、更改当前工作目录和删除目录（文件夹）、获取其内容、更改和识别当前目录的函数。

```py
# 导入模块
import os
# 创建目录
os.mkdir('directory_name')
# 更改目录
os.chdir('path')
# 获取当前工作目录
os.getcwd()
# 删除目录
os.rmdir()
```

### Sys 模块

_sys_ 模块提供了用于操作 Python 运行时环境的函数和变量。函数 _sys.argv_ 返回传递给 Python 脚本的命令行参数的列表。此列表中索引 0 的项始终是脚本的名称，索引 1 是从命令行传递的参数。

示例：script.py 文件

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # 这行将会输出: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

现在，我们在命令行中输入以下内容来了解此脚本的工作方式：

```sh
python script.py Asabeneh 30DaysOfPython
```

输出结果:

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge!
```

一些有用的 _sys_ 命令:

```py
# 退出 sys
sys.exit()
# 获取最大整数
sys.maxsize
# 获取环境目录
sys.path
# 获取正在使用的 python 版本
sys.version
```

### Statistics 模块

_statistics_ 模块提供了对数字数据的数学统计的函数。在此模块中定义了一些流行的统计函数：_mean_、_median_、_mode_、_stdev_ 等。

```py
from statistics import * # 导入 statistics 模块中的所有函数
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Math 模块

_math_ 模块包含许多数学运算和常量。

```py
import math
print(math.pi)           # 3.141592653589793, 圆周率常量
print(math.sqrt(2))      # 1.4142135623730951, 取平方根
print(math.pow(2, 3))    # 8.0, 指数运算
print(math.floor(9.81))  # 9, 向下取整
print(math.ceil(9.81))   # 10, 向上取整
print(math.log10(100))   # 2, 对数运算
```

现在，我们已经导入了 _math_ 模块，其中包含许多函数，可以帮助我们执行数学计算。要检查模块具有哪些函数，我们可以使用 _help(math)_ 或 _dir(math)_。这将显示模块中可用的函数。如果我们只想导入模块中的特定函数，我们可以按如下方式导入：

```py
from math import pi
print(pi)
```

我们还可以一次导入多个函数

```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

但是，如果我们想导入 _math_ 模块中的所有函数，我们可以使用 \*。

```py
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
```

当我们导入时，我们还可以重命名函数的名称。

```py

from math import pi as  PI
print(PI) # 3.141592653589793
```

### String 模块

字符串模块对于许多场景都很有用。下面的示例显示了一些字符串模块的用法。

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Random 模块

到目前为止，您已经熟悉了导入模块。我们再导入一个模块，以便更加熟悉。让我们导入 _random_ 模块，它可以为我们提供 0 到 0.9999 之间的随机数。_random_ 模块有很多函数，但在本节中，我们只使用 _random_ 和 _randint_。

```py

from random import random, randint
print(random())   # 不需要输入参数，返回 0~9999 间的随机数
print(randint(5, 20)) # 返回 [5, 20] 之间的随机整数
```

🌕 你已经走了很远。继续前进！你刚刚完成了第 12 天的挑战，你正在向伟大的道路迈进 12 步。现在做一些练习来锻练你的大脑和肌肉。

## 💻 练习 - 第十二天

### 练习： 1 级

1. 编写一个函数，生成一个六位数字/字符的 random_user_id。
    ```py
      print(random_user_id());
      '1ee33d'
    ```
2. 修改上一个任务。声明一个名为 user_id_gen_by_user 的函数。它不带任何参数，但使用 input() 函数获取两个输入。第一个输入是字符数，第二个输入是要生成的 ID 数。

```py
print(user_id_gen_by_user()) # user input: 5 5
#output:
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

3. 编写一个函数，生成一个十六进制颜色。它将返回一个十六进制颜色，例如 #a3e12f。十六进制数字系统由 16 个符号组成，0-9 和字母 a-f 的前 6 个字母。检查任务 6 以获取输出示例。

```py

print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
```

### 练习： 2 级

1. 编写一个函数 list_of_hexa_colors，它返回一个数组中的任意数量的十六进制颜色（# 后面写六个十六进制数字。十六进制数字系统由 16 个符号组成，0-9 和字母 a-f 的前 6 个字母。检查任务 6 以获取输出示例）。
1. 编写一个函数 list_of_rgb_colors，它返回一个数组中的任意数量的 RGB 颜色。
1. 编写一个函数 generate_colors，它可以生成任意数量的十六进制或 RGB 颜色。

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
```

### 练习： 3 级

1. 编写一个函数 shuffle_list, 它以列表作为参数并返回一个打乱的列表。
1. 编写一个函数, 该函数接受一个列表并返回一个列表，其中包含七个 0-9 范围内的随机数字。所有数字必须是唯一的。

🎉 恭喜 ! 🎉

[<< Day 11](../11_functions.md) | [Day 13>>](../13_list_comprehension.md)

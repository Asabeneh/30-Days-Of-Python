# 🐍 30 天 Python

| # 天数 |                                           主题                                           |
| ------ | :--------------------------------------------------------------------------------------: |
| 01     |                                   [介绍](./readme.md)                                    |
| 02     | [变量，内置函数](./02_variables_builtin_functions.md) |
| 03     |                       [运算符](./03_operators.md)                       |
| 04     |                         [字符串](./04_strings.md)                         |
| 05     |                            [列表](./05_lists.md)                            |
| 06     |                           [元组](./06_tuples.md)                           |
| 07     |                             [集合](./07_sets.md)                             |
| 08     |                     [字典](./08_dictionaries.md)                     |
| 09     |                     [条件](./09_conditionals.md)                     |
| 10     |                            [循环](./10_loops.md)                            |
| 11     |                        [函数](./11_functions.md)                        |
| 12     |                          [模块](./12_modules.md)                          |
| 13     |             [列表解析](./13_list_comprehension.md)             |
| 14     |         [高阶函数](./14_higher_order_functions.md)         |
| 15     |             [类型错误](./15_python_type_errors.md)             |
| 16     |            [Python 日期时间](./16_python_datetime.md)            |
| 17     |             [异常处理](./17_exception_handling.md)             |
| 18     |           [正则表达式](./18_regular_expressions.md)           |
| 19     |                  [文件处理](./19_file_handling.md)                  |
| 20     |         [包管理器](./20_python_package_manager.md)         |
| 21     |            [类和对象](./21_classes_and_objects.md)            |
| 22     |                   [网页抓取](./22_web_scraping.md)                   |
| 23     |            [虚拟环境](./23_virtual_environment.md)            |
| 24     |                       [统计](./24_statistics.md)                       |
| 25     |                          [Pandas](./25_pandas.md)                          |
| 26     |                   [Python 网页](./26_python_web.md)                    |
| 27     |       [Python 与 MongoDB](./27_python_with_mongodb.md)        |
| 28     |                              [API](./28_API.md)                               |
| 29     |                   [构建 API](./29_building_API.md)                   |
| 30     |                      [结论](./30_conclusions.md)                      |

🧡🧡🧡 快乐编码 🧡🧡🧡

<div>
<small>帮助 <strong>作者</strong> 创作更多教育材料</small> <br />  
<a href = "https://www.paypal.me/asabeneh"><img src='.././images/paypal_lg.png' alt='Paypal Logo' style="width:10%"/></a>
</div>

<div align="center">
  <h1> 30 天 Python：第 1 天 - 介绍</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者：
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> 第二版：2021 年 7 月</small>
</sub>

</div>

[第 2 天 >>](./02_variables_builtin_functions.md)

![30DaysOfPython](.././images/30DaysOfPython_banner3@2x.png)

- [🐍 30 天 Python](#-30-天-python)
- [📘 第 1 天](#-第-1-天)
  - [欢迎！](#欢迎)
  - [介绍](#介绍)
  - [为什么选择 Python？](#为什么选择-python)
  - [环境设置](#环境设置)
    - [安装 Python](#安装-python)
    - [Python Shell](#python-shell)
    - [安装 Visual Studio Code](#安装-visual-studio-code)
      - [如何使用 Visual Studio Code](#如何使用-visual-studio-code)
  - [Python 基础](#python-基础)
    - [Python 语法](#python-语法)
    - [Python 缩进](#python-缩进)
    - [注释](#注释)
- [示例：单行注释](#示例单行注释)
- [示例：多行注释，称为文档字符串](#示例多行注释称为文档字符串)
    - [数据类型](#数据类型)
      - [数字](#数字)
      - [字符串](#字符串)
      - [布尔值](#布尔值)
      - [列表](#列表)
      - [字典](#字典)
      - [元组](#元组)
      - [集合](#集合)
    - [检查数据类型](#检查数据类型)
    - [Python 文件](#python-文件)
  - [💻 练习 - 第 1 天](#-练习---第-1-天)
    - [练习：等级 1](#练习等级-1)
    - [练习：等级 2](#练习等级-2)
    - [练习：等级 3](#练习等级-3)

# 📘 第 1 天

## 欢迎！

**恭喜** 你决定参加 _30 天 Python_ 编程挑战。在这个挑战中，你将学习成为一名 Python 程序员所需的一切以及所有编程概念。挑战结束时，你将获得 _30DaysOfPython_ 编程挑战证书。

如果你想积极参与挑战，可以加入 Telegram 群组 [30DaysOfPython challenge](https://t.me/ThirtyDaysOfPython)。

## 介绍

Python 是一种高级编程语言，适用于通用编程。它是一种开源、解释性和面向对象的编程语言。Python 由荷兰程序员 Guido van Rossum 创建。编程语言 Python 的名称来源于英国喜剧系列 _Monty Python's Flying Circus_。第一个版本于 1991 年 2 月 20 日发布。这个 30 天的 Python 挑战将帮助你逐步学习最新版本的 Python，Python 3。每一天都有不同的主题，包含易于理解的解释、现实世界的示例、大量的实际练习和项目。

本挑战适合初学者和希望学习 Python 编程语言的专业人士。完成挑战可能需要 30 到 100 天，积极参与 Telegram 群组的成员更有可能完成挑战。

本挑战易于阅读，最初以通俗英语编写，并翻译成中文，既具有吸引力、激励性，又具有很高的挑战性。你需要投入大量时间来完成这个挑战。如果你是通过观看学习效果更好的人，可以观看视频教程，访问 <a href="https://www.youtube.com/channel/UC7PNRuno1rzYPb1xLa4yktw">
Washera YouTube 频道</a> 你可以从 [Python 对绝对初学者的视频](https://youtu.be/OCCWZheOesI) 开始。订阅频道，在 YouTube 视频中评论你的问题，并积极主动，作者最终会注意到你。

作者喜欢听取你对挑战的意见，分享文章并反馈你对 30DaysOfPython 挑战的看法。你可以在此处留下对文章的反馈：[link](https://www.asabeneh.com/testimonials)

## 为什么选择 Python？

它是一种非常接近人类语言的编程语言，语法简单，因此易于学习和使用。
Python 被各行各业和公司（包括 Google）使用。它被用于开发 Web 应用程序、桌面应用程序、系统管理和机器学习库。Python 在数据科学和机器学习社区中被广泛采用。希望这足以说服你开始学习 Python。

## 环境设置

### 安装 Python

要运行用 Python 编写的脚本，你需要安装 Python。访问 [Python 下载页面](https://www.python.org/)。

如果你是 Windows 用户。点击红色圈出的按钮。

[![在 Windows 上安装](.././images/installing_on_windows.png)](https://www.python.org/)

如果你是 MacOS 用户。点击红色圈出的按钮。

[![在 MacOS 上安装](.././images/installing_on_macOS.png)](https://www.python.org/)

要检查是否安装了 Python，请在设备的终端中输入以下命令。

```shell
python --version
```

![Python Version](../images/python_versio.png)

如你所见，在终端中，我当前使用的版本是 Python 3.7.5。你的 Python 版本可能与我的不同，但应为 3.6 或更高版本。如果你能看到 Python 版本，很好。Python 已安装在你的机器上。继续下一部分。

### Python Shell

Python 是一种解释型脚本语言，因此不需要编译。这意味着它逐行执行代码。Python 附带一个 Python Shell (Python 交互式 Shell)，也称为 REPL (Read Eval Print Loop)。它用于执行单个 Python 命令并获得结果。

Python Shell 等待用户的 Python 代码。当输入代码时，它会解释并显示结果。
打开终端或命令提示符 (cmd) 并输入：

```shell
python
```

![Python Scripting Shell](../images/opening_python_shell.png)

Python 交互式 Shell 已打开，等待你在该符号 >>> 旁边编写 Python 代码（Python 脚本）。编写第一个脚本并点击 Enter。
让我们在 Python 脚本 Shell 中编写第一个脚本。

![Python script on Python shell](../images/adding_on_python_shell.png)

非常好，你已经在 Python 交互式 Shell 中编写了第一个 Python 脚本。如何关闭 Python 交互式 Shell？
要关闭 Shell，请在该符号 >>> 旁边输入命令 **exit()** 并按 Enter。

![Exit from python shell](../images/exit_from_shell.png)

现在你知道如何打开 Python 交互式 Shell 以及如何退出它。

Python 将在你编写 Python 可理解的脚本时提供结果；否则，它将返回错误。让我们故意犯一个错误，看看 Python 返回什么。

![Invalid Syntax Error](../images/invalid_syntax_error.png)

如你所见，返回的错误表明 Python 非常智能，它知道我们犯了语法错误：Syntax Error: Invalid Syntax。在 Python 中使用 x 作为乘法是语法错误，因为 (x) 不是 Python 中的有效语法。我们用星号 (\*) 来表示乘法而不是 (x)。返回的错误明确显示了需要修正的地方。

识别和删除程序中的错误的过程称为调试。让我们通过将 \* 替换为 x 来调试它。

![Fixing Syntax Error](../images/fixing_syntax_error.png)

我们的错误已修复，代码已执行，并得到了我们期望的结果。作为程序员，你每天都会看到这种类型的错误。了解如何调试是很重要的。为了擅长调试，你必须了解所遇到的错误类型。你可能会遇到的 Python 错误类型有 _SyntaxError_, _IndexError_, _NameError_, _ModuleNotFoundError_, _KeyError_, _ImportError_, _AttributeError_, _TypeError_, _ValueError_, _ZeroDivisionError_ 等等。我们将在后面的部分详细了解不同类型的 Python 错误！

让我们更多地练习如何使用 Python 交互式 Shell。转到终端或命令提示符并输入单词 python。

![Python Scripting Shell](../images/opening_python_shell.png)

Python 交互式 Shell 已打开。让我们做一些基本的数学运算（加法、减法、乘法、除法、取模、指数运算）。

在编写任何 Python 代码之前，让我们做一些数学运算：

- 2 + 3 是 5
- 3 - 2 是 1
- 3 \* 2 是 6
- 3 / 2 是 1.5
- 3 \*_ 2 相当于 3 _ 3

在 Python 中，我们有以下附加运算：

- 3 % 2 = 1 => 这意味着找到余数或（除法的模数）
- 3 // 2 = 1 => 这意味着删除除法的余数

让我们将上述数学表达式转换为 Python 代码。已打开 Python Shell，让我们在 Shell 的开头编写一个注释。

A _comment_ 是代码中未被 Python 执行的一部分，注释被 Python 解释器忽略。因此，我们可以在代码中留下某些文本以提高其可读性。Python 不执行注释部分。Python 中的注释以井号 (#) 符号开头。
这就是你在 Python 中编写注释的方式：

```python
# 注释以井号开头
# 这是一个python注释，因为它以（#）符号开头
```

![Maths on python shell](../images/maths_on_python_shell.png)

在进入下一部分之前，让我们更多地练习 Python 交互式 Shell。通过在 Shell 中输入 _exit()_ 关闭已打开的 Shell，然后再次打开它，让我们练习如何在 Python Shell 中编写文本。

![Writing String on python shell](./images/writing_string_on_shell.png)

### 安装 Visual Studio Code

Python 交互式 Shell 非常适合测试小的脚本代码，但对于大型项目来说并不适用。在实际的工作环境中，开发人员使用不同的代码编辑器来编写代码。在这个 30 天的 Python 编程挑战中，我们将使用 Visual Studio Code。Visual Studio Code 是一个非常流行的开源文本编辑器。我是 vscode 的粉丝，并推荐下载 Visual Studio Code，但如果你喜欢其他编辑器，可以随意使用。

[![Visual Studio Code](../images/vscode.png)](https://code.visualstudio.com/)

如果你已安装 Visual Studio Code，让我们看看如何使用它。
如果你喜欢视频教程，你可以观看安装和配置 Visual Studio Code 以用于 Python 的[视频教程](https://www.youtube.com/watch?v=bn7Cx4z-vSo)

#### 如何使用 Visual Studio Code

通过双击 Visual Studio 图标打开 Visual Studio Code。打开后，你会看到类似的界面。尝试与标注的图标进行交互。

![Visual studio Code](../images/vscode_ui.png)

在桌面上创建一个名为 30DaysOfPython 的文件夹。然后使用 Visual Studio Code 打开它。

![Opening Project on Visual studio](../images/how_to_open_project_on_vscode.png)

![Opening a project](../images/opening_project.png)

打开后，你会看到在 30DaysOfPython 项目目录中创建文件和文件夹的快捷方式。如下所示，我创建了第一个文件 helloworld.py。你也可以这样做。

![Creating a python file](../images/helloworld.png)

经过长时间的编码，你想关闭你的代码编辑器，对吗？这是你关闭已打开项目的方法。

![Closing project](../images/closing_opened_project.png)

恭喜你，完成了开发环境的设置。让我们开始编码。

## Python 基础

### Python 语法

Python 脚本可以在 Python 交互式 Shell 或代码编辑器中编写。Python 文件的扩展名为 .py。

### Python 缩进

缩进是文本中的空白。在许多语言中，缩进用于提高代码的可读性，但 Python 使用缩进来创建代码块。在其他编程语言中，使用大括号来创建代码块，而不是缩进。在 Python 中编写代码时，一个常见的错误是缩进错误。

![Indentation Error](../images/indentation.png)

### 注释

注释对于提高代码的可读性和在代码中留下注释非常重要。Python 不执行代码中的注释部分。
在 Python 中，任何以井号 (#) 开头的文本都是注释。

# 示例：单行注释

```shell
# 这是第一个注释
# 这是第二个注释
# Python 正在吞噬世界
```

# 示例：多行注释，称为文档字符串

三重引号可以用于多行注释，如果它没有被分配给变量。

```shell
"""这是多行注释
多行注释占用多行。
Python 正在吞噬世界
"""
```

### 数据类型

Python 中有多种数据类型。让我们从最常见的开始。不同的数据类型将在其他部分详细讨论。现在，让我们浏览一下不同的数据类型并熟悉它们。你现在不需要有明确的理解。

#### 数字

- 整数：它被认为是整数（负数、零和正数）
  示例：
  ... -3, -2, -1, 0, 1, 2, 3 ...
- 浮点数：小数
  示例：
  ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- 复数
  示例：
  1 + j, 2 + 4j

#### 字符串

一串字符组成的文本，使用单引号或双引号表示。如果字符串超过一行，可以使用三引号。

**例子:**

```py
'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
```

#### 布尔值

布尔值是 True 或 False。T 和 F 必须大写。

**例子:**

```python
True # 灯是开的吗？如果是开着的，那么值是 True
False # 灯是开的吗？如果是关着的，那么值是 False
```

#### 列表

列表是一个有序的集合，可以存储不同类型的数据。类似于 JavaScript 中的数组。

**例子:**

```py
[0, 1, 2, 3, 4, 5] # 所有都是相同数据类型 - 数字列表
['Banana', 'Orange', 'Mango', 'Avocado'] # 所有都是相同数据类型 - 字符串列表（水果）
['Finland','Estonia', 'Sweden','Norway'] # 所有都是相同数据类型 - 字符串列表（国家）
['Banana', 10, False, 9.81] # 列表中的不同数据类型 - 字符串、整数、布尔值和浮点数
```

#### 字典

Python 字典对象是以键值对格式存储的无序集合。

**例子:**

```py
{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland',
'age':250,
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
```

#### 元组

元组是一个有序的集合，类似于列表，但元组一旦创建就不能修改。它们是不可变的。

**例子:**

```py
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # 名字
```

```py
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # 行星
```

#### 集合

集合是类似于列表和元组的集合数据类型。与列表和元组不同，集合不是一个有序的集合。就像在数学中一样，Python 中的集合只存储唯一的项目。

在后面的部分，我们将详细介绍每种 Python 数据类型。

**例子:**

```py
{2, 4, 3, 5}
{3.14, 9.81, 2.7} # 集合中的顺序不重要
```

### 检查数据类型

要检查某个数据/变量的数据类型，我们使用 **type** 函数。在以下终端中，你将看到不同的 Python 数据类型：

![Checking Data types](../images/checking_data_types.png)

### Python 文件

首先打开你的项目文件夹，30DaysOfPython。如果你没有这个文件夹，创建一个名为 30DaysOfPython 的文件夹。在这个文件夹内，创建一个名为 helloworld.py 的文件。现在，让我们在 Visual Studio Code 中做我们在 Python 交互式 Shell 中所做的事情。

Python 交互式 Shell 在不使用 **print** 的情况下打印，但在 Visual Studio Code 中，为了查看我们的结果，我们应该使用内置函数 _print()_。_print()_ 内置函数接受一个或多个参数，如下所示 _print('arument1', 'argument2', 'argument3')_。请参见以下示例。

**例子:**

​ 文件名是 helloworld.py

```py
# 第 1 天 - 30DaysOfPython 挑战

print(2 + 3)             # 加法(+)
print(3 - 1)             # 减法(-)
print(2 * 3)             # 乘法(*)
print(3 / 2)             # 除法(/)
print(3 ** 2)            # 指数(**)
print(3 % 2)             # 取模(%)
print(3 // 2)            # 整除(//)

# 检查数据类型
print(type(10))          # 整数
print(type(3.14))        # 浮点数
print(type(1 + 3j))      # 复数
print(type('Asabeneh'))  # 字符串
print(type([1, 2, 3]))   # 列表
print(type({'name':'Asabeneh'})) # 字典
print(type({9.8, 3.14, 2.7}))    # 集合
print(type((9.8, 3.14, 2.7)))    # 元组
```

要运行 Python 文件，请查看下图。你可以通过在 Visual Studio Code 中点击绿色按钮或在终端中输入 _python helloworld.py_ 来运行 Python 文件。

![Running python script](../images/running_python_script.png)

🌕 你很棒。你刚刚完成了第 1 天的挑战，你正在迈向伟大。现在做一些练习来锻练你的大脑和肌肉。

## 💻 练习 - 第 1 天

### 练习：等级 1

1. 检查你使用的 Python 版本
2. 打开 Python 交互式 Shell 并执行以下操作。操作数是 3 和 4。
   - 加法(+)
   - 减法(-)
   - 乘法(\*)
   - 取模(%)
   - 除法(/)
   - 指数(\*\*)
   - 整除(//)
3. 在 Python 交互式 Shell 中编写字符串。字符串如下：
   - 你的名字
   - 你的姓氏
   - 你的国家
   - 我正在享受 30 天的 Python
4. 检查以下数据的数据类型：
   - 10
   - 9.8
   - 3.14
   - 4 - 4j
   - ['Asabeneh', 'Python', 'Finland']
   - 你的名字
   - 你的姓氏
   - 你的国家

### 练习：等级 2

1. 在 30DaysOfPython 文件夹中创建一个名为 day*1 的文件夹。在 day_1 文件夹中，创建一个名为 helloworld.py 的 Python 文件，并重复问题 1、2、3 和 4。记住在处理 Python 文件时使用 \_print()*。导航到你保存文件的目录，并运行它。

### 练习：等级 3

1. 为不同的 Python 数据类型编写一个示例，如数字（整数、浮点数、复数）、字符串、布尔值、列表、元组、集合和字典。
2. 找到 (2, 3) 和 (10, 8) 之间的 [欧几里得距离](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance)。

🎉 恭喜 ! 🎉

[第 2 天 >>](./02_variables_builtin_functions.md)

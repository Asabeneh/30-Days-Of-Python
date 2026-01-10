# 30天Python编程挑战：第15天 - Python类型错误

- [Day 15](#day-15)
  - [Python错误类型](#python错误类型)
    - [SyntaxError (语法错误)](#syntaxerror-语法错误)
    - [NameError (名称错误)](#nameerror-名称错误)
    - [IndexError (索引错误)](#indexerror-索引错误)
    - [ModuleNotFoundError (模块未找到错误)](#modulenotfounderror-模块未找到错误)
    - [AttributeError (属性错误)](#attributeerror-属性错误)
    - [KeyError (键错误)](#keyerror-键错误)
    - [TypeError (类型错误)](#typeerror-类型错误)
    - [ImportError (导入错误)](#importerror-导入错误)
    - [ValueError (值错误)](#valueerror-值错误)
    - [ZeroDivisionError (零除错误)](#zerodivisionerror-零除错误)
  - [💻 练习 - 第15天](#-练习---第15天)

# 📘 Day 15

## Python错误类型

当我们编写代码时，常常会出现打字错误或其他常见错误。如果我们的代码运行失败，Python解释器会显示一条消息，提供有关问题发生位置和错误类型的反馈信息。有时它还会给我们提供可能的修复建议。了解编程语言中不同类型的错误将帮助我们快速调试代码，并使我们在编程技能上有所提高。

让我们一一查看最常见的错误类型。首先，让我们打开Python交互式shell。转到你的计算机终端并输入'python'。Python交互式shell将会被打开。

### SyntaxError (语法错误)

**示例1: SyntaxError**

```python
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

如你所见，我们犯了一个语法错误，因为我们忘记用括号括起字符串，而Python已经提出了解决方案。让我们修复它。

```python
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

错误是一个_SyntaxError_。修复后，我们的代码顺利执行。让我们看看更多的错误类型。

### NameError (名称错误)

**示例1: NameError**

```python
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

从上面的消息可以看出，名称age没有被定义。是的，确实如此，我们没有定义age变量，但我们试图像已经声明了一样打印它。现在，让我们通过声明变量并为其赋值来修复这个问题。

```python
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

错误类型是_NameError_。我们通过定义变量名来调试了错误。

### IndexError (索引错误)

**示例1: IndexError**

```python
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

在上面的例子中，Python抛出了一个_IndexError_，因为列表的索引只有0到4，所以索引5超出了范围。

### ModuleNotFoundError (模块未找到错误)

**示例1: ModuleNotFoundError**

```python
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

在上面的例子中，我故意在math后面添加了一个多余的s，结果抛出了_ModuleNotFoundError_。让我们通过从math中删除多余的s来修复它。

```python
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

我们修复了它，所以让我们使用math模块中的一些函数。

### AttributeError (属性错误)

**示例1: AttributeError**

```python
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

如你所见，我又犯了一个错误！我试图从math模块调用PI函数，而不是pi。这抛出了一个属性错误，表示该函数在模块中不存在。让我们通过将PI更改为pi来修复它。

```python
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

现在，当我们从math模块调用pi时，我们得到了结果。

### KeyError (键错误)

**示例1: KeyError**

```python
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

如你所见，在用于获取字典值的键中有一个拼写错误。这是一个键错误，修复方法很简单。让我们来做这个！

```python
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

我们调试了错误，我们的代码运行并得到了结果。

### TypeError (类型错误)

**示例1: TypeError**

```python
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

在上面的例子中，出现了TypeError，因为我们不能将数字与字符串相加。第一个解决方案是将字符串转换为int或float。另一个解决方案是将数字转换为字符串（那么结果将是'43'）。让我们采用第一种修复方式。

```python
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

错误已消除，我们得到了预期的结果。

### ImportError (导入错误)

**示例1: ImportError**

```python
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

math模块中没有名为power的函数，它的名字是不同的：_pow_。让我们纠正它：

```python
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

### ValueError (值错误)

```python
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

在这种情况下，我们无法将给定的字符串转换为数字，因为其中有字母'a'。

### ZeroDivisionError (零除错误)

```python
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

我们不能用零去除一个数字。

我们已经介绍了一些Python错误类型，如果你想了解更多，请查看Python文档中关于Python错误类型的内容。
如果你擅长阅读错误类型，那么你将能够快速修复你的bug，你也将成为一个更好的程序员。

🌕 你正在进步。你已经完成了一半的道路，正走向伟大。现在做一些练习来锻炼你的大脑和肌肉。

## 💻 练习 - 第15天

1. 打开你的Python交互式shell，尝试本节中介绍的所有示例。

🎉 恭喜！🎉

[<< 第 14 天](./14_higher_order_functions.md) | [第 16 天 >>](./16_python_datetime_cn.md) 
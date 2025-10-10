# 30天Python编程挑战：第17天 - 异常处理

- [第17天](#-第17天)
  - [异常处理](#异常处理)
  - [Python中的打包和解包参数](#python中的打包和解包参数)
    - [解包](#解包)
      - [解包列表](#解包列表)
      - [解包字典](#解包字典)
    - [打包](#打包)
    - [打包列表](#打包列表)
      - [打包字典](#打包字典)
  - [Python中的展开](#python中的展开)
  - [枚举](#枚举)
  - [Zip](#zip)
  - [练习：第17天](#练习第17天)

# 📘 第17天

## 异常处理

Python使用 _try_ 和 _except_ 优雅地处理错误。优雅的退出（或优雅的错误处理）是一种简单的编程习惯 - 程序检测到严重的错误条件并"优雅地退出"，即以受控的方式处理结果。通常，程序会在优雅退出时向终端或日志打印描述性错误消息，这使我们的应用程序更加健壮。异常的原因通常是程序本身之外的因素，例如错误的输入、错误的文件名、找不到文件、IO设备故障等。优雅的错误处理可以防止我们的应用程序崩溃。

我们在前一部分已经介绍了不同类型的Python _错误_。如果我们在程序中使用 _try_ 和 _except_，那么这些块中就不会引发错误。

![Try and Except](../images/try_except.png)

```py
try:
    # 如果一切正常，执行这个块中的代码
except:
    # 如果出错，执行这个块中的代码
```

**示例：**

```py
try:
    print(10 + '5')
except:
    print('出现了一些错误')
```

在上面的例子中，第二个操作数是一个字符串。我们可以将其更改为float或int，使其能够与数字相加。但如果不做任何更改，第二个块 _except_ 将被执行。

**示例：**

```py
try:
    name = input('输入你的名字:')
    year_born = input('你出生的年份:')
    age = 2019 - year_born
    print(f'你是{name}. 你的年龄是{age}.')
except:
    print('出现了一些错误')
```

```sh
出现了一些错误
```

在上面的例子中，异常块将运行，但我们不知道具体的问题是什么。为了分析问题，我们可以使用不同的错误类型配合except。

在下面的例子中，它将处理错误，并且告诉我们引发了什么类型的错误。

```py
try:
    name = input('输入你的名字:')
    year_born = input('你出生的年份:')
    age = 2019 - year_born
    print(f'你是{name}. 你的年龄是{age}.')
except TypeError:
    print('发生了类型错误')
except ValueError:
    print('发生了值错误')
except ZeroDivisionError:
    print('发生了除零错误')
```

```sh
输入你的名字:Asabeneh
你出生的年份:1920
发生了类型错误
```

在上述代码中，输出将是 _TypeError_。
现在，让我们添加一个额外的块：

```py
try:
    name = input('输入你的名字:')
    year_born = input('你出生的年份:')
    age = 2019 - int(year_born)
    print(f'你是{name}. 你的年龄是{age}.')
except TypeError:
    print('发生了类型错误')
except ValueError:
    print('发生了值错误')
except ZeroDivisionError:
    print('发生了除零错误')
else:
    print('我通常与try块一起运行')
finally:
    print('我总是运行。')
```

```sh
输入你的名字:Asabeneh
你出生的年份:1920
你是Asabeneh. 你的年龄是99.
我通常与try块一起运行
我总是运行。
```

也可以将上述代码简化如下：

```py
try:
    name = input('输入你的名字:')
    year_born = input('你出生的年份:')
    age = 2019 - int(year_born)
    print(f'你是{name}. 你的年龄是{age}.')
except Exception as e:
    print(e)
```

## Python中的打包和解包参数

我们使用两个操作符：

- \* 用于元组
- \*\* 用于字典

让我们看一个例子。假设函数只接受参数，但我们有一个列表。我们可以解包列表并将其转换为参数。

### 解包

#### 解包列表

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

当我们运行这段代码时，会引发错误，因为这个函数接受数字（而不是列表）作为参数。让我们解包/解构这个列表。

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

我们也可以在内置的range函数中使用解包，该函数需要一个起始和结束参数。

```py
numbers = range(2, 7)  # 正常调用，使用单独的参数
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # 使用从列表解包的参数调用
print(numbers)      # [2, 3, 4, 5,6]
```

列表或元组也可以这样解包：

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### 解包字典

```py
def unpacking_person_info(name, country, city, age):
    return f'{name}住在{country}的{city}。他{age}岁。'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh住在Finland的Helsinki。他250岁。
```

### 打包

有时候我们不知道需要向Python函数传递多少个参数。我们可以使用打包方法让我们的函数接受无限数量或任意数量的参数。

### 打包列表

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### 打包字典

```py
def packing_person_info(**kwargs):
    # 检查kwargs的类型，它是一个字典类型
    # print(type(kwargs))
    # 打印字典项
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

## Python中的展开

与JavaScript类似，Python中也可以进行展开操作。让我们通过下面的例子来看看：

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
```

## 枚举

如果我们对列表的索引感兴趣，我们使用enumerate内置函数。

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```py
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('国家 {i} 位于索引 {index}')
```

```sh
0 20
1 30
2 40
```

## Zip

有时，我们可能需要将列表组合起来。看看以下示例：

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

## 练习：第17天

1. 为名为 _countries_data.py_ 的文件中的数据创建一个名为 _countries.py_ 的函数。
   - 创建一个函数，找出十大使用的语言
   - 创建一个函数，找出十大人口最多的国家

🎉 恭喜！🎉

[<< 第 16 天](./16_python_datetime_cn.md) | [第 18 天 >>](./18_regular_expressions_cn.md) 
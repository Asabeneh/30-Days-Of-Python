<div align="center">
  <h1> 30 天 Python：第十天 - Loops</h1>
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

[<<第九天](../Chinese/09_conditionals.md) | [第十一天>>](../Chinese/11_functions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)


- [📘 第十天](#-第十天)
  - [循环](#循环)
    - [while 循环](#while-循环)
    - [break和continue - part 1](#break和continue---part-1)
    - [for 循环](#for-循环)
    - [break 和 continue - part 2](#break-和-continue---part-2)
    - [range() 函数](#range-函数)
    - [嵌套for循环](#嵌套for循环)
    - [for和else](#for和else)
    - [pass语句](#pass语句)
  - [💻 练习：第十天](#-练习第十天)
    - [练习：一级](#练习一级)
    - [练习：二级](#练习二级)
    - [练习：三级](#练习三级)

# 📘 第十天

## 循环

生活充满了循环。在编程中，我们会做很多重复的任务。编程语言使用循环来处理重复的任务，而Python编程语言提供了以下两种类型的循环:
1. while 循环
2. for 循环

### while 循环

我们使用关键字`while`来创建while循环。它在条件被满足时重复执行代码块。当条件变为false时，会结束循环代码块，执行循环之后的代码。

```python
  # syntax
while condition:
    code goes here
```

**示例:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
```

在上面的循环中，当count等于5时，循环条件变为false，此时循环停止。

如果我们想要在循环条件变为false时运行特定的代码块，我们可以使用`else`关键字。

```python
  # syntax
while condition:
    code goes here
else:
    code goes here
```

**示例:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

当count等于5时，循环条件变为false，循环终止，然后开始执行else块中的代码。因此，5将会被打印输出。

### break和continue - part 1

* Break：当我们想要退出循环时，我们使用`break`关键字。

```python
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

**Example:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```
上面的while循环只会打印输出0，1，2，但当count等于3时，循环会终止。
- Continue：当我们想要跳过当前循环并继续执行下一个循环时，我们使用`continue`关键字。

```python
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

**示例:**

```python
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
```

上面的while循环只会打印输出0，1，2，4。（3被跳过了）

### for 循环

`for`关键字用于创建for循环。和别的编程语言相似，但语法上有一些不同。它可以用于对序列的遍历（也就是列表、元组、字典、集合、字符串等）。

- 列表的for循环

```python
# syntax
for iterator in lst:
    code goes here
```

**示例:**

```python
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number是引用列表项的临时名称，仅在此循环中有效
    print(number)       # number将会被逐行打印，从0到5
```

- 字符串的for循环

```python
# syntax
for iterator in string:
    code goes here
```

**示例:**

```python
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])
```

- 元组的for循环

```python
# syntax
for iterator in tpl:
    code goes here
```

**示例:**

```python
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- 字典的for循环
  循环遍历将会遍历字典的键。

```python
  # syntax
for iterator in dct:
    code goes here
```

**示例:**

```python
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key) #仅输出键

for key, value in person.items():
    print(key, value) # 这样我们可以在迭代的过程中同时访问键和值
```

- 集合的for循环

```python
# syntax
for iterator in st:
    code goes here
```

**示例:**

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### break 和 continue - part 2

提示：
_break_:当我们想要在循环完成前退出循环时，我们使用`break`关键字。

```python
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

**示例:**

```python
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)#输出 0，1，2，3
    if number == 3:
        break
```
在上面的例子中，当number等于3时，循环会终止。

_continue_:当我们想要跳过当前循环并继续执行下一个循环时，我们使用`continue`关键字。

```python
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**示例:**

```python
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # 简而言之，对于简短的条件，需要同时使用if和else语句
print('outside the loop')
```
在上面的例子中，当number等于3时，在此条件之后的（但在循环中的）语句会被跳过，如果还有未完成的遍历元素，它会继续执行下一个循环。

### range() 函数

`range()`函数用于生成一个序列的数字。_range(start, end, step)_函数接受三个参数：起始值、结束值和步长。默认情况下，起始值是0，步长是1。这个函数需要至少一个参数。（结束值end）

使用`range()`函数生成序列

```python
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 两个参数分别代表start和stop，步长step为默认值1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```python
# syntax
for iterator in range(start, end, step):
```

**示例:**

```python
for number in range(11):
    print(number)   # 打印输出0到10，不包括11。
```

### 嵌套for循环

我们可以在循环中嵌套另一个循环。这种循环称为嵌套循环。

```python
# syntax
for x in y:
    for t in x:
        print(t)
```

**示例:**

```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### for和else

如果我们想要在循环结束时执行特定的代码块，我们可以使用`else`关键字。

```python
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**示例:**

```python
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

### pass语句

在python中，当需要一些语句（比如在`:`后），但我们不想执行任何代码时，我们可以使用`pass`关键字来避免报错。此外，我们也可以用它来作为一个占位符，以便在以后填充代码。

**示例:**

```python
for number in range(6):
    pass
```

🌕 你完成了伟大的一步，太猛了哥。冲冲冲！你刚刚完成了第10天的挑战，你在通往伟大的道路上迈出了10步。现在我们做一些练习来练练肌肉和大脑。

## 💻 练习：第十天

### 练习：一级

1. 分别使用while和for实现从0到10的迭代。
2. 分别使用while和for实现从10到0的迭代。
3. 写一个循环，调用7次`print()`函数，输出如下的三角形：
    ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. 使用嵌套循环来实现下面的输出：

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```
5. 使用循环实现下面格式的输出：
   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```
6. 用for循环遍历列表`['Python', 'Numpy','Pandas','Django', 'Flask']`，并打印输出每个元素。
7. 用for循环从0到100遍历并且打印输出所有偶数。
8. 用for循环从0到100遍历并且打印输出所有奇数。

### 练习：二级

1. 使用for循环从0到100遍历并且输出所有数字的和。
    ```sh
   The sum of all numbers is 5050.
   ```
2. 使用for循环从0到100遍历并且分别输出所有奇数和所有偶数的和。
    ```sh
   The sum of all odd numbers is 2500. And the sum of all even numbers is 2550.
   ```

### 练习：三级

1. 跳转到data文件夹并使用[countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py)文件。循环遍历所有国家，并且提取出所有包含字母`land`的国家。
2. 有一个列表`fruits = ['banana', 'orange', 'mango', 'lemon']`，使用循环反转列表中的元素。
3. 跳转到data文件夹并使用[countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py)文件。
   1. 数据中一共有多少个语言？
   2. 找到被最多国家使用的语言。
   3. 找到人数排名前十的国家。

🎉 恭喜！ 🎉

[<< Day 9](./09_conditionals.md) | [Day 11 >>](./11_functions.md)
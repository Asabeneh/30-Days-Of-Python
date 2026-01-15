<div align="center">
  <h1> 30 天 Python：第五天 - Lists</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> 第二版：2021 年 7 月</small>
</sub>

</div>

[<< 第四天](./04_strings.md) | [第六天 >>](./06_tuples.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [第五天](#第五天)
  - [列表](#列表)
    - [如何创建列表](#如何创建列表)
    - [使用正索引访问列表项](#使用正索引访问列表项)
    - [使用负索引访问列表项](#使用负索引访问列表项)
    - [拆解列表项](#拆解列表项)
    - [列表切分](#列表切分)
    - [修改列表](#修改列表)
    - [检索列表项](#检索列表项)
    - [添加列表项](#添加列表项)
    - [插入列表项](#插入列表项)
    - [移除列表项](#移除列表项)
    - [使用 Pop 删除列表项](#使用-pop-删除列表项)
    - [使用 Del 删除列表项](#使用-del-删除列表项)
    - [清空列表项](#清空列表项)
    - [列表复制](#列表复制)
    - [连接列表](#连接列表)
    - [统计列表项](#统计列表项)
    - [查找项的索引](#查找项的索引)
    - [列表反转](#列表反转)
    - [列表排序](#列表排序)
  - [💻 练习 - 第五天](#-练习---第五天)
    - [练习： 1级](#练习-1级)
    - [练习： 2级](#练习-2级)

# 第五天

## 列表

Python 中有四种集合数据类型：

- List：有序且可变的集合。允许重复的成员。
- Tuple：有序且不可变的集合。允许重复的成员。
- Set：无序、不可索引且不可变的集合，但我们可以向集合中添加新项。不允许重复的成员。
- Dictionary：无序、可变且可索引的集合。不允许重复的成员。


列表是不同数据类型的集合，有序且可修改（可变）。列表可以为空，也可以包含不同数据类型的项。

### 如何创建列表

在 Python 中，我们可以通过两种方式创建列表：

- 使用内置函数 list()

```py
# 语法
lst = list()
```

```py
empty_list = list() # 这是一个空列表
print(len(empty_list)) # 0
```
- 使用方括号，[]

```py
# 语法
lst = []
```

```py
empty_list = [] # 这是一个空列表
print(len(empty_list)) # 0
```

具有初始值的列表。我们使用 _len()_ 来检查列表的长度。

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# 打印列表及其长度
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```

```sh
输出
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

- 列表可以包含不同数据类型的项

```py
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # 包含不同数据类型的列表
```


### 使用正索引访问列表项

我们使用索引访问列表中的每个项。列表索引从 0 开始。下图清楚地显示了索引从哪里开始。

![List index](../images/list_index.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # 我们正在使用其索引访问第一项
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

### 使用负索引访问列表项

负索引意味着从末尾开始，-1 指的是最后一项，-2 指的是倒数第二项。

![List negative indexing](../images/list_negative_indexing.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

### 拆解列表项

```py
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```

```py
# 示例一
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# 示例二
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# 示例三
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

### 列表切分

- 正索引：我们可以通过指定开始、结束和步长来指定一系列正索引，返回值将是一个新列表。 （开始默认值为 0，结束默认值为 len(lst) - 1（最后一项），步长默认值为 1）

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # 返回所有项
#与上面返回值相同
all_fruits = fruits[0:] # 如果不指定结束索引，将返回从开始到最后一项的所有项
orange_and_mango = fruits[1:3] # 不包含第一项
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # 我们使用了第三个参数，步长。 每两项取一条 - ['banana', 'mango']
```

- 负索引：我们可以通过指定开始、结束和步长来指定一系列负索引，返回值将是一个新列表。

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # 返回所有项
orange_and_mango = fruits[-3:-1] # 不包含最后一项，['orange', 'mango']
orange_mango_lemon = fruits[-3:] # 返回从-3到末尾的项，['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # 负步长将按相反顺序排列列表,['lemon', 'mango', 'orange', 'banana']
```

### 修改列表

列表是一个可变或可修改的有序集合。下面我们修改 fruit 列表。


```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### 检索列表项

使用 *in* 运算符检查列表项是否为列表的成员。请参阅下面的示例。

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### 添加列表项

要将项添加到现有列表的末尾，我们使用 *append()* 方法。

```py
# 语法
lst = list()
lst.append(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

### 插入列表项

我们可以使用 *insert()* 方法在列表中的指定索引处插入单个项。请注意，其他项将向右移动。*insert()* 方法接受两个参数：索引和要插入的项。


```py
# 语法
lst = ['item1', 'item2']
lst.insert(index, item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # 在 orange 。 mango 中插入 apple
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

### 移除列表项

- 使用 *remove()* 方法从列表中删除指定的项

```py
# 语法
lst = ['item1', 'item2']
lst.remove(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - 此方法删除列表中第一次出现的项
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

### 使用 Pop 删除列表项

使用 *pop()* 方法删除指定索引（如果未指定索引，则删除最后一项）：

```py
# 语法
lst = ['item1', 'item2']
lst.pop()       # 最后一项
lst.pop(index)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### 使用 Del 删除列表项

使用 *del* 关键字删除指定索引，也可以用于删除索引范围内的项。它还可以完全删除列表


```py
# 语法
lst = ['item1', 'item2']
del lst[index] # 只删除一项
del lst        # 删除整个列表
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # 这将删除给定索引之间的项，因此不会删除索引为 3 的项!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # 这里会提示: NameError: name 'fruits' is not defined
```

### 清空列表项

使用 *clear()* 方法清空列表：

```py
# 语法
lst = ['item1', 'item2']
lst.clear()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

### 列表复制

可以通过将其重新分配给新变量来复制列表: list2 = list1。现在，list2 是 list1 的引用，我们对 list2 进行的任何更改也将修改原始的 list1。但是有很多时候我们不想修改原始的列表，而是想要一个不同的副本。为了避免这个问题，我们使用 *copy()*。

```py
# 语法
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### 连接列表

有几种方法可以连接或连接两个或多个列表。

- 加号 (+)

```py
# 语法
list3 = list1 + list2
```

```py
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- 使用 *extend()* 方法
*extend()* 方法可以将列表附加到列表中。请参阅下面的示例。

```py
# 语法
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

```py
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### 统计列表项

使用 *count()* 方法返回列表中指定项出现的次数:


```py
# 语法
lst = ['item1', 'item2']
lst.count(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### 查找项的索引

*index()* 方法返回列表中项的索引:

```py
# 语法
lst = ['item1', 'item2']
lst.index(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2， 第一次出现
```

### 列表反转

使用 *reverse()* 方法反转列表的顺序。

```py
# 语法
lst = ['item1', 'item2']
lst.reverse()

```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

### 列表排序

要对列表进行排序，我们可以使用 *sort()* 方法或内置函数 *sorted()*。*sort()* 方法将列表项按升序重新排序并修改原始列表。如果 *sort()* 方法的 reverse 参数为 true，则会按降序排列列表。

- sort(): 这个方法会修改原始列表

  ```py
  # 语法
  lst = ['item1', 'item2']
  lst.sort()                # ascending
  lst.sort(reverse=True)    # descending
  ```

  **示例：**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.sort()
  print(fruits)             # 按字母排序， ['banana', 'lemon', 'mango', 'orange']
  fruits.sort(reverse=True)
  print(fruits) # ['orange', 'mango', 'lemon', 'banana']
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.sort()
  print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
 
  ages.sort(reverse=True)
  print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
  ```

  sorted(): 不会修改原始列表，而是返回一个新列表

  **示例:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
  # Reverse order
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
  ```



🌕 你很勤奋，已经取得了很多成就。你刚刚完成了第 5 天的挑战，并且已经朝着伟大的目标迈出了 5 步。现在做一些练习来锻练你的大脑和肌肉。

## 💻 练习 - 第五天

### 练习： 1级

1. 声明一个空列表
2. 声明一个包含 5 个以上项的列表
3. 查找列表的长度
4. 获取列表的第一项、中间项和最后一项
5. 声明一个名为 mixed_data_types 的列表，包含你的姓名、年龄、身高、婚姻状况和地址
6. 声明一个名为 it_companies 的列表，并分配初始值 Facebook、Google、Microsoft、Apple、IBM、Oracle 和 Amazon。
7. 使用 _print()_ 打印列表
8. 打印列表中的公司数
9. 打印第一、中间和最后一家公司
10. 修改其中一家公司的名称后打印列表
11. 向 it_companies 添加一家 IT 公司
12. 在公司列表中间插入一家 IT 公司
13. 将其中一家 it_companies 公司的名称更改为大写（不包括 IBM!）
14. 使用字符串 '#;&nbsp; ' 连接 it_companies
15. 检查 it_companies 列表中是否存在某个公司。
16. 使用 sort() 方法对列表进行排序
17. 使用 reverse() 方法按降序反转列表
18. 从列表中切分出前 3 家公司
19. 从列表中切分出最后 3 家公司
20. 从列表中切分出中间的 IT 公司或公司
21. 从列表中删除第一家 IT 公司
22. 从列表中删除中间的 IT 公司或公司
23. 从列表中删除最后一家 IT 公司
24. 从列表中删除所有 IT 公司
25. 销毁 it_companies 列表
26. 连接以下列表：

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
27. 在连接的列表中插入 Python 和 SQL 到变量 full_stack 之后。

### 练习： 2级

1. 以下是 10 个学生的年龄列表：

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- 对列表进行排序，并找出最大和最小年龄
- 将最小年龄和最大年龄再次添加到列表中
- 找到年龄中位数（一个中间项或两个中间项除以二）
- 找到平均年龄（所有项的总和除以它们的数量）
- 找到年龄范围（最大减去最小）
- 比较 (min - average) 和 (max - average) 的值，使用 _abs()_ 方法

1. 在 [国家列表](https://github.com/Taki-Ta/30-Days-Of-Python-Simplified_Chinese_Version/tree/master/data/countries.py) 中查找中间的国家
2. 将国家列表分成两个相等的列表（如果是偶数，如果不是，则第一个半多一个国家）
3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']。拆解前三个国家和剩下的北欧国家。

🎉 恭喜 ! 🎉

[<< 第四天](./04_strings.md) | [第六天 >>](./06_tuples.md)

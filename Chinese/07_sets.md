<div align="center">
  <h1> 30 天 Python：第 7 天 - 集合</h1>
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

[<< 第 6 天](../06_Day_Tuples/06_tuples.md) | [第 8 天 >>](../08_Day_Dictionaries/08_dictionaries.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 7 天](#-第-7-天)
  - [集合](#集合)
    - [创建集合](#创建集合)
    - [获取集合长度](#获取集合长度)
    - [访问集合中的项目](#访问集合中的项目)
    - [检查项目](#检查项目)
    - [向集合中添加项目](#向集合中添加项目)
    - [从集合中移除项目](#从集合中移除项目)
    - [清空集合中的项目](#清空集合中的项目)
    - [删除集合](#删除集合)
    - [将列表转换为集合](#将列表转换为集合)
    - [合并集合](#合并集合)
    - [查找交集项目](#查找交集项目)
    - [检查子集和超集](#检查子集和超集)
    - [检查两个集合之间的差异](#检查两个集合之间的差异)
    - [查找两个集合之间的对称差异](#查找两个集合之间的对称差异)
    - [合并集合](#合并集合-1)
  - [💻 练习：第 7 天](#-练习-第-7-天)
    - [练习：等级 1](#练习-等级-1)
    - [练习：等级 2](#练习-等级-2)
    - [练习：等级 3](#练习-等级-3)

# 📘 第 7 天

## 集合

集合是项目的集合。让我带你回到小学或高中的数学课。集合的数学定义也适用于 Python。集合是无序且未索引的不同元素的集合。在 Python 中，集合用于存储唯一项目，可以在集合之间找到 _并集_、_交集_、_差集_、_对称差集_、_子集_、_超集_ 和 _不相交集_。

### 创建集合

我们使用 _set()_ 内置函数。

- 创建空集合

```py
# 语法
st = set()
```

- 创建一个包含初始项目的集合

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
```

**示例：**

```py
# 语法
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### 获取设置的长度

我们使用**len()**方法来查找集合的长度。

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**示例：**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

### 访问集合中的项目

我们使用循环来访问项目。我们将在循环部分看到这一点。

### 检查项目

要检查列表中是否存在某个项目，我们使用 _in_ 成员运算符。

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**示例：**

```py

fruits = {'香蕉', '橙色', '芒果', '柠檬'}

print('芒果' in fruits ) # True

```

### 向集合中添加元素

一旦集合创建后，我们不能改变其中的任何元素，但可以添加其他的元素。

- 使用 _add()_ 方法添加单个元素

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**示例:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

- 使用 _update()_ 方法添加多个元素
  _update()_ 方法允许向集合中添加多个元素。_update()_ 接收一个列表作为参数。

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**示例:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### 从集合中移除元素

我们可以使用 _remove()_ 方法从集合中移除一个元素。如果找不到该元素，_remove()_ 方法会抛出错误，因此最好先检查该元素是否存在于集合中。_discard()_ 方法则不会抛出任何错误。

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

_pop()_ 方法从集合中移除一个随机元素并返回该被移除的元素。

**示例:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # 从集合中移除一个随机元素
```

如果我们对被移除的元素感兴趣。

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
```

### 清空集合中的项目

如果我们想要清空或清除集合中的所有项目，可以使用 _clear_ 方法。

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**示例:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### 删除一个集合

如果我们想要删除整个集合，可以使用 _del_ 操作符。

```py
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**示例:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### 将列表转换为集合

我们可以将列表转换为集合，也可以将集合转换为列表。将列表转换为集合会去除重复项，只保留唯一项。

```py
# 语法
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - 顺序是随机的，因为集合在一般情况下是无序的
```

**示例:**

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### 合并集合

我们可以使用 _union()_ 或 _update()_ 方法来合并两个集合。

- Union
  这个方法返回一个新集合

```py
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

**示例:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

- Update
  这个方法将一个集合插入到给定的集合中

```py
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 的内容被添加到 st1 中
```

**示例:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

### 查找交集项

交集返回两个集合中都存在的项的集合。请参见示例

```py
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```

**示例：**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)     # {'o', 'n'}
```

### 检查子集和超集

一个集合可以是另一个集合的子集或超集：

- 子集: _issubset()_
- 超集: _issuperset_

```py
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**示例：**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # 错误，因为它是超集
whole_numbers.issuperset(even_numbers) # 正确

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.issubset(dragon)     # 错误
```

### 检查两个集合之间的差异

它返回两个集合之间的差异。

```py
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

**示例：**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)     # {'p', 'y', 't'}  - 结果是无序的（集合的特性）
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### 查找两个集合之间的对称差异

它返回两个集合之间的对称差异。它意味着它返回一个包含两个集合中所有项的集合，除了同时出现在两个集合中的项，数学上：(A\B) ∪ (B\A)

```py
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# 意思是 (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```

**示例：**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

### 合并集合

如果两个集合没有共同的项或项，我们称它们为不相交集合。我们可以使用 _isdisjoint()_ 方法来检查两个集合是否相交。

```py
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # 错误
```

**示例：**

```py
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # 正确，因为没有共同项

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)  # 错误，有共同项 {'o', 'n'}
```

🌕 你是一颗冉冉升起的明星。你刚刚完成了第 7 天的挑战，你在通往伟大的道路上前进了 7 步。现在为你的大脑和肌肉做一些练习。

## 💻 练习：第 7 天

```py
# 集合
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### 练习：第 1 级

1. 找到集合 it_companies 的长度
2. 向 it_companies 添加'Twitter'
3. 一次性向集合 it_companies 插入多个 IT 公司
4. 从集合 it_companies 中移除一家公司
5. 移除和丢弃之间有什么区别

### 练习：第 2 级

1. 合并 A 和 B
1. 找到 A 和 B 的交集
1. A 是 B 的子集吗
1. A 和 B 是不相交集合吗
1. 将 A 与 B 合并，反之亦然
1. A 和 B 之间的对称差异是什么
1. 完全删除集合

### 练习：第 3 级

1. 将年龄转换为集合并比较列表和集合的长度，哪一个更大？
1. 解释以下数据类型之间的区别：字符串、列表、元组和集合
1. _我是一个老师，我喜欢激励和教导人们。_ 这句句子中用了多少独特的单词？使用 split 方法和集合来获取独特的单词。

🎉 恭喜！ 🎉

[<< 第 6 天](../06_Day_Tuples/06_tuples.md) | [第 8 天 >>](../08_Day_Dictionaries/08_dictionaries.md)

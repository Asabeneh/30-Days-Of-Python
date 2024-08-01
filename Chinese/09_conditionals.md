<div align="center">
  <h1> 30天Python学习：第9天 - 条件语句</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者：
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>第二版：2021 年 7 月</small>
</sub>

</div>

[<< 第 8 天](../08_Day_Dictionaries/08_dictionaries.md) | [第 10 天 >>](../10_Day_Loops/10_loops.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 9 天](#-第9天)
  - [条件语句](#条件语句)
    - [If 条件](#if条件)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [简写](#简写)
    - [嵌套条件](#嵌套条件)
    - [If 条件和逻辑运算符](#if条件和逻辑运算符)
    - [If 和 Or 逻辑运算符](#if和or逻辑运算符)
  - [💻 练习：第 9 天](#-练习第9天)
    - [练习：第一层级](#练习第一层级)

# 📘 第 9 天

## 条件语句

默认情况下，Python 脚本中的语句是从上到下顺序执行的。如果处理逻辑需要，可以通过两种方式来改变顺序：

- 条件执行：如果某个表达式为真，则执行一个或多个语句块
- 重复执行：只要某个表达式为真，则重复执行一个或多个语句块。在本节中，我们将讨论*if*，_else_，*elif*语句。前面章节中学到的比较运算符和逻辑运算符在这里将派上用场。

### If 条件

在 Python 和其他编程语言中，关键字*if*用于检查条件是否为真并执行代码块。请记住冒号后的缩进。

```py
# 语法
if condition:
    如果条件为真，则运行此部分代码
```

**示例：1**

```py
a = 3
if a > 0:
    print('A是一个正数')
# A是一个正数
```

如上例所示，3 大于 0。条件为真，执行代码块。然而，如果条件为假，我们不会看到结果。为了看到假条件的结果，我们应有另一个代码块，即*else*。

### If Else

如果条件为真，则执行第一个代码块，否则执行*else*条件。

```py
# 语法
if condition:
    如果条件为真，则运行此部分代码
else:
    如果条件为假，则运行此部分代码
```

**示例：**

```py
a = 3
if a < 0:
    print('A是一个负数')
else:
    print('A是一个正数')
```

上面的条件为假，因此执行*else*代码块。如果我们的条件超过两个呢？我们可以使用*elif*。

### If Elif Else

在我们的日常生活中，我们每天都在做决策。我们做出决策不仅仅是检查一个或两个条件，而是多个条件。与生活相似，编程中也充满了条件。当我们有多个条件时，可以使用*elif*。

```py
# 语法
if condition:
    代码
elif condition:
    代码
else:
    代码

```

**示例：**

```py
a = 0
if a > 0:
    print('A是一个正数')
elif a < 0:
    print('A是一个负数')
else:
    print('A是零')
```

### 简写

```py
# 语法
代码 if 条件 else 代码
```

**示例：**

```py
a = 3
print('A是正数') if a > 0 else print('A是负数') # 满足第一个条件，将打印 'A是正数'
```

### 嵌套条件

条件可以嵌套

```py
# 语法
if 条件:
    代码
    if 条件:
        代码
```

**示例：**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A是一个正数且为偶数')
    else:
        print('A是一个正数')
elif a == 0:
    print('A是零')
else:
    print('A是一个负数')
```

我们可以使用逻辑运算符*and*来避免编写嵌套条件。

### If 条件和逻辑运算符

```py
# 语法
if 条件 and 条件:
    代码
```

**示例：**

```py
a = 0
if a > 0 and a % 2 == 0:
    print('A是一个正数且为偶数')
elif a > 0 and a % 2 !=  0:
    print('A是一个正数')
elif a == 0:
    print('A是零')
else:
    print('A是一个负数')
```

### If 和 Or 逻辑运算符

```py
# 语法
if 条件 or 条件:
    代码
```

**示例：**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('访问授权！')
else:
    print('访问拒绝！')
```

🌕 你做得很好。永远不要放弃，因为伟大的事情需要时间。你刚刚完成了第 9 天的挑战，你已经在通向伟大的道路上前进了 9 步。现在做一些练习来锻炼你的大脑和肌肉。

## 💻 练习：第 9 天

### 练习：第一层级

1. 使用 input 获取用户输入（例如：“输入你的年龄：”）。如果用户 18 岁或以上，给出反馈：你已经足够大，可以学习驾驶。如果未满 18 岁，则给出需要等待的年数。输出：

   ```sh
   输入你的年龄：30
   你已经足够大，可以学习驾驶。
   输出：
   输入你的年龄：15
   你还需要等待3年才能学习驾驶。
   ```

2. 使用 if…else 比较 my_age 和 your_age 的值。谁更年长（我还是你）？使用 input（“输入你的年龄：”）获取年龄作为输入。您可以使用嵌套条件来打印'年'表示 1 年的年龄差异，'年'表示更大的差异，如果 my_age = your_age，则打印自定义文本。输出：

   ```sh
   输入你的年龄：30
   你比我大5岁。
   ```

3. 使用输入提示从用户处获得两个数字。如果 a 大于 b，返回 a 大于 b，如果 a 小于 b，返回 a 小于 b，否则返回 a 等于 b。输出:

```sh
输入第一个数字：4
输入第二个数字：3
4大于3
```

### 练习：第二层级

1. 编写代码，根据学生的分数给出等级：

   ```sh
   80-100, A
   70-79, B
   60-69, C
   50-59, D
   0-49, F
   ```

2. 检查是否是秋天、冬天、春天或夏天。如果用户输入：
   9 月、10 月或 11 月，是秋天。
   12 月、1 月或 2 月，是冬天。
   3 月、4 月或 5 月，是春天。
   6 月、7 月或 8 月，是夏天。
3. 以下列表包含了一些水果：

   ```sh
   fruits = ['banana', 'orange', 'mango', 'lemon']
   ```

   如果列表中不存在某个水果，则将其添加到列表中并打印修改后的列表。如果水果存在，则打印('该水果已在列表中')。

### 练习：第三层级

1. 这里有一个人员字典。请随意修改它！

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': '芬兰',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '太空街',
        'zipcode': '02210'
    }
}
```

- 检查是否在字典中有 skills 键，如果有则打印 skills 列表中的中间技能。
- 检查是否在字典中有 skills 键，如果有则检查该人是否具备'Python'技能并打印结果。
- 如果一个人的技能只有 JavaScript 和 React，打印('他是前端开发者')，如果一个人的技能有 Node、Python、MongoDB，打印('他是后端开发者')，如果一个人的技能有 React、Node 和 MongoDB，打印('他是全栈开发者')，否则打印'未知头衔' - 为获得更准确的结果，可以嵌套更多条件！
- 如果该人结婚了且居住在芬兰，按以下格式打印信息：

```py
Asabeneh Yetayeh住在芬兰。他已婚。
```

🎉 恭喜！ 🎉

[<< 第 8 天](../08_Day_Dictionaries/08_dictionaries.md) | [第 10 天 >>](../10_Day_Loops/10_loops.md)

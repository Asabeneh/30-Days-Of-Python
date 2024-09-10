<div align="center">
  <h1> 30 天 Python 学习：第 8 天 - 字典</h1>
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

[<< 第 7 天 ](../07_Day_Sets/07_sets.md) | [第 9 天 >>](../09_Day_Conditionals/09_conditionals.md)

![30 天 Python 学习](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 8 天](#-第-8-天)
  - [字典](#字典)
    - [创建字典](#创建字典)
    - [字典长度](#字典长度)
    - [访问字典项](#访问字典项)
    - [向字典添加项](#向字典添加项)
    - [修改字典中的项](#修改字典中的项)
    - [检查字典中的键](#检查字典中的键)
    - [从字典中移除键值对](#从字典中移除键值对)
    - [将字典转换为项目列表](#将字典转换为项目列表)
    - [清空字典](#清空字典)
    - [删除字典](#删除字典)
    - [复制字典](#复制字典)
    - [将字典键转换为列表](#将字典键转换为列表)
    - [将字典值转换为列表](#将字典值转换为列表)
  - [💻 练习：第 8 天](#-练习-第-8-天)

# 📘 第 8 天

## 字典

字典是一种由无序、可修改（可变）的键值对组成的数据类型。

### 创建字典

为了创建字典，我们使用大括号 {} 或内置函数 _dict()_。

```py
# 语法
empty_dict = {}
# 带数据值的字典
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

**示例：**

```py
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
```

上面的字典显示，值可以是任何数据类型：字符串、布尔值、列表、元组、集合或字典。

### 字典长度

它检查字典中的键值对的数量。

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**示例：**

```py
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
print(len(person)) # 7

```

### 访问字典项

我们可以通过参考其键名来访问字典项。

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
```

**示例：**

```py
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # 错误
```

通过键名访问项时，如果键不存在会引发错误。为了避免这个错误，我们首先要检查键是否存在，或者使用 _get_ 方法。get 方法在键不存在时返回 None（这是 NoneType 对象数据类型）。

```py
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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### 向字典添加项

我们可以向字典中添加新的键值对

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

**示例：**

```py
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

### 修改字典中的项目

我们可以修改字典中的项目

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
```

**示例:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
person['first_name'] = 'Eyob'
person['age'] = 252
```

### 检查字典中的键

我们使用 _in_ 运算符来检查字典中是否存在某个键

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### 从字典中删除键值对

- _pop(key)_: 删除具有指定键名的项目
- _popitem()_: 删除最后一个项目
- _del_: 删除具有指定键名的项目

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # 删除 key1 项目
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # 删除最后一项
del dct['key2'] # 删除 key2 项目
```

**示例:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
person.pop('first_name')  # 删除 firstname 项目
person.popitem()          # 删除 address 项目
del person['is_married']  # 删除 is_married 项目
```

### 将字典改变为项目列表

_items()_ 方法将字典变成由元组组成的列表。

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### 清空字典

如果我们不需要字典中的项目，我们可以使用 _clear()_ 方法来清空它们

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### 删除字典

如果我们不再使用字典，我们可以完全删除它

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### 复制字典

我们可以使用 _copy()_ 方法复制一个字典。使用 copy 方法可以避免原始字典被修改。

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### 获取字典的键列表

keys() 方法给我们一个包含所有字典键的列表。

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys) # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### 获取字典的值列表

values 方法给我们一个包含所有字典值的列表。

```py
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values) # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 你很了不起。现在，你已经掌握了字典的强大功能。你已经完成了第 8 天的挑战，离成功又近了一步。现在为你的大脑和肌肉做一些练习。

## 💻 练习：第 8 天

1. 创建一个名为 dog 的空字典
2. 向 dog 字典添加 name、color、breed、legs、age 键
3. 创建一个学生字典，添加 first_name、last_name、gender、age、marital status、skills、country、city 和 address 作为字典的键
4. 获取学生字典的长度
5. 获取 skills 的值并检查数据类型，应该是列表
6. 修改 skills 值，添加一到两个技能
7. 获取字典的键列表
8. 获取字典的值列表
9. 使用 _items()_ 方法将字典变为由元组组成的列表
10. 删除字典中的一项
11. 删除其中一个字典

🎉 恭喜你! 🎉

[<< 第 7 天 ](../07_Day_Sets/07_sets.md) | [第 9 天 >>](../09_Day_Conditionals/09_conditionals.md)

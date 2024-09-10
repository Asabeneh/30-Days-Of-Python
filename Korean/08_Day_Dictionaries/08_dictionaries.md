<div align="center">
  <h1> 30 Days Of Python: Day 8 - Dictionaries</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 7 ](../07_Day_Sets/07_sets.md) | [Day 9 >>](../09_Day_Conditionals/09_conditionals.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 8](#-day-8)
  - [Dictionaries](#dictionaries)
    - [Creating a Dictionary](#creating-a-dictionary)
    - [Dictionary Length](#dictionary-length)
    - [Accessing Dictionary Items](#accessing-dictionary-items)
    - [Adding Items to a Dictionary](#adding-items-to-a-dictionary)
    - [Modifying Items in a Dictionary](#modifying-items-in-a-dictionary)
    - [Checking Keys in a Dictionary](#checking-keys-in-a-dictionary)
    - [Removing Key and Value Pairs from a Dictionary](#removing-key-and-value-pairs-from-a-dictionary)
    - [Changing Dictionary to a List of Items](#changing-dictionary-to-a-list-of-items)
    - [Clearing a Dictionary](#clearing-a-dictionary)
    - [Deleting a Dictionary](#deleting-a-dictionary)
    - [Copy a Dictionary](#copy-a-dictionary)
    - [Getting Dictionary Keys as a List](#getting-dictionary-keys-as-a-list)
    - [Getting Dictionary Values as a List](#getting-dictionary-values-as-a-list)
  - [💻 Exercises: Day 8](#-exercises-day-8)

# 📘 Day 8

## Dictionaries

Dictionary는 순서가 없는 수정(변형) 가능한 쌍(키: 값)의 자료형의 컬렉션입니다.

### Creating a Dictionary

Dictionary를 만들려면 중괄호 {} 또는 *dict()* 내장 함수를 사용합니다.

```py
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

**Example:**

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

상단의 Dictionary는 값이 어떤 자료형일 수도 있다는 것을 보여줍니다:string, boolean, list, tuple, set 또는 dictionary.

### Dictionary Length

dictionary 내 'key: value' 쌍의 개수를 확인합니다.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Example:**

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

### Accessing Dictionary Items

키의 이름을 통해 딕셔너리 아이템에 접근할 수 있습니다.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
```

**Example:**

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
print(person['city'])       # Error
```

존재하지 않는 키의 이름으로 아이템에 접근할 경우 에러가 발생할 수 있습니다. 이 에러를 피하기위해 우리는 우선 키가 존재하는지 확인해야합니다. 또는 _get_ 메서드를 사용할수 있습니다. get 메서드는 키가 존재하지 않을 경우, NoneType object 자료형인 None을 반환합니다.
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

### Adding Items to a Dictionary

딕셔너리에 새로운 키와 값의 쌍을 추가할 수 있습니다.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

**Example:**

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

### Modifying Items in a Dictionary

딕셔너리의 아이템을 수정할 수 있습니다

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
```

**Example:**

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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### Checking Keys in a Dictionary

딕셔너리에 키가 존재하는 지 확인하기 위해  _in_ 연산자를 사용합니다

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Removing Key and Value Pairs from a Dictionary

- _pop(key)_: 특정 키 이름을 가진 아이템을 삭제합니다
- _popitem()_: 마지막 아이템을 삭제합니다
- _del_: 특정 키 이름을 가진 아이템을 삭제합니다

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
```

**Example:**

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
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item
```

### Changing Dictionary to a List of Items

_items()_ 메서드는 딕셔너리를 튜플의 리스트로 변환합니다.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Clearing a Dictionary

딕셔너리 내의 아이템을 원하지 않는다면  _clear()_ 메서드를 사용해 비울 수 있습니다

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Deleting a Dictionary

딕셔너리를 사용하지않는다면 완전히 지울 수 있습니다

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copy a Dictionary

_copy()_ 메서드를 통해 딕셔너리를 복사할 수 있습니다. copy를 사용해 원래 딕셔너리의 변화를 막을 수 있습니다.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Getting Dictionary Keys as a List

_keys()_ 메서드는 하나의 딕셔너리의 모든 키를 리스트로 줍니다.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Getting Dictionary Values as a List

_values_ 메서드는 하나의 딕셔너리의 모든 값을 리스트로 줍니다.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 당신은 정말 놀라워요. 이제, 여러분은 사전의 힘으로 완전히 충전되어 있습니다. 여러분은 이제 막 8일째의 도전을 마쳤고 위대함을 향해 8보 전진했습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 Exercises: Day 8

1. dog라는 이름의 빈 딕셔너리를 생성합니다
2. dog 딕셔너리에 name, color, breed, legs, age 를 추가합니다
3. student 딕셔너리를 생성하고 first_name, last_name, gender, age, marital status, skills, country, city 와 address 를 키로 추가합니다
4. student 딕셔너리의 길이를 얻습니다
5. skills 의 값을 얻고 자료형을 확인합니다, list 여야 합니다
6. 한개나 두개를 추가해 skills의 값을 수정합니다
7. 딕셔너리의 키를 리스트로 얻습니다
8. 딕셔너리의 값을 리스트로 얻습니다
9. _items()_ 메서드를 이용해 튜플의 리스트로 딕셔너리를 바꿉니다
10. 딕셔너리의 아이템중 하나를 삭제합니다
11. 딕셔너리 중 하나를 삭제합니다

🎉 CONGRATULATIONS ! 🎉

[<< Day 7 ](../07_Day_Sets/07_sets.md) | [Day 9 >>](../09_Day_Conditionals/09_conditionals.md)

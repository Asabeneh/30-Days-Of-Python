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

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

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

# 📘 Day 8

## Dictionaries

A dictionary ជាប្រភេទទិន្នន័យដែលគ្មានលំដាប់, អាចកែក្រែបាន។ ទិន្នន័យសរសេរជា (key: value)

### Creating a Dictionary

ដើម្បីបង្កើត dictionary យើងប្រើខ្នៀប, {} ឬ ប្រើអនុគមន៍ *dict()*.

```py
# syntax
empty_dict = {}
# Dictionary មានទិន្នន័យ
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

Dictionary ខាងលើបង្ហាញថាតម្លៃអាចជាប្រភេទទិន្នន័យណាក៍បាន:string, boolean, list, tuple, set ឬ dictionary.

### Dictionary Length

ប្រវែង Dictionary
វាត្រួតពិនិត្យចំនួន 'key: value' គូក្នុង dictionary.

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

We can access Dictionary items by referring to its key name.
យើងអាចទៅយកវត្ថុក្នុង Dictionary ដោយហៅឈ្មោះ Key របស់វា។

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

ការចូលទៅកាន់វត្ថុដោយឈ្មោះ key បានបង្ហាញ error ប្រសិនបើ key នោះមិនមាន។ ដើម្បីចៀសវាង error នេះយើងត្រូវពិនិត្យមើលថាតើ key មានឬអត់ យើងអាចប្រើវិធីសាស្រ្ត _get_ ។ វិធី get អោយវិញ None ដែលជា ប្រភេទទិន្នន័យ NoneType ប្រសិនបើ key មិនមាន។

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

យើងអាចបន្ថែម key និង value pair ថ្មីទៅក្នុង Dictionary

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

យើងអាចកែប្រែវត្ថុនៅក្នុង dictionary

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

យើងប្រើវិធីសាស្រ្ត _in_ ដើម្បីពិនិត្យមើលថាតើ key មាននៅក្នុង dictionary ឬអត់

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Removing Key and Value Pairs from a Dictionary

- _pop(key)_: ដកវត្ថុចេញដែលមានឈ្មោះ key ដែលបានកំណត់:
- _popitem()_: លុបវត្ថុចុងក្រោយ
- _del_: ដកវត្ថុចេញដែលមានឈ្មោះ key ដែលបានកំណត់:

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
person.pop('first_name')        # លុប firstname
person.popitem()                # លុបវត្ថុ
del person['is_married']        # លុប is_married
```

### Changing Dictionary to a List of Items

The _items()_ method changes dictionary to a list of tuples.

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Clearing a Dictionary

If we don't want the items in a dictionary we can clear them using _clear()_ method
ប្រសិនបើយើងមិនចង់បានវត្ថុនៅក្នុង dictionary យើងអាចលុបវាដោយប្រើវិធីសាស្ត្រ _clear()_

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Deleting a Dictionary

If we do not use the dictionary we can delete it completely
បើយើងមិនប្រើ dictionary យើងអាចលុបវាទាំងស្រុង

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copy a Dictionary

យើងអាចចម្លង dictionary ដោយប្រើវិធីសាស្រ្ត _copy()_ ។ ការប្រើ Copy យើងអាចចៀសវាងការប្រែប្រួលនៃ Dictionary ដើម។

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Getting Dictionary Keys as a List

The _keys()_ method gives us all the keys of a a dictionary as a list.
វិធីសាស្ត្រ _keys()_ ផ្តល់ឱ្យយើងនូវ key ទៅជា list។

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Getting Dictionary Values as a List

វិធីសាស្ត្រ _values_ ផ្តល់ឱ្យយើងនូវតម្លៃទាំងអស់ទៅជា list។

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

[<< Day 7 ](../07_Day_Sets/07_sets.md) | [Day 9 >>](../09_Day_Conditionals/09_conditionals.md)

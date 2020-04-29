
<div align="center">
  <h1> 30 Days Of Python: Day 7 - Dictionary</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> First Edition: Nov 22 - Dec 22, 2019</small>
  </sub>
</div>
</div>

[<< Day 7 ](../07_Day/07_set.md) | [Day 9 >>](../09_Day/09_conditional.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 8](#%f0%9f%93%98-day-8)
  - [Dictionary](#dictionary)
    - [Creating a dictionary](#creating-a-dictionary)
    - [Dictionary Length](#dictionary-length)
    - [Accessing a dictionary items](#accessing-a-dictionary-items)
    - [Adding Item to a dictionary](#adding-item-to-a-dictionary)
    - [Modifying Item in a dictionary](#modifying-item-in-a-dictionary)
    - [Checking a key in a dictionary](#checking-a-key-in-a-dictionary)
    - [Removing key items from dictionary](#removing-key-items-from-dictionary)
    - [Changing dictionary to list items](#changing-dictionary-to-list-items)
    - [Clearing dictionary list items](#clearing-dictionary-list-items)
    - [Deleting dictionary](#deleting-dictionary)
    - [Copy a dictionary](#copy-a-dictionary)
    - [Getting dictionary keys as list](#getting-dictionary-keys-as-list)
    - [Getting dictionary values as list](#getting-dictionary-values-as-list)
  - [💻 Exercises: Day 8](#%f0%9f%92%bb-exercises-day-8)
# 📘 Day 8
## Dictionary
A dictionary is a collection of unordered, modifiable(mutable) key value paired data type.
### Creating a dictionary
To create a dictionary we use a curly bracket, {}.
```py
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
```
**Example:**
```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
```

The dictionary above shows that a value could be any different data type:string, boolean, list, tuple, set or a dictionary.

### Dictionary Length
It checks the number of key value pairs in the dictionary.
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
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

### Accessing a dictionary items
We can access a dictionary items by referring to its key name.
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
print(dct['key1']) # item1
print(dct['key4']) # item4
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
print(person['skills'])     # ['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['city'])       # Error
```
Accessing an item by key name raises an error if the key does not exist. To avoid this error first we have to check if a key exist or we can use the _get_ method.The get method returns None, which is a NoneType object data type.
object if the data
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

### Adding Item to a dictionary

We can add new key and value pair to a dictionary

```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
dct['key5'] = 'item5'
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

### Modifying Item in a dictionary
We can add modify item in a dictionary
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
dct['key1'] = 'item-one'
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
person['age']
```

### Checking a key in a dictionary
We use the _in_ operator to check if a key exist in a dictionary
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Removing key items from dictionary

- _pop(key)_: removes the item with the specified key name:
- _popitem()_: remove the last time
- _del_: removes the item with the specified key name

```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
dct.pop('key1') # the first key pair removed
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
dct.popitem() # remove the last item
del dct['key2'] # remove key 2 item
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
person.pop('first_name')        # Remove the firstname item
person.popitem()                # Remove the lastname item
del person['is_married']        # Remove the is_married item
```

### Changing dictionary to list items
The *items()* method change a dictionary to list of tuples.
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
print(dct.items()) # dict_items([('key1', 'item1'), ('key2', 'item2'), ('key3', 'item3'), ('key4', 'item4')])
```
### Clearing dictionary list items
If we don't want the items in a dictionary we can clear them using _clear()_ methods
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
print(dct.clear()) # {}
```
### Deleting dictionary
If we do not use the dictionary we can delete it completely
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
del dct
```
### Copy a dictionary
We copy a dictionary using a _copy()_ method. Using copy we can avoid mutation of the original dictionary.
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
dct_copy = dct.copy() # {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
```
### Getting dictionary keys as list
The _keys()_ method gives us all the keys of a a dictionary as a list.
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```
### Getting dictionary values as list
The _values_ method gives us all the values of a a dictionary as a list.
```py
# syntax
dct = {'key1':'item1', 'key2':'item2', 'key3':'item3', 'key4':'item4'}
values = dct.values()
print(values)     # dict_values(['item1', 'item2', 'item3', 'item4'])
```
## 💻 Exercises: Day 8
1. Create a an empty dictionary called dog
2. Add name, color, breed, legs, age to the dog, dictionary
3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as key for the dictionary
4. Get the length of student dictionary
5. Get the value of skills and check the data type, it should be list
6. Modify the skills value by adding one or two skills
7. Get the dictionary keys as list
8. Get the dictionary values as list
9. Change the dictionary to a list of tuples using *items() method
10. Delete one of the item in the dictionary
11. Delete the dictionary completely

🎉 CONGRATULATIONS ! 🎉

[<< Day 7 ](../07_Day/07_set.md) | [Day 9 >>](../09_Day/09_conditional.md)
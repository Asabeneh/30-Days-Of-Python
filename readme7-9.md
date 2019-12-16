![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

🧳 [Part 1: Day 1 - 3](https://github.com/Asabeneh/30-Days-Of-Python)  
🧳 [Part 2: Day 4 - 6](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)  
🧳 [Part 3: Day 7 - 9](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)  
🧳 [Part 4: Day 10 - 12](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)  
🧳 [Part 5: Day 13 - 15](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)  
🧳 [Part 6: Day 16 - 18](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)  
🧳 [Part 7: Day 19 - 21](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)  
🧳 [Part 8: Day 22 - 24](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme22-24.md)  
🧳 [Part 9: Day 25 - 27](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme25-27.md)  
🧳 [Part 10: Day 28 - 30](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme28-30.md) 

---
- [📘 Day 7](#%f0%9f%93%98-day-7)
  - [Set](#set)
    - [Creating a set](#creating-a-set)
    - [Getting set length](#getting-set-length)
    - [Accessing Items in set](#accessing-items-in-set)
    - [Checking an item](#checking-an-item)
    - [Adding items to a list](#adding-items-to-a-list)
    - [Removing item from a list](#removing-item-from-a-list)
    - [Clearing item in a set](#clearing-item-in-a-set)
    - [Deleting a set](#deleting-a-set)
    - [Converting list to set](#converting-list-to-set)
    - [Joining sets](#joining-sets)
    - [Finding intersection items](#finding-intersection-items)
    - [Checking subset and super set](#checking-subset-and-super-set)
    - [Checking difference between two sets](#checking-difference-between-two-sets)
    - [Finding Symmetric difference between two sets](#finding-symmetric-difference-between-two-sets)
    - [Joining set](#joining-set)
  - [💻 Exercises: Day 7](#%f0%9f%92%bb-exercises-day-7)
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
- [📘 Day 9](#%f0%9f%93%98-day-9)
  - [Conditionals](#conditionals)
    - [If condition](#if-condition)
    - [If Else](#if-else)
    - [If elif else](#if-elif-else)
    - [Short Hand](#short-hand)
    - [Nested condition](#nested-condition)
    - [If condition and and logical operator](#if-condition-and-and-logical-operator)
    - [If and or logical operator](#if-and-or-logical-operator)
  - [💻 Exercises: Day 9](#%f0%9f%92%bb-exercises-day-9)

# 📘 Day 7
## Set
Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of set can be applied also in python. Set is a collection of unordered and unindexed distinct elements. In python set uses to store unique items, and it is possible to find the *union*, *intersection*, *difference*, *symmetric difference*, *subset*, *super set* and *disjoint set* among sets.
### Creating a set
We use curly bracket, {}  to create a set.
* Creating an empty set
```py
# syntax
st = {} 
# or
st = set()
```
* Creating a set with initial items
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```
**Example:**

```py
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```
### Getting set length
We use **len()**  method to find the length of a set.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(set)
```
**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```
### Accessing Items in set
We use loops to access items. We will see this in loop section
### Checking an item
To check if an item exist in a list use use *in*.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
'item3' in st
```
**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
'mango' in fruits
```
### Adding items to a list
Once a list is created we can not change an item but we can add additional items.
* Add one item using *add()*
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```
**Example:**
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```
* Add multiple items or using *update()*
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```
**Example:**
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits.update(vegetables)
```
### Removing item from a list
We can remove an item from a list using *remove()* method. If the item is not found *remove()* method raise an errors, so it is good to check if the item exist or not. However, *discard() method doesn't raise an error.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2")
```
**Example:**
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()
```
### Clearing item in a set
If we want to clear or empty the set we use *clear* method.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```
**Example:**
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
```
### Deleting a set
If we want to delete the set itself we use *del* operator.
```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del set
```

**Example:**
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```
### Converting list to set
We can convert list to set and set to list back. Converting list to set removes duplicates and only unique items will be reserved.
```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'}
```

**Example:**
```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### Joining sets
We can join two using the *union()* or *update() method.
* Union
This method returns a new set

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```
**Example:**
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'}
fruits.union(vegetables) # {'lemon', 'Carrot', 'Tomato', 'banana', 'mango', 'orange', 'Cabbage', 'Potato', 'Onion'}
```
* Update
This method insert an other set

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)
```
**Example:**
```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'Carrot', 'Tomato', 'banana', 'mango', 'orange', 'Cabbage', 'Potato', 'Onion'}
```
### Finding intersection items
Intersection returns a set of items which are in both the sets. See the example

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```
**Example:**
```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```

### Checking subset and super set 
A set can be a subset or super set of other sets:
* Subset: *issubset()*
* Super set: *issuperset*

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```
**Example:**
```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### Checking difference between two sets 
It return the difference between the two sets.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # {'item1', 'item4'} => st1\st2
```
**Example:**
```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### Finding Symmetric difference between two sets 
It return the the symmetric difference between the two sets, it means that it return a set that contains all items from both sets, except items that are present in both set, mathematically: (A\B) U (B\A)

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it mean (A\B)U(B)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```
**Example:**
```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(even_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd'}
```
### Joining set
If two set do not have common item or items we call it disjoint set. We can check if two sets are joint or disjoint using *isdisjoint()* method.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```
**Example:**
```py
even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.disjoint(dragon)  # False, there is common items {'o', 'n'}
```

## 💻 Exercises: Day 7
```py
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```
1. Find the length of the set, it_companies
2. Add 'Twitter' to it companies
3. Insert multiple it companies at once to the set, it_companies
4. Remove one of the companies from the set, it_companies
5. What is the difference between remove and discard
6. Join A and B
7. Find A intersection B
8. Is A subset of B
9. Are A and B disjoint sets
10. Join A with B and B with A
11. What is the symmetric difference between A and B
12. Delete the sets completely
13. Convert the ages to set and compare the length of the list and the set, which is larger ? 
14. Explain the difference among the following data types: string, list, tuple and set
15. *I am a teacher and I love to inspire and teach people.* How many unique words have been used in the sentence.

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


# 📘 Day 9
## Conditionals
By default , statements in python script executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:
* Conditional execution: a block of one or more statements will be executed if a certain expression is true
* Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover *if*, *else* , *elif* statements. The comparison and logical operator we learned in the previous sections will be useful here. 

### If condition
In python and other programming languages the key word *if* use to check if a condition is true and to execute the block code. Remember the indentation after the colon.
```py
# syntax
if condition:
    this part of code run for truthy condition
```
**Example:**
```py
a = 3
if a > 0:
    print('A is a positive number')
# a is a positive number
```
As you can see in the above condition, 3 is greater than 0 and it is a positive number. The condition was true and the block code was executed. However, if the condition is false, we do not see a result. In order to see the result of the falsy condition, we should have another block, which is going to be *else*.

### If Else
If condition is true the first block will be executed, if not the else condition will run. 
```py
# syntax
if condition:
    this part of code run for truthy condition
else:
     this part of code run for false condition
```
**Example:**
```py
a = 3
if a < 0:
    print('A is a positive number')
else:
    print('A is a negative number')
```
The above condition is false, therefore the else block was executed. How about if our condition is more than two, we will use *elif*.
### If elif else
On our daily life, we make decision on daily basis. We make decision not by checking  one or two conditions instead multiple conditions. As similar to life, programming is also full conditions. We use *elif* when we have multiple conditions.
```py
# syntax
if condition:
    code
elif condition:
    code
else:
    code

```
**Example:**
```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```
### Short Hand

```py
# syntax
code if condition else code
```
**Example:**
```py
a = 3
print('A is positive') if a > 0 else print('A is negative')
```

### Nested condition
Condition can be nested
```py
# syntax
if condition:
    code
    if condition:
    code
```
**Example:**
```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is positive even integer')
    else:
        print('A positive number')
elif a == 0:
    print('Zero')
else:
    print('A negative number')

```
We can avoid writing nested condition by using logical operator, *and*.

### If condition and and logical operator
```py
# syntax
if condition and condition:
    code
```
**Example:**
```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is even positive integer')
elif a > 0 and a % 2 !== 0:
     print('A is positive integer') 
elif a == 0:
    print('Zero')
else:
    print('A negative number')
```
### If and or logical operator
```py
# syntax
if condition or condition:
    code
```
**Example:**
```py
a = 0
if a > 0 or  % 2 == 0:
        print('A is positive integer')
elif a == 0:
    print('Zero')
else:
    print('A negative number')
```

## 💻 Exercises: Day 9
1. Get user input using input(“Enter your age:”). If user is 18 or older , give feedback:You are old enough to drive but if not 18 give feedback to wait for the years he supposed to wait for. Output:
    ```sh
    Enter your age: 30
    You are old enough to drive.
    Output:
    Enter your age:15
    You are left with 3 years to drive.
    ```
1. Compare the values of my_age and your_age using if … else. Based on the comparison print who is older (me or you). Use input(“Enter your age:”) to get the age as input. Output:
    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```
1. Get two numbers from user using, input prompt. If a is greater than b return a is greater than b,if a is less b return a lesson b,  else a is equal to b. Output:
    ```sh
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
    ```
1. Write a code which give grade to students according to theirs scores:
    ```sh
    80-100, A
    70-89, B
    60-69, C
    50-59, D
    0 -49, F
    ```
1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
September, October or November, the season is Autumn.
December, January or February, the season is Winter.
March, April or May, the season is Spring
June, July or August, the season is Summer
1. The following list contains some fruits:
    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```
    If a fruit doesn't exist in the list add the fruit in the list and print the modified list but if the fruit exists print('A fruit already exist in the list')
1. Here we have a person dictionary. 
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
* Check if the person dictionary has skills,  if it has skills key check print out the middle skill in the skills list.
* Check if the person dictionary has skills,  if it has skills key check if the person has 'Python' skill and print the skill.
* If a person skills has only JavaScript and React,  print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print ('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') 
* If the person is married and if he lives in Finland, print the following: 
    ```py
    Asabeneh Yetayeh lives in Finland. He is married.
    ```
[<< Part 2 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md) | [Part 4 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)
***
<div align="center">
  <h1> 30 Days Of Python: Day 7 - Set</h1>
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

[<< Day 6](../06_Day_Tuples/06_tuple.md) | [Day 8 >>](../08_Day/08_dictionary.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

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

# 📘 Day 7

## Set

Let me take you back to your elementary or high school Mathematics lesson. The Mathematics definition of set can be applied also in python. Set is a collection of unordered and unindexed distinct elements. In python set uses to store unique items, and it is possible to find the _union_, _intersection_, _difference_, _symmetric difference_, _subset_, _super set_ and _disjoint set_ among sets.

### Creating a set

We use curly bracket, {} to create a set.

- Creating an empty set

```py
# syntax
st = {}
# or
st = set()
```

- Creating a set with initial items

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

We use **len()** method to find the length of a set.

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

To check if an item exist in a list use use _in_.

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

- Add one item using _add()_

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

- Add multiple items or using _update()_

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

We can remove an item from a list using _remove()_ method. If the item is not found _remove()_ method raise an errors, so it is good to check if the item exist or not. However, \*discard() method doesn't raise an error.

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

If we want to clear or empty the set we use _clear_ method.

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

If we want to delete the set itself we use _del_ operator.

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

We can join two using the _union()_ or \*update() method.

- Union
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

- Update
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

- Subset: _issubset()_
- Super set: _issuperset_

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

If two set do not have common item or items we call it disjoint set. We can check if two sets are joint or disjoint using _isdisjoint()_ method.

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
15. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence.

🎉 CONGRATULATIONS ! 🎉

[<< Day 6](../06_Day_Tuples/06_tuple.md) | [Day 8 >>](../08_Day/08_dictionary.md)

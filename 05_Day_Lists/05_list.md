<div align="center">
  <h1> 30 Days Of Python: Day 5 - List</h1>
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

[<< Day 5](../04_Day_Strings/04_string.md) | [Day 6 >>](../06_Day_Tuples/06_tuple.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Day 5](#day-5)
  - [Lists](#lists)
    - [How to create a list](#how-to-create-a-list)
    - [Accessing list items using positive indexing](#accessing-list-items-using-positive-indexing)
    - [Accessing list items using negative indexing](#accessing-list-items-using-negative-indexing)
    - [Unpacking list items](#unpacking-list-items)
    - [Slicing items from list](#slicing-items-from-list)
    - [Modifying list](#modifying-list)
    - [Check items in a list](#check-items-in-a-list)
    - [Adding item in a list](#adding-item-in-a-list)
    - [Inserting item in to a list](#inserting-item-in-to-a-list)
    - [Removing item from list](#removing-item-from-list)
    - [Removing item using pop](#removing-item-using-pop)
    - [Removing item using del](#removing-item-using-del)
    - [Clearing list items](#clearing-list-items)
    - [Copying a list](#copying-a-list)
    - [Joining lists](#joining-lists)
    - [Counting Items in a list](#counting-items-in-a-list)
    - [Finding index of an item](#finding-index-of-an-item)
    - [Reversing a list](#reversing-a-list)
    - [Sorting list items](#sorting-list-items)
  - [💻 Exercises: Day 5](#%f0%9f%92%bb-exercises-day-5)

# Day 5

## Lists

The are four collection data types in python :

- List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
- Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
- Set: is a collection which is unordered and unindexed. No duplicate members.
- Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items or items

### How to create a list

In python we can create list in two ways:

- Using list builtin function

```py
# syntax
lst = list()
```

```py
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

- Using square brackets, []

```py
# syntax
lst = []
```

```py
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

List with initial values. We use _len()_ to find the length of a list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
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
output
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

- List can have items of different data types

```py
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
```

### Accessing list items using positive indexing

We access each item in a list using their index. A list index start from 0. The picture below show clearly where the index starts
![List index](../images/list_index.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

### Accessing list items using negative indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.

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

### Unpacking list items

```py
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item1
print(third_item)     # item2
print(rest)           # ['item4', 'item5']

```

```py
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

### Slicing items from list

- Positive Indexing: We can specify a range of positive indexes by specifying the starting and the ending, the return value will be a new list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]
```

- Negative Indexing: We can specify a range of negative indexes by specifying the starting and the ending, the return value will be a new list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]
```

### Modifying list

List is a mutable or modifiable ordered collection of items or items. Lets modify the fruit list.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'Avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits)
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### Check items in a list

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### Adding item in a list

To add item to the end of an existing list we use the method

```py
# syntax
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

### Inserting item in to a list

Use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right.

```py
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon']
print(fruits)
```

### Removing item from list

The remove method remove a specified item from a list

```py
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']
```

### Removing item using pop

The pop() method removes the specified index, (or the last item if index is not specified):

```py
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.remove(0)
print(fruits)       # ['orange', 'mango']
```

### Removing item using del

The del keyword removes the specified index and it can be also use to delete the list completely

```py
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```

### Clearing list items

The clear() method empties the list:

```py
# syntax
lst = ['item1', 'item2']
lst.clear()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

### Copying a list

It is possible to copy a list by reassigning to a new variable in the following way list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list2. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way avoid the above problem is using _copy()_.

```py
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### Joining lists

There are several ways to join, or concatenate, two or more lists in Python.

- Plus Operator (+)

```py
# syntax
list3 = list1 +list2
```

```py
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

```

```py
# output
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- Joining using extend() method

```py
# syntax
lst1 = ['item1', 'item2']
lst2 = ['item3', 'item4','item5']
list1.extend(list2)
```

```py
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

```

```py
Numbers: [0, 1, 2, 3, 4, 5, 6]
Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### Counting Items in a list

The count() method returns the number of times an item appears in a list:

```py
# syntax
lst = ['item1', 'item2']
lst.count(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### Finding index of an item

The count() method returns the index of an item in the list:

```py
# syntax
lst = ['item1', 'item2']
lst.index(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```

### Reversing a list

The reverse() method reverse the order of a list.

```py
# syntax
lst = ['item1', 'item2']
lst.reverse()

```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())
```

```py
['lemon', 'mango', 'orange', 'banana']
[24, 25, 24, 26, 25, 24, 19, 22]
```

### Sorting list items

To sort list we can use *sort() method or *sorted()\* builtin function. The sort() method reorder the list items in ascending order and modify the original list. If a reverse is equal to true it arrange in descending order.

- sort():

  ```py
  # syntax
  lst = ['item1', 'item2']
  lst.sort()                # ascending
  lst.sort(reverse=True)    # descending
  ```

  **Example:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.sort()
  print(fruits)
  fruits.sort(reverse=True)
  print(fruits)
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.sort()
  print(ages)
  ages.sort(reverse=True)
  print(ages)
  ```

  ```sh
  ['banana', 'lemon', 'mango', 'orange']
  ['orange', 'mango', 'lemon', 'banana']
  [19, 22, 24, 24, 24, 25, 25, 26]
  [26, 25, 25, 24, 24, 24, 22, 19]
  ```

  sorted(): returns the ordered list without modifying the original
  **Example:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits)
  print(fruits)     # ['banana', 'lemon', 'mango', 'orange']
  # Reverse order
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
  ```

## 💻 Exercises: Day 5

1. Declare an empty list
2. Declare a list with more than 5 number of items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types,put your(name, age, height, marital status, address)
6. Declare a list variable name it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using _print()_
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print modify any of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies item to uppercase
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list.
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies item
25. Destroy the IT companies list
26. Join the following lists:
    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
27. After joining the lists in question 26. Copy the joined list and assigned it to a variable full_stack. Then insert, Python and SQL after Redux.
28. The following is a list of 10 students ages:

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- Sort the list and find the min and max age
- Add the min age and the max age
- Find the median age(one middle item or two middle items divided by two)
- Find the average age(all items divided by number of items)
- Find the range of the ages(max minus min)
- Compare the value of (min - average) and (max - average), use _abs()_ method

29. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
30. Divide the countries list into two equal lists if it is even if not one more country for the first half.
31. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

🎉 CONGRATULATIONS ! 🎉

[<< Day 5](../04_Day_Strings/04_string.md) | [Day 6 >>](../06_Day_Tuples/06_tuple.md)

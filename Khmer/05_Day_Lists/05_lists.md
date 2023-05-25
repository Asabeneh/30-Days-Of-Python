<div align="center">
  <h1> 30 Days Of Python: Day 5 - Lists</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July - 2021</small>
</sub>

</div>

[<< Day 4](../04_Day_Strings/04_strings.md) | [Day 6 >>](../06_Day_Tuples/06_tuples.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Day 5](#day-5)
  - [Lists](#lists)
    - [How to Create a List](#how-to-create-a-list)
    - [Accessing List Items Using Positive Indexing](#accessing-list-items-using-positive-indexing)
    - [Accessing List Items Using Negative Indexing](#accessing-list-items-using-negative-indexing)
    - [Unpacking List Items](#unpacking-list-items)
    - [Slicing Items from a List](#slicing-items-from-a-list)
    - [Modifying Lists](#modifying-lists)
    - [Checking Items in a List](#checking-items-in-a-list)
    - [Adding Items to a List](#adding-items-to-a-list)
    - [Inserting Items into a List](#inserting-items-into-a-list)
    - [Removing Items from a List](#removing-items-from-a-list)
    - [Removing Items Using Pop](#removing-items-using-pop)
    - [Removing Items Using Del](#removing-items-using-del)
    - [Clearing List Items](#clearing-list-items)
    - [Copying a List](#copying-a-list)
    - [Joining Lists](#joining-lists)
    - [Counting Items in a List](#counting-items-in-a-list)
    - [Finding Index of an Item](#finding-index-of-an-item)
    - [Reversing a List](#reversing-a-list)
    - [Sorting List Items](#sorting-list-items)

# Day 5

## Lists

មានទម្រង់ ៤ ប្រភេទសម្រាប់ការប្រមូលទិន្នន័យនៅក្នុង Python

- List: គឺជាការប្រមូលផ្តុំដែលត្រូវបានបញ្ជា និងអាចផ្លាស់ប្តូរ ។ អនុញ្ញាតឱ្យមានសមាជិកដដែល ឬ ទិន្នន័យដូចគ្នា
- Tuple: គឺជាការប្រមូលផ្តុំដែលត្រូវបានបញ្ជា និងមិនអាចផ្លាស់ប្តូរ ឬមិនអាចកែប្រែ ។ អនុញ្ញាតឱ្យមានសមាជិកដដែល ឬ ទិន្នន័យដូចគ្នា
- Set: គឺជាប្រមូលដែលមិនមានលំដាប់ និងមិនអាចកែប្រែបានប៉ុន្តែយើងអាចបន្ថែមវត្ថុថ្មីទៅក្នុង set ។ មិនអនុញ្ញាតឱ្យមានសមាជិក ឬ ទិន្នន័យដូចគ្នា
- Dictionary: គឺជាការប្រមូលផ្តុំដែលមិនត្រូវបានរៀបចំ, អាចផ្លាស់ប្តូរ និងត្រូវបានកំណត់។ មិនអនុញ្ញាតឱ្យមានសមាជិក ឬ ទិន្នន័យដូចគ្នា

បញ្ជីគឺជាការប្រមូលផ្តុំនៃប្រភេទទិន្នន័យ ផ្សេងគ្នាដែលត្រូវបានបញ្ជា និងអាចកែប្រែ។ បញ្ជីមួយអាចគ្មានឬអាចមានប្រភេទទិន្នន័យ ផ្សេងៗ

### How to create a List

ក្នុង Python យើងអាចបង្កើតបញ្ជីបាន 2 វិធី:

- ប្រើ list built-in function

```py
# syntax
lst = list()
```

```py
empty_list = list() # នេះជា list គ្មានបញ្ជី ឬ ទិន្នន័យ 

print(len(empty_list)) # 0
```

- ប្រើ square brackets, []

```py
# syntax
lst = []
```

```py
empty_list = [] # នេះជា list គ្មានបញ្ជី ឬ ទិន្នន័យ 
print(len(empty_list)) # 0
```

Lists ដែលមានទិន្នន័យដំបូង. យើងប្រើ _len()_ ដើម្បីរកទំហំនៃ list

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# បង្ហាញ list និងប្រវែងរបស់វា។
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

- Lists អាចមានលក្ខខណ្ឌនៃប្រភេទទិន្នន័យផ្សេងៗ

```py
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list មានប្រភេទទិន្នន័យផ្សេងៗគ្នា
```

### Accessing List Items Using Positive Indexing

យើងអាចចូលទៅកាន់ទិន្នន័យនីមួយៗ ក្នុងបញ្ជី ដោយប្រើ index។ បញ្ជី index ចាប់ផ្តើមពី 0។ រូបភាពខាងក្រោមបង្ហាញយ៉ាងច្បាស់ថា តើ index ចាប់ផ្តើមនៅឯណា។
![List index](../images/list_index.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # យើងកំពុងចូលទៅកាន់វត្ថុទីមួយដោយប្រើ index របស់វា
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# index ចុងក្រោយ
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

### Accessing List Items Using Negative Indexing

Indexing អវិជ្ជមាន មានន័យថា ចាប់ផ្តើមពីចុង, -1 សំដៅទៅលើចំណុចចុងក្រោយ, -2 សំដៅទៅលើចំណុចមុនចុងក្រោយ
។

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

### Unpacking List Items

```py
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```

```py
# ឧទាហរណ៍ទីមួយ
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# ឧទាហរណ៍ទីពីរអំពីបញ្ចេញ list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# ឧទាហរណ៍ទីបីអំពីបញ្ចេញ list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

### Slicing Items from a List

- Positive Indexing: យើងអាចកំណត់អតិបរមានៃវិភាគវិជ្ជមានដោយកំណត់ការចាប់ផ្តើម, បញ្ចប់និងជំហាន, តម្លៃត្រឡប់នឹងជា list ថ្មី។ (តម្លៃដើមសម្រាប់ start = 0, end = len(lst) - 1 (វត្ថុចុងក្រោយ), step = 1)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # វាត្រលប់ fruits មកវិញទាំងអស់
# នេះនឹងផ្តល់លទ្ធផលដូចគ្នានឹងលទ្ធផលខាងលើ
all_fruits = fruits[0:] # បើយើងមិនកំណត់កន្លែងដែលត្រូវឈប់ វានឹងយកទាំងអស់
orange_and_mango = fruits[1:3] # វាមិនរាប់បញ្ចូល index ទីមួយទេ
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # នៅទីនេះយើងបានប្រើ argument ទី៣, ជំហាន. វានឹងយកចំណែកទីពីរទាំងអស់ - ['banana', 'mango']
```

- Negative Indexing: យើងអាចកំណត់អតិបរមានៃកម្រិតអវិជ្ជមានដោយកំណត់ការចាប់ផ្តើម, បញ្ចប់និងជំហាន, តម្លៃត្រឡប់នឹងជា list ថ្មី។

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # វាត្រលប់ fruits មកវិញទាំងអស់
orange_and_mango = fruits[-3:-1] # វាមិនរួមបញ្ចូល index ចុងក្រោយ, ['orange', 'mango']
orange_mango_lemon = fruits[-3:] # នេះ នឹងផ្តល់ចាប់ពី -3 ដល់ ចុង,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # ជំហានអវិជ្ជមាននឹងយក list តាមលំដាប់បញ្ច្រាស, ['lemon', 'mango', 'orange', 'banana']
```

### Modifying Lists

List គឺជាការផ្លាស់ប្តូរ ឬការកែប្រែនៃការបញ្ជាបញ្ជីនៃឯកសារ។ យើងត្រូវផ្លាស់ប្តូរ fruit list។

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

### Checking Items in a List

ការត្រួតពិនិត្យអាត្រាមួយ ប្រសិនបើវាជាសមាជិកនៃ list ដោយប្រើ *in* operator ។ សូមមើលឧទាហរណ៍ខាង ក្រោម។

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### Adding Items to a List

ដើម្បីបន្ថែមវត្ថុទៅចុងនៃបញ្ជីដែលមានយើងប្រើវិធីសាស្ត្រ *append()*.

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

### Inserting Items into a List

យើងអាចប្រើ *insert()* វិធីសាស្ត្រដើម្បីបញ្ចូលវត្ថុតែមួយនៅក្នុង list ដែលកំណត់. សូមបញ្ជាក់ថា វត្ថុ ផ្សេងទៀតត្រូវបានផ្លាស់ប្តូរទៅខាងស្តាំ។ *insert()* វិធីសាស្រ្តយកពីរ arguments: index និងវត្ថុដើម្បីបញ្ចូល។

```py
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

### Removing Items from a List

វិធី remove លុបវត្ថុដែលបានកំណត់ពីបញ្ជី

```py
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - វិធីសាស្ត្រនេះលុបចោលការកើតឡើងដំបូងនៃវត្ថុនៅក្នុងបញ្ជី
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

### Removing Items Using Pop

*pop()* វិធីសាស្ត្រលុបបំបាត់បញ្ជីដែលបានកំណត់ (ឬបញ្ជីចុងក្រោយ ប្រសិនបើបញ្ជីមិនត្រូវបានកំណត់):

```py
# syntax
lst = ['item1', 'item2']
lst.pop()       # វត្ថុចុងក្រោយ
lst.pop(index)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### Removing Items Using Del

*del* keyword លុបបញ្ជីដែលបានកំណត់ ហើយវាក៏អាចត្រូវបានប្រើដើម្បីលុបវត្ថុនៅក្នុងប្រវែង index ។ វាក៏អាចលុប list ទាំងស្រុង

```py
# syntax
lst = ['item1', 'item2']
del lst[index] # តែមួយមុខ
del lst        # លុប list ទាំងស្រុង
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # នេះលុបរវាង index ដែលបានផ្តល់, ដូច្នេះវាមិនលុបបំបាត់ index 3 ទេ!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # នេះអាចផ្តល់: NameError: name 'fruits' is not defined
```

### Clearing List Items

*clear()* វិធីសាស្ត្រទទេ list:

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

### Copying a List

វាអាចធ្វើជាលិខិតចម្លង list ដោយការកំណត់វាទៅលើចលនាត្រូវថ្មីដោយវិធីដូចខាងក្រោម: list2 = list1. ឥឡូវ, list2 គឺជាការណែនាំនៃ list1, ការផ្លាស់ប្តូរណាមួយដែលយើងធ្វើនៅក្នុង list2 នឹងកែប្រែ original, list1. ប៉ុន្តែមានករណីជាច្រើនដែលយើងមិនចូលចិត្តកែប្រែ original ទេយើងចូលចិត្តមានកំណែ ផ្សេងៗ។ វិធីមួយដើម្បីចៀសវាងបញ្ហាខាងលើគឺប្រើ _copy()_.

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

### Joining Lists

មានវិធីជាច្រើនដើម្បីចូលរួម ឬ រួមបញ្ចូល lists ពីរ ឬ ច្រើនទៀតនៅក្នុង Python ។

- Plus Operator (+)

```py
# syntax
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

- បង ប្រើប្រាស់ extend() method
  The *extend()* method អនុញ្ញាតឱ្យភ្ជាប់ list ក្នុង list។ សូមមើលឧទាហរណ៍ខាងក្រោម។

```py
# syntax
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

### Counting Items in a List

The *count()* method ឱ្យចំនួនដងដែលវត្ថុមួយបង្ហាញនៅក្នុងបញ្ជី:

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

### Finding Index of an Item

The *index()* method ឱ្យ index នៃវត្ថុក្នុង list:

```py
# syntax
lst = ['item1', 'item2']
lst.index(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, ករណីដំបូង
```

### Reversing a List

The *reverse()* method កែប្រែលំដាប់នៃ list។

```py
# syntax
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

### Sorting List Items

ដើម្បីរចនា list យើងអាចប្រើ _sort()_ method or _sorted()_ built-in functions. The _sort()_ method ផ្លាស់ប្តូរលំដាប់វត្ថុក្នុង list តាមលំដាប់ឡើង និងកែប្រែ list ដើម។ ប្រសិនបើអាគុយម៉ង់នៃ _sort()_ method បញ្ច្រាសគឺស្មើនឹងពិត វានឹងរៀបចំបញ្ជីតាមលំដាប់ចុះ។

- sort(): វិធីសាស្រ្តនេះកែប្រែ list ដើម

  ```py
  # syntax
  lst = ['item1', 'item2']
  lst.sort()                # លំដាប់ឡើង
  lst.sort(reverse=True)    # លំដាប់ចុះ
  ```

  **Example:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.sort()
  print(fruits)             # តម្រៀបតាមលំដាប់អក្ខរក្រម, ['banana', 'lemon', 'mango', 'orange']
  fruits.sort(reverse=True)
  print(fruits) # ['orange', 'mango', 'lemon', 'banana']
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.sort()
  print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]
 
  ages.sort(reverse=True)
  print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
  ```

  sorted(): ឱ្យ list ដើលមានលំដាប់ដោយមិនផ្លាស់ប្តូរ list ដើម
  **Example:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
  # លំដាប់បញ្ច្រាស
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
  ```

[<< Day 4](../04_Day_Strings/04_strings.md) | [Day 6 >>](../06_Day_Tuples/06_tuples.md)

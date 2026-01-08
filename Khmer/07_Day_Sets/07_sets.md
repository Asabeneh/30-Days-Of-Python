<div align="center">
  <h1> 30 Days Of Python: Day 7 - Sets</h1>
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

[<< Day 6](../06_Day_Tuples/06_tuples.md) | [Day 8 >>](../08_Day_Dictionaries/08_dictionaries.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 7](#-day-7)
  - [Sets](#sets)
    - [Creating a Set](#creating-a-set)
    - [Getting Set's Length](#getting-sets-length)
    - [Accessing Items in a Set](#accessing-items-in-a-set)
    - [Checking an Item](#checking-an-item)
    - [Adding Items to a Set](#adding-items-to-a-set)
    - [Removing Items from a Set](#removing-items-from-a-set)
    - [Clearing Items in a Set](#clearing-items-in-a-set)
    - [Deleting a Set](#deleting-a-set)
    - [Converting List to Set](#converting-list-to-set)
    - [Joining Sets](#joining-sets)
    - [Finding Intersection Items](#finding-intersection-items)
    - [Checking Subset and Super Set](#checking-subset-and-super-set)
    - [Checking the Difference Between Two Sets](#checking-the-difference-between-two-sets)
    - [Finding Symmetric Difference Between Two Sets](#finding-symmetric-difference-between-two-sets)
    - [Joining Sets](#joining-sets)

# 📘 Day 7

## Sets

set គឺជាការប្រមូលផ្តុំនៃវតដែលគ្មានលំដាប់និងគ្មាន index។ ក្នុង Python, set ត្រូវបានប្រើដើម្បីរក្សាទុវត្ថុដែលមានតែមួយរបស់វា, ហើយវាអាចរកបាន _union_, _intersection_, _difference_, _symmetric difference_, _subset_, _super set_ and _disjoint set_ ក្នុងចំណោម sets.

### Creating a Set

យើងប្រើ {} ដើម្បីបង្កើត set ឬ _set()_ built-in function.

- បង្កើត set ទទេរ

```py
# syntax
st = {}
# or
st = set()
```

- បង្កើត set មានវត្ថុស្រាប់

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

**Example:**

```py
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### Getting Set's Length

យើងប្រើវិធីសាស្រ្ត **len()** ដើម្បីរកចំនួនវត្ថុនៅក្នុង set។

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

### Accessing Items in a Set

ការចូលប្រើវត្ថុរបស់ set

យើងប្រើ loop ដើម្បីចូលប្រើវត្ថុនៅក្នុង set។

### Checking an Item

យើងអាចត្រួតពិនិត្យថាតើវត្ថយមានឬគ្មាននៅក្នុង set ដោយប្រើ _in_ ។

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### Adding Items to a Set

បន្ថែមវត្ថុទៅក្នុង set ។
នៅពេលដែល set មួយត្រូវបានបង្កើតយើងមិនអាចផ្លាស់ប្តូរអ្វីៗ ប៉ុន្តែយើងអាចដាក់វត្ថុចូលបន្ថែមបាន។

- ដាក់វត្ថុចូលបន្ថែមមួយប្រើ _add()_

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

- ដាក់វត្ថុចូលបន្ថែមច្រើនប្រើ _update()_

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### Removing Items from a Set

យើងអាចលុបវត្ថុមួយចេញពីកំរិតដោយប្រើវិធីសាស្រ្ត _remove()_ ។ ប្រសិនបើវត្ថុមិនត្រូវបានរកឃើញ _remove()_ វិធីសាស្ត្រនឹងបង្កើត error, ដូច្នេះ យើងគួរពិនិត្យមើលថាតើវត្ថុនោះមាននៅក្នុង set ដែលអត់។ ទោះយ៉ាងណាក៏ដោយ, វិធីសាស្រ្ត _discard()_ មិនបញ្ចេញ error ទេ។

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

វិធីសាស្រ្ត pop() លុបវត្ថុណាមួយដោយចៃដន្យពី set ហើយវានឹងត្រឡប់មកវិញវត្ថុដែលលុបចោល។

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

```

ប្រសិនបើយើងចាប់អារម្មណ៍នឹងវត្ថុដែលត្រូវបានដកចេញ។

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
```

### Clearing Items in a Set

If we want to clear or empty the set we use _clear_ method.
ប្រសិនបើយើងចង់បំបាត់វត្ថុទាំងអស់ក្នុង sets យើងប្រើវិធី _clear_ ។

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### Deleting a Set

ប្រសិនបើយើងចង់លុប set យើងប្រើវិធី _del_ ។

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### Converting List to Set

យើងអាចបម្លែង list ទៅជា set និង set ទៅជា list ។ ការបម្លែង list ទៅជា set នឹងត្រូវលុបចោលវត្ថុដែលពីរឬច្រើនដង ហើយនឹងមានតែវត្ថុដែលមានតែមួយ។

```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

**Example:**

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### Joining Sets

យើងបញ្ចូលគ្នា set ពីរឬច្រើនទៀតដោយប្រើវិធី _union()_ or _update()_

- Union
  វិធីសាស្ត្រនេះត្រឡប់មកនូវ set ថ្មី

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

- Update
  វិធីសាស្ត្រនេះបញ្ចូល set មួយក្នុង set មួយទៀត។

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

### Finding Intersection Items

ការប្រសព្វ (Intersection) នឹងត្រឡប់មកវិញ នូវវត្ថុដែលស្ថិតនៅក្នុង set ទាំងពីរ។ សូមមើលឧទាហរណ៍

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```

**Example:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```

### Checking Subset and Super Set

set អាចជា subset ឬ superset នៃ set ផ្សេងទៀត។

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
whole_numbers.issubset(even_numbers) # False, ដោយសារវាជា super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### Checking the Difference Between Two Sets

ត្រឡប់មកវិញនូវភាពខុសគ្នារវាង set ពីរ។

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

**Example:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### Finding Symmetric Difference Between Two Sets

វាត្រឡប់មកវិញ ភាពខុសគ្នាស៊ីមេទ្រី (Symmetric Difference) រវាងពីរsets។ វាមានន័យថា វាវិលត្រឡប់មកនូវ set ដែលមានវត្ថុទាំងអស់ពី set ទាំងពីរ, លើកលែងតែវត្ថុដែលមាននៅក្នុង set ទាំងពីរ, តាមគណិតវិទ្យា: (A\B) ∪ (B\A)

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```

**Example:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

### Joining Sets

ប្រសិនបើ set ពីរគ្មានវត្ថុរួម, យើងហៅវាថា sets ដែលមិនរួមគ្នា. យើងអាចត្រួតពិនិត្យថា តើ set ពីរត្រូវបានរួមគ្នាឬមិនរួមគ្នាដោយប្រើវិធីសាស្ត្រ _isdisjoint()_ ។

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
even_numbers.isdisjoint(odd_numbers) # True, ដោយសារគ្មានវត្ថុរួមគ្នា

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, ដោយសារមានវត្ថុរួមគ្នា {'o', 'n'}
```

[<< Day 6](../06_Day_Tuples/06_tuples.md) | [Day 8 >>](../08_Day_Dictionaries/08_dictionaries.md)

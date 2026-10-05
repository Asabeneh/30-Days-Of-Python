<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 5 — لسٹس</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../05_Day_Lists/05_lists.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 4](./04_strings.md) | [فہرست](./readme.md) | [اگلا دن: 6](./06_tuples.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [دن 5](#day-5-section-1)
  - [لسٹس](#day-5-section-2)
    - [لسٹ کیسے بنائیں](#day-5-section-3)
    - [مثبت انڈیکس سے عناصر تک رسائی](#day-5-section-4)
    - [منفی انڈیکس سے عناصر تک رسائی](#day-5-section-5)
    - [لسٹ کے عناصر الگ متغیرات میں رکھنا](#day-5-section-6)
    - [لسٹ کے حصے نکالنا](#day-5-section-7)
    - [لسٹ تبدیل کرنا](#day-5-section-8)
    - [لسٹ میں عنصر کی موجودگی جانچنا](#day-5-section-9)
    - [لسٹ کے آخر میں عنصر شامل کرنا](#day-5-section-10)
    - [مخصوص مقام پر عنصر شامل کرنا](#day-5-section-11)
    - [لسٹ سے عنصر ہٹانا](#day-5-section-12)
    - [pop سے عنصر ہٹانا](#day-5-section-13)
    - [del سے عناصر ہٹانا](#day-5-section-14)
    - [لسٹ خالی کرنا](#day-5-section-15)
    - [لسٹ کی نقل بنانا](#day-5-section-16)
    - [لسٹس جوڑنا](#day-5-section-17)
    - [کسی عنصر کی تعداد گننا](#day-5-section-18)
    - [عنصر کا انڈیکس معلوم کرنا](#day-5-section-19)
    - [لسٹ الٹنا](#day-5-section-20)
    - [لسٹ کے عناصر ترتیب دینا](#day-5-section-21)
  - [💻 مشقیں — دن 5](#day-5-section-22)
    - [مشقیں: درجہ 1](#day-5-section-23)
    - [مشقیں: درجہ 2](#day-5-section-24)

<a id="day-5-section-1"></a>

# دن 5

<a id="day-5-section-2"></a>

## لسٹس

پائتھن میں مجموعوں کی چار اہم اقسام ہیں:

- *List*: ترتیب وار اور قابلِ تبدیلی؛ ایک قدر کئی بار آ سکتی ہے۔
- *Tuple*: ترتیب وار اور ناقابلِ تبدیلی؛ دہرائی گئی قدریں ممکن ہیں۔
- *Set*: غیر مرتب، بغیر انڈیکس اور منفرد عناصر کا مجموعہ۔ عناصر شامل یا حذف کر سکتے ہیں، مگر کسی انڈیکس پر عنصر تبدیل نہیں کر سکتے۔
- *Dictionary*: کلید اور قدر کے جوڑوں کا قابلِ تبدیلی مجموعہ؛ کلیدیں منفرد ہوتی ہیں۔ اصل متن اسے غیر مرتب کہتا ہے، مگر پائتھن 3.7 سے اندراج کی ترتیب برقرار رہتی ہے۔

لسٹ ترتیب وار اور قابلِ تبدیلی (*mutable*) ہوتی ہے۔ یہ خالی بھی ہو سکتی ہے یا مختلف اقسام کے عناصر رکھ سکتی ہے۔

<a id="day-5-section-3"></a>

### لسٹ کیسے بنائیں

لسٹ بنانے کے دو طریقے ہیں:

- بلٹ اِن فنکشن `list()` سے۔

<div dir="ltr">

```py
# syntax
lst = list()
```

</div>

<div dir="ltr">

```py
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

</div>

- مربع قوسین `[]` سے۔

<div dir="ltr">

```py
# syntax
lst = []
```

</div>

<div dir="ltr">

```py
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

</div>

ابتدائی قدروں والی لسٹس کی مثالیں؛ لمبائی کے لیے `len()` استعمال کریں۔

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
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

</div>

<div dir="ltr">

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

</div>

- ایک لسٹ میں مختلف اقسام کے عناصر رکھے جا سکتے ہیں۔

<div dir="ltr">

```py
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
```

</div>

<a id="day-5-section-4"></a>

### مثبت انڈیکس سے عناصر تک رسائی

ہر عنصر تک اس کے انڈیکس سے پہنچتے ہیں۔ پہلا انڈیکس `0` ہے۔ تصویر میں ترتیب دیکھیں۔

![لسٹ کے انڈیکس](../images/list_index.png)

<div dir="ltr">

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

</div>

<a id="day-5-section-5"></a>

### منفی انڈیکس سے عناصر تک رسائی

منفی انڈیکس آخر سے گنتا ہے۔ `-1` آخری اور `-2` آخری سے پہلے عنصر کا انڈیکس ہے۔

![لسٹ کے منفی انڈیکس](../images/list_negative_indexing.png)

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

</div>

<a id="day-5-section-6"></a>

### لسٹ کے عناصر الگ متغیرات میں رکھنا

<div dir="ltr">

```py
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```

</div>

<div dir="ltr">

```py
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
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

</div>

<a id="day-5-section-7"></a>

### لسٹ کے حصے نکالنا

- مثبت انڈیکس: آغاز، اختتام اور قدم (`step`) دے کر نئی لسٹ حاصل کریں۔ عام آگے جانے والے سلائس میں آغاز `0`، اختتام `len(lst)` اور قدم `1` ہوتا ہے۔ اختتامی انڈیکس شامل نہیں ہوتا۔

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
```

</div>

- منفی انڈیکس: منفی آغاز اور اختتام کے ساتھ بھی سلائس بنا سکتے ہیں؛ نتیجہ نئی لسٹ ہوتا ہے۔

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
```

</div>

<a id="day-5-section-8"></a>

### لسٹ تبدیل کرنا

لسٹ کے عناصر بدلے جا سکتے ہیں۔ پھلوں کی لسٹ میں تبدیلی دیکھیں۔

<div dir="ltr">

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

</div>

<a id="day-5-section-9"></a>

### لسٹ میں عنصر کی موجودگی جانچنا

`in` سے جانچیں کہ عنصر لسٹ میں موجود ہے یا نہیں۔

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

</div>

<a id="day-5-section-10"></a>

### لسٹ کے آخر میں عنصر شامل کرنا

موجودہ لسٹ کے آخر میں عنصر شامل کرنے کے لیے `append()` استعمال ہوتا ہے۔

<div dir="ltr">

```py
# syntax
lst = list()
lst.append(item)
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

</div>

<a id="day-5-section-11"></a>

### مخصوص مقام پر عنصر شامل کرنا

`insert()` کسی انڈیکس پر ایک عنصر شامل کرتا ہے اور بعد کے عناصر آگے سرک جاتے ہیں۔ اس کے دو آرگیومنٹ ہیں: انڈیکس اور نیا عنصر۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

</div>

<a id="day-5-section-12"></a>

### لسٹ سے عنصر ہٹانا

`remove()` دی گئی قدر کا پہلا ملنے والا عنصر ہٹاتا ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

</div>

<a id="day-5-section-13"></a>

### pop سے عنصر ہٹانا

`pop()` مخصوص انڈیکس کا عنصر ہٹا کر واپس دیتا ہے۔ انڈیکس نہ دیں تو آخری عنصر ہٹتا ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

</div>

<a id="day-5-section-14"></a>

### del سے عناصر ہٹانا

`del` سے مخصوص انڈیکس، انڈیکس کی حد یا لسٹ کا پورا متغیر حذف کیا جا سکتا ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```

</div>

<a id="day-5-section-15"></a>

### لسٹ خالی کرنا

`clear()` تمام عناصر ہٹا کر لسٹ خالی کر دیتا ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.clear()
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

</div>

<a id="day-5-section-16"></a>

### لسٹ کی نقل بنانا

`list2 = list1` سے الگ نقل نہیں بنتی؛ دونوں نام ایک ہی لسٹ کا حوالہ ہوتے ہیں۔ اس لیے `list2` میں تبدیلی `list1` میں بھی نظر آتی ہے۔ الگ سطحی نقل بنانے کے لیے `copy()` استعمال کریں۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

</div>

<a id="day-5-section-17"></a>

### لسٹس جوڑنا

دو یا زیادہ لسٹس ملانے کے مختلف طریقے ہیں:

- جمع کا آپریٹر `+`۔

<div dir="ltr">

```py
# syntax
list3 = list1 + list2
```

</div>

<div dir="ltr">

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

</div>

- `extend()` دوسری لسٹ کے عناصر پہلی لسٹ کے آخر میں شامل کرتا ہے۔

<div dir="ltr">

```py
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
```

</div>

<div dir="ltr">

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

</div>

<a id="day-5-section-18"></a>

### کسی عنصر کی تعداد گننا

`count()` بتاتا ہے کہ ایک قدر لسٹ میں کتنی بار موجود ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.count(item)
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

</div>

<a id="day-5-section-19"></a>

### عنصر کا انڈیکس معلوم کرنا

`index()` عنصر کا پہلا ملنے والا انڈیکس دیتا ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.index(item)
```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```

</div>

<a id="day-5-section-20"></a>

### لسٹ الٹنا

`reverse()` لسٹ کے عناصر کی ترتیب الٹ دیتا ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.reverse()

```

</div>

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

</div>

<a id="day-5-section-21"></a>

### لسٹ کے عناصر ترتیب دینا

ترتیب دینے کے لیے `sort()` یا بلٹ اِن `sorted()` استعمال کریں۔ `sort()` اصل لسٹ کو بڑھتی ترتیب میں بدلتا ہے۔ `reverse=True` سے گھٹتی ترتیب بنتی ہے۔

- `sort()` اصل لسٹ بدلتا ہے۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

ages.sort(reverse=True)
print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
```

</div>

`sorted()` اصل لسٹ بدلے بغیر نئی مرتب لسٹ دیتا ہے۔

**مثال:**

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
```

</div>

🌕 آپ نے پانچویں دن کا چیلنج مکمل کر لیا! اب مشق کریں۔

<a id="day-5-section-22"></a>

## 💻 مشقیں — دن 5

<a id="day-5-section-23"></a>

### مشقیں: درجہ 1

1. خالی لسٹ بنائیں۔
2. پانچ سے زیادہ عناصر کی لسٹ بنائیں۔
3. اس کی لمبائی معلوم کریں۔
4. پہلا، درمیانی اور آخری عنصر حاصل کریں۔
5. `mixed_data_types` میں اپنا نام، عمر، قد، ازدواجی حیثیت اور پتہ رکھیں۔
6. `it_companies` میں Facebook، Google، Microsoft، Apple، IBM، Oracle اور Amazon رکھیں۔
7. `print()` سے لسٹ دکھائیں۔
8. کمپنیوں کی تعداد دکھائیں۔
9. پہلی، درمیانی اور آخری کمپنی دکھائیں۔
10. ایک کمپنی بدل کر لسٹ دکھائیں۔
11. ایک آئی ٹی کمپنی شامل کریں۔
12. درمیان میں ایک کمپنی داخل کریں۔
13. IBM کے علاوہ کسی کمپنی کا نام بڑے حروف میں بدلیں۔
14. کمپنیوں کو `'#; '` سے جوڑیں۔
15. کسی مخصوص کمپنی کی موجودگی جانچیں۔
16. `sort()` سے ترتیب دیں۔
17. `reverse()` سے مرتب لسٹ الٹ کر گھٹتی ترتیب بنائیں۔
18. پہلی تین کمپنیاں سلائس سے نکالیں۔
19. آخری تین کمپنیاں نکالیں۔
20. درمیان کی کمپنی یا کمپنیاں نکالیں۔
21. پہلی کمپنی ہٹائیں۔
22. درمیان کی کمپنی یا کمپنیاں ہٹائیں۔
23. آخری کمپنی ہٹائیں۔
24. تمام کمپنیاں ہٹائیں۔
25. کمپنیوں والی لسٹ کا متغیر حذف کریں۔
26. یہ لسٹس جوڑیں:

<div dir="ltr">

```py
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
```

</div>

27. سوال 26 کی جوڑی ہوئی لسٹ کی نقل `full_stack` میں رکھیں۔ `Redux` کے بعد `Python` اور `SQL` داخل کریں۔

<a id="day-5-section-24"></a>

### مشقیں: درجہ 2

1. دس طلبہ کی عمروں کی لسٹ:

<div dir="ltr">

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

</div>

- ترتیب دیں اور کم سے کم اور زیادہ سے زیادہ عمر معلوم کریں۔
- کم سے کم اور زیادہ سے زیادہ عمر دوبارہ لسٹ میں شامل کریں۔
- میڈین معلوم کریں: درمیان کا عنصر، یا دو درمیانی عناصر کا اوسط۔
- اوسط عمر نکالیں: تمام عمروں کا مجموعہ تقسیم تعداد۔
- حد (*range*) نکالیں: زیادہ سے زیادہ منفی کم سے کم۔
- `abs()` سے `(min - average)` اور `(max - average)` کی مطلق قدروں کا موازنہ کریں۔

2. [ملکوں کی لسٹ](../data/countries.py) میں درمیان کا ملک یا ممالک تلاش کریں۔
3. ملکوں کی لسٹ کو دو حصوں میں بانٹیں۔ تعداد جفت ہو تو برابر، ورنہ پہلے حصے میں ایک ملک زیادہ ہو۔
4. `['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']` کے پہلے تین ممالک الگ متغیرات میں اور باقی `scandic` ممالک کے طور پر رکھیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 4](./04_strings.md) | [فہرست](./readme.md) | [اگلا دن: 6](./06_tuples.md)

</div>

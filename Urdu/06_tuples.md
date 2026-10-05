<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 6 — ٹپلز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../06_Day_Tuples/06_tuples.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 5](./05_lists.md) | [فہرست](./readme.md) | [اگلا دن: 7](./07_sets.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [دن 6](#day-6-section-1)
  - [ٹپلز](#day-6-section-2)
    - [ٹپل بنانا](#day-6-section-3)
    - [ٹپل کی لمبائی](#day-6-section-4)
    - [ٹپل کے عناصر تک رسائی](#day-6-section-5)
    - [ٹپل کے حصے نکالنا](#day-6-section-6)
    - [ٹپل کو لسٹ میں بدلنا](#day-6-section-7)
    - [ٹپل میں عنصر کی موجودگی جانچنا](#day-6-section-8)
    - [ٹپل جوڑنا](#day-6-section-9)
    - [ٹپل حذف کرنا](#day-6-section-10)
  - [💻 مشقیں — دن 6](#day-6-section-11)
    - [مشقیں: درجہ 1](#day-6-section-12)
    - [مشقیں: درجہ 2](#day-6-section-13)

<a id="day-6-section-1"></a>

# دن 6

<a id="day-6-section-2"></a>

## ٹپلز

ٹپل مختلف اقسام کی قدروں کا ترتیب وار اور ناقابلِ تبدیلی (*immutable*) مجموعہ ہے۔ اسے عموماً گول قوسین `()` میں لکھتے ہیں۔ بننے کے بعد اس کے عناصر تبدیل، شامل یا حذف نہیں کر سکتے؛ اس میں لسٹ کے `append()`، `insert()` اور `remove()` جیسے میتھڈ نہیں ہوتے۔ ٹپل سے متعلق اہم عمل:

- `tuple()`: خالی ٹپل بنانا۔
- `count()`: کسی عنصر کی تعداد گننا۔
- `index()`: کسی عنصر کا انڈیکس معلوم کرنا۔
- `+`: دو یا زیادہ ٹپل جوڑ کر نیا ٹپل بنانا۔

<a id="day-6-section-3"></a>

### ٹپل بنانا

- خالی ٹپل:

<div dir="ltr">

```py
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
```

</div>

- ابتدائی قدروں والا ٹپل:

<div dir="ltr">

```py
# syntax
tpl = ('item1', 'item2','item3')
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
```

</div>

<a id="day-6-section-4"></a>

### ٹپل کی لمبائی

لمبائی کے لیے `len()` استعمال کریں۔

<div dir="ltr">

```py
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

</div>

<a id="day-6-section-5"></a>

### ٹپل کے عناصر تک رسائی

- مثبت انڈیکس: لسٹ کی طرح ٹپل کے عناصر تک مثبت یا منفی انڈیکس سے پہنچ سکتے ہیں۔

![ٹپل کے عناصر تک رسائی](../images/tuples_index.png)

<div dir="ltr">

```py
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[last_index]
```

</div>

- منفی انڈیکس: `-1` آخری، `-2` آخری سے پہلے اور ٹپل کی لمبائی کا منفی پہلے عنصر کا انڈیکس ہے۔

![ٹپل کے منفی انڈیکس](../images/tuple_negative_indexing.png)

<div dir="ltr">

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
```

</div>

<a id="day-6-section-6"></a>

### ٹپل کے حصے نکالنا

آغاز اور اختتام کے انڈیکس دے کر ذیلی ٹپل حاصل کریں۔ نتیجہ منتخب عناصر کا نیا ٹپل ہوتا ہے؛ اختتامی انڈیکس شامل نہیں ہوتا۔

- مثبت انڈیکس کی حد:

<div dir="ltr">

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
```

</div>

- منفی انڈیکس کی حد:

<div dir="ltr">

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
```

</div>

<a id="day-6-section-7"></a>

### ٹپل کو لسٹ میں بدلنا

ٹپل کو لسٹ اور لسٹ کو ٹپل میں بدل سکتے ہیں۔ ٹپل ناقابلِ تبدیلی ہے؛ عناصر بدلنے ہوں تو اسے پہلے لسٹ میں تبدیل کریں۔

<div dir="ltr">

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

</div>

<a id="day-6-section-8"></a>

### ٹپل میں عنصر کی موجودگی جانچنا

`in` سے موجودگی جانچیں؛ نتیجہ بولین ہوتا ہے۔

<div dir="ltr">

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

</div>

<a id="day-6-section-9"></a>

### ٹپل جوڑنا

`+` سے دو یا زیادہ ٹپل جوڑ سکتے ہیں۔

<div dir="ltr">

```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

</div>

<a id="day-6-section-10"></a>

### ٹپل حذف کرنا

ٹپل سے ایک عنصر ہٹانا ممکن نہیں، مگر `del` سے ٹپل کا متغیر حذف کیا جا سکتا ہے۔

<div dir="ltr">

```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

```

</div>

<div dir="ltr">

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

</div>

🌕 آپ نے چھٹے دن کا چیلنج مکمل کر لیا! اب مشق کریں۔

<a id="day-6-section-11"></a>

## 💻 مشقیں — دن 6

<a id="day-6-section-12"></a>

### مشقیں: درجہ 1

1. خالی ٹپل بنائیں۔
2. بہنوں اور بھائیوں کے ناموں کے الگ ٹپل بنائیں؛ فرضی نام بھی لے سکتے ہیں۔
3. دونوں جوڑ کر `siblings` میں رکھیں۔
4. بہن بھائیوں کی تعداد معلوم کریں۔
5. `siblings` کے ساتھ والد اور والدہ کے نام ملا کر نیا ٹپل `family_members` بنائیں۔

<a id="day-6-section-13"></a>

### مشقیں: درجہ 2

1. `family_members` سے بہن بھائیوں اور والدین کو الگ متغیرات میں رکھیں۔
2. پھلوں، سبزیوں اور حیوانی غذاؤں کے الگ ٹپل بنا کر `food_stuff_tp` میں جوڑیں۔
3. اسے لسٹ `food_stuff_lt` میں بدلیں۔
4. ٹپل یا لسٹ سے درمیانی عنصر یا عناصر نکالیں۔
5. `food_stuff_lt` سے پہلے تین اور آخری تین عناصر نکالیں۔
6. `food_stuff_tp` حذف کریں۔
7. نیچے دیے گئے ٹپل میں جانچیں:
   - کیا `'Estonia'` نورڈک ممالک میں شامل ہے؟
   - کیا `'Iceland'` نورڈک ممالک میں شامل ہے؟

<div dir="ltr">

```py
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
```

</div>

---

[پچھلا دن: 5](./05_lists.md) | [فہرست](./readme.md) | [اگلا دن: 7](./07_sets.md)

</div>

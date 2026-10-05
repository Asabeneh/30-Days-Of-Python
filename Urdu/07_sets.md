<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 7 — سیٹس</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../07_Day_Sets/07_sets.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 6](./06_tuples.md) | [فہرست](./readme.md) | [اگلا دن: 8](./08_dictionaries.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 7](#day-7-section-1)
  - [سیٹس](#day-7-section-2)
    - [سیٹ بنانا](#day-7-section-3)
    - [سیٹ کی لمبائی معلوم کرنا](#day-7-section-4)
    - [سیٹ کے عناصر تک رسائی](#day-7-section-5)
    - [عنصر کی موجودگی جانچنا](#day-7-section-6)
    - [سیٹ میں عناصر شامل کرنا](#day-7-section-7)
    - [سیٹ سے عناصر ہٹانا](#day-7-section-8)
    - [سیٹ خالی کرنا](#day-7-section-9)
    - [سیٹ حذف کرنا](#day-7-section-10)
    - [لسٹ کو سیٹ میں بدلنا](#day-7-section-11)
    - [سیٹس جوڑنا](#day-7-section-12)
    - [مشترک عناصر معلوم کرنا](#day-7-section-13)
    - [ذیلی اور بالائی مجموعہ جانچنا](#day-7-section-14)
    - [دو سیٹس کا فرق معلوم کرنا](#day-7-section-15)
    - [متناظر فرق معلوم کرنا](#day-7-section-16)
    - [غیر مشترک سیٹس جانچنا](#day-7-section-17)
  - [💻 مشقیں — دن 7](#day-7-section-18)
    - [مشقیں: درجہ 1](#day-7-section-19)
    - [مشقیں: درجہ 2](#day-7-section-20)
    - [مشقیں: درجہ 3](#day-7-section-21)

<a id="day-7-section-1"></a>

# 📘 دن 7

<a id="day-7-section-2"></a>

## سیٹس

سیٹ عناصر کا مجموعہ ہے، بالکل اس تصور کی طرح جو ریاضی میں پڑھا جاتا ہے۔ اس کے عناصر منفرد، غیر مرتب اور بغیر انڈیکس ہوتے ہیں۔ پائتھن میں سیٹس پر اتحاد (*union*)، اشتراک (*intersection*)، فرق (*difference*)، متناظر فرق (*symmetric difference*)، ذیلی مجموعہ (*subset*)، بالائی مجموعہ (*superset*) اور غیر مشترک ہونے کی جانچ جیسے عمل کیے جا سکتے ہیں۔

<a id="day-7-section-3"></a>

### سیٹ بنانا

خالی سیٹ `set()` سے بنتا ہے۔ خالی گھنگریالی قوسین `{}` ڈکشنری بناتی ہیں۔

- خالی سیٹ:

<div dir="ltr">

```py
# syntax
st = set()
```

</div>

- ابتدائی عناصر والا سیٹ:

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

</div>

**مثال:**

<div dir="ltr">

```py
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

</div>

<a id="day-7-section-4"></a>

### سیٹ کی لمبائی معلوم کرنا

`len()` سے عناصر کی تعداد معلوم کریں۔

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

</div>

<a id="day-7-section-5"></a>

### سیٹ کے عناصر تک رسائی

عناصر تک رسائی کے لیے لوپ استعمال کرتے ہیں؛ اس کی تفصیل لوپس کے حصے میں آئے گی۔

<a id="day-7-section-6"></a>

### عنصر کی موجودگی جانچنا

`in` سے جانچیں کہ عنصر سیٹ میں موجود ہے یا نہیں۔

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

</div>

<a id="day-7-section-7"></a>

### سیٹ میں عناصر شامل کرنا

سیٹ میں کسی انڈیکس پر قدر تبدیل نہیں کر سکتے، مگر نئے عناصر شامل کر سکتے ہیں۔

- ایک عنصر کے لیے `add()`۔

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

</div>

- کئی عناصر کے لیے `update()`۔ اسے لسٹ یا کوئی دوسرا قابلِ تکرار مجموعہ دیا جا سکتا ہے۔

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

</div>

<a id="day-7-section-8"></a>

### سیٹ سے عناصر ہٹانا

`remove()` کسی عنصر کو ہٹاتا ہے۔ عنصر موجود نہ ہو تو خرابی آتی ہے، اس لیے پہلے موجودگی جانچ سکتے ہیں۔ `discard()` کو عنصر نہ ملے تو خرابی نہیں آتی۔

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

</div>

`pop()` سیٹ سے ایک غیر متعین عنصر ہٹا کر واپس دیتا ہے؛ اسے بے ترتیب نمونہ چننے کا طریقہ نہ سمجھیں۔

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

```

</div>

ہٹایا گیا عنصر محفوظ کرنا ہو تو:

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
```

</div>

<a id="day-7-section-9"></a>

### سیٹ خالی کرنا

تمام عناصر ہٹانے کے لیے `clear()` استعمال کریں۔

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

</div>

<a id="day-7-section-10"></a>

### سیٹ حذف کرنا

سیٹ کا متغیر حذف کرنے کے لیے `del` استعمال کریں۔

<div dir="ltr">

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

</div>

<a id="day-7-section-11"></a>

### لسٹ کو سیٹ میں بدلنا

لسٹ کو سیٹ اور سیٹ کو لسٹ بنایا جا سکتا ہے۔ لسٹ کو سیٹ میں بدلنے سے دہرائی گئی قدریں نکل جاتی ہیں اور صرف منفرد عناصر رہتے ہیں۔

<div dir="ltr">

```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

</div>

<a id="day-7-section-12"></a>

### سیٹس جوڑنا

`union()`، `update()` یا `|` سے دو سیٹس جوڑ سکتے ہیں۔

- `union()` نیا سیٹ دیتا ہے۔

<div dir="ltr">

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# or using this : print(fruits | vegetables)
```

</div>

- `update()` دوسرے سیٹ کے عناصر موجودہ سیٹ میں شامل کرتا ہے۔

<div dir="ltr">

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

</div>

**مثال:**

<div dir="ltr">

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

</div>

<a id="day-7-section-13"></a>

### مشترک عناصر معلوم کرنا

`intersection()` یا `&` ان عناصر کا سیٹ دیتا ہے جو دونوں میں موجود ہوں۔

<div dir="ltr">

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# or using thia : st1 & st2
```

</div>

**مثال:**

<div dir="ltr">

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon
```

</div>

<a id="day-7-section-14"></a>

### ذیلی اور بالائی مجموعہ جانچنا

ایک سیٹ دوسرے کا ذیلی یا بالائی مجموعہ ہو سکتا ہے:

- ذیلی مجموعہ: `issubset()`۔
- بالائی مجموعہ: `issuperset()`۔

<div dir="ltr">

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

</div>

**مثال:**

<div dir="ltr">

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

</div>

<a id="day-7-section-15"></a>

### دو سیٹس کا فرق معلوم کرنا

`difference()` یا `-` پہلے سیٹ کے وہ عناصر دیتا ہے جو دوسرے میں نہیں ہیں۔

<div dir="ltr">

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1
```

</div>

**مثال:**

<div dir="ltr">

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python
```

</div>

<a id="day-7-section-16"></a>

### متناظر فرق معلوم کرنا

متناظر فرق میں دونوں سیٹس کے وہ عناصر آتے ہیں جو صرف ایک میں ہوں؛ مشترک عناصر شامل نہیں ہوتے۔ اسے `symmetric_difference()` یا `^` سے حاصل کرتے ہیں۔ ریاضی میں اسے `(A\B) ∪ (B\A)` لکھتے ہیں۔

<div dir="ltr">

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
```

</div>

**مثال:**

<div dir="ltr">

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon
```

</div>

<a id="day-7-section-17"></a>

### غیر مشترک سیٹس جانچنا

دو سیٹس میں کوئی مشترک عنصر نہ ہو تو انہیں *disjoint* کہتے ہیں۔ `isdisjoint()` سے یہ جانچ سکتے ہیں۔

<div dir="ltr">

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

</div>

**مثال:**

<div dir="ltr">

```py
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
```

</div>

🌕 آپ نے ساتویں دن کا چیلنج مکمل کر لیا! اب مشق کریں۔

<a id="day-7-section-18"></a>

## 💻 مشقیں — دن 7

<div dir="ltr">

```py
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

</div>

<a id="day-7-section-19"></a>

### مشقیں: درجہ 1

1. `it_companies` کی لمبائی معلوم کریں۔
2. اس میں `'Twitter'` شامل کریں۔
3. کئی کمپنیاں ایک ساتھ شامل کریں۔
4. ایک کمپنی ہٹائیں۔
5. `remove()` اور `discard()` میں کیا فرق ہے؟

<a id="day-7-section-20"></a>

### مشقیں: درجہ 2

1. `A` اور `B` جوڑیں۔
2. دونوں کا اشتراک معلوم کریں۔
3. کیا `A`، `B` کا ذیلی مجموعہ ہے؟
4. کیا `A` اور `B` غیر مشترک ہیں؟
5. `A` کو `B` سے اور `B` کو `A` سے جوڑیں۔
6. دونوں کا متناظر فرق معلوم کریں۔
7. سیٹس کے متغیرات حذف کریں۔

<a id="day-7-section-21"></a>

### مشقیں: درجہ 3

1. عمروں کی لسٹ کو سیٹ میں بدل کر دونوں کی لمبائی کا موازنہ کریں۔ کون سی زیادہ ہے؟
2. سٹرنگ، لسٹ، ٹپل اور سیٹ کا فرق سمجھائیں۔
3. جملے `I am a teacher and I love to inspire and teach people.` میں کتنے منفرد الفاظ ہیں؟ `split()` اور سیٹ استعمال کریں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 6](./06_tuples.md) | [فہرست](./readme.md) | [اگلا دن: 8](./08_dictionaries.md)

</div>

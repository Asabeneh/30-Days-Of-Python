<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 17 — استثناؤں کو سنبھالنا</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../17_Day_Exception_handling/17_exception_handling.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 16](./16_python_datetime.md) | [فہرست](./readme.md) | [اگلا دن: 18](./18_regular_expressions.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 17](#day-17-section-1)
  - [استثناؤں کو سنبھالنا](#day-17-section-2)
  - [آرگیومنٹس کو جمع کرنا اور کھولنا](#day-17-section-3)
    - [کھولنا: Unpacking](#day-17-section-4)
      - [لسٹ کھولنا](#day-17-section-5)
      - [ڈکشنری کھولنا](#day-17-section-6)
    - [جمع کرنا: Packing](#day-17-section-7)
    - [positional آرگیومنٹس جمع کرنا](#day-17-section-8)
      - [نام زد آرگیومنٹس جمع کرنا](#day-17-section-9)
  - [پائتھن میں عناصر پھیلانا](#day-17-section-10)
  - [enumerate](#day-17-section-11)
  - [zip](#day-17-section-12)
  - [مشقیں — دن 17](#day-17-section-13)

<a id="day-17-section-1"></a>

# 📘 دن 17

<a id="day-17-section-2"></a>

## استثناؤں کو سنبھالنا

پائتھن میں `try` اور `except` سے خرابی کو قابو میں رکھا جا سکتا ہے۔ پروگرام خرابی پہچان کر مناسب پیغام دے سکتا ہے یا باقاعدہ طریقے سے بند ہو سکتا ہے۔ پیغام ٹرمینل یا لاگ میں درج کرنے سے مسئلہ سمجھنا آسان ہوتا ہے۔ غلط ان پٹ، غلط فائل نام، فائل نہ ملنا یا ان پٹ/آؤٹ پٹ آلے کی خرابی ممکنہ اسباب ہیں۔ درست ہینڈلنگ پروگرام کو اچانک بند ہونے سے بچاتی ہے۔

پچھلے حصے میں مختلف غلطیاں پڑھیں۔ `try` میں خرابی آئے تو اس سے مطابقت رکھنے والا `except` اسے سنبھال سکتا ہے؛ ہر ممکن خرابی خودبخود نہیں سنبھلتی۔

![try اور except](../images/try_except.png)

<div dir="ltr">

```py
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
```

</div>

**مثال:**

<div dir="ltr">

```py
try:
    print(10 + '5')
except:
    print('Something went wrong')
```

</div>

دوسری قدر سٹرنگ ہے۔ اسے `int` یا `float` بنائیں تو عدد کے ساتھ جمع ہو سکتی ہے۔ تبدیلی کے بغیر خرابی آئے گی اور `except` چلے گا۔

**مثال:**

<div dir="ltr">

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```

</div>

<div dir="ltr">

```sh
Something went wrong
```

</div>

یہاں `except` چلتا ہے مگر اصل خرابی واضح نہیں ہوتی۔ اس کی نوعیت جاننے کے لیے مخصوص exception اقسام استعمال کریں۔

اگلی مثال خرابی سنبھالنے کے ساتھ اس کی قسم بھی بتاتی ہے۔

<div dir="ltr">

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
```

</div>

<div dir="ltr">

```sh
Enter your name:Asabeneh
Year you born:1920
Type error occured
```

</div>

نتیجہ `TypeError` ہو گا۔ اب مزید بلاک شامل کریں۔

<div dir="ltr">

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
```

</div>

<div dir="ltr">

```sh
Enter your name:Asabeneh
Year you born:1920
You are Asabeneh. And your age is 99.
I usually run with the try block
I alway run.
```

</div>

اسی کو مختصر انداز میں یوں لکھ سکتے ہیں:

<div dir="ltr">

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

```

</div>

<a id="day-17-section-3"></a>

## آرگیومنٹس کو جمع کرنا اور کھولنا

دو آپریٹرز استعمال ہوتے ہیں:

- `*`: positional آرگیومنٹس اور سلسلوں کے لیے۔
- `**`: ڈکشنری اور نام زد آرگیومنٹس کے لیے۔

مثلاً فنکشن الگ آرگیومنٹ لیتا ہو مگر ہمارے پاس لسٹ ہو، تو اسے کھول کر قدریں دے سکتے ہیں۔

<a id="day-17-section-4"></a>

### کھولنا: Unpacking

<a id="day-17-section-5"></a>

#### لسٹ کھولنا

<div dir="ltr">

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

</div>

یہ کوڈ خرابی دیتا ہے، کیونکہ فنکشن کو الگ اعداد چاہییں، پوری لسٹ نہیں۔ لسٹ کھول کر دیں۔

<div dir="ltr">

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

</div>

`range()` کو آغاز اور اختتام دینے میں بھی یہ طریقہ استعمال ہو سکتا ہے۔

<div dir="ltr">

```py
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

```

</div>

لسٹ یا ٹپل کو اس طرح متغیرات میں بھی کھول سکتے ہیں:

<div dir="ltr">

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

</div>

<a id="day-17-section-6"></a>

#### ڈکشنری کھولنا

<div dir="ltr">

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```

</div>

<a id="day-17-section-7"></a>

### جمع کرنا: Packing

آرگیومنٹس کی تعداد پہلے معلوم نہ ہو تو packing سے فنکشن مختلف تعداد قبول کر سکتا ہے۔

<a id="day-17-section-8"></a>

### positional آرگیومنٹس جمع کرنا

`*args` ملنے والی قدروں کو ٹپل میں جمع کرتا ہے۔

<div dir="ltr">

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

</div>

<a id="day-17-section-9"></a>

#### نام زد آرگیومنٹس جمع کرنا

<div dir="ltr">

```py
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

</div>

<div dir="ltr">

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

</div>

<a id="day-17-section-10"></a>

## پائتھن میں عناصر پھیلانا

JavaScript کی طرح پائتھن میں بھی ایک مجموعے کے عناصر دوسرے میں کھول کر شامل کر سکتے ہیں۔

<div dir="ltr">

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

</div>

<a id="day-17-section-11"></a>

## enumerate

عنصر کے ساتھ اس کا انڈیکس بھی چاہیے تو بلٹ اِن `enumerate()` استعمال کریں۔

<div dir="ltr">

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

</div>

<div dir="ltr">

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
```

</div>

<div dir="ltr">

```sh
The country Finland has been found at index 0.
```

</div>

<a id="day-17-section-12"></a>

## zip

کئی لسٹس کے عناصر پر ایک ساتھ لوپ چلانے کے لیے `zip()` استعمال کریں۔

<div dir="ltr">

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

</div>

<div dir="ltr">

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

</div>

🌕 آپ نے سترہویں دن کا چیلنج مکمل کر لیا! اب مشق کریں۔

<a id="day-17-section-13"></a>

## مشقیں — دن 17

1. `names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']` میں پہلے پانچ ممالک `nordic_countries` میں، Estonia کو `es` اور Russia کو `ru` میں کھول کر رکھیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 16](./16_python_datetime.md) | [فہرست](./readme.md) | [اگلا دن: 18](./18_regular_expressions.md)

</div>

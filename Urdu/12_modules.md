<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 12 — ماڈیولز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../12_Day_Modules/12_modules.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 11](./11_functions.md) | [فہرست](./readme.md) | [اگلا دن: 13](./13_list_comprehension.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 12](#day-12-section-1)
  - [ماڈیولز](#day-12-section-2)
    - [ماڈیول کیا ہے؟](#day-12-section-3)
    - [ماڈیول بنانا](#day-12-section-4)
    - [ماڈیول امپورٹ کرنا](#day-12-section-5)
    - [ماڈیول سے فنکشنز امپورٹ کرنا](#day-12-section-6)
    - [امپورٹ کرتے وقت نیا نام دینا](#day-12-section-7)
  - [معیاری لائبریری کے ماڈیولز امپورٹ کرنا](#day-12-section-8)
    - [os ماڈیول](#day-12-section-9)
    - [sys ماڈیول](#day-12-section-10)
    - [statistics ماڈیول](#day-12-section-11)
    - [math ماڈیول](#day-12-section-12)
    - [string ماڈیول](#day-12-section-13)
    - [random ماڈیول](#day-12-section-14)
  - [💻 مشقیں — دن 12](#day-12-section-15)
    - [مشقیں: درجہ 1](#day-12-section-16)
    - [مشقیں: درجہ 2](#day-12-section-17)
    - [مشقیں: درجہ 3](#day-12-section-18)

<a id="day-12-section-1"></a>

# 📘 دن 12

<a id="day-12-section-2"></a>

## ماڈیولز

<a id="day-12-section-3"></a>

### ماڈیول کیا ہے؟

ماڈیول کوڈ یا فنکشنز والی فائل ہے جسے کسی ایپلی کیشن میں شامل کیا جا سکتا ہے۔ اس میں ایک متغیر، ایک فنکشن یا بہت سا کوڈ ہو سکتا ہے۔

<a id="day-12-section-4"></a>

### ماڈیول بنانا

پائتھن کوڈ کو `.py` فائل میں محفوظ کریں۔ منصوبے کے فولڈر میں `mymodule.py` بنائیں اور یہ کوڈ لکھیں۔

<div dir="ltr">

```py
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

</div>

اسی فولڈر میں `main.py` بنائیں اور `mymodule` امپورٹ کریں۔

<a id="day-12-section-5"></a>

### ماڈیول امپورٹ کرنا

`import` کے بعد ماڈیول کا نام لکھیں، `.py` توسیع نہیں۔

<div dir="ltr">

```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

</div>

<a id="day-12-section-6"></a>

### ماڈیول سے فنکشنز امپورٹ کرنا

ایک فائل میں کئی فنکشن ہو سکتے ہیں۔ مطلوبہ فنکشنز الگ بھی امپورٹ کیے جا سکتے ہیں۔

<div dir="ltr">

```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

</div>

<a id="day-12-section-7"></a>

### امپورٹ کرتے وقت نیا نام دینا

`as` سے امپورٹ شدہ فنکشن یا ماڈیول کو مقامی نام دے سکتے ہیں۔

<div dir="ltr">

```py
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

</div>

<a id="day-12-section-8"></a>

## معیاری لائبریری کے ماڈیولز امپورٹ کرنا

`import` سے پائتھن کے ساتھ آنے والے ماڈیولز بھی شامل ہوتے ہیں۔ عام مثالیں `math`، `datetime`، `os`، `sys`، `random`، `statistics`، `collections`، `json` اور `re` ہیں۔

<a id="day-12-section-9"></a>

### os ماڈیول

`os` آپریٹنگ سسٹم کے کام خودکار بنانے میں مدد دیتا ہے، مثلاً فولڈر بنانا، موجودہ فولڈر بدلنا یا معلوم کرنا، مواد دیکھنا اور فولڈر ہٹانا۔

<div dir="ltr">

```py
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

</div>

<a id="day-12-section-10"></a>

### sys ماڈیول

`sys` پائتھن کے چلنے والے ماحول سے متعلق فنکشنز اور متغیرات دیتا ہے۔ `sys.argv` اسکرپٹ کو کمانڈ لائن سے ملنے والے آرگیومنٹس کی لسٹ ہے۔ انڈیکس `0` پر اسکرپٹ کا نام، اور `1` پر پہلا دیا گیا آرگیومنٹ ہوتا ہے۔

`script.py` کی مثال:

<div dir="ltr">

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

</div>

کمانڈ لائن میں اسے یوں چلائیں:

<div dir="ltr">

```sh
python script.py Asabeneh 30DaysOfPython
```

</div>

نتیجہ:

<div dir="ltr">

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge!
```

</div>

`sys` کے چند مفید استعمال:

<div dir="ltr">

```py
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

</div>

<a id="day-12-section-11"></a>

### statistics ماڈیول

عددی ڈیٹا کے شماریاتی حساب کے لیے `mean`، `median`، `mode` اور `stdev` جیسے فنکشنز فراہم کرتا ہے۔

<div dir="ltr">

```py
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

</div>

<a id="day-12-section-12"></a>

### math ماڈیول

اس میں بہت سے ریاضیاتی عمل اور مستقل قدریں ہیں۔

<div dir="ltr">

```py
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
```

</div>

`help(math)` یا `dir(math)` سے دستیاب فنکشنز دیکھیں۔ صرف ایک مخصوص فنکشن امپورٹ کرنا ہو تو:

<div dir="ltr">

```py
from math import pi
print(pi)
```

</div>

کئی فنکشن ایک ساتھ بھی امپورٹ کر سکتے ہیں۔

<div dir="ltr">

```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

</div>

تمام متعلقہ نام امپورٹ کرنے کے لیے `*` استعمال کیا جا سکتا ہے۔

<div dir="ltr">

```py
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
```

</div>

امپورٹ کے وقت فنکشن کا مقامی نام بھی بدل سکتے ہیں۔

<div dir="ltr">

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

</div>

<a id="day-12-section-13"></a>

### string ماڈیول

`string` متن سے متعلق مختلف کاموں میں مفید ہے۔ چند استعمال:

<div dir="ltr">

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

</div>

<a id="day-12-section-14"></a>

### random ماڈیول

ایک اور ماڈیول امپورٹ کر کے مشق کریں۔ `random` میں کئی فنکشنز ہیں؛ یہاں `random()` اور `randint()` استعمال کریں گے۔ `random()` صفر یا اس سے زیادہ اور ایک سے کم اعشاری عدد دیتا ہے۔

<div dir="ltr">

```py
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
```

</div>

🌕 آپ نے بارہویں دن کا چیلنج مکمل کر لیا! اب مشق کریں۔

<a id="day-12-section-15"></a>

## 💻 مشقیں — دن 12

<a id="day-12-section-16"></a>

### مشقیں: درجہ 1

1. `random_user_id` بنائیں جو چھ اعداد یا حروف پر مشتمل اتفاقی شناخت بنائے۔

<div dir="ltr">

```py
  print(random_user_id())
  '1ee33d'
```

</div>

2. `user_id_gen_by_user` بنائیں۔ یہ پیرامیٹر نہ لے، مگر `input()` سے دو قدریں لے: ہر شناخت کے حروف کی تعداد اور بنائی جانے والی شناختوں کی تعداد۔

<div dir="ltr">

```py
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

</div>

3. `rgb_color_gen` بنائیں جو RGB رنگ دے؛ اس کی تین قدریں `0` تا `255` ہوں۔

<div dir="ltr">

```py
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
```

</div>

<a id="day-12-section-17"></a>

### مشقیں: درجہ 2

1. `list_of_hexa_colors` بنائیں جو مطلوبہ تعداد میں ہیکساڈیسیمل رنگوں کی لسٹ دے۔ ہر رنگ `#` کے بعد چھ ہندسوں پر مشتمل ہو؛ سولہ علامتیں `0-9` اور `a-f` استعمال ہوتی ہیں۔ نیچے مثالیں دیکھیں۔
2. `list_of_rgb_colors` بنائیں جو مطلوبہ تعداد میں RGB رنگوں کی لسٹ دے۔
3. `generate_colors` بنائیں جو مطلوبہ تعداد میں `hexa` یا `rgb` رنگ دے۔

<div dir="ltr">

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
```

</div>

<a id="day-12-section-18"></a>

### مشقیں: درجہ 3

1. `shuffle_list` بنائیں جو لسٹ لے اور اس کے عناصر اتفاقی ترتیب میں واپس دے۔
2. فنکشن بنائیں جو `0` تا `9` سے سات منفرد اتفاقی اعداد کی لسٹ دے۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 11](./11_functions.md) | [فہرست](./readme.md) | [اگلا دن: 13](./13_list_comprehension.md)

</div>

<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 15 — پائتھن میں غلطیوں کی اقسام</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../15_Day_Python_type_errors/15_python_type_errors.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 14](./14_higher_order_functions.md) | [فہرست](./readme.md) | [اگلا دن: 16](./16_python_datetime.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 15](#day-15-section-1)
  - [پائتھن میں غلطیوں کی اقسام](#day-15-section-2)
    - [SyntaxError](#day-15-section-3)
    - [NameError](#day-15-section-4)
    - [IndexError](#day-15-section-5)
    - [ModuleNotFoundError](#day-15-section-6)
    - [AttributeError](#day-15-section-7)
    - [KeyError](#day-15-section-8)
    - [TypeError](#day-15-section-9)
    - [ImportError](#day-15-section-10)
    - [ValueError](#day-15-section-11)
    - [ZeroDivisionError](#day-15-section-12)
  - [💻 مشقیں — دن 15](#day-15-section-13)

<a id="day-15-section-1"></a>

# 📘 دن 15

<a id="day-15-section-2"></a>

## پائتھن میں غلطیوں کی اقسام

کوڈ لکھتے وقت املا یا دوسری غلطیاں عام ہیں۔ کوڈ نہ چل سکے تو انٹرپریٹر خرابی کی جگہ اور نوعیت بتاتا ہے، اور کبھی ممکنہ حل بھی تجویز کرتا ہے۔ غلطیوں کی اقسام سمجھنے سے ڈیبگنگ تیز ہوتی ہے۔

ٹرمینل میں `python` لکھ کر تعاملی شیل کھولیں اور عام غلطیاں ایک ایک کر کے دیکھیں۔

<a id="day-15-section-3"></a>

### SyntaxError

**مثال 1: نحوی غلطی**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

</div>

یہاں `print` کے آرگیومنٹ کے گرد قوسین لگانا بھول گئے ہیں۔ پائتھن حل بھی تجویز کرتا ہے۔ اسے درست کریں۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

</div>

`SyntaxError` دور ہونے کے بعد کوڈ چل گیا۔

<a id="day-15-section-4"></a>

### NameError

**مثال 1: نام کی غلطی**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

</div>

`age` کی تعریف کیے بغیر اسے دکھانے کی کوشش ہوئی۔ متغیر بنا کر قدر دیں۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

</div>

متغیر کی تعریف سے `NameError` دور ہو گیا۔

<a id="day-15-section-5"></a>

### IndexError

**مثال 1: انڈیکس کی غلطی**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

</div>

لسٹ کے انڈیکس صرف `0` تا `4` ہیں۔ حد سے باہر انڈیکس استعمال کرنے پر `IndexError` آیا۔

<a id="day-15-section-6"></a>

### ModuleNotFoundError

**مثال 1: ماڈیول نہ ملنا**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

</div>

جان بوجھ کر `math` کے آخر میں اضافی `s` لکھا گیا ہے۔ اسے ہٹا دیں۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

</div>

اب `math` کے فنکشن استعمال کر سکتے ہیں۔

<a id="day-15-section-7"></a>

### AttributeError

**مثال 1: وصف نہ ملنا**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

</div>

`math` میں `pi` کی جگہ `PI` مانگا گیا ہے۔ اس نام کا وصف موجود نہیں، اس لیے `AttributeError` آیا۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

</div>

درست نام `pi` سے نتیجہ مل گیا۔

<a id="day-15-section-8"></a>

### KeyError

**مثال 1: کلید کی غلطی**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

</div>

ڈکشنری کی کلید میں املا کی غلطی ہے۔ درست کلید استعمال کریں۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

</div>

اب مطلوبہ قدر مل گئی۔

<a id="day-15-section-9"></a>

### TypeError

**مثال 1: قسم کی غلطی**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

</div>

عدد اور سٹرنگ کو براہِ راست جمع نہیں کر سکتے۔ سٹرنگ کو `int` یا `float` میں بدلیں۔ دوسری صورت میں عدد کو سٹرنگ بنا کر جوڑ سکتے ہیں، مگر اس کا نتیجہ `'43'` ہو گا۔ پہلے طریقے سے درست کریں۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

</div>

خرابی دور ہو گئی اور متوقع مجموعہ مل گیا۔

<a id="day-15-section-10"></a>

### ImportError

**مثال 1: امپورٹ کی غلطی**

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

</div>

`math` میں `power` نام کا فنکشن نہیں؛ درست نام `pow` ہے۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

</div>

<a id="day-15-section-11"></a>

### ValueError

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

</div>

دی گئی سٹرنگ میں `a` ہے، اس لیے اسے مطلوبہ عدد میں تبدیل نہیں کر سکتے۔

<a id="day-15-section-12"></a>

### ZeroDivisionError

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

</div>

عدد کو صفر سے تقسیم نہیں کر سکتے۔

یہ پائتھن کی چند عام غلطیاں ہیں۔ مزید کے لیے پائتھن کی غلطیوں سے متعلق دستاویزات دیکھیں۔ پیغامات سمجھ کر آپ خرابی جلد درست کر سکیں گے۔

🌕 آپ نے آدھا چیلنج مکمل کر لیا! اب مشق کریں۔

<a id="day-15-section-13"></a>

## 💻 مشقیں — دن 15

1. تعاملی شیل کھولیں اور اس حصے کی تمام مثالیں آزمائیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 14](./14_higher_order_functions.md) | [فہرست](./readme.md) | [اگلا دن: 16](./16_python_datetime.md)

</div>

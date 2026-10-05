<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 14 — ہائر آرڈر فنکشنز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 13](./13_list_comprehension.md) | [فہرست](./readme.md) | [اگلا دن: 15](./15_python_type_errors.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 14](#day-14-section-1)
  - [ہائر آرڈر فنکشنز](#day-14-section-2)
    - [فنکشن بطور پیرامیٹر](#day-14-section-3)
    - [فنکشن بطور واپس آنے والی قدر](#day-14-section-4)
  - [پائتھن کلوزرز](#day-14-section-5)
  - [پائتھن ڈیکوریٹرز](#day-14-section-6)
    - [ڈیکوریٹر بنانا](#day-14-section-7)
    - [ایک فنکشن پر کئی ڈیکوریٹرز](#day-14-section-8)
    - [ڈیکوریٹر کے ذریعے پیرامیٹرز قبول کرنا](#day-14-section-9)
  - [دستیاب ہائر آرڈر فنکشنز](#day-14-section-10)
    - [map فنکشن](#day-14-section-11)
    - [filter فنکشن](#day-14-section-12)
    - [reduce فنکشن](#day-14-section-13)
  - [💻 مشقیں — دن 14](#day-14-section-14)
    - [مشقیں: درجہ 1](#day-14-section-15)
    - [مشقیں: درجہ 2](#day-14-section-16)
    - [مشقیں: درجہ 3](#day-14-section-17)

<a id="day-14-section-1"></a>

# 📘 دن 14

<a id="day-14-section-2"></a>

## ہائر آرڈر فنکشنز

پائتھن میں فنکشنز کو عام قدروں کی طرح استعمال کیا جا سکتا ہے:

- فنکشن ایک یا زیادہ فنکشنز کو پیرامیٹر کے طور پر لے سکتا ہے۔
- ایک فنکشن دوسرے فنکشن کو نتیجے کے طور پر واپس کر سکتا ہے۔
- فنکشن کے رویے میں اضافہ کیا جا سکتا ہے۔
- فنکشن کو متغیر میں رکھا جا سکتا ہے۔

اس حصے میں ہم یہ پڑھیں گے:

1. فنکشن کو پیرامیٹر کے طور پر دینا۔
2. فنکشن کو نتیجے کے طور پر واپس کرنا۔
3. کلوزرز اور ڈیکوریٹرز استعمال کرنا۔

<a id="day-14-section-3"></a>

### فنکشن بطور پیرامیٹر

<div dir="ltr">

```py
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

</div>

<a id="day-14-section-4"></a>

### فنکشن بطور واپس آنے والی قدر

<div dir="ltr">

```py
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

</div>

اوپر ہائر آرڈر فنکشن دیے گئے پیرامیٹر کے مطابق مختلف فنکشن واپس کرتا ہے۔

<a id="day-14-section-5"></a>

## پائتھن کلوزرز

اندرونی فنکشن اپنے بیرونی فنکشن کے دائرے کی قدروں تک رسائی رکھ سکتا ہے۔ جب وہ باہر واپس کیے جانے کے بعد بھی ان قدروں کا حوالہ محفوظ رکھے تو اسے *closure* کہتے ہیں۔ مثال میں بیرونی فنکشن کے اندر فنکشن بنایا اور پھر واپس کیا گیا ہے۔

**مثال:**

<div dir="ltr">

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

</div>

<a id="day-14-section-6"></a>

## پائتھن ڈیکوریٹرز

ڈیکوریٹر موجودہ فنکشن کی تعریف کا متن بدلے بغیر اس کے رویے میں اضافہ کرنے کا طریقہ ہے۔ عموماً اسے متعلقہ فنکشن کی تعریف سے پہلے `@` کے ساتھ لکھتے ہیں۔

<a id="day-14-section-7"></a>

### ڈیکوریٹر بنانا

ایک بیرونی فنکشن اور اس کے اندر لپیٹنے والا *wrapper* فنکشن بنائیں۔

**مثال:**

<div dir="ltr">

```py
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

</div>

<a id="day-14-section-8"></a>

### ایک فنکشن پر کئی ڈیکوریٹرز

<div dir="ltr">

```py

'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#Decorators will be executed from bottom to top
@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

</div>

<a id="day-14-section-9"></a>

### ڈیکوریٹر کے ذریعے پیرامیٹرز قبول کرنا

اصل فنکشن اکثر پیرامیٹر لیتا ہے، اس لیے wrapper کو بھی مناسب آرگیومنٹس قبول کرنے کی ضرورت ہوتی ہے۔

<div dir="ltr">

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

</div>

<a id="day-14-section-10"></a>

## دستیاب ہائر آرڈر فنکشنز

یہاں `map()`، `filter()` اور `reduce()` پڑھیں گے۔ `map` اور `filter` بلٹ اِن ہیں؛ `reduce` کو `functools` سے امپورٹ کرتے ہیں۔ ان میں لیمبڈا بطور فنکشن دینا ایک عام استعمال ہے۔

<a id="day-14-section-11"></a>

### map فنکشن

`map()` ایک فنکشن اور قابلِ تکرار مجموعہ لیتا ہے۔

<div dir="ltr">

```py
    # syntax
    map(function, iterable)
```

</div>

**مثال 1:**

<div dir="ltr">

```py
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

</div>

**مثال 2:**

<div dir="ltr">

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

</div>

**مثال 3:**

<div dir="ltr">

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

</div>

`map()` ہر عنصر پر فنکشن لگاتا ہے، مثلاً نام بڑے حروف میں بدلتا ہے۔ پائتھن 3 میں یہ iterator دیتا ہے؛ اوپر اسے `list()` سے لسٹ بنایا گیا ہے۔

<a id="day-14-section-12"></a>

### filter فنکشن

`filter()` ہر عنصر کے لیے دیا گیا فنکشن چلاتا ہے اور وہ عناصر منتخب کرتا ہے جن کا نتیجہ درست ہو۔ پائتھن 3 میں یہ iterator دیتا ہے؛ لسٹ چاہیے تو نتیجے کو `list()` میں دیں۔

<div dir="ltr">

```py
    # syntax
    filter(function, iterable)
```

</div>

**مثال 1:**

<div dir="ltr">

```py
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

</div>

**مثال 2:**

<div dir="ltr">

```py
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

</div>

<div dir="ltr">

```py
# Filter long name
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

</div>

<a id="day-14-section-13"></a>

### reduce فنکشن

`reduce()`، `functools` میں ہے۔ فنکشن اور قابلِ تکرار مجموعہ لے کر قدروں کو یکجا کرتا ہے اور ایک نتیجہ واپس کرتا ہے۔

**مثال 1:**

<div dir="ltr">

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

</div>

<a id="day-14-section-14"></a>

## 💻 مشقیں — دن 14

<div dir="ltr">

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

</div>

<a id="day-14-section-15"></a>

### مشقیں: درجہ 1

1. `map`، `filter` اور `reduce` کا فرق سمجھائیں۔
2. ہائر آرڈر فنکشن، کلوزر اور ڈیکوریٹر کا فرق سمجھائیں۔
3. مثالوں کی طرح `map`، `filter` یا `reduce` میں دینے سے پہلے متعلقہ فنکشن تعریف کریں۔
4. `for` سے `countries` کا ہر ملک دکھائیں۔
5. `for` سے `names` کا ہر نام دکھائیں۔
6. `for` سے `numbers` کا ہر عدد دکھائیں۔

<a id="day-14-section-16"></a>

### مشقیں: درجہ 2

1. `map` سے ممالک کے نام بڑے حروف میں بدل کر نئی لسٹ بنائیں۔
2. `map` سے ہر عدد کا مربع لے کر نئی لسٹ بنائیں۔
3. `map` سے تمام نام بڑے حروف میں بدلیں۔
4. `filter` سے `land` والے ممالک منتخب کریں۔
5. بالکل چھ حروف والے ممالک منتخب کریں۔
6. چھ یا زیادہ حروف والے ممالک منتخب کریں۔
7. `E` سے شروع ہونے والے ممالک منتخب کریں۔
8. دو یا زیادہ تبدیلیاں، مثلاً `map`، پھر `filter`، پھر `reduce`، ملا کر استعمال کریں۔ اصل سوال کی `arr.map(callback).filter(callback).reduce(callback)` عبارت JavaScript کا انداز ہے؛ پائتھن میں متعلقہ فنکشنز ایک دوسرے کے نتیجے پر لگائیں۔
9. `get_string_lists` بنائیں جو لسٹ سے صرف سٹرنگ عناصر واپس کرے۔
10. `reduce` سے تمام اعداد جمع کریں۔
11. `reduce` سے ممالک جوڑ کر یہ جملہ بنائیں: `Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries`۔
12. `categorize_countries` بنائیں جو مشترک نمونے، مثلاً `land`، `ia`، `island` یا `stan`، والے ممالک کی لسٹ دے۔ [countries.py](../data/countries.py) استعمال کریں۔
13. فنکشن بنائیں جو ڈکشنری دے؛ کلید ملک کے نام کا پہلا حرف اور قدر اس حرف سے شروع ہونے والے ممالک کی تعداد ہو۔
14. `get_first_ten_countries` پہلے دس ممالک دے۔
15. `get_last_ten_countries` آخری دس ممالک دے۔

<a id="day-14-section-17"></a>

### مشقیں: درجہ 3

1. [countries-data.py](../data/countries-data.py) استعمال کریں:
   - ممالک کو نام، دارالحکومت اور آبادی کے لحاظ سے ترتیب دیں۔
   - ڈیٹا کے مطابق سب سے زیادہ بولی جانے والی دس زبانیں نکالیں۔
   - سب سے زیادہ آبادی والے دس ممالک نکالیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 13](./13_list_comprehension.md) | [فہرست](./readme.md) | [اگلا دن: 15](./15_python_type_errors.md)

</div>

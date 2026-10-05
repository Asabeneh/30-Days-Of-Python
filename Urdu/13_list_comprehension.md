<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 13 — لسٹ کمپری ہینشن</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../13_Day_List_comprehension/13_list_comprehension.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 12](./12_modules.md) | [فہرست](./readme.md) | [اگلا دن: 14](./14_higher_order_functions.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 13](#day-13-section-1)
  - [لسٹ کمپری ہینشن](#day-13-section-2)
  - [لیمبڈا فنکشن](#day-13-section-3)
    - [لیمبڈا فنکشن بنانا](#day-13-section-4)
    - [دوسرے فنکشن کے اندر لیمبڈا](#day-13-section-5)
  - [💻 مشقیں — دن 13](#day-13-section-6)

<a id="day-13-section-1"></a>

# 📘 دن 13

<a id="day-13-section-2"></a>

## لسٹ کمپری ہینشن

لسٹ کمپری ہینشن کسی سلسلے سے نئی لسٹ بنانے کا مختصر طریقہ ہے۔ یہ اکثر ایسا `for` لوپ لکھنے سے مختصر، اور بعض صورتوں میں تیز، ہوتا ہے جو ایک ایک عنصر شامل کرتا ہے۔

<div dir="ltr">

```py
# syntax
[expression for i in iterable if condition]
```

</div>

**مثال 1:**

سٹرنگ کو حروف کی لسٹ بنانے کے مختلف طریقے دیکھیں۔

<div dir="ltr">

```py
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

</div>

**مثال 2:**

اعداد کی لسٹ بنانا:

<div dir="ltr">

```py
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

</div>

**مثال 3:**

لسٹ کمپری ہینشن میں `if` کی شرط بھی شامل کر سکتے ہیں۔

<div dir="ltr">

```py
# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</div>

<a id="day-13-section-3"></a>

## لیمبڈا فنکشن

لیمبڈا ایک مختصر، بے نام فنکشن ہے۔ کئی آرگیومنٹ لے سکتا ہے مگر صرف ایک expression پر مشتمل ہوتا ہے۔ یہ JavaScript کے بے نام فنکشن سے ملتا جلتا ہے، اور دوسرے فنکشن کے اندر مختصر فنکشن لکھنے میں کام آتا ہے۔

<a id="day-13-section-4"></a>

### لیمبڈا فنکشن بنانا

`lambda` کے بعد پیرامیٹرز اور پھر expression لکھیں۔ اس میں `return` نہیں لکھتے؛ expression کی قدر خود واپس ہوتی ہے۔

<div dir="ltr">

```py
# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

</div>

**مثال:**

<div dir="ltr">

```py
# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

</div>

<a id="day-13-section-5"></a>

### دوسرے فنکشن کے اندر لیمبڈا

<div dir="ltr">

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32
```

</div>

🌕 آپ نے تیرہویں دن کا چیلنج مکمل کر لیا! مشق جاری رکھیں۔

<a id="day-13-section-6"></a>

## 💻 مشقیں — دن 13

1. لسٹ کمپری ہینشن سے صرف منفی اعداد اور صفر چھانٹیں۔

<div dir="ltr">

```py
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
```

</div>

2. لسٹوں کے اندر موجود لسٹوں کو ایک سطح کی لسٹ بنائیں۔

<div dir="ltr">

```py
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

</div>

3. لسٹ کمپری ہینشن سے ٹپلز کی یہ لسٹ بنائیں:

<div dir="ltr">

```py
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
```

</div>

4. درج ذیل لسٹ کو دکھائی گئی نئی لسٹ میں بدلیں:

<div dir="ltr">

```py
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
```

</div>

5. یہ لسٹ ڈکشنریز کی لسٹ میں بدلیں:

<div dir="ltr">

```py
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
```

</div>

6. اندرونی لسٹس کو جوڑی ہوئی سٹرنگز کی لسٹ میں بدلیں:

<div dir="ltr">

```py
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
```

</div>

7. خطی فنکشن کی ڈھلوان یا وہ قدر معلوم کرنے والا لیمبڈا لکھیں جہاں خط عمودی محور کو کاٹتا ہے (*y-intercept*)۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 12](./12_modules.md) | [فہرست](./readme.md) | [اگلا دن: 14](./14_higher_order_functions.md)

</div>

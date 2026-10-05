<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 3 — آپریٹرز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../03_Day_Operators/03_operators.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 2](./02_variables_builtin_functions.md) | [فہرست](./readme.md) | [اگلا دن: 4](./04_strings.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 3](#day-3-section-1)
  - [بولین](#day-3-section-2)
  - [آپریٹرز](#day-3-section-3)
    - [اسائنمنٹ آپریٹرز](#day-3-section-4)
    - [حسابی آپریٹرز](#day-3-section-5)
    - [موازنہ کرنے والے آپریٹرز](#day-3-section-6)
    - [منطقی آپریٹرز](#day-3-section-7)
  - [💻 مشقیں — دن 3](#day-3-section-8)

<a id="day-3-section-1"></a>

# 📘 دن 3

<a id="day-3-section-2"></a>

## بولین

بولین کی دو ممکنہ قدریں ہیں: `True` اور `False`۔ موازنہ کرنے والے آپریٹرز کے ساتھ ان کا استعمال زیادہ واضح ہو گا۔ JavaScript کے برعکس، پائتھن میں `True` کا **T** اور `False` کا **F** بڑا ہونا چاہیے۔

**مثال: بولین قدریں**

<div dir="ltr">

```py
print(True)
print(False)
```

</div>

<a id="day-3-section-3"></a>

## آپریٹرز

پائتھن میں کئی طرح کے آپریٹرز ہوتے ہیں۔ اس حصے میں چند اہم اقسام پڑھیں گے۔

<a id="day-3-section-4"></a>

### اسائنمنٹ آپریٹرز

اسائنمنٹ آپریٹرز متغیرات کو قدریں دینے کے لیے ہوتے ہیں۔ مثلاً `=` ریاضی میں مساوات دکھاتا ہے، مگر پائتھن میں یہ کسی متغیر کو قدر دیتا ہے۔ نیچے [W3Schools](https://www.w3schools.com/python/python_operators.asp) سے مختلف اسائنمنٹ آپریٹرز کی جدول دی گئی ہے۔

![اسائنمنٹ آپریٹرز](../images/assignment_operators.png)

<a id="day-3-section-5"></a>

### حسابی آپریٹرز

- جمع (`+`): `a + b`
- تفریق (`-`): `a - b`
- ضرب (`*`): `a * b`
- تقسیم (`/`): `a / b`
- باقی (`%`): `a % b`
- فلور ڈویژن (`//`): `a // b`
- قوت (`**`): `a ** b`

![حسابی آپریٹرز](../images/arithmetic_operators.png)

**مثال: صحیح اعداد**

<div dir="ltr">

```py
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division: ', 6 / 2)        # 3.0
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, Gives the remainder
print('Exponentiation: ', 2 ** 3) # 8 it means 2 * 2 * 2
```

</div>

**مثال: اعشاری اعداد**

<div dir="ltr">

```py
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
```

</div>

**مثال: مختلط اعداد**

<div dir="ltr">

```py
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

</div>

ایک متغیر بنا کر اسے عددی قدر دیں۔ یہاں ایک حرف کے نام استعمال ہوئے ہیں، مگر واضح اور بامعنی نام رکھنے کی عادت اپنائیں۔

**مثال:**

<div dir="ltr">

```python
# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
print(total) # if you do not label your print with some string, you never know where the result is coming from
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
```

</div>

**مثال:**

<div dir="ltr">

```py
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
```

</div>

اب سیکھی ہوئی باتوں کو ملا کر رقبہ، حجم، کثافت، وزن، محیط، فاصلہ اور قوت معلوم کریں۔

**مثال:**

<div dir="ltr">

```py
# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # Adding unit to the density

```

</div>

<a id="day-3-section-6"></a>

### موازنہ کرنے والے آپریٹرز

پروگرامنگ میں قدروں کا موازنہ ان آپریٹرز سے کیا جاتا ہے۔ مثلاً جانچتے ہیں کہ ایک قدر دوسری سے بڑی، چھوٹی یا برابر ہے۔ یہ جدول [W3Schools](https://www.w3schools.com/python/python_operators.asp) سے لی گئی ہے۔

![موازنے کے آپریٹرز](../images/comparison_operators.png)

**مثال: موازنے کے آپریٹرز**

<div dir="ltr">

```py
print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# Comparing something gives either a True or False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```

</div>

پائتھن میں درج ذیل آپریٹرز بھی استعمال ہوتے ہیں:

- `is`: دونوں متغیرات ایک ہی آبجیکٹ کا حوالہ ہوں تو `True`، مثلاً `x is y`۔
- `is not`: دونوں ایک ہی آبجیکٹ کا حوالہ نہ ہوں تو `True`، مثلاً `x is not y`۔
- `in`: مطلوبہ عنصر مجموعے میں موجود ہو تو `True`، مثلاً `x in y`۔
- `not in`: مطلوبہ عنصر موجود نہ ہو تو `True`، مثلاً `x not in y`۔

<div dir="ltr">

```py
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
```

</div>

<a id="day-3-section-7"></a>

### منطقی آپریٹرز

پائتھن میں منطقی عمل کے لیے `and`، `or` اور `not` استعمال ہوتے ہیں۔ ان سے شرطوں کو یکجا یا الٹ کیا جا سکتا ہے۔

![منطقی آپریٹرز](../images/logical_operators.png)

<div dir="ltr">

```py
print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

```

</div>

🌕 آپ نے تیسرے دن کا چیلنج مکمل کر لیا! اب اپنی سمجھ کو مشقوں سے آزمائیں۔

<a id="day-3-section-8"></a>

## 💻 مشقیں — دن 3

1. اپنی عمر صحیح عدد والے متغیر میں رکھیں۔
2. اپنا قد اعشاری متغیر میں رکھیں۔
3. مختلط عدد رکھنے والا متغیر بنائیں۔
4. ایسا اسکرپٹ لکھیں جو صارف سے مثلث کی بنیاد اور اونچائی لے اور رقبہ نکالے: `area = 0.5 * b * h`۔

<div dir="ltr">

```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```

</div>

5. صارف سے مثلث کے اضلاع `a`، `b` اور `c` لیں اور محیط نکالیں: `perimeter = a + b + c`۔

<div dir="ltr">

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

</div>

6. مستطیل کی لمبائی اور چوڑائی لیں۔ رقبہ `length * width` اور محیط `2 * (length + width)` معلوم کریں۔
7. دائرے کا رداس لیں۔ `pi = 3.14` فرض کرتے ہوئے رقبہ `pi * r * r` اور محیط `2 * pi * r` معلوم کریں۔
8. `y = 2x - 2` کی ڈھلوان اور وہ نقاط معلوم کریں جہاں خط افقی اور عمودی محور کو کاٹتا ہے۔
9. ڈھلوان کا فارمولا `m = (y2 - y1) / (x2 - x1)` ہے۔ نقاط `(2, 2)` اور `(6, 10)` کے درمیان ڈھلوان اور [اقلیدسی فاصلہ](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) معلوم کریں۔
10. سوال 8 اور 9 کی ڈھلوانوں کا موازنہ کریں۔
11. `y = x² + 6x + 9` میں مختلف `x` رکھ کر `y` نکالیں۔ کس `x` پر `y` صفر ہوتا ہے؟
12. `'python'` اور `'dragon'` کی لمبائی معلوم کریں اور ایسا موازنہ لکھیں جس کا نتیجہ `False` ہو۔
13. `and` سے جانچیں کہ `'on'` دونوں سٹرنگز `'python'` اور `'dragon'` میں موجود ہے۔
14. جملے `I hope this course is not full of jargon` میں `in` سے لفظ `jargon` کی موجودگی جانچیں۔
15. یہ دعویٰ جانچیں کہ `'on'`، `'dragon'` اور `'python'` دونوں میں موجود نہیں۔
16. متن `'python'` کی لمبائی کو پہلے `float` اور پھر سٹرنگ میں تبدیل کریں۔
17. جفت عدد کو 2 سے تقسیم کرنے پر باقی صفر ہوتا ہے۔ پائتھن میں کیسے جانچیں گے کہ عدد جفت ہے؟
18. جانچیں کہ `7 // 3`، `int(2.7)` کے برابر ہے یا نہیں۔
19. جانچیں کہ `'10'` اور `10` کی اقسام ایک جیسی ہیں یا نہیں۔
20. جانچیں کہ `int('9.8')`، `10` کے برابر ہے یا نہیں؛ تبدیلی کے دوران آنے والے نتیجے یا خرابی پر غور کریں۔
21. صارف سے کام کے گھنٹے اور فی گھنٹہ اجرت لیں اور کل اجرت نکالیں۔

<div dir="ltr">

```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

</div>

22. صارف سے سالوں کی تعداد لے کر سیکنڈز میں تبدیل کریں۔ فرض کریں کہ انسان سو سال زندہ رہ سکتا ہے۔

<div dir="ltr">

```py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
```

</div>

23. ایسا پائتھن اسکرپٹ لکھیں جو یہ جدول دکھائے:

<div dir="ltr">

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

</div>

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 2](./02_variables_builtin_functions.md) | [فہرست](./readme.md) | [اگلا دن: 4](./04_strings.md)

</div>

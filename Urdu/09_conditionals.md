<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 9 — شرطیں</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../09_Day_Conditionals/09_conditionals.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 8](./08_dictionaries.md) | [فہرست](./readme.md) | [اگلا دن: 10](./10_loops.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 9](#day-9-section-1)
  - [شرطیں](#day-9-section-2)
    - [if کی شرط](#day-9-section-3)
    - [if اور else](#day-9-section-4)
    - [if، elif اور else](#day-9-section-5)
    - [مختصر صورت](#day-9-section-6)
    - [شرط کے اندر شرط](#day-9-section-7)
    - [if کے ساتھ منطقی and](#day-9-section-8)
    - [if کے ساتھ منطقی or](#day-9-section-9)
  - [💻 مشقیں — دن 9](#day-9-section-10)
    - [مشقیں: درجہ 1](#day-9-section-11)
    - [مشقیں: درجہ 2](#day-9-section-12)
    - [مشقیں: درجہ 3](#day-9-section-13)

<a id="day-9-section-1"></a>

# 📘 دن 9

<a id="day-9-section-2"></a>

## شرطیں

عام طور پر پائتھن اسکرپٹ کی ہدایات اوپر سے نیچے ترتیب وار چلتی ہیں۔ پروگرام کی منطق کے مطابق اس بہاؤ کو دو طرح سے بدل سکتے ہیں:

- مشروط اجرا: شرط درست ہو تو ایک یا زیادہ ہدایات کا بلاک چلتا ہے۔
- تکراری اجرا: شرط درست رہنے تک بلاک بار بار چلتا ہے۔

اس حصے میں `if`، `else` اور `elif` پڑھیں گے۔ پہلے سیکھے ہوئے موازنے اور منطقی آپریٹرز یہاں کام آئیں گے۔

<a id="day-9-section-3"></a>

### if کی شرط

`if` شرط جانچ کر درست ہونے پر متعلقہ بلاک چلاتا ہے۔ کولن `:` کے بعد بلاک کی انڈینٹیشن یاد رکھیں۔

<div dir="ltr">

```py
# syntax
if condition:
    this part of code runs for truthy conditions
```

</div>

**مثال 1:**

<div dir="ltr">

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

</div>

یہاں `3`، `0` سے بڑا ہے، اس لیے بلاک چلا۔ شرط غلط ہو تو یہ بلاک نہیں چلے گا۔ ایسی صورت میں کوئی اور کام کرنے کے لیے `else` چاہیے۔

<a id="day-9-section-4"></a>

### if اور else

شرط درست ہو تو پہلا بلاک، ورنہ `else` والا بلاک چلتا ہے۔

<div dir="ltr">

```py
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

</div>

**مثال:**

<div dir="ltr">

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

</div>

یہاں شرط غلط ہے، اس لیے `else` چلا۔ دو سے زیادہ امکانات جانچنے کے لیے `elif` استعمال کر سکتے ہیں۔

<a id="day-9-section-5"></a>

### if، elif اور else

روزمرہ فیصلوں کی طرح پروگرامنگ میں بھی کئی شرطیں جانچنی پڑتی ہیں۔ `elif` مزید شرطیں ترتیب سے جانچنے کے لیے ہے۔

<div dir="ltr">

```py
# syntax
if condition:
    code
elif condition:
    code
else:
    code

```

</div>

**مثال:**

<div dir="ltr">

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

</div>

<a id="day-9-section-6"></a>

### مختصر صورت

<div dir="ltr">

```py
# syntax
code if condition else code
```

</div>

**مثال:**

<div dir="ltr">

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
```

</div>

<a id="day-9-section-7"></a>

### شرط کے اندر شرط

ایک شرط کے بلاک میں دوسری شرط رکھی جا سکتی ہے۔

<div dir="ltr">

```py
# syntax
if condition:
    code
    if condition:
    code
```

</div>

**مثال:**

<div dir="ltr">

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

```

</div>

بعض صورتوں میں اندرونی شرط کے بجائے منطقی `and` استعمال کیا جا سکتا ہے۔

<a id="day-9-section-8"></a>

### if کے ساتھ منطقی and

<div dir="ltr">

```py
# syntax
if condition and condition:
    code
```

</div>

**مثال:**

<div dir="ltr">

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

</div>

<a id="day-9-section-9"></a>

### if کے ساتھ منطقی or

<div dir="ltr">

```py
# syntax
if condition or condition:
    code
```

</div>

**مثال:**

<div dir="ltr">

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

</div>

🌕 آپ نے نویں دن کا چیلنج مکمل کر لیا! مسلسل مشق سے مہارت بڑھتی ہے۔

<a id="day-9-section-10"></a>

## 💻 مشقیں — دن 9

<a id="day-9-section-11"></a>

### مشقیں: درجہ 1

1. `input('Enter your age: ')` سے عمر لیں۔ عمر 18 یا زیادہ ہو تو ڈرائیونگ کی عمر پوری ہونے کا پیغام دیں۔ کم ہو تو بتائیں کہ مزید کتنے سال انتظار کرنا ہے۔ مطلوبہ نتیجہ:

<div dir="ltr">

```sh
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
```

</div>

2. `if ... else` سے `my_age` اور `your_age` کا موازنہ کریں۔ `input('Enter your age: ')` سے عمر لیں۔ فرق ایک سال ہو تو `year`، زیادہ ہو تو `years` اور برابر ہو تو مناسب پیغام دکھائیں۔ اندرونی شرط استعمال کر سکتے ہیں۔

<div dir="ltr">

```sh
Enter your age: 30
You are 5 years older than me.
```

</div>

3. صارف سے دو اعداد لیں۔ بتائیں کہ `a`، `b` سے بڑا، چھوٹا یا برابر ہے۔

<div dir="ltr">

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

</div>

<a id="day-9-section-12"></a>

### مشقیں: درجہ 2

1. نمبروں کے مطابق یہ گریڈ دیں:

<div dir="ltr">

```sh
90-100, A
80-89, B
70-79, C
60-69, D
0-59, F
```

</div>

2. صارف سے مہینہ لے کر اس مشق کی درج ذیل تقسیم کے مطابق موسم بتائیں:
   - September، October، November: خزاں۔
   - December، January، February: سردی۔
   - March، April، May: بہار۔
   - June، July، August: گرمی۔
3. پھلوں کی یہ لسٹ استعمال کریں:

<div dir="ltr">

```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```

</div>

پھل موجود نہ ہو تو شامل کر کے تبدیل شدہ لسٹ دکھائیں۔ موجود ہو تو `That fruit already exist in the list` دکھائیں۔

<a id="day-9-section-13"></a>

### مشقیں: درجہ 3

1. ایک شخص کی یہ ڈکشنری استعمال کریں؛ چاہیں تو قدریں بدل لیں۔

<div dir="ltr">

```py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

</div>

- `skills` کلید موجود ہو تو مہارتوں کی لسٹ کا درمیانی عنصر دکھائیں۔
- `skills` موجود ہو تو `'Python'` کی موجودگی جانچ کر نتیجہ دکھائیں۔
- صرف JavaScript اور React ہوں تو `He is a front end developer` دکھائیں۔ Node، Python اور MongoDB ہوں تو `He is a backend developer`؛ React، Node اور MongoDB ہوں تو `He is a fullstack developer`؛ ورنہ `unknown title`۔ زیادہ درست درجہ بندی کے لیے مزید شرطیں شامل کر سکتے ہیں۔
- شخص شادی شدہ ہو اور فن لینڈ میں رہتا ہو تو معلومات اس صورت میں دکھائیں:

<div dir="ltr">

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

</div>

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 8](./08_dictionaries.md) | [فہرست](./readme.md) | [اگلا دن: 10](./10_loops.md)

</div>

<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 10 — لوپس</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../10_Day_Loops/10_loops.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 9](./09_conditionals.md) | [فہرست](./readme.md) | [اگلا دن: 11](./11_functions.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 10](#day-10-section-1)
  - [لوپس](#day-10-section-2)
    - [while لوپ](#day-10-section-3)
    - [break اور continue — حصہ 1](#day-10-section-4)
    - [for لوپ](#day-10-section-5)
    - [break اور continue — حصہ 2](#day-10-section-6)
    - [range فنکشن](#day-10-section-7)
    - [for لوپ کے اندر لوپ](#day-10-section-8)
    - [for کے ساتھ else](#day-10-section-9)
    - [pass](#day-10-section-10)
  - [💻 مشقیں — دن 10](#day-10-section-11)
    - [مشقیں: درجہ 1](#day-10-section-12)
    - [مشقیں: درجہ 2](#day-10-section-13)
    - [مشقیں: درجہ 3](#day-10-section-14)

<a id="day-10-section-1"></a>

# 📘 دن 10

<a id="day-10-section-2"></a>

## لوپس

پروگرامنگ میں کئی کام بار بار کرنے پڑتے ہیں۔ انہیں دہرانے کے لیے لوپس استعمال ہوتے ہیں۔ پائتھن میں دو بنیادی لوپس ہیں:

1. `while` لوپ
2. `for` لوپ

<a id="day-10-section-3"></a>

### while لوپ

`while` کا بلاک اس وقت تک بار بار چلتا ہے جب تک شرط درست ہو۔ شرط غلط ہوتے ہی لوپ کے بعد کی ہدایات چلتی ہیں۔

<div dir="ltr">

```py
  # syntax
while condition:
    code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
```

</div>

`count` کی قدر `5` ہوتے ہی شرط غلط ہو جاتی ہے اور لوپ رک جاتا ہے۔ شرط ختم ہونے پر کوئی بلاک چلانا ہو تو `else` استعمال کر سکتے ہیں۔

<div dir="ltr">

```py
  # syntax
while condition:
    code goes here
else:
    code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

</div>

یہاں `count` کے `5` ہونے پر لوپ ختم ہوتا ہے، پھر `else` چل کر `5` دکھاتا ہے۔

<a id="day-10-section-4"></a>

### break اور continue — حصہ 1

- `break`: لوپ فوراً روکنے کے لیے۔

<div dir="ltr">

```py
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

</div>

**مثال:**

<div dir="ltr">

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

</div>

یہ لوپ `0`، `1` اور `2` دکھاتا ہے؛ `3` پر رک جاتا ہے۔

- `continue`: موجودہ چکر کی باقی ہدایات چھوڑ کر اگلا چکر شروع کرنے کے لیے۔

<div dir="ltr">

```py
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

</div>

**مثال:**

<div dir="ltr">

```py
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

</div>

یہ لوپ `0`، `1`، `2` اور `4` دکھاتا ہے؛ `3` چھوڑ دیتا ہے۔

<a id="day-10-section-5"></a>

### for لوپ

`for` سے کسی قابلِ تکرار مجموعے، مثلاً لسٹ، ٹپل، ڈکشنری، سیٹ یا سٹرنگ، کے عناصر پر باری باری کام کرتے ہیں۔ اس کی نحو دوسری زبانوں سے کچھ مختلف ہو سکتی ہے۔

- لسٹ پر `for`:

<div dir="ltr">

```py
# syntax
for iterator in lst:
    code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
```

</div>

- سٹرنگ پر `for`:

<div dir="ltr">

```py
# syntax
for iterator in string:
    code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

</div>

- ٹپل پر `for`:

<div dir="ltr">

```py
# syntax
for iterator in tpl:
    code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

</div>

- ڈکشنری پر `for`: براہِ راست ڈکشنری پر لوپ چلانے سے کلیدیں ملتی ہیں۔

<div dir="ltr">

```py
  # syntax
for iterator in dct:
    code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

</div>

- سیٹ پر `for`:

<div dir="ltr">

```py
# syntax
for iterator in st:
    code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

</div>

<a id="day-10-section-6"></a>

### break اور continue — حصہ 2

یاد رکھیں: `break` لوپ کو مکمل ہونے سے پہلے روک دیتا ہے۔

<div dir="ltr">

```py
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

</div>

**مثال:**

<div dir="ltr">

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

</div>

اوپر لوپ `3` پر رک جاتا ہے۔

`continue` موجودہ چکر کی باقی ہدایات چھوڑ دیتا ہے۔

<div dir="ltr">

```py
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

</div>

**مثال:**

<div dir="ltr">

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```

</div>

عدد `3` ہو تو شرط کے بعد موجود لوپ کی ہدایات چھوڑ دی جاتی ہیں؛ باقی عناصر کے لیے لوپ جاری رہتا ہے۔

<a id="day-10-section-7"></a>

### range فنکشن

`range()` اعداد کا سلسلہ ظاہر کرنے والا آبجیکٹ دیتا ہے؛ پائتھن 3 میں یہ خود لسٹ نہیں ہوتا۔ `range(start, end, step)` میں آغاز، اختتام اور قدم دیا جاتا ہے۔ طے شدہ آغاز `0` اور قدم `1` ہے۔ کم از کم اختتام دینا ضروری ہے، اور وہ سلسلے میں شامل نہیں ہوتا۔

<div dir="ltr">

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

</div>

<div dir="ltr">

```py
# syntax
for iterator in range(start, end, step):
```

</div>

**مثال:**

<div dir="ltr">

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

</div>

<a id="day-10-section-8"></a>

### for لوپ کے اندر لوپ

ایک لوپ کے اندر دوسرا لوپ لکھ سکتے ہیں۔

<div dir="ltr">

```py
# syntax
for x in y:
    for t in x:
        print(t)
```

</div>

**مثال:**

<div dir="ltr">

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

</div>

<a id="day-10-section-9"></a>

### for کے ساتھ else

لوپ معمول کے مطابق مکمل ہو جائے تو `else` چلتا ہے۔ `break` سے نکلنے پر یہ نہیں چلتا۔

<div dir="ltr">

```py
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

</div>

**مثال:**

<div dir="ltr">

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

</div>

<a id="day-10-section-10"></a>

### pass

جہاں ہدایت ضروری ہو، مثلاً کولن کے بعد بلاک میں، مگر ابھی کوئی کام نہ کرنا ہو تو `pass` لکھیں۔ اسے بعد میں کوڈ شامل کرنے کی جگہ محفوظ رکھنے کے لیے بھی استعمال کرتے ہیں۔

**مثال:**

<div dir="ltr">

```py
for number in range(6):
    pass
```

</div>

🌕 آپ نے دس دن مکمل کر لیے! آگے بڑھیں اور مشق جاری رکھیں۔

<a id="day-10-section-11"></a>

## 💻 مشقیں — دن 10

<a id="day-10-section-12"></a>

### مشقیں: درجہ 1

1. `for` سے `0` تا `10` دکھائیں، پھر `while` سے یہی کریں۔
2. `for` سے `10` تا `0` دکھائیں، پھر `while` سے یہی کریں۔
3. سات بار `print()` چلانے والا لوپ لکھیں جو یہ مثلث بنائے:

<div dir="ltr">

```py
  #
  ##
  ###
  ####
  #####
  ######
  #######
```

</div>

4. اندرونی لوپس سے یہ بنائیں:

<div dir="ltr">

```sh
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
```

</div>

5. یہ نمونہ دکھائیں:

<div dir="ltr">

```sh
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
```

</div>

6. `['Python', 'Numpy', 'Pandas', 'Django', 'Flask']` کے عناصر `for` سے دکھائیں۔
7. `0` تا `100` میں صرف جفت اعداد دکھائیں۔
8. اسی حد میں صرف طاق اعداد دکھائیں۔

<a id="day-10-section-13"></a>

### مشقیں: درجہ 2

1. `for` سے `0` تا `100` تمام اعداد کا مجموعہ دکھائیں۔

<div dir="ltr">

```sh
The sum of all numbers is 5050.
```

</div>

2. اسی حد میں جفت اعداد اور طاق اعداد کے الگ مجموعے دکھائیں۔

<div dir="ltr">

```sh
The sum of all evens is 2550. And the sum of all odds is 2500.
```

</div>

<a id="day-10-section-14"></a>

### مشقیں: درجہ 3

1. ڈیٹا فولڈر کی [countries.py](../data/countries.py) استعمال کریں۔ لوپ سے وہ ممالک نکالیں جن کے نام میں `land` آتا ہے۔
2. `['banana', 'orange', 'mango', 'lemon']` کی ترتیب لوپ سے الٹیں۔
3. [countries-data.py](../data/countries-data.py) استعمال کرتے ہوئے:
   1. زبانوں کی کل تعداد معلوم کریں۔
   2. ڈیٹا میں سب سے زیادہ بولی جانے والی دس زبانیں نکالیں۔
   3. سب سے زیادہ آبادی والے دس ممالک نکالیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 9](./09_conditionals.md) | [فہرست](./readme.md) | [اگلا دن: 11](./11_functions.md)

</div>

<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 4 — سٹرنگز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../04_Day_Strings/04_strings.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 3](./03_operators.md) | [فہرست](./readme.md) | [اگلا دن: 5](./05_lists.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [دن 4](#day-4-section-1)
  - [سٹرنگز](#day-4-section-2)
    - [سٹرنگ بنانا](#day-4-section-3)
    - [سٹرنگز جوڑنا](#day-4-section-4)
    - [سٹرنگز میں ایسکیپ سیکوئنس](#day-4-section-5)
    - [سٹرنگ کی فارمیٹنگ](#day-4-section-6)
      - [پرانا انداز: فیصد آپریٹر](#day-4-section-7)
      - [نیا انداز: str.format](#day-4-section-8)
      - [سٹرنگ انٹرپولیشن: f-Strings، پائتھن 3.6 اور بعد](#day-4-section-9)
    - [پائتھن سٹرنگ بطور حروف کا سلسلہ](#day-4-section-10)
      - [حروف الگ متغیرات میں رکھنا](#day-4-section-11)
      - [انڈیکس سے حروف تک رسائی](#day-4-section-12)
      - [سٹرنگ کے حصے نکالنا](#day-4-section-13)
      - [سٹرنگ الٹنا](#day-4-section-14)
      - [سلائسنگ میں حروف چھوڑنا](#day-4-section-15)
    - [سٹرنگ میتھڈز](#day-4-section-16)
  - [💻 مشقیں — دن 4](#day-4-section-17)

<a id="day-4-section-1"></a>

# دن 4

<a id="day-4-section-2"></a>

## سٹرنگز

متن کی قسم کو سٹرنگ کہتے ہیں۔ سنگل، ڈبل یا تین اقتباسی نشانوں کے اندر لکھا ڈیٹا سٹرنگ ہوتا ہے۔ سٹرنگز کے لیے مختلف میتھڈ اور بلٹ اِن فنکشنز موجود ہیں۔ لمبائی معلوم کرنے کے لیے `len()` استعمال کریں۔

<a id="day-4-section-3"></a>

### سٹرنگ بنانا

<div dir="ltr">

```py
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
```

</div>

کئی سطروں کی سٹرنگ تین سنگل (`'''`) یا تین ڈبل (`"""`) اقتباسی نشانوں سے بنائی جاتی ہے۔

<div dir="ltr">

```py
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```

</div>

<a id="day-4-section-4"></a>

### سٹرنگز جوڑنا

دو یا زیادہ سٹرنگز کو ملانے کا عمل *concatenation* کہلاتا ہے۔

<div dir="ltr">

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```

</div>

<a id="day-4-section-5"></a>

### سٹرنگز میں ایسکیپ سیکوئنس

پائتھن اور دوسری زبانوں میں بیک سلیش `\` کے بعد مخصوص حرف ایک ایسکیپ سیکوئنس بناتا ہے۔ عام مثالیں:

- `\n`: نئی سطر۔
- `\t`: ٹیب؛ دکھائی دینے والی چوڑائی ماحول اور موجودہ مقام پر منحصر ہے۔
- `\\`: بیک سلیش۔
- `\'`: سنگل اقتباسی نشان۔
- `\"`: ڈبل اقتباسی نشان۔

ان کا استعمال مثالوں میں دیکھیں:

<div dir="ltr">

```py
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
I hope every one is enjoying the Python Challenge.
Are you ?
Days  Topics  Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

</div>

<a id="day-4-section-6"></a>

### سٹرنگ کی فارمیٹنگ

<a id="day-4-section-7"></a>

#### پرانا انداز: فیصد آپریٹر

پائتھن میں سٹرنگ کی فارمیٹنگ کے کئی طریقے ہیں۔ `%` آپریٹر ایک فارمیٹ سٹرنگ اور ٹپل میں دی گئی قدروں کو ملاتا ہے۔ فارمیٹ سٹرنگ میں عام متن کے ساتھ `%s`، `%d` اور `%f` جیسی علامتیں ہوتی ہیں۔

- `%s`: سٹرنگ یا کوئی آبجیکٹ جس کی متنی صورت بن سکے، مثلاً عدد۔
- `%d`: صحیح عدد۔
- `%f`: اعشاری عدد۔
- `%.nf`: اعشاری نقطے کے بعد `n` ہندسے؛ مثلاً `%.2f`۔

<div dir="ltr">

```py
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
```

</div>

<a id="day-4-section-8"></a>

#### نیا انداز: str.format

یہاں `str.format()` کا انداز استعمال کیا گیا ہے، جسے کورس پائتھن 3 کے تناظر میں متعارف کراتا ہے۔

<div dir="ltr">

```py

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

```

</div>

<a id="day-4-section-9"></a>

#### سٹرنگ انٹرپولیشن: f-Strings، پائتھن 3.6 اور بعد

ایک اور طریقہ f-string ہے۔ سٹرنگ کے شروع میں `f` لگائیں اور مطلوبہ جگہ پر گھنگریالی قوسین `{}` میں قدریں یا عبارتیں شامل کریں۔

<div dir="ltr">

```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

</div>

<a id="day-4-section-10"></a>

### پائتھن سٹرنگ بطور حروف کا سلسلہ

سٹرنگ حروف کا ترتیب وار سلسلہ ہے۔ اس کے عناصر تک رسائی لسٹ اور ٹپل جیسی ہے۔ حروف الگ کرنے کا ایک طریقہ انہیں الگ متغیرات میں *unpack* کرنا ہے۔

<a id="day-4-section-11"></a>

#### حروف الگ متغیرات میں رکھنا

<div dir="ltr">

```
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

</div>

<a id="day-4-section-12"></a>

#### انڈیکس سے حروف تک رسائی

پروگرامنگ میں انڈیکس صفر سے شروع ہوتا ہے۔ پہلے حرف کا انڈیکس `0` اور آخری کا سٹرنگ کی لمبائی سے ایک کم ہوتا ہے۔

![سٹرنگ کے انڈیکس](../images/string_index.png)

<div dir="ltr">

```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

</div>

آخر سے گننے کے لیے منفی انڈیکس استعمال کریں۔ `-1` آخری حرف ہے۔

<div dir="ltr">

```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

</div>

<a id="day-4-section-13"></a>

#### سٹرنگ کے حصے نکالنا

سلائسنگ سے سٹرنگ کا ایک حصہ، یعنی ذیلی سٹرنگ، حاصل کیا جا سکتا ہے۔

<div dir="ltr">

```py
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

</div>

<a id="day-4-section-14"></a>

#### سٹرنگ الٹنا

پائتھن میں سٹرنگ کی ترتیب آسانی سے الٹی کی جا سکتی ہے۔

<div dir="ltr">

```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

</div>

<a id="day-4-section-15"></a>

#### سلائسنگ میں حروف چھوڑنا

سلائس میں `step` دینے سے کچھ حروف چھوڑ کر آگے بڑھ سکتے ہیں۔

<div dir="ltr">

```py
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```

</div>

<a id="day-4-section-16"></a>

### سٹرنگ میتھڈز

سٹرنگز جانچنے اور فارمیٹ کرنے کے کئی میتھڈ ہیں:

- `capitalize()`: پہلے حرف کو بڑا اور باقی حروف کو چھوٹا کرتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```

</div>

- `count()`: ذیلی سٹرنگ کے آنے کی تعداد دیتا ہے۔ `count(substring, start, end)` میں آغاز شامل اور اختتام خارج ہوتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1,
print(challenge.count('th')) # 2`
```

</div>

- `endswith()`: جانچتا ہے کہ سٹرنگ مخصوص متن پر ختم ہوتی ہے یا نہیں۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

</div>

- `expandtabs()`: ٹیب کو خالی جگہوں میں بدلتا ہے۔ طے شدہ tab size `8` ہے؛ آرگیومنٹ سے اسے بدلا جا سکتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```

</div>

- `find()`: ذیلی سٹرنگ کا پہلا انڈیکس دیتا ہے؛ نہ ملے تو `-1`۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```

</div>

- `rfind()`: ذیلی سٹرنگ کا آخری انڈیکس دیتا ہے؛ نہ ملے تو `-1`۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
```

</div>

- `format()`: قدروں کو سٹرنگ کے مقررہ مقامات پر رکھتا ہے۔ مزید تفصیل اس [رابطے](https://www.programiz.com/python-programming/methods/string/format) پر ہے۔

<div dir="ltr">

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```

</div>

- `index()`: ذیلی سٹرنگ کا پہلا انڈیکس دیتا ہے۔ اختیاری آرگیومنٹ آغاز اور اختتام بتاتے ہیں؛ اختتام شامل نہیں ہوتا۔ نہ ملنے پر `ValueError` آتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
```

</div>

- `rindex()`: ذیلی سٹرنگ کا آخری انڈیکس دیتا ہے۔ آغاز اور اختتام بھی دے سکتے ہیں؛ نہ ملنے پر `ValueError` آتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19
```

</div>

- `isalnum()`: جانچتا ہے کہ سٹرنگ کے تمام حروف حروفِ تہجی یا اعداد ہیں۔

<div dir="ltr">

```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```

</div>

- `isalpha()`: جانچتا ہے کہ تمام عناصر حروفِ تہجی ہیں، مثلاً `a-z` اور `A-Z`۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```

</div>

- `isdecimal()`: جانچتا ہے کہ تمام حروف اعشاری ہندسے ہیں، مثلاً `0-9`۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
```

</div>

- `isdigit()`: ہندسوں کی جانچ کرتا ہے؛ `0-9` کے علاوہ بعض یونیکوڈ عددی حروف بھی قبول کرتا ہے۔

<div dir="ltr">

```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

</div>

- `isnumeric()`: عددی حروف اور `½` جیسی علامتیں بھی قبول کرتا ہے؛ اس کا دائرہ `isdigit()` سے وسیع ہے۔

<div dir="ltr">

```py
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

</div>

- `isidentifier()`: جانچتا ہے کہ سٹرنگ درست شناخت کنندہ بن سکتی ہے۔ مخصوص keyword ہونے کی جانچ الگ ہوتی ہے۔

<div dir="ltr">

```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

</div>

- `islower()`: جن حروف کی بڑی اور چھوٹی صورتیں ہوتی ہیں، ان سب کے چھوٹے ہونے کی جانچ کرتا ہے۔ سٹرنگ میں کم از کم ایک ایسا حرف ہونا ضروری ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```

</div>

- `isupper()`: جن حروف کی بڑی اور چھوٹی صورتیں ہوتی ہیں، ان سب کے بڑے ہونے کی جانچ کرتا ہے۔ سٹرنگ میں کم از کم ایک ایسا حرف ہونا ضروری ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

</div>

- `join()`: سٹرنگز کو جوڑ کر ایک سٹرنگ بناتا ہے۔

<div dir="ltr">

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
```

</div>

<div dir="ltr">

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

</div>

- `strip()`: سٹرنگ کے آغاز اور اختتام سے دیے گئے حروف ہٹاتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
```

</div>

- `replace()`: ذیلی سٹرنگ کو دوسرے متن سے بدلتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```

</div>

- `split()`: دیے گئے جداکار یا خالی جگہ کی بنیاد پر سٹرنگ تقسیم کرتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```

</div>

- `title()`: الفاظ کے ابتدائی حروف بڑے کرتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```

</div>

- `swapcase()`: بڑے حروف کو چھوٹا اور چھوٹے حروف کو بڑا کرتا ہے۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```

</div>

- `startswith()`: جانچتا ہے کہ سٹرنگ مخصوص متن سے شروع ہوتی ہے یا نہیں۔

<div dir="ltr">

```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```

</div>

🌕 آپ نے چوتھے دن کا چیلنج مکمل کر لیا! اب مشق کریں۔

<a id="day-4-section-17"></a>

## 💻 مشقیں — دن 4

1. `'Thirty'`، `'Days'`، `'Of'` اور `'Python'` کو جوڑ کر `'Thirty Days Of Python'` بنائیں۔
2. `'Coding'`، `'For'` اور `'All'` کو جوڑ کر `'Coding For All'` بنائیں۔
3. `company` بنائیں اور اسے `"Coding For All"` دیں۔
4. `print()` سے `company` دکھائیں۔
5. `len()` اور `print()` سے اس کی لمبائی دکھائیں۔
6. `upper()` سے تمام حروف بڑے کریں۔
7. `lower()` سے تمام حروف چھوٹے کریں۔
8. `Coding For All` پر `capitalize()`، `title()` اور `swapcase()` آزمائیں۔
9. سلائسنگ سے `Coding For All` کا پہلا لفظ نکالیں۔
10. `index()`، `find()` یا کسی دوسرے میتھڈ سے `Coding` کی موجودگی جانچیں۔
11. `'Coding For All'` میں `Coding` کو `Python` سے بدلیں۔
12. `replace()` یا کسی اور طریقے سے `"Python for Everyone"` کو `"Python for All"` بنائیں۔
13. `split()` سے `'Coding For All'` کو خالی جگہ پر تقسیم کریں۔
14. `"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"` کو کاما پر تقسیم کریں۔
15. `Coding For All` کے انڈیکس `0` پر کون سا حرف ہے؟
16. اس سٹرنگ کا آخری انڈیکس کیا ہے؟
17. انڈیکس `10` پر کون سا حرف ہے؟
18. `'Python For Everyone'` کے ابتدائی حروف سے مخفف بنائیں۔
19. `'Coding For All'` کا مخفف بنائیں۔
20. `index()` سے `Coding For All` میں پہلے `C` کا مقام معلوم کریں۔
21. اسی طرح پہلے `F` کا مقام معلوم کریں۔
22. `rfind()` سے `Coding For All People` میں آخری چھوٹے `l` کا مقام معلوم کریں۔
23. جملے `'You cannot end a sentence with because because because is a conjunction'` میں `index()` یا `find()` سے پہلے `because` کا مقام معلوم کریں۔
24. اسی جملے میں `rindex()` سے آخری `because` کا مقام معلوم کریں۔
25. اسی جملے سے `'because because because'` کا حصہ نکالیں۔
26. اسی جملے میں پہلے `because` کا مقام دوبارہ معلوم کریں۔
27. اسی جملے سے `'because because because'` کا حصہ دوبارہ نکالیں۔
28. کیا `'Coding For All'`، `Coding` سے شروع ہوتی ہے؟
29. کیا `'Coding For All'`، `coding` پر ختم ہوتی ہے؟
30. `'  Coding For All    '` کے دونوں سروں سے خالی جگہیں ہٹائیں۔
31. `isidentifier()` کس کے لیے `True` دے گا؟
    - `30DaysOfPython`
    - `thirty_days_of_python`
32. `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']` کو ہیش اور خالی جگہ (`'# '`) سے جوڑیں۔
33. نئی سطر کے ایسکیپ سیکوئنس سے یہ جملے الگ کریں:

<div dir="ltr">

```py
I am enjoying this challenge.
I just wonder what is next.
```

</div>

34. ٹیب ایسکیپ سیکوئنس سے یہ سطریں لکھیں:

<div dir="ltr">

```py
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
```

</div>

35. سٹرنگ فارمیٹنگ سے یہ نتیجہ دکھائیں:

<div dir="ltr">

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```

</div>

36. سٹرنگ فارمیٹنگ سے درج ذیل بنائیں:

<div dir="ltr">

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```

</div>

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 3](./03_operators.md) | [فہرست](./readme.md) | [اگلا دن: 5](./05_lists.md)

</div>

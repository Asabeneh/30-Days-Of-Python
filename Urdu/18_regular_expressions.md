<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 18 — ریگولر ایکسپریشنز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../18_Day_Regular_expressions/18_regular_expressions.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 17](./17_exception_handling.md) | [فہرست](./readme.md) | [اگلا دن: 19](./19_file_handling.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 18](#day-18-section-1)
  - [ریگولر ایکسپریشنز](#day-18-section-2)
    - [re ماڈیول](#day-18-section-3)
    - [re کے فنکشنز](#day-18-section-4)
      - [match](#day-18-section-5)
      - [search](#day-18-section-6)
      - [findall سے تمام مماثلتیں تلاش کرنا](#day-18-section-7)
      - [ذیلی سٹرنگ بدلنا](#day-18-section-8)
  - [RegEx سے متن تقسیم کرنا](#day-18-section-9)
  - [RegEx نمونے لکھنا](#day-18-section-10)
    - [مربع قوسین](#day-18-section-11)
    - [RegEx میں بیک سلیش](#day-18-section-12)
    - [ایک یا زیادہ بار: جمع کی علامت](#day-18-section-13)
    - [نقطہ](#day-18-section-14)
    - [صفر یا زیادہ بار: ستارہ](#day-18-section-15)
    - [صفر یا ایک بار: سوالیہ نشان](#day-18-section-16)
    - [تکرار کی تعداد مقرر کرنا](#day-18-section-17)
    - [کیرٹ کی علامت](#day-18-section-18)
  - [💻 مشقیں — دن 18](#day-18-section-19)
    - [مشقیں: درجہ 1](#day-18-section-20)
    - [مشقیں: درجہ 2](#day-18-section-21)
    - [مشقیں: درجہ 3](#day-18-section-22)

<a id="day-18-section-1"></a>

# 📘 دن 18

<a id="day-18-section-2"></a>

## ریگولر ایکسپریشنز

ریگولر ایکسپریشن، یا RegEx، متن میں نمونے تلاش کرنے والی مخصوص عبارت ہے۔ اس سے جانچ سکتے ہیں کہ کسی سٹرنگ میں مطلوبہ نمونہ موجود ہے یا نہیں۔ پائتھن میں اس کے لیے `re` ماڈیول امپورٹ کریں۔

<a id="day-18-section-3"></a>

### re ماڈیول

امپورٹ کے بعد نمونے تلاش کر سکتے ہیں۔

<div dir="ltr">

```py
import re
```

</div>

<a id="day-18-section-4"></a>

### re کے فنکشنز

مختلف علامتوں اور فنکشنز سے سٹرنگ میں مماثلت تلاش ہوتی ہے:

- `re.match()`: صرف سٹرنگ کے آغاز پر تلاش؛ مل جائے تو match آبجیکٹ، ورنہ `None`۔
- `re.search()`: سٹرنگ میں کہیں بھی پہلی مماثلت تلاش کرتا ہے، چاہے متن کئی سطروں کا ہو۔
- `re.findall()`: تمام مماثلتوں کی لسٹ دیتا ہے۔
- `re.split()`: مماثلت کے مقامات پر تقسیم کر کے لسٹ دیتا ہے۔
- `re.sub()`: ایک یا زیادہ مماثلتوں کو بدلتا ہے۔

<a id="day-18-section-5"></a>

#### match

<div dir="ltr">

```py
# syntax
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
```

</div>

<div dir="ltr">

```py
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0 15
substring = txt[start:end]
print(substring)       # I love to teach
```

</div>

یہاں نمونہ `I love to teach` ہے۔ `match()` **صرف** اسی وقت آبجیکٹ دے گا جب متن اس نمونے سے شروع ہو۔

<div dir="ltr">

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

</div>

سٹرنگ `I like to teach` سے شروع نہیں ہوتی، اس لیے `None` ملا۔

<a id="day-18-section-6"></a>

#### search

<div dir="ltr">

```py
# syntax
re.search(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag
```

</div>

<div dir="ltr">

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

</div>

پورے متن میں تلاش کرنی ہو تو `search()` موزوں ہے۔ یہ پہلی مماثلت کا آبجیکٹ دیتا ہے، ورنہ `None`۔ تمام مماثلتیں چاہیے ہوں تو `findall()` استعمال کریں۔

<a id="day-18-section-7"></a>

#### findall سے تمام مماثلتیں تلاش کرنا

`findall()` تمام نتائج کی لسٹ دیتا ہے۔

<div dir="ltr">

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

</div>

`language` دو بار ملا۔ اب `Python` اور `python` دونوں تلاش کریں۔

<div dir="ltr">

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

</div>

`re.I` چھوٹے اور بڑے حروف کا فرق نظر انداز کرتا ہے۔ یہ flag نہ ہو تو نمونہ اس طرح بدل سکتے ہیں:

<div dir="ltr">

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

</div>

<a id="day-18-section-8"></a>

#### ذیلی سٹرنگ بدلنا

<div dir="ltr">

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
```

</div>

اگلے متن میں `%` پڑھنے میں رکاوٹ ہے۔ اسے خالی سٹرنگ سے بدل کر متن صاف کریں۔

<div dir="ltr">

```py

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

</div>

<div dir="ltr">

```sh
I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?
```

</div>

<a id="day-18-section-9"></a>

## RegEx سے متن تقسیم کرنا

<div dir="ltr">

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol
```

</div>

<div dir="ltr">

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

</div>

<a id="day-18-section-10"></a>

## RegEx نمونے لکھنا

عام سٹرنگ سنگل یا ڈبل اقتباسی نشانوں میں لکھتے ہیں۔ RegEx کے لیے اکثر raw string، یعنی `r''`، استعمال کرتے ہیں۔ نیچے کا نمونہ صرف چھوٹے حروف والا `apple` پہچانتا ہے۔ حروف کی صورت نظر انداز کرنے کے لیے flag دیں یا نمونہ بدلیں۔

<div dir="ltr">

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```

</div>

- `[]`: حروف کا مجموعہ؛ `[a-c]` میں `a`، `b` یا `c`، `[a-z]` میں چھوٹے حروف، `[A-Z]` میں بڑے حروف، `[0-3]` میں صفر تا تین، `[0-9]` میں ہندسے اور `[A-Za-z0-9]` میں ان میں سے کوئی ایک حرف یا ہندسہ۔
- `\`: خاص علامت کا مخصوص مطلب بدلنے کے لیے؛ `\d` عددی ہندسے سے اور `\D` غیر عددی حرف سے ملتا ہے۔
- `.`: نئی سطر `\n` کے سوا کوئی ایک حرف، جب تک متعلقہ flag سے رویہ نہ بدلا جائے۔
- `^`: آغاز؛ `r'^love'` آغاز میں `love` تلاش کرتا ہے۔ مربع قوسین میں `r'[^abc]'` کا مطلب `a`، `b` اور `c` کے سوا کوئی حرف ہے۔
- `$`: اختتام؛ `r'love$'` آخر میں `love` تلاش کرتا ہے۔
- `*`: صفر یا زیادہ تکرار؛ `r'[a]*'` میں `a` نہ بھی ہو سکتا ہے یا کئی بار ہو سکتا ہے۔
- `+`: ایک یا زیادہ تکرار؛ `r'[a]+'` میں کم از کم ایک `a`۔
- `?`: صفر یا ایک تکرار؛ `r'[a]?'` میں `a` اختیاری ہے۔
- `{3}`: پچھلے نمونے کی بالکل تین تکرار۔
- `{3,}`: کم از کم تین تکرار۔
- `{3,8}`: تین سے آٹھ تکرار۔
- `|`: متبادل؛ `r'apple|banana'` میں apple یا banana۔
- `()`: گروپ بنانا اور مماثل حصہ محفوظ کرنا۔

![ریگولر ایکسپریشن کی مختصر رہنمائی](../images/regex.png)

اب ان علامتوں کو مثالوں سے سمجھیں۔

<a id="day-18-section-11"></a>

### مربع قوسین

چھوٹے اور بڑے دونوں حروف شامل کریں۔

<div dir="ltr">

```py
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

</div>

banana بھی تلاش کرنا ہو تو:

<div dir="ltr">

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

</div>

مربع قوسین اور متبادل کی علامت سے Apple، apple، Banana اور banana نکال لیے گئے۔

<a id="day-18-section-12"></a>

### RegEx میں بیک سلیش

<div dir="ltr">

```py
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
```

</div>

<a id="day-18-section-13"></a>

### ایک یا زیادہ بار: جمع کی علامت

<div dir="ltr">

```py
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!
```

</div>

<a id="day-18-section-14"></a>

### نقطہ

<div dir="ltr">

```py
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

</div>

<a id="day-18-section-15"></a>

### صفر یا زیادہ بار: ستارہ

نمونہ موجود نہ ہو یا کئی بار ہو، دونوں صورتیں قبول ہوتی ہیں۔

<div dir="ltr">

```py
regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

</div>

<a id="day-18-section-16"></a>

### صفر یا ایک بار: سوالیہ نشان

نمونہ اختیاری ہے؛ زیادہ سے زیادہ ایک بار۔

<div dir="ltr">

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

</div>

<a id="day-18-section-17"></a>

### تکرار کی تعداد مقرر کرنا

گھنگریالی قوسین سے تکرار کی تعداد مقرر کریں۔ مثلاً چار حروف والا حصہ تلاش کریں۔

<div dir="ltr">

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

</div>

<a id="day-18-section-18"></a>

### کیرٹ کی علامت

- آغاز جانچنا:

<div dir="ltr">

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

</div>

- حروف خارج کرنا:

<div dir="ltr">

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

</div>

<a id="day-18-section-19"></a>

## 💻 مشقیں — دن 18

<a id="day-18-section-20"></a>

### مشقیں: درجہ 1

1. اس پیراگراف میں سب سے زیادہ آنے والا لفظ کون سا ہے؟

<div dir="ltr">

```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

</div>

<div dir="ltr">

```sh
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

</div>

2. افقی محور پر ذرات کے مقامات منفی سمت میں `-12`، `-4`، `-3` اور `-1`، مبدا پر `0`، اور مثبت سمت میں `4` اور `8` ہیں۔ اس متن سے اعداد نکالیں اور سب سے دور دو ذرات کا فاصلہ معلوم کریں۔

<div dir="ltr">

```py
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20
```

</div>

<a id="day-18-section-21"></a>

### مشقیں: درجہ 2

1. ایسا نمونہ لکھیں جو جانچے کہ سٹرنگ درست پائتھن متغیر کا نام ہے۔

<div dir="ltr">

```sh
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
```

</div>

<a id="day-18-section-22"></a>

### مشقیں: درجہ 3

1. یہ متن صاف کریں، پھر سب سے زیادہ آنے والے تین الفاظ اور ان کی تعداد معلوم کریں۔

<div dir="ltr">

```py
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

print(clean_text(sentence));
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
```

</div>

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 17](./17_exception_handling.md) | [فہرست](./readme.md) | [اگلا دن: 19](./19_file_handling.md)

</div>

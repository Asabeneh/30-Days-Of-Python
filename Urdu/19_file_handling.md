<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 19 — فائلوں کے ساتھ کام</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../19_Day_File_handling/19_file_handling.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 18](./18_regular_expressions.md) | [فہرست](./readme.md) | [اگلا دن: 20](./20_python_package_manager.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 19](#day-19-section-1)
  - [فائلوں کے ساتھ کام کرنا](#day-19-section-2)
    - [پڑھنے کے لیے فائل کھولنا](#day-19-section-3)
    - [لکھنے اور اضافہ کرنے کے لیے فائل کھولنا](#day-19-section-4)
    - [فائلیں حذف کرنا](#day-19-section-5)
  - [فائلوں کی اقسام](#day-19-section-6)
    - [txt فائل](#day-19-section-7)
    - [json فائل](#day-19-section-8)
    - [JSON کو ڈکشنری میں بدلنا](#day-19-section-9)
    - [ڈکشنری کو JSON میں بدلنا](#day-19-section-10)
    - [JSON فائل محفوظ کرنا](#day-19-section-11)
    - [csv فائل](#day-19-section-12)
    - [xlsx فائل](#day-19-section-13)
    - [xml فائل](#day-19-section-14)
  - [💻 مشقیں — دن 19](#day-19-section-15)
    - [مشقیں: درجہ 1](#day-19-section-16)
    - [مشقیں: درجہ 2](#day-19-section-17)

<a id="day-19-section-1"></a>

# 📘 دن 19

<a id="day-19-section-2"></a>

## فائلوں کے ساتھ کام کرنا

ڈیٹا عام طور پر مختلف فائل فارمیٹس میں محفوظ ہوتا ہے۔ اس حصے میں فائلیں سنبھالنے کے ساتھ `.txt`، `.json`، `.xml`، `.csv`، `.tsv` اور Excel جیسے فارمیٹس دیکھیں گے۔ آغاز عام متنی فائل سے کریں۔

فائل ہینڈلنگ سے فائلیں بنا، پڑھ، بدل اور حذف کر سکتے ہیں۔ پائتھن کا بلٹ اِن `open()` اس کام کے لیے استعمال ہوتا ہے۔

<div dir="ltr">

```py
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
```

</div>

- `r`: پڑھنا؛ طے شدہ موڈ۔ فائل موجود نہ ہو تو خرابی۔
- `a`: آخر میں اضافہ؛ فائل موجود نہ ہو تو نئی بناتا ہے۔
- `w`: لکھنا؛ موجودہ مواد مٹا کر لکھتا ہے یا نئی فائل بناتا ہے۔
- `x`: صرف نئی فائل بنانا؛ پہلے سے موجود ہو تو خرابی۔
- `t`: متن؛ طے شدہ صورت۔
- `b`: بائنری ڈیٹا، مثلاً تصاویر۔

<a id="day-19-section-3"></a>

### پڑھنے کے لیے فائل کھولنا

طے شدہ موڈ پڑھنا ہے، اس لیے `r` یا `rt` لکھنا ضروری نہیں۔ `files` فولڈر کی `reading_file_example.txt` استعمال کریں۔

<div dir="ltr">

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

</div>

کھلی فائل کا آبجیکٹ دکھانے سے اس کی معلومات ملتی ہیں۔ پڑھنے کے طریقوں میں `read()`، `readline()` اور `readlines()` شامل ہیں۔ کام کے بعد `close()` سے فائل بند کریں۔

- `read()`: پورا متن سٹرنگ کے طور پر پڑھتا ہے۔ `read(number)` سے حروف کی تعداد محدود کر سکتے ہیں۔

<div dir="ltr">

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

</div>

<div dir="ltr">

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

</div>

اب صرف پہلے دس حروف دکھائیں۔

<div dir="ltr">

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

</div>

<div dir="ltr">

```sh
# output
<class 'str'>
This is an
```

</div>

- `readline()`: موجودہ مقام سے ایک سطر پڑھتا ہے؛ شروع میں ہو تو پہلی سطر۔

<div dir="ltr">

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

</div>

<div dir="ltr">

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
```

</div>

- `readlines()`: باقی سطروں کی لسٹ دیتا ہے۔

<div dir="ltr">

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

</div>

<div dir="ltr">

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

</div>

پورا متن پڑھ کر `splitlines()` سے بھی سطروں کی لسٹ بنا سکتے ہیں۔

<div dir="ltr">

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

</div>

<div dir="ltr">

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

</div>

فائل بند کرنا بھولنا آسان ہے۔ `with` استعمال کریں تو بلاک ختم ہونے پر فائل خود بند ہو جاتی ہے۔

<div dir="ltr">

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

</div>

<div dir="ltr">

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

</div>

<a id="day-19-section-4"></a>

### لکھنے اور اضافہ کرنے کے لیے فائل کھولنا

`open()` کو مناسب موڈ دیں:

- `a`: آخر میں اضافہ؛ ضرورت ہو تو نئی فائل۔
- `w`: موجودہ مواد کی جگہ نیا متن؛ ضرورت ہو تو نئی فائل۔

پہلے پڑھی ہوئی فائل کے آخر میں متن شامل کریں۔

<div dir="ltr">

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

</div>

یہ طریقہ فائل موجود نہ ہو تو نئی بناتا ہے:

<div dir="ltr">

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

</div>

<a id="day-19-section-5"></a>

### فائلیں حذف کرنا

پچھلے حصے میں `os` سے فولڈر بنانا اور ہٹانا دیکھا۔ فائل حذف کرنے کے لیے بھی `os` استعمال کریں۔

<div dir="ltr">

```py
import os
os.remove('./files/example.txt')

```

</div>

فائل موجود نہ ہو تو `remove()` خرابی دیتا ہے۔ پہلے جانچ سکتے ہیں:

<div dir="ltr">

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

</div>

<a id="day-19-section-6"></a>

## فائلوں کی اقسام

<a id="day-19-section-7"></a>

### txt فائل

`.txt` عام متنی فارمیٹ ہے جسے اوپر پڑھ چکے ہیں۔ اب JSON دیکھیں۔

<a id="day-19-section-8"></a>

### json فائل

JSON کا پورا نام JavaScript Object Notation ہے۔ یہ ڈیٹا کی متنی نمائندگی ہے؛ JSON آبجیکٹ کی ساخت JavaScript آبجیکٹ اور پائتھن ڈکشنری سے ملتی ہے۔

**مثال:**

<div dir="ltr">

```py
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

</div>

<a id="day-19-section-9"></a>

### JSON کو ڈکشنری میں بدلنا

`json` امپورٹ کر کے `loads()` استعمال کریں۔

<div dir="ltr">

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

</div>

<div dir="ltr">

```sh
# output
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

</div>

<a id="day-19-section-10"></a>

### ڈکشنری کو JSON میں بدلنا

`json.dumps()` استعمال کریں۔

<div dir="ltr">

```py
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
```

</div>

<div dir="ltr">

```sh
# output
# when you print it, it does not have the quote, but actually it is a string
# JSON does not have type, it is a string type.
<class 'str'>
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
```

</div>

<a id="day-19-section-11"></a>

### JSON فائل محفوظ کرنا

`json.dump()` سے ڈیٹا فائل میں لکھیں۔ اسے ڈیٹا، آؤٹ پٹ فائل، `ensure_ascii` اور `indent` جیسے آرگیومنٹ دیے جا سکتے ہیں۔

<div dir="ltr">

```py
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

</div>

انڈینٹیشن سے JSON پڑھنا آسان ہوتا ہے؛ encoding متن محفوظ کرنے کی صورت طے کرتی ہے۔

<a id="day-19-section-12"></a>

### csv فائل

CSV کا مطلب comma-separated values ہے۔ یہ جدول کی صورت میں ڈیٹا رکھنے کا سادہ فارمیٹ ہے، مثلاً اسپریڈشیٹ یا ڈیٹابیس کا ڈیٹا۔ ڈیٹا سائنس میں عام ہے۔

**مثال:**

<div dir="ltr">

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

</div>

**مثال:**

<div dir="ltr">

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

</div>

<div dir="ltr">

```sh
# output:
Column names are :name, country, city, skills
Number of lines:  1
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines:  2
```

</div>

<a id="day-19-section-13"></a>

### xlsx فائل

اصل سبق Excel پڑھنے کے لیے `xlrd` دکھاتا ہے۔ پیکیج انسٹال کرنا اگلے حصے میں پڑھیں گے۔ یہ پرانے کورس کی مثال ہے؛ جدید `xlrd` میں `.xlsx` کی معاونت نہیں، اس لیے اصل مثال کے ورژن اور فارمیٹ کا خیال رکھیں۔

<div dir="ltr">

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

</div>

<a id="day-19-section-14"></a>

### xml فائل

XML ساخت رکھنے والا ڈیٹا فارمیٹ ہے جو HTML جیسا دکھتا ہے۔ اس کے ٹیگ پہلے سے مقرر نہیں ہوتے۔ پہلی سطر XML declaration ہے، `person` جڑ کا عنصر اور `gender` اس کا وصف ہے۔

**مثال: XML**

<div dir="ltr">

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

</div>

مزید کے لیے اصل سبق میں دیا گیا [دستاویز کا رابطہ](https://docs.python.org/2/library/xml.etree.elementtree.html) دیکھیں؛ یہ پائتھن 2 کی دستاویز ہے۔

<div dir="ltr">

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```

</div>

<div dir="ltr">

```sh
# output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

</div>

🌕 آپ نے انیسویں دن کا سبق مکمل کر لیا! اب مشق کریں۔

<a id="day-19-section-15"></a>

## 💻 مشقیں — دن 19

<a id="day-19-section-16"></a>

### مشقیں: درجہ 1

1. متن کی سطریں اور الفاظ گننے والا فنکشن بنائیں۔ ڈیٹا فولڈر کی یہ فائلیں پڑھیں:
   1. `obama_speech.txt`
   2. `michelle_obama_speech.txt`
   3. `donald_speech.txt`
   4. `melina_trump_speech.txt`
2. `countries_data.json` پڑھ کر سب سے زیادہ بولی جانے والی دس زبانیں معلوم کرنے والا فنکشن بنائیں۔

<div dir="ltr">

```py
# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
```

</div>

3. اسی فائل سے سب سے زیادہ آبادی والے دس ممالک کی لسٹ بنائیں۔

<div dir="ltr">

```py
# Your output should look like this
print(most_populated_countries(filename='./data/countries_data.json', 10))

[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000},
{'country': 'Indonesia', 'population': 258705000},
{'country': 'Brazil', 'population': 206135893},
{'country': 'Pakistan', 'population': 194125062},
{'country': 'Nigeria', 'population': 186988000},
{'country': 'Bangladesh', 'population': 161006790},
{'country': 'Russian Federation', 'population': 146599183},
{'country': 'Japan', 'population': 126960000}
]

# Your output should look like this

print(most_populated_countries(filename='./data/countries_data.json', 3))
[
{'country': 'China', 'population': 1377422166},
{'country': 'India', 'population': 1295210000},
{'country': 'United States of America', 'population': 323947000}
]
```

</div>

<a id="day-19-section-17"></a>

### مشقیں: درجہ 2

1. `email_exchange_big.txt` سے آنے والی ای میلز کے پتے نکال کر لسٹ بنائیں۔
2. `find_most_common_words` بنائیں جو متن یا فائل اور ایک مثبت صحیح عدد لے۔ عام ترین الفاظ کی اتنی تعداد گھٹتی ترتیب کے ٹپلز میں دے۔

<div dir="ltr">

```py
    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

</div>

3. لفظوں کی تکرار والے فنکشن سے ان تقاریر کے دس سب سے عام الفاظ نکالیں؛ اصل سوال اسے `find_most_frequent_words` بھی کہتا ہے:
   1. [اوباما کی تقریر](../data/obama_speech.txt)
   2. [مشیل کی تقریر](../data/michelle_obama_speech.txt)
   3. [ٹرمپ کی تقریر](../data/donald_speech.txt)
   4. [میلانیا کی تقریر](../data/melina_trump_speech.txt)
4. دو متون کی مماثلت جانچنے والی ایپلی کیشن بنائیں۔ مثلاً [مشیل](../data/michelle_obama_speech.txt) اور [میلانیا](../data/melina_trump_speech.txt) کی تقاریر کا موازنہ کریں۔ `clean_text`، `remove_support_words` اور `check_text_similarity` جیسے فنکشن مدد دے سکتے ہیں۔ [stop_words.py](../data/stop_words.py) ڈیٹا فولڈر میں ہے۔
5. `romeo_and_juliet.txt` کے دس سب سے زیادہ دہرائے گئے الفاظ معلوم کریں۔
6. [hacker_news.csv](../data/hacker_news.csv) پڑھ کر:
   1. `python` یا `Python` والی سطریں گنیں۔
   2. `JavaScript`، `javascript` یا `Javascript` والی سطریں گنیں۔
   3. `Java` والی مگر `JavaScript` کے بغیر سطریں گنیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 18](./18_regular_expressions.md) | [فہرست](./readme.md) | [اگلا دن: 20](./20_python_package_manager.md)

</div>

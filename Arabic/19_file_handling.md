<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 19 - معالجة الملفات</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="متابعة في تويتر" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>المؤلف:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>الطبعة الثانية: يوليو 2021</small>
  </sub>
</div>

[<< اليوم 18](./18_regular_expressions.md) | [اليوم 20 >>](./20_python_package_manager.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 19](#-اليوم-19)
  - [معالجة الملفات](#معالجة-الملفات)
    - [فتح الملفات للقراءة](#فتح-الملفات-للقراءة)
    - [فتح الملفات للكتابة والتحديث](#فتح-الملفات-للكتابة-والتحديث)
    - [حذف الملفات](#حذف-الملفات)
  - [أنواع الملفات](#أنواع-الملفات)
    - [ملف بامتداد txt](#ملف-بامتداد-txt)
    - [ملف بامتداد json](#ملف-بامتداد-json)
    - [تحويل JSON إلى قاموس](#تحويل-json-إلى-قاموس)
    - [تحويل القاموس إلى JSON](#تحويل-القاموس-إلى-json)
    - [الحفظ كملف JSON](#الحفظ-كملف-json)
    - [ملف بامتداد csv](#ملف-بامتداد-csv)
    - [ملف بامتداد xlsx](#ملف-بامتداد-xlsx)
    - [ملف بامتداد xml](#ملف-بامتداد-xml)
  - [💻 تمارين: اليوم 19](#-تمارين-اليوم-19)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 19

## معالجة الملفات

لقد رأينا حتى الآن أنواع بيانات بايثون المختلفة. عادةً ما نخزن بياناتنا في صيغ ملفات مختلفة. بالإضافة إلى معالجة الملفات، سنرى أيضًا صيغ ملفات مختلفة (.txt، .json، .xml، .csv، .tsv، .excel) في هذا القسم. أولاً، دعنا نتعرف على معالجة الملفات بصيغة الملف الشائعة (.txt).

معالجة الملفات هي جزء مهم من البرمجة تسمح لنا بإنشاء وقراءة وتحديث وحذف الملفات. في بايثون، لمعالجة البيانات نستخدم الدالة المضمنة 'open()'.

```py
# صيغة
open('filename', mode) # الوضع (r, a, w, x, t, b) يمكن أن يكون للقراءة أو الكتابة أو التحديث
```

- "r" - قراءة - القيمة الافتراضية. يفتح ملفًا للقراءة، يعيد خطأ إذا لم يكن الملف موجودًا
- "a" - إلحاق - يفتح ملفًا للإلحاق، ينشئ الملف إذا لم يكن موجودًا
- "w" - كتابة - يفتح ملفًا للكتابة، ينشئ الملف إذا لم يكن موجودًا
- "x" - إنشاء - ينشئ الملف المحدد، يعيد خطأ إذا كان الملف موجودًا
- "t" - نص - القيمة الافتراضية. وضع النص
- "b" - ثنائي - الوضع الثنائي (مثل الصور)

### فتح الملفات للقراءة

الوضع الافتراضي لدالة 'open' هو القراءة، لذا لا نحتاج إلى تحديد 'r' أو 'rt'. لقد أنشأت وحفظت ملفًا باسم 'reading_file_example.txt' في مجلد 'files'. دعنا نرى كيف يتم ذلك:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

كما ترى في المثال أعلاه، قمت بطباعة الملف المفتوح وأعطاني بعض المعلومات عنه. الملف المفتوح له طرق قراءة مختلفة: 'read()'، 'readline'، 'readlines'. يجب إغلاق الملف المفتوح بطريقة 'close()'.

- 'read()': يقرأ النص بالكامل كنص. إذا أردنا تحديد عدد الأحرف التي نريد قراءتها، يمكننا تحديدها بتمرير قيمة صحيحة لطريقة 'read(number)'.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# المخرجات
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

بدلاً من طباعة كل النص، دعنا نطبع أول 10 أحرف من ملف النص.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# المخرجات
<class 'str'>
This is an
```

- 'readline()': يقرأ السطر الأول فقط

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# المخرجات
<class 'str'>
This is an example to show how to open a file and read.
```

- 'readlines()': يقرأ كل النص سطرًا سطرًا ويعيد قائمة بأسطر

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# المخرجات
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

طريقة أخرى للحصول على جميع الأسطر كقائمة هي استخدام 'splitlines()':

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# المخرجات
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

بعد فتح ملف، يجب إغلاقه. هناك احتمال كبير أن ننسى إغلاقه. هناك طريقة جديدة لفتح الملفات باستخدام 'with' - تُغلق الملفات تلقائيًا. دعنا نعيد كتابة المثال السابق بطريقة 'with':

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# المخرجات
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### فتح الملفات للكتابة والتحديث

للكتابة في ملف موجود، يجب إضافة وضع كوسيلة للدالة 'open()':

- "a" - إلحاق - سيلحق في نهاية الملف، إذا لم يكن الملف موجودًا سيُنشئ ملفًا جديدًا.
- "w" - كتابة - سيُكتب فوق أي محتوى موجود، إذا لم يكن الملف موجودًا سيُنشئه.

دعنا نلحق بعض النصوص بالملف الذي كنا نقرأه:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

الطريقة التالية تنشئ ملفًا جديدًا، إذا لم يكن الملف موجودًا:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### حذف الملفات

لقد رأينا في القسم السابق كيفية إنشاء وإزالة دليل باستخدام وحدة 'os'. مرة أخرى الآن، إذا أردنا إزالة ملف نستخدم وحدة 'os'.

```py
import os
os.remove('./files/example.txt')

```

إذا لم يكن الملف موجودًا، سترفع طريقة Remove خطأ، لذا من الجيد استخدام شرط كهذا:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## أنواع الملفات

### ملف بامتداد txt

ملف بامتداد 'txt' هو صيغة بيانات شائعة جدًا وقد غطيناه في القسم السابق. دعنا ننتقل إلى ملف 'JSON'.

### ملف بامتداد json

'JSON' يرمز لـ 'JavaScript Object Notation'. في الواقع، هو كائن 'JavaScript' مُحوَّل إلى نص أو قاموس بايثون.

**مثال:**

```py
# قاموس
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: نص يمثل قاموس
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# نستخدم ثلاثة اقتباسات ونجعله متعدد الأسطر لجعله أسهل في القراءة
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### تحويل JSON إلى قاموس

لتحويل 'JSON' إلى قاموس، نستورد أولاً وحدة 'json' ثم نستخدم طريقة 'loads'.

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# لنحول JSON إلى قاموس
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# المخرجات
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### تحويل القاموس إلى JSON

لتحويل قاموس إلى 'JSON' نستخدم طريقة 'dumps' من وحدة 'json'.

```py
import json
# قاموس بايثون
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# لنحوّله إلى json
person_json = json.dumps(person, indent=4) # indent يمكن أن يكون 2 أو 4 أو 8. يجعل 'json' أسهل في القراءة
print(type(person_json))
print(person_json)
```

```sh
# المخرجات
# عند طباعته، لا يحتوي على علامات اقتباس، لكنه في الواقع نص
# JSON لا يحتوي على نوع، إنه نوع نص.
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

### الحفظ كملف JSON

يمكننا أيضًا حفظ بياناتنا كملف 'json'. دعنا نحفظه كملف 'json' باستخدام الخطوات التالية. لكتابة ملف 'json'، نستخدم طريقة 'json.dump()'، يمكنها أخذ قاموس وملف الإخراج و'ensure_ascii' و'indent'.

```py
import json
# قاموس بايثون
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

في الكود أعلاه، نستخدم الترميز والمسافة البادئة. المسافة البادئة تجعل ملف 'json' أسهل في القراءة.

### ملف بامتداد csv

'CSV' يرمز لـ 'Comma Separated Values'. 'CSV' هو صيغة ملف بسيطة تُستخدم لتخزين البيانات الجدولية، مثل جدول بيانات أو قاعدة بيانات. 'CSV' هو صيغة بيانات شائعة جدًا في علوم البيانات.

**مثال:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**مثال:**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # نستخدم طريقة reader لقراءة csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'أسماء الأعمدة هي: {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} معلم. يعيش في {row[1]}, {row[2]}.')
            line_count += 1
    print(f'عدد الأسطر: {line_count}')
```

```sh
# المخرجات:
أسماء الأعمدة هي: name, country, city, skills
عدد الأسطر:  1
        Asabeneh معلم. يعيش في Finland, Helsinki.
عدد الأسطر:  2
```

### ملف بامتداد xlsx

لقراءة ملفات 'Excel' نحتاج إلى تثبيت حزمة 'xlrd'. سنغطي هذا بعد تغطية تثبيت الحزم باستخدام 'pip'.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### ملف بامتداد xml

'XML' هو صيغة بيانات منظمة أخرى تبدو مثل 'HTML'. في 'XML' العلامات غير محددة مسبقًا. السطر الأول هو إعلان 'XML'. علامة 'person' هي جذر 'XML'. 'person' لها سمة 'gender'.

**مثال: XML**

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

لمزيد من المعلومات حول كيفية قراءة ملف XML تحقق من [التوثيق](https://docs.python.org/2/library/xml.etree.elementtree.html)

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```

```sh
# المخرجات
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

🌕 أنت تحقق تقدمًا كبيرًا. حافظ على زخمك، واصل العمل الجيد. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 19

### تمارين: المستوى 1

1. اكتب دالة تعد عدد الأسطر وعدد الكلمات في نص. جميع الملفات في مجلد data:
   1) اقرأ ملف obama_speech.txt وعد عدد الأسطر والكلمات
   2) اقرأ ملف michelle_obama_speech.txt وعد عدد الأسطر والكلمات
   3) اقرأ ملف donald_speech.txt وعد عدد الأسطر والكلمات
   4) اقرأ ملف melina_trump_speech.txt وعد عدد الأسطر والكلمات
2. اقرأ ملف بيانات countries_data.json في مجلد data، أنشئ دالة تجد أكثر عشر لغات تحدثًا

   ```py
   # يجب أن تبدو مخرجاتك هكذا
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

   # يجب أن تبدو مخرجاتك هكذا
   print(most_spoken_languages(filename='./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. اقرأ ملف بيانات countries_data.json في مجلد data، أنشئ دالة تنشئ قائمة بأكثر عشر دول كثافة سكانية

   ```py
   # يجب أن تبدو مخرجاتك هكذا
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

   # يجب أن تبدو مخرجاتك هكذا

   print(most_populated_countries(filename='./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

### تمارين: المستوى 2

1. استخرج جميع عناوين البريد الإلكتروني الواردة كقائمة من ملف email_exchange_big.txt.
2. ابحث عن أكثر الكلمات شيوعًا في اللغة الإنجليزية. اسم دالتك find_most_common_words، ستأخذ وسيلتين - نصًا أو ملفًا وعددًا صحيحًا موجبًا، يشير إلى عدد الكلمات. ستعيد دالتك مصفوفة توبل بترتيب تنازلي. تحقق من المخرجات

```py
    # يجب أن تبدو مخرجاتك هكذا
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

    # يجب أن تبدو مخرجاتك هكذا
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. استخدم الدالة find_most_frequent_words للعثور على:
   1) أكثر عشر كلمات تكرارًا في [خطاب أوباما](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   2) أكثر عشر كلمات تكرارًا في [خطاب ميشيل](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   3) أكثر عشر كلمات تكرارًا في [خطاب ترمب](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   4) أكثر عشر كلمات تكرارًا في [خطاب ميلينا](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
4. اكتب تطبيق بايثون يتحقق من التشابه بين نصين. يأخذ نصًا أو ملفًا كوسيلة ويقيّم تشابه النصين. على سبيل المثال تحقق من التشابه بين نصي [ميشيل](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) و [ميلينا](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt). قد تحتاج إلى دالتين، دالة لتنظيف النص ('clean_text') ودالة لإزالة كلمات الدعم ('remove_support_words') وأخيرًا للتحقق من التشابه ('check_text_similarity'). قائمة [كلمات التوقف](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) موجودة في مجلد data
5. ابحث عن أكثر 10 كلمات تكرارًا في romeo_and_juliet.txt
6. اقرأ [ملف hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) واكتشف:
   1) عدد الأسطر التي تحتوي على python أو Python
   2) عدد الأسطر التي تحتوي على JavaScript أو javascript أو Javascript
   3) عدد الأسطر التي تحتوي على Java وليست JavaScript

🎉 مبروك! 🎉

[<< اليوم 18](./18_regular_expressions.md) | [اليوم 20 >>](./20_python_package_manager.md)
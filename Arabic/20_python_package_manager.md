<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 20 - PIP</h1>
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

[<< اليوم 19](./19_file_handling.md) | [اليوم 21 >>](./21_classes_and_objects.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 20](#-اليوم-20)
  - [PIP في بايثون - مدير حزم بايثون](#pip-في-بايثون---مدير-حزم-بايثون)
    - [ما هو PIP؟](#ما-هو-pip)
    - [تثبيت PIP](#تثبيت-pip)
    - [تثبيت الحزم باستخدام pip](#تثبيت-الحزم-باستخدام-pip)
    - [إلغاء تثبيت الحزم](#إلغاء-تثبيت-الحزم)
    - [قائمة الحزم](#قائمة-الحزم)
    - [عرض الحزمة](#عرض-الحزمة)
    - [PIP Freeze](#pip-freeze)
    - [القراءة من URL](#القراءة-من-url)
    - [إنشاء حزمة](#إنشاء-حزمة)
    - [مزيد من المعلومات حول الحزم](#مزيد-من-المعلومات-حول-الحزم)
  - [💻 تمارين: اليوم 20](#-تمارين-اليوم-20)

# 📘 اليوم 20

## PIP في بايثون - مدير حزم بايثون

### ما هو PIP؟

'PIP' يرمز لـ 'Preferred Installer Program'. نستخدم 'pip' لتثبيت حزم بايثون المختلفة.
الحزمة هي وحدة بايثون يمكن أن تحتوي على وحدة واحدة أو أكثر أو حزم أخرى. الوحدة أو الوحدات التي يمكننا تثبيتها في تطبيقنا هي حزمة.
في البرمجة، لا نضطر إلى برمجة كل أداة بأنفسنا، بل نثبّت الحزم ونستوردها إلى تطبيقاتنا.

### تثبيت PIP

إذا لم تكن قد ثبّت 'pip'، دعنا نثبّته الآن. اذهب إلى الطرفية أو موجه الأوامر وانسخ والصق هذا:

```sh
asabeneh@Asabeneh:~$ pip install pip
```

تحقق مما إذا كان 'pip' مثبتًا بكتابة

```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

كما ترى، أنا أستخدم إصدار 'pip' 21.1.3، إذا رأيت رقمًا أقل أو أعلى قليلًا، فهذا يعني أن 'pip' مثبت لديك.

دعنا نتحقق من بعض الحزم المستخدمة في مجتمع بايثون لأغراض مختلفة. فقط لنعلمك أن هناك الكثير من الحزم المتاحة للاستخدام مع تطبيقات مختلفة.

### تثبيت الحزم باستخدام pip

دعنا نحاول تثبيت 'numpy'، أي 'numeric python'. إنها واحدة من أكثر الحزم شعبية في مجتمع التعلم الآلي وعلم البيانات.

- 'NumPy' هي الحزمة الأساسية للحوسبة العلمية مع بايثون. تحتوي من بين أشياء أخرى على:
  - كائن مصفوفة متعدد الأبعاد قوي
  - دوال متطورة ('broadcasting')
  - أدوات لتكامل كود 'C/C++' و 'Fortran'
  - قدرات مفيدة في الجبر الخطي وتحويل فورييه والأرقام العشوائية

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

دعنا نبدأ باستخدام 'numpy'. افتح شل بايثون التفاعلي، اكتب 'python' ثم استورد 'numpy' كما يلي:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>
```

'Pandas' هي مكتبة مفتوحة المصدر مرخصة بـ 'BSD' توفر هياكل بيانات عالية الأداء وسهلة الاستخدام وأدوات تحليل بيانات للغة برمجة بايثون. دعنا نثبت الأخ الأكبر لـ 'numpy'، وهو 'pandas':

```sh
asabeneh@Asabeneh:~$ pip install pandas
```

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

هذا القسم ليس عن 'numpy' ولا 'pandas'، هنا نحاول تعلم كيفية تثبيت الحزم وكيفية استيرادها. إذا لزم الأمر، سنتحدث عن حزم مختلفة في أقسام أخرى.

دعنا نستورد وحدة متصفح الويب، التي يمكن أن تساعدنا في فتح أي موقع ويب. لا نحتاج إلى تثبيت هذه الوحدة، إنها مثبتة بالفعل بشكل افتراضي مع بايثون 3. على سبيل المثال إذا كنت ترغب في فتح أي عدد من المواقع في أي وقت أو إذا كنت ترغب في جدولة شيء ما، يمكن استخدام وحدة 'webbrowser' هذه.

```py
import webbrowser # وحدة متصفح الويب لفتح المواقع

# قائمة عناوين url: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# يفتح قائمة المواقع أعلاه في علامة تبويب مختلفة
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### إلغاء تثبيت الحزم

إذا كنت لا ترغب في الاحتفاظ بالحزم المثبتة، يمكنك إزالتها باستخدام الأمر التالي.

```sh
pip uninstall packagename
```

### قائمة الحزم

لرؤية الحزم المثبتة على جهازنا، يمكننا استخدام 'pip' متبوعًا بـ 'list'.

```sh
pip list
```

### عرض الحزمة

لعرض معلومات حول حزمة

```sh
pip show packagename
```

```sh
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

إذا أردنا المزيد من التفاصيل، فقط أضف '--verbose'

```sh
asabeneh@Asabeneh:~$ pip show --verbose pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

'pip freeze' ينشئ قائمة بحزم بايثون المثبتة مع إصداراتها، ومخرجات مناسبة للاستخدام في ملف متطلبات. ملف 'requirements.txt' هو ملف يجب أن يحتوي على جميع حزم بايثون المثبتة في مشروع بايثون.

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

أعطانا 'pip freeze' الحزم المستخدمة والمثبتة وإصداراتها. نستخدمه مع ملف 'requirements.txt' للنشر.

### القراءة من URL

بحلول الآن أصبحت معتادًا على كيفية القراءة أو الكتابة على ملف موجود على جهازك المحلي. أحيانًا، نرغب في القراءة من موقع ويب باستخدام 'url' أو من 'API'.
'API' يرمز لـ 'Application Program Interface'. إنها وسيلة لتبادل البيانات المنظمة بين الخوادم بشكل أساسي كبيانات 'json'. لفتح اتصال شبكة، نحتاج إلى حزمة تسمى 'requests' - تسمح بفتح اتصال شبكة وتنفيذ عمليات 'CRUD' (إنشاء، قراءة، تحديث، حذف). في هذا القسم، سنغطي فقط جزء القراءة أو الحصول من 'CRUD'.

دعنا نثبت 'requests':

```py
asabeneh@Asabeneh:~$ pip install requests
```

سنرى طرق 'get' و 'status_code' و 'headers' و 'text' و 'json' في وحدة 'requests':
  - 'get()': لفتح شبكة وجلب البيانات من 'url' - يعيد كائن استجابة
  - 'status_code': بعد جلب البيانات، يمكننا التحقق من حالة العملية (نجاح، خطأ، إلخ)
  - 'headers': للتحقق من أنواع الترويسة
  - 'text': لاستخراج النص من كائن الاستجابة الذي تم جلبه
  - 'json': لاستخراج بيانات 'json'
دعنا نقرأ ملف 'txt' من هذا الموقع، https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # استيراد وحدة requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # نص من موقع ويب

response = requests.get(url) # فتح شبكة وجلب البيانات
print(response)
print(response.status_code) # رمز الحالة، النجاح:200
print(response.headers)     # معلومات الترويسات
print(response.text) # يعطي كل النص من الصفحة
```

```sh
<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

- دعنا نقرأ من 'API'. 'API' يرمز لـ 'Application Program Interface'. إنها وسيلة لتبادل البيانات المنظمة بين الخوادم بشكل أساسي كبيانات 'json'. مثال على 'API': https://restcountries.eu/rest/v2/all. دعنا نقرأ هذا الـ 'API' باستخدام وحدة 'requests'.

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # api الدول
response = requests.get(url)  # فتح شبكة وجلب البيانات
print(response) # كائن الاستجابة
print(response.status_code)  # رمز الحالة، النجاح:200
countries = response.json()
print(countries[:1])  # قمنا بقص أول دولة فقط، أزل القص لرؤية جميع الدول
```

```sh
<Response [200]>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
```

نستخدم طريقة 'json()' من كائن الاستجابة، إذا كنا نجلب بيانات 'JSON'. بالنسبة لـ 'txt' و 'html' و 'xml' وصيغ ملفات أخرى يمكننا استخدام 'text'.

### إنشاء حزمة

ننظم عددًا كبيرًا من الملفات في مجلدات ومجلدات فرعية مختلفة بناءً على معايير معينة، حتى نتمكن من العثور عليها وإدارتها بسهولة. كما تعلم، يمكن أن تحتوي الوحدة على كائنات متعددة، مثل الفئات والدوال وما إلى ذلك. يمكن أن تحتوي الحزمة على وحدة واحدة أو أكثر ذات صلة. الحزمة هي في الواقع مجلد يحتوي على ملف أو أكثر من ملفات الوحدات. دعنا ننشئ حزمة باسم 'mypackage'، باستخدام الخطوات التالية:

أنشئ مجلدًا جديدًا باسم 'mypackage' داخل مجلد '30DaysOfPython'
أنشئ ملف **__init__**.py فارغًا في مجلد 'mypackage'.
أنشئ وحدتي 'arithmetic.py' و 'greet.py' بالكود التالي:

```py
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
```

```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```

يجب أن يبدو هيكل مجلد الحزمة هكذا:

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

الآن دعنا نفتح شل بايثون التفاعلي ونجرب الحزمة التي أنشأناها:

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Asabeneh', 'Yetayeh')
'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'
>>>
```

كما ترى حزمتنا تعمل بشكل مثالي. يحتوي مجلد الحزمة على ملف خاص يسمى **__init__**.py - يخزن محتوى الحزمة. إذا وضعنا **__init__**.py في مجلد الحزمة، يبدأ بايثون في التعرف عليها كحزمة.
يكشف **__init__**.py الموارد المحددة من وحداته ليتم استيرادها إلى ملفات بايثون أخرى. ملف **__init__**.py الفارغ يجعل جميع الدوال متاحة عند استيراد حزمة. **__init__**.py ضروري للتعرف على المجلد كحزمة من قبل بايثون.

### مزيد من المعلومات حول الحزم

- قواعد البيانات
  - 'SQLAlchemy' أو 'SQLObject' - وصول كائني التوجه للعديد من أنظمة قواعد البيانات المختلفة
    - 'pip install SQLAlchemy'
- تطوير الويب
  - 'Django' - إطار عمل ويب عالي المستوى.
    - 'pip install django'
  - 'Flask' - إطار عمل صغير لبايثون مبني على 'Werkzeug' و 'Jinja 2'. (مرخص بـ 'BSD')
    - 'pip install flask'
- محلل HTML
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - محلل 'HTML/XML' مصمم لمشاريع سريعة مثل 'screen-scraping'، يقبل الترميز السيئ.
    - 'pip install beautifulsoup4'
  - 'PyQuery' - ينفذ 'jQuery' في بايثون؛ أسرع من 'BeautifulSoup'، كما يبدو.

- معالجة XML
  - 'ElementTree' - نوع 'Element' هو كائن حاوٍ بسيط ولكنه مرن، مصمم لتخزين هياكل بيانات هرمية، مثل معلومات 'XML' المبسطة، في الذاكرة. --ملاحظة: بايثون 2.5 وما فوق يحتوي على 'ElementTree' في المكتبة القياسية
- واجهات المستخدم الرسومية
  - 'PyQt' - روابط لإطار عمل 'Qt' متعدد المنصات.
  - 'TkInter' - مجموعة أدوات واجهة مستخدم بايثون التقليدية.
- تحليل البيانات وعلم البيانات والتعلم الآلي
  - 'Numpy': 'Numpy' ('numeric python') معروف كواحدة من أكثر مكتبات التعلم الآلي شعبية في بايثون.
  - 'Pandas': هي مكتبة تحليل بيانات وعلم بيانات وتعلم آلي في بايثون توفر هياكل بيانات عالية المستوى ومجموعة واسعة من أدوات التحليل.
  - 'SciPy': 'SciPy' هي مكتبة تعلم آلي لمطوري التطبيقات والمهندسين. تحتوي مكتبة 'SciPy' على وحدات للتحسين والجبر الخطي والتكامل ومعالجة الصور والإحصاء.
  - 'Scikit-Learn': إنها 'NumPy' و 'SciPy'. تعتبر واحدة من أفضل المكتبات للعمل مع البيانات المعقدة.
  - 'TensorFlow': هي مكتبة تعلم آلي بنتها 'Google'.
  - 'Keras': تعتبر واحدة من أروع مكتبات التعلم الآلي في بايثون. توفر آلية أسهل للتعبير عن الشبكات العصبية. توفر 'Keras' أيضًا بعضًا من أفضل الأدوات لتجميع النماذج ومعالجة مجموعات البيانات وتصور الرسوم البيانية والمزيد.
- الشبكات:
  - 'requests': هي حزمة يمكننا استخدامها لإرسال طلبات إلى خادم ('GET'، 'POST'، 'DELETE'، 'PUT')
    - 'pip install requests'

🌕 أنت تتقدم دائمًا وأنت متقدم بـ 20 خطوة في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 20

1. اقرأ هذا 'url' وابحث عن أكثر 10 كلمات تكرارًا. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
2. اقرأ API القطط cats_api = 'https://api.thecatapi.com/v1/breeds' وابحث عن:
   1. الحد الأدنى والحد الأقصى والمتوسط والوسيط والانحراف المعياري لوزن القطط في الوحدات المترية.
   2. الحد الأدنى والحد الأقصى والمتوسط والوسيط والانحراف المعياري لعمر القطط بالسنوات.
   3. أنشئ جدول تكرار للدولة وسلالة القطط
3. اقرأ [API الدول](https://restcountries.eu/rest/v2/all) وابحث عن
   1. أكبر 10 دول
   2. أكثر 10 لغات تحدثًا
   3. العدد الإجمالي للغات في API الدول
4. UCI هو أحد أكثر الأماكن شيوعًا للحصول على مجموعات بيانات لعلم البيانات والتعلم الآلي. اقرأ محتوى UCL (https://archive.ics.uci.edu/ml/datasets.php). بدون مكتبات إضافية سيكون الأمر صعبًا، لذا قد تجربه مع BeautifulSoup4

🎉 مبروك! 🎉

[<< اليوم 19](./19_file_handling.md) | [اليوم 21 >>](./21_classes_and_objects.md)
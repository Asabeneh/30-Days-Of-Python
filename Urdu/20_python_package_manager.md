<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 20 — پیکیج مینیجر</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../20_Day_Python_package_manager/20_python_package_manager.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 19](./19_file_handling.md) | [فہرست](./readme.md) | [اگلا دن: 21](./21_classes_and_objects.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 20](#day-20-section-1)
  - [پائتھن پیکیج مینیجر: pip](#day-20-section-2)
    - [pip کیا ہے؟](#day-20-section-3)
    - [pip انسٹال کرنا](#day-20-section-4)
    - [pip سے پیکیج انسٹال کرنا](#day-20-section-5)
    - [پیکیج ہٹانا](#day-20-section-6)
    - [انسٹال شدہ پیکیجز کی فہرست](#day-20-section-7)
    - [پیکیج کی معلومات](#day-20-section-8)
    - [pip freeze](#day-20-section-9)
    - [URL سے ڈیٹا پڑھنا](#day-20-section-10)
    - [پیکیج بنانا](#day-20-section-11)
    - [پیکیجز کے بارے میں مزید معلومات](#day-20-section-12)
  - [مشقیں — دن 20](#day-20-section-13)

<a id="day-20-section-1"></a>

# 📘 دن 20

<a id="day-20-section-2"></a>

## پائتھن پیکیج مینیجر: pip

<a id="day-20-section-3"></a>

### pip کیا ہے؟

`pip` سے پائتھن پیکیج انسٹال کرتے ہیں۔ اصل متن اسے Preferred Installer Program کہتا ہے؛ اس کا معروف نام “pip installs packages” بھی ہے۔ پیکیج میں ایک یا زیادہ ماڈیول یا ذیلی پیکیج ہو سکتے ہیں۔ ہر سہولت خود لکھنے کے بجائے مناسب پیکیج انسٹال کر کے اپنی ایپلی کیشن میں امپورٹ کر سکتے ہیں۔

<a id="day-20-section-4"></a>

### pip انسٹال کرنا

اگر `pip` موجود نہیں تو اصل سبق یہ کمانڈ دکھاتا ہے:

<div dir="ltr">

```sh
asabeneh@Asabeneh:~$ pip install pip
```

</div>

انسٹال ہونے کی جانچ کریں:

<div dir="ltr">

```sh
pip --version
```

</div>

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

</div>

مثال میں ورژن `21.1.3` ہے۔ آپ کو مختلف ورژن نظر آ سکتا ہے؛ ورژن دکھائی دینا `pip` موجود ہونے کی علامت ہے۔

پائتھن میں مختلف کاموں کے لیے بہت سے پیکیج ہیں۔ چند عام مثالیں دیکھیں۔

<a id="day-20-section-5"></a>

### pip سے پیکیج انسٹال کرنا

NumPy، یعنی numerical Python، سائنسی حساب، ڈیٹا سائنس اور مشین لرننگ میں استعمال ہوتا ہے۔ اس میں یہ سہولتیں ہیں:

- کئی جہتوں کے arrays۔
- broadcasting کے فنکشنز۔
- C، C++ اور Fortran کوڈ کے ساتھ کام کرنے کے اوزار۔
- خطی الجبرا، فوریئر تبدیلی اور اتفاقی اعداد کے فنکشنز۔

<div dir="ltr">

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

</div>

شیل میں `python` لکھیں، پھر NumPy امپورٹ کریں۔

<div dir="ltr">

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

</div>

Pandas، BSD لائسنس کے تحت دستیاب اوپن سورس لائبریری ہے، جو ڈیٹا کی ساختیں اور تجزیے کے اوزار دیتی ہے۔ اسے انسٹال کریں۔

<div dir="ltr">

```sh
asabeneh@Asabeneh:~$ pip install pandas
```

</div>

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

</div>

یہاں مقصد NumPy یا Pandas کی مکمل تعلیم نہیں، بلکہ پیکیج انسٹال اور امپورٹ کرنا ہے۔ ان کی تفصیل بعد میں آئے گی۔

`webbrowser` ویب سائٹس کھول سکتا ہے۔ یہ پائتھن 3 کے ساتھ آتا ہے، اس لیے الگ انسٹال نہیں کرنا پڑتا۔ کئی سائٹس کھولنے یا طے شدہ وقت پر براؤزر کھولنے والے اپنے پروگرام میں اسے استعمال کر سکتے ہیں۔

<div dir="ltr">

```py
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
```

</div>

<a id="day-20-section-6"></a>

### پیکیج ہٹانا

انسٹال شدہ پیکیج ہٹانے کی کمانڈ:

<div dir="ltr">

```sh
pip uninstall packagename
```

</div>

<a id="day-20-section-7"></a>

### انسٹال شدہ پیکیجز کی فہرست

`pip list` سے فہرست دیکھیں۔

<div dir="ltr">

```sh
pip list
```

</div>

<a id="day-20-section-8"></a>

### پیکیج کی معلومات

کسی پیکیج کی معلومات دکھائیں۔

<div dir="ltr">

```sh
pip show packagename
```

</div>

<div dir="ltr">

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

</div>

مزید تفصیل کے لیے `--verbose` دیں۔

<div dir="ltr">

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

</div>

<a id="day-20-section-9"></a>

### pip freeze

یہ انسٹال شدہ پیکیجز اور ان کے ورژن ایسے فارمیٹ میں دکھاتا ہے جو requirements فائل میں رکھا جا سکتا ہے۔ `requirements.txt` منصوبے کی درکار dependencies درج کرتی ہے۔

<div dir="ltr">

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

</div>

اس نتیجے کو deployment کے لیے `requirements.txt` میں استعمال کر سکتے ہیں۔

<a id="day-20-section-10"></a>

### URL سے ڈیٹا پڑھنا

مقامی فائلوں کے علاوہ ویب سائٹ یا API سے بھی ڈیٹا پڑھ سکتے ہیں۔ API، یعنی Application Programming Interface، پروگراموں کے درمیان ساخت والے ڈیٹا کے تبادلے کا ذریعہ ہے؛ اکثر JSON استعمال ہوتا ہے۔ `requests` سے HTTP درخواستیں بھیج سکتے ہیں، جن سے CRUD، یعنی بنانا، پڑھنا، بدلنا اور حذف کرنا، انجام دیا جا سکتا ہے۔ یہاں صرف پڑھنا دیکھیں گے۔

`requests` انسٹال کریں۔

<div dir="ltr">

```py
asabeneh@Asabeneh:~$ pip install requests
```

</div>

اہم فنکشن اور اوصاف:

- `get()`: URL سے ڈیٹا مانگتا ہے اور response آبجیکٹ دیتا ہے۔
- `status_code`: کامیابی یا خرابی کی حالت۔
- `headers`: response کی header معلومات۔
- `text`: response کا متن۔
- `json()`: JSON جواب کو پائتھن ڈیٹا میں بدلنا۔

اس [متنی فائل](https://www.w3.org/TR/PNG/iso_8859-1.txt) کو پڑھیں۔

<div dir="ltr">

```py
import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
```

</div>

<div dir="ltr">

```sh
<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

</div>

اب اصل سبق کی [ممالک والی API](https://restcountries.eu/rest/v2/all) پڑھنے کی مثال دیکھیں۔ یہ تاریخی endpoint ہے اور اس کی موجودہ دستیابی اس ترجمے میں تصدیق نہیں کی گئی۔

<div dir="ltr">

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries
```

</div>

<div dir="ltr">

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

</div>

JSON ڈیٹا کے لیے response کا `json()`، جبکہ txt، HTML، XML اور دوسرے متنی فارمیٹس کے لیے `text` استعمال کریں۔

<a id="day-20-section-11"></a>

### پیکیج بنانا

بہت سی فائلوں کو متعلقہ فولڈروں میں رکھنے سے انہیں سمجھنا اور سنبھالنا آسان ہوتا ہے۔ ماڈیول میں کلاسز اور فنکشنز ہو سکتے ہیں، جبکہ پیکیج متعلقہ ماڈیولز کو یکجا کرتا ہے۔ `mypackage` بنائیں:

1. `30DaysOfPython` میں `mypackage` فولڈر بنائیں۔
2. اس میں خالی `__init__.py` بنائیں۔
3. `arithmetic.py` اور `greet.py` میں یہ کوڈ لکھیں۔

<div dir="ltr">

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

</div>

<div dir="ltr">

```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```

</div>

فولڈر کی ساخت:

<div dir="ltr">

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

</div>

تعاملی شیل میں اپنا پیکیج آزمائیں۔

<div dir="ltr">

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

</div>

مثال کا پیکیج کام کرتا ہے۔ عام پیکیج میں `__init__.py` ابتدائی کوڈ رکھ سکتی ہے اور اس میں مطلوبہ نام امپورٹ کر کے باہر دستیاب کیے جا سکتے ہیں۔ خالی `__init__.py` تمام ذیلی ماڈیولز کے فنکشن خود امپورٹ نہیں کرتی۔ پائتھن namespace packages میں یہ فائل ضروری بھی نہیں؛ یہاں عام پیکیج کا طریقہ استعمال ہوا ہے۔

<a id="day-20-section-12"></a>

### پیکیجز کے بارے میں مزید معلومات

- ڈیٹابیس: SQLAlchemy اور SQLObject مختلف ڈیٹابیسز تک آبجیکٹ پر مبنی رسائی دیتے ہیں۔ کمانڈ: `pip install SQLAlchemy`۔
- ویب ڈیولپمنٹ: Django ایک اعلیٰ سطح کا ویب فریم ورک ہے (`pip install django`)۔ Flask، Werkzeug اور Jinja پر مبنی مختصر فریم ورک ہے (`pip install flask`)۔
- HTML parsing: [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) HTML/XML پڑھنے، حتیٰ کہ خراب markup کے ساتھ بھی کام کرنے، میں مدد دیتا ہے (`pip install beautifulsoup4`)۔ PyQuery پائتھن میں jQuery جیسا انداز دیتا ہے۔
- XML: ElementTree درخت نما ڈیٹا کو میموری میں رکھنے کے لیے سادہ اور لچک دار اوزار دیتا ہے؛ پائتھن 2.5 سے معیاری لائبریری کا حصہ ہے۔
- گرافیکل انٹرفیس: PyQt، Qt فریم ورک کی bindings ہے۔ Tkinter پائتھن کا روایتی GUI toolkit ہے۔
- ڈیٹا تجزیہ اور مشین لرننگ: NumPy عددی حساب، Pandas جدول والے ڈیٹا، اور SciPy optimization، خطی الجبرا، integration، تصاویر اور شماریات میں کام آتے ہیں۔ Scikit-learn، NumPy اور SciPy پر قائم مشین لرننگ کے اوزار دیتا ہے۔ TensorFlow گوگل کا بنایا ہوا مشین لرننگ فریم ورک ہے۔ Keras نیورل نیٹ ورک لکھنے، ماڈل ترتیب دینے اور ڈیٹا کے ساتھ کام کرنے کو آسان بناتا ہے۔
- نیٹ ورک: `requests` سے سرور کو GET، POST، DELETE اور PUT درخواستیں بھیج سکتے ہیں (`pip install requests`)۔

🌕 آپ نے بیس دن مکمل کر لیے! اب مشق کریں۔

<a id="day-20-section-13"></a>

## مشقیں — دن 20

1. `romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'` سے متن پڑھ کر دس سب سے عام الفاظ نکالیں۔
2. `cats_api = 'https://api.thecatapi.com/v1/breeds'` سے:
   1. بلیوں کے میٹرک وزن کا کم سے کم، زیادہ سے زیادہ، اوسط، میڈین اور معیاری انحراف نکالیں۔
   2. سالوں میں متوقع عمر کے یہی اعداد نکالیں۔
   3. ملک اور نسل کی تعدادی جدول بنائیں۔
3. [ممالک والی API](https://restcountries.eu/rest/v2/all) سے:
   1. رقبے کے لحاظ سے دس بڑے ممالک۔
   2. دس سب سے زیادہ بولی جانے والی زبانیں۔
   3. زبانوں کی کل تعداد۔
4. UCI ڈیٹا سائنس اور مشین لرننگ کے ڈیٹا سیٹس کا معروف ذخیرہ ہے۔ اصل سبق کے [UCI رابطے](https://archive.ics.uci.edu/ml/datasets.php) کا مواد پڑھیں۔ اضافی لائبریری کے بغیر مشکل ہو سکتا ہے، اس لیے BeautifulSoup4 آزمائیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 19](./19_file_handling.md) | [فہرست](./readme.md) | [اگلا دن: 21](./21_classes_and_objects.md)

</div>

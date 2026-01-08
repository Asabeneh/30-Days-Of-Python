<div align="center">
  <h1> 30 Days Of Python: Day 20 - PIP </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Second Edition: July, 2021</small>
</sub>
</div>

[<< Day 19](../19_Day_File_handling/19_file_handling.md) | [Day 21 >>](../21_Day_Classes_and_objects/21_classes_and_objects.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 20](#-day-20)
  - [Python PIP - Python Package Manager](#python-pip---python-package-manager)
    - [What is PIP ?](#what-is-pip-)
    - [Installing PIP](#installing-pip)
    - [Installing packages using pip](#installing-packages-using-pip)
    - [Uninstalling Packages](#uninstalling-packages)
    - [List of Packages](#list-of-packages)
    - [Show Package](#show-package)
    - [PIP Freeze](#pip-freeze)
    - [Reading from URL](#reading-from-url)
    - [Creating a Package](#creating-a-package)
    - [Further Information About Packages](#further-information-about-packages)

# 📘 Day 20

## Python PIP - Python Package Manager

### What is PIP ?

PIP មានន័យថា កម្មវិធី Installer Preferred ។ យើងប្រើ _pip_ ដើម្បីដំឡើងកម្មវិធី Python ផ្សេងៗ
Package គឺជាម៉ូឌុល Python ដែលអាចមានមួយឬច្រើនម៉ូឌុលឬឯកសារផ្សេងទៀត។ ម៉ូឌុល ឬ ម៉ូឌុល ដែល យើង អាច ដំឡើង ទៅលើ កម្មវិធី របស់ យើង គឺជា កញ្ចប់ ។
ក្នុងការរៀបចំកម្មវិធី យើងមិនចាំបាច់សរសេរកម្មវិធី Utility ទាំងអស់ទេ ជំនួសវិញយើងបានដំឡើង Package និងimportវាទៅក្នុងកម្មវិធីរបស់យើង

### Installing PIP

បើសិនជាអ្នកមិនបានដំឡើង pip សូមឲ្យយើងដំឡើងវាឥឡូវនេះ ចូលទៅក្នុង Terminal ឬ Command Prompt របស់អ្នក ហើយ Copy និង paste នេះ:

```sh
asabeneh@Asabeneh:~$ pip install pip
```

ត្រួតពិនិត្យថា pip ត្រូវបានដំឡើងដោយសរសេរ
```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

ដូច ដែល អ្នក អាច មើល បាន ខ្ញុំ កំពុង ប្រើ Pip Version 21.1.3 ប្រសិន បើ អ្នក ឃើញ ចំនួន ណាមួយ នៅ ខាង ក្រោម ឬ ខាង លើ នោះ មាន ន័យ ថា អ្នក មាន Pip បាន ដំឡើង

សូមយើងពិនិត្យមើលនូវ Package មួយចំនួនដែលត្រូវបានប្រើនៅក្នុងសហគមន៍ Python សម្រាប់គោលដៅផ្សេងៗ គ្រាន់តែអោយអ្នកដឹងថា មានច្រើននូវកម្មវិធីសម្រាប់ប្រើជាមួយកម្មវិធីផ្សេងៗ

### Installing packages using pip

សូមព្យាយាមដំឡើង _numpy_ ហៅថា numeric python វាគឺជាកម្មវិធីមួយដែលពេញនិយមបំផុតនៅក្នុងការសិក្សាពីម៉ាស៊ីន និងសហគមន៍វិទ្យាសាស្ត្រទិន្នន័យ។

- NumPy គឺជាកញ្ចប់មូលដ្ឋានសម្រាប់គណនេយ្យវិទ្យា ជាមួយ Python ។ ក្នុងនោះរួមមាន៖
- a powerful N-dimensional array object
- មុខងារ (ការផ្សាយ) ដែលមានលក្ខណៈខ្ពស់
- ឧបករណ៍សម្រាប់បញ្ចូលកូដ C/C++ និង Fortran
- algebra linear ដែលមានប្រសិទ្ធភាព ប្តូរ Fourier និងសមត្ថភាពចំនួនលេចលឺ

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

Let us start using numpy. Open your python interactive shell, write python and then import numpy as follows:

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

Pandas គឺជាបណ្ណាល័យដែលមានលិខិតអនុញ្ញាតដោយ BSD ដែលមានប្រភពបើកទូលាយ ដែលផ្តល់នូវលក្ខណៈសម្បត្តិខ្ពស់ និងងាយស្រួលក្នុងការប្រើប្រាស់ និងឧបករណ៍វិភាគទិន្នន័យសម្រាប់ភាសា Python ។ សូមឲ្យយើងដំឡើងបងធំរបស់ Numpy, _pandas_:

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
ផ្នែកនេះមិនមែនជាអំពី numpy ឬ pandas ទេយើងកំពុងតែព្យាយាមរៀនសូត្រអំពីរបៀបដំឡើងឯកសារ និងរបៀបនាំចូលវា។ ប្រសិនបើ វា ត្រូវការ យើង នឹង និយាយ អំពី កញ្ចប់ ផ្សេងគ្នា នៅក្នុង ផ្នែក ផ្សេងទៀត ។

សូមយើងនាំចូលម៉ូឌុល Browser ដែលអាចជួយយើងបើកគេហទំព័រណាមួយ។ យើងមិនចាំបាច់ដំឡើងម៉ូឌុលនេះទេ វាត្រូវបានដំឡើងដោយ default ជាមួយ Python 3 ។ ឧទាហរណ៍ ប្រសិនបើអ្នកចង់បើកគេហទំព័រចំនួនណាមួយក្នុងពេលណាមួយ ឬប្រសិនបើអ្នកចង់កំណត់ពេលអ្វីមួយនេះ _webbrowser_ module អាចត្រូវបានប្រើ។

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

### Uninstalling Packages

ប្រសិនបើលោកអ្នកមិនចង់រក្សាឯកសារដែលបានដំឡើងនោះទេ លោកអ្នកអាចលុបវាដោយប្រើបញ្ជាខាងក្រោម។

```sh
pip uninstall packagename
```

### List of Packages

ដើម្បីមើលឯកសារដែលបានដំឡើងនៅលើម៉ាស៊ីនរបស់យើង។ យើងអាចប្រើ pip តាមដានដោយបញ្ជី

```sh
pip list
```

### Show Package

ដើម្បីបង្ហាញព័ត៌មានអំពីកញ្ចប់
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

ប្រសិនបើយើងចង់បានព័ត៌មានបន្ថែមទៀត សូមបន្ថែម --verbose
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

បង្កើតឯកសារ Python ដែលបានដំឡើង ជាមួយនឹងវីសេរីរបស់វា ហើយ output គឺសមស្របសម្រាប់ប្រើវានៅក្នុងឯកសារតម្រូវការ។ ឯកសារ requirements.txt គឺជាឯកសារដែលត្រូវមានឯកសារ Python ទាំងអស់ដែលបានដំឡើងនៅក្នុងគម្រោង Python ។

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

The pip freeze gave us the packages used, installed and their version. We use it with requirements.txt file for deployment.

### Reading from URL
ឥឡូវនេះអ្នកបានស្គាល់អំពីរបៀបអានឬសរសេរទៅលើឯកសារដែលស្ថិតនៅលើម៉ាស៊ីនក្នុងស្រុករបស់អ្នក។ ពេលខ្លះយើងចង់អានពីគេហទំព័រមួយ ដោយប្រើ url ឬពី API
API មានន័យថា Application Program Interface (ប្រព័ន្ធប្រតិបត្តិការកម្មវិធី) ។ វាគឺជាមធ្យោបាយមួយដើម្បីផ្លាស់ប្តូរទិន្នន័យដែលមានលក្ខណៈរចនាសម្ព័ន្ធរវាង server ជាពិសេសជាទិន្នន័យ json ។ ដើម្បីបើកការភ្ជាប់ប្រព័ន្ធប្រតិបត្តិការ, យើងត្រូវការឯកសារមួយដែលហៅថា _requests_ - វាអនុញ្ញាតឱ្យបើកការភ្ជាប់ប្រព័ន្ធប្រតិបត្តិការនិងអនុវត្ត CRUD (បង្កើត, អាន, បច្ចុប្បន្នភាពនិងលុប) ប្រតិបត្តិការ។ នៅក្នុងផ្នែកនេះយើងនឹងពិនិត្យមើលតែការអានដែកដែលទទួលបានផ្នែកនៃ CRUD ។

Let us install _requests_:

```py
asabeneh@Asabeneh:~$ pip install requests
```

យើងនឹងឃើញ _get_, _status_code_, _headers_, _text_ និង _json_ វិធីសាស្ត្រនៅក្នុង _requests_ module:

- _get()_: ដើម្បីបើកបណ្តាញនិងទាញយកទិន្នន័យពី url - វាត្រឡប់មកវិញ Reply Object
- _status_code_: បន្ទាប់ពីយើងបានទាញយកទិន្នន័យ, យើងអាចពិនិត្យស្ថានភាពនៃប្រតិបត្តិការ (ជោគជ័យ, កំហុស, ជាដើម)
- _headers_: ដើម្បីពិនិត្យប្រភេទ headers
- _text_: ដើម្បីទាញយកអត្ថបទពី object ប្រតិកម្មទាញយក
- _json_: ដើម្បីទាញយកទិន្នន័យ json
- 
Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
```

```sh
<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

- សូមឱ្យយើងអានពី API ។ API មានន័យថា Application Program Interface (ប្រព័ន្ធប្រតិបត្តិការកម្មវិធី) ។ វាជាមធ្យោបាយដើម្បីផ្លាស់ប្តូរទិន្នន័យរចនាសម្ព័ន្ធរវាង server ជាពិសេសទិន្នន័យ json ។ ឧទាហរណ៍នៃ API:<https://restcountries.eu/rest/v2/all> សូមយើងអាន API នេះដោយប្រើម៉ូឌុល _requests_

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries
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

យើងប្រើវិធីសាស្ត្រ _json()_ ពី Reply Object ប្រសិនបើយើងកំពុងទាញយកទិន្នន័យ JSON ។ សម្រាប់ txt, html, xml និងឯកសារផ្សេងទៀតយើងអាចប្រើ _text_ ។

### Creating a Package

យើង រៀបចំ ឯកសារ ជាច្រើន នៅក្នុង ក្រដាស និង ក្រដាស អនុ ផ្សេងគ្នា ដោយ ផ្អែកលើ លក្ខខណ្ឌ មួយចំនួន ដើម្បី យើង អាច រក និង គ្រប់គ្រង វា បាន ដោយ ងាយស្រួល ។ ដូចដែលអ្នកដឹងម៉ូដល័រអាចមានច្រើនប្រភេទដូចជា Class, Function ជាដើម។ កញ្ចប់មួយអាចមានមួយឬច្រើនម៉ូឌុលដែលមានសារៈសំខាន់។ Package គឺជា folder ដែលមានឯកសារ module មួយ ឬច្រើន។ សូមយើងបង្កើតឯកសារដែលមានឈ្មោះ mypackage ដោយប្រើជំហានដូចខាងក្រោម:

បង្កើត folder ថ្មីដែលមានឈ្មោះ mypacakge នៅក្នុង folder 30DaysOfPython
បង្កើតឯកសារ ****init****.py ដែលគ្មាននៅក្នុង folder mypackage ។
បង្កើតម៉ូឌុល arithmetic.py និង greet.py ជាមួយនឹងកូដដូចខាងក្រោម:

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

រចនាសម្ព័ន្ធ folder របស់ package របស់អ្នកគួរមើលទៅដូចនេះ:
```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

ឥឡូវនេះយើងត្រូវបើក shell interactive python ហើយសាកល្បងកម្មវិធីដែលយើងបានបង្កើត:

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

ដូចដែលអ្នកអាចមើលឃើញបាន កញ្ចប់របស់យើងដំណើរការយ៉ាងល្អ។ ក្រដាសកញ្ចប់មានឯកសារពិសេសដែលមានឈ្មោះថា ****init****.py - វារក្សាទុកផ្ទុករបស់កញ្ចប់។ ប្រសិនបើយើងដាក់ ****init****.py នៅក្នុង folder package, python start នឹងស្គាល់វាជា package ។

****init****.py បង្ហាញធនធានដែលបានកំណត់ពីម៉ូឌុលរបស់វាដើម្បីនាំចូលទៅក្នុងឯកសារ Python ផ្សេងទៀត។ ឯកសារ ****init****.py ដែលសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែសុទ្ធសឹងតែ ****init****.py គឺមានសារៈសំខាន់សម្រាប់ folder ដែល Python អាចទទួលស្គាល់ថាជា packages ។

### Further Information About Packages

- Database
  - SQLAlchemy or SQLObject - Object oriented access to several different database systems
    - _pip install SQLAlchemy_
- Web Development
  - Django - High-level web framework.
    - _pip install django_
  - Flask - micro framework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
    - _pip install flask_
- HTML Parser
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
    - _pip install beautifulsoup4_
  - PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

- XML Processing
  - ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
- GUI
  - PyQt - Bindings for the cross-platform Qt framework.
  - TkInter - The traditional Python user interface toolkit.
- Data Analysis, Data Science and Machine learning
  - Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
  - Pandas: is a data analysis, data science and a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
  - SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
  - Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
  - TensorFlow: is a machine learning library built by Google.
  - Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
- Network:
  - requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
    - _pip install requests_



🎉 CONGRATULATIONS ! 🎉

[<< Day 19](../19_Day_File_handling/19_file_handling.md) | [Day 21 >>](../21_Day_Classes_and_objects/21_classes_and_objects.md)

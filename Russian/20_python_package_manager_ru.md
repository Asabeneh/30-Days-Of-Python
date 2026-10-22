<div align="center">
  <h1> 30 Days Of Python: День 20 - PIP </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Второе издание: июль 2021</small>
</sub>
</div>

[<< День 19](./19_file_handling_ru.md) | [День 21 >>](./21_classes_and_objects_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 20](#-день-20)
  - [Python PIP - менеджер пакетов Python](#python-pip---менеджер-пакетов-python)
    - [Что такое PIP ?](#что-такое-pip-)
    - [Установка PIP](#установка-pip)
    - [Установка пакетов с помощью pip](#установка-пакетов-с-помощью-pip)
    - [Удаление пакетов](#удаление-пакетов)
    - [Список пакетов](#список-пакетов)
    - [Показать пакет](#показать-пакет)
    - [PIP Freeze](#pip-freeze)
    - [Чтение по URL](#чтение-по-url)
    - [Создание пакета](#создание-пакета)
    - [Дополнительная информация о пакетах](#дополнительная-информация-о-пакетах)
  - [Упражнения: День 20](#упражнения-день-20)

# 📘 День 20

## Python PIP - менеджер пакетов Python

### Что такое PIP ?

PIP расшифровывается как Preferred installer program (предпочтительная программа установки). Мы используем _pip_ для установки различных пакетов Python.
Пакет — это модуль Python, который может содержать один или несколько модулей или других пакетов. Модуль или модули, которые мы можем установить в наше приложение, — это пакет.
В программировании нам не нужно писать каждую служебную программу, вместо этого мы устанавливаем пакеты и импортируем их в наши приложения.

### Установка PIP

Если вы не устанавливали pip, давайте установим его сейчас. Перейдите в терминал или командную строку и скопируйте и вставьте это:

```sh
asabeneh@Asabeneh:~$ pip install pip
```

Проверьте, установлен ли pip, написав

```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

Как видите, я использую pip версии 21.1.3; если вы видите число немного меньше или больше, это значит, что pip у вас установлен.

Давайте посмотрим на некоторые пакеты, которые используются в сообществе Python для разных целей. Просто чтобы вы знали: существует множество пакетов для использования в различных приложениях.

### Установка пакетов с помощью pip

Давайте попробуем установить _numpy_, который называют numeric python. Это один из самых популярных пакетов в сообществе машинного обучения и анализа данных.

- NumPy — фундаментальный пакет для научных вычислений на Python. Среди прочего он содержит:
  - мощный объект N-мерного массива
  - продвинутые (широковещательные) функции
  - инструменты для интеграции кода на C/C++ и Fortran
  - полезные возможности линейной алгебры, преобразования Фурье и работы со случайными числами

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

Давайте начнём использовать numpy. Откройте интерактивную оболочку Python, введите python и затем импортируйте numpy следующим образом:

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

Pandas — это библиотека с открытым исходным кодом под лицензией BSD, предоставляющая высокопроизводительные и простые в использовании структуры данных и инструменты анализа данных для языка программирования Python. Давайте установим старшего брата numpy — _pandas_:

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

Этот раздел не о numpy и не о pandas; здесь мы пытаемся научиться устанавливать пакеты и импортировать их. При необходимости мы поговорим о разных пакетах в других разделах.

Давайте импортируем модуль веб-браузера, который поможет нам открыть любой сайт. Нам не нужно устанавливать этот модуль, он уже установлен по умолчанию вместе с Python 3. Например, если вы хотите открыть любое количество сайтов в любое время или если вы хотите что-то запланировать, можно использовать этот модуль _webbrowser_.

```py
import webbrowser # модуль веб-браузера для открытия сайтов

# список url: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# открывает приведённый выше список сайтов в новой вкладке
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### Удаление пакетов

Если вы не хотите хранить установленные пакеты, вы можете удалить их с помощью следующей команды.

```sh
pip uninstall packagename
```

### Список пакетов

Чтобы увидеть установленные на нашей машине пакеты, мы можем использовать pip, а затем list.

```sh
pip list
```

### Показать пакет

Чтобы показать информацию о пакете

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

Если мы хотим получить ещё больше деталей, просто добавьте --verbose

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

Сгенерируйте список установленных пакетов Python с их версиями; вывод подходит для использования в файле требований. Файл requirements.txt — это файл, который должен содержать все установленные пакеты Python в проекте на Python.

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

Pip freeze выдал нам использованные и установленные пакеты и их версии. Мы используем его вместе с файлом requirements.txt для развёртывания.

### Чтение по URL

К настоящему моменту вы знакомы с тем, как читать или записывать в файл, расположенный на вашей локальной машине. Иногда мы хотим читать с сайта по url или из API.
API расшифровывается как Application Program Interface (интерфейс прикладного программирования). Это средство обмена структурированными данными между серверами, преимущественно в виде json-данных. Чтобы открыть сетевое соединение, нам нужен пакет _requests_ — он позволяет открыть сетевое соединение и реализовать операции CRUD (create, read, update and delete — создание, чтение, обновление и удаление). В этом разделе мы рассмотрим только часть CRUD, связанную с чтением или получением.

Давайте установим _requests_:

```py
asabeneh@Asabeneh:~$ pip install requests
```

Мы увидим методы _get_, _status_code_, _headers_, _text_ и _json_ в модуле _requests_:
  - _get()_: чтобы открыть сетевое соединение и получить данные по url — возвращает объект ответа
  - _status_code_: после получения данных мы можем проверить статус операции (успех, ошибка и т. д.)
  - _headers_: чтобы проверить типы заголовков
  - _text_: чтобы извлечь текст из полученного объекта ответа
  - _json_: чтобы извлечь json-данные
Давайте прочитаем txt-файл с этого сайта: https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # импортируем модуль requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # текст с сайта

response = requests.get(url) # открываем сетевое соединение и получаем данные
print(response)
print(response.status_code) # код состояния, успех: 200
print(response.headers)     # информация о заголовках
print(response.text) # возвращает весь текст со страницы
```

```sh
<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

- Давайте прочитаем из API. API расшифровывается как Application Program Interface (интерфейс прикладного программирования). Это средство обмена структурированными данными между серверами, преимущественно в виде json-данных. Пример API: https://restcountries.eu/rest/v2/all. Давайте прочитаем этот API с помощью модуля _requests_.

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # api стран
response = requests.get(url)  # открываем сетевое соединение и получаем данные
print(response) # объект ответа
print(response.status_code)  # код состояния, успех: 200
countries = response.json()
print(countries[:1])  # мы взяли только первую страну, уберите срез, чтобы увидеть все страны
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

Мы используем метод _json()_ из объекта ответа, если получаем JSON-данные. Для txt, html, xml и других форматов файлов можно использовать _text_.

### Создание пакета

Мы организуем большое количество файлов в разных папках и подпапках по некоторому критерию, чтобы было легко их находить и управлять ими. Как вы знаете, модуль может содержать несколько объектов, таких как классы, функции и т. д. Пакет может содержать один или несколько связанных модулей. Пакет на самом деле — это папка, содержащая один или несколько файлов модулей. Давайте создадим пакет с именем mypackage, выполнив следующие шаги:

Создайте новую папку с именем mypackage внутри папки 30DaysOfPython
Создайте пустой файл **__init__**.py в папке mypackage.
Создайте модули arithmetic.py и greet.py со следующим кодом:

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

Структура папок вашего пакета должна выглядеть так:

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

Теперь давайте откроем интерактивную оболочку Python и попробуем пакет, который мы создали:

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

Как видите, наш пакет работает отлично. Папка пакета содержит специальный файл **__init__**.py — он хранит содержимое пакета. Если мы поместим **__init__**.py в папку пакета, Python начнёт распознавать её как пакет.
**__init__**.py предоставляет определённые ресурсы из своих модулей для импорта в другие файлы Python. Пустой файл **__init__**.py делает все функции доступными при импорте пакета. **__init__**.py необходим для того, чтобы Python распознал папку как пакет.

### Дополнительная информация о пакетах

- Базы данных
  - SQLAlchemy или SQLObject — объектно-ориентированный доступ к нескольким разным системам баз данных
    - _pip install SQLAlchemy_
- Веб-разработка
  - Django — высокоуровневый веб-фреймворк.
    - _pip install django_
  - Flask — микрофреймворк для Python на основе Werkzeug, Jinja 2. (Лицензия BSD)
    - _pip install flask_
- HTML-парсер
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) — парсер HTML/XML, предназначенный для быстрых проектов вроде скрапинга экранов, принимает плохую разметку.
    - _pip install beautifulsoup4_
  - PyQuery — реализует jQuery в Python; по-видимому, быстрее BeautifulSoup.

- Обработка XML
  - ElementTree — тип Element представляет собой простой, но гибкий объект-контейнер, предназначенный для хранения иерархических структур данных, таких как упрощённые наборы информации XML, в памяти. --Примечание: начиная с Python 2.5 ElementTree входит в стандартную библиотеку
- GUI
  - PyQt — привязки для кроссплатформенного фреймворка Qt.
  - TkInter — традиционный набор инструментов пользовательского интерфейса Python.
- Анализ данных, наука о данных и машинное обучение
  - Numpy: Numpy (numeric python) известен как одна из самых популярных библиотек машинного обучения в Python.
  - Pandas: библиотека анализа данных, науки о данных и машинного обучения в Python, которая предоставляет структуры данных высокого уровня и широкий набор инструментов для анализа.
  - SciPy: SciPy — библиотека машинного обучения для разработчиков приложений и инженеров. Библиотека SciPy содержит модули для оптимизации, линейной алгебры, интегрирования, обработки изображений и статистики.
  - Scikit-Learn: это NumPy и SciPy. Считается одной из лучших библиотек для работы со сложными данными.
  - TensorFlow: библиотека машинного обучения, созданная Google.
  - Keras: считается одной из самых классных библиотек машинного обучения в Python. Она предоставляет более простой механизм для выражения нейронных сетей. Keras также предлагает одни из лучших утилит для компиляции моделей, обработки наборов данных, визуализации графиков и многого другого.
- Сети:
  - requests: пакет, который мы можем использовать для отправки запросов на сервер (GET, POST, DELETE, PUT)
    - _pip install requests_

🌕 Вы всегда продвигаетесь вперёд, и вам осталось 20 шагов на пути к величию. Теперь сделайте несколько упражнений для мозга и мышц.

## Упражнения: День 20

1. Прочитайте этот url и найдите 10 самых частых слов. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
2. Прочитайте API кошек cats_api = 'https://api.thecatapi.com/v1/breeds' и найдите:
   1. минимум, максимум, среднее, медиану, стандартное отклонение веса кошек в метрических единицах.
   2. минимум, максимум, среднее, медиану, стандартное отклонение продолжительности жизни кошек в годах.
   3. Создайте таблицу частот стран и пород кошек
3. Прочитайте [API стран](https://restcountries.eu/rest/v2/all) и найдите
   1. 10 крупнейших стран
   2. 10 самых распространённых языков
   3. общее количество языков в API стран
4. UCI — одно из самых распространённых мест, где берут наборы данных для науки о данных и машинного обучения. Прочитайте содержимое UCL (https://archive.ics.uci.edu/ml/datasets.php). Без дополнительных библиотек это будет сложно, так что можете попробовать с BeautifulSoup4

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 19](./19_file_handling_ru.md) | [День 21 >>](./21_classes_and_objects_ru.md)

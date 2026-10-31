<div align="center">
  <h1> 30 дней Python: День 19 - Работа с файлами</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Асабенех Йетаех</a><br>
<small>Второе издание: июль 2021</small>
</sub>
</div>

[<< День 18](../18_Day_Regular_expressions/18_regular_expressions.md) | [День 20 >>](../20_Day_Python_package_manager/20_python_package_manager.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 19](#-день-19)
  - [Работа с файлами](#работа-с-файлами)
    - [Открытие файлов для чтения](#открытие-файлов-для-чтения)
    - [Открытие файлов для записи и обновления](#открытие-файлов-для-записи-и-обновления)
    - [Удаление файлов](#удаление-файлов)
  - [Типы файлов](#типы-файлов)
    - [Файл с расширением txt](#файл-с-расширением-txt)
    - [Файл с расширением json](#файл-с-расширением-json)
    - [Преобразование JSON в словарь](#преобразование-json-в-словарь)
    - [Преобразование словаря в JSON](#преобразование-словаря-в-json)
    - [Сохранение в файл JSON](#сохранение-в-файл-json)
    - [Файл с расширением csv](#файл-с-расширением-csv)
    - [Файл с расширением xlsx](#файл-с-расширением-xlsx)
    - [Файл с расширением xml](#файл-с-расширением-xml)
  - [💻 Упражнения: День 19](#-упражнения-день-19)
    - [Упражнения: Уровень 1](#упражнения-уровень-1)
    - [Упражнения: Уровень 2](#упражнения-уровень-2)
    - [Упражнения: Уровень 3](#упражнения-уровень-3)

# 📘 День 19

## Работа с файлами

До сих пор мы видели различные типы данных Python. Мы обычно храним наши данные в разных форматах файлов. Помимо работы с файлами, в этом разделе мы также рассмотрим различные форматы файлов (.txt, .json, .xml, .csv, .tsv, .excel). Сначала давайте познакомимся с обработкой файлов с распространённым форматом файла (.txt).

Работа с файлами - важная часть программирования, которая позволяет нам создавать, читать, обновлять и удалять файлы. В Python для работы с данными мы используем встроенную функцию _open()_.

```py
# Синтаксис
open('filename', mode) # режим (r, a, w, x, t,b) может быть для чтения, записи, обновления
```

- "r" - Чтение - значение по умолчанию. Открывает файл для чтения, возвращает ошибку, если файл не существует
- "a" - Добавление - Открывает файл для добавления, создаёт файл, если он не существует
- "w" - Запись - Открывает файл для записи, создаёт файл, если он не существует
- "x" - Создание - Создаёт указанный файл, возвращает ошибку, если файл существует
- "t" - Текст - значение по умолчанию. Текстовый режим
- "b" - Бинарный - двоичный режим (например, изображения)

### Открытие файлов для чтения

Режим по умолчанию для _open_ - чтение, поэтому нам не нужно указывать 'r' или 'rt'. Я создал и сохранил файл с именем reading_file_example.txt в каталоге files. Давайте посмотрим, как это делается:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

Как видите в примере выше, я вывел открытый файл, и он дал некоторую информацию о нём. Открытый файл имеет различные методы чтения: _read()_, _readline_, _readlines_. Открытый файл должен быть закрыт методом _close()_.

- _read()_: читает весь текст как строку. Если мы хотим ограничить количество символов для чтения, мы можем ограничить его, передав целочисленное значение в метод *read(number)*.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# вывод
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

Вместо вывода всего текста давайте выведем первые 10 символов текстового файла.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# вывод
<class 'str'>
This is an
```

- _readline()_: читает только первую строку

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# вывод
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: читает весь текст построчно и возвращает список строк

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# вывод
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Другой способ получить все строки в виде списка - использовать _splitlines()_:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# вывод
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

После того как мы открыли файл, мы должны закрыть его. Существует высокая вероятность забыть закрыть их. Есть новый способ открытия файлов с помощью _with_ - он закрывает файлы сам. Давайте перепишем предыдущий пример с методом _with_:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# вывод
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Открытие файлов для записи и обновления

Чтобы записать в существующий файл, мы должны добавить режим в качестве параметра функции _open()_:

- "a" - добавление - добавит в конец файла, если файл не существует, он создаст новый файл.
- "w" - запись - перезапишет любое существующее содержимое, если файл не существует, он создаст его.

Давайте добавим некоторый текст в файл, который мы читали:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

Метод ниже создаёт новый файл, если файл не существует:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### Удаление файлов

В предыдущем разделе мы видели, как создать и удалить каталог с помощью модуля _os_. Теперь, если мы хотим удалить файл, мы используем модуль _os_.

```py
import os
os.remove('./files/example.txt')

```

Если файл не существует, метод remove вызовет ошибку, поэтому лучше использовать условие, подобное этому:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## Типы файлов

### Файл с расширением txt

Файл с расширением _txt_ - очень распространённая форма данных, и мы рассмотрели её в предыдущем разделе. Давайте перейдём к файлу JSON

### Файл с расширением json

JSON означает JavaScript Object Notation. На самом деле это строковый объект JavaScript или словарь Python.

_Пример:_

```py
# словарь
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: строковая форма словаря
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# мы используем три кавычки и делаем её многострочной, чтобы сделать её более читаемой
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### Преобразование JSON в словарь

Чтобы преобразовать JSON в словарь, сначала мы импортируем модуль json, а затем используем метод _loads_.

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# давайте преобразуем JSON в словарь
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# вывод
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### Преобразование словаря в JSON

Чтобы преобразовать словарь в JSON, мы используем метод _dumps_ из модуля json.

```py
import json
# словарь python
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# давайте преобразуем его в json
person_json = json.dumps(person, indent=4) # отступ может быть 2, 4, 8. Он делает json красивым
print(type(person_json))
print(person_json)
```

```sh
# вывод
# когда вы печатаете его, у него нет кавычек, но на самом деле это строка
# JSON не имеет типа, это строковый тип.
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

### Сохранение в файл JSON

Мы также можем сохранить наши данные в файл json. Давайте сохраним их в файл json, выполнив следующие шаги. Для записи в файл json мы используем метод json.dump(), он может принимать словарь, выходной файл, ensure_ascii и indent.

```py
import json
# словарь python
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

В коде выше мы используем кодировку и отступ. Отступ делает файл json лёгким для чтения.

### Файл с расширением csv

CSV означает значения, разделённые запятыми. CSV - это простой формат файла, используемый для хранения табличных данных, таких как электронная таблица или база данных. CSV - очень распространённый формат данных в науке о данных.

**Пример:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**Пример:**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # мы используем метод reader для чтения csv
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

```sh
# вывод:
Column names are :name, country, city, skills
Number of lines:  1
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines:  2
```

### Файл с расширением xlsx

Для чтения файлов Excel нам нужно установить пакет _xlrd_. Мы рассмотрим это после того, как изучим установку пакетов с помощью pip.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### Файл с расширением xml

XML - это ещё один структурированный формат данных, который выглядит как HTML. В XML теги не предопределены. Первая строка - это объявление XML. Тег person является корнем XML. Person имеет атрибут пола (gender).
**Пример:XML**

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

Для получения дополнительной информации о том, как читать файл XML, смотрите [документацию](https://docs.python.org/2/library/xml.etree.elementtree.html)

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
# вывод
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

🌕 Ты делаешь большой прогресс. Сохраняй импульс, продолжай в том же духе. Теперь выполни несколько упражнений для своего мозга и мышц.

## 💻 Упражнения: День 19

### Упражнения: Уровень 1

1. Напиши функцию, которая подсчитывает количество строк и количество слов в тексте. Все файлы находятся в папке data:
   1) Прочитай файл obama_speech.txt и подсчитай количество строк и слов
   2) Прочитай файл michelle_obama_speech.txt и подсчитай количество строк и слов
   3) Прочитай файл donald_speech.txt и подсчитай количество строк и слов
   4) Прочитай файл melina_trump_speech.txt и подсчитай количество строк и слов
2. Прочитай файл данных countries_data.json в каталоге data, создай функцию, которая находит десять самых распространённых языков

   ```py
   # Ваш вывод должен выглядеть так
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

   # Ваш вывод должен выглядеть так
   print(most_spoken_languages(filename='./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. Прочитай файл данных countries_data.json в каталоге data, создай функцию, которая создаёт список десяти самых населённых стран

   ```py
   # Ваш вывод должен выглядеть так
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

   # Ваш вывод должен выглядеть так

   print(most_populated_countries(filename='./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

### Упражнения: Уровень 2

1. Извлеки все входящие адреса электронной почты в виде списка из файла email_exchange_big.txt.
2. Найди наиболее распространённые слова в английском языке. Назови имя своей функции find_most_common_words, она будет принимать два параметра - строку или файл и положительное целое число, указывающее количество слов. Твоя функция вернёт массив кортежей в порядке убывания. Проверь вывод

```py
    # Ваш вывод должен выглядеть так
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

    # Ваш вывод должен выглядеть так
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. Используй функцию find_most_frequent_words, чтобы найти:
   1) Десять наиболее часто используемых слов в [речи Обамы](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   2) Десять наиболее часто используемых слов в [речи Мишель](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   3) Десять наиболее часто используемых слов в [речи Трампа](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   4) Десять наиболее часто используемых слов в [речи Мелины](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
4. Напиши приложение на Python, которое проверяет сходство между двумя текстами. Оно принимает файл или строку в качестве параметра и оценивает сходство двух текстов. Например, проверь сходство между стенограммами речей [Мишель](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) и [Мелины](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt). Тебе может понадобиться пара функций: функция для очистки текста (clean_text), функция для удаления стоп-слов (remove_support_words) и, наконец, функция для проверки сходства (check_text_similarity). Список [стоп-слов](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) находится в каталоге data
5. Найди 10 наиболее повторяющихся слов в файле romeo_and_juliet.txt
6. Прочитай [файл hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) и выясни:
   1) Подсчитай количество строк, содержащих python или Python
   2) Подсчитай количество строк, содержащих JavaScript, javascript или Javascript
   3) Подсчитай количество строк, содержащих Java и не JavaScript

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 18](../18_Day_Regular_expressions/18_regular_expressions.md) | [День 20 >>](../20_Day_Python_package_manager/20_python_package_manager.md)

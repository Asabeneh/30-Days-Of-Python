<div align="center">
  <h1> 30 Days Of Python: День 19 - Работа с файлами </h1>
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

[<< День 18](./18_regular_expressions_ru.md) | [День 20 >>](./20_python_package_manager_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

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
    - [Упражнения: уровень 1](#упражнения-уровень-1)
    - [Упражнения: уровень 2](#упражнения-уровень-2)
    - [Упражнения: уровень 3](#упражнения-уровень-3)

# 📘 День 19

## Работа с файлами

До сих пор мы рассматривали различные типы данных Python. Обычно мы храним наши данные в разных форматах файлов. Помимо работы с файлами, в этом разделе мы также рассмотрим различные форматы файлов (.txt, .json, .xml, .csv, .tsv, .excel). Сначала давайте познакомимся с работой с файлами распространённого формата (.txt).

Работа с файлами — важная часть программирования, которая позволяет нам создавать, читать, обновлять и удалять файлы. В Python для работы с данными мы используем встроенную функцию _open()_.

```py
# Синтаксис
open('filename', mode) # mode(r, a, w, x, t,b) может означать чтение, запись, обновление
```

- "r" - Read - Значение по умолчанию. Открывает файл для чтения, возвращает ошибку, если файл не существует
- "a" - Append - Открывает файл для добавления в конец, создаёт файл, если он не существует
- "w" - Write - Открывает файл для записи, создаёт файл, если он не существует
- "x" - Create - Создаёт указанный файл, возвращает ошибку, если файл существует
- "t" - Text - Значение по умолчанию. Текстовый режим
- "b" - Binary - Бинарный режим (например, изображения)

### Открытие файлов для чтения

Режим _open_ по умолчанию — чтение, поэтому нам не нужно указывать 'r' или 'rt'. Я создал и сохранил файл с именем reading_file_example.txt в каталоге files. Давайте посмотрим, как это делается:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

Как видно из примера выше, я вывел открытый файл, и он дал некоторую информацию о нём. У открытого файла есть разные методы чтения: _read()_, _readline_, _readlines_. Открытый файл нужно закрывать методом _close()_.

- _read()_: читает весь текст как строку. Если мы хотим ограничить количество символов, которое хотим прочитать, мы можем ограничить его, передав целое число в метод *read(number)*.

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

Вместо того чтобы выводить весь текст, давайте выведем первые 10 символов текстового файла.

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

Другой способ получить все строки в виде списка — использовать _splitlines()_:

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

После того как мы открыли файл, мы должны его закрыть. Существует высокая склонность забывать закрывать их. Есть новый способ открытия файлов с помощью _with_ — он закрывает файлы сам. Давайте перепишем предыдущий пример с помощью метода _with_:

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

Чтобы записать в существующий файл, мы должны добавить режим как параметр в функцию _open()_:

- "a" - append — добавит в конец файла, если файл не существует, создаст новый файл.
- "w" - write — перезапишет любое существующее содержимое, если файл не существует, создаст его.

Давайте добавим немного текста в файл, который мы читали:

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

В предыдущем разделе мы видели, как создать и удалить каталог с помощью модуля _os_. Снова теперь: если мы хотим удалить файл, мы используем модуль _os_.

```py
import os
os.remove('./files/example.txt')

```

Если файл не существует, метод remove вызовет ошибку, поэтому хорошо использовать условие вроде этого:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## Типы файлов

### Файл с расширением txt

Файл с расширением _txt_ — очень распространённая форма данных, и мы рассмотрели её в предыдущем разделе. Давайте перейдём к файлу JSON

### Файл с расширением json

JSON расшифровывается как JavaScript Object Notation. На самом деле это строковое представление объекта JavaScript или словаря Python.

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

# мы используем три кавычки и делаем его многострочным, чтобы он был более читаемым
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
# давайте изменим JSON на словарь
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
person_json = json.dumps(person, indent=4) # indent может быть 2, 4, 8. Это делает json красивее
print(type(person_json))
print(person_json)
```

```sh
# вывод
# когда вы выводите его, в нём нет кавычек, но на самом деле это строка
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

Мы также можем сохранить наши данные как файл json. Давайте сохраним их как файл json, выполнив следующие шаги. Для записи файла json мы используем метод json.dump(), он может принимать словарь, выходной файл, ensure_ascii и indent.

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

В коде выше мы используем кодировку и отступы. Отступы делают файл json легко читаемым.

### Файл с расширением csv

CSV расшифровывается как comma separated values (значения, разделённые запятыми). CSV — простой формат файла, используемый для хранения табличных данных, таких как электронная таблица или база данных. CSV — очень распространённый формат данных в науке о данных.

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

Чтобы читать файлы excel, нам нужно установить пакет _xlrd_. Мы рассмотрим это после того, как рассмотрим установку пакетов с помощью pip.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### Файл с расширением xml

XML — ещё один формат структурированных данных, который выглядит как HTML. В XML теги не предопределены. Первая строка — объявление XML. Тег person является корнем XML. У person есть атрибут gender.
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

Для получения дополнительной информации о том, как читать XML-файл, смотрите [документацию](https://docs.python.org/2/library/xml.etree.elementtree.html)

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

🌕 Вы делаете большой прогресс. Поддерживайте импульс, продолжайте хорошую работу. Теперь сделайте несколько упражнений для мозга и мышц.

## 💻 Упражнения: День 19

### Упражнения: уровень 1

1. Напишите функцию, которая считает количество строк и количество слов в тексте. Все файлы находятся в папке data:
   1) Прочитайте файл obama_speech.txt и посчитайте количество строк и слов
   2) Прочитайте файл michelle_obama_speech.txt и посчитайте количество строк и слов
   3) Прочитайте файл donald_speech.txt и посчитайте количество строк и слов
   4) Прочитайте файл melina_trump_speech.txt и посчитайте количество строк и слов
2. Прочитайте файл данных countries_data.json в каталоге data, создайте функцию, которая находит десять самых распространённых языков

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

3. Прочитайте файл данных countries_data.json в каталоге data, создайте функцию, которая создаёт список десяти самых населённых стран

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

### Упражнения: уровень 2

1. Извлеките все входящие адреса электронной почты в виде списка из файла email_exchange_big.txt.
2. Найдите самые распространённые слова в английском языке. Назовите вашу функцию find_most_common_words, она будет принимать два параметра — строку или файл и положительное целое число, указывающее количество слов. Ваша функция вернёт массив кортежей в порядке убывания. Проверьте вывод

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

3. Используйте функцию find_most_frequent_words, чтобы найти:
   1) Десять самых частых слов, использованных в [речи Обамы](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   2) Десять самых частых слов, использованных в [речи Мишель](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   3) Десять самых частых слов, использованных в [речи Трампа](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   4) Десять самых частых слов, использованных в [речи Мелины](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
4. Напишите приложение на python, которое проверяет сходство между двумя текстами. Оно принимает файл или строку как параметр и оценивает сходство двух текстов. Например, проверьте сходство между стенограммами речи [Мишель](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) и [Мелины](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt). Возможно, вам понадобится несколько функций: функция для очистки текста (clean_text), функция для удаления служебных слов (remove_support_words) и, наконец, проверка сходства (check_text_similarity). Список [стоп-слов](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) находится в каталоге data
5. Найдите 10 самых повторяющихся слов в romeo_and_juliet.txt
6. Прочитайте [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) файл и выясните:
   1) Посчитайте количество строк, содержащих python или Python
   2) Посчитайте количество строк, содержащих JavaScript, javascript или Javascript
   3) Посчитайте количество строк, содержащих Java и не содержащих JavaScript

🎉 ПОЗДРАВЛЯЮ ! 🎉

[<< День 18](./18_regular_expressions_ru.md) | [День 20 >>](./20_python_package_manager_ru.md)

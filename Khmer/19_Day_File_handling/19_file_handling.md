<div align="center">
  <h1> 30 Days Of Python: Day 19 - File Handling </h1>
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

[<< Day 18](../18_Day_Regular_expressions/18_regular_expressions.md) | [Day 20 >>](../20_Day_Python_package_manager/20_python_package_manager.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 19](#-day-19)
  - [File Handling](#file-handling)
    - [Opening Files for Reading](#opening-files-for-reading)
    - [Opening Files for Writing and Updating](#opening-files-for-writing-and-updating)
    - [Deleting Files](#deleting-files)
  - [File Types](#file-types)
    - [File with txt Extension](#file-with-txt-extension)
    - [File with json Extension](#file-with-json-extension)
    - [Changing JSON to Dictionary](#changing-json-to-dictionary)
    - [Changing Dictionary to JSON](#changing-dictionary-to-json)
    - [Saving as JSON File](#saving-as-json-file)
    - [File with csv Extension](#file-with-csv-extension)
    - [File with xlsx Extension](#file-with-xlsx-extension)
    - [File with xml Extension](#file-with-xml-extension)
  - [💻 Exercises: Day 19](#-exercises-day-19)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 19

## File Handling

file = ឯកសារ

រហូតមកដល់ពេលនេះយើងបានឃើញប្រភេទទិន្នន័យ Python ផ្សេងៗច្រើន។ យើងជាធម្មតារក្សាទិន្នន័យរបស់យើងនៅក្នុងទ្រង់ទ្រាយ file ផ្សេងៗ។ ក្រៅពីការគ្រប់គ្រង file, យើងក៏នឹងឃើញទ្រង់ទ្រាយ file ផ្សេងៗ (.txt, .json, .xml, .csv, .tsv, .excel) នៅក្នុងផ្នែកនេះ។ ដំបូងយើងត្រូវយល់ដឹងអំពីការគ្រប់គ្រង file ដែលគេប្រើច្រើនជាងគេ ដែលមានទ្រង់ទ្រាយជា (.txt).

ការគ្រប់គ្រង file គឺជាផ្នែកសំខាន់មួយនៃ programming ដែលអនុញ្ញាតឱ្យយើងបង្កើត, អាន, កែ, និងលុប file។ នៅក្នុង Python ដើម្បីគ្រប់គ្រងទិន្នន័យយើងប្រើ _open()_ built-in function ។

```py
# Syntax
open('filename', mode) # mode(r, a, w, x, t, b)  អាចជា អាន, សរសេរ, និង កែ
```

- "r" - Read អាន - លំនាំដើម។ បើក file ដើម្បីអាន, វាត្រឡប់មក error ប្រសិនបើ file មិនមាន។
- "a" - Append បន្ថែម - បើក file រសម្រាប់ការបន្ថែម, បង្កើត file ប្រសិនបើវាមិនមាន។
- "w" - Write សរសេរ - បើក file ដើម្បីសរសេរ, បង្កើត file ប្រសិនបើវាមិនមាន។
- "x" - create បង្កើត - បង្កើតឯកសារ វិលត្រឡប់មក error ប្រសិនបើ file មានស្រាប់ហើយ។
- "t" - Text អត្ថបទ - លំនាំដើម។ របៀបអត្ថបទ។
- "b" - Binary គោលពីរ - របៀបគោលពីរ (e.g. images)

### Opening Files for Reading

លំនាំដើមនៃ _open_ គឺការអាន, ដូច្នេះយើងមិនចាំបាច់បញ្ជាក់ 'r' ឬ 'rt'. ខ្ញុំបានបង្កើតនិងបន្សំ file ដែលមានឈ្មោះ reading_file_example.txt នៅក្នុង files directory។ សូមមើលថា តើធ្វើយ៉ាងដូចម្តេច៖

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

ដូចដែលអ្នកអាចមើលឃើញក្នុងឧទាហរណ៍ខាងលើ ខ្ញុំបានបើក file ហើយបានផ្តល់ព័ត៌មានខ្លះអំពីវា។ File ដែលបានបើកមានវិធីអានផ្សេងៗ: _read()_, _readline_, _readlines_. File ដែលបើកត្រូវបិទដោយ _close()_ ។

- _read()_: អានអត្ថបទទាំងមូលជា string។ ប្រសិនបើយើងចង់កំណត់ចំនួនអក្សរដែលយើងចង់អាន យើងអាចកំណត់វាដោយផ្ទេរតម្លៃ int ទៅកាន់វិធី _read(number)_ ។

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

ដើម្បីកុំ print អក្សរទាំងអស់។ យើងនឹងបង្ហាញអក្សរ 10 ដំបូងនៃ file អក្សរ។

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# output
<class 'str'>
This is an
```

- _readline()_: អានតែខ្សែទីមួយប៉ុណ្ណោះ

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: អានអក្សរទាំងអស់តាមខ្សែ និងត្រឡប់មកវិញ list នៃខ្សែអត្ថបទ។

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

វិធីមួយទៀតដើម្បីទទួលបាន list នៃខ្សែអត្ថប គឺប្រើ _splitlines()_:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

ន្ទាប់ពីយើងបើក file មួយ យើងត្រូវបិទវា។ យើងមានលក្ខណៈងាយស្រួលក្នុងការភ្លេចបិទវា។ មានវិធីថ្មីក្នុងការបើក file ដោយប្រើ _with_ - បិទឯកសារដោយខ្លួនឯង។ សូមយើងសរសេរឡើងវិញឧទាហរណ៍មុនជាមួយវិធីសាស្ត្រ _with_:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Opening Files for Writing and Updating

ដើម្បីសរសេរទៅលើ file ដែលមានរួចមកហើយ យើងត្រូវបន្ថែម mode ជា parameter ទៅលើ function _open()_:

- "a" - append បន្ថែម - នឹងបន្ថែមទៅចុងនៃ file ប្រសិនបើ file មិនមាន វាបង្កើត file ថ្មី។
- "w" - write សរសេរ - នឹងសរសេរជាន់លើរាល់អ្វីដែលមានស្រាប់ បើសិនជាវាមិនមាន file វាបង្កើត file ថ្មី។

យើងអាចបន្ថែមអត្ថបទទៅនឹង file ដែលយើងកំពុងប្រើ:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

វិធីខាងក្រោមនេះបង្កើត file ថ្មី ប្រសិនបើ file មិនមាន:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### Deleting Files

យើងបានឃើញនៅក្នុងផ្នែកមុន, របៀបបង្កើត និងលុប directory មួយដោយប្រើ _os_ module ។ ម្តងទៀត ឥឡូវនេះ, ប្រសិនបើយើងចង់លុប file មួយយើងប្រើ _os_ module

```py
import os
os.remove('./files/example.txt')

```

ប្រសិនបើ file មិនមាន, នោះ remove method នឹងបង្ហាញ error ដូច្នេះវាជាការល្អក្នុងការប្រើលក្ខខណ្ឌដូចខាងក្រោមនេះ:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## File Types

### File with txt Extension

file ដែលមាន _txt_ extension គឺជាទម្រង់ទិន្នន័យ ដែលគេប្រើច្រើនជាងគេ។ នាំយើងទៅកាន់ JSON file វិញ។

### File with json Extension

JSON មានន័យថា JavaScript Object Notation. ជាការពិតវាជា stringified JavaScript object ឬ Python dictionary.

_Example:_

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

# យើងប្រើ quote ' 3 និងធ្វើវាជាច្រើនខ្សែ ដើម្បីធ្វើអោយវាស្រួលអាន
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### Changing JSON to Dictionary

ដើម្បីផ្លាស់ប្តូរ JSON ទៅជា dictionary, ជាមុន import json module ហើយបន្ទាប់មកយើងប្រើវិធីសាស្ត្រ _loads_ ។

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# សូមផ្លាស់ប្តូរ JSON ទៅ dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# output
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### Changing Dictionary to JSON

ដើម្បីផ្លាស់ប្តូរ dictionary ទៅជា JSON យើងប្រើ _dumps_ method មកពី json module.

```py
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# សូមបម្លែងវាទៅជា json
person_json = json.dumps(person, indent=4)
print(type(person_json))
print(person_json)
```

```sh
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

### Saving as JSON File

យើងក៏អាចរក្សាទិន្នន័យរបស់យើងបានផងដែរជា json file។ នាំយើងរក្សាជា json file ដោយប្រើវិធីខាងក្រោមនេះ។ សម្រាប់ការសរសេរ json file, យើងប្រើ json.dump() method, វាអាចយកបាន dictionary, output file, ensure_ascii និង indent.

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

នៅក្នុង code ខាងលើយើងប្រើ encoding និង indentation. Indentation ធ្វើអោយ json file ងាយស្រួលអាន។

### File with csv Extension

CSV មានន័យថា comma separated values។ CSV គឺជាទម្រង់ file សាមញ្ញដែលប្រើដើម្បីរក្សាទិន្នន័យតារាងដូចជា spreadsheet ឬ database ។ CSV គឺជាទម្រង់ទិន្នន័យដែលប្រើច្រើនក្នុង data science។

**Example:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**Example:**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
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
# output:
Column names are :name, country, city, skills
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines:  2
```

### File with xlsx Extension

ដើម្បីអាន excel file យើងត្រូវបញ្ចូល _xlrd_ package។ យើងនឹងពិនិត្យមើលរឿងនេះបន្ទាប់ពីយើងពិនិត្យមើល ការបញ្ចូល package ប្រើ pip។

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### File with xml Extension

XML ជាទិន្នន័យដែលមានរចនាសម្ព័ន្ធមួយទៀតដែលមើលទៅដូចជា HTML។ ក្នុង XML, tags មិនត្រូវបានកំណត់ជាមុន។ ខ្សែដំបូងគឺ ការប្រកាស XML។ person tag iគឺជាមូលនៃ XML ។ person មានទិន្នន័យជាភេទ។
**Example:XML**

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

សម្រាប់ព័ត៌មានបន្ថែមអំពីរបៀបអានឯកសារ XML សូមមើល [documentation](https://docs.python.org/2/library/xml.etree.elementtree.html)

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
# output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```
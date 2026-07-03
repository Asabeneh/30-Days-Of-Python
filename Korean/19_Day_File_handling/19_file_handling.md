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

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 19](#-day-19)
  - [파일 처리](#파일-처리)
    - [읽기용 파일 열기](#읽기용-파일-열기)
    - [쓰기 및 업데이트용 파일 열기](#쓰기-및-업데이트용-파일-열기)
    - [파일 삭제하기](#파일-삭제하기)
  - [파일 유형](#파일-유형)
    - [txt 확장자 파일](#txt-확장자-파일)
    - [json 확장자 파일](#json-확장자-파일)
    - [JSON을 딕셔너리로 변환하기](#json을-딕셔너리로-변환하기)
    - [딕셔너리를 JSON으로 변환하기](#딕셔너리를-json으로-변환하기)
    - [JSON 파일로 저장하기](#json-파일로-저장하기)
    - [csv 확장자 파일](#csv-확장자-파일)
    - [xlsx 확장자 파일](#xlsx-확장자-파일)
    - [xml 확장자 파일](#xml-확장자-파일)
  - [💻 연습문제: Day 19](#-연습문제-day-19)
    - [연습문제: Level 1](#연습문제-level-1)
    - [연습문제: Level 2](#연습문제-level-2)
    - [연습문제: Level 3](#연습문제-level-3)

# 📘 Day 19

## 파일 처리

지금까지 다양한 Python 데이터 타입을 살펴보았습니다. 일반적으로 데이터를 다양한 파일 형식으로 저장합니다. 파일을 처리하는 것 외에도 이 섹션에서는 다양한 파일 형식(.txt, .json, .xml, .csv, .tsv, .excel)도 살펴볼 것입니다. 먼저 일반적인 파일 형식(.txt)으로 파일 처리에 익숙해져 봅시다.

파일 처리는 파일을 생성, 읽기, 업데이트 및 삭제할 수 있게 해주는 프로그래밍의 중요한 부분입니다. Python에서 데이터를 처리하기 위해 _open()_ 내장 함수를 사용합니다.

```py
# 구문
open('filename', mode) # mode(r, a, w, x, t,b)는 읽기, 쓰기, 업데이트를 위한 것입니다
```

- "r" - Read - 기본값. 읽기용으로 파일을 엽니다. 파일이 존재하지 않으면 오류를 반환합니다
- "a" - Append - 추가용으로 파일을 엽니다. 파일이 존재하지 않으면 파일을 생성합니다
- "w" - Write - 쓰기용으로 파일을 엽니다. 파일이 존재하지 않으면 파일을 생성합니다
- "x" - Create - 지정된 파일을 생성합니다. 파일이 이미 존재하면 오류를 반환합니다
- "t" - Text - 기본값. 텍스트 모드
- "b" - Binary - 바이너리 모드 (예: 이미지)

### 읽기용 파일 열기

_open_의 기본 모드는 읽기이므로 'r' 또는 'rt'를 지정할 필요가 없습니다. files 디렉토리에 reading_file_example.txt라는 파일을 생성하고 저장했습니다. 어떻게 하는지 확인해 봅시다:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

위의 예시에서 볼 수 있듯이 열린 파일을 출력하면 파일에 대한 정보를 제공합니다. 열린 파일에는 다양한 읽기 메서드가 있습니다: _read()_, _readline_, _readlines_. 열린 파일은 _close()_ 메서드로 닫아야 합니다.

- _read()_: 전체 텍스트를 문자열로 읽습니다. 읽고 싶은 문자 수를 제한하려면 *read(number)* 메서드에 int 값을 전달하여 제한할 수 있습니다.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# 출력
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

전체 텍스트를 출력하는 대신 텍스트 파일의 처음 10자를 출력해 봅시다.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# 출력
<class 'str'>
This is an
```

- _readline()_: 첫 번째 줄만 읽습니다

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# 출력
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: 모든 텍스트를 줄별로 읽고 줄의 리스트를 반환합니다

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# 출력
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

모든 줄을 리스트로 가져오는 또 다른 방법은 _splitlines()_를 사용하는 것입니다:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# 출력
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

파일을 열고 나면 닫아야 합니다. 파일을 닫는 것을 잊어버리는 경향이 높습니다. _with_를 사용하여 파일을 여는 새로운 방법이 있으며, 이는 파일을 자동으로 닫아줍니다. _with_ 메서드를 사용하여 이전 예시를 다시 작성해 봅시다:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# 출력
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### 쓰기 및 업데이트용 파일 열기

기존 파일에 쓰려면 _open()_ 함수에 매개변수로 모드를 추가해야 합니다:

- "a" - append - 파일의 끝에 추가합니다. 파일이 존재하지 않으면 새 파일을 생성합니다.
- "w" - write - 기존 내용을 모두 덮어씁니다. 파일이 존재하지 않으면 생성합니다.

읽고 있던 파일에 텍스트를 추가해 봅시다:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

아래 메서드는 파일이 존재하지 않으면 새 파일을 생성합니다:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### 파일 삭제하기

이전 섹션에서 _os_ 모듈을 사용하여 디렉토리를 만들고 제거하는 방법을 보았습니다. 다시 파일을 제거하려면 _os_ 모듈을 사용합니다.

```py
import os
os.remove('./files/example.txt')

```

파일이 존재하지 않으면 remove 메서드가 오류를 발생시키므로 다음과 같은 조건을 사용하는 것이 좋습니다:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## 파일 유형

### txt 확장자 파일

_txt_ 확장자를 가진 파일은 매우 일반적인 데이터 형식이며 이전 섹션에서 다루었습니다. JSON 파일로 넘어가 봅시다.

### json 확장자 파일

JSON은 JavaScript Object Notation의 약자입니다. 실제로는 문자열화된 JavaScript 객체 또는 Python 딕셔너리입니다.

_예시:_

```py
# 딕셔너리
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: 딕셔너리의 문자열 형태
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# 삼중 따옴표를 사용하여 여러 줄로 만들어 더 읽기 쉽게 합니다
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### JSON을 딕셔너리로 변환하기

JSON을 딕셔너리로 변경하려면 먼저 json 모듈을 임포트한 다음 _loads_ 메서드를 사용합니다.

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# JSON을 딕셔너리로 변환합니다
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# 출력
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### 딕셔너리를 JSON으로 변환하기

딕셔너리를 JSON으로 변경하려면 json 모듈의 _dumps_ 메서드를 사용합니다.

```py
import json
# Python 딕셔너리
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# JSON으로 변환합니다
person_json = json.dumps(person, indent=4) # indent는 2, 4, 8이 될 수 있습니다. JSON을 보기 좋게 만들어줍니다
print(type(person_json))
print(person_json)
```

```sh
# 출력
# 출력할 때 따옴표가 없지만 실제로는 문자열입니다
# JSON은 타입이 없으며 문자열 타입입니다.
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

### JSON 파일로 저장하기

데이터를 json 파일로도 저장할 수 있습니다. 다음 단계를 사용하여 json 파일로 저장해 봅시다. json 파일을 쓰기 위해 json.dump() 메서드를 사용하며 딕셔너리, 출력 파일, ensure_ascii 및 indent를 받을 수 있습니다.

```py
import json
# Python 딕셔너리
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

위의 코드에서 인코딩과 들여쓰기를 사용합니다. 들여쓰기는 json 파일을 읽기 쉽게 만들어줍니다.

### csv 확장자 파일

CSV는 comma separated values(쉼표로 구분된 값)의 약자입니다. CSV는 스프레드시트나 데이터베이스와 같은 표 형식 데이터를 저장하는 데 사용되는 간단한 파일 형식입니다. CSV는 데이터 과학에서 매우 일반적인 데이터 형식입니다.

**예시:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**예시:**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # reader 메서드를 사용하여 csv를 읽습니다
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
# 출력:
Column names are :name, country, city, skills
Number of lines:  1
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines:  2
```

### xlsx 확장자 파일

Excel 파일을 읽으려면 _xlrd_ 패키지를 설치해야 합니다. pip를 사용한 패키지 설치를 다룬 후에 이를 다룰 것입니다.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### xml 확장자 파일

XML은 HTML과 비슷한 또 다른 구조화된 데이터 형식입니다. XML에서는 태그가 미리 정의되지 않습니다. 첫 번째 줄은 XML 선언입니다. person 태그는 XML의 루트입니다. person은 gender 속성을 가지고 있습니다.
**예시:XML**

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

XML 파일을 읽는 방법에 대한 자세한 정보는 [문서](https://docs.python.org/2/library/xml.etree.elementtree.html)를 확인하세요.

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
# 출력
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

🌕 큰 발전을 이루고 있습니다. 모멘텀을 유지하고 좋은 작업을 계속하세요. 이제 두뇌와 근육을 위한 연습을 해보세요.

## 💻 연습문제: Day 19

### 연습문제: Level 1

1. 텍스트의 줄 수와 단어 수를 세는 함수를 작성하세요. 모든 파일은 data 폴더에 있습니다:
   1) obama_speech.txt 파일을 읽고 줄 수와 단어 수를 세세요
   2) michelle_obama_speech.txt 파일을 읽고 줄 수와 단어 수를 세세요
   3) donald_speech.txt 파일을 읽고 줄 수와 단어 수를 세세요
   4) melina_trump_speech.txt 파일을 읽고 줄 수와 단어 수를 세세요
2. data 디렉토리의 countries_data.json 데이터 파일을 읽고 가장 많이 사용되는 10개의 언어를 찾는 함수를 만드세요

   ```py
   # 출력은 다음과 같아야 합니다
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

   # 출력은 다음과 같아야 합니다
   print(most_spoken_languages(filename='./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. data 디렉토리의 countries_data.json 데이터 파일을 읽고 인구가 가장 많은 10개 국가의 리스트를 만드는 함수를 만드세요

   ```py
   # 출력은 다음과 같아야 합니다
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

   # 출력은 다음과 같아야 합니다

   print(most_populated_countries(filename='./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

### 연습문제: Level 2

1. email_exchange_big.txt 파일에서 수신 이메일 주소를 모두 리스트로 추출하세요.
2. 영어에서 가장 흔한 단어를 찾으세요. 함수 이름을 find_most_common_words로 하고 두 개의 매개변수를 받습니다 - 문자열 또는 파일과 양의 정수(단어 수). 함수는 내림차순으로 튜플의 배열을 반환합니다. 출력을 확인하세요

```py
    # 출력은 다음과 같아야 합니다
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

    # 출력은 다음과 같아야 합니다
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. find_most_frequent_words 함수를 사용하여 다음을 찾으세요:
   1) [Obama의 연설](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)에서 가장 자주 사용된 10개의 단어
   2) [Michelle의 연설](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)에서 가장 자주 사용된 10개의 단어
   3) [Trump의 연설](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)에서 가장 자주 사용된 10개의 단어
   4) [Melina의 연설](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)에서 가장 자주 사용된 10개의 단어
4. 두 텍스트 간의 유사성을 확인하는 Python 애플리케이션을 작성하세요. 파일 또는 문자열을 매개변수로 받아 두 텍스트의 유사성을 평가합니다. 예를 들어 [Michelle의](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) 연설과 [Melina의](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) 연설 사이의 유사성을 확인하세요. 텍스트를 정리하는 함수(clean_text), 보조 단어를 제거하는 함수(remove_support_words), 유사성을 확인하는 함수(check_text_similarity) 등 몇 가지 함수가 필요할 수 있습니다. [불용어](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) 목록은 data 디렉토리에 있습니다
5. romeo_and_juliet.txt에서 가장 많이 반복되는 10개의 단어를 찾으세요
6. [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) 파일을 읽고 다음을 확인하세요:
   1) python 또는 Python을 포함하는 줄 수를 세세요
   2) JavaScript, javascript 또는 Javascript를 포함하는 줄 수를 세세요
   3) Java를 포함하고 JavaScript는 포함하지 않는 줄 수를 세세요

🎉 축하합니다! 🎉

[<< Day 18](../18_Day_Regular_expressions/18_regular_expressions.md) | [Day 20 >>](../20_Day_Python_package_manager/20_python_package_manager.md)

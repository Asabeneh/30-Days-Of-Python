<div align="center">
  <h1> 30 Days Of Python: Day 18 - Regular Expressions </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> First Edition: Nov 22 - Dec 22, 2019</small>
  </sub>
</div>


[<< Day 17](../17_Day_Exception_handling/17_exception_handling.md) | [Day 19>>](../19_Day_File_handling/19_file_handling.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 18](#-day-18)
  - [정규 표현식](#정규-표현식)
    - [*re* 모듈](#re-모듈)
    - [*re* 모듈의 메서드](#re-모듈의-메서드)
      - [Match](#match)
      - [Search](#search)
      - [*findall*을 사용하여 모든 일치 항목 검색하기](#findall을-사용하여-모든-일치-항목-검색하기)
      - [부분 문자열 대체하기](#부분-문자열-대체하기)
  - [RegEx Split을 사용한 텍스트 분할](#regex-split을-사용한-텍스트-분할)
  - [RegEx 패턴 작성하기](#regex-패턴-작성하기)
    - [대괄호](#대괄호)
    - [RegEx의 이스케이프 문자(\\)](#regex의-이스케이프-문자)
    - [한 번 이상(+)](#한-번-이상)
    - [마침표(.)](#마침표)
    - [0번 이상(\\*)](#0번-이상)
    - [0번 또는 한 번(?)](#0번-또는-한-번)
    - [RegEx의 수량자](#regex의-수량자)
    - [캐럿 ^](#캐럿-)
  - [💻 연습문제: Day 18](#-연습문제-day-18)
    - [연습문제: Level 1](#연습문제-level-1)
    - [연습문제: Level 2](#연습문제-level-2)
    - [연습문제: Level 3](#연습문제-level-3)

# 📘 Day 18

## 정규 표현식

정규 표현식(Regular Expression) 또는 RegEx는 데이터에서 패턴을 찾는 데 도움이 되는 특별한 텍스트 문자열입니다. RegEx를 사용하여 다른 데이터 타입에서 어떤 패턴이 존재하는지 확인할 수 있습니다. Python에서 RegEx를 사용하려면 먼저 *re*라고 불리는 RegEx 모듈을 임포트해야 합니다.

### *re* 모듈

모듈을 임포트한 후 패턴을 감지하거나 찾는 데 사용할 수 있습니다.

```py
import re
```

### *re* 모듈의 메서드

패턴을 찾기 위해 문자열에서 일치하는 것을 검색할 수 있는 다양한 *re* 문자 집합을 사용합니다.

- *re.match()*: 문자열의 첫 번째 줄의 시작 부분에서만 검색하며 일치하는 객체가 발견되면 반환하고, 그렇지 않으면 None을 반환합니다.
- *re.search*: 여러 줄 문자열을 포함하여 문자열의 어디에서든 일치하는 객체가 있으면 반환합니다.
- *re.findall*: 모든 일치 항목을 포함하는 리스트를 반환합니다
- *re.split*: 문자열을 받아 일치 지점에서 분할하고 리스트를 반환합니다
- *re.sub*: 문자열 내에서 하나 또는 여러 일치 항목을 대체합니다

#### Match

```py
# 구문
re.match(substring, string, re.I)
# substring은 문자열 또는 패턴, string은 패턴을 찾을 텍스트, re.I는 대소문자 무시입니다
```

```py
import re

txt = 'I love to teach python and javaScript'
# span과 match가 있는 객체를 반환합니다
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# span을 사용하여 일치의 시작 및 끝 위치를 튜플로 가져올 수 있습니다
span = match.span()
print(span)     # (0, 15)
# span에서 시작 및 끝 위치를 찾아봅시다
start, end = span
print(start, end)  # 0 15
substring = txt[start:end]
print(substring)       # I love to teach
```

위의 예시에서 볼 수 있듯이, 찾고 있는 패턴(또는 찾고 있는 부분 문자열)은 *I love to teach*입니다. match 함수는 텍스트가 패턴으로 시작하는 경우**에만** 객체를 반환합니다.

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

문자열이 *I like to teach*로 시작하지 않으므로 일치하는 것이 없었고 match 메서드는 None을 반환했습니다.

#### Search

```py
# 구문
re.search(substring, string, re.I)
# substring은 패턴, string은 패턴을 찾을 텍스트, re.I는 대소문자 무시 플래그입니다
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# span과 match가 있는 객체를 반환합니다
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# span을 사용하여 일치의 시작 및 끝 위치를 튜플로 가져올 수 있습니다
span = match.span()
print(span)     # (100, 105)
# span에서 시작 및 끝 위치를 찾아봅시다
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

보시다시피 search는 텍스트 전체에서 패턴을 찾을 수 있기 때문에 match보다 훨씬 좋습니다. search는 처음 발견된 일치 항목으로 match 객체를 반환하고, 그렇지 않으면 *None*을 반환합니다. 훨씬 더 좋은 *re* 함수는 *findall*입니다. 이 함수는 전체 문자열에서 패턴을 확인하고 모든 일치 항목을 리스트로 반환합니다.

#### *findall*을 사용하여 모든 일치 항목 검색하기

*findall()*은 모든 일치 항목을 리스트로 반환합니다

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# 리스트를 반환합니다
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

보시다시피 *language*라는 단어가 문자열에서 두 번 발견되었습니다. 조금 더 연습해 봅시다.
이제 문자열에서 Python과 python 단어를 모두 찾아보겠습니다:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# 리스트를 반환합니다
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

*re.I*를 사용하고 있으므로 소문자와 대문자 모두 포함됩니다. re.I 플래그가 없으면 패턴을 다르게 작성해야 합니다. 확인해 봅시다:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

#### 부분 문자열 대체하기

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
# 또는
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
```

하나 더 예시를 추가해 봅시다. 다음 문자열은 % 기호를 제거하지 않으면 읽기가 정말 어렵습니다. %를 빈 문자열로 대체하면 텍스트가 깨끗해집니다.

```py

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

```sh
I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?
```

## RegEx Split을 사용한 텍스트 분할

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # \n - 줄 끝 기호를 사용하여 분할합니다
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## RegEx 패턴 작성하기

문자열 변수를 선언하려면 작은따옴표 또는 큰따옴표를 사용합니다. RegEx 변수를 선언하려면 *r''*을 사용합니다.
다음 패턴은 소문자 apple만 식별하며, 대소문자를 구분하지 않게 하려면 패턴을 다시 작성하거나 플래그를 추가해야 합니다.

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# 대소문자를 구분하지 않게 하기 위해 플래그를 추가합니다
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# 또는 문자 집합 방법을 사용할 수 있습니다
regex_pattern = r'[Aa]pple'  # 이는 첫 글자가 Apple 또는 apple일 수 있음을 의미합니다
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```

* []: 문자 집합
  - [a-c]는 a 또는 b 또는 c를 의미합니다
  - [a-z]는 a부터 z까지의 모든 문자를 의미합니다
  - [A-Z]는 A부터 Z까지의 모든 문자를 의미합니다
  - [0-3]은 0 또는 1 또는 2 또는 3을 의미합니다
  - [0-9]는 0부터 9까지의 모든 숫자를 의미합니다
  - [A-Za-z0-9]는 a부터 z, A부터 Z 또는 0부터 9까지의 모든 단일 문자를 의미합니다
- \\: 특수 문자를 이스케이프하는 데 사용합니다
  - \d는: 문자열에 숫자(0-9)가 포함된 곳과 일치합니다
  - \D는: 문자열에 숫자가 포함되지 않은 곳과 일치합니다
- . : 줄 바꿈 문자(\n)를 제외한 모든 문자
- ^: ~로 시작
  - r'^substring' 예: r'^love', love라는 단어로 시작하는 문장
  - r'[^abc]는 a가 아니고 b가 아니고 c가 아닌 것을 의미합니다.
- $: ~로 끝남
  - r'substring$' 예: r'love$', love라는 단어로 끝나는 문장
- *: 0번 이상
  - r'[a]*'는 a가 선택사항이거나 여러 번 나타날 수 있음을 의미합니다.
- +: 한 번 이상
  - r'[a]+'는 최소 한 번(또는 그 이상)을 의미합니다
- ?: 0번 또는 한 번
  - r'[a]?'는 0번 또는 한 번을 의미합니다
- {3}: 정확히 3자
- {3,}: 최소 3자
- {3,8}: 3~8자
- |: 또는
  - r'apple|banana'는 apple 또는 banana를 의미합니다
- (): 캡처 및 그룹화

![정규 표현식 치트 시트](../../images/regex.png)

위의 메타 문자를 명확히 하기 위해 예시를 사용해 봅시다

### 대괄호

소문자와 대문자를 포함하기 위해 대괄호를 사용해 봅시다

```py
regex_pattern = r'[Aa]pple' # 이 대괄호는 A 또는 a를 의미합니다
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

banana를 찾으려면 다음과 같이 패턴을 작성합니다:

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # 이 대괄호는 A 또는 a를 의미합니다
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

대괄호와 or 연산자를 사용하여 Apple, apple, Banana 및 banana를 추출할 수 있었습니다.

### RegEx의 이스케이프 문자(\\)

```py
regex_pattern = r'\d'  # d는 숫자를 의미하는 특수 문자입니다
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], 이것은 우리가 원하는 것이 아닙니다
```

### 한 번 이상(+)

```py
regex_pattern = r'\d+'  # d는 숫자를 의미하는 특수 문자, +는 한 번 이상을 의미합니다
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - 이제 더 좋습니다!
```

### 마침표(.)

```py
regex_pattern = r'[a].'  # 이 대괄호는 a를 의미하고 .은 줄 바꿈을 제외한 모든 문자를 의미합니다
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . 모든 문자, + 모든 문자 한 번 이상
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### 0번 이상(\*)

0번 또는 여러 번. 패턴이 나타나지 않을 수도 있고 여러 번 나타날 수도 있습니다.

```py
regex_pattern = r'[a].*'  # . 모든 문자, * 모든 문자 0번 이상
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### 0번 또는 한 번(?)

0번 또는 한 번. 패턴이 나타나지 않을 수도 있고 한 번 나타날 수도 있습니다.

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ?는 여기서 '-'이 선택사항임을 의미합니다
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### RegEx의 수량자

중괄호를 사용하여 텍스트에서 찾고 있는 부분 문자열의 길이를 지정할 수 있습니다. 길이가 4자인 부분 문자열에 관심이 있다고 상상해 봅시다:

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # 정확히 4번
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] 
```

### 캐럿 ^

- 시작

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^는 ~로 시작함을 의미합니다
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

- 부정

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # 문자 집합에서 ^는 부정을 의미합니다. A부터 Z가 아닌, a부터 z가 아닌, 공백이 아닌
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

## 💻 연습문제: Day 18

### 연습문제: Level 1

 1. 다음 문단에서 가장 빈도가 높은 단어는 무엇입니까?

```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```sh
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

2. 수평 x축에서 일부 입자의 위치는 음의 방향으로 -12, -4, -3, -1이고, 원점에서 0, 양의 방향으로 4와 8입니다. 이 전체 텍스트에서 이 숫자들을 추출하고 가장 먼 두 입자 사이의 거리를 구하세요.

```py
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20
```

### 연습문제: Level 2

1. 문자열이 유효한 Python 변수인지 식별하는 패턴을 작성하세요

    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```

### 연습문제: Level 3

1. 다음 텍스트를 정리하세요. 정리 후 문자열에서 가장 빈도가 높은 세 단어를 세세요.

    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```

🎉 축하합니다! 🎉

[<< Day 17](../17_Day_Exception_handling/17_exception_handling.md) | [Day 19>>](../19_Day_File_handling/19_file_handling.md)

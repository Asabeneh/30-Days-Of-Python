<div align="center">
<h1> 30 Days Of Python: Day 4 - Strings</h1> <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/"> <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social"> </a> <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh"> <img src="https://img.shields.io/twitter/follow/asabeneh?style=social" alt="Twitter Follow"> </a>
</div>
<p data-md-type="paragraph"><sub data-md-type="raw_html">Author: <a data-md-type="raw_html" href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br> <small data-md-type="raw_html"> Second Edition: July, 2021</small></sub></p>
<div data-md-type="block_html"></div>

[&lt;&lt; Day 3](../03_Day_Operators/03_operators.md) | [Day 5 &gt;&gt;](../05_Day_Lists/05_lists.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Day 4](#day-4)
    - [문자열](#strings)
        - [문자열 만들기](#문자열-만들기)
        - [문자열 연결](#문자열-연결)
        - [문자열의 이스케이프 시퀀스](#문자열의-이스케이프-시퀀스)
        - [문자열 포매팅](#문자열-포매팅)
            - [올드 스타일 문자열 포매팅(% 연산자)](#올드-스타일-문자열-포매팅%-연산자)
            - [새로운 스타일 문자열 포매팅(str.format)](#새로운-스타일-문자열-포매팅str.format)
            - [문자열 Interpolation / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
        - [문자 시퀀스로서의 Python 문자열](#문자-시퀀스로서의-Python-문자열)
            - [언패킹 문자](#언패킹-문자)
            - [인덱스로 문자열의 문자에 액세스](#인덱스로-문자열의-문자에-액세스)
            - [파이썬 문자열 슬라이싱](#파이썬-문자열-슬라이싱)
            - [문자열 리버스](#문자열-리버스)
            - [슬라이싱하는 동안 문자 건너뛰기](#슬라이싱하는-동안-문자-건너뛰기)
        - [문자열 메서드](#문자열-메서드)
    - [💻 Exercises - Day 4](#-exercises---day-4)

# Day 4

## 문자열

텍스트는 문자열 데이터 유형입니다. 텍스트로 작성된 모든 데이터 유형은 문자열입니다. 작은따옴표, 큰따옴표 또는 삼중따옴표 아래의 모든 데이터는 문자열입니다. 문자열 데이터 유형을 처리하기 위한 다양한 문자열 메서드와 내장 함수가 있습니다. 문자열의 길이를 확인하려면 len() 메서드를 사용하십시오.

### 문자열 만들기

```py
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
```

여러 줄 문자열은 세 개의 작은따옴표(''') 또는 세 개의 큰따옴표(""")를 사용하여 생성됩니다. 아래 예를 참조하십시오.

```py
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```

### 문자열 연결

문자열을 함께 연결할 수 있습니다. 문자열을 병합하거나 연결하는 것을 연결이라고 합니다. 아래 예를 참조하십시오.

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```

### 문자열의 이스케이프 시퀀스

Python 및 기타 프로그래밍 언어에서 \ 다음에 오는 문자는 이스케이프 시퀀스입니다. 가장 일반적인 이스케이프 문자를 살펴보겠습니다.

- \n: 새로운 라인
- \t: 탭은(8칸)을 의미합니다.
- \\: 백슬래시
- \': 작은따옴표(')
- \": 큰따옴표(")

이제 위의 이스케이프 시퀀스를 예제와 함께 사용하는 방법을 살펴보겠습니다.

```py
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
I hope every one is enjoying the Python Challenge.
Are you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

### 문자열 포매팅

#### 올드 스타일 문자열 형식화(% 연산자)

Python에는 문자열 형식을 지정하는 여러 가지 방법이 있습니다. 이 섹션에서는 그 중 일부를 다룰 것입니다. "%" 연산자는 "인수 지정자", "%s"와 같은 특수 기호와 함께 일반 텍스트를 포함하는 형식 문자열과 함께 "튜플"(고정 크기 목록)로 묶인 변수 세트의 형식을 지정하는 데 사용됩니다. , "%d", "%f", "%. <small>자릿수</small> f".

- %s - 문자열(또는 숫자와 같은 문자열 표현이 있는 모든 객체)
- %d - 정수
- %f - 부동 소수점 숫자
- "%. <small>number of digits</small> f" - 정밀도가 고정된 부동 소수점 숫자

```py
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
```

#### 새로운스타일 문자열 형식화(str.format)

이 형식은 Python 버전 3에서 도입되었습니다.

```py

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

```

#### 문자열 Interpolation / f-Strings (Python 3.6+)

또 다른 새로운 문자열 형식화는 문자열 보간법인 f-문자열입니다. 문자열은 f로 시작하고 해당 위치에 데이터를 주입할 수 있습니다.

```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

### 문자 시퀀스로서의 Python 문자열

Python 문자열은 문자 시퀀스이며, 기본 액세스 방법을 다른 Python 순서 객체 시퀀스(목록 및 튜플)와 공유합니다. 문자열(및 모든 시퀀스의 개별 멤버)에서 단일 문자를 추출하는 가장 간단한 방법은 해당 변수로 압축을 푸는 것입니다.

#### 언패킹 문자

```
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

#### 인덱스로 문자열의 문자에 액세스

프로그래밍에서 카운팅은 0부터 시작합니다. 따라서 문자열의 첫 번째 문자는 인덱스가 0이고 문자열의 마지막 문자는 문자열의 길이에서 1을 뺀 값입니다.

![String index](../images/string_index.png)

```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

오른쪽 끝에서 시작하려면 음수 인덱싱을 사용할 수 있습니다. -1은 마지막 인덱스입니다.

```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

#### 파이썬 문자열 슬라이싱

파이썬에서는 문자열을 하위 문자열로 슬라이스할 수 있습니다.

```py
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

#### <a>문자열 리버스</a>

파이썬에서 문자열을 쉽게 뒤집을 수 있습니다.

```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

#### 슬라이싱하는 동안 문자 건너뛰기

슬라이스 메소드에 단계 인수를 전달하여 슬라이스하는 동안 문자를 건너뛸 수 있습니다.

```py
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```

### 문자열 메서드

문자열을 형식화할 수 있는 많은 문자열 메서드가 있습니다. 다음 예제에서 일부 문자열 메서드를 참조하십시오.

- capitalize(): 문자열의 첫 번째 문자를 대문자로 변환

```py
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```

- count(): 문자열에서 하위 문자열의 발생을 반환합니다. count(substring, start=.., end=..). 시작은 카운트를 위한 시작 인덱싱이고 끝은 카운트할 마지막 인덱스입니다.

```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1,
print(challenge.count('th')) # 2`
```

- endswith(): 문자열이 지정된 끝으로 끝나는지 확인합니다.

```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

- expandtabs(): 탭 문자를 공백으로 바꿉니다. 기본 탭 크기는 8입니다. 탭 크기 인수를 사용합니다.

```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```

- find(): 하위 문자열이 처음 나타나는 인덱스를 반환합니다. 찾을 수 없으면 -1을 반환합니다.

```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1,
print(challenge.count('th')) # 2`
```

- rfind(): 하위 문자열이 마지막으로 나타나는 인덱스를 반환합니다. 찾을 수 없으면 -1을 반환합니다.

```py
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 5
print(challenge.rfind('th')) # 1
```

- format(): 문자열을 더 나은 출력으로 포맷합니다.<br> 문자열 형식에 대한 자세한 내용은 이 [링크](https://www.programiz.com/python-programming/methods/string/format) 를 확인하세요.

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```

- index(): 하위 문자열의 가장 낮은 색인을 반환하고 추가 인수는 시작 및 끝 색인을 나타냅니다(기본값 0 및 문자열 길이 - 1). 하위 문자열을 찾을 수 없으면 valueError가 발생합니다.

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
```

- rindex(): 하위 문자열의 가장 높은 색인을 반환합니다. 추가 인수는 시작 및 끝 색인을 나타냅니다(기본값 0 및 문자열 길이 - 1).

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error
```

- isalnum(): 영숫자 확인

```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```

- isalpha(): 모든 문자열 요소가 알파벳 문자(az 및 AZ)인지 확인합니다.

```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```

- isdecimal(): 문자열의 모든 문자가 십진수(0-9)인지 확인합니다.

```py
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
```

- isdigit(): 문자열의 모든 문자가 숫자인지 확인합니다(숫자는 0-9 및 일부 다른 유니코드 문자).

```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

- isnumeric(): 문자열의 모든 문자가 숫자인지 또는 숫자와 관련된 것인지 확인합니다(isdigit()와 마찬가지로 ½과 같은 더 많은 기호를 허용합니다).

```py
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

- isidentifier(): 유효한 식별자를 확인합니다. 문자열이 유효한 변수 이름인지 확인합니다.

```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

- islower(): 문자열의 모든 알파벳 문자가 소문자인지 확인

```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```

- islower(): 문자열의 모든 알파벳 문자가 소문자인지 확인

```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

- join(): 연결된 문자열을 반환합니다.

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
```

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

- strip(): 문자열의 시작과 끝에서 시작하여 주어진 모든 문자를 제거합니다.

```py
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
```

- replace(): 하위 문자열을 주어진 문자열로 대체합니다.

```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```

- split(): 주어진 문자열 또는 공백을 구분 기호로 사용하여 문자열을 분할합니다.

```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```

- title(): 제목 케이스 문자열을 반환합니다.

```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```

- swapcase(): 모든 대문자를 소문자로, 모든 소문자를 대문자로 변환

```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```

- startswith(): 문자열이 지정된 문자열로 시작하는지 확인

```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```

🌕 당신은 특별한 사람이고 놀라운 잠재력을 가지고 있습니다. 당신은 방금 4일 차 도전을 완료했고 당신은 위대함을 향한 당신의 길에 4걸음 남았습니다. 이제 뇌와 근육을 위한 몇 가지 훈련을 하십시오.

## 💻 Exercises - Day 4

1. 문자열 'Thirty', 'Days', 'Of', 'Python'을 단일 문자열 'Thirty Days Of Python'에 연결합니다.
2. 문자열 'Coding', 'For' , 'All'을 단일 문자열 'Coding For All'에 연결합니다.
3. company라는 변수를 선언하고 초기 값 "Coding For All"에 할당합니다.
4. *print()* 를 사용하여 회사 변수를 인쇄합니다.
5. *len()* 메서드와 *print()* 를 사용하여 회사 문자열의 길이를 인쇄합니다.
6. *upper()* 메서드를 사용하여 모든 문자를 대문자로 변경합니다.
7. *lower()* 메서드를 사용하여 모든 문자를 소문자로 변경합니다.
8. 문자열 *Coding For All* 의 값을 형식화하려면 capitalize(), title(), swapcase() 메소드를 사용하십시오.
9. *Coding For All* 문자열의 첫 번째 단어를 잘라냅니다.
10. Index, find 또는 기타 방법을 사용하여 *Coding For All* 문자열에 단어 Coding이 포함되어 있는지 확인합니다.
11. 문자열 'Coding For All'의 코딩이라는 단어를 Python으로 바꿉니다.
12. replace 메서드 또는 기타 메서드를 사용하여 모두를 위한 Python을 모두를 위한 Python으로 변경합니다.
13. 공백을 구분 기호로 사용하여 문자열 'Coding For All'을 분할합니다(split()).
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"은 쉼표에서 문자열을 나눕니다.
15. 문자열 *Coding For All* 에서 인덱스 0에 있는 문자는 무엇입니까?
16. 문자열 *Coding For All* 에서 인덱스 0에 있는 문자는 무엇입니까?
17. "Coding For All" 문자열에서 인덱스 10에 있는 문자는 무엇입니까?
18. 'Python For Everyone'이라는 이름의 약어 또는 약어를 만듭니다.
19. 'Coding For All'이라는 이름의 약어 또는 약어를 만듭니다.
20. Index를 사용하여 Coding For All에서 C가 처음 나타나는 위치를 결정합니다.
21. Index를 사용하여 Coding For All에서 F가 처음 나타나는 위치를 결정합니다.
22. Coding For All People에서 l이 마지막으로 나타나는 위치를 결정하려면 rfind를 사용하십시오.
23. 색인 또는 찾기를 사용하여 다음 문장에서 'because'라는 단어가 처음 나타나는 위치를 찾습니다.
24. 색인 또는 찾기를 사용하여 다음 문장에서 'because'라는 단어가 처음 나타나는 위치를 찾습니다.
25. 색인 또는 찾기를 사용하여 다음 문장에서 'because'라는 단어가 처음 나타나는 위치를 찾습니다.
26. 색인 또는 찾기를 사용하여 다음 문장에서 'because'라는 단어가 처음 나타나는 위치를 찾습니다.
27. 다음 문장에서 'because because because'라는 구문을 잘라냅니다.
28. 'Coding For All'은 하위 문자열 *Coding* 으로 시작합니까?
29. 'Coding For All'은 하위 문자열 *코딩* 으로 끝납니까?
30. ' Coding For All ' , 주어진 문자열에서 왼쪽 및 오른쪽 후행 공백을 제거합니다.
31. 다음 변수 중 isidentifier() 메서드를 사용할 때 True를 반환하는 변수는 무엇입니까?
    - 30DaysOfPython
    - thirty_days_of_python
32. 다음 목록에는 일부 파이썬 라이브러리의 이름이 포함되어 있습니다: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 공백 문자열이 있는 해시로 목록에 가입하십시오.
33. 새 줄 이스케이프 시퀀스를 사용하여 다음 문장을 구분합니다.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. 새 줄 이스케이프 시퀀스를 사용하여 다음 문장을 구분합니다.
    ```py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
    ```
35. 문자열 형식 지정 방법을 사용하여 다음을 표시합니다:

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```

1. 문자열 형식화 방법을 사용하여 다음을 작성하십시오:

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```

🎉 축하합니다! 🎉

[&lt;&lt; Day 3](../03_Day_Operators/03_operators.md) | [Day 5 &gt;&gt;](../05_Day_Lists/05_lists.md)

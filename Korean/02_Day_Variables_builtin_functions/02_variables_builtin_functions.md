<div align="center">
  <h1> 30 Days Of Python: Day 2 - 변수, 내장 함수</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 1](../readme.md) | [Day 3 >>](../03_Day_Operators/03_operators.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 2](#-day-2)
  - [내장 함수](#내장-함수)
  - [변수](#변수)
    - [한 줄로 여러개의 변수 선언](#한-줄로-여러개의-변수-선언)
  - [자료형](#자료형)
  - [자료형 확인 및 형변환](#자료형-확인-및-형변환)
  - [숫자](#숫자)
  - [💻 Exercises - Day 2](#-exercises---day-2)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)

# 📘 Day 2

## 내장 함수

파이썬에는 수많은 내장 함수가 있습니다. 내장 함수는 전역에서 사용 가능하고 그건 importing 이나 configuring없이 내장 함수를 사용 가능하다는 뜻입니다. 다음은 가장 자주 사용되는 파이썬 내장함수들 중 몇가지입니다: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, and _dir()_. 밑의 표에서 [파이썬 공식문서](https://docs.python.org/3.9/library/functions.html) 에 쓰여진 파이썬 내장 함수의 전체 목록을 볼 수 있습니다.

![Built-in Functions](../../images/builtin-functions.png)

파이썬 쉘을 열고 가장 자주 사용되는 내장 함수를 사용해봅시다.

![Built-in functions](../../images/builtin-functions_practice.png)

다른 내장 함수를 사용해 더 연습해봅시다.

![Help and Dir Built in Functions](../../images/help_and_dir_builtin.png)

위의 터미널에서 볼 수 있듯이, 파이썬에는 reserved word가 있습니다. reserved word는 변수나 함수를 선언할때 사용되지 않습니다. 변수에 관해서는 다음 장에서 다룰것입니다.

이제 당신은 내장 함수에 익숙해졌을 것이라 믿습니다. 한번 더 내장 함수의 연습을 하고 다음 장으로 넘어갑시다.
![Min Max Sum](../../images/builtin-functional-final.png)

## 변수

변수는 컴퓨터 메모리에 정보를 저장합니다. Mnemonic 변수는 많은 프로그래밍 언어에서 사용하도록 권장됩니다. Mnemonic 변수는 쉽게 기억하고 연관지을 수 있는 변수 이름입니다. 한 변수는 정보가 저장되어있는 메모리 주소를 참조합니다.
변수 이름을 지정할 때는 시작 부분의 숫자, 특수 문자, 하이픈을 사용할 수 없습니다. 변수는 짧은 이름(예: x, y, z)을 가질 수 있지만 더 변수에 대한 설명을 담은 이름(이름, 성, 나이, 국가)을 사용하는 것을 추천합니다.

파이썬 변수 이름 규칙

- 변수 이름은 문자 또는 밑줄 문자로 시작해야 합니다
- 변수 이름은 숫자로 시작할 수 없습니다 
- 변수 이름에는 알파벳과 숫자와 밑줄(A-z, 0-9 및 \_)만 사용할 수 있습니다 
- 변수 이름은 대소문자를 구분합니다(firstname, Firstname, FirstName, FIRSTNAME은 서로 다른 변수)

사용가능한 변수 이름들을 살펴봅시다

```shell
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # reserved word를 변수 이름으로 사용하고 싶은 경우
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

사용할 수 없는 변수 이름들

```shell
first-name
first@name
first$name
num-1
1num
```

우리는 많은 파이썬 개발자들이 채택한 표준 파이썬 변수 명명 방식을 사용할 것입니다. 파이썬 개발자들은 스네이크 케이스(snake_case) 변수 명명 규칙을 사용합니다. 우리는 두 개 이상의 단어를 포함하는 변수에 대해 각 단어 뒤에 밑줄 문자를 사용합니다(예: first_name, last_name, engine_rotation_speed). 아래 예제는 변수의 표준 명명 예제이며, 변수 이름이 둘 이상의 단어일 경우 밑줄이 필요합니다.

변수에 특정 데이터 유형을 할당할 때 이를 변수 선언이라고 합니다. 예를 들어 아래 예제에서 내 이름은 first_name 변수에 할당됩니다. 등호 기호는 할당 연산자입니다. 할당은 변수에 데이터를 저장하는 것을 의미합니다. 파이썬에서 등호 기호는 수학에서의 등호가 아닙니다.

_Example:_

```py
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

내장 함수인 _print()_ 와 _len()_ 을 사용해봅시다. Print 함수는 인자의 수에 제한이 없습니다. 인자는 함수 괄호 안에 넣어 전달할 수 있는 값입니다. 아래 예제를 봅시다.

**Example:**

```py
print('Hello, World!') # Hello, World! 라는 글이 하나의 인자입니다
print('Hello',',', 'World','!') # 여러개의 인자를 받을 수 있습니다, 네개의 인자가 넘겨졌습니다 
print(len('Hello, World!')) # 하나의 인자만을 받습니다
```

위에서 정의된 변수들을 찍어보고 길이를 찾아봅시다:

**Example:**

```py
# 변수에 저장된 값 찍기

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### 한 줄로 여러개의 변수 선언

하나의 줄에서 여러개의 변수를 선언할 수도 있습니다:

**Example:**

```py
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

내장 함수 _input()_ 을 사용해 사용자의 입력 받기. 사용자로부터 받은 정보를 first_name과 age 변수에 할당해봅시다.
**Example:**

```py
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
```

## 자료형

파이썬에는 몇 가지 자료형이 있습니다. 자료형을 식별하기 위해 내장 함수 _type()_ 을 사용합니다. 서로 다른 자료형을 잘 이해하는 데 집중해 주시기를 부탁드립니다. 프로그래밍에서 모든것은 자료형과 관련이 있습니다. 처음에 자료형을 소개했지만 모든 주제가 자료형과 관련이 있기 때문에 다시 나옵니다. 자료형에 대해서는 각 섹션에서 자세히 설명하겠습니다.

## 자료형 확인 및 형변환

- 자료형 확인: 특정 정보/변수의 자료형을 확인하기위해 우리는 _type()_ 을 사용합니다
  **Example:**

```py
# 다양한 파이썬 자료형
# 다양한 자료형의 변수들을 선언해 봅시다.

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, 제 실제 나이가 아닙니다, 걱정마세요

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
```

- 형변환: 하나의 자료형을 다른 자료형으로 변환합니다.  _int()_, _float()_, _str()_, _list_, _set_ 를 사용합니다.
  산술 연산을 수행할 때 문자열 숫자들을 먼저 int 나 float로 변환해야 합니다. 그렇지 않으면 오류가 반환됩니다. 만약 숫자를 문자열과 결합한다면, 그 숫자는 먼저 문자열로 변환되어야 합니다. 결합에 대해서는 String 섹션에서 설명하겠습니다.

  **Example:**

```py
# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

## 숫자

파이썬의 숫자 자료형:

1. Integers: 정수(음수, 0 , 양수) 
   예:
   ... -3, -2, -1, 0, 1, 2, 3 ...

2. 부동 소수점 숫자(10진수)
   예:
   ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. 복소수
   예:
   1 + j, 2 + 4j, 1 - 1j

🌕 당신은 정말 멋집니다. 여러분은 이제 막 2일차 도전을 마쳤고 위대함으로 가는 길에 두 걸음 앞서 있습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 Exercises - Day 2

### Exercises: Level 1

1. 30DaysOfPython 내에 day_2라는 폴더를 생성하세요. 그 폴더 내에 variables.py 라는 파일을 생성하세요.
2. 'Day 2: 30 Days of python programming'이라는 파이썬 주석을 작성합니다.
3. first name 변수를 선언하고 변수에 값을 할당합니다.
4. last name 변수를 선언하고 변수에 값을 할당합니다.
5. full name 변수를 선언하고 변수에 값을 할당합니다.
6. country 변수를 선언하고 값을 할당합니다.
7. city 변수를 선언하고 값을 할당합니다.
8. age 변수를 선언하고 값을 할당합니다.
9. year 변수를 선언하고 값을 할당합니다.
10. is_married 변수를 선언하고 값을 할당합니다.
11. is_true 변수를 선언하고 값을 할당합니다.
12. is_light_on 변수를 선언하고 값을 할당합니다.
13. 한 줄에 여러개의 변수를 선언합니다.

### Exercises: Level 2

1. Check the data type of all your variables using type() built-in function
1. Using the _len()_ built-in function, find the length of your first name
1. Compare the length of your first name and your last name
1. Declare 5 as num_one and 4 as num_two
    1. Add num_one and num_two and assign the value to a variable total
    2. Subtract num_two from num_one and assign the value to a variable diff
    3. Multiply num_two and num_one and assign the value to a variable product
    4. Divide num_one by num_two and assign the value to a variable division
    5. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    6. Calculate num_one to the power of num_two and assign the value to a variable exp
    7. Find floor division of num_one by num_two and assign the value to a variable floor_division
1. The radius of a circle is 30 meters.
    1. Calculate the area of a circle and assign the value to a variable name of _area_of_circle_
    2. Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
    3. Take radius as user input and calculate the area.
1. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
1. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

1. type() 내장 함수를 사용하여 모든 변수의 자료형을 확인합니다.
1. _len()_ 내장 함수를 사용하여 당신의 first name 의 길이를 찾습니다.
1. 당신의 first name 과 last name 의 길이를 비교합니다.
1. 5를 num_1로, 4를 num_2로 선언합니다.
    1. num_one과 num_two를 더하고 그 값을 변수 total 에 할당합니다.
    2. num_1에서 num_2를 빼고 그 값을 변수 diff 에 할당합니다.
    3. num_two와 num_one을 곱하여 그 값을 변수 product 에 할당합니다.
    4. num_one을 num_two로 나누고 그 값을 변수 division 에 할당합니다.
    5. 나머지 연산을 사용하여 num_two를 num_one으로 나눈 값을 찾고 변수 remainder 에 할당합니다.
    6. num_one을 num_two의 거듭제곱으로 계산하고 그 값을 변수 exp 에 할당합니다.
    7. num_one을 num_two로 나누고 소숫값은 버린 정수 값을 구하고 변수 floor_division 에 값을 할당합니다.
1. 원의 반지름은 30미터입니다.
    1. 원의 면적을 계산하여 _area_of_circle_ 이라는 이름의 변수에 값을 할당합니다.
    2. 원의 둘레를 계산하여 _circum_of_circum_ 이라는 이름의 변수에 값을 할당합니다.
    3. 반경을 사용자 입력으로 받아서 면적을 계산합니다.
1. 내장 함수 input을 사용하여 사용자로부터 이름, 성, 국가 및 나이를 얻고 해당 변수 이름에 값을 저장합니다.
1. Python 셸 또는 파일에서 help('keywords')을 실행하여 파이썬의 reserved words 또는 키워드를 확인합니다.

🎉 축하합니다 ! 🎉

[<< Day 1](../readme.md) | [Day 3 >>](../03_Day_Operators/03_operators.md)

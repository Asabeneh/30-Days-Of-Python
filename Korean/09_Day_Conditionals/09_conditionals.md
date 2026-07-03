<div align="center">
  <h1> 30 Days Of Python: Day 9 - Conditionals</h1>
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

[<< Day 8](../08_Day_Dictionaries/08_dictionaries.md) | [Day 10 >>](../10_Day_Loops/10_loops.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 9](#-day-9)
  - [Conditionals](#conditionals)
    - [If Condition](#if-condition)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Short Hand](#short-hand)
    - [Nested Conditions](#nested-conditions)
    - [If Condition and Logical Operators](#if-condition-and-logical-operators)
    - [If and Or Logical Operators](#if-and-or-logical-operators)
  - [💻 Exercises: Day 9](#-exercises-day-9)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 9

## Conditionals

기본적으로 파이썬 스크립트의 문장은 위에서 아래로 순차적으로 실행됩니다. 처리 로직이 요구하는 경우, 순차적 실행 흐름은 두 가지 방법으로 변경될 수 있습니다:

- 조건부 실행: 특정 표현식이 참이면 하나 이상의 문장 블록이 실행됩니다
- 반복 실행: 특정 표현식이 참인 동안 하나 이상의 문장 블록이 반복적으로 실행됩니다. 이 섹션에서는 _if_, _else_, _elif_ 문을 다룹니다. 이전 섹션에서 배운 비교 연산자와 논리 연산자가 여기서 유용할 것입니다.

### If Condition

파이썬 및 다른 프로그래밍 언어에서 키워드 _if_ 는 조건이 참인지 확인하고 블록 코드를 실행하는 데 사용됩니다. 콜론 뒤의 들여쓰기를 기억하세요.

```py
# syntax
if condition:
    this part of code runs for truthy conditions
```

**Example: 1**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

위의 예에서 볼 수 있듯이 3은 0보다 큽니다. 조건이 참이었고 블록 코드가 실행되었습니다. 그러나 조건이 거짓이면 결과를 볼 수 없습니다. 거짓 조건의 결과를 보려면 또 다른 블록이 필요하며, 그것이 _else_ 입니다.

### If Else

조건이 참이면 첫 번째 블록이 실행되고, 그렇지 않으면 else 조건이 실행됩니다.

```py
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**Example:**

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

위의 조건은 거짓으로 판명되었으므로 else 블록이 실행되었습니다. 조건이 두 개 이상이라면 어떨까요? _elif_ 를 사용할 수 있습니다.

### If Elif Else

일상생활에서 우리는 매일 결정을 내립니다. 우리는 하나 또는 두 개의 조건만 확인하는 것이 아니라 여러 조건을 확인하여 결정을 내립니다. 프로그래밍도 삶과 마찬가지로 조건으로 가득합니다. 여러 조건이 있을 때 _elif_ 를 사용합니다.

```py
# syntax
if condition:
    code
elif condition:
    code
else:
    code

```

**Example:**

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### Short Hand

```py
# syntax
code if condition else code
```

**Example:**

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # 첫 번째 조건이 충족되어 'A is positive'가 출력됩니다
```

### Nested Conditions

조건은 중첩될 수 있습니다.

```py
# syntax
if condition:
    code
    if condition:
    code
```

**Example:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

```

논리 연산자 _and_ 를 사용하여 중첩 조건 작성을 피할 수 있습니다.

### If Condition and Logical Operators

```py
# syntax
if condition and condition:
    code
```

**Example:**

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

### If and Or Logical Operators

```py
# syntax
if condition or condition:
    code
```

**Example:**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

🌕 잘하고 있습니다. 절대 포기하지 마세요. 위대한 것들은 시간이 필요합니다. 9일차 도전을 완료했으며 위대함을 향한 9걸음 앞에 있습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 Exercises: Day 9

### Exercises: Level 1

1. input("Enter your age: ")을 사용하여 사용자 입력을 받습니다. 사용자가 18세 이상이면 "You are old enough to drive."라는 피드백을 제공합니다. 18세 미만이면 부족한 년수를 기다리라는 피드백을 제공합니다. 출력:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. if … else를 사용하여 my_age와 your_age의 값을 비교합니다. 누가 더 나이가 많은지 (나인지 당신인지)? input("Enter your age: ")을 사용하여 나이를 입력받습니다. 1년 차이의 경우 'year'를, 더 큰 차이의 경우 'years'를, my_age = your_age인 경우 사용자 지정 텍스트를 출력하기 위해 중첩 조건을 사용할 수 있습니다. 출력:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

3. 입력 프롬프트를 사용하여 사용자로부터 두 개의 숫자를 받습니다. a가 b보다 크면 a is greater than b를 반환하고, a가 b보다 작으면 a is smaller than b를 반환하고, 그렇지 않으면 a is equal to b를 반환합니다. 출력:

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

### Exercises: Level 2

   1. 학생들의 점수에 따라 등급을 매기는 코드를 작성합니다:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

   2. 사용자 입력으로 월을 받은 다음 계절이 가을, 겨울, 봄 또는 여름인지 확인합니다. 사용자 입력이:
    September, October 또는 November이면 계절은 가을입니다.
    December, January 또는 February이면 계절은 겨울입니다.
    March, April 또는 May이면 계절은 봄입니다.
    June, July 또는 August이면 계절은 여름입니다.
   3. 다음 리스트에는 몇 가지 과일이 포함되어 있습니다:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    과일이 리스트에 없으면 과일을 리스트에 추가하고 수정된 리스트를 출력합니다. 과일이 이미 있으면 print('That fruit already exist in the list')를 출력합니다.

### Exercises: Level 3

   1. 여기에 person 딕셔너리가 있습니다. 자유롭게 수정하세요!

```py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

     * person 딕셔너리에 skills 키가 있는지 확인하고, 있다면 skills 리스트의 중간 스킬을 출력합니다.
     * person 딕셔너리에 skills 키가 있는지 확인하고, 있다면 그 사람이 'Python' 스킬을 가지고 있는지 확인하여 결과를 출력합니다.
     * 사람의 스킬이 JavaScript와 React만 있다면 print('He is a front end developer')를, Node, Python, MongoDB가 있다면 print('He is a backend developer')를, React, Node, MongoDB가 있다면 Print('He is a fullstack developer')를, 그렇지 않으면 print('unknown title')를 출력합니다 - 더 정확한 결과를 위해 더 많은 조건을 중첩할 수 있습니다!
     * 그 사람이 기혼이고 핀란드에 산다면 다음 형식으로 정보를 출력합니다:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 CONGRATULATIONS ! 🎉

[<< Day 8](../08_Day_Dictionaries/08_dictionaries.md) | [Day 10 >>](../10_Day_Loops/10_loops.md)

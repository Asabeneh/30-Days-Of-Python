<div align="center">   <h1> 30 Days Of Python: Day 10 - Loops</h1>   <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">   <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">   </a>   <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">   <img src="https://img.shields.io/twitter/follow/asabeneh?style=social" alt="Twitter Follow">   </a>
</div>
<p data-md-type="paragraph"><sub data-md-type="raw_html">Author: <a data-md-type="raw_html" href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br> <small data-md-type="raw_html"> Second Edition: July, 2021</small></sub></p>
<div data-md-type="block_html"></div>

[&lt;&lt; Day 9](../09_Day_Conditionals/09_conditionals.md) | [Day 11 &gt;&gt;](../11_Day_Functions/11_functions.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 10](#-day-10)
    - [Loops](#loops)
        - [While 루프](#while-루프)
        - [Break 과 Continue - Part 1](#break-과-continue---part-1)
        - [For 루프](#for-루프)
        - [Break 과 Continue - Part 2](#break-과-continue---part-2)
        - [범위 기능](#범위-기능)
        - [중첩 For 루프](#중첩-for-루프)
        - [For Else](#for-else)
        - [Pass](#pass)
    - [💻 Exercises: Day 10](#-exercises-day-10)
        - [Exercises: Level 1](#exercises-level-1)
        - [Exercises: Level 2](#exercises-level-2)
        - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 10

## Loops

인생은 일상으로 가득 차 있습니다. 프로그래밍에서 우리는 또한 많은 반복 작업을 수행합니다. 반복 작업을 처리하기 위해 프로그래밍 언어는 루프를 사용합니다. Python 프로그래밍 언어는 또한 다음 유형의 두 루프를 제공합니다.

1. while loop
2. for loop

### While 루프

우리는 while 루프를 만들기 위해 예약어 *while* 을 사용합니다. 주어진 조건이 만족될 때까지 문 블록을 반복적으로 실행하는 데 사용됩니다. 조건이 거짓이 되면 루프 뒤의 코드 행이 계속 실행됩니다.

```py
  # syntax
while condition:
    code goes here
```

**예시:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
```

위의 while 루프에서 count가 5일 때 조건이 false가 됩니다. 이때 루프가 중지됩니다. 조건이 더 이상 참이 아닐 때 코드 블록을 실행하고 싶다면 *else* 를 사용할 수 있습니다.

```py
  # syntax
while condition:
    code goes here
else:
    code goes here
```

**예시:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
```

위의 루프 조건은 count가 5이고 루프가 중지되고 실행이 else 문을 시작하면 거짓이 됩니다. 결과적으로 5가 인쇄됩니다.

### Break 과 Continue - Part 1

- 중단: 루프에서 벗어나거나 중단하고 싶을 때 중단을 사용합니다.

```py
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

**예시:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

위의 while 루프는 0, 1, 2만 인쇄하지만 3에 도달하면 중지합니다.

- 계속: continue 문을 사용하면 현재 반복을 건너뛰고 다음을 계속할 수 있습니다.

```py
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

**예시:**

```py
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
```

위의 while 루프는 0, 1, 2 및 4만 인쇄합니다(3을 건너뜁니다).

### For 루프

*for* 키워드는 다른 프로그래밍 언어와 유사하지만 구문이 약간 다른 for 루프를 만드는 데 사용됩니다. 루프는 시퀀스(즉, 목록, 튜플, 사전, 집합 또는 문자열)를 반복하는 데 사용됩니다.

- For loop with list

```py
# syntax
for iterator in lst:
    code goes here
```

**예시:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
```

- For loop with string

```py
# syntax
for iterator in string:
    code goes here
```

**예시:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- For loop with tuple

```py
# syntax
for iterator in tpl:
    code goes here
```

**예시:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- 사전을 사용한 For 루프 사전을 통한 루프는 사전의 키를 제공합니다.

```py
  # syntax
for iterator in dct:
    code goes here
```

**예시:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

- Loops in set

```py
# syntax
for iterator in st:
    code goes here
```

**예시:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break 과 Continue - Part 2

짧은 알림: *중단* : 루프가 완료되기 전에 중단하고 싶을 때 중단을 사용합니다.

```py
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

**예시:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

위의 예에서 루프는 3에 도달하면 중지됩니다.

계속: 루프 반복에서 일부 단계를 건너뛰고 싶을 때 계속을 사용합니다.

```py
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**예시:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```

위의 예에서 숫자가 3이면 조건 *다음* 단계(루프 내부)를 건너뛰고 반복이 남아 있으면 루프 실행이 계속됩니다.

### 범위 기능

*range()* 함수는 숫자 목록에 사용됩니다. *범위(시작, 끝, 단계)* 는 시작, 종료 및 증분의 세 가지 매개변수를 사용합니다. 기본적으로 0부터 시작하고 증분은 1입니다. 범위 시퀀스에는 최소 1개의 인수(종료)가 필요합니다. 범위를 사용하여 시퀀스 만들기

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```py
# syntax
for iterator in range(start, end, step):
```

**예시:**

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

### 중첩 For 루프

루프 안에 루프를 작성할 수 있습니다.

```py
# syntax
for x in y:
    for t in x:
        print(t)
```

**예시:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

루프가 끝날 때 메시지를 실행하려면 else를 사용합니다.

```py
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**예시:**

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

### Pass

Python에서 when 문이 필요하지만(세미콜론 뒤에) 코드를 실행하는 것을 좋아하지 않으므로 오류를 피하기 위해 *pass* 라는 단어를 쓸 수 있습니다. 또한 향후 진술을 위해 자리 표시자로 사용할 수 있습니다.

**예시:**

```py
for number in range(6):
    pass
```

🌕 당신은 큰 이정표를 세웠고, 당신은 멈출 수 없습니다. 계속하세요! 10일차 챌린지를 방금 완료했으며 위대함을 향한 10단계를 앞두고 있습니다. 이제 뇌와 근육을 위한 몇 가지 운동을 하십시오.

## 💻 Exercises: Day 10

### Exercises: Level 1

1. for 루프를 사용하여 0에서 10까지 반복하고 while 루프를 사용하여 동일한 작업을 수행합니다.

2. for 루프를 사용하여 10에서 0까지 반복하고 while 루프를 사용하여 동일한 작업을 수행합니다.

3. print()를 7번 호출하는 루프를 작성하여 다음 삼각형을 출력합니다.

    ```py
      #
      ##
      ###
      ####
      #####
      ######
      #######
    ```

4. 중첩 루프를 사용하여 다음을 만듭니다.

    ```sh
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    ```

5. 다음 패턴을 인쇄합니다.

    ```sh
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100
    ```

6. for 루프를 사용하여 ['Python', 'Numpy','Pandas','Django', 'Flask'] 목록을 반복하고 항목을 출력합니다.

7. for 루프를 사용하여 0에서 100까지 반복하고 짝수만 출력

8. for 루프를 사용하여 0에서 100까지 반복하고 홀수만 출력

### Exercises: Level 2

1. for 루프를 사용하여 0에서 100까지 반복하고 모든 숫자의 합계를 인쇄합니다.

```sh
The sum of all numbers is 5050.
```

1. for 루프를 사용하여 0에서 100까지 반복하고 모든 짝수의 합과 모든 승산의 합을 인쇄합니다.

    ```sh
    The sum of all evens is 2550. And the sum of all odds is 2500.
    ```

### Exercises: Level 3

1. 데이터 폴더로 이동하여 [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) 파일을 사용합니다. 국가를 순환하고 단어 *land* 를 포함하는 모든 국가를 추출합니다.
2. 이것은 과일 목록입니다. ['banana', 'orange', 'mango', 'lemon'] 루프를 사용하여 순서를 뒤집습니다.
3. 데이터 폴더로 이동하여 [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) 파일을 사용합니다.
    1. 데이터의 총 언어 수는 얼마입니까?
    2. 데이터에서 가장 많이 사용되는 10개 언어 찾기
    3. 세계에서 인구가 가장 많은 10개 국가 찾기

🎉 축하합니다! 🎉

[&lt;&lt; Day 9](../09_Day_Conditionals/09_conditionals.md) | [Day 11 &gt;&gt;](../11_Day_Functions/11_functions.md)

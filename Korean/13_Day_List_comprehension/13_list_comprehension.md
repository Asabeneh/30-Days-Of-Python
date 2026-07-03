<div align="center">
  <h1> 30 Days Of Python: Day 13 - List Comprehension</h1>
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

[<< Day 12](../12_Day_Modules/12_modules.md) | [Day 14>>](../14_Day_Higher_order_functions/14_higher_order_functions.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 13](#-day-13)
  - [List Comprehension](#list-comprehension)
  - [Lambda Function](#lambda-function)
    - [Creating a Lambda Function](#creating-a-lambda-function)
    - [Lambda Function Inside Another Function](#lambda-function-inside-another-function)
  - [💻 Exercises: Day 13](#-exercises-day-13)

# 📘 Day 13

## List Comprehension

파이썬의 List comprehension은 시퀀스에서 리스트를 만드는 간결한 방법입니다. 새 리스트를 만드는 짧은 방법입니다. List comprehension은 _for_ 루프를 사용하여 리스트를 처리하는 것보다 상당히 빠릅니다.

```py
# syntax
[expression for i in iterable if condition]
```

**Example:1**

예를 들어 문자열을 문자 리스트로 변경하고 싶다면, 몇 가지 방법을 사용할 수 있습니다. 그 중 일부를 살펴봅시다:

```py
# 첫 번째 방법
language = 'Python'
lst = list(language) # 문자열을 리스트로 변경
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# 두 번째 방법: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**Example:2**

예를 들어 숫자 리스트를 생성하고 싶다면:

```py
# 숫자 생성
numbers = [i for i in range(11)]  # 0부터 10까지의 숫자 생성
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 반복 중에 수학적 연산이 가능합니다
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 튜플의 리스트를 만드는 것도 가능합니다
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**Example:2**

List comprehension은 if 표현식과 결합할 수 있습니다.


```py
# 짝수 생성
even_numbers = [i for i in range(21) if i % 2 == 0]  # 0부터 21 범위에서 짝수 리스트 생성
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 홀수 생성
odd_numbers = [i for i in range(21) if i % 2 != 0]  # 0부터 21 범위에서 홀수 생성
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 숫자 필터링: 아래 리스트에서 양수 짝수만 필터링해봅시다
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 2차원 배열 펼치기
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Lambda Function

Lambda 함수는 이름이 없는 작은 익명 함수입니다. 인자를 여러 개 받을 수 있지만 하나의 표현식만 가질 수 있습니다. Lambda 함수는 JavaScript의 익명 함수와 유사합니다. 다른 함수 내에서 익명 함수를 작성하고 싶을 때 필요합니다.

### Creating a Lambda Function

lambda 함수를 만들려면 _lambda_ 키워드 뒤에 매개변수, 그 다음에 표현식을 사용합니다. 아래의 구문과 예제를 참조하세요. Lambda 함수는 return을 사용하지 않지만 명시적으로 표현식을 반환합니다.

```py
# syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

**Example:**

```py
# 명명된 함수
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# 위의 함수를 lambda 함수로 변환해봅시다
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# 자기 호출 lambda 함수
(lambda a, b: a + b)(2,3) # 5 - 콘솔에서 결과를 보려면 print()로 감싸야 합니다

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# 다중 변수
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### Lambda Function Inside Another Function

다른 함수 내에서 lambda 함수를 사용합니다.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # power 함수는 이제 실행하려면 별도의 괄호에 2개의 인자가 필요합니다
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

🌕 좋은 작업을 계속하세요. 모멘텀을 유지하세요, 하늘이 한계입니다! 13일차 도전을 완료했으며 위대함을 향한 13걸음 앞에 있습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 Exercises: Day 13

1. list comprehension을 사용하여 리스트에서 음수와 0만 필터링합니다.
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. 다음 리스트의 리스트의 리스트를 1차원 리스트로 펼칩니다:

   ```py
   list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. list comprehension을 사용하여 다음 튜플 리스트를 만듭니다:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. 다음 리스트를 새 리스트로 펼칩니다:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
5. 다음 리스트를 딕셔너리 리스트로 변경합니다:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
6. 다음 리스트의 리스트를 연결된 문자열 리스트로 변경합니다:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
7. 일차 함수의 기울기 또는 y절편을 구하는 lambda 함수를 작성합니다.

🎉 CONGRATULATIONS ! 🎉

[<< Day 12](../12_Day_Modules/12_modules.md) | [Day 14>>](../14_Day_Higher_order_functions/14_higher_order_functions.md)

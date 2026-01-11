<div align="center">
  <h1> 30 Days Of Python: Day 3 - Operators</h1>
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

[<< Day 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Day 4 >>](../04_Day_Strings/04_strings.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 3일차](#-3일차)
  - [불리언](#불리언)
  - [연산자](#연산자)
    - [대입 연산자](#대입-연산자)
    - [산술 연산자:](#산술-연산자)
    - [비교 연산자](#비교-연산자)
    - [논리 연산자](#논리-연산자)
  - [💻 3일차: 실습](#-3일차-실습)

# 📘 3일차

## 불리언

불리언 데이터 타입은 True 또는 False 두 값 중 하나를 나타냅니다. 비교 연산자를 사용하면 이 데이터 타입의 사용이 명확해질 것입니다. 첫 번째 문자 **T** 는 참, **F** 는 거짓으로 표현되는 자바 스크립트와 달리 대문자여야 합니다.
**예시: 불리언 값**

```py
print(True)
print(False)
```

## 연산자

파이썬은 몇 가지 타입의 연산자를 지원합니다. 이 섹션에서 이것에 대해 알아볼 것입니다.

### 대입 연산자

대입 연산자는 변수에 값을 대입할 때 사용됩니다. = 로 예시를 들어보겠습니다. 수학에서 등호란 두 값이 동일하다는 것을 의미하지만, 파이썬에서는 특정 변수가 값을 가지고 있으며, 이 변수에 값을 대입한다고 합니다. 아래 표는 [w3school](https://www.w3schools.com/python/python_operators.asp)에서 가져온 다양한 유형의 파이썬 할당 연산자를 보여줍니다.

![대입 연산자](../images/assignment_operators.png)

### 산술 연산자:

- 더하기(+): a + b
- 빼기(-): a - b
- 곱하기(*): a * b
- 나누기(/): a / b
- 나머지 연산(%): a % b
- 버림 나눗셈(//): a // b
- 지수(**): a ** b

![산술 연산자](../images/arithmetic_operators.png)

**예시: Integers**

```py
# Arithmetic Operations in Python
# Integers

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  파이썬의 나누기는 부동 소수를 제공합니다.
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3, 부동 소수 또는 나머지가 없는 값을 제공합니다.
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, 나머지를 제공합니다.
print('Exponentiation: ', 2 ** 3) # 9  2 * 2 * 2 를 의미합니다.
```

**예시: Floats**

```py
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
```

**예시: 복소수**

```py
# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

변수를 선언하고 숫자 데이터 유형을 지정합니다. 여기서는 단일 문자 변수를 사용할 것이지만, 이런 유형의 변수를 선언하는 습관은 좋지 않다는 것을 기억하셔야 합니다. 변수 이름은 항상 기억해야 합니다. 

**Example:**

```python
# 첫 번째로 변수를 먼저 선언합니다.

a = 3 # a는 변수의 이름이며 정수 데이터 타입입니다.
b = 2 # b는 변수의 이름이며 정수 데이터 타입입니다.

# 산술 연산 및 결과를 변수에 대입합니다.
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# sum 대신 total을 사용했어야 하지만 sum은 내장 함수입니다. 내장 함수를 재정의하지 않도록 하십시오.
print(total) # 만약 몇몇 출력에 문자열로 표시를 하지 않는다면, 어디서 결과가 오는지 알지 못할 것입니다.
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)
```

**Example:**

```py
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# 값을 선언하고 함께 정리
num_one = 3
num_two = 4

# 산술 연산
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# 레이블로 값 출력
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
```

이제 점 연결을 시작하고 이미 알고 있는 계산 방법(면적, 부피, 밀도, 무게, 둘레, 거리, 힘)을 사용해 보겠습니다.

**Example:**

```py
# 원의 넓이 계산
radius = 10                                 # 원의 반지름
area_of_circle = 3.14 * radius ** 2         # 두 개의 * 기호는 지수를 의미합니다
print('Area of a circle:', area_of_circle)

# 직사각형의 넓이 계산
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# 개체의 무게 계산
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # 무게에 단위 추가

# 액체의 밀도 계산
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3

```

### 비교 연산자

프로그래밍에서 우리는 비교 연산자를 사용하여 두 값을 비교합니다. 우리는 값이 다른 값보다 크거나 작거나 같은지 확인합니다. 다음 표는[w3shool](https://www.w3schools.com/python/python_operators.asp)에서 가져온 파이썬의 비교 연산자를 보여줍니다.

![Comparison Operators](../images/comparison_operators.png)
**Example: 비교 연산자**

```py
print(3 > 2)     # 참, 3이 2보다 크기 때문에
print(3 >= 2)    # 참, 3이 2보다 크기 때문에
print(3 < 2)     # 거짓, 3이 더 크기 때문에
print(2 < 3)     # 참, 2가 3보다 작기 때문에
print(2 <= 3)    # 참, 2가 3보다 작기 때문에
print(3 == 2)    # 거짓, 3과 2는 같지 않기 때문에
print(3 != 2)    # 참, 3은 2와 다르기 때문에
print(len('mango') == len('avocado'))  # 거짓
print(len('mango') != len('avocado'))  # 참
print(len('mango') < len('avocado'))   # 참
print(len('milk') != len('meat'))      # 거짓
print(len('milk') == len('meat'))      # 참
print(len('tomato') == len('potato'))  # 참
print(len('python') > len('dragon'))   # 거짓


# 무언가를 비교하면 참 또는 거짓이 됩니다.

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```

위의 비교 연산자 외에 파이썬은 다음과 같은 연산자를 사용합니다:

- _is_: 두 변수가 동일할 경우 참을 반환합니다.(x is y)
- _is not_: 두 변수가 동일하지 않을 경우 참을 반환합니다.(x is not y)
- _in_: 제시된 목록에 특정 항목이 포함된 경우 참을 반환합니다.(x in y)
- _not in_: 제시된 목록에 특정 항목이 없으면 참을 반환합니다.(x in y)

```py
print('1 is 1', 1 is 1)                   # 참 - 데이터 값이 동일하기 때문에
print('1 is not 2', 1 is not 2)           # 참 - 1과 2는 다르기 때문에
print('A in Asabeneh', 'A' in 'Asabeneh') # 참 - 문자열에서 A를 찾을 수 있습니다
print('B in Asabeneh', 'B' in 'Asabeneh') # 거짓 - 대문자 B가 없습니다
print('coding' in 'coding for all') # 참 - coding이라는 단어를 coding for all이 가지고 있기 때문에
print('a in an:', 'a' in 'an')      # 참
print('4 is 2 ** 2:', 4 is 2 ** 2)   # 참
```

### 논리 연산자

다른 프로그래밍 언어와 달리 파이썬은 논리 연산자를 위해 _and_, _or_, _not_ 키워드를 사용합니다. 논리 연산자는 다음과 같은 조건문을 결합하는 데 사용됩니다.

![Logical Operators](../images/logical_operators.png)

```py
print(3 > 2 and 4 > 3) # 참 - 두 개의 문장이 참이기 때문에 
print(3 > 2 and 4 < 3) # 거짓 - 두 번째 문장이 거짓이기 때문에
print(3 < 2 and 4 < 3) # 거짓 - 두 가지 문장 모두 거짓이기 때문에
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # 참 - 두 가지 문장 모두 참이기 때문에
print(3 > 2 or 4 < 3)  # 참 - 두 가지 중 하나의 문장이 참이기 때문에
print(3 < 2 or 4 < 3)  # 거짓 - 두 가지 문장 모두 거짓이기 때문에
print('True or False:', True or False)
print(not 3 > 2)     # 거짓 - 3이 2보다 큰 것은 참이기 때문에, 참이 아닐 경우 거짓을 줍니다.
print(not True)      # 거짓 - 부정으로 참에서 거짓으로 바뀝니다.
print(not False)     # True
print(not not True)  # True
print(not not False) # False

```

🌕 당신은 무한한 에너지를 가지고 있어요. 여러분은 이제 막 3일차 도전을 마쳤고 위대함으로 가는 길에 세 걸음 앞서 있습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 3일차 실습

1. 나이를 정수 변수로 선언합니다.
2. 자신의 키를 플로트 변수로 선언합니다.
3. 복소수를 저장하는 변수 선언합니다.
4. 삼각형의 밑면과 높이를 입력하도록 사용자에게 지시하는 스크립트를 작성하고 이 삼각형의 면적(면적 = 0.5 x b x h)을 계산합니다.

```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```

5. 삼각형의 측면 a, 측면 b, 측면 c를 입력하라는 메시지를 표시하는 스크립트를 작성합니다. 삼각형의 둘레(지름 = a + b + c)를 계산합니다.

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

6. 프롬프트를 사용하여 직사각형의 길이와 너비를 가져옵니다. 면적(면적 = 길이 x 폭) 및 둘레(면적 = 2 x (길이 + 폭)) 계산합니다.
7. 프롬프트를 사용하여 원의 반지름을 구합니다. 면적(면적 = 픽스 r x r)과 원주(c = 2 x 픽스 r)를 계산합니다. 여기서 pi = 3.14입니다.
8. y = 2x-2의 기울기, x-제곱 및 y-제곱을 계산합니다.
9. 기울기는 (m = y2-y1/x2-x1)입니다. 기울기와 [유클리드 거리](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) 점(2,2)과 점(6,10) 사이를 구합니다.
10. 과제 8과 9의 기울기를 비교합니다.
11. y 값(y = x^2 + 6x + 9)을 계산합니다. 다른 x 값을 사용하고 y 값이 0이 되는 x 값을 계산해 보십시오.
12. 'python'과 'dragon'의 길이를 찾아 거짓 비교를 합니다.
13. _and_ 연산자를 사용하여 'python'과 'dragon' 모두에 'on'이 있는지 확인합니다.
14. _나는 이 강좌가 전문용어로 가득하지 않기를 바랍니다. _in_ 연산자를 사용하여 _jargon_ 이 문장에 있는지 확인합니다.
15. dragon과 python 모두 'On'이 없습니다.
16. _python_ 텍스트의 길이를 찾아서 값을 float로 변환하고 문자열로 변환합니다.
17. 짝수는 2로 나누고 나머지는 0입니다. 파이썬을 사용하여 숫자가 짝수인지 아닌지 어떻게 확인하겠습니까?
18. 7 x 3의 나눗셈 버림이 2.7의 int 변환값과 동일한지 확인합니다.
19. '10'의 유형이 10의 유형과 동일한지 확인합니다.
20. if int('9.8')이 10과 같은지 확인합니다.
21. 사용자에게 시간 및 시간당 요금을 입력하도록 요청하는 스크립트를 작성합니다. 그 사람의 급여를 계산합니까?

```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

22. 사용자에게 년 수를 입력하도록 요청하는 스크립트를 작성합니다. 사람이 살 수 있는 시간을 초 단위로 계산합니다. 사람이 100년을 살 수 있다고 가정합시다.

```py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
```

23. 다음을 표시하는 파이썬 스크립트를 작성합니다.

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

🎉 축하합니다 ! 🎉

[<< Day 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Day 4 >>](../04_Day_Strings/04_strings.md)

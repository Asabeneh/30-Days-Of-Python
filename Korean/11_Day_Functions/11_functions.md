<div align="center">
  <h1> 30 Days Of Python: Day 11 - Functions</h1>
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

[<< Day 10](../10_Day_Loops/10_loops.md) | [Day 12 >>](../12_Day_Modules/12_modules.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 11](#-day-11)
  - [Functions](#functions)
    - [Defining a Function](#defining-a-function)
    - [Declaring and Calling a Function](#declaring-and-calling-a-function)
    - [Function without Parameters](#function-without-parameters)
    - [Function Returning a Value - Part 1](#function-returning-a-value---part-1)
    - [Function with Parameters](#function-with-parameters)
    - [Passing Arguments with Key and Value](#passing-arguments-with-key-and-value)
    - [Function Returning a Value - Part 2](#function-returning-a-value---part-2)
    - [Function with Default Parameters](#function-with-default-parameters)
    - [Arbitrary Number of Arguments](#arbitrary-number-of-arguments)
    - [Default and Arbitrary Number of Parameters in Functions](#default-and-arbitrary-number-of-parameters-in-functions)
    - [Function as a Parameter of Another Function](#function-as-a-parameter-of-another-function)
  - [Testimony](#testimony)
  - [💻 Exercises: Day 11](#-exercises-day-11)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 11

## Functions

지금까지 우리는 많은 파이썬 내장 함수들을 보았습니다. 이 섹션에서는 사용자 정의 함수에 집중하겠습니다. 함수란 무엇일까요? 함수를 만들기 전에 함수가 무엇이고 왜 필요한지 알아봅시다.

### Defining a Function

함수는 특정 작업을 수행하도록 설계된 재사용 가능한 코드 블록 또는 프로그래밍 문장입니다. 함수를 정의하거나 선언하기 위해 파이썬은 _def_ 키워드를 제공합니다. 다음은 함수를 정의하는 구문입니다. 함수의 코드 블록은 함수가 호출되거나 실행될 때만 실행됩니다.

### Declaring and Calling a Function

함수를 만들 때 이를 함수 선언이라고 합니다. 함수를 사용하기 시작할 때 이를 함수 _호출_ 또는 _실행_ 이라고 합니다. 함수는 매개변수가 있거나 없이 선언할 수 있습니다.

```py
# syntax
# 함수 선언
def function_name():
    codes
    codes
# 함수 호출
function_name()
```

### Function without Parameters

함수는 매개변수 없이 선언할 수 있습니다.

**Example:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # 함수 호출

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Function Returning a Value - Part 1

함수는 _return_ 문을 사용하여 값을 반환합니다. 함수에 return 문이 없으면 None을 반환합니다. 위의 함수들을 return을 사용하여 다시 작성해봅시다. 이제부터 함수를 호출할 때 값을 받아서 출력합니다.

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Function with Parameters

함수에서 다양한 자료형(숫자, 문자열, 불리언, 리스트, 튜플, 딕셔너리 또는 세트)을 매개변수로 전달할 수 있습니다.

- 단일 매개변수: 함수가 매개변수를 받는 경우 인자와 함께 함수를 호출해야 합니다.

```py
  # syntax
  # 함수 선언
  def function_name(parameter):
    codes
    codes
  # 함수 호출
  print(function_name(argument))
```

**Example:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- 두 개의 매개변수: 함수는 매개변수가 있을 수도 있고 없을 수도 있습니다. 함수는 두 개 이상의 매개변수를 가질 수도 있습니다. 함수가 매개변수를 받는 경우 인자와 함께 호출해야 합니다. 두 개의 매개변수가 있는 함수를 확인해봅시다:

```py
  # syntax
  # 함수 선언
  def function_name(para1, para2):
    codes
    codes
  # 함수 호출
  print(function_name(arg1, arg2))
```

**Example:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # 값을 먼저 문자열로 변환해야 합니다
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Passing Arguments with Key and Value

키와 값으로 인자를 전달하면 인자의 순서는 중요하지 않습니다.

```py
# syntax
# 함수 선언
def function_name(para1, para2):
    codes
    codes
# 함수 호출
print(function_name(para1 = 'John', para2 = 'Doe')) # 여기서 인자의 순서는 중요하지 않습니다
```

**Example:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # 순서는 중요하지 않습니다
```

### Function Returning a Value - Part 2

함수에서 값을 반환하지 않으면 기본적으로 _None_ 을 반환합니다. 함수에서 값을 반환하려면 _return_ 키워드 뒤에 반환할 변수를 사용합니다. 함수에서 모든 종류의 자료형을 반환할 수 있습니다.

- 문자열 반환:
**Example:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- 숫자 반환:

**Example:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))
```

- 불리언 반환:
  **Example:**

```py
def is_even (n):
    if n % 2 == 0:
        return True    # return은 break와 유사하게 함수의 추가 실행을 중지합니다
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- 리스트 반환:
  **Example:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Function with Default Parameters

때때로 매개변수에 기본값을 전달합니다. 함수를 호출할 때 인자를 전달하지 않으면 기본값이 사용됩니다.

```py
# syntax
# 함수 선언
def function_name(param = value):
    codes
    codes
# 함수 호출
function_name()
function_name(arg)
```

**Example:**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # 값을 먼저 문자열로 변환해야 합니다
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - 지구 표면의 평균 중력
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # 달 표면의 중력
```

### Arbitrary Number of Arguments

함수에 전달할 인자의 수를 모르는 경우 매개변수 이름 앞에 \*를 추가하여 임의의 수의 인자를 받을 수 있는 함수를 만들 수 있습니다.

```py
# syntax
# 함수 선언
def function_name(*args):
    codes
    codes
# 함수 호출
function_name(param1, param2, param3,..)
```

**Example:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # total = total + num 과 동일
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Default and Arbitrary Number of Parameters in Functions

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```
### Dictionary unpacking

일치하는 키 이름을 가진 딕셔너리를 사용하여 명명된 인자를 가진 함수를 호출할 수 있습니다. ``**``를 사용하여 이를 수행합니다.

```py
# 두 개의 인자 'name'과 'location'을 받는 함수 정의
def greet(name, location):
    # 제공된 인자를 사용하여 인사 메시지 출력
    print("Hi there", name, "how is the weather in", location)

# 키워드 인자를 사용하여 함수 호출
greet(name="Alice", location="New York")  
# 출력: Hi there Alice how is the weather in New York

# 함수의 매개변수 이름과 일치하는 키를 가진 딕셔너리 생성
my_dict = {"name": "Alice", "location": "New York"}

# 딕셔너리 언패킹을 사용하여 함수 호출
greet(**my_dict)  
# ** 연산자는 딕셔너리를 언패킹하여 키-값 쌍을
# 함수의 키워드 인자로 전달합니다.
# 출력: Hi there Alice how is the weather in New York
```

### Arbitrary Number of Named Arguments

임의의 수의 명명된 인자를 받는 함수를 정의할 수도 있습니다.

```py
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
```

일반적으로 필요하지 않다면 이 방법은 피하는 것이 좋습니다. 함수가 무엇을 받고 무엇을 하는지 이해하기 어렵게 만들기 때문입니다.

### Function as a Parameter of Another Function

```py
# 함수를 매개변수로 전달할 수 있습니다
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 여러분은 지금까지 상당히 많은 것을 성취했습니다. 계속 나아가세요! 11일차 도전을 완료했으며 위대함을 향한 11걸음 앞에 있습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## Testimony

이제 저자와 30DaysOfPython에 대한 여러분의 생각을 표현할 시간입니다. 이 [링크](https://testimonial-s3sw.onrender.com/)에서 여러분의 후기를 남길 수 있습니다.

## 💻 Exercises: Day 11

### Exercises: Level 1

1. _add_two_numbers_ 함수를 선언합니다. 두 개의 매개변수를 받아 합계를 반환합니다.
2. 원의 넓이는 다음과 같이 계산합니다: area = π x r x r. _area_of_circle_ 을 계산하는 함수를 작성합니다.
3. 임의의 수의 인자를 받아 모든 인자를 합산하는 add_all_nums 함수를 작성합니다. 모든 리스트 아이템이 숫자 타입인지 확인합니다. 그렇지 않으면 적절한 피드백을 제공합니다.
4. °C의 온도는 다음 공식을 사용하여 °F로 변환할 수 있습니다: °F = (°C x 9/5) + 32. °C를 °F로 변환하는 함수 _convert_celsius_to-fahrenheit_ 를 작성합니다.
5. check-season이라는 함수를 작성합니다. month 매개변수를 받아 계절(Autumn, Winter, Spring 또는 Summer)을 반환합니다.
6. 일차 방정식의 기울기를 반환하는 calculate_slope 함수를 작성합니다.
7. 이차 방정식은 다음과 같이 계산됩니다: ax² + bx + c = 0. 이차 방정식의 해집합을 계산하는 함수 _solve_quadratic_eqn_ 을 작성합니다.
8. print_list라는 함수를 선언합니다. 리스트를 매개변수로 받아 리스트의 각 요소를 출력합니다.
9. reverse_list라는 함수를 선언합니다. 배열을 매개변수로 받아 배열의 역순을 반환합니다 (반복문을 사용합니다).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
```

10. capitalize_list_items라는 함수를 선언합니다. 리스트를 매개변수로 받아 대문자로 변환된 아이템 리스트를 반환합니다.
11. add_item이라는 함수를 선언합니다. 리스트와 아이템 매개변수를 받습니다. 아이템이 끝에 추가된 리스트를 반환합니다.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. remove_item이라는 함수를 선언합니다. 리스트와 아이템 매개변수를 받습니다. 아이템이 제거된 리스트를 반환합니다.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. sum_of_numbers라는 함수를 선언합니다. 숫자 매개변수를 받아 해당 범위의 모든 숫자를 더합니다.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. sum_of_odds라는 함수를 선언합니다. 숫자 매개변수를 받아 해당 범위의 모든 홀수를 더합니다.
15. sum_of_even이라는 함수를 선언합니다. 숫자 매개변수를 받아 해당 범위의 모든 짝수를 더합니다.

### Exercises: Level 2

1. evens_and_odds라는 함수를 선언합니다. 양의 정수를 매개변수로 받아 해당 숫자의 짝수와 홀수의 개수를 셉니다.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

1. factorial 함수를 호출합니다. 정수를 매개변수로 받아 해당 숫자의 팩토리얼을 반환합니다.
1. _is_empty_ 함수를 호출합니다. 매개변수를 받아 비어 있는지 여부를 확인합니다.
1. 리스트를 받는 다양한 함수를 작성합니다. calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (표준편차)를 계산해야 합니다.
1. _greet_ 라는 기본 인자 _name_ 을 받는 함수를 작성합니다. 인자가 제공되지 않으면 "Hello, Guest!"를 출력하고, 그렇지 않으면 이름으로 인사합니다.

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```
1. 임의의 수의 명명된 인자를 받아 이름과 값을 출력하는 _show_args_ 함수를 만듭니다.
   ```py
   show_args(name="Alice", age=30, city="New York")
   # Received: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```


### Exercises: Level 3

1. 숫자가 소수인지 확인하는 is_prime 함수를 작성합니다.
1. 리스트의 모든 아이템이 고유한지 확인하는 함수를 작성합니다.
1. 리스트의 모든 아이템이 동일한 자료형인지 확인하는 함수를 작성합니다.
1. 제공된 변수가 유효한 파이썬 변수인지 확인하는 함수를 작성합니다.
1. data 폴더로 이동하여 countries-data.py 파일에 접근합니다.

- 세계에서 가장 많이 사용되는 언어를 반환하는 most_spoken_languages 함수를 만듭니다. 내림차순으로 10개 또는 20개의 가장 많이 사용되는 언어를 반환해야 합니다.
- 가장 인구가 많은 국가를 반환하는 most_populated_countries 함수를 만듭니다. 내림차순으로 10개 또는 20개의 가장 인구가 많은 국가를 반환해야 합니다.

🎉 CONGRATULATIONS ! 🎉

[<< Day 10](../10_Day_Loops/10_loops.md) | [Day 12 >>](../12_Day_Modules/12_modules.md)

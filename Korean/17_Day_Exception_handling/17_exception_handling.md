<div align="center">
  <h1> 30 Days Of Python: Day 17 - 예외 처리 </h1>
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

[<< Day 16](../16_Day_Python_date_time/16_python_datetime.md) | [Day 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 17](#-day-17)
  - [예외 처리](#예외-처리)
  - [Python에서 인수 패킹과 언패킹](#python에서-인수-패킹과-언패킹)
    - [언패킹](#언패킹)
      - [리스트 언패킹](#리스트-언패킹)
      - [딕셔너리 언패킹](#딕셔너리-언패킹)
    - [패킹](#패킹)
    - [리스트 패킹](#리스트-패킹)
      - [딕셔너리 패킹](#딕셔너리-패킹)
  - [Python에서의 스프레딩](#python에서의-스프레딩)
  - [Enumerate](#enumerate)
  - [Zip](#zip)
  - [연습문제: Day 17](#연습문제-day-17)

# 📘 Day 17

## 예외 처리

Python은 오류를 우아하게 처리하기 위해 _try_와 _except_를 사용합니다. 오류의 우아한 종료(또는 우아한 처리)는 간단한 프로그래밍 관용구입니다 - 프로그램이 심각한 오류 조건을 감지하고 결과적으로 제어된 방식으로 "우아하게 종료"합니다. 종종 프로그램은 우아한 종료의 일부로 터미널이나 로그에 설명적인 오류 메시지를 출력하며, 이는 우리의 애플리케이션을 더 견고하게 만듭니다. 예외의 원인은 종종 프로그램 자체 외부에 있습니다. 예외의 예로는 잘못된 입력, 잘못된 파일 이름, 파일을 찾을 수 없음, 오작동하는 IO 장치 등이 있습니다. 오류의 우아한 처리는 애플리케이션의 충돌을 방지합니다.

이전 섹션에서 다양한 Python _오류_ 유형을 다루었습니다. 프로그램에서 _try_와 _except_를 사용하면 해당 블록에서 오류가 발생하지 않습니다.

![Try and Except](../../images/try_except.png)

```py
try:
    # 이 블록의 코드는 정상적으로 실행될 때
    code in this block if things go well
except:
    # 이 블록의 코드는 문제가 발생했을 때 실행
    code in this block run if things go wrong
```

**예시:**

```py
try:
    print(10 + '5')
except:
    print('Something went wrong')
```

위 예시에서 두 번째 피연산자는 문자열입니다. 숫자와 더하기 위해 float 또는 int로 변경할 수 있습니다. 하지만 변경 없이는 두 번째 블록인 _except_가 실행됩니다.

**예시:**

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```

```sh
Something went wrong
```

위 예시에서 except 블록이 실행되지만 정확한 문제가 무엇인지 알 수 없습니다. 문제를 분석하기 위해 except와 함께 다양한 오류 유형을 사용할 수 있습니다.

다음 예시에서는 오류를 처리하고 발생한 오류의 종류도 알려줍니다.

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
```

```sh
Enter your name:Asabeneh
Year you born:1920
Type error occured
```

위 코드에서 출력은 _TypeError_가 됩니다.
이제 추가 블록을 추가해 봅시다:

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
```

```sh
Enter your name:Asabeneh
Year you born:1920
You are Asabeneh. And your age is 99.
I usually run with the try block
I alway run.
```

위 코드를 다음과 같이 줄일 수도 있습니다:

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

```

## Python에서 인수 패킹과 언패킹

두 가지 연산자를 사용합니다:

- \* 튜플용
- \*\* 딕셔너리용

아래 예시를 살펴봅시다. 함수는 인수만 받지만 우리에게는 리스트가 있습니다. 리스트를 언패킹하여 인수로 변환할 수 있습니다.

### 언패킹

#### 리스트 언패킹

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

이 코드를 실행하면 오류가 발생합니다. 이 함수는 인수로 (리스트가 아닌) 숫자를 받기 때문입니다. 리스트를 언패킹/구조 분해해 봅시다.

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

시작과 끝을 기대하는 range 내장 함수에서도 언패킹을 사용할 수 있습니다.

```py
numbers = range(2, 7)  # 별도의 인수로 일반 호출
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # 리스트에서 언패킹된 인수로 호출
print(numbers)      # [2, 3, 4, 5,6]

```

리스트나 튜플은 다음과 같이 언패킹할 수도 있습니다:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### 딕셔너리 언패킹

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```

### 패킹

때때로 Python 함수에 얼마나 많은 인수를 전달해야 하는지 모를 수 있습니다. 패킹 방법을 사용하여 함수가 무제한 또는 임의의 수의 인수를 받을 수 있게 할 수 있습니다.

### 리스트 패킹

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### 딕셔너리 패킹

```py
def packing_person_info(**kwargs):
    # kwargs의 타입을 확인하면 dict 타입입니다
    # print(type(kwargs))
    # 딕셔너리 항목 출력
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

## Python에서의 스프레딩

JavaScript에서와 마찬가지로 Python에서도 스프레딩이 가능합니다. 아래 예시에서 확인해 봅시다:

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

리스트의 인덱스에 관심이 있다면, _enumerate_ 내장 함수를 사용하여 리스트의 각 항목의 인덱스를 가져올 수 있습니다.

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
```

```sh
The country Finland has been found at index 0.
```

## Zip

때때로 반복할 때 리스트를 결합하고 싶을 수 있습니다. 아래 예시를 참조하세요:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

🌕 당신은 결단력이 있습니다. 위대함을 향한 여정에서 17단계를 앞서고 있습니다. 이제 뇌와 근육을 위한 연습을 해봅시다.

## 연습문제: Day 17

1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. 처음 다섯 개 나라를 언패킹하여 nordic_countries 변수에 저장하고, Estonia와 Russia를 각각 es, ru에 저장하세요.


🎉 축하합니다 ! 🎉

[<< Day 16](../16_Day_Python_date_time/16_python_datetime.md) | [Day 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)

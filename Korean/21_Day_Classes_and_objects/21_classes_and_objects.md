<div align="center">
  <h1> 30 Days Of Python: Day 21 - Classes and Objects</h1>
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

[<< Day 20](../20_Day_Python_package_manager/20_python_package_manager.md) | [Day 22 >>](../22_Day_Web_scraping/22_web_scraping.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 21](#-day-21)
  - [클래스와 객체](#클래스와-객체)
    - [클래스 만들기](#클래스-만들기)
    - [객체 만들기](#객체-만들기)
    - [클래스 생성자](#클래스-생성자)
    - [객체 메서드](#객체-메서드)
    - [객체 기본 메서드](#객체-기본-메서드)
    - [클래스 기본값을 수정하는 메서드](#클래스-기본값을-수정하는-메서드)
    - [상속](#상속)
    - [부모 메서드 오버라이딩](#부모-메서드-오버라이딩)
  - [💻 연습문제: Day 21](#-연습문제-day-21)
    - [연습문제: Level 1](#연습문제-level-1)
    - [연습문제: Level 2](#연습문제-level-2)
    - [연습문제: Level 3](#연습문제-level-3)

# 📘 Day 21

## 클래스와 객체

Python은 객체 지향 프로그래밍 언어입니다. Python의 모든 것은 속성과 메서드를 가진 객체입니다. 프로그램에서 사용되는 숫자, 문자열, 리스트, 딕셔너리, 튜플, 세트 등은 해당하는 내장 클래스의 객체입니다. 객체를 만들기 위해 클래스를 생성합니다. 클래스는 객체 생성자 또는 객체를 만들기 위한 "청사진"과 같습니다. 클래스를 인스턴스화하여 객체를 만듭니다. 클래스는 객체의 속성과 동작을 정의하고, 반면에 객체는 클래스를 나타냅니다.

이 챌린지의 처음부터 우리는 자신도 모르게 클래스와 객체를 사용해 왔습니다. Python 프로그램의 모든 요소는 클래스의 객체입니다.
Python의 모든 것이 클래스인지 확인해 봅시다:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### 클래스 만들기

클래스를 만들려면 **class** 키워드 뒤에 이름과 콜론이 필요합니다. 클래스 이름은 **CamelCase**여야 합니다.

```sh
# 구문
class ClassName:
  code goes here
```

**예시:**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### 객체 만들기

클래스를 호출하여 객체를 만들 수 있습니다.

```py
p = Person()
print(p)
```

### 클래스 생성자

위의 예시에서 Person 클래스로부터 객체를 만들었습니다. 그러나 생성자가 없는 클래스는 실제 애플리케이션에서 그다지 유용하지 않습니다. 클래스를 더 유용하게 만들기 위해 생성자 함수를 사용해 봅시다. Java나 JavaScript의 생성자 함수처럼 Python에도 내장 **__init__**() 생성자 함수가 있습니다. **__init__** 생성자 함수는 클래스의 현재 인스턴스에 대한 참조인 self 매개변수를 가지고 있습니다.
**예시:**

```py
class Person:
      def __init__ (self, name):
        # self를 사용하여 클래스에 매개변수를 연결합니다
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# 출력
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

생성자 함수에 더 많은 매개변수를 추가해 봅시다.

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# 출력
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### 객체 메서드

객체는 메서드를 가질 수 있습니다. 메서드는 객체에 속하는 함수입니다.

**예시:**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# 출력
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

### 객체 기본 메서드

때때로 객체 메서드에 기본값을 설정하고 싶을 수 있습니다. 생성자의 매개변수에 기본값을 지정하면 매개변수 없이 클래스를 호출하거나 인스턴스화할 때 오류를 방지할 수 있습니다. 어떻게 보이는지 확인해 봅시다:

**예시:**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# 출력
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

### 클래스 기본값을 수정하는 메서드

아래 예시에서 person 클래스의 모든 생성자 매개변수에는 기본값이 있습니다. 이에 더해 메서드를 사용하여 접근할 수 있는 skills 매개변수가 있습니다. skills 리스트에 스킬을 추가하는 add_skill 메서드를 만들어 봅시다.

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# 출력
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### 상속

상속을 사용하면 부모 클래스의 코드를 재사용할 수 있습니다. 상속을 통해 부모 클래스의 모든 메서드와 속성을 상속받는 클래스를 정의할 수 있습니다. 부모 클래스 또는 슈퍼 클래스 또는 기본 클래스는 모든 메서드와 속성을 제공하는 클래스입니다. 자식 클래스는 다른 클래스 또는 부모 클래스로부터 상속받는 클래스입니다.
person 클래스를 상속받아 student 클래스를 만들어 봅시다.

```py
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

```sh
output
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

자식 클래스에서 **__init__**() 생성자를 호출하지 않았습니다. 호출하지 않으면 부모의 모든 속성에 여전히 접근할 수 있습니다. 하지만 생성자를 호출하면 _super_를 호출하여 부모 속성에 접근할 수 있습니다.  
자식에 새 메서드를 추가하거나 자식 클래스에서 같은 이름의 메서드를 만들어 부모 클래스 메서드를 오버라이드할 수 있습니다. **__init__**() 함수를 추가하면 자식 클래스는 더 이상 부모의 **__init__**() 함수를 상속받지 않습니다.

### 부모 메서드 오버라이딩

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

super() 내장 함수 또는 부모 이름 Person을 사용하여 부모로부터 메서드와 속성을 자동으로 상속받을 수 있습니다. 위의 예시에서 부모 메서드를 오버라이드했습니다. 자식 메서드는 다른 기능을 가지고 있으며, 성별이 남성인지 여성인지 식별하고 적절한 대명사(He/She)를 할당할 수 있습니다.

🌕 이제 프로그래밍의 슈퍼 파워로 완전히 충전되었습니다. 이제 두뇌와 근육을 위한 연습을 해보세요.

## 💻 연습문제: Day 21

### 연습문제: Level 1

1. Python에는 _statistics_라는 모듈이 있으며 이 모듈을 사용하여 모든 통계 계산을 수행할 수 있습니다. 그러나 함수를 만들고 재사용하는 방법을 배우기 위해 표본의 중심 경향 측정(평균, 중앙값, 최빈값)과 변동성 측정(범위, 분산, 표준 편차)을 계산하는 프로그램을 개발해 봅시다. 이러한 측정 외에도 표본의 최솟값, 최댓값, 개수, 백분위수 및 빈도 분포를 찾으세요. Statistics라는 클래스를 만들고 통계 계산을 수행하는 모든 함수를 Statistics 클래스의 메서드로 만들 수 있습니다. 아래 출력을 확인하세요.

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# 출력은 다음과 같아야 합니다
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### 연습문제: Level 2

1. PersonAccount라는 클래스를 만드세요. firstname, lastname, incomes, expenses 속성을 가지며 total_income, total_expense, account_info, add_income, add_expense, account_balance 메서드를 가집니다. Incomes는 수입과 그 설명의 집합입니다. expenses도 마찬가지입니다.

🎉 축하합니다! 🎉

[<< Day 20](../20_Day_Python_package_manager/20_python_package_manager.md) | [Day 22 >>](../22_Day_Web_scraping/22_web_scraping.md)

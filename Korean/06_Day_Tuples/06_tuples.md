<div align="center">
  <h1> 30 Days Of Python: Day 6 - Tuples</h1>
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

[<< Day 5](../05_Day_Lists/05_lists.md) | [Day 7 >>](../07_Day_Sets/07_sets.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [Day 6:](#day-6)
  - [Tuples](#tuples)
    - [Creating a Tuple](#creating-a-tuple)
    - [Tuple length](#tuple-length)
    - [Accessing Tuple Items](#accessing-tuple-items)
    - [Slicing tuples](#slicing-tuples)
    - [Changing Tuples to Lists](#changing-tuples-to-lists)
    - [Checking an Item in a Tuple](#checking-an-item-in-a-tuple)
    - [Joining Tuples](#joining-tuples)
    - [Deleting Tuples](#deleting-tuples)
  - [💻 Exercises: Day 6](#-exercises-day-6)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)

# Day 6:

## Tuples

튜플은 정렬되고 변경할 수 없는(불변) 다양한 자료형의 컬렉션입니다. 튜플은 둥근 괄호 ()로 작성합니다. 튜플이 생성되면 값을 변경할 수 없습니다. 튜플은 수정 가능(mutable)하지 않기 때문에 add, insert, remove 메서드를 사용할 수 없습니다. 리스트와 달리 튜플은 메서드가 거의 없습니다. 튜플과 관련된 메서드는 다음과 같습니다:

- tuple(): 빈 튜플을 생성합니다
- count(): 튜플에서 지정된 아이템의 개수를 셉니다
- index(): 튜플에서 지정된 아이템의 인덱스를 찾습니다
- `+` operator: 두 개 이상의 튜플을 결합하여 새 튜플을 생성합니다

### Creating a Tuple

- 빈 튜플: 빈 튜플 만들기
  
  ```py
  # syntax
  empty_tuple = ()
  # 또는 tuple 생성자를 사용
  empty_tuple = tuple()
  ```

- 초기 값이 있는 튜플
  
  ```py
  # syntax
  tpl = ('item1', 'item2','item3')
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  ```

### Tuple length

_len()_ 메서드를 사용하여 튜플의 길이를 구합니다.

```py
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Accessing Tuple Items

- 양수 인덱싱
  리스트 자료형과 마찬가지로 양수 또는 음수 인덱싱을 사용하여 튜플 아이템에 접근합니다.
  ![Accessing tuple items](../../images/tuples_index.png)

  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3')
  first_item = tpl[0]
  second_item = tpl[1]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[0]
  second_fruit = fruits[1]
  last_index =len(fruits) - 1
  last_fruit = fruits[last_index]
  ```

- 음수 인덱싱
  음수 인덱싱은 끝에서부터 시작하는 것을 의미하며, -1은 마지막 아이템을, -2는 마지막에서 두 번째 아이템을, 그리고 리스트/튜플 길이의 음수값은 첫 번째 아이템을 의미합니다.
  ![Tuple Negative indexing](../../images/tuple_negative_indexing.png)

  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  first_item = tpl[-4]
  second_item = tpl[-3]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[-4]
  second_fruit = fruits[-3]
  last_fruit = fruits[-1]
  ```

### Slicing tuples

인덱스 범위(시작 위치와 끝 위치)를 지정하여 하위 튜플을 슬라이스할 수 있습니다. 반환 값은 지정된 아이템을 포함하는 새 튜플입니다.

- 양수 인덱스 범위

  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # 모든 아이템
  all_items = tpl[0:]         # 모든 아이템
  middle_two_items = tpl[1:3]  # 인덱스 3의 아이템은 포함하지 않습니다
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # 모든 아이템
  all_fruits= fruits[0:]      # 모든 아이템
  orange_mango = fruits[1:3]  # 인덱스 3의 아이템은 포함하지 않습니다
  orange_to_the_rest = fruits[1:]
  ```

- 음수 인덱스 범위

  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # 모든 아이템
  middle_two_items = tpl[-3:-1]  # 인덱스 3(-1)의 아이템은 포함하지 않습니다
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # 모든 아이템
  orange_mango = fruits[-3:-1]  # 인덱스 3의 아이템은 포함하지 않습니다
  orange_to_the_rest = fruits[-3:]
  ```

### Changing Tuples to Lists

튜플을 리스트로, 리스트를 튜플로 변경할 수 있습니다. 튜플은 불변이므로 튜플을 수정하려면 리스트로 변경해야 합니다.

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### Checking an Item in a Tuple

_in_ 을 사용하여 튜플에 아이템이 존재하는지 확인할 수 있으며, 불리언 값을 반환합니다.

```py
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

### Joining Tuples

+ 연산자를 사용하여 두 개 이상의 튜플을 결합할 수 있습니다.

```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

### Deleting Tuples

튜플에서 하나의 아이템을 제거하는 것은 불가능하지만 _del_ 을 사용하여 튜플 자체를 삭제하는 것은 가능합니다.

```py
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

🌕 당신은 매우 용감하며, 여기까지 해냈습니다. 6일차 도전을 완료했으며 위대함을 향한 6걸음 앞에 있습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 Exercises: Day 6

### Exercises: Level 1

1. 빈 튜플을 만듭니다
2. 여러분의 자매와 형제의 이름이 포함된 튜플을 만듭니다 (가상의 형제도 괜찮습니다)
3. brothers와 sisters 튜플을 결합하여 siblings에 할당합니다
4. 형제자매가 몇 명인가요?
5. siblings 튜플을 수정하여 아버지와 어머니의 이름을 추가하고 family_members에 할당합니다

### Exercises: Level 2

1. family_members에서 siblings와 parents를 언패킹합니다
1. fruits, vegetables, animal products 튜플을 만듭니다. 세 개의 튜플을 결합하여 food_stuff_tp라는 변수에 할당합니다.
1. food_stuff_tp 튜플을 food_stuff_lt 리스트로 변경합니다
1. food_stuff_tp 튜플 또는 food_stuff_lt 리스트에서 중간 아이템을 슬라이스합니다.
1. food_stuff_lt 리스트에서 처음 세 개의 아이템과 마지막 세 개의 아이템을 슬라이스합니다
1. food_stuff_tp 튜플을 완전히 삭제합니다
1. 튜플에 아이템이 존재하는지 확인합니다:

- 'Estonia'가 nordic country인지 확인합니다
- 'Iceland'가 nordic country인지 확인합니다

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```


[<< Day 5](../05_Day_Lists/05_lists.md) | [Day 7 >>](../07_Day_Sets/07_sets.md)

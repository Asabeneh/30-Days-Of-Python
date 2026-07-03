<div align="center">   <h1> 30 Days Of Python: Day 7 - Sets</h1>   <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">   <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">   </a>   <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">   <img src="https://img.shields.io/twitter/follow/asabeneh?style=social" alt="Twitter Follow">   </a>
</div>
<p data-md-type="paragraph"><sub data-md-type="raw_html">Author: <a data-md-type="raw_html" href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br> <small data-md-type="raw_html"> Second Edition: July, 2021</small></sub></p>
<div data-md-type="block_html"></div>

[&lt;&lt; Day 6](../06_Day_Tuples/06_tuples.md) | [Day 8 &gt;&gt;](../08_Day_Dictionaries/08_dictionaries.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 7](#-day-7)
    - [Sets](#sets)
        - [세트 만들기](#세트-만들기)
        - [세트의 길이 구하기](#세트의-길이-구하기)
        - [세트의 항목에 액세스](#세트의-항목에-엑세스)
        - [항목 확인](#항목-확인)
        - [세트에 항목 추가](#세트에-항목-추가)
        - [세트에서 항목 제거](#세트에서-항목-제거)
        - [세트의 항목 지우기](#세트의-항목-지우기)
        - [세트 삭제](#세트-삭제)
        - [목록을 집합으로 변환](#목록을-집합으로-변환)
        - [집합 결합](#집합-결합)
        - [교차 항목 찾기](#교차-항목-찾기)
        - [하위 집합 및 수퍼 집합 확인](#하위-집합-및-수퍼-집합-확인)
        - [두 세트 간의 차이 확인](#두-세트-간의-차이-확인)
        - [두 집합 간의 대칭적 차이 찾기](#두-집합-간의-대칭적-차이-찾기)
        - [집합 결합](#집합-결합)
    - [💻 Exercises: Day 7](#-exercises-day-7)
        - [Exercises: Level 1](#exercises-level-1)
        - [Exercises: Level 2](#exercises-level-2)
        - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 7

## Sets

세트는 항목의 모음입니다. 초등학교 또는 고등학교 수학 수업으로 돌아가겠습니다. 집합의 수학 정의는 Python에서도 적용될 수 있습니다. 집합은 순서가 지정되지 않고 인덱싱되지 않은 개별 요소의 모음입니다. Python에서 집합은 고유한 항목을 저장하는 데 사용되며 집합 간에 *합집합* , *교차* , *차이* , *대칭적 차이* , *하위 집합* , *상위 집합* 및 *분리 집합* 을 찾을 수 있습니다.

### 세트 만들기

중괄호 {}를 사용하여 세트 또는 *set()* 내장 함수를 생성합니다.

- 빈 세트 만들기

```py
# syntax
st = {}
# or
st = set()
```

- 초기 항목으로 세트 만들기

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

**예시:**

```py
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### 세트의 길이 구하기

**len()** 메서드를 사용하여 집합의 길이를 찾습니다.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(set)
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

### 세트의 항목에 액세스

루프를 사용하여 항목에 액세스합니다. 우리는 루프 섹션에서 이것을 볼 것입니다

### 항목 확인

목록에 항목이 있는지 확인하기 위해 멤버십 연산자 *에서* 사용합니다.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### 세트에 항목 추가

세트가 생성되면 항목을 변경할 수 없으며 항목을 추가할 수도 있습니다.

- *add()* 를 사용하여 하나의 항목 추가

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

- *update()* 를 사용하여 여러 항목 추가 *update()* 를 사용하면 세트에 여러 항목을 추가할 수 있습니다. *update()* 는 목록 인수를 사용합니다.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### <a>세트에서 항목 제거</a>

*remove()* 메서드를 사용하여 집합에서 항목을 제거할 수 있습니다. 항목을 찾을 수 없으면 *remove()* 메서드는 오류를 발생시키므로 해당 항목이 주어진 집합에 있는지 확인하는 것이 좋습니다. 그러나, *discard()* 메서드는 오류를 발생시키지 않습니다.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

pop() 메서드는 목록에서 임의의 항목을 제거하고 제거된 항목을 반환합니다.

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set

```

제거된 항목에 관심이 있는 경우.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
```

### 세트의 항목 지우기

세트를 지우거나 비우려면 *clear* 메소드를 사용합니다.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### 세트 삭제

세트 자체를 삭제하려면 *del* 연산자를 사용합니다.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### 목록을 집합으로 변환

리스트를 세트로, 세트를 리스트로 변환할 수 있습니다. 목록을 세트로 변환하면 중복 항목이 제거되고 고유한 항목만 예약됩니다.

```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

**예시:**

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### 집합 결합

*union()* 또는 *update()* 메서드를 사용하여 두 집합을 결합할 수 있습니다.

- Union 이 메서드는 새 집합을 반환합니다.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

- 업데이트 이 메서드는 주어진 집합에 집합을 삽입합니다.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

**예시:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

### 교차 항목 찾기

Intersection은 두 집합 모두에 있는 항목 집합을 반환합니다. 예를 참조하십시오

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```

**예시:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```

### 하위 집합 및 수퍼 집합 확인

집합은 다른 집합의 하위 집합 또는 상위 집합일 수 있습니다.

- Subset: *issubset()*
- Super set: *issuperset*

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**예시:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### 두 세트 간의 차이 확인

두 집합 간의 차이를 반환합니다.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

**예시:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### 두 집합 간의 대칭적 차이 찾기

두 집합 간의 대칭 차이를 반환합니다. 수학적으로 두 세트에 있는 항목을 제외하고 두 세트의 모든 항목을 포함하는 세트를 리턴한다는 의미입니다. (A\B) ∪ (B\A)

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```

**예시:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

### 집합 결합

두 세트에 공통 항목이 없으면 분리 세트라고 합니다. *isdisjoint()* 메서드를 사용하여 두 집합이 결합인지 분리인지 확인할 수 있습니다.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

**예시:**

```py
even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
```

🌕 당신은 떠오르는 별입니다. 당신은 방금 7일차 챌린지를 완료했으며 위대함을 향한 당신의 길에 7걸음 앞서 있습니다. 이제 뇌와 근육을 위한 몇 가지 훈련을 하십시오.

## 💻 Exercises: Day 7

```py
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Exercises: Level 1

1. 집합 it_companies의 길이 찾기
2. it_companies에 'Twitter' 추가
3. it_companies 집합에 여러 IT 회사를 한 번에 삽입
4. it_companies 집합에서 회사 중 하나를 제거합니다.
5. 제거하다와 버리다의 차이점은 무엇인가요?

### Exercises: Level 2

1. A와 B를 결합
2. <a>교차 항목 찾기</a>
3. A는 B의 부분집합
4. A와 B는 서로소 집합입니다.
5. A는 B와, B는 A와 조인
6. A와 B의 대칭 차이는 무엇입니까
7. 세트를 완전히 삭제

### Exercises: Level 3

1. 연령을 세트로 변환하고 목록의 길이와 세트의 길이를 비교합니다. 어느 것이 더 큽니까?
2. 문자열, 목록, 튜플 및 집합과 같은 데이터 유형의 차이점을 설명하십시오.
3. *저는 교사이고 사람들에게 영감을 주고 가르치는 것을 좋아합니다.* 문장에 사용된 독특한 단어는 몇 개입니까? 분할 방법을 사용하고 고유한 단어를 가져오도록 설정합니다.

🎉 축하합니다! 🎉

[&lt;&lt; 6일차](../06_Day_Tuples/06_tuples.md) | [8일차 &gt;&gt;](../08_Day_Dictionaries/08_dictionaries.md)

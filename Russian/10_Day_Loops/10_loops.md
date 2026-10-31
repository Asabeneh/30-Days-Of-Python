<div align="center">
  <h1> 30 дней Python: День 10 - Циклы</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Асабенех Йетаех</a><br>
<small> Второе издание: июль 2021</small>
</sub>

</div>

[<< День 9](../09_Day_Conditionals/09_conditionals.md) | [День 11 >>](../11_Day_Functions/11_functions.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 10](#-день-10)
  - [Циклы](#циклы)
    - [Цикл While](#цикл-while)
    - [Break и Continue - Часть 1](#break-и-continue--часть-1)
    - [Цикл For](#цикл-for)
    - [Break и Continue - Часть 2](#break-и-continue--часть-2)
    - [Функция Range](#функция-range)
    - [Вложенный цикл For](#вложенный-цикл-for)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [💻 Упражнения: День 10](#-упражнения-день-10)
    - [Упражнения: Уровень 1](#упражнения-уровень-1)
    - [Упражнения: Уровень 2](#упражнения-уровень-2)
    - [Упражнения: Уровень 3](#упражнения-уровень-3)

# 📘 День 10

## Циклы

Жизнь полна рутины. В программировании мы тоже выполняем множество повторяющихся задач. Чтобы справляться с повторяющимися задачами, языки программирования используют циклы. Язык программирования Python также предоставляет следующие два типа циклов:

1. цикл while
2. цикл for

### Цикл While

Мы используем зарезервированное слово _while_ для создания цикла while. Он используется для многократного выполнения блока операторов, пока заданное условие не будет выполнено. Когда условие становится ложным, код после цикла продолжит выполняться.

```py
  # синтаксис
while condition:
    code goes here
```

**Пример:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
# выводит от 0 до 4
```

В приведённом выше цикле while условие становится ложным, когда count равно 5. Именно тогда цикл останавливается.
Если мы хотим выполнить блок кода один раз, когда условие больше не истинно, мы можем использовать _else_.

```py
  # синтаксис
while condition:
    code goes here
else:
    code goes here
```

**Пример:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

Условие приведённого выше цикла будет ложным, когда count равно 5, и цикл останавливается, и начинает выполняться оператор else. В результате будет выведено 5.

### Break и Continue - Часть 1

- Break: Мы используем break, когда хотим выйти из цикла или остановить его.

```py
# синтаксис
while condition:
    code goes here
    if another_condition:
        break
```

**Пример:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

Приведённый выше цикл while выводит только 0, 1, 2, но когда он достигает 3, он останавливается.

- Continue: С помощью оператора continue мы можем пропустить текущую итерацию и продолжить со следующей:

```py
  # синтаксис
while condition:
    code goes here
    if another_condition:
        continue
```

**Пример:**

```py
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

Приведённый выше цикл while выводит только 0, 1, 2 и 4 (пропускает 3).

### Цикл For

Ключевое слово _for_ используется для создания цикла for, аналогично другим языкам программирования, но с некоторыми отличиями в синтаксисе. Цикл используется для итерации по последовательности (это может быть список, кортеж, словарь, множество или строка).

- Использование цикла For для списка

```py
# синтаксис
for iterator in lst:
    code goes here
```

**Пример:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number - временное имя для ссылки на элементы списка, действует только внутри этого цикла
    print(number)       # числа будут выводиться построчно, от 0 до 5
```

- Использование цикла For для строки

```py
# синтаксис
for iterator in string:
    code goes here
```

**Пример:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- Использование цикла For для кортежа

```py
# синтаксис
for iterator in tpl:
    code goes here
```

**Пример:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- Цикл For для словаря
  Итерация по словарю даёт вам ключ словаря.

```py
  # синтаксис
for iterator in dct:
    code goes here
```

**Пример:**

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
    print(key, value) # таким образом выводятся и ключи, и значения
```

- Использование цикла For для множества

```py
# синтаксис
for iterator in st:
    code goes here
```

**Пример:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break и Continue - Часть 2

Краткое напоминание:
_Break_: Мы используем break, когда хотим остановить наш цикл до его завершения.

```py
# синтаксис
for iterator in sequence:
    code goes here
    if condition:
        break
```

**Пример:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

В приведённом выше примере цикл останавливается, когда достигает 3.

Continue: Мы используем continue, когда хотим пропустить некоторые шаги в итерации цикла.

```py
  # синтаксис
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**Пример:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # для сокращённых условий нужны оба оператора if и else
print('outside the loop')
```

В приведённом выше примере, если число равно 3, шаг _после_ условия (но внутри цикла) пропускается, и выполнение цикла продолжается, если остались ещё итерации.

### Функция Range

Функция _range()_ используется для возврата списка чисел. _range(start, end, step)_ принимает три параметра: начало, конец и шаг. По умолчанию она начинается с 0, а шаг равен 1. Последовательность range требует как минимум 1 аргумент (end).
Создание последовательностей с помощью range

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 аргумента указывают начало и конец последовательности, шаг установлен по умолчанию 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

    # для обратного отсчёта от начала к концу
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

```py
# синтаксис
for iterator in range(start, end, step):
```

**Пример:**

```py
for number in range(11):
    print(number)   # выводит от 0 до 10, не включая 11
```

### Вложенный цикл For

Мы можем писать циклы внутри цикла.

```py
# синтаксис
for x in y:
    for t in x:
        print(t)
```

**Пример:**

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

Если мы хотим вывести некоторое сообщение, когда цикл завершается, мы используем else.

```py
# синтаксис
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**Пример:**

```py
for number in range(11):
    print(number)   # выводит от 0 до 10, не включая 11
else:
    print('The loop stops at', number)
```

### Pass

В Python, когда требуется оператор (после двоеточия), но мы не хотим выполнять там какой-либо код, мы можем написать слово _pass_, чтобы избежать ошибок. Также мы можем использовать его как заполнитель для будущих операторов.

**Пример:**

```py
for number in range(6):
    pass
```

🌕 Ты достиг важной вехи, тебя не остановить. Продолжай! Ты только что завершил испытания десятого дня, и ты на 10 шагов впереди на пути к величию. Теперь выполни несколько упражнений для своего мозга и мышц.

## 💻 Упражнения: День 10

### Упражнения: Уровень 1

1. Пройди от 0 до 10 с помощью цикла for, сделай то же самое с помощью цикла while.
2. Пройди от 10 до 0 с помощью цикла for, сделай то же самое с помощью цикла while.
3. Напиши цикл, который делает семь вызовов print(), чтобы получить на выходе следующий треугольник:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Используй вложенные циклы для создания следующего:

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

5. Выведи следующий шаблон:

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

6. Пройди по списку ['Python', 'Numpy','Pandas','Django', 'Flask'] с помощью цикла for и выведи элементы.
7. Используй цикл for для итерации от 0 до 100 и выведи только чётные числа
8. Используй цикл for для итерации от 0 до 100 и выведи только нечётные числа

### Упражнения: Уровень 2

1.  Используй цикл for для итерации от 0 до 100 и выведи сумму всех чисел.

```sh
The sum of all numbers is 5050.
```

2. Используй цикл for для итерации от 0 до 100 и выведи сумму всех чётных и сумму всех нечётных чисел.

   ```sh
   The sum of all evens is 2550. And the sum of all odds is 2500.
   ```

### Упражнения: Уровень 3

1. Перейди в папку data и используй файл [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py). Пройди по всем странам и извлеки те, названия которых содержат слово _land_.
1. Это список фруктов, ['banana', 'orange', 'mango', 'lemon'], разверни порядок с помощью цикла.
1. Перейди в папку data и используй файл [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
   1. Каково общее количество языков в данных
   2. Найди десять самых распространённых языков в данных
   3. Найди 10 самых населённых стран мира

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 9](../09_Day_Conditionals/09_conditionals.md) | [День 11 >>](../11_Day_Functions/11_functions.md)

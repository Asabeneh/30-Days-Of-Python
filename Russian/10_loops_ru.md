<div align="center">
  <h1> 30 Days Of Python: День 10 - Циклы</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Второе издание: июль 2021</small>
</sub>

</div>

[<< День 9](./09_conditionals_ru.md) | [День 11 >>](./11_functions_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 10](#-день-10)
  - [Циклы](#циклы)
    - [Цикл while](#цикл-while)
    - [Break и Continue - часть 1](#break-и-continue---часть-1)
    - [Цикл for](#цикл-for)
    - [Break и Continue - часть 2](#break-и-continue---часть-2)
    - [Функция range](#функция-range)
    - [Вложенный цикл for](#вложенный-цикл-for)
    - [For else](#for-else)
    - [Pass](#pass)
  - [💻 Упражнения: День 10](#-упражнения-день-10)
    - [Упражнения: уровень 1](#упражнения-уровень-1)
    - [Упражнения: уровень 2](#упражнения-уровень-2)
    - [Упражнения: уровень 3](#упражнения-уровень-3)

# 📘 День 10

## Циклы

Жизнь полна рутины. В программировании мы также выполняем множество повторяющихся задач. Чтобы справляться с повторяющимися задачами, языки программирования используют циклы. Язык программирования Python также предоставляет следующие два типа циклов:

1. цикл while
2. цикл for

### Цикл while

Мы используем зарезервированное слово _while_, чтобы создать цикл while. Он используется для повторного выполнения блока инструкций до тех пор, пока не будет выполнено заданное условие. Когда условие становится ложным, строки кода после цикла продолжают выполняться.

```py
  # синтаксис
while condition:
    здесь код
```

**Пример:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#печатает от 0 до 4
```

В приведённом выше цикле while условие становится ложным, когда count равно 5. Именно тогда цикл останавливается.
Если мы хотим выполнить блок кода, когда условие больше не истинно, мы можем использовать _else_.

```py
  # синтаксис
while condition:
    здесь код
else:
    здесь код
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

Условие приведённого выше цикла станет ложным, когда count будет равно 5, цикл остановится, и начнётся выполнение инструкции else. В результате будет напечатано 5.

### Break и Continue - часть 1

- Break: мы используем break, когда хотим выйти из цикла или остановить его.

```py
# синтаксис
while condition:
    здесь код
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

Приведённый выше цикл while печатает только 0, 1, 2, но когда он доходит до 3, он останавливается.

- Continue: с помощью инструкции continue мы можем пропустить текущую итерацию и продолжить со следующей:

```py
  # синтаксис
while condition:
    здесь код
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

Приведённый выше цикл while печатает только 0, 1, 2 и 4 (пропускает 3).

### Цикл for

Ключевое слово _for_ используется для создания цикла for, как и в других языках программирования, но с некоторыми различиями в синтаксисе. Цикл используется для итерации по последовательности (это может быть список, кортеж, словарь, множество или строка).

- Использование цикла for со списком

```py
# синтаксис
for iterator in lst:
    здесь код
```

**Пример:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number — временное имя для обращения к элементам списка, действительно только внутри этого цикла
    print(number)       # числа будут напечатаны построчно, от 0 до 5
```

- Использование цикла for со строкой

```py
# синтаксис
for iterator in string:
    здесь код
```

**Пример:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- Использование цикла for с кортежем

```py
# синтаксис
for iterator in tpl:
    здесь код
```

**Пример:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- Цикл for со словарём
  Итерация по словарю даёт вам ключ словаря.

```py
  # синтаксис
for iterator in dct:
    здесь код
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
    print(key, value) # так мы печатаем и ключи, и значения
```

- Использование цикла for с множеством

```py
# синтаксис
for iterator in st:
    здесь код
```

**Пример:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break и Continue - часть 2

Короткое напоминание:
_Break_: мы используем break, когда хотим остановить наш цикл до его завершения.

```py
# синтаксис
for iterator in sequence:
    здесь код
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

В приведённом выше примере цикл останавливается, когда доходит до 3.

Continue: мы используем continue, когда хотим пропустить некоторые шаги в итерации цикла.

```py
  # синтаксис
for iterator in sequence:
    здесь код
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
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # для сокращённых условий нужны и if, и else
print('outside the loop')
```

В приведённом выше примере, если число равно 3, шаг _после_ условия (но внутри цикла) пропускается, и выполнение цикла продолжается, если остались итерации.

### Функция range

Функция _range()_ используется для возврата списка чисел. _range(start, end, step)_ принимает три параметра: начало, конец и приращение. По умолчанию она начинается с 0, а приращение равно 1. Последовательности range нужен как минимум 1 аргумент (end).
Создание последовательностей с помощью range

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 аргумента указывают начало и конец последовательности, шаг по умолчанию 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# для обратного прохода от начала к концу
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
    print(number)   # печатает от 0 до 10, не включая 11
```

### Вложенный цикл for

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

### For else

Если мы хотим выполнить какое-то сообщение, когда цикл завершается, мы используем else.

```py
# синтаксис
for iterator in range(start, end, step):
    делаем что-то
else:
    print('The loop ended')
```

**Пример:**

```py
for number in range(11):
    print(number)   # печатает от 0 до 10, не включая 11
else:
    print('The loop stops at', number)
```

### Pass

В python, когда требуется инструкция (после точки с запятой), но мы не хотим выполнять там какой-либо код, мы можем написать слово _pass_, чтобы избежать ошибок. Также мы можем использовать его как заглушку для будущих инструкций.

**Пример:**

```py
for number in range(6):
    pass
```

🌕 Вы достигли большого рубежа, вас не остановить. Продолжайте! Вы только что завершили испытания дня 10, и вы на 10 шагов ближе к своему пути к величию. Теперь сделайте несколько упражнений для своего мозга и мышц.

## 💻 Упражнения: День 10

### Упражнения: уровень 1

1. Пройдитесь циклом for от 0 до 10, сделайте то же самое с помощью цикла while.
2. Пройдитесь циклом for от 10 до 0, сделайте то же самое с помощью цикла while.
3. Напишите цикл, который делает семь вызовов print(), чтобы на выходе мы получили следующий треугольник:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Используйте вложенные циклы, чтобы создать следующее:

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

5. Напечатайте следующий шаблон:

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

6. Пройдитесь по списку ['Python', 'Numpy','Pandas','Django', 'Flask'] с помощью цикла for и напечатайте его элементы.
7. Используйте цикл for, чтобы пройти от 0 до 100 и напечатать только чётные числа
8. Используйте цикл for, чтобы пройти от 0 до 100 и напечатать только нечётные числа

### Упражнения: уровень 2

1.  Используйте цикл for, чтобы пройти от 0 до 100 и напечатать сумму всех чисел.

```sh
The sum of all numbers is 5050.
```

2. Используйте цикл for, чтобы пройти от 0 до 100 и напечатать сумму всех чётных и сумму всех нечётных чисел.

   ```sh
   The sum of all evens is 2550. And the sum of all odds is 2500.
   ```

### Упражнения: уровень 3

1. Перейдите в папку data и используйте файл [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py). Пройдитесь циклом по странам и извлеките все страны, содержащие слово _land_.
1. Это список фруктов ['banana', 'orange', 'mango', 'lemon'], измените порядок на обратный с помощью цикла.
1. Перейдите в папку data и используйте файл [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
   1. Каково общее число языков в данных
   2. Найдите десять самых распространённых языков из данных
   3. Найдите 10 самых населённых стран мира

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 9](./09_conditionals_ru.md) | [День 11 >>](./11_functions_ru.md)

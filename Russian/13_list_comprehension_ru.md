<div align="center">
  <h1> 30 дней Python: День 13 — List Comprehension</h1>
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

[<< День 12](./12_modules_ru.md) | [День 14>>](./14_higher_order_functions_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 13](#-день-13)
  - [List Comprehension](#list-comprehension)
  - [Лямбда-функция](#лямбда-функция)
    - [Создание лямбда-функции](#создание-лямбда-функции)
    - [Лямбда-функция внутри другой функции](#лямбда-функция-внутри-другой-функции)
  - [💻 Упражнения: День 13](#-упражнения-день-13)

# 📘 День 13

## List Comprehension

List comprehension в Python — это компактный способ создания списка из последовательности. Это короткий способ создать новый список. List comprehension значительно быстрее, чем обработка списка с помощью цикла _for_.

```py
# синтаксис
[expression for i in iterable if condition]
```

**Пример:1**

Например, если вы хотите преобразовать строку в список символов. Вы можете использовать пару методов. Давайте рассмотрим некоторые из них:

```py
# Один способ
language = 'Python'
lst = list(language) # преобразование строки в список
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Второй способ: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**Пример:2**

Например, если вы хотите сгенерировать список чисел

```py
# Генерация чисел
numbers = [i for i in range(11)]  # чтобы сгенерировать числа от 0 до 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Во время итерации можно выполнять математические операции
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Также можно создать список кортежей
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**Пример:2**

List comprehension можно комбинировать с выражением if


```py
# Генерация чётных чисел
even_numbers = [i for i in range(21) if i % 2 == 0]  # чтобы сгенерировать список чётных чисел в диапазоне от 0 до 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Генерация нечётных чисел
odd_numbers = [i for i in range(21) if i % 2 != 0]  # чтобы сгенерировать нечётные числа в диапазоне от 0 до 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Фильтрация чисел: отфильтруем положительные чётные числа из списка ниже
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Разворачивание двумерного массива
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Лямбда-функция

Лямбда-функция — это небольшая анонимная функция без имени. Она может принимать любое количество аргументов, но может иметь только одно выражение. Лямбда-функция похожа на анонимные функции в JavaScript. Она нужна нам, когда мы хотим написать анонимную функцию внутри другой функции.

### Создание лямбда-функции

Чтобы создать лямбда-функцию, мы используем ключевое слово _lambda_, за которым следуют параметр(ы), а затем выражение. Смотрите синтаксис и пример ниже. Лямбда-функция не использует return, но она явно возвращает выражение.

```py
# синтаксис
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

**Пример:**

```py
# Именованная функция
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Преобразуем функцию выше в лямбда-функцию
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Самовызывающаяся лямбда-функция
(lambda a, b: a + b)(2,3) # 5 - нужно обернуть в print(), чтобы увидеть результат в консоли

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Несколько переменных
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### Лямбда-функция внутри другой функции

Использование лямбда-функции внутри другой функции.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # функции power теперь нужно 2 аргумента для запуска, в отдельных круглых скобках
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

🌕 Продолжайте в том же духе. Не теряйте импульс, предела возможностям нет! Вы только что завершили испытания тринадцатого дня и вы на 13 шагов ближе на своём пути к величию. Теперь сделайте несколько упражнений для мозга и мышц.

## 💻 Упражнения: День 13

1. Отфильтруйте только отрицательные числа и ноль в списке с помощью list comprehension
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. Разверните следующий список списков списков в одномерный список :

   ```py
   list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. Используя list comprehension, создайте следующий список кортежей:
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
4. Разверните следующий список в новый список:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
5. Преобразуйте следующий список в список словарей:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
6. Преобразуйте следующий список списков в список объединённых строк:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
7. Напишите лямбда-функцию, которая может находить наклон или точку пересечения с осью y линейных функций.

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 12](./12_modules_ru.md) | [День 14>>](./14_higher_order_functions_ru.md)

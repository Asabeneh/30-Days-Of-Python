<div align="center">
  <h1> 30 дней Python: День 11 - Функции</h1>
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

[<< День 10](../10_Day_Loops/10_loops.md) | [День 12 >>](../12_Day_Modules/12_modules.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 11](#-день-11)
  - [Функции](#функции)
    - [Определение функции](#определение-функции)
    - [Объявление и вызов функции](#объявление-и-вызов-функции)
    - [Функция без параметров](#функция-без-параметров)
    - [Функция, возвращающая значение - Часть 1](#функция-возвращающая-значение--часть-1)
    - [Функция с параметрами](#функция-с-параметрами)
    - [Передача аргументов по ключу и значению](#передача-аргументов-по-ключу-и-значению)
    - [Функция, возвращающая значение - Часть 2](#функция-возвращающая-значение--часть-2)
    - [Функция с параметрами по умолчанию](#функция-с-параметрами-по-умолчанию)
    - [Произвольное количество аргументов](#произвольное-количество-аргументов)
    - [Параметры по умолчанию и произвольное количество параметров в функциях](#параметры-по-умолчанию-и-произвольное-количество-параметров-в-функциях)
    - [Распаковка словаря](#распаковка-словаря)
    - [Произвольное количество именованных аргументов](#произвольное-количество-именованных-аргументов)
    - [Функция как параметр другой функции](#функция-как-параметр-другой-функции)
  - [Отзыв](#отзыв)
  - [💻 Упражнения: День 11](#-упражнения-день-11)
    - [Упражнения: Уровень 1](#упражнения-уровень-1)
    - [Упражнения: Уровень 2](#упражнения-уровень-2)
    - [Упражнения: Уровень 3](#упражнения-уровень-3)

# 📘 День 11

## Функции

До сих пор мы видели множество встроенных функций Python. В этом разделе мы сосредоточимся на пользовательских функциях. Что такое функция? Прежде чем мы начнём создавать функции, давайте узнаем, что такое функция и зачем они нужны?

### Определение функции

Функция - это переиспользуемый блок кода или программных операторов, предназначенный для выполнения определённой задачи. Для определения или объявления функции Python предоставляет ключевое слово _def_. Ниже приведён синтаксис определения функции. Блок кода функции выполняется только если функцию вызвать (invoke).

### Объявление и вызов функции

Когда мы создаём функцию, это называется объявлением функции. Когда мы начинаем использовать её, это называется _вызовом_ (calling) или _invoking_ функции. Функции могут быть объявлены с параметрами или без них.

```py
# синтаксис
# Объявление функции
def function_name():
    codes
    codes
# Вызов функции
function_name()
```

### Функция без параметров

Функция может быть объявлена без параметров.

**Пример:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # вызов функции

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Функция, возвращающая значение - Часть 1

Функции возвращают значения с помощью оператора _return_. Если у функции нет оператора return, она возвращает None. Перепишем приведённые выше функции с использованием return. С этого момента мы получаем значение из функции, когда вызываем её, и выводим его.

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

### Функция с параметрами

В функцию мы можем передавать различные типы данных (число, строку, логическое значение, список, кортеж, словарь или множество) в качестве параметров.

- Один параметр: если наша функция принимает параметр, мы должны вызывать её с аргументом

```py
  # синтаксис
  # Объявление функции
  def function_name(parameter):
    codes
    codes
  # Вызов функции
  print(function_name(argument))
```

**Пример:**

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

- Два параметра: функция может иметь или не иметь параметр или параметры. Функция также может иметь два или более параметров. Если наша функция принимает параметры, мы должны вызывать её с аргументами. Давайте проверим функцию с двумя параметрами:

```py
  # синтаксис
  # Объявление функции
  def function_name(para1, para2):
    codes
    codes
  # Вызов функции
  print(function_name(arg1, arg2))
```

**Пример:**

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
    weight = str(mass * gravity)+ ' N' # значение сначала должно быть преобразовано в строку
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Передача аргументов по ключу и значению

Если мы передаём аргументы по ключу и значению, порядок аргументов не имеет значения.

```py
# синтаксис
# Объявление функции
def function_name(para1, para2):
    codes
    codes
# Вызов функции
print(function_name(para1 = 'John', para2 = 'Doe')) # порядок аргументов здесь не имеет значения
```

**Пример:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Порядок не имеет значения 
```

### Функция, возвращающая значение - Часть 2

Если мы не возвращаем значение из функции, то наша функция по умолчанию возвращает _None_. Чтобы вернуть значение из функции, мы используем ключевое слово _return_, за которым следует переменная, которую мы возвращаем. Мы можем возвращать из функции любые типы данных.

- Возврат строки:
**Пример:**

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

- Возврат числа:

**Пример:**

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

- Возврат логического значения:
  **Пример:**

```py
def is_even (n):
    if n % 2 == 0:
        return True    # return останавливает дальнейшее выполнение функции, аналогично break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Возврат списка:
  **Пример:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Функция с параметрами по умолчанию

Иногда мы передаём значения по умолчанию параметрам, когда вызываем функцию. Если мы не передаём аргументы при вызове функции, используются их значения по умолчанию.

```py
# синтаксис
# Объявление функции
def function_name(param = value):
    codes
    codes
# Вызов функции
function_name()
function_name(arg)
```

**Пример:**

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
    weight = str(mass * gravity)+ ' N' # значение сначала должно быть преобразовано в строку
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - средняя гравитация на поверхности Земли
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # гравитация на поверхности Луны
```

### Произвольное количество аргументов

Если мы не знаем количество аргументов, передаваемых нашей функции, мы можем создать функцию, которая принимает произвольное количество аргументов, добавив \* перед именем параметра.

```py
# синтаксис
# Объявление функции
def function_name(*args):
    codes
    codes
# Вызов функции
function_name(param1, param2, param3,..)
```

**Пример:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # то же самое, что и total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Параметры по умолчанию и произвольное количество параметров в функциях

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```
### Распаковка словаря

Вы можете вызвать функцию с именованными аргументами, используя словарь с соответствующими именами ключей. Для этого используется ``**``.

```py
# Определите функцию, принимающую два аргумента: 'name' и 'location'
def greet(name, location):
    # Выведите приветственное сообщение с использованием предоставленных аргументов
    print("Hi there", name, "how is the weather in", location)

# Вызовите функцию с именованными аргументами
greet(name="Alice", location="New York")  
# Вывод: Hi there Alice how is the weather in New York

# Создайте словарь с ключами, соответствующими именам параметров функции
my_dict = {"name": "Alice", "location": "New York"}

# Вызовите функцию с помощью распаковки словаря
greet(**my_dict)  
# Оператор ** распаковывает словарь, передавая его пары ключ-значение 
# в качестве именованных аргументов функции.
# Вывод: Hi there Alice how is the weather in New York
```

### Произвольное количество именованных аргументов

Вы также можете определить функцию для приёма произвольного количества именованных аргументов.

```py
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
```

Как правило, избегайте этого, если это не требуется, так как это затрудняет понимание того, что принимает и делает функция.

### Функция как параметр другой функции

```py
#Вы можете передавать функции как параметры
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 Ты уже многого достиг. Продолжай! Ты только что завершил испытания одиннадцатого дня, и ты на 11 шагов впереди на пути к величию. Теперь выполни несколько упражнений для своего мозга и мышц.

## Отзыв

Теперь пришло время выразить свои мысли об авторе и 30DaysOfPython. Вы можете оставить свой отзыв по этой [ссылке](https://testimonial-s3sw.onrender.com/)

## 💻 Упражнения: День 11

### Упражнения: Уровень 1

1. Объяви функцию _add_two_numbers_. Она принимает два параметра и возвращает сумму.
2. Площадь круга вычисляется следующим образом: area = π x r x r. Напиши функцию, которая вычисляет _area_of_circle_.
3. Напиши функцию add_all_nums, которая принимает произвольное количество аргументов и суммирует все аргументы. Проверь, все ли элементы списка являются числовыми типами. Если нет, сообщи об этом понятным образом (дай разумную обратную связь).
4. Температуру в °C можно преобразовать в °F по этой формуле: °F = (°C x 9/5) + 32. Напиши функцию, которая преобразует °C в °F, _convert_celsius_to-fahrenheit_.
5. Напиши функцию check-season, которая принимает параметр месяца и возвращает сезон: Осень, Зима, Весна или Лето.
6. Напиши функцию calculate_slope, которая возвращает наклон линейного уравнения
7. Квадратное уравнение вычисляется следующим образом: ax² + bx + c = 0. Напиши функцию, которая вычисляет множество решений квадратного уравнения, _solve_quadratic_eqn_.
8. Объяви функцию print_list. Она принимает список в качестве параметра и выводит каждый элемент списка.
9. Объяви функцию reverse_list. Она принимает массив в качестве параметра и возвращает обратный порядок массива (используй циклы).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
```

10. Объяви функцию capitalize_list_items. Она принимает список в качестве параметра и возвращает список элементов с заглавной буквы
11. Объяви функцию add_item. Она принимает список и элемент в качестве параметров. Она возвращает список с добавленным в конец элементом.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. Объяви функцию remove_item. Она принимает список и элемент в качестве параметров. Она возвращает список с удалённым элементом.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Объяви функцию sum_of_numbers. Она принимает параметр-число и суммирует все числа в этом диапазоне.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. Объяви функцию sum_of_odds. Она принимает параметр-число и суммирует все нечётные числа в этом диапазоне.
15. Объяви функцию sum_of_even. Она принимает параметр-число и суммирует все чётные числа в этом диапазоне.

### Упражнения: Уровень 2

1. Объяви функцию evens_and_odds. Она принимает положительное целое число в качестве параметра и подсчитывает количество чётных и нечётных чисел в этом числе.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

1. Вызови свою функцию factorial, она принимает целое число в качестве параметра и возвращает факториал числа
1. Вызови свою функцию _is_empty_, она принимает параметр и проверяет, пустой он или нет
1. Напиши различные функции, которые принимают списки. Они должны вычислять calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (стандартное отклонение).
1. Напиши функцию _greet_, которая принимает аргумент по умолчанию _name_. Если аргумент не указан, она должна вывести "Hello, Guest!", иначе - поприветствовать человека по имени.

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```
1. Создай функцию _show_args_, чтобы принимать произвольное количество именованных аргументов и выводить их имена и значения.
   ```py
   show_args(name="Alice", age=30, city="New York")
   # Received: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```


### Упражнения: Уровень 3

1. Напиши функцию is_prime, которая проверяет, является ли число простым.
1. Напиши функцию, которая проверяет, все ли элементы списка уникальны.
1. Напиши функцию, которая проверяет, все ли элементы списка одного типа данных.
1. Напиши функцию, которая проверяет, является ли предоставленная переменная допустимой переменной Python
1. Перейди в папку data и обратись к файлу countries-data.py.

- Создай функцию most_spoken_languages. Она должна возвращать 10 или 20 самых распространённых языков мира в порядке убывания
- Создай функцию most_populated_countries. Она должна возвращать 10 или 20 самых населённых стран в порядке убывания.

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 10](../10_Day_Loops/10_loops.md) | [День 12 >>](../12_Day_Modules/12_modules.md)

<div align="center">
  <h1> 30 дней Python: День 9 - Условия</h1>
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

[<< День 8](../08_Day_Dictionaries/08_dictionaries.md) | [День 10 >>](../10_Day_Loops/10_loops.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 9](#-день-9)
  - [Условия](#условия)
    - [Условие If](#условие-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Сокращённая запись](#сокращённая-запись)
    - [Вложенные условия](#вложенные-условия)
    - [Условие If и логические операторы](#условие-if-и-логические-операторы)
    - [If и логический оператор Or](#if-и-логический-оператор-or)
  - [💻 Упражнения: День 9](#-упражнения-день-9)
    - [Упражнения: Уровень 1](#упражнения-уровень-1)
    - [Упражнения: Уровень 2](#упражнения-уровень-2)
    - [Упражнения: Уровень 3](#упражнения-уровень-3)

# 📘 День 9

## Условия

По умолчанию операторы в скрипте Python выполняются последовательно сверху вниз. Если логика обработки требует этого, последовательный поток выполнения может быть изменён двумя способами:

- Условное выполнение: блок из одного или нескольких операторов будет выполняться, если определённое выражение истинно
- Повторяющееся выполнение: блок из одного или нескольких операторов будет выполняться повторно, пока определённое выражение истинно. В этом разделе мы рассмотрим операторы _if_, _else_, _elif_. Операторы сравнения и логические операторы, изученные в предыдущих разделах, будут здесь полезны.

### Условие If

В Python и других языках программирования ключевое слово _if_ используется для проверки, является ли условие истинным, и для выполнения блока кода. Помните об отступе после двоеточия.

```py
# синтаксис
if condition:
    this part of code runs for truthy conditions
```

**Пример: 1**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

Как видно из примера выше, 3 больше 0. Условие было истинным, и блок кода был выполнен. Однако если условие ложно, мы не видим результата. Чтобы увидеть результат ложного условия, нам нужен другой блок, который будет _else_.

### If Else

Если условие истинно, будет выполнен первый блок, если нет - выполнится блок else.

```py
# синтаксис
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**Пример:**

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

Условие выше оказалось ложным, поэтому был выполнен блок else. А что если у нас более двух условий? Мы можем использовать _elif_.

### If Elif Else

В повседневной жизни мы принимаем решения ежедневно. Мы принимаем решения, проверяя не одно или два условия, а множество условий. Подобно жизни, программирование тоже полно условий. Мы используем _elif_, когда у нас есть несколько условий.

```py
# синтаксис
if condition:
    code
elif condition:
    code
else:
    code

```

**Пример:**

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### Сокращённая запись

```py
# синтаксис
code if condition else code
```

**Пример:**

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # первое условие выполнено, будет выведено 'A is positive'
```

### Вложенные условия

Условия могут быть вложенными

```py
# синтаксис
if condition:
    code
    if condition:
    code
```

**Пример:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

```

Мы можем избежать написания вложенных условий, используя логический оператор _and_.

### Условие If и логические операторы

```py
# синтаксис
if condition and condition:
    code
```

**Пример:**

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

### If и логический оператор Or

```py
# синтаксис
if condition or condition:
    code
```

**Пример:**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

🌕 Ты отлично справляешься. Никогда не сдавайся, потому что великие дела требуют времени. Ты только что завершил испытания девятого дня, и теперь ты на 9 шагов впереди в своём пути к величию. Теперь сделай несколько упражнений для своего мозга и мышц.

## 💻 Упражнения: День 9

### Упражнения: Уровень 1

1. Получи пользовательский ввод с помощью input(“Enter your age: ”). Если пользователю 18 лет или больше, дай обратную связь: You are old enough to drive. Если меньше 18 лет, дай обратную связь о том, сколько лет не хватает. Вывод:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. Сравни значения my_age и your_age с помощью if … else. Кто старше (я или ты)? Используй input(“Enter your age: ”) для получения возраста в качестве ввода. Ты можешь использовать вложенное условие для вывода 'year' при разнице в возрасте в 1 год, 'years' для больших разниц и собственный текст, если my_age = your_age. Вывод:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

3. Получи два числа от пользователя с помощью prompt. Если a больше b, верни a is greater than b, если a меньше b, верни a is smaller than b, иначе a is equal to b. Вывод:

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

### Упражнения: Уровень 2

   1. Напиши код, который выставляет оценку студентам в соответствии с их баллами:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

   2. Получи месяц от пользователя, затем проверь, какой это сезон: Осень, Зима, Весна или Лето. Если пользователь вводит:
    Сентябрь, Октябрь или Ноябрь - сезон Осень.
    Декабрь, Январь или Февраль - сезон Зима.
    Март, Апрель или Май - сезон Весна
    Июнь, Июль или Август - сезон Лето
   3. Следующий список содержит некоторые фрукты:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    Если фрукта нет в списке, добавь фрукт в список и выведи изменённый список. Если фрукт существует, выведи print('That fruit already exist in the list')

### Упражнения: Уровень 3

   1. Здесь у нас есть словарь person. Не стесняйся изменять его!

```py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

     * Проверь, есть ли в словаре person ключ skills, и если да, выведи средний навык из списка skills.
     * Проверь, есть ли в словаре person ключ skills, и если да, проверь, есть ли у человека навык 'Python', и выведи результат.
     * Если навыки человека содержат только JavaScript и React, выведи print('He is a front end developer'); если навыки человека содержат Node, Python, MongoDB, выведи print('He is a backend developer'); если навыки человека содержат React, Node и MongoDB, выведи print('He is a fullstack developer'), иначе выведи print('unknown title') - для более точных результатов можно вложить больше условий!
     * Если человек женат и живёт в Финляндии, выведи информацию в следующем формате:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 8](../08_Day_Dictionaries/08_dictionaries.md) | [День 10 >>](../10_Day_Loops/10_loops.md)

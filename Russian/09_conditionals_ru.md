<div align="center">
  <h1> 30 дней Python: День 9 — Условные операторы</h1>
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

[<< День 8](./08_dictionaries_ru.md) | [День 10 >>](./10_loops_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 9](#-день-9)
  - [Условные операторы](#условные-операторы)
    - [Условие if](#условие-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Краткая запись](#краткая-запись)
    - [Вложенные условия](#вложенные-условия)
    - [Условие if и логические операторы](#условие-if-и-логические-операторы)
    - [Логические операторы if и or](#логические-операторы-if-и-or)
  - [💻 Упражнения: День 9](#-упражнения-день-9)
    - [Упражнения: Уровень 1](#упражнения-уровень-1)
    - [Упражнения: Уровень 2](#упражнения-уровень-2)
    - [Упражнения: Уровень 3](#упражнения-уровень-3)

# 📘 День 9

## Условные операторы

По умолчанию инструкции в скрипте Python выполняются последовательно сверху вниз. Если логика обработки требует этого, последовательный поток выполнения можно изменить двумя способами:

- Условное выполнение: блок из одной или нескольких инструкций будет выполнен, если определённое выражение истинно
- Повторяющееся выполнение: блок из одной или нескольких инструкций будет повторно выполняться, пока определённое выражение истинно. В этом разделе мы рассмотрим инструкции _if_, _else_, _elif_. Операторы сравнения и логические операторы, которые мы изучили в предыдущих разделах, будут здесь полезны.

### Условие if

В Python и других языках программирования ключевое слово _if_ используется, чтобы проверить, истинно ли условие, и выполнить блок кода. Помните об отступе после двоеточия.

```py
# синтаксис
if condition:
    эта часть кода выполняется для истинных условий
```

**Пример: 1**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A — положительное число
```

Как видно из примера выше, 3 больше 0. Условие было истинным, и блок кода выполнился. Однако если условие ложно, мы не увидим результат. Чтобы увидеть результат ложного условия, нам нужен другой блок — _else_.

### If Else

Если условие истинно, выполнится первый блок, если нет — выполнится блок else.

```py
# синтаксис
if condition:
    эта часть кода выполняется для истинных условий
else:
     эта часть кода выполняется для ложных условий
```

**Пример:**

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

Условие выше оказалось ложным, поэтому выполнился блок else. А если у нас больше двух условий? Мы могли бы использовать _elif_.

### If Elif Else

В повседневной жизни мы принимаем решения каждый день. Мы принимаем решения, проверяя не одно или два условия, а множество условий. Как и жизнь, программирование тоже полно условий. Мы используем _elif_, когда у нас есть несколько условий.

```py
# синтаксис
if condition:
    код
elif condition:
    код
else:
    код

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

### Краткая запись

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
    код
    if condition:
    код
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

Мы можем избежать написания вложенного условия, используя логический оператор _and_.

### Условие if и логические операторы

```py
# синтаксис
if condition and condition:
    код
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

### Логические операторы if и or

```py
# синтаксис
if condition or condition:
    код
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

🌕 Вы отлично справляетесь. Никогда не сдавайтесь, потому что великие вещи требуют времени. Вы только что завершили испытания девятого дня и вы на 9 шагов ближе на своём пути к величию. Теперь сделайте несколько упражнений для мозга и мышц.

## 💻 Упражнения: День 9

### Упражнения: Уровень 1

1. Получите ввод от пользователя с помощью input(“Enter your age: ”). Если пользователю 18 лет или больше, дайте обратную связь: You are old enough to drive. Если меньше 18, дайте обратную связь подождать недостающее количество лет. Output:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. Сравните значения my_age и your_age с помощью if … else. Кто старше (я или вы)? Используйте input(“Enter your age: ”), чтобы получить возраст в качестве ввода. Вы можете использовать вложенное условие, чтобы вывести 'year' для разницы в возрасте в 1 год, 'years' для больших разниц и пользовательский текст, если my_age = your_age. Output:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

3. Получите два числа от пользователя с помощью запроса input. Если a больше b, верните a is greater than b, если a меньше b, верните a is smaller than b, иначе a is equal to b. Output:

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

### Упражнения: Уровень 2

   1. Напишите код, который выставляет оценку студентам в соответствии с их баллами:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

   2. Получите месяц от пользователя, затем проверьте, какое время года — Autumn, Winter, Spring или Summer. Если ввод пользователя:
    September, October или November — время года Autumn.
    December, January или February — Winter.
    March, April или May — Spring
    June, July или August — Summer
   3. Следующий список содержит некоторые фрукты:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    Если фрукта нет в списке, добавьте фрукт в список и выведите изменённый список. Если фрукт существует, выведите print('That fruit already exist in the list')

### Упражнения: Уровень 3

   1. Здесь у нас есть словарь person. Не стесняйтесь его изменять!

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

     * Проверьте, есть ли в словаре person ключ skills, и если да, выведите средний навык в списке skills.
     * Проверьте, есть ли в словаре person ключ skills, и если да, проверьте, есть ли у человека навык 'Python', и выведите результат.
     * Если у человека в навыках только JavaScript и React, выведите print('He is a front end developer'), если у человека навыки Node, Python, MongoDB, выведите print('He is a backend developer'), если у человека навыки React, Node и MongoDB, выведите Print('He is a fullstack developer'), иначе выведите print('unknown title') — для более точных результатов можно вложить больше условий!
     * Если человек женат и живёт в Финляндии, выведите информацию в следующем формате:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 8](./08_dictionaries_ru.md) | [День 10 >>](./10_loops_ru.md)

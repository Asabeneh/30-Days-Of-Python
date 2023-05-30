# Арифметические операции в Python
# Целые числа

print('Сложение: ', 1 + 2)
print('Вычитание: ', 2 - 1)
print('Умножение: ', 2 * 3)
print('Деление: ', 4 / 2)                          # Результатом деления будет число с плавающей точкой (тип float)
print('Деление: ', 6 / 2)
print('Деление: ', 7 / 2)
print('Деление без остатка: ', 7 // 2)              # результат будет без плавающей точки или без остатка
print('Деление по модулю (остаток от деления): ', 3 % 2)  # результат - остаток от деления
print('Возведение в степень: ', 3 ** 2)             # эквивалентно 3 * 3

# Числа с плавающей точкой
print('Число с плавающей точкой, число пи', 3.14)
print('Число с плавающей точкой, число g', 9.81)

# Комплексные числа
print('Комплексное число: ', 1 + 1j)
print('Умножение комплексных чисел: ', (1 + 1j) * (1 - 1j))

# Сперва объявляем переменную

a = 3  # a - это название переменной, а 3 - это значение типа integer (целочисленное)
b = 2  # b - это название переменной, а 2 - это значение типа integer

# Арифметические операции и присвоение результата переменной
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Название sum больше подходит по смыслу, чем total, но sum - это название встроенной функции,
# старайтесь избегать перезапись встроенных функций
print(total)  # если не пометить print какой-нибудь строкой, будет сложно понять, что за результат выведен на печать
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Объявляем переменные и группируем их вместе в коде
num_one = 3
num_two = 4

# Арифметические операции
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Выводим на печать значения с пометкой
print('сумма: ', total)
print('разность: ', diff)
print('произведение: ', product)
print('частное: ', div)
print('остаток: ', remainder)


# Рассчитаем площадь круга
radius = 10                                 # радиус круга
area_of_circle = 3.14 * radius ** 2         # два знака * означают возведение в степень
print('Площадь круга:', area_of_circle)

# Рассчитаем площадь прямоугольника
length = 10
width = 20
area_of_rectangle = length * width
print('Площадь прямоугольника:', area_of_rectangle)

# Рассчитаем вес предмета
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'Н')

print(3 > 2)    # True, потому что 3 больше чем 2
print(3 >= 2)   # True, потому что 3 больше чем 2
print(3 < 2)    # False, потому что 3 больше чем 2
print(2 < 3)    # True, потому что 2 меньше чем 3
print(2 <= 3)   # True, потому что 2 меньше чем 3
print(3 == 2)   # False, потому что 3 не равно 2
print(3 != 2)   # True, потому что 3 не равно 2
print(len('манго') == len('авокадо'))   # False
print(len('манго') != len('авокадо'))   # True
print(len('манго') < len('авокадо'))    # True
print(len('вода') != len('мясо'))       # False
print(len('вода') == len('мясо'))       # True
print(len('томат') == len('перец'))     # True
print(len('питон') > len('бизон'))      # False

# Сравнение булевых значений
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Другой способ сравнения
print('1 это 1', 1 is 1)                    # True - потому что значения одинаковы
print('1 это не 2', 1 is not 2)             # True - потому что 1 это не 2
print('P в Python', 'P' in 'Python')        # True - символ P присутствует в строке
print('O в Python', 'O' in 'Python')        # False - в строке нет символа O в верхнем регистре
print('программирование' in 'программирование для всех')    # True - потому что программирование для всех содержит слово программирование
print('т в ты:', 'т' in 'ты')               # True
print('4 это 2 ** 2:', 4 is 2 ** 2)         # True

print(3 > 2 and 4 > 3)  # True - потому что оба выражения истинны
print(3 > 2 and 4 < 3)  # False - потому что второе выражение ложно
print(3 < 2 and 4 < 3)  # False - потому что оба выражения ложны
print(3 > 2 or 4 > 3)   # True - потому что оба выражения истинны
print(3 > 2 or 4 < 3)   # True - потому что одно из выражений истинно
print(3 < 2 or 4 < 3)   # False - потому что оба выражения ложны
print(not 3 > 2)        # False - потому что 3 > 2 это True, тогда not True это False
print(not True)         # False - Отрицание, оператор not превращает True в False
print(not False)        # True
print(not not True)     # True
print(not not False)    # False

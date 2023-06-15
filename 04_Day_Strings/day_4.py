
# Одиночная строка
letter = 'P'                # Строка может быть как одним символом, так и набором из символов (текстом)
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # Строку можно создать используя одинарные или двойные кавычки,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "Надеюсь, Вам нравится 30 дней испытаний Python."
print(sentence)

# Многострочная строка
multiline_string = '''Я - учитель и наслаждаюсь преподаванием.
Я не нашел ничего такого, что было бы столь же благотворным, как наделение людей знаниями.
Вот почему я создал 30 дней Python.'''
print(multiline_string)

# Another way of doing the same thing
multiline_string = """Я - учитель и наслаждаюсь преподаванием.
Я не нашел ничего такого, что было бы столь же благотворным, как наделение людей знаниями.
Вот почему я создал 30 дней Python."""
print(multiline_string)

# Конкатенация строк
first_name = 'Питер'
last_name = 'Паркер'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Питер Паркер
# Проверка длинны строки с помощью встроенной функции len()
print(len(first_name))  # 5
print(len(last_name))   # 6
print(len(last_name) > len(first_name)) # True
print(len(full_name)) # 12

#### Распаковка строк
language = 'Python'
a,b,c,d,e,f = language # распаковка строки в последовательность переменные
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n

# Доступ к символам в строках по индексу
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# Если мы хотим начать с конца строки, мы можем использовать отрицательный индекс. -1 обозначает индекс последнего символа, -2 индекс второго символа с конца и т.д.
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Срезы

language = 'Python'
first_three = language[0:3] # начинаем с нулевого индекса включительно и идем до 3 невключительно.
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Другой способ
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Пропуск символов в срезах
language = 'Python'
pto = language[0:6:2] # берем 0, 2 и 4 индексы
print(pto) # Pto

# Экранирование последовательностей
print('Я надеюсь, что каждый получает удовольствие от Python Challenge.\nА вы получаете?') # Перенос строки
print('Дни\tТемы\tУпражнения') # Добавление табуляции или 4-х пробелов
print('День 1\t3\t5')
print('День 2\t3\t5')
print('День 3\t3\t5')
print('День 4\t3\t5')
print('Это символ обратной косой черты (\\)') # Запись обратной косой черты
print('Изучения языков программирования принято начинать с фразы \"Hello, World!\"') # Запись двойных кавычек внутри одинарных

## Методы строк

# capitalize(): Преобразует первый символ строки в заглавную букву.

challenge = 'тридцать дней Python'
print(challenge.capitalize()) # 'Тридцать дней Python'

# count(): Возвращает количество вхождений подстроки в строку. Метод имеет следующий синтаксис: count(substring, start=..., end=...). Аргумент start принимает начальный индекс, а аргумент end принимает последний индекс, где будет вестись поиск подстроки.

challenge = 'тридцать дней python'
print(challenge.count('т')) # 2
print(challenge.count('д', 7, 14)) # 1,
print(challenge.count('th')) # 1

# endswith(): Проверяет, заканчивается ли строка указанным набором символов

challenge = 'тридцать дней python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Заменяет символ табуляции пробелами. Размер табуляции по умолчанию равен 8, а данный метод принимает аргумент и изменяет размер табуляции.

challenge = 'тридцать\tдней\tpython'
print(challenge.expandtabs())   # 'тридцать  дней      python'
print(challenge.expandtabs(10)) # 'тридцать    дней        python'

# find(): Возвращает индекс первого вхождения подстроки, если подстрока не найдена, возвращает -1.

challenge = 'традцать дней python'
print(challenge.find('y'))  # 15
print(challenge.find('th')) # 16

# rfind(): Возвращает индекс последнего вхождения подстроки, если подстрока не найдена, возвращает -1.

challenge = 'тридцать дней python вместе'
print(challenge.rfind('т'))  # 6
print(challenge.rfind('е')) # 26

# format(): форматирует строку для более красивого вывода.

first_name = 'Питер'
last_name = 'Паркер'
age = 250
job = 'учитель'
country = 'Италия'
sentence = 'Меня зовут {} {}. Мне {} лет. Я {}. Моя любимая страна {}.'.format(first_name, last_name, age, job, country)
print(sentence) # Меня зовут Питер Паркер. Мне 250 лет. Я учитель. Моя любимая страна Италия.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'Окружность круга с радиусом {} равна {}'.format(str(radius), str(area))
print(result) # Окружность круга с радиусом 10 равна 314

# index(): Возвращает наименьший индекс подстроки. В качестве дополнительных аргументов могут выступать начальный и конечный индексы. Если подстрока не найдена, возвращает ошибку valueError.

challenge = 'тридцать дней python'
sub_string = 'ца'
print(challenge.index(sub_string))  # 4
print(challenge.index(sub_string, 5)) # error

# rindex(): Возвращает наибольший индекс подстроки. В качестве дополнительных аргументов также могут выступать начальный и конечный индексы.

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error

# isalnum(): Проверяет, содержит ли строка только буквенно-цифровые символы.

challenge = 'ТридцатьДнейPython'
print(challenge.isalnum()) # True

challenge = '30ДнейPython'
print(challenge.isalnum()) # True

challenge = 'тридцать дней python'
print(challenge.isalnum()) # False, пробел не является буквенно-цифровым символом

challenge = 'тридцать дней python 2019'
print(challenge.isalnum()) # False

# isalpha(): Проверяет, состоит ли строка только из буквенных символов.

challenge = 'тридцать дней python'
print(challenge.isalpha()) # False, пробел снова не включается
challenge = 'ТридцатьДнейPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Проверяет, являются ли все символы в строке из десятичных цифр (от 0 до 9).

challenge = 'тридцать дней python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, пробел не допускается

# isdigit(): Проверяет, являются ли все символы в строке числами (от 0 до 9 и некоторми другми символами Юникода, представляющими числа).

challenge = 'Тридцать'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

# isnumeric(): Проверяет, являются ли все символы в строке числами или связаными с числами символами(аналогично isdigit(), но принимает больше символов, например, ½).

num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

# isidentifier(): Проверяет, является ли строка допустимым именем переменной.

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, потому что начинается с числа
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

# islower(): Проверяет, являются ли все буквы в строке __строчными__.

challenge = 'тридцать дней python'
print(challenge.islower()) # True
challenge = 'Тридцать дней python'
print(challenge.islower()) # False

# isupper(): Проверяет, являются ли все буквы в строке __заглавными__.

challenge = 'тридцать дней python'
print(challenge.isupper()) #  False
challenge = 'ТРИДЦАТЬ ДНЕЙ PYTHON'
print(challenge.isupper()) # True

# join(): Возвращает объединенную строку.

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Удаляет все указанные символы в начале и конце строки.

challenge = 'тридцать дней pythoonnn'
print(challenge.strip('noth')) # 'тридцать дней py'
# replace(): Заменяет подстроку на заданную строку.

challenge = 'тридцать дней python'
print(challenge.replace('python', 'удовольствия')) # 'стридцать дней удовольствия'

# split(): Разделяет строку, используя заданную строку или пробел в качестве разделителя.

challenge = 'тридцать дней python'
print(challenge.split()) # ['тридцать', 'дней', 'python']
challenge = 'тридцать, дней, python'
print(challenge.split(', ')) # ['тридцать', 'дней', 'python']

# title(): Возвращает строку с заглавными буквами в каждом слове.

challenge = 'тридцать дней python'
print(challenge.title()) # Тридцать Дней Python

# swapcase(): Преобразует все заглавные буквы в строчные и все строчные буквы в заглавные.

challenge = 'тридцать дней python'
print(challenge.swapcase())   # ТРИДЦАТЬ ДНЕЙ PYTHON
challenge = 'Тридцать Дней Python'
print(challenge.swapcase())  # тРИДЦАТЬ дНЕЙ pYTHON

# startswith(): Проверяет, начинается ли строка с указанной строки.

challenge = 'тридцать python'
print(challenge.startswith('три')) # True

challenge = '30 дней python'
print(challenge.startswith('thirty')) # False

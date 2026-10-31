<div align="center">
  <h1> 30 дней Python: День 8 - Словари</h1>
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

[<< День 7 ](../07_Day_Sets/07_sets.md) | [День 9 >>](../09_Day_Conditionals/09_conditionals.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 8](#-день-8)
  - [Словари](#словари)
    - [Создание словаря](#создание-словаря)
    - [Длина словаря](#длина-словаря)
    - [Доступ к элементам словаря](#доступ-к-элементам-словаря)
    - [Добавление элементов в словарь](#добавление-элементов-в-словарь)
    - [Изменение элементов словаря](#изменение-элементов-словаря)
    - [Проверка ключей в словаре](#проверка-ключей-в-словаре)
    - [Удаление пар ключ-значение из словаря](#удаление-пар-ключ-значение-из-словаря)
    - [Преобразование словаря в список элементов](#преобразование-словаря-в-список-элементов)
    - [Очистка словаря](#очистка-словаря)
    - [Удаление словаря](#удаление-словаря)
    - [Копирование словаря](#копирование-словаря)
    - [Получение ключей словаря в виде списка](#получение-ключей-словаря-в-виде-списка)
    - [Получение значений словаря в виде списка](#получение-значений-словаря-в-виде-списка)
  - [💻 Упражнения: День 8](#-упражнения-день-8)

# 📘 День 8

## Словари

Словарь - это коллекция неупорядоченного, модифицируемого (изменяемого) парного (ключ: значение) типа данных.

### Создание словаря

Чтобы создать словарь, мы используем фигурные скобки {} или встроенную функцию *dict()*.

```py
# синтаксис
empty_dict = {}
# Словарь со значениями данных
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
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
```

Словарь выше показывает, что значение может быть любым типом данных: строка, логическое значение, список, кортеж, множество или словарь.

### Длина словаря

Она проверяет количество пар «ключ: значение» в словаре.

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Пример:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

```

### Доступ к элементам словаря

Мы можем обращаться к элементам словаря, ссылаясь на имя его ключа.

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
```

Доступ к элементу по имени ключа вызывает ошибку, если ключ не существует. Чтобы избежать этой ошибки, сначала нужно проверить, существует ли ключ, или можно использовать метод _get_. Метод get возвращает None, который является объектом типа NoneType, если ключ не существует.
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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### Добавление элементов в словарь

Мы можем добавлять новые пары ключ-значение в словарь

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

### Изменение элементов словаря

Мы можем изменять элементы в словаре

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### Проверка ключей в словаре

Мы используем оператор _in_ для проверки существования ключа в словаре

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Удаление пар ключ-значение из словаря

- _pop(key)_: удаляет элемент с указанным именем ключа:
- _popitem()_: удаляет последний элемент
- _del_: удаляет элемент с указанным именем ключа

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # удаляет элемент key1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # удаляет последний элемент
del dct['key2'] # удаляет элемент key2
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
person.pop('first_name')        # Удаляет элемент firstname
person.popitem()                # Удаляет элемент address
del person['is_married']        # Удаляет элемент is_married
```

### Преобразование словаря в список элементов

Метод _items()_ преобразует словарь в список кортежей.

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Очистка словаря

Если мы не хотим оставлять элементы в словаре, мы можем очистить их с помощью метода _clear()_

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Удаление словаря

Если мы не используем словарь, мы можем удалить его полностью

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Копирование словаря

Мы можем скопировать словарь с помощью метода _copy()_. Используя копирование, мы можем избежать изменения исходного словаря.

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Получение ключей словаря в виде списка

Метод _keys()_ даёт нам все ключи словаря в виде списка.

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Получение значений словаря в виде списка

Метод _values_ даёт нам все значения словаря в виде списка.

```py
# синтаксис
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 Ты поразителен. Теперь ты заряжен мощью словарей. Ты только что завершил испытания восьмого дня, и ты на 8 шагов впереди на пути к величию. Теперь выполни несколько упражнений для своего мозга и мышц.

## 💻 Упражнения: День 8

1. Создай пустой словарь с именем dog
2. Добавь name, color, breed, legs, age в словарь dog
3. Создай словарь student и добавь first_name, last_name, gender, age, marital status, skills, country, city и address в качестве ключей словаря
4. Получи длину словаря student
5. Получи значение skills и проверь тип данных, это должен быть список
6. Измени значения skills, добавив один или два навыка
7. Получи ключи словаря в виде списка
8. Получи значения словаря в виде списка
9. Преобразуй словарь в список кортежей с помощью метода _items()_
10. Удали один из элементов словаря
11. Удали один из словарей

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 7 ](../07_Day_Sets/07_sets.md) | [День 9 >>](../09_Day_Conditionals/09_conditionals.md)

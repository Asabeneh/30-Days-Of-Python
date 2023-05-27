<div align="center">
  <h1> 30 Days Of Python: Day 17 - Exception Handling </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Second Edition: July, 2021</small>
  </sub>
</div>

[<< Day 16](../16_Day_Python_date_time/16_python_datetime.md) | [Day 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 17](#-day-17)
  - [Exception Handling](#exception-handling)
  - [Packing and Unpacking Arguments in Python](#packing-and-unpacking-arguments-in-python)
    - [Unpacking](#unpacking)
      - [Unpacking Lists](#unpacking-lists)
      - [Unpacking Dictionaries](#unpacking-dictionaries)
    - [Packing](#packing)
    - [Packing Lists](#packing-lists)
      - [Packing Dictionaries](#packing-dictionaries)
  - [Spreading in Python](#spreading-in-python)
  - [Enumerate](#enumerate)
  - [Zip](#zip)

# 📘 Day 17

## Exception Handling

Python ប្រើ _try_ និង _except_ ដើម្បីដោះស្រាយកំហុសដោយមានសុភាព។ ការចាកចេញពីកំហុស (errors) ដោយប្រណិត គឺជា programming វចនានុក្រម  - programs រកឃើញលក្ខខណ្ឌកំហុសធ្ងន់ធ្ងរ ហើយ "ចេញដោយសុភាព", តាមរបៀបគ្រប់គ្រងជាលទ្ធផល។ ជាញឹកញាប់ program prints សារកំហុសរៀបរាប់ទៅកាន់ terminal ឬ log ជាផ្នែកមួយនៃការចេញដោយរលូន ធ្វើឲ្យកម្មវិធីរបស់យើងកាន់តែរឹងមាំ។ មូលហេតុនៃការលើកលែងនេះជាញឹកញាប់គឺនៅខាងក្រៅ program ផ្ទាល់ខ្លួន។ ឧទាហរណ៍នៃការលើកលែងអាចជាការបញ្ចូលមិនត្រឹមត្រូវ, ឈ្មោះឯកសារមិនត្រឹមត្រូវ, មិនអាចរកឯកសារ, ឧបករណ៍ IO មិនដំណើរការបាន។ ការគ្រប់គ្រងកំហុសដោយសុភាពនឹងការពារ program របស់យើងពីការគាំង។
យើងបានពិនិត្យមើលប្រភេទ Python _error_ នៅក្នុងផ្នែកមុន។ ប្រសិនបើយើងប្រើ _try_ និង _except_ នៅក្នុង program របស់យើងនោះ វានឹងមិនលើកកំហុសនៅក្នុង blocks ទាំងនោះទេ។

![Try and Except](../images/try_except.png)

```py
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
```

**Example:**

```py
try:
    print(10 + '5')
except:
    print('Something went wrong')
```

នៅក្នុងឧទាហរណ៍ខាងលើ operand ទីពីរគឺ string។ យើងអាចផ្លាស់ប្តូរវាទៅជា float ឬ int ដើម្បីបន្ថែមវាជាមួយលេខដើម្បីធ្វើឱ្យវាដំណើរការ។ ប៉ុន្តែដោយគ្មានការប្រែប្រួលអ្វីទេ block ទី២ _except_, នឹងត្រូវដំណេីការ។

**Example:**

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
```

```sh
Something went wrong
```

នៅក្នុងឧទាហរណ៍ខាងលើនេះ exception block នឹងដំណើរការ ហើយយើងមិនដឹងច្បាស់អំពីបញ្ហាទេ។ ដើម្បីវិភាគបញ្ហានេះ យើងអាចប្រើប្រភេទ Error ផ្សេងគ្នាជាមួយ except ។

នៅក្នុងឧទាហរណ៍ខាងក្រោមនេះ វានឹងគ្រប់គ្រងកំហុសនិងក៏នឹងប្រាប់យើងអំពីប្រភេទកំហុសដែលលើកឡើង។

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
```

```sh
Enter your name:Asabeneh
Year you born:1920
Type error occured
```

នៅក្នុងកូដខាងលើ output នឹងមាន _TypeError_.
ឥឡូវនេះ, យើងត្រូវបន្ថែម block បន្ថែម:

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
```

```sh
Enter your name:Asabeneh
Year you born:1920
You are Asabeneh. And your age is 99.
I usually run with the try block
I alway run.
```

វាត្រូវបានកាត់បន្ថយ code ខាងលើដូចខាងក្រោម:
```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print('You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

```

## Packing and Unpacking Arguments in Python

យើងប្រើ operator ពីរ:

- \* for tuples
- \*\* for dictionaries

សូមយកឧទាហរណ៍ខាងក្រោមនេះ។ វាគ្រាន់តែត្រូវការ arguments គ្នាប៉ុណ្ណោះ ប៉ុន្តែយើងមាន list. យើងអាចបើក list និងផ្លាស់ប្តូ arguments.

### Unpacking

#### Unpacking Lists

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

នៅពេលដែលយើងដំណើរការ code នេះវានឹងបង្កើតនូវកំហុសមួយ ព្រោះថាលក្ខណៈនេះយកលេខ (មិនមែនជា list) ជាលក្ខខណ្ឌ។ សូមឲ្យយើងបើក / បំផ្លាញ list នេះ។

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

យើងក៏អាចប្រើ unpacking នៅក្នុង range built-in function ដែលរំពឹងទុកនូវការចាប់ផ្តើម និងការបញ្ចប់។

```py
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

```

list ឬ tuple ក៏អាចបំបែកបានដូចនេះដែរ:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### Unpacking Dictionaries

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```

### Packing

ជួនកាលយើងមិនដែលដឹងថា តើវាត្រូវបានផ្ទេរ arguments ចំនួនប៉ុន្មាន ទៅកាន់លក្ខខណ្ឌ Python នោះទេ។ យើងអាចប្រើវិធី packaging ដើម្បីអនុញ្ញាតឱ្យលក្ខខណ្ឌរបស់យើងយកលេខមិនកំណត់ ឬលេខ arbitrary នៃ arguments.

### Packing Lists

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### Packing Dictionaries

```py
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

## Spreading in Python

ដូច JavaScript ដែរ ការបម្លែងអាចធ្វើបាននៅក្នុង Python សូមយើងពិនិត្យមើលនៅក្នុងឧទាហរណ៍ខាងក្រោម:

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

ប្រសិនបើយើងចាប់អារម្មណ៍លើ index នៃ list មួយយើងប្រើ *enumerate* built-in function ដើម្បីទទួលបាន index នៃវត្ថុនីមួយៗ

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```py
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print('The country {i} has been found at index {index}')
```

```sh
The country Finland has been found at index 1.
```

## Zip

ជួនកាលយើងចង់ភ្ជាប់ list នៅពេលដែលយើង loop list ទាំងអស់នោះ។ សូមមើលឧទាហរណ៍ខាងក្រោម:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

🎉 CONGRATULATIONS ! 🎉

[<< Day 16](../16_Day_Python_date_time/16_python_datetime.md) | [Day 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)
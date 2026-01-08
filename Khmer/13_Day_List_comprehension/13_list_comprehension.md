<div align="center">
  <h1> 30 Days Of Python: Day 13 - List Comprehension</h1>
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
</div>

[<< Day 12](../12_Day_Modules/12_modules.md) | [Day 14>>](../14_Day_Higher_order_functions/14_higher_order_functions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 13](#-day-13)
  - [List Comprehension](#list-comprehension)
  - [Lambda Function](#lambda-function)
    - [Creating a Lambda Function](#creating-a-lambda-function)
    - [Lambda Function Inside Another Function](#lambda-function-inside-another-function)

# 📘 Day 13

## List Comprehension
ការយល់ដឹងពីបញ្ជីក្នុង Python គឺជាវិធីដ៏សាមញ្ញក្នុងការបង្កើតបញ្ជីមួយពីលំដាប់។ វាជាវិធីខ្លីដើម្បីបង្កើតបញ្ជីថ្មី។ ការយល់ដឹងបញ្ជីគឺលឿនជាងការប្រតិបត្តិការបញ្ជីដោយប្រើ _for_ loop ។

```py
# syntax
[i for i in iterable if expression]
```

**Example:1**

ឧទាហរណ៍ បើអ្នកចង់ផ្លាស់ប្តូរ string ទៅជាបញ្ជីអក្សរ។ អ្នក អាច ប្រើ វិធីសាស្ត្រ ពីរ បី។ សូម មើល មួយ ចំនួន ៖

```py
# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**Example:2**

ឧទាហរណ៍ ប្រសិនបើអ្នកចង់បង្កើតបញ្ជីលេខ
```py
# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**Example:2**

ការយល់ដឹងបញ្ជីអាចត្រូវបានរួមបញ្ចូលជាមួយ if expression

```py
# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Lambda Function

Lambda function គឺជា function តូចមួយដែលគ្មានឈ្មោះ។ វាអាចយកលេខអធិប្បាយជាច្រើន ប៉ុន្តែអាចមានតែពាក្យមួយប៉ុណ្ណោះ។ តួនាទី Lambda មាន លក្ខណៈ ស្រដៀង គ្នា នឹង តួនាទី អនាមិក ក្នុង JavaScript ។ យើង ត្រូវការ វា នៅពេល ដែល យើង ចង់ សរសេរ តួនាទី អនាមិក នៅ ក្នុង តួនាទី ផ្សេង។

### Creating a Lambda Function

ដើម្បីបង្កើត a lambda function យើងប្រើ _lambda_ keyword ដែលបន្ទាប់មកដោយ parameter (s) ដែលបន្ទាប់មកដោយ expression ។ សូមមើល syntax និងឧទាហរណ៍ខាងក្រោម។ តួនាទី Lambda មិនប្រើ return ទេ ប៉ុន្តែវាបានប្ដូរ expression ដោយច្បាស់លាស់។

```py
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

**Example:**

```py
# Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### Lambda Function Inside Another Function

ប្រើប្រាស់លំហាត់ lambda នៅក្នុងលំហាត់ផ្សេងទៀត។
```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```


🎉 CONGRATULATIONS ! 🎉

[<< Day 12](../12_Day_Modules/12_modules.md) | [Day 14>>](../14_Day_Higher_order_functions/14_higher_order_functions.md)

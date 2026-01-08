<div align="center">
  <h1> 30 Days Of Python: Day 11 - Functions</h1>
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

[<< Day 10](../10_Day_Loops/10_loops.md) | [Day 12 >>](../12_Day_Modules/12_modules.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 11](#-day-11)
  - [Functions](#functions)
    - [Defining a Function](#defining-a-function)
    - [Declaring and Calling a Function](#declaring-and-calling-a-function)
    - [Function without Parameters](#function-without-parameters)
    - [Function Returning a Value - Part 1](#function-returning-a-value---part-1)
    - [Function with Parameters](#function-with-parameters)
    - [Passing Arguments with Key and Value](#passing-arguments-with-key-and-value)
    - [Function Returning a Value - Part 2](#function-returning-a-value---part-2)
    - [Function with Default Parameters](#function-with-default-parameters)
    - [Arbitrary Number of Arguments](#arbitrary-number-of-arguments)
    - [Default and Arbitrary Number of Parameters in Functions](#default-and-arbitrary-number-of-parameters-in-functions)
    - [Function as a Parameter of Another Function](#function-as-a-parameter-of-another-function)

# 📘 Day 11

## Functions

(អនុគមន៍)

កន្លងមកយើងបានឃើញ អនុគមន័ដែលមានស្រាប់ជាច្រើននៅក្នុង Python ហើយនៅក្នុងចំណុចនេះ យើងនឹងផ្ដោតទៅលើអនុគមន៍ដែលយើងអាចបង្កើត និង កែប្រែបាន។ តើអ្វីទៅជាអនុគមន៍? មុននឹងយើងចាប់ផ្ដើមបង្កើតអនុគមន៍ យើងនឹងស្វែងយល់ថាអ្វីទៅជាអនុគមន៍ហើយហេតុអ្វីបានជាយើងត្រូវ
ការវា។

### Defining a Function

(ការកំណត់អនុគមន៍)

អនុគមន៍មួយអាចកាត់បន្ថយបណ្ដុំនៃកូដឬ ល្បះកូដ(programming statements) ដែលធ្វើឡើងដើម្បីធ្វើកិច្ចការដ៏ជាក់
លាក់មួយ ។ ដើម្បីអាចកំណត់ឬបង្កើតអនុគមន៍មួយ python ប្រើប្រាស់ពាក្យមួួយ _def_។ បន្តទៅនេះគឺជាកូដដែលបានកំណត់សម្រាប់ការបង្កើតអនុគមន៍មួួយ។ អនុគមន៍ត្រូវបានប្រើប្រាស់ តែនៅពេលដែលយើងហៅអនុគមន៍នោះមកប្រើតែប៉ុណ្ណោះ ដែលនៅក្នុងភាសាអង់គ្លេសគេហៅថា call ឬក៏ invoke function. 

### Declaring and Calling a Function

(ការតាង និង ហៅអនុគមន៍មកប្រេី)

នៅពេលដែលយើងបង្កើត អនុគមន៍មួយ យើងហៅវាថាជាការតាងអនុគមន៍ (បង្កើតអនុគមន៍តែមិនទាន់បានប្រើប្រាស់)។ នៅពេលដែលយើងចាប់ផ្ដើមប្រើប្រាស់អនុគមន៍នោះយើងហៅវាថា *calling* ឬ *invoking" អនុគមន៍។ អនុគមន៍អាចតាងបានដោយមិនចាំបាច់មានតម្លៃប៉ារ៉ាម៉ែត្រ។ 

*បញ្ជាក់:* មុនពេលយើងអាចប្រើប្រាស់អនុគមន៍មួយបានដូចដែលបានរៀបរាប់ខាងលើគឺយើងត្រូវ *តាង* អនុគមន៍នោះជាមុនសិន ហើយ បន្ទាប់ពី *តាង* ហើយអនុគមន៍នោះនឹងមិនត្រូវបានប្រើប្រាស់នោះទេលុះត្រាណាតែយើង ហៅវា "calling" ឬ "involking" វា។ 


```py
# syntax (លំនាំ)
# Declaring a function (ការតាងអនុគមន៍)
def function_name():
    codes
    codes
# ការហៅអនុគមន៍មកប្រើប្រាស់ 
function_name()
```

### Function without Parameters 

(អនុគមន៍ដែលគ្មានតម្លៃប៉ារ៉ាម៉ែត្រ)

អនុគមន័អាចតាងបានដោយមិនចាំបាច់មានតម្លៃប៉ារ៉ាម៉ែត្រទេ។


**ឧទាហរណ៍:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # ការហៅអនុគមន៍មកប្រើប្រាស់

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Function Returning a Value - Part 1

(អនុគមន៍ដែលផ្ដល់នៅតម្លៃមួយត្រឡប់មក)

អនុគមន៍អាចផ្ដល់នូវតម្លៃមកវិញ ប្រសិនបើអនុគមន៍គ្មានតម្លៃត្រឡប់ទេ តម្លៃនៃអនុគមន៍គឺទទេរ។ តោះយើងសរសេរឡើងវិញនូវអនុគមន៍ដោយមានតម្លៃត្រឡប់។ យើងនឹងទទួលបានតម្លៃត្រឡប់មកវិញពីអនុគមន៏នៅពេលដែលយើងហៅ (call) និង (print) វា។

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

### Function with Parameters 

(អនុគមន៍ដែលមានតម្លៃប៉ារ៉ាម៉ែត្រ)

នៅក្នុងអនុគមន៍យើងអាចដាក់បញ្ចូលនៅប្រភេទនៃទិន្ន័យ (number, string, boolean, list, triple, dictionary, ឬ set ) ជាតម្លៃប៉ារ៉ាម៉ែត្រ។

- Single Paramenter( ប៉ារ៉ាម៉ែត្រតែមួយ ): ប្រសិនបើអនុគមន៍មានតម្លៃប៉ារ៉ាម៉ែត្រមួយ យើងត្រូវតែហៅអនុគមន៍របស់យើងជាមួយនិងអាគុយម៉ង់ចំនួនមួយ។


```py
  # លំនាំ
  # ការតាងអនុគមន៍មួួយ
  def function_name(parameter):
    codes
    codes
  # ការហៅយកអនុគមន៍មកប្រើប្រាស់
  print(function_name(argument))
```

**ឧទាហរណ៍:**

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
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```
- Two Parameter (តម្លៃប៉ារ៉ាម៉ែត្រចំនួនពីរ): អនុគមន៍មួយអាច មាន ឬ មិនមានតម្លៃប៉ារ៉ាម៉ែត្រមួយ ឬ តម្លៃប៉ារ៉ាម៉ែត្រច្រើន។ ប្រសិនបើអនុគមន៍របស់យើងមានតម្លៃប៉ារ៉ាម៉ែត្រយើងគួរហៅវាជាមួយនឹងអាគុយម៉ង់។ តោះយើងក្រឡេកមើលអនុគមន៍ដែលមានអាគុយម៉ង់ចំនួនពីរ:


```py
  # លំនាំ
  # ការតាងអនុគមន៍
  def function_name(para1, para2):
    codes
    codes
  # ការហៅអនុគមន៍
  print(function_name(arg1, arg2))
```

**ឧទាហរណ៍:**

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
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # តម្លៃត្រូវផ្លាស់ប្តូរទៅជា string ជាមុនសិន
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Passing Arguments with Key and Value

(ការបញ្ចូលអាគុយម៉ង់ជាមួយ key និង value)

ប្រសិនបើយើងបញ្ចូលនូវអាគុយម៉ង់ជាមួយ key និង value លំដាប់លំដោយនៃអាគុយម៉ង់គឺមិនសំខាន់ទេ។ 


```py
# លំនាំ
# ការតាងអនុគមន៍
def function_name(para1, para2):
    codes
    codes
# ការហៅអនុគមន៍មកប្រើប្រាស់
print(function_name(para1 = 'John', para2 = 'Doe')) # លំដាប់លំដោយនៃអាគុយម៉ង់មិនសំខាន់នោះទេ គឺយើងអាចសរសេរថា print(function_name(para2= 'John', para1 = 'Doe')) ក៏បានដែរ
```

**ឧទាហរណ៍:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # ដូចដែលបានសរសេរខាងដើមគឺលំដាប់លំដោយមិនសំខាន់ឡើយ 
```

### Function Returning a Value - Part 2

(អនុគមន៍ដែលផ្ដល់តម្លៃ មួយ ត្រឡប់មកវិញ - ផ្នែក ២)
 
 កាលណាដែលយើងមិនទាញយើងតម្លៃណាមួយពី អនុគមន៍ត្រឡប់មកវិញទេ នោះអនុគមន៍របស់យើងនឹងមានតម្លៃ ទទេរ (_None_) ជាគោលការណ៍ដើម។ ដើម្បីអាចទាញយកតម្លៃណាមួយពីអនុគមន៍បានយើងត្រូវប្រើ ពាក្យគន្លឹះ (keyword) _return_ បន្ទាប់មកគឺអថេរដែលយើងទាញយកតម្លៃពីវា។ យើងអាចទាញយកតម្លៃ មិនថាវាមានទិន្ន័យប្រភេទអ្វីនោះទេ ពីអនុគមន៍។


- Returning a string (ទាយយក string):
**ឧទាហរណ៍:**

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

- Returning a number (ទាញយកតម្លៃជា number):

**ឧទាហរណ៍:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
```

- Returning a boolean (ទាញយកតម្លៃជាប៊ូលីន):
  **ឧទាហរណ៍:**

```py
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return បញ្ឍប់នូវដំណេីរការនៃអនុគមន៍បន្តទៀតដែលវាស្រដៀងទៅនឹង  break ដែរ
    return False
print(is_even(10)) # True ពិត
print(is_even(7)) # False មិនពិត
```

- Returning a list (ទាញយកតម្លៃជា list ):
  **ឧទាហរណ៍:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Function with Default Parameters

(អនុគមន៍ជាមួយនឹងតម្លៃប៉ារ៉ាម៉ែត្រដើម)

ពេលខ្លះយើងបញ្ចូលនៅតម្លៃនៃប៉ារ៉ាម៉ែត្រដើមឬគោល (មានន័យថា ប្រសិនបើនៅពេលហៅ (call or invoke) អនុគមន៍មកប្រើហើយមិនបានដាក់តម្លៃប៉ារ៉ាម៉ែត្រឱ្យវា អនុគមន៍នឹងប្រើប្រាស់តម្លៃប៉ារ៉ាម៉ែត្រដើមមកប្រើប្រាស់ ប៉ុន្តែបើមានតម្លៃប៉ារ៉ាម៉ែត្រថ្មី អនុគមន៍នឹងប្រើប្រាស់តម្លៃប៉ារ៉ាម៉ែត្រថ្មីជំនួសតម្លៃប៉ារ៉ាម៉ែត្រចាស់វិញ)។


```py
# លំនាំ
# ការតាងអនុគមន៍
def function_name(param = value):
    codes
    codes
# ការហៅអនុគមន៍មកប្រើប្រាស់
function_name()
function_name(arg)
```

**ឧទាហរណ៍:**

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
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # តម្លៃត្រូវកែប្រែទៅជា string ជាមុនសិន
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - ទំនាញមធ្យមលើផ្ទៃផែនដី
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # ទំនាញលើផ្ទៃព្រះច័ន្ទ
```

### Arbitrary Number of Arguments

(ចំនួនអាគុយម៉ង់មិនជាក់លាក់)

ប្រសិនបើយើងមិនដឹងពីចំនួននៃអាគុយម៉ង់ជាក់លាក់នៅពេលដែលយើងដាក់ក្នុងអនុគមន៍ថាមានប៉ុន្មានទេ យើងអាចបង្កើតអនុគមន៍ដោយគ្មានចំនួនជាក់លាក់ដោយបន្ថែម \* មុនឈ្មោះរបស់ ប៉ារ៉ាម៉ែត្រ។


```py
# លំនាំ
# ការតាងអនុគមន៍
def function_name(*args):
    codes
    codes
# ការហៅអនុគមន៍មកប្រើប្រាស់
function_name(param1, param2, param3,..)
```

**ឧទាហរណ៍:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     #  total +=num យើងអាចសរសេរថា   total = total+ num  ក៏បាន 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Default and Arbitrary Number of Parameters in Functions

(ប៉ារ៉ាម៉ែត្រគោល ឬ តម្លៃប៉ារ៉ាម៉ែត្រមិនជាក់លាក់នៅក្នុងអនុគមន៍)

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))
```

### Function as a Parameter of Another Function 

(អនុគមន៍ជាប៉ារ៉ាម៉ែទ្រនៃអនុគមន៍មួយផ្សេងទៀត)

```py
#You can pass functions around as parameters អ្នកអាចបញ្ចូលអនុគមន៍ជា ប៉ារ៉ាម៉ែត្រក៏បាន
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

## 💻 Exercises: Day 11

### Exercises: Level 1

1. តាងអនុគមន៍មួយដែលមានឈ្មោះថា  _add_two_numbers_ ដែលមានពីរប៉ារ៉ាម៉ែត្រ ហើយ ទាញតម្លៃវាត្រឡប់មកវិញបន្ទាប់ពីបូកតម្លៃប៉ារ៉ាម៉ែត្រទាំងពីរនោះបញ្ចូលគ្នា។  
2.  ផ្ទៃរង្វង់មានរូបបន្ត:  area = π x r x r។ ចូរសរសេរអនុគមន៍ដែលគណនា _area_of_circle_។
3. សរសេរអនុុគមន៍ដែលហៅថា add_all_nums ដោយមិនកំណត់ចំនួនជាក់លាក់នៃអាគុយម៉ង់ ហើយបូកបញ្ចូលអាគុយម៉ង់ទាំងអស់បញ្ចូលគ្នា។ ពិនិត្រមើលប្រសិនបើទិន្នន័យទាំងអស់គឺជាលេខ ប្រសិនបើមិនមែនជាលេខទេ ត្រូវផ្ដល់ចម្លើយមួយដែលសមរម្យ។ 


4. សីតុណ្ហភាពជា °C អាចបំម្លែងវាទៅជា °F ដោយប្រើរូបមន្ត: °F = (°C x 9/5) + 32។ សរសេរអនុគមន៍ដែលបំម្លែងពី °C ទៅ °F _convert_celsius_to-fahrenheit_។

5. សរសេរអនុគមន៍មួយដែលអាច ឆែក រដូវកាល។ យើងយក ខែ ជាតម្លៃប៉ារ៉ាម៉ែត្រនៃអនុគមន៍ ហើយទាញតម្លៃចេញពីអនុគមន៍វិញជារដូវកាលរួមមាន៖ សរទរដូវ រដូវរងា និទាឃរដូវ ឬរដូវក្តៅ។

6. សរសេរអនុុគមន៍ដែលហៅថា calculate_slope ដែលទាញតម្លៃជម្រាលនៃសមីការនីលេអ៊ែរចេញពីអនុគមន៍នោះវិញ។ 

7. សមីការ​ការ៉េត្រូវបានគណនាដោយប្រើរូបមន្ត: ax² + bx + c = 0. ចូរសរសេរអនុគមន៍មួយដើម្បីគណនាចម្លើយនៃសមីការការ៉េ។ solve_quadratic_eqn_។
8. តាងសមីការមួយដែលមានឈ្មោះថា print_list. វាយក list ជាតម្លៃប៉ារ៉ាម៉ែត្រ ហើយ វាបង្ហាញមកវិញនូវតម្លៃនីមួយៗដែលមាននៅក្នុង list។ 
9. តាងអនុគមន៍មួយដែលមានឈ្មោះថា reverse_list . វាប្រើប្រាស់ array ជាតម្លៃប៉ារ៉ាម៉ែត្រ ហើយវាផ្ដល់តម្លៃត្រឡប់វីញជា array បញ្ច្រាស (ប្រើប្រាស់ loop ដើម្បីដោះស្រាយលំហាត់នេះ)។


```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]
```
10. តាងអនុគមន៍មួយដែលមានឈ្មោះថា capitalize_list_items. វាប្រើប្រាស់ list ជាតម្លៃប៉ារ៉ាម៉ែត្រ ហើយផ្ដល់តម្លៃមកវិញជា អក្សរធំ នៃធាតុទាំងអស់ដែលមាននៅក្នុុង list។

11. តាងអនុគមន៍មួុយដែលមានឈ្មោះថា add_item. វាប្រើប្រាស់ list និង ធាតុ (តម្លៃ) ប៉ារ៉ាម៉ែត្រមួយ។ ហើយអនុគមន៍នោះផ្ដល់ត្រឡប់វិញនូវ list ជាមួយនឹង ធាតុចុងក្រោយដែលត្រូវបានបន្ថែមទៅក្នុង list។  


```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
```

12. តាងអនុគមន៍មួុយដែលមានឈ្មោះថា remove_item. វាប្រើប្រាស់ list និង ធាតុ (តម្លៃ) ប៉ារ៉ាម៉ែត្រមួយ។  ប្រសិនបើតម្លៃធាតុ មាននៅក្នុង list ស្រាប់ អនុគមន៍ត្រូវផ្ដល់ត្រឡប់វិញនូវ list ដែលត្រូវបានលុប ធាតុ (ធាតុដែលជាតម្លៃប៉ារ៉ាម៉ែត្រ) ចេញពីវា។


```py
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]
```
13. តាងអនុគមន៍មួយដែលមានឈ្មោះថា sum_of_numbers. វាប្រើប្រាស់ លេខជាតម្លៃប៉ារ៉ាម៉ែត្រ ហើយ ធ្វើផលបូកនៃលេខដែលស្ថិតនៅក្នុងចន្លោះនៃលេខនោះ។


```py
print(sum_of_numbers(5))  # 15 = 1+2+3+4+5

print(sum_all_numbers(10)) # 55 = 1+2+4+5+ ...+10
print(sum_all_numbers(100)) # 5050
```

14. តាងអនុគមន៍មួយដែលមានឈ្មោះថាsum_of_odds. វាប្រើប្រាស់ លេខជាតម្លៃប៉ារ៉ាម៉ែត្រ ហើយ ធ្វើផលបូកនៃលេខដែលសេសស្ថិតនៅក្នុងចន្លោះនៃលេខនោះ។

15. តាងអនុគមន៍មួយដែលមានឈ្មោះថាsum_of_odds. វាប្រើប្រាស់ លេខជាតម្លៃប៉ារ៉ាម៉ែត្រ ហើយ ធ្វើផលបូកនៃលេខដែលគូស្ថិតនៅក្នុងចន្លោះនៃលេខនោះ។


### Exercises: Level 2

1. តាងអនុគមន៍មួយដែលមានឈ្មោះថា evens_and_odds . វាយកចំនួនគត់វិជ្ជមានជាប៉ារ៉ាម៉ែត្រ ហើយវារាប់ចំនួនគូ និងសេសក្នុងចំនួននោះ។

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

2. ហៅអនុគមន៍ ហ្វាក់តូរីយ្យែល ដែលវាយកលេខទាំងមូលជាតម្លៃប៉ារ៉ាម៉ែត្រ ហើយ ផ្ដល់តម្លៃ ហ្វាក់តូរីយ្យែល នៃលេខនោះ។ 

3. ហៅអនុគមន៍   _is_empty_, ហើយវាប្រើប្រាស់តម្លៃប៉ារ៉ាម៉ែត្រហើយពិនិត្យមើលថាវាទទេរឬអត់។ 
4. សរសេរអនុគមន៍ផ្សេងៗគ្នាដែលប្រើប្រាស់ lists. វាគួរតែ calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

### Exercises: Level 3

1. សរសេរអនុគមន៍ដដែលមានឈ្មោះថា is_prime ដែលពិនិត្យមើលថាលេខនោះជា  លេខបឋម ដែរឬអត់។ 


1. សរសេរអនុគមន៍មួយដែលពិនិត្យមើលថាគ្រប់ធាតុទាំងអស់ដែលមាននៅក្នុុង list មានលក្ខណះខុសៗគ្នា។ 

1.សរសេរអនុគមន៍មួយដែលពិនិត្យមើលថាគ្រប់ធាតុទាំងអស់ដែលមាននៅក្នុុង list មានប្រភេទនៃទិន្នន័យដូចគ្នា (ឧទាហរណ៍ថា ប្រភេទនៃទិន្នន័យនៃគ្រប់ធាតុដែលនៅក្នុង list មាន data type ជា int )។  

1. សរសេរអនុគមន៍ដែលពិនិត្យមើលថា variable( អញ្ញត្តិ ) ដែលបានតាងជាអញ្ញត្តិដែលត្រឹមត្រូវក្នុងភាសា python។ 

1. ចូលក្នុង data folder ហើយស្វែងរក file ដែលមានឈ្មោះថា countries-data.py។
 - បង្កើតអនុគមន៍មួយដែលហៅថា most_spoken_languages  នៅលើពិភពលោក។ វាគួរតែផ្ដល់តម្លៃត្រឡប់វិញ 10 ឬ 20 ភាសាដែលមនុស្សលើពិភពលោកនិយាយច្រើនជាងគេតាមលំដាប់លំដោយពីធំទៅតូច។ 
 - បង្កើតអនុគមន៍មួយដែលហៅថា most_populated_countries ដែលតម្រូវឱ្យអនុគមន៍នោះផ្ដល់តម្លៃ 10 ឬ 20 ត្រឡប់មកវិញនូវប្រទេសដែលល្បីជាងគេលើពិភពលោកតាមលំដាប់
 លំដោយដោយប្រទេសដែលល្បីជាងគេនៅខាងលើ។ 


🎉 CONGRATULATIONS ! 🎉

[<< Day 10](../10_Day_Loops/10_loops.md) | [Day 12 >>](../12_Day_Modules/12_modules.md)

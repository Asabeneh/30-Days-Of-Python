<div align="center">
  <h1> 30 Days Of Python: Day 10 - Loops</h1>
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

[<< Day 9](../09_Day_Conditionals/09_conditionals.md) | [Day 11 >>](../11_Day_Functions/11_functions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 10](#-day-10)
  - [Loops](#loops)
    - [While Loop](#while-loop)
    - [Break and Continue - Part 1](#break-and-continue---part-1)
    - [For Loop](#for-loop)
    - [Break and Continue - Part 2](#break-and-continue---part-2)
    - [The Range Function](#the-range-function)
    - [Nested For Loop](#nested-for-loop)
    - [For Else](#for-else)
    - [Pass](#pass)

# 📘 Day 10

## Loops

ក្នុង programming យើងធ្វើការងារច្រើនដែលដដែលៗ។ ដើម្បីគ្រប់គ្រងការធ្វើអ្វីដដែលៗច្រើន​​ យើងប្រើ loop ។ Python programming language ក៏បានផ្តល់នូវប្រភេទ loops​​ ពីរ:

1. while loop
2. for loop

### While Loop

យើងប្រើពាក្យ _while_ ដើម្បីបង្កើត while loop។​ យើងប្រើចវាដើម្បី​ run code​​ ដដែលៗ រហូតដល់លក្ខខណ្ឌណាមួយត្រូវបានបំពេញ។ នៅពេលដែលលក្ខខណ្ឌនេះក្លាយជាមិនពិត, code ដែលនៅក្រោយ loop​​ នឹងបន្តអនុវត្ត។

```py
  # syntax
while condition:
    code goes here
```

**Example:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
```

នៅខាងលើ while loop, លក្ខខណ្ឌនេះនឹងក្លាយជាមិនពិត នៅពេលដែលចំនួនគឺ 5 នោះជាពេលដែល loop ឈប់។
បើយើងចង់​ run code នៅពេលដែលលក្ខខណ្ឌមិនត្រឹមត្រូវ​ យើងប្រើ _else_​។

```py
  # syntax
while condition:
    code goes here
else:
    code goes here
```

**Example:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

នៅខាងលើ លក្ខខណ្ឌ​ loop នឹងក្លាយជាមិនពិតនៅពេលដែលចំនួន ៥ និង loop ឈប់, និងការអនុវត្តនៃ else ចាប់ផ្តើម។​ យើងនឹងបាន 5 ជាលទ្ធផល។


### Break and Continue - Part 1

- Break: យើងប្រើ break នៅពេលដែលយើងចង់ចេញ ឬឈប់ loop។

```py
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

**Example:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

ខាងលើ​ while loop បញ្ចេញតែ 0, 1, 2, ប៉ុន្តែនៅពេលដែលវាឈានដល់ 3 វាឈប់។

- Continue: ជាមួយនឹង continue យើងអាចចាកចេញពី loop បច្ចុប្បន្ន ហើយបន្តទៅនឹងការ loop នៅខាងមុខទៀត។

```py
  # syntax
while condition:
    code goes here
    if another_condition:
        continue
```

**Example:**

```py
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
```

ខាងលើ while loop បញ្ចេញតែ 0, 1, 2 និង 4 (អត់យក 3).

### For Loop

ពាក្យគន្លឹះ​ _for_ ត្រូវបានប្រើដើម្បីបង្កើត for loop, ស្រដៀងជាមួយ programming language​ ផ្សេងៗ, ប៉ុន្តែមានភាពខុសគ្នារវាង syntax។ Loop ប្រើសម្រាប់ធ្វើម្តងៗទៅលើលំដាប់ណាមួយ (ដែលជា list, tuple, dictionary, set, ឬ string).

- For loop ជាមួយ list

```py
# syntax
for iterator in lst:
    code goes here
```

**Example:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
```

- For loop ជាមួយ string

```py
# syntax
for iterator in string:
    code goes here
```

**Example:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- For loop with tuple

```py
# syntax
for iterator in tpl:
    code goes here
```

**Example:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- For loop ជាមួយ dictionary
  Looping តាមរយៈ dictionary ផ្តល់ជូនអ្នក key នៃ dictionary។

```py
  # syntax
for iterator in dct:
    code goes here
```

**Example:**

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
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

- Loops ក្នុង set

```py
# syntax
for iterator in st:
    code goes here
```

**Example:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break and Continue - Part 2

ការរំលឹកខ្លី:
_Break_: យើងប្រើ break នៅពេលដែលយើងចង់បញ្ឈប់ loop របស់យើងមុនពេលវាត្រូវបានបញ្ចប់។

```py
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

**Example:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

នៅក្នុងឧទាហរណ៍ខាងលើ, loop ឈប់នៅពេលដែលវាឈានដល់ 3 ។

Continue: យើងប្រើ continue នៅពេលដែលយើងចង់ចាកចេញពីជំហានមួយចំនួនក្នុង iteration នៃ loop ។

```py
  # syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**Example:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```

នៅក្នុងឧទាហរណ៍ខាងលើ ប្រសិនបើចំនួននេះស្មើនឹង 3, ជំហានក្រោយពីលក្ខខណ្ឌ (ប៉ុន្តែនៅក្នុង loop) ត្រូវបានចាកចេញ ហើយការប្រតិបត្តិការនៃ loop បន្ត ប្រសិនបើមាន iterations នៅសល់។

### The Range Function

 _range()_ function ត្រូវបានប្រើសម្រាប់បញ្ជីលេខ។ _range(start, end, step)_ ចាប់យក 3 parameters: starting, ending and increment។ ជាធម្មតា វាចាប់ផ្តើមពី 0 និងការកើនឡើងគឺ 1 ។​ ការតម្រង់ range ត្រូវការយ៉ាងហោចណាស់ 1 argument (end).

បង្កើត sequence ដោយប្រើ range

```py
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```py
# syntax
for iterator in range(start, end, step):
```

**Example:**

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

### Nested For Loop

យើងអាចសរសេរ loop ក្នុង loop

```py
# syntax
for x in y:
    for t in x:
        print(t)
```

**Example:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

ប្រសិនបើយើងចង់អនុវត្តសារមួយចំនួននៅពេលដែល loop បញ្ចប់យើងប្រើ else។

```py
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**Example:**

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

### Pass

ក្នុង python នៅពេលដែលត្រូវការ statement (ក្រោយ semicolon), ប៉ុន្តែយើងមិនចូលចិត្តបំពេញ code នៅទីនោះ, យើងអាចសរសេរពាក្យ _pass_ ដើម្បីជៀសវាង error។ យើងក៏អាចប្រើវាជាទីតាំងសម្រាប់ការសរសេរ code​​ លើកក្រោយ។

**Example:**

```py
for number in range(6):
    pass
```

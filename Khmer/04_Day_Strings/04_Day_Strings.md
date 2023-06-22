<div align="center">
  <h1> 30 Days Of Python: Day 4 - Strings</h1>
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

[<< Day 3](../03_Day_Operators/03_Day_Operators.md) | [Day 5 >>](../05_Day_Lists/05_lists.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Day4](#day4)
  - [Strings](#strings)
    - [Creating a String](#creating-a-string)
    - [String Concatenation](#string-concatenation)
    - [Escape Sequences in Strings](#escape-sequences-in-strings)
- [String formatting](#string-formatting)
    - [Old style string formatting](#old-style-string-formatting)
      - [New Style String Formatting (str.format)](#new-style-string-formatting-strformat)
      - [String Interpolation / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
    - [Python Strings as Sequences of Characters](#python-strings-as-sequences-of-characters)
      - [Unpacking Characters](#unpacking-characters)
      - [Accessing Characters in Strings by Index](#accessing-characters-in-strings-by-index)
      - [Slicing Python Strings](#slicing-python-strings)
      - [Reversing a String](#reversing-a-string)
      - [Skipping Characters While Slicing](#skipping-characters-while-slicing)
    - [String Methods](#string-methods)

# Day4

## Strings
 អត្ថបទជាប្រភេទ ទិន្នន័យសំណុំអក្សរ (string) រឺអាចហៅបាន ថា ប្រភេទទិន្នន័យ string ៕ ប្រភេទទិន្នន័យណាមួយដែលសរសេរជាអក្សរគឺ ទិន្នន័យសំណុំអក្សរ(string)៕
ទិន្នន័យទាំងអស់ដែលស្ថិតក្រោមសញ្ញាធ្មេញកណ្ដុរតែមួយ, ពីរ ឬបីជា សំណុំអក្សរ រឺ ស្រ្តីង ។ នេះគឺជាវិធីសាស្រ្ត string ផ្សេងគ្នា និងមុខងារ built-in ដើម្បីដោះស្រាយប្រភេទទិន្នន័យ string ។ ដើម្បីពិនិត្យទំហំ(ប្រវែង)នៃ string ប្រើ វិធីសាស្ត្រ len() ។

### Creating a String

```py
letter = 'P'                # សំណុំអក្សរមួយអាចជាអក្សរតែមួយឬសារខ្លីជាច្រើន
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String សំណុំអក្សរ អាចធ្វើឡើងដោយប្រើពាក្យសញ្ញាធ្មេញកណ្ដុរតែមួយឬពីរ "Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
```
សំណុំអក្សរ លក្ខណៈច្រើនជួរត្រូវបានបង្កើតឡើងដោយប្រើ triple single (''') ឬ triple double quotes ("""") ។ សូម មើល ឧទាហរណ៍ ខាង ក្រោម។

```py
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# វិធីមួយទៀតដើម្បីធ្វើដូចគ្នា
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```

### String Concatenation

យើងអាចភ្ជាប់សំណុំអក្សរជាមួយគ្នា៕ការភ្ជាប់ ឬផ្កុំសំណុំអក្សរត្រូវបានគេហៅថា ការភ្ជាប់សំណុំអក្សរ។ សូមមើលឧទាហរណ៍ខាងក្រោម:

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# ការត្រួតពិនិត្យទំហំនៃ stringឬសំណុំអក្សរ ដោយប្រើ len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```

### Escape Sequences in Strings

Escape sequences ក្នុងសំណុំអក្សរ គឺជាការចម្រុះអក្សរពិសេសដែលប្រើដើម្បីតំណាងអក្សរដែលពិបាកឬមិនអាចចូលដោយផ្ទាល់ទៅក្នុង string literal ។ វាត្រូវបានបង្កើតឡើងដោយ backslash \ ដែលបន្ទាប់មកដោយអក្សរណាមួយឬលំដាប់អក្សរ។ នៅពេលដែល backslash ត្រូវបានជួបប្រទះនៅក្នុងសំណុំអក្សរ, វាបង្ហាញពីការចាប់ផ្តើមនៃEscape sequences។សូមមើលរូបភាពសសរសេបន្ទាត់ថ្មីដែលពេញនិយមបំផុត:

- \n: បន្ទាត់ថ្មី
- \t: Tab means(ដកឃ្លា ៨ ដង)
- \\\\: Back slash
- \\': សញ្ញាធ្មេញកណ្ដុរតែមួយ (')
- \\": សញ្ញាធ្មេញកណ្ដុរពីរ (")

ឥឡូវនេះយើងសូមមើលការប្រើប្រាស់នៃEscape sequences ខាងលើជាមួយឧទាហរណ៍។

```py
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # ចុះបន្ទាត់
print('Days\tTopics\tExercises') # បន្ថែមកន្លែង tab ឬ  ដកឃ្លា 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # ដើម្បីសរសេរ backslash មួយ
print('In every programming language it starts with \"Hello, World!\"') # ដើម្បីសរសេរសញ្ញាធ្មេញកណ្ដុរពីរ

# លទ្ធផល
I hope every one is enjoying the Python Challenge.
Are you ?
Days Topics Exercises
Day 1 5     5
Day 2 6     20
Day 3 5     23
Day 4 1     35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```
# String formatting

### Old style string formatting
នៅក្នុងPython មានវិធីជាច្រើនក្នុងការ Format string ។ នៅក្នុងផ្នែកនេះយើង នឹង ពិភាក្សាអំពីវិធីមួយចំនួន។ សញ្ញា "%" គឺបានប្រើជាទម្រង់សម្រាប់ កំណត់ អថេរ បិទជុំវិញដោយ "Tuple" ()

- %s - សំនុំអក្សរ (រឺ  object អ្វីមួយជាមួយសំនុំអក្សរតំណាងមួយ, ដូចជាលេខជាដេីម)
- %d - ចំនួនគត់
- %f - ចំនួនទសភាគ 
- "%.<small>number of digits</small>f" - ចំនួនទសភាគ with fixed precision

```py
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
```

#### New Style String Formatting (str.format)
ការរៀបចំទម្រង់នេះត្រូវបានបញ្ចូលនៅក្នុង Python version 3 ។

```py

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # កំណត់វាទៅជាលេខ២ខ្ទង់បន្ទាប់
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# សំណុំអក្សរ  និង លេខ
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)
```

#### String Interpolation / f-Strings (Python 3.6+)
ការកែច្នៃ string ថ្មីមួយទៀតគឺ string interpolation, f-strings ។ string ចាប់ផ្តើមដោយ f ហើយយើងអាចបញ្ចូលទិន្នន័យទៅក្នុងតំណែងដែលស្មើគ្នា។

```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```
### Python Strings as Sequences of Characters

Python strings គឺជាលំដាប់តួរអក្សរ និង ចែករំលែកវិធីសាស្រ្តមូលដ្ឋាននៃការចូលទៅជាមួយលំដាប់Python ផ្សេងទៀត នៃobject-lists and tuples។ របៀបដែលធម្មតាបំផុតសំរាប់ទាញយកតួរអក្សរមកពីstring(និងសមាជិកម្នាក់ៗ ពីលំដាប់ណាមួយ)គឺសំរាប់លុបពួកវាទៅជាអថេរ are sequences of characters, and share their basic methods of access with other Python ordered sequences of objects – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.

#### Unpacking Characters

```
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

#### Accessing Characters in Strings by Index
ក្នុងprogrammingរាប់លេខចាប់ពីលេខ០។តួអក្សរ
ទី១ ក៏រាប់ចាប់ពីតួទី០ និង ចំនួនតួចុងក្រោយនៃតួអក្សរនៃបណ្ដុំតួរអក្សរ ដក ១ គឺជាប្រវែងរបស់string.

![String index](../images/string_index.png)

```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```
ប្រសិន បើ យើង ចង់ ចាប់ផ្តើម ពី ចុង ខាងស្តាំ យើង អាច ប្រើ indexing អវិជ្ជមាន -1 ជា index ចុងក្រោយ។

```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

#### Slicing Python Strings

ក្នុង Python យើងអាចកាត់ string ទៅជា substring ។

```py
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

#### Reversing a String
យើង អាច ងាយ ស្រួល ត្រលប់ផ្លាស់ប្តូរ stringនៅ Python បាន។
```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

#### Skipping Characters While Slicing

វាអាចជួសជុលអក្សរនៅពេលកាត់ដោយផ្ទេរ step argument ទៅ Slice method ។

```py
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```

### String Methods

មានវិធីសាស្រ្ត string ជាច្រើនដែលអនុញ្ញាតឱ្យយើងបម្លែង strings ។ សូមមើលវិធីសាស្រ្ត string មួយចំនួននៅក្នុងឧទាហរណ៍ខាងក្រោម:

- capitalize(): បម្លែងអក្សរដំបូងនៃ string ទៅជា capital letter

```py
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```
- count(): បញ្ជូននូវការកើតឡើងនៃ substring ក្នុង string, count(substring, start=.., end=..). ការចាប់ផ្តើមគឺជាការចាប់ផ្ដើមបញ្ជីសម្រាប់ការរាប់ និងបញ្ចប់គឺជាបញ្ជីចុងក្រោយដើម្បីរាប់។

```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`
```

- endswith (): ត្រួតពិនិត្យថាតើ string បញ្ចប់ដោយការបញ្ចប់ដែលបានកំណត់

```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

- expandtabs(): ជំនួសតួអក្សរ tab ដោយចំណុចរហ័ស, ទំហំ tab default គឺ 8 វាយកទំហំ tab argument

```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```

- find(): បញ្ជូនទិន្នន័យនៃការកើតឡើងលើកដំបូងនៃ substring, ប្រសិនបើមិនត្រូវបានរកឃើញវិញ -1

```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 16
print(challenge.find('th')) # 17
```

- rfind(): បញ្ជូនបញ្ជីនៃការកើតឡើងចុងក្រោយនៃ substring, ប្រសិនបើមិនរកឃើញបញ្ជូន -1

```py
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 5
print(challenge.rfind('th')) # 1
```

- format(): format string ទៅជា output ល្អជាង string formatting check this [link](https://www.programiz.com/python-programming/methods/string/format)

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```

- index(): ផ្តល់នូវបញ្ជីទាបបំផុតនៃ substring, សញ្ញាបន្ថែមបង្ហាញបញ្ជីចាប់ផ្តើមនិងបញ្ចប់ (ការចម្លង 0 និងវែងខ្សែ - 1) ។ ប្រសិនបើ substring មិនត្រូវបានរកឃើញវាលើក valueError ។

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
```

- rindex(): បញ្ជូន មកវិញនូវ index ខ្ពស់បំផុតនៃ substring, សំនួរបន្ថែមបង្ហាញ start និង end index (ការចម្លង 0 និង length string - 1)

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9)) # error
```

- isalnum(): ត្រួតពិនិត្យតួរអក្សរនិងលេខ

```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```

- isalpha(): ត្រួតពិនិត្យតួរអក្សរប្រសិនបើ string គឺជាតួរអក្សរទាំងអស់(a-z and A-Z)

```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```

- isdecimal(): ត្រួតពិនិត្យតួរអក្សរប្រសិនបើ string គឺជាdecimal (0-9)

```py
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
```

- isdigit(): ត្រួតពិនិត្យតួរអក្សរទាំងអស់ក្នុងstring គឺជាលេខ(0-9 and some other unicode characters for numbers)

```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

- isnumeric():ត្រួតពិនិត្យថាតើអក្សរទាំងអស់នៅក្នុងខ្សែសង្វាក់គឺជាលេខឬលេខដែលតភ្ជាប់គ្នា (ដូច isdigit (((), គ្រាន់តែទទួលយកសញ្ញាច្រើនជាង, ដូចជា 1⁄2)))

```py
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

- isidentifier(): ត្រួតពិនិត្យសម្រាប់អត្តសញ្ញាណដែលត្រឹមត្រូវ - វាត្រួតពិនិត្យថាតើ string គឺជាvariableដែលត្រឹមត្រូវ

```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

- islower(): ត្រួតពិនិត្យតួរអក្សរក្នុងstringគឺជាlowercase

```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```

- isupper(): ត្រួតពិនិត្យតួរអក្សរក្នុងstringគឺជា uppercase

```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

- join(): បញ្ជូន string ដែលជាប់គ្នា

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
```

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

- strip(): ដកតួអក្សរទាំងអស់ដែលត្រូវបានផ្តល់ចាប់ពីដើមនិងចុងនៃ string

```py
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
```

- replace(): ជំនួស substring ដោយ string ដែលបានផ្តល់

```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```

- split(): បំបែកstring, ប្រើstring ឬកន្លែងដែលផ្តល់ជាបំបែក

```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```

- title(): កែប្រែតួអក្សរផ្ដើមនៃពាក្យជាuppercaseនិងអក្សរបន្ទាប់ជាlowercase

```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```

- swapcase(): បម្លែងអក្សរធំទាំងអស់ទៅជាអក្សរតូច និងអក្សរតូចទាំងអស់ទៅជាអក្សរធំ

```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```

- startswith(): ត្រួតពិនិត្យថា String ចាប់ផ្តើមជាមួយ String ដែលបានកំណត់

```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```

🌕 You are an extraordinary person and you have a remarkable potential. You have just completed day 4 challenges and you are four steps a head in to your way to greatness. Now do some exercises for your brain and muscles.


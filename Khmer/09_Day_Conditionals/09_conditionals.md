<div align="center">
  <h1> 30 Days Of Python: Day 9 - Conditionals</h1>
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

[<< Day 8](../08_Day_Dictionaries/08_dictionaries.md) | [Day 10 >>](../10_Day_Loops/10_loops.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 9](#-day-9)
  - [Conditionals](#conditionals)
    - [If Condition](#if-condition)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Short Hand](#short-hand)
    - [Nested Conditions](#nested-conditions)
    - [If Condition and Logical Operators](#if-condition-and-logical-operators)
    - [If and Or Logical Operators](#if-and-or-logical-operators)

# 📘 Day 9

## Conditionals

ដោយលំនាំដើម, ការបញ្ជានៅក្នុង Python script ត្រូវបានបំពេញដោយលំដាប់ពីលើទៅក្រោម។ ប្រសិនបើការប្រតិបត្ដិការ logical តម្រូវឱ្យដូច្នេះ, ការលំហូរ sequential នៃការអនុវត្តអាចត្រូវបានផ្លាស់ប្តូរក្នុងពីរវិធី:

- Conditional execution: block នៃពាក្យមួយឬច្រើនទៀតនឹងត្រូវបានអនុវត្តប្រសិនបើពាក្យមួយគឺពិត
- Repetitive execution: block នៃពាក្យមួយឬច្រើនទៀតនឹងត្រូវបានបំពេញឡើងជាបន្តបន្ទាប់ដរាបណាពាក្យមួយគឺពិត។ នៅក្នុងផ្នែកនេះយើងនឹងគ្របដណ្តប់ _if_, _else_, _elif_ statements. ការប្រៀបធៀប និងប្រតិបត្តិការយោធាដែលយើងបានរៀននៅក្នុងផ្នែកមុននឹងមានប្រយោជន៍នៅទីនេះ។

### If Condition

នៅក្នុង Python និងភាសា programming ផ្សេងទៀតពាក្យគន្លឹះ _if_ ត្រូវបានប្រើដើម្បីពិនិត្យមើលថាតើលក្ខខណ្ឌណាមួយគឺជាការពិត និងដើម្បីបំពេញលេខកូដ block ។ ចងចាំការបង្កប់ក្រោយ colon ។

```py
# syntax
if condition:
    this part of code runs for truthy conditions
```

**Example: 1**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

ដូចដែលអ្នកអាចឃើញនៅក្នុងឧទាហរណ៍ខាងលើ 3 គឺធំជាង 0។ លក្ខខណ្ឌនេះគឺជាការពិត ហើយ code ត្រូវបានអនុវត្ត។ ទោះបីជាយ៉ាងណាក៏ដោយ ប្រសិនបើលក្ខខណ្ឌគឺមិនពិត យើងមិនឃើញលទ្ធផលទេ។ ដើម្បីមើលលទ្ធផលនៃ false condition យើងត្រូវមាន block មួយទៀតគឺ _else_.

### If Else

ប្រសិនបើលក្ខខណ្ឌគឺជាការពិត block ដំបូងនឹងត្រូវបានអនុវត្ត បើមិនដូច្នេះលក្ខខណ្ឌ else នឹងអនុវត្ត។

```py
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**Example: **

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

លក្ខខណ្ឌខាងលើនេះត្រូវបានបង្ហាញថាមិនពិត ដូច្នេះ block else ត្រូវបានអនុវត្ត។ បើសិនជាលក្ខខណ្ឌរបស់យើងមានច្រើនជាងពីរ? យើងអាចប្រើ _ elif_.

### If Elif Else

នៅក្នុងជីវិតប្រចាំថ្ងៃយើងតែងតែសម្រេចចិត្តជារៀងរាល់ថ្ងៃ។ យើងសម្រេចចិត្តមិនមែនតាមរយៈការពិនិត្យលក្ខខណ្ឌមួយឬពីរទេប៉ុន្តែ លក្ខខណ្ឌជាច្រើន។ ដូចជីវិតដែរ កម្មវិធី ក៏ពោរពេញទៅដោយលក្ខខណ្ឌ។ យើងប្រើ _elif_ នៅពេលដែលយើងមានលក្ខខណ្ឌជាច្រើន។

```py
# syntax
if condition:
    code
elif condition:
    code
else:
    code

```

**Example: **

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### Short Hand

```py
# syntax
code if condition else code
```

**Example: **

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
```

### Nested Conditions

Conditions can be nested

```py
# syntax
if condition:
    code
    if condition:
    code
```

**Example: **

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

យើងអាចចៀសវាងការសរសេរលក្ខខណ្ឌ nested (រញ៉េរញ៉ៃ) ដោយប្រើ logical operator _and_.

### If Condition and Logical Operators

```py
# syntax
if condition and condition:
    code
```

**Example: **

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

### If and Or Logical Operators

```py
# syntax
if condition or condition:
    code
```

**Example: **

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

[<< Day 8](../08_Day_Dictionaries/08_dictionaries.md) | [Day 10 >>](../10_Day_Loops/10_loops.md)

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

- [Day 4](#day-4)
  - [សំណុំអក្សរ](#strings)
    - [ការបង្កេីតសំណុំអក្សរមួយ](#creating-a-string)
    - [ការផ្កុំសំណុំអក្សរ](#string-concatenation)
    - [ការដកឃ្លា រឺ ចុះបន្ទាត់ក្នុងសំណុំអក្សរ](#escape-sequences-in-strings)
    - [ការរៀបចំទ្រង់ទ្រាយសំណុំអក្សរ](#string-formatting)
      - [ការរៀបចំទ្រង់ទ្រាយសំណុំអក្សរតាមរបៀបចាស់(% Operator)](#old-style-string-formatting--operator)
      - [ការរៀបចំទ្រង់ទ្រាយសំណុំអក្សរតាមរបៀបថ្មី (str.format)](#new-style-string-formatting-strformat)
      - [ការដាក់បញ្ចូលសំណុំអក្សរ / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
    - [Python សំណុំអក្សរជាលំដាប់នៃតួអក្សរ](#python-strings-as-sequences-of-characters)
      - [ការពង្រាយតួអក្សរ](#unpacking-characters)
      - [ការចូលដំណើរការ តួអក្សរ ក្នុង សំណុំអក្សរ ដោយ កម្រិតនៃតួអក្សរ](#accessing-characters-in-strings-by-index)
      - [ការកាត់សំណុំអក្សរក្នុងPython](#slicing-python-strings)
      - [ការត្រលប់សំណុំអក្សរ](#reversing-a-string)
      - [ការរំលងតួរអក្សរ កំឡុងពេលកាត់](#skipping-characters-while-slicing)
    - [វិធីសាស្ត្រ ប្រេីប្រាស់សំណុំអក្សរ](#string-methods)
  - [💻 លំហាត់ - Day 4](#-exercises---day-4)

# Day4

## សំណុំអក្សរ រឺ ស្រ្តីង
 អត្ថបទជាប្រភេទ ទិន្នន័យសំណុំអក្សរ (string) រឺអាចហៅបាន ថា ប្រភេទទិន្នន័យ string ៕ ប្រភេទទិន្នន័យណាមួយដែលសរសេរជាអក្សរគឺ ទិន្នន័យសំណុំអក្សរ(string)៕
ទិន្នន័យទាំងអស់ដែលស្ថិតក្រោមសញ្ញាធ្មេញកណ្ដុរតែមួយ, ពីរ ឬបីជា សំណុំអក្សរ រឺ ស្រ្តីង ។ នេះគឺជាវិធីសាស្រ្ត string ផ្សេងគ្នា និងមុខងារ built-in ដើម្បីដោះស្រាយប្រភេទទិន្នន័យ string ។ ដើម្បីពិនិត្យទំហំ(ប្រវែង)នៃ string ប្រើ វិធីសាស្ត្រ len() ។

### ការបង្កេីតសំណុំអក្សរមួយ

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

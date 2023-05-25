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
- [Day 4](#day-4)
  - [Strings](#strings)
    - [Creating a String](#creating-a-string)
    - [String Concatenation](#string-concatenation)
    - [Escape Sequences in Strings](#escape-sequences-in-strings)
    - [String formatting](#string-formatting)
      - [Old Style String Formatting (% Operator)](#old-style-string-formatting--operator)
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

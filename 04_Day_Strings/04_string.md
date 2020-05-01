
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
  <small> First Edition: Nov 22 - Dec 22, 2019</small>
  </sub>
</div>
</div>

[<< Day 3](../03_Day_Operators/03_operators.md) | [Day 5 >>](../05_Day_Lists/05_list.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [Day 4](#day-4)
  - [String](#string)
    - [Creating a string](#creating-a-string)
    - [String Concatenation](#string-concatenation)
    - [Escape Sequences in string](#escape-sequences-in-string)
    - [String formating](#string-formating)
      - [Old Style String Formatting (% Operator)](#old-style-string-formatting--operator)
      - [New Style String Formatting (str.format)](#new-style-string-formatting-strformat)
      - [String Interpolation / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
    - [Python strings as sequences of characters](#python-strings-as-sequences-of-characters)
      - [Unpacking characters](#unpacking-characters)
      - [Accessing characters in strings by index](#accessing-characters-in-strings-by-index)
      - [Slicing Python Strings](#slicing-python-strings)
      - [Reversing a string](#reversing-a-string)
      - [Skipping characters while slicing](#skipping-characters-while-slicing)
    - [String Methods](#string-methods)
  - [💻 Exercises - Day 4](#%f0%9f%92%bb-exercises---day-4)
# Day 4

## String

Text is a string data type. Any data type written as text is a string. Any data under single or double quote are strings. There are different string methods and built-in functions to deal with string data types. To check the length of a string use the len() method.

### Creating a string

```py
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)
```

Multiline string is created by using triple ''' or  quotes.See the example below.

```py
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```

### String Concatenation

We can connect to strings together. Merging or connecting to strings together is called concatenation.See the example below

  ```py
  first_name = 'Asabeneh'
  last_name = 'Yetayeh'
  space = ' '
  full_name = first_name  +  space + last_name
  print(full_name) # Asabeneh Yetayeh
  # Checking length of a string using len() builtin function
  print(len(first_name))  # 8
  print(len(last_name))   # 7
  print(len(first_name) > len(last_name)) # True
  print(len(full_name)) # 15
  ```

### Escape Sequences in string

In python and other programming language \ followed by a character. Let's see the most common escape characters:

* \n: new line
* \t: Tab means(8 spaces)
* \\\\: Back slash
* \\': Single quote (')
* \\":Double quote (")

```py
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"') 

# output
I hope every one enjoying the python challenge.
Do you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a back slash  symbol (\)
In every programming language it starts with "Hello, World!"
```

### String formating

#### Old Style String Formatting (% Operator)

In python there many ways of formating string. In this section we will cover some of them.
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s",  "%d", "%f", "%.<number of digits>f". 

* %s - String (or any object with a string representation, like numbers)
* %d - Integers
* %f - Floating point numbers
* %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

```py
# Strings only
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formatted_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formatted_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formatted_string = 'The following are python libraries:' % python_libraries
print(formatted_string) # "The following are python libraries:['Django', 'Flask', 'Numpy', 'Pandas']"
```
#### New Style String Formatting (str.format)
This is formating is introduced in python version 3. 

```py

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formatted_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formatted_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
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

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formatted_string)

```
####  String Interpolation / f-Strings (Python 3.6+)
Another new string formatting is string interpolation, f-strings. String started with f and we can inject the data in their corresponding positions.
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

### Python strings as sequences of characters
Python strings are sequences of  characters, and share their basic methods of access with those other Python sequences – lists and tuples. The simplest way of extracting single characters from strings (and individual members from any sequence) is to unpack them into corresponding variables.
#### Unpacking characters 
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
#### Accessing characters in strings by index
  In programming counting starts from zero. Therefore the first letter of a string is at zero index and the last letter of a string is the length of a string minus one.

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
If we want to start from right end we can use negative indexing. -1 is the last index.
```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
  ```

#### Slicing Python Strings

In python we can slice substrings from a string.

```py
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

#### Reversing a string

We can easily reverse string in python.

```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

#### Skipping characters while slicing
It is possible to skip characters while slicing by passing step argument to slice method.
```py
language = 'Python'
pto = language[0,6:2] # 
print(pto) # Pto
```

### String Methods
There are many string methods which allow us to format strings. See some of the string methods in the following example:

* capitalize(): Converts the first character the string to Capital Letter
```py
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```
* count(): returns occurrences of substring in string, count(substring, start=.., end=..)
```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`
```
* endswith(): Checks if a string ends with a specified ending
```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```
* expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```
* find(): Returns the index of first occurrence of substring
```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```
* format()	formats string into nicer output    
    More about string formating check this [link](https://www.programiz.com/python-programming/methods/string/format)
```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0
```
* index(): Returns the index of substring
```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```
* isalnum(): Checks alphanumeric character
```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```
* isalpha(): Checks if all characters are alphabets
```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```
* isdecimal(): Checks Decimal Characters
```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```
* isdigit(): Checks Digit Characters
```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.digit())   # True
```
* isdecimal():Checks decimal characters
```py
num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False
```

* isidentifier():Checks for valid identifier means it check if a string is a valid variable name
```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

* islower():Checks if all alphabets in a string are lowercase
```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```
* isupper(): returns if all characters are uppercase characters
```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

* isnumeric():Checks numeric characters
```py
num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False
```
* join(): Returns a concatenated string
```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```
* strip(): Removes both leading and trailing characters
```py
challenge = ' thirty days of python '
print(challenge.strip('y')) # 5
```
* replace(): Replaces substring inside
```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```
* split():Splits String from Left
```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
```
* title(): Returns a Title Cased String
```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```
* swapcase(): Checks if String Starts with the Specified String
  The string swapcase() method converts all uppercase characters to lowercase and all lowercase characters to uppercase characters of the given string, and returns it.
```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```
* startswith(): Checks if String Starts with the Specified String
```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```

## 💻 Exercises - Day 4
1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
3. Declare a variable name company and assign it to an initial value "Coding For All.
4. Print company using *print()*
5. Print the length of the company string using *len()* method and *print()*
6. Change all the characters to capital letters using *upper()* method
7. Change all the characters to lowercase letters using *lower()* method
8. Use capitalize(), title(), swapcase() methods to format the value the string *Coding For All*.
9.  Cut(slice) out the first word of *Coding For All* string
10. Check if *Coding For All* string contains a word Coding using the method index, find or other methods.
11. Replace the word coding in the string 'Coding For All' to Python.
12. Change Python for Everyone to Python for All using the replace method or other methods
13. Split the string 'Coding For All' at the space using split() method
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
15. What is character at index 0 in the string *Coding For All*.
16. What is the last index of the string *Coding For All*
17. What character is at index 10 in "Coding For All" string.
18. Create an acronym or an abbreviation for the name 'Python For Everyone'
19. Create an acronym or an abbreviation for the name 'Coding For All'
20. Use index to determine the position of the first occurrence of C in Coding For All.
21. Use index to determine the position of the first occurrence of F in Coding For All
22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
23. Use index or find to find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
24. Use rindex to find the position of the last occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
25. Slice out the phrase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
26. Find the position of the first occurrence of the word because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
27. Slice out the phase because because because in the following sentence:'You cannot end a sentence with because because because is a conjunction'
28. Does Coding For All starts with a substring *Coding*?
29. Does Coding For All ends with a substring *coding*?
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;,    remove the left and right trailing spaces in the given string.
31. Which one of the following variable return True when we use the method isidentifier()
    * 30DaysOfPython
    * thirty_days_of_python
32. The following are some of python libraries list: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string. 
33. Use new line escape sequence to writ the following sentence.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. Use a tab escape sequence to writ the following sentence.
    ```py
    Name      Age     Country
    Asabeneh  250     Finland
    ```
35. Use string formatting method to display the following:
```sh
radius = 10
area = 3.14 * radius ** 2
The area of radius 10 is 314 meters squares. 
```
36. Make the following using string formatting methods:
```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```

🎉 CONGRATULATIONS ! 🎉

[<< Day 3](../03_Day_Operators/03_operators.md) | [Day 5 >>](../05_Day_Lists/05_list.md)
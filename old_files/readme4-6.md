![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

🧳 [Part 1: Day 1 - 3](https://github.com/Asabeneh/30-Days-Of-Python)  
🧳 [Part 2: Day 4 - 6](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)  
🧳 [Part 3: Day 7 - 9](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)  
🧳 [Part 4: Day 10 - 12](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)  
🧳 [Part 5: Day 13 - 15](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)  
🧳 [Part 6: Day 16 - 18](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)  
🧳 [Part 7: Day 19 - 21](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)  
🧳 [Part 8: Day 22 - 24](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme22-24.md)  
🧳 [Part 9: Day 25 - 27](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme25-27.md)  
🧳 [Part 10: Day 28 - 30](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme28-30.md) 

---
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
- [Day 5](#day-5)
  - [Lists](#lists)
    - [How to create a list](#how-to-create-a-list)
    - [Accessing list items using positive indexing](#accessing-list-items-using-positive-indexing)
    - [Accessing list items using negative indexing](#accessing-list-items-using-negative-indexing)
    - [Unpacking list items](#unpacking-list-items)
    - [Slicing  items from list](#slicing-items-from-list)
    - [Modifying list](#modifying-list)
    - [Check items in a list](#check-items-in-a-list)
    - [Adding item in a list](#adding-item-in-a-list)
    - [Inserting item in to a list](#inserting-item-in-to-a-list)
    - [Removing item from list](#removing-item-from-list)
    - [Removing item using pop](#removing-item-using-pop)
    - [Removing item using del](#removing-item-using-del)
    - [Clearing list items](#clearing-list-items)
    - [Copying  a list](#copying-a-list)
    - [Joining lists](#joining-lists)
    - [Counting Items in a list](#counting-items-in-a-list)
    - [Finding index of an item](#finding-index-of-an-item)
    - [Reversing a list](#reversing-a-list)
    - [Sorting list items](#sorting-list-items)
  - [💻 Exercises: Day 5](#%f0%9f%92%bb-exercises-day-5)
- [Day 6:](#day-6)
  - [Tuple](#tuple)
    - [Creating Tuple](#creating-tuple)
    - [Tuple length](#tuple-length)
    - [Accessing tuple items](#accessing-tuple-items)
    - [Slicing tuples](#slicing-tuples)
    - [Changing tuples to list](#changing-tuples-to-list)
    - [Checking an item in a list](#checking-an-item-in-a-list)
    - [Joining tuples](#joining-tuples)
    - [Deleting tuple](#deleting-tuple)
  - [💻 Exercises: Day 6](#%f0%9f%92%bb-exercises-day-6)

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

  ![String index](./images/string_index.png)
  
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
# Day 5
## Lists
The are four collection data types in python :
* List:  is a collection which is ordered and changeable(modifiable). Allows duplicate members.
* Tuple:  is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
* Set:  is a collection which is unordered and unindexed. No duplicate members.
* Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.

A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items or items
### How to create a list
In python we can create list in two ways:
* Using list builtin function
```py
# syntax
lst = list()
```
```py
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```
* Using square brackets, []
```py
# syntax
lst = []
```
```py
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

List with initial values. We use *len()* to find the length of a list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```
```sh
output
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```
* List can have items of different data types
```py
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types
```
### Accessing list items using positive indexing
We access each item in a list using their index. A list index start from 0. The picture below show clearly where the index starts
![List index](./images/list_index.png)
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```
### Accessing list items using negative indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.

![List negative indexing](./images/list_negative_indexing.png)
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```
### Unpacking list items
```py
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item1
print(third_item)     # item2
print(rest)           # ['item4', 'item5']

```
```py
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```
### Slicing  items from list
* Positive Indexing: We can specify a range of positive indexes by specifying the starting  and the ending, the return value will be a new list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # it returns all the fruits
# this is also give the same result as the above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the end index
orange_mango_lemon = fruits[1:]
```
* Negative Indexing:  We can specify a range of negative indexes by specifying the starting  and the ending, the return value will be a new list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1] # it does not include the end index
orange_mango_lemon = fruits[-3:]
```
### Modifying list
List is a mutable or modifiable ordered collection of items or items. Lets modify the fruit list.
```py
fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits)
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```
### Check items in a list
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```
### Adding item in a list
To add item to the end of an existing list we use the method
```py
# syntax
lst = list()
lst.append(item)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```
### Inserting item in to a list
Use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right.
```py
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon']
print(fruits)
```
### Removing item from list
The remove method remove a specified item from a list
```py
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']
```
### Removing item using pop
The pop() method removes the specified index, (or the last item if index is not specified):
```py
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.remove(0)     
print(fruits)       # ['orange', 'mango']    
```
### Removing item using del
The del keyword removes the specified index and it can be also use to delete the list completely

```py
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```
### Clearing list items
The clear() method empties the list:
```py
# syntax
lst = ['item1', 'item2']
lst.clear()
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []   
```
### Copying  a list
It is possible to copy a list by reassigning to a new variable in the  following way list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list2. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. One of way avoid the above problem is using *copy()*.
```py
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```
```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```
### Joining lists
There are several ways to join, or concatenate, two or more lists in Python. 

* Plus Operator (+)
```py
# syntax
list3 = list1 +list2
```
```py
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

```
```py
# output
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```
  * Joining using extend() method

```py
# syntax
lst1 = ['item1', 'item2']
lst2 = ['item3', 'item4','item5']
list1.extend(list2)
```
```py
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

```
```py
Numbers: [0, 1, 2, 3, 4, 5, 6]
Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### Counting Items in a list
The count() method returns the number of times an item appears in a list:
  ```py
  # syntax
  lst = ['item1', 'item2']
  lst.count(item) 
  ```
  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(fruits.count('orange'))   # 1
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  print(ages.count(24))           # 3
  ```
### Finding index of an item
The count() method returns the index of an item in the list:
  ```py
  # syntax
  lst = ['item1', 'item2']
  lst.index(item) 
  ```
  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(fruits.index('orange'))   # 1
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  print(ages.index(24))           # 2, the first occurrence
  ```
### Reversing a list
The reverse() method reverse the order of a list.
  ```py
  # syntax
  lst = ['item1', 'item2']
  lst.reverse() 

  ```
  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.reverse()
  print(fruits.reverse())  
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.reverse()
  print(ages.reverse())         
  ```
  ```py
  ['lemon', 'mango', 'orange', 'banana']
  [24, 25, 24, 26, 25, 24, 19, 22]
  ```
### Sorting list items
To sort list we can use *sort() method or *sorted()* builtin function. The sort() method reorder the list items in ascending order and modify the original list. If a reverse is equal to true it arrange in descending order.
* sort():
  ```py
  # syntax
  lst = ['item1', 'item2']
  lst.sort()                # ascending
  lst.sort(reverse=True)    # descending
  ```
  **Example:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.sort()
  print(fruits) 
  fruits.sort(reverse=True)
  print(fruits)
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.sort()
  print(ages) 
  ages.sort(reverse=True)
  print(ages)           
  ```
  ```sh
  ['banana', 'lemon', 'mango', 'orange']
  ['orange', 'mango', 'lemon', 'banana']
  [19, 22, 24, 24, 24, 25, 25, 26]
  [26, 25, 25, 24, 24, 24, 22, 19]
  ```
  sorted(): returns the ordered list without modifying the original
  **Example:**
   ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits)
  print(fruits)     # ['banana', 'lemon', 'mango', 'orange']
  # Reverse order
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']          
  ```
  
## 💻 Exercises: Day 5
1. Declare an empty list
2. Declare a list with more than 5 number of items
3. Find the length of your list
4. Get the first item, the middle item and the last item of the list
5. Declare a list called mixed_data_types,put your(name, age, height, marital status, address)
6. Declare a list variable name it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
7. Print the list using *print()*
8. Print the number of companies in the list
9. Print the first, middle and last company
10. Print modify any of the companies
11. Add an IT company to it_companies
12. Insert an IT company in the middle of the companies list
13. Change one of the it_companies item to uppercase
14. Join the it_companies with a string '#;&nbsp; '
15. Check if a certain company exists in the it_companies list. 
16. Sort the list using sort() method
17. Reverse the list in descending order using reverse() method
18. Slice out the first 3 companies from the list
19. Slice out the last 3 companies from the list
20. Slice out the middle IT company or companies from the list
21. Remove the first IT company from the list
22. Remove the middle IT company or companies from the list
23. Remove the last IT company from the list
24. Remove all IT companies item
25. Destroy the IT companies list
26. Join the following lists:
    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```
27. After joining the lists in question 26. Copy the joined list and assigned it to a variable full_stack. Then insert, Python and SQL after Redux.
28. The following is a list of 10 students ages:
```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```
  * Sort the list and find the min and max age
  * Add the min age and the max age
  * Find the median age(one middle item or two middle items divided by two)
  * Find the average age(all items divided by number of items)
  * Find the range of the ages(max minus min)
  * Compare the value of (min - average) and (max - average), use *abs()* method
29. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
30. Divide the countries list into two equal lists if it is even if not one more country for the first half.
31. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

# Day 6:
## Tuple
A tuple is a collection of different data types which is ordered and unchangeable(immutable). Tuples are written with round brackets,(). Once a tuple is created, we can not change its values. We can not add, insert, remove a tuple because it is not modifiable (mutable). Unlike list, tuple has few methods. Methods related to tuple:
* tuple(): to create an empty tuple
* count(): to count the number of a specified item in a tuple
* index(): to find the index of a specified item in a tuple
* + operator: to join two or more tuples and to create new tuple
### Creating Tuple

* Empty tuple: Creating an empty tuple
  ```py
  # syntax
  empty_tuple = () 
  # or using the tuple constructor
  empty_tuple = tuple()
  ```
* Tuple with initial values
  ```py
  # syntax
  tpl = ('item1', 'item2','item3')
  ```
  * 
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  ```
### Tuple length
We use the *len()* method to get the length of a tuple.
  ```py
  # syntax
  tpl = ('item1', 'item2', 'item3')
  len(tpl)
  ```
### Accessing tuple items
* Positive Indexing
Similar to the list data type we use positive or negative indexing to access tuple items.
![Accessing tuple items](images/tuples_index.png)

  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3')
  first_item = tpl[0]
  second_item = tpl[1]
  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[0]
  second_fruit = fruits[1]
  last_index =len(fruits) - 1
  last_fruit = fruits[las_index]
  ```
* Negative indexing
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last and the negative of the list length refers to the first item.
![Tuple Negative indexing](images/tuple_negative_indexing.png)
  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  first_item = tpl[-4]
  second_item = tpl[-3]
  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[-4]
  second_fruit = fruits[-3]
  last_fruit = fruits[-1]
  ```
### Slicing tuples
We can slice out a sub tuple by  specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.

* Range of Positive Indexes

  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # all items
  all_items = tpl[0:]         # all items
  middle_two_items = tpl[1:3]  # does not include item at index 3
  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # all items
  all_fruits= fruits[0:]      # all items
  orange_mango = fruits[1:3]  # doesn't include item at index 3
  orange_to_the_rest = fruits[1:]
  ```

* Range of Negative Indexes

  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # all items
  middle_two_items = tpl[-3:-1]  # does not include item at index 3
  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # all items
  orange_mango = fruits[-3:-1]  # doesn't include item at index 3
  orange_to_the_rest = fruits[-3:]
  ```
### Changing tuples to list
We can change tuples to list and list to tuple. Tuple is immutable if we want to modify a tuple we should change to a list.
  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  lst = list(tpl)
  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  fruits = list(fruits)
  fruits[0] = 'apple'
  print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
  fruits = tuple(fruits)
  print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
  ```
### Checking an item in a list
We can check an item if it exists in a list or not using *in*, it returns boolean.
  ```py
  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  'item2' in tpl # True
  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  'orange' in fruits # True
  'apple' in fruits # False
  fruits[0] = 'apple'
  ```
### Joining tuples
We can join two or more tuples using + operator
  ```py
  # syntax
  tpl1 = ('item1', 'item2', 'item3')
  tpl2 = ('item4', 'item5','item6')
  tpl3 = tpl1 + tpl2
  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')                    
  vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
  fruits_and_vegetables = fruits + vegetables 
  ```
### Deleting tuple
It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using *del*.
  ```py
  # syntax
  tpl1 = ('item1', 'item2', 'item3')
  del tpl1

  ```
  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon') 
  del fruits                  
  ```


## 💻 Exercises: Day 6
1. Create an empty tuple
2. Create a tuple containing name of your sisters and your brothers
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have ?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
6. Unpack siblings and parents from family_members
7. Create a fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff. 
8. Slice out the middle item or items from the food_staff list
9. Slice out the first three items and the last three items from food_staff list
10. Delete the food_staff list completely
11. Check if an item exist in a tuple:
* Check if 'Estonia' is a nordic country
* Check if 'Iceland' is a nordic country
  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```

[<< Part 1](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme.md) | [Part 3>>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)
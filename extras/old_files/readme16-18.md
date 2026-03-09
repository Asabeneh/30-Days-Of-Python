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

- [📘 Day 16](#%f0%9f%93%98-day-16)
  - [Python Datetime](#python-datetime)
    - [Getting the datetime information](#getting-the-datetime-information)
    - [Formating datetime output using strftime](#formating-datetime-output-using-strftime)
    - [String to time using strptime](#string-to-time-using-strptime)
    - [Use date from datetime](#use-date-from-datetime)
    - [Time object to represent time](#time-object-to-represent-time)
    - [Difference between two datetime](#difference-between-two-datetime)
    - [Difference between two dates and times using timedelata](#difference-between-two-dates-and-times-using-timedelata)
  - [💻 Exercises: Day 16](#%f0%9f%92%bb-exercises-day-16)
- [📘 Day 17](#%f0%9f%93%98-day-17)
  - [Exception Handling](#exception-handling)
  - [Packing and Unpacking Arguments in Python](#packing-and-unpacking-arguments-in-python)
    - [Unpacking](#unpacking)
      - [Unpacking list](#unpacking-list)
      - [Unpacking dictionary](#unpacking-dictionary)
    - [Packing](#packing)
    - [Packing list](#packing-list)
      - [Packing dictionary](#packing-dictionary)
  - [Spreading in Python](#spreading-in-python)
  - [Enumerate](#enumerate)
  - [Zip](#zip)
  - [Exercises: Day 17](#exercises-day-17)
- [📘 Day 18](#%f0%9f%93%98-day-18)
  - [Regular Expression](#regular-expression)
    - [Import re module](#import-re-module)
    - [re functions](#re-functions)
      - [Match](#match)
      - [Search](#search)
      - [Searching all matches using findall](#searching-all-matches-using-findall)
      - [Replacing a substring](#replacing-a-substring)
  - [Spliting text using RegEx split](#spliting-text-using-regex-split)
  - [Writing RegEx pattern](#writing-regex-pattern)
    - [Square Bracket](#square-bracket)
    - [Escape character(\) in RegEx](#escape-character-in-regex)
    - [One or more times(+)](#one-or-more-times)
    - [Period(.)](#period)
    - [Zero or more times(*)](#zero-or-more-times)
    - [Zero or one times(?)](#zero-or-one-times)
    - [Quantifier in RegEx](#quantifier-in-regex)
    - [Cart ^](#cart)
  - [💻 Exercises: Day 18](#%f0%9f%92%bb-exercises-day-18)
GIVE FEEDBACK: http://thirtydayofpython-api.herokuapp.com/feedback
# 📘 Day 16

## Python Datetime

Python has _datetime_ module to handle date and time.

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

Using the dir or help builtin function it is possible to know the available functions in a certain module. As you can see in the datetime there are many functions but we will focus on _date_, _datetime_, _time_ and _timedelta_. Let see them step by step.

### Getting the datetime information

```py
from datetime import datetime
now = datetime.now()
print(now)                      # 2019-12-04 23:34:46.549883
day = now.day                   # 4
month = now.month               # 12
year = now.year                 # 2019
hour = now.hour                 # 23
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 4/12/2019, 23:38
```

### Formating datetime output using strftime

```py
from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0

```

Time formating

```py
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)
```

```sh
time: 01:05:01
time one: 12/05/2019, 01:05:01
time two: 05/12/2019, 01:05:01
```

Here are all the _strftime_ symbols we use to format time. A reference of all the legal format codes.

![strftime](./images/strftime.png)

### String to time using strptime

```py
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
```

```sh
date_string = 5 December, 2019
date_object = 2019-12-05 00:00:00
```

### Use date from datetime

```py
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
```

### Time object to represent time

```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
```

output  
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555

### Difference between two datetime

```py
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Time left for new year:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
```

### Difference between two dates and times using timedelata

```py
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

```sh
    date_string = 5 December, 2019
    date_object = 2019-12-05 00:00:00
    t3 = 86 days, 22:56:50
```

## 💻 Exercises: Day 16

1. Get the current day, month, year, hour, minute and timestamp from time date module
1. Format the current date using in this format: "%m/%d/%Y, %H:%M:%S")
1. Today is 5 December, 2019. Change this time string to time.
1. Calculate the time difference from now to new year.
1. Calculate the time difference between 1 January 1970 and now.
1. Think about for what you can you use datetime module,
   - Time series analysis
   - To get time stamp of any activities in an application
   - And many other users

# 📘 Day 17

## Exception Handling

Python uses _try_ and _except_ to handle error gracefully. A graceful exit (or graceful handling) of error is a simple programming idiom wherein a program detects a serious error condition and "exits gracefully" in a controlled manner as a result. Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this make our application more robust. The cause of an exception is often external to the program itself. An example of exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning IO device. Graceful handling of errors prevent our application from crashing.

We have cover the different python _error_ types in the previous section. If we use _try_ and _except_ our program don't raise error.

![Try and Except](images/try_except.png)

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
    print('Something goes wrong')
```

In the above example the second operand is a string. So, we should change to float or int to add it with a number. Therefore, the second block which is the _except_ executed.
**Example:**

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born

    print(f'You are {name}. And your age is {age}.')
except:
    print('Something goes wrong')
```

```sh
Something goes wrong
```

In the above example, the exception block will run and we do not know exactly the problem. To know the problem we can use the different error types with except.

In the following example, it will handle the error and also tells the kind of error raised.

```py
except TypeError:
    print(TypeError)
except:
    print('Something goes wrong')
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
```

```sh
Enter your name:Asabeneh
Year you born:1920
Type error occur
I alway run.
```

In the above code the output is going to be _TypeError_.

Now, lets by by adding additional block:

```py
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)

    print(f'You are {name}. And your age is {age}.')
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

## Packing and Unpacking Arguments in Python

We use two operators:

- \* for tuples
- \*\* for dictionaries

Let's take as an example below. It takes only arguments but we have list. We can unpack the list and changes to argument.

### Unpacking

#### Unpacking list

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

When we run the above code, it raises an error because this function takes numbers as arguments not as list. Let's unpack or destructure the list.

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1,2,3,4,5]
print(sum_of_five_nums(*lst))  # 15
```

We can also use unpacking in the range builtin function that expects start and end.

```py
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

```

A list or a tuple can be also be unpacked like this:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle,last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### Unpacking dictionary

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```

### Packing

Sometimes we never know how many arguments need to be passed to a python function, we can use packing method to allow our function to take unlimited number or arbitrary number of arguments.

### Packing list

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### Packing dictionary

```py
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
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

Like JavaScript it is possible to spread in python. Lets see the example below:

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6,7]
lst = [0, *list_one, *list_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)        ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```
## Enumerate
In we are interested in an index of a list, we use *enumerate*.
```py
for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
```
```sh
The country Finland has been found at index 1.
```
## Zip
Sometimes we like to combine to lists when we loop through. See the example below:
```py
fruits = ['banana', 'orange', 'mango', 'lemon']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```
```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}]
```

## Exercises: Day 17
1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

# 📘 Day 18
## Regular Expression
A regular expression or RegEx is a small programming language that helps to find pattern in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is *re*.

### Import re module
After importing the module we can use it to detect or find patterns.
```py
import re
```
### re functions
To find a pattern we use different set of *re* functions that allows to search a string for match.
* *re.match()*:searches only in the beginning of the first line of the string and return match object if found, else return none. 
* *re.search*:Returns a Match object if there is a match anywhere in the string including or in multiline string.
* *re.findall*:Returns a list containing all matches
* *re.split*:	Returns a list where the string has been split at each match
* *re.sub*:  Replaces one or many matches with a string

#### Match
```py
# syntac
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
```
```py
txt = 'I love to teach python or javaScript'
# It return an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```
As you can see from the above example, the pattern we are looking for or the substring *I love to teach* is the beginning of the text. The match function only returns an object if the text starts with the pattern.

#### Search
```py
# syntax
re.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag
```
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

# It return an object with span, and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```
As you can see search is much better than match because it can look for the pattern through out the text. Search return returns a match object right way a first match found. A much better *re* function is *findall*. This function check the pattern through the string and returns all the matches as a list.

#### Searching all matches using findall
*findall()* returns all the matches as a list

```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

```
As you can see, the word language found two times in the string. Let's practice more

Let's look for the word both Python and python in the string
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```
Since we are using *re.I* both lowercase and uppercase are included but if we don't have the flag, we write our pattern differently. Let's see that
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```
#### Replacing a substring
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human begin has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human begin has ever created.
```
Let's add one more example, the following string is really hard to read unless we remove the % symbol. Replacing the % with a empty string will clean the text.
```py

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as m%ore r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher.'''

matches = re.sub('%', '', txt)
print(matches)  # ['Python', 'python']
```
```sh
I am teacher and  I love teaching.
There is nothing as more rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher.
```
## Spliting text using RegEx split
```py
txt = '''I am teacher and  I love teaching.
There is nothing as more rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher.'''
print(re.split('\n', txt))
```
```sh
['I am teacher and  I love teaching.', 'There is nothing as more rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher.']
```
## Writing RegEx pattern
To declare a string variable we use a single or double quote. To declare RegEx variable *r''*.
The following pattern only identifies apple with lowercase, to make it case insensitive either we should rewrite our pattern or we should add a flag.  
```py
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```
* []:  A set of characters
  * [a-c] means, a or b or c
  * [a-z] means, any letter a to z
  * [A-Z] means, any character A to Z
  * [0-3] means, 0 or 1 or 2 or 3
  * [0-9] means any number 0 to 9
  * [A-Za-z0-9] any character which is a to z, A to Z, 0 to 9
* \\:  uses to escape special characters
  * \d mean:match where the string contains digits (numbers from 0-9)
  * \D mean: match where the string does not contain digits
* . : any character except new line character(\n)
* ^: starts with
  * r'^substring' eg r'^love', a sentence which starts with a word love
  * r'[^abc] mean not a, not b, not c.
* $: ends with
  * r'substring$' eg r'love$', sentence ends with a word love
* *: zero or more times
  * r'[a]*' means a optional or it can be occur many times.
* +: one or more times
  * r'[a]+' mean at least once or more times
* ?: zero or one times
  *  r'[a]?' mean zero times or once
* {3}: Exactly 3 characters
* {3,}: At least 3 character
* {3,8}: 3 to 8 characters
* |: Either or
  * r'apple|banana' mean either of an apple or a banana
* (): Capture and group

![Regular Expression cheat sheet](images/regex.png)

Let's use example to clarify the above meta characters
### Square Bracket
Let's use square bracket to include lower and upper case
```py
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```
If we want to look for the banana, we write the pattern as follows:
```py
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```
Using the square bracket and or operator , we manage to extract Apple, apple, Banana and banana.

### Escape character(\\) in RegEx
```py
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made in December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9'], this is not what we want

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more
txt = 'This regular expression example was made in December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']
```
### One or more times(+)
```py
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made in December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']
```

### Period(.)
```py
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

```
### Zero or more times(*)
Zero or many times. The pattern could may not occur or it can occur many times.
```py

regex_pattern = r'[a].*'  # . any character, + any character one or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

```
### Zero or one times(?)
Zero or one times. The pattern could may not occur or it may occur once.
```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

```
### Quantifier in RegEx
We can specify the length of the substring we look for in a text, using a curly bracket. Lets imagine, we are interested in substring that their length are 4 characters
```py
txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019']

txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']

```
### Cart ^
* Starts with
  
```py
txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'^This'  # ^ means starts with
print(matches)  # ['This']
```

* Negation
```py
txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```


## 💻 Exercises: Day 18
  1. What is the most frequent word in the following paragraph ?
```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```
```sh
    [(6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')]
```
2. The position of some particles on the horizontal x-axis -12, -4, -3 and  -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers and find the distance between the two furthest particles.
```py
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 12
```
3. Write a pattern which identify if a string is a valid python variable
    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```
4. Clean the following text. After cleaning, count three most frequent words in the string.
    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```
   
[<< Part 5 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md) | [Part 7 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)

---



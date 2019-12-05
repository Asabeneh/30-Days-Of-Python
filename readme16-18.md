![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

🧳 [Part 1: Day 1 - 3](https://github.com/Asabeneh/30-Days-Of-Python)  
🧳 [Part 2: Day 4 - 6](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)  
🧳 [Part 3: Day 7 - 9](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)  
🧳 [Part 4: Day 10 - 12](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)  
🧳 [Part 5: Day 13 - 15](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)  
🧳 [Part 6: Day 16 - 18](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)  
🧳 [Part 7: Day 19 - 21](#) 🔒  
🧳 [Part 8: Day 22 - 24](#) 🔒  
🧳 [Part 9: Day 25 - 27](#) 🔒  
🧳 [Part 10: Day 28 - 30](#) 🔒

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
   

[<< Part 5 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md) | [Part 7 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)

---

```

```

```

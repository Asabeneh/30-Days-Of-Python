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
Here are all the *strftime* symbols we use to format time. A reference of all the legal format codes.

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
## 💻  Exercises: Day 16
1. Get the current day, month, year, hour, minute and timestamp from time date module
1. Format the current date using in this format: "%m/%d/%Y, %H:%M:%S")
1. Today is 5 December, 2019. Change this time string to time.
1. Calculate the time difference from now to new year.
1. Calculate the time difference between 1 January 1970 and now.
1. Think about for what you can you use datetime module, 
    * Time series analysis 
    * To get time stamp of any activities in an application
    * And many other users
[<< Part 5 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md) | [Part 7 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)

---
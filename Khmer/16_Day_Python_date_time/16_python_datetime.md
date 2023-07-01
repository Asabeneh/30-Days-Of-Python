<div align="center">
  <h1> 30 Days Of Python: Day 16 - Python Date time </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>Second Edition: July, 2021</small>
  </sub>

</div>

[<< Day 15](../15_Day_Python_type_errors/15_python_type_errors.md) | [Day 17 >>](../17_Day_Exception_handling/17_exception_handling.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 16](#-day-16)
  - [Python *datetime*](#python-datetime)
    - [Getting *datetime* Information](#getting-datetime-information)
    - [Formatting Date Output Using *strftime*](#formatting-date-output-using-strftime)
    - [String to Time Using *strptime*](#string-to-time-using-strptime)
    - [Using *date* from *datetime*](#using-date-from-datetime)
    - [Time Objects  តំណាង ឲ្យ ពេល វេលា](#time-objects--តំណាង-ឲ្យ-ពេល-វេលា)
    - [ភាពខុសគ្នារវាងចំណុចពីរក្នុងពេលប្រើ](#ភាពខុសគ្នារវាងចំណុចពីរក្នុងពេលប្រើ)
    - [ភាពខុសគ្នារវាងចំណុចពីរក្នុងពេលប្រើ *timedelata*](#ភាពខុសគ្នារវាងចំណុចពីរក្នុងពេលប្រើ-timedelata)

# 📘 Day 16

## Python *datetime*

Python មាន_datetime_ ដើម្បីគ្រប់គ្រងថ្ងៃ និងម៉ោង។

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

ជាមួយ dir ឬ help បញ្ជាដែលត្រូវបានបង្កើតឡើងវាអាចដឹងថាមុខងារដែលមាននៅក្នុងម៉ូឌុលមួយ។ ដូចដែលអ្នកអាចមើលបាននៅក្នុងម៉ូឌុល datetime មានមុខងារជាច្រើន ប៉ុន្តែយើងនឹងផ្តោតលើ *date*, *datetime*, *time* និង *timedelta*

### Getting *datetime* Information

```py
from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38
```

Timestamp ឬ Unix timestamp គឺជាចំនួនវិនាទីដែលបានហួសពីថ្ងៃទី 1 ខែមករាឆ្នាំ 1970 UTC ។

### Formatting Date Output Using *strftime*

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

ការកំណត់កាលបរិច្ឆេទពេលប្រើវិធីសាស្ត្រ *strftime* និងឯកសារអាចរកបាននៅទីនេះ (<https://strftime.org/>) ។

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

ការកំណត់កាលបរិច្ឆេទពេលប្រើវិធីសាស្ត្រ *strftime* និងឯកសារអាចរកបាននៅទីនេះ (<https://strftime.org/>) ។
![strftime](../images/strftime.png)

### String to Time Using *strptime*

Here is a [documentation](https://www.programiz.com/python-programming/datetime/strptimet) hat helps to understand the format.

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

### Using *date* from *datetime*

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

### Time Objects  តំណាង ឲ្យ ពេល វេលា

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

### ភាពខុសគ្នារវាងចំណុចពីរក្នុងពេលប្រើ

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

### ភាពខុសគ្នារវាងចំណុចពីរក្នុងពេលប្រើ *timedelata*

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



🎉 CONGRATULATIONS ! 🎉

[<< Day 15](../15_Day_Python_type_errors/15_python_type_errors.md) | [Day 17 >>](../17_Day_Exception_handling/17_exception_handling.md)

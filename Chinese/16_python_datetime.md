<div align="center">
  <h1> 30天Python学习：第16天 - Python日期和时间 </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>作者：
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>第二版：2021 年 7 月</small>
</sub>

</div>

[<< 第 15 天](../15_Day_Python_type_errors/15_python_type_errors.md) ｜ [第 17 天 >>](../17_Day_Exception_handling/17_exception_handling.md)

![30天Python学习](../images/30DaysOfPython_banner3@2x.png)

- [📘 第 16 天](#-第16天)
  - [Python _datetime_ 模块](#python-datetime-模块)
    - [获取 _datetime_ 信息](#获取-datetime-信息)
    - [使用 _strftime_ 格式化日期输出](#使用-strftime-格式化日期输出)
    - [使用 _strptime_ 将字符串转换为时间](#使用-strptime-将字符串转换为时间)
    - [从 _datetime_ 中使用 _date_](#从-datetime-中使用-date)
    - [用时间对象表示时间](#用时间对象表示时间)
    - [计算两个时间点之间的差异](#计算两个时间点之间的差异)
    - [使用 _timedelta_ 计算两个时间点之间的差异](#使用-timedelta-计算两个时间点之间的差异)
  - [💻 练习：第 16 天](#-练习-第16天)

# 📘 第 16 天

## Python _datetime_ 模块

Python 有一个 _datetime_ 模块来处理日期和时间。

```python
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

使用 dir 或 help 内置命令可以知道某个模块中可用的函数。如你所见，datetime 模块中有很多函数，但我们将专注于 _date_, _datetime_, _time_ 和 _timedelta_。让我们一一看一下它们。

### 获取 _datetime_ 信息

```python
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

时间戳或 Unix 时间戳是从 1970 年 1 月 1 日 UTC 起经过的秒数。

### 使用 _strftime_ 格式化日期输出

```python
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

使用 _strftime_ 方法格式化日期时间，可以在[这里](https://strftime.org/)找到文档。

```python
from datetime import datetime
# 当前日期和时间
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S 格式
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S 格式
print("time two:", time_two)
```

```sh
time: 01:05:01
time one: 12/05/2019, 01:05:01
time two: 05/12/2019, 01:05:01
```

下面是我们用来格式化时间的 _strftime_ 符号。此模块的所有格式示例。

![strftime](../images/strftime.png)

### 使用 _strptime_ 将字符串转换为时间

这里有一个帮助理解格式的[文档](https://www.programiz.com/python-programming/datetime/strptimet)。

```python
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

### 从 _datetime_ 中使用 _date_

```python
from datetime import date
d = date(2020, 1, 1)
print(d)
print('Current date:', d.today())    # 2019-12-05
# 今日日期对象
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
```

### 用时间对象表示时间

```python
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

输出结果
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555

### 计算两个时间点之间的差异

```python
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# 距离新年的时间：27天，0:00:00
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # 距离新年：26天，23:01:00
```

### 使用 _timedelta_ 计算两个时间点之间的差异

```python
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

🌕 你是非凡的。你已经向着伟大的道路迈出了第 16 步。现在为你的大脑和肌肉做一些练习吧。

## 💻 练习：第 16 天

1. 获取当前日期、月、年、小时、分钟和时间戳
2. 使用此格式格式化当前日期：“%m/%d/%Y, %H:%M:%S”
3. 今天是 2019 年 12 月 5 日。将这个时间字符串转换为时间。
4. 计算现在和新年之间的时间差。
5. 计算 1970 年 1 月 1 日和现在之间的时间差。
6. 想想，你可以使用 datetime 模块做什么？示例：
   - 时间序列分析
   - 获取应用程序中任何活动的时间戳
   - 添加博客上的帖子

🎉 恭喜你 ! 🎉

[<< 第 15 天](../15_Day_Python_type_errors/15_python_type_errors.md) ｜ [第 17 天 >>](../17_Day_Exception_handling/17_exception_handling.md)

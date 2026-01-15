# 30天Python编程挑战：第16天 - Python日期时间

- [第16天](#-第16天)
  - [Python *datetime*](#python-datetime)
    - [获取 *datetime* 信息](#获取-datetime-信息)
    - [使用 *strftime* 格式化日期输出](#使用-strftime-格式化日期输出)
    - [使用 *strptime* 将字符串转换为时间](#使用-strptime-将字符串转换为时间)
    - [从 *datetime* 使用 *date*](#从-datetime-使用-date)
    - [使用Time对象表示时间](#使用time对象表示时间)
    - [计算两个时间点之间的差异](#计算两个时间点之间的差异)
    - [使用 *timedelta* 计算两个时间点之间的差异](#使用-timedelta-计算两个时间点之间的差异)
  - [💻 练习 - 第16天](#-练习---第16天)

# 📘 第16天

## Python *datetime*

Python有一个 _datetime_ 模块用于处理日期和时间。

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

通过dir或help内置命令，可以了解特定模块中可用的函数。如你所见，datetime模块中有许多函数，但我们将重点关注 _date_、_datetime_、_time_ 和 _timedelta_。让我们一个一个地看。

### 获取 *datetime* 信息

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

时间戳或Unix时间戳是从1970年1月1日UTC开始经过的秒数。

### 使用 *strftime* 格式化日期输出

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

使用 *strftime* 方法格式化日期时间，相关文档可以在[这里](https://strftime.org/)找到。

```py
from datetime import datetime
# 当前日期和时间
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("时间:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S 格式
print("时间一:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S 格式
print("时间二:", time_two)
```

```sh
时间: 01:05:01
时间一: 12/05/2019, 01:05:01
时间二: 05/12/2019, 01:05:01
```

以下是我们用来格式化时间的所有 _strftime_ 符号。这个模块的所有格式示例。

![strftime](../images/strftime.png)

### 使用 *strptime* 将字符串转换为时间
这里有一个[文档](https://www.programiz.com/python-programming/datetime/strptimet)，有助于理解格式。

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

### 从 *datetime* 使用 *date*

```py
from datetime import date
d = date(2020, 1, 1)
print(d)
print('当前日期:', d.today())    # 2019-12-05
# 今天的日期对象
today = date.today()
print("当前年份:", today.year)   # 2019
print("当前月份:", today.month) # 12
print("当前日:", today.day)     # 5
```

### 使用Time对象表示时间

```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute 和 second)
b = time(10, 30, 50)
print("b =", b)
# time(hour, minute 和 second)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)
```

输出：  
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555

### 计算两个时间点之间的差异

```py
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# 距离新年的时间：  27 days, 0:00:00
print('距离新年的时间: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('距离新年的时间:', diff) # 距离新年的时间: 26 days, 23: 01: 00
```

### 使用 *timedelta* 计算两个时间点之间的差异

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

🌕 你太了不起了。你在通往卓越的道路上已经前进了16步。现在做一些练习锻炼你的大脑和肌肉。

## 💻 练习 - 第16天

1. 从datetime模块获取当前的日、月、年、小时、分钟和时间戳
2. 使用此格式格式化当前日期："%m/%d/%Y, %H:%M:%S"
3. 今天是2019年12月5日。将此时间字符串转换为时间。
4. 计算现在和新年之间的时间差。
5. 计算1970年1月1日和现在之间的时间差。
6. 思考，你可以将datetime模块用于什么？例如：
   - 时间序列分析
   - 获取应用程序中任何活动的时间戳
   - 在博客上添加帖子

🎉 恭喜！🎉

[<< 第 15 天](./15_python_type_errors_cn.md) | [第 17 天 >>](./17_exception_handling_cn.md) 
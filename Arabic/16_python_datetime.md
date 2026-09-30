<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 16 - التاريخ والوقت في بايثون</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="متابعة في تويتر" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>المؤلف:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>الطبعة الثانية: يوليو 2021</small>
  </sub>
</div>

[<< اليوم 15](./15_python_type_errors.md) | [اليوم 17 >>](./17_exception_handling.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 16](#-اليوم-16)
  - [وحدة *datetime* في بايثون](#وحدة-datetime-في-بايثون)
    - [الحصول على معلومات *datetime*](#الحصول-على-معلومات-datetime)
    - [تنسيق مخرجات التاريخ باستخدام *strftime*](#تنسيق-مخرجات-التاريخ-باستخدام-strftime)
    - [تحويل النص إلى وقت باستخدام *strptime*](#تحويل-النص-إلى-وقت-باستخدام-strptime)
    - [استخدام *date* من *datetime*](#استخدام-date-من-datetime)
    - [كائنات الوقت لتمثيل الوقت](#كائنات-الوقت-لتمثيل-الوقت)
    - [الفرق بين نقطتين في الوقت](#الفرق-بين-نقطتين-في-الوقت)
    - [الفرق بين نقطتين في الوقت باستخدام *timedelta*](#الفرق-بين-نقطتين-في-الوقت-باستخدام-timedelta)
  - [💻 تمارين: اليوم 16](#-تمارين-اليوم-16)

# 📘 اليوم 16

## وحدة *datetime* في بايثون

تحتوي بايثون على وحدة 'datetime' للتعامل مع التاريخ والوقت.

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

باستخدام أوامر 'dir' أو 'help' المضمنة في بايثون، يمكننا معرفة الدوال المتاحة في أي وحدة. كما ترى، في وحدة 'datetime' هناك العديد من الدوال، لكننا سنركز على 'date'، 'datetime'، 'time' و 'timedelta'. دعنا نراها واحدًا تلو الآخر.

### الحصول على معلومات *datetime*

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

الطابع الزمني (timestamp) هو عدد الثواني المنقضية منذ منتصف ليل الأول من يناير عام 1970 بالتوقيت العالمي المنسق (UTC).

### تنسيق مخرجات التاريخ باستخدام *strftime*

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

تنسيق التاريخ والوقت باستخدام دالة 'strftime'، ويمكن العثور على الوثائق [هنا](https://strftime.org/).

```py
from datetime import datetime
# التاريخ والوقت الحالي
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# تنسيق mm/dd/YY H:M:S
print("time one:", time_one)        # time one: 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# تنسيق dd/mm/YY H:M:S
print("time two:", time_two)        # time two: 28/06/2022, 18:21:40
```

```sh
time: 01:05:01
time one: 12/05/2019, 01:05:01
time two: 05/12/2019, 01:05:01
```

هنا جميع رموز 'strftime' التي نستخدمها لتنسيق الوقت. مثال على جميع التنسيقات لهذه الوحدة.

![strftime](../images/strftime.png)

### تحويل النص إلى وقت باستخدام *strptime*

هذه [وثيقة](https://www.programiz.com/python-programming/datetime/strptime) تساعد على فهم التنسيق.

```py
from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)     # date_string = 5 December, 2019
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)     # date_object = 2019-12-05 00:00:00
```

```sh
date_string = 5 December, 2019
date_object = 2019-12-05 00:00:00
```

### استخدام *date* من *datetime*

```py
from datetime import date
d = date(2020, 1, 1)
print(d)        # 2020-01-01
print('Current date:', d.today())    # 2019-12-05
# كائن date لتاريخ اليوم
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
```

### كائنات الوقت لتمثيل الوقت

```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)     # a = 00:00:00
# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555
```

المخرجات
a = 00:00:00
b = 10:30:50
c = 10:30:50
d = 10:30:50.200555

### الفرق بين نقطتين في الوقت

```py
from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# الوقت المتبقي للسنة الجديدة: 27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
```

### الفرق بين نقطتين في الوقت باستخدام *timedelta*

```py
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)
```

```sh
t3 = 86 days, 22:56:50
```

🌕 أنت استثنائي. أنت على بعد 16 خطوة في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 16

1. احصل على اليوم والشهر والسنة والساعة والدقيقة والطابع الزمني (timestamp) الحاليين من وحدة 'datetime'
2. قم بتنسيق التاريخ الحالي باستخدام هذا التنسيق: "%m/%d/%Y, %H:%M:%S"
3. اليوم هو 5 ديسمبر 2019. غيّر هذا النص الزمني إلى وقت.
4. احسب الفرق الزمني بين الآن والسنة الجديدة.
5. احسب الفرق الزمني بين 1 يناير 1970 والآن.
6. فكر، ماذا يمكنك استخدام وحدة 'datetime' لأجله؟ أمثلة:
   - تحليل السلاسل الزمنية
   - للحصول على طابع زمني لأي أنشطة في تطبيق
   - إضافة منشورات على مدونة

🎉 مبروك! 🎉

[<< اليوم 15](./15_python_type_errors.md) | [اليوم 17 >>](./17_exception_handling.md)
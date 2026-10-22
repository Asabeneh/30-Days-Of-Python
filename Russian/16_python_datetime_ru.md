<div align="center">
  <h1> 30 дней Python: День 16 - Дата и время в Python </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>Второе издание: июль 2021</small>
  </sub>
</div>

[<< День 15](./15_python_type_errors_ru.md) | [День 17 >>](./17_exception_handling_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 День 16](#-день-16)
  - [Python *datetime*](#python-datetime)
    - [Получение информации из *datetime*](#получение-информации-из-datetime)
    - [Форматирование вывода даты с помощью *strftime*](#форматирование-вывода-даты-с-помощью-strftime)
    - [Строка в дату с помощью *strptime*](#строка-в-дату-с-помощью-strptime)
    - [Использование *date* из *datetime*](#использование-date-из-datetime)
    - [Объекты времени для представления времени](#объекты-времени-для-представления-времени)
    - [Разница между двумя моментами времени с помощью](#разница-между-двумя-моментами-времени-с-помощью)
    - [Разница между двумя моментами времени с помощью *timedelta*](#разница-между-двумя-моментами-времени-с-помощью-timedelta)
  - [💻 Упражнения: День 16](#-упражнения-день-16)
# 📘 День 16

## Python *datetime*

В Python есть модуль _datetime_ для работы с датой и временем.

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

С помощью встроенных команд dir или help можно узнать доступные функции в определённом модуле. Как видите, в модуле datetime много функций, но мы сосредоточимся на _date_, _datetime_, _time_ и _timedelta_. Давайте рассмотрим их по очереди.

### Получение информации из *datetime*

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

Timestamp, или Unix-время, — это количество секунд, прошедших с 1 января 1970 года по UTC.

### Форматирование вывода даты с помощью *strftime*

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

Форматирование даты и времени с помощью метода *strftime*; документацию можно найти [здесь](https://strftime.org/).

```py
from datetime import datetime
# текущая дата и время
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# формат мм/дд/гг Ч:М:С
print("time one:", time_one)        # time one: 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# формат дд/мм/гг Ч:М:С
print("time two:", time_two)        # time two: 28/06/2022, 18:21:40
```

```sh
time: 01:05:01
time one: 12/05/2019, 01:05:01
time two: 05/12/2019, 01:05:01
```

Вот все символы _strftime_, которые мы используем для форматирования времени. Пример всех форматов для этого модуля.

![strftime](../images/strftime.png)

### Строка в дату с помощью *strptime*
Вот [документация](https://www.programiz.com/python-programming/datetime/strptime), которая помогает понять формат. 

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

### Использование *date* из *datetime*

```py
from datetime import date
d = date(2020, 1, 1)
print(d)        # 2020-01-01
print('Current date:', d.today())    # 2019-12-05
# объект date сегодняшней даты
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
```

### Объекты времени для представления времени

```py
from datetime import time
# время(час = 0, минута = 0, секунда = 0)
a = time()
print("a =", a)     # a = 00:00:00
# время(час, минута и секунда)
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
# время(час, минута и секунда)
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
# время(час, минута, секунда, микросекунда)
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555
```

вывод  
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555

### Разница между двумя моментами времени с помощью

```py
from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# Осталось времени до Нового года:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
```

### Разница между двумя моментами времени с помощью *timedelta*

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

🌕 Вы необыкновенны. Вы на 16 шагов впереди на пути к величию. Теперь сделайте несколько упражнений для ума и мышц.

## 💻 Упражнения: День 16

1. Получите текущий день, месяц, год, час, минуту и timestamp из модуля datetime
2. Отформатируйте текущую дату в формате: "%m/%d/%Y, %H:%M:%S")
3. Сегодня 5 декабря 2019 года. Преобразуйте эту строку времени во время.
4. Вычислите разницу во времени между сейчас и Новым годом.
5. Вычислите разницу во времени между 1 января 1970 года и сейчас.
6. Подумайте, для чего можно использовать модуль datetime? Примеры:
   - Анализ временных рядов
   - Получение отметки времени любых действий в приложении
   - Добавление постов в блог 

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 15](./15_python_type_errors_ru.md) | [День 17 >>](./17_exception_handling_ru.md)

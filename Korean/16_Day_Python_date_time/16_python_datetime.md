<div align="center">
  <h1> 30 Days Of Python: Day 16 - Python 날짜와 시간 </h1>
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

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 16](#-day-16)
  - [Python *datetime*](#python-datetime)
    - [*datetime* 정보 가져오기](#datetime-정보-가져오기)
    - [*strftime*을 사용한 날짜 출력 포맷팅](#strftime을-사용한-날짜-출력-포맷팅)
    - [*strptime*을 사용한 문자열을 시간으로 변환](#strptime을-사용한-문자열을-시간으로-변환)
    - [*datetime*에서 *date* 사용하기](#datetime에서-date-사용하기)
    - [시간을 나타내는 Time 객체](#시간을-나타내는-time-객체)
    - [두 시점 간의 차이 계산](#두-시점-간의-차이-계산)
    - [*timedelta*를 사용한 두 시점 간의 차이](#timedelta를-사용한-두-시점-간의-차이)
  - [💻 연습문제: Day 16](#-연습문제-day-16)
# 📘 Day 16

## Python *datetime*

Python에는 날짜와 시간을 처리하기 위한 _datetime_ 모듈이 있습니다.

```py
import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

dir 또는 help 내장 명령을 사용하면 특정 모듈에서 사용 가능한 함수를 알 수 있습니다. 보시다시피 datetime 모듈에는 많은 함수가 있지만, 우리는 _date_, _datetime_, _time_ 및 _timedelta_에 초점을 맞출 것입니다. 하나씩 살펴봅시다.

### *datetime* 정보 가져오기

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

Timestamp 또는 Unix timestamp는 1970년 1월 1일 UTC부터 경과한 초의 수입니다.

### *strftime*을 사용한 날짜 출력 포맷팅

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

*strftime* 메서드를 사용하여 날짜와 시간을 포맷팅할 수 있으며, 관련 문서는 [여기](https://strftime.org/)에서 찾을 수 있습니다.

```py
from datetime import datetime
# 현재 날짜와 시간
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)           # time: 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S 포맷
print("time one:", time_one)        # time one: 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S 포맷
print("time two:", time_two)        # time two: 28/06/2022, 18:21:40
```

```sh
time: 01:05:01
time one: 12/05/2019, 01:05:01
time two: 05/12/2019, 01:05:01
```

다음은 시간을 포맷팅하는 데 사용하는 모든 _strftime_ 기호입니다. 이 모듈의 모든 포맷 예시입니다.

![strftime](../../images/strftime.png)

### *strptime*을 사용한 문자열을 시간으로 변환
다음은 포맷을 이해하는 데 도움이 되는 [문서](https://www.programiz.com/python-programming/datetime/strptime)입니다.

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

### *datetime*에서 *date* 사용하기

```py
from datetime import date
d = date(2020, 1, 1)
print(d)        # 2020-01-01
print('Current date:', d.today())    # 2019-12-05
# 오늘 날짜의 date 객체
today = date.today()
print("Current year:", today.year)   # 2019
print("Current month:", today.month) # 12
print("Current day:", today.day)     # 5
```

### 시간을 나타내는 Time 객체

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

출력  
a = 00:00:00  
b = 10:30:50  
c = 10:30:50  
d = 10:30:50.200555

### 두 시점 간의 차이 계산

```py
from datetime import date, datetime
today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
time_left_for_newyear = new_year - today
# 새해까지 남은 시간:  27 days, 0:00:00
print('Time left for new year: ', time_left_for_newyear)  # Time left for new year:  27 days, 0:00:00

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00
```

### *timedelta*를 사용한 두 시점 간의 차이

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

🌕 당신은 대단합니다. 위대함을 향한 여정에서 16단계를 앞서고 있습니다. 이제 뇌와 근육을 위한 연습을 해봅시다.

## 💻 연습문제: Day 16

1. datetime 모듈에서 현재 날짜, 월, 연도, 시, 분 및 타임스탬프를 가져오세요
2. 현재 날짜를 다음 포맷으로 포맷팅하세요: "%m/%d/%Y, %H:%M:%S")
3. 오늘은 2019년 12월 5일입니다. 이 시간 문자열을 시간으로 변환하세요.
4. 현재와 새해 사이의 시간 차이를 계산하세요.
5. 1970년 1월 1일과 현재 사이의 시간 차이를 계산하세요.
6. datetime 모듈을 어디에 사용할 수 있는지 생각해 보세요. 예시:
   - 시계열 분석
   - 애플리케이션에서 활동의 타임스탬프 가져오기
   - 블로그에 게시글 추가

🎉 축하합니다 ! 🎉

[<< Day 15](../15_Day_Python_type_errors/15_python_type_errors.md) | [Day 17 >>](../17_Day_Exception_handling/17_exception_handling.md)

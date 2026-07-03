<div align="center">
  <h1> 30 Days Of Python: Day 12 - Modules </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>


</div>

[<< Day 11](../11_Day_Functions/11_functions.md) | [Day 13>>](../13_Day_List_comprehension/13_list_comprehension.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 12](#-day-12)
  - [Modules](#modules)
    - [What is a Module](#what-is-a-module)
    - [Creating a Module](#creating-a-module)
    - [Importing a Module](#importing-a-module)
    - [Import Functions from a Module](#import-functions-from-a-module)
    - [Import Functions from a Module and Renaming](#import-functions-from-a-module-and-renaming)
  - [Import Built-in Modules](#import-built-in-modules)
    - [OS Module](#os-module)
    - [Sys Module](#sys-module)
    - [Statistics Module](#statistics-module)
    - [Math Module](#math-module)
    - [String Module](#string-module)
    - [Random Module](#random-module)
  - [💻 Exercises: Day 12](#-exercises-day-12)
    - [Exercises: Level 1](#exercises-level-1)
    - [Exercises: Level 2](#exercises-level-2)
    - [Exercises: Level 3](#exercises-level-3)

# 📘 Day 12

## Modules

### What is a Module

모듈은 애플리케이션에 포함할 수 있는 코드 세트 또는 함수 세트를 포함하는 파일입니다. 모듈은 단일 변수, 함수 또는 대규모 코드 베이스를 포함하는 파일일 수 있습니다.

### Creating a Module

모듈을 만들려면 파이썬 스크립트에 코드를 작성하고 .py 파일로 저장합니다. 프로젝트 폴더 안에 mymodule.py라는 파일을 만들어봅시다. 이 파일에 코드를 작성해봅시다.

```py
# mymodule.py 파일
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

프로젝트 디렉토리에 main.py 파일을 만들고 mymodule.py 파일을 임포트합니다.

### Importing a Module

파일을 임포트하려면 _import_ 키워드와 파일 이름만 사용합니다.

```py
# main.py 파일
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### Import Functions from a Module

파일에 많은 함수가 있을 수 있으며 모든 함수를 다르게 임포트할 수 있습니다.

```py
# main.py 파일
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Import Functions from a Module and Renaming

임포트하는 동안 모듈의 이름을 변경할 수 있습니다.

```py
# main.py 파일
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Import Built-in Modules

다른 프로그래밍 언어와 마찬가지로 _import_ 키워드를 사용하여 파일/함수를 임포트하여 모듈을 임포트할 수도 있습니다. 가장 자주 사용하는 일반적인 모듈을 임포트해봅시다. 일반적인 내장 모듈 중 일부는 다음과 같습니다: _math_, _datetime_, _os_, _sys_, _random_, _statistics_, _collections_, _json_, _re_

### OS Module

파이썬 _os_ 모듈을 사용하면 많은 운영 체제 작업을 자동으로 수행할 수 있습니다. 파이썬의 OS 모듈은 디렉토리(폴더)를 생성, 현재 작업 디렉토리를 변경, 디렉토리를 제거, 내용을 가져오기, 현재 디렉토리를 변경 및 식별하는 기능을 제공합니다.

```py
# 모듈 임포트
import os
# 디렉토리 생성
os.mkdir('directory_name')
# 현재 디렉토리 변경
os.chdir('path')
# 현재 작업 디렉토리 가져오기
os.getcwd()
# 디렉토리 제거
os.rmdir()
```

### Sys Module

sys 모듈은 파이썬 런타임 환경의 다양한 부분을 조작하는 데 사용되는 함수와 변수를 제공합니다. sys.argv 함수는 파이썬 스크립트에 전달된 명령줄 인자의 리스트를 반환합니다. 이 리스트에서 인덱스 0의 항목은 항상 스크립트의 이름이고, 인덱스 1은 명령줄에서 전달된 인자입니다.

script.py 파일의 예시:

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # 이 줄은 다음을 출력합니다: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

이 스크립트가 어떻게 작동하는지 확인하기 위해 명령줄에 다음을 입력했습니다:

```sh
python script.py Asabeneh 30DaysOfPython
```

결과:

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge! 
```

유용한 sys 명령들:

```py
# sys 종료
sys.exit()
# 가장 큰 정수 변수 크기를 알려줍니다
sys.maxsize
# 환경 경로를 알려줍니다
sys.path
# 사용 중인 파이썬 버전을 알려줍니다
sys.version
```

### Statistics Module

statistics 모듈은 수치 데이터의 수학적 통계 함수를 제공합니다. 이 모듈에서 정의된 인기 있는 통계 함수들: _mean_, _median_, _mode_, _stdev_ 등.

```py
from statistics import * # 모든 statistics 모듈 임포트
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Math Module

많은 수학적 연산과 상수를 포함하는 모듈입니다.

```py
import math
print(math.pi)           # 3.141592653589793, pi 상수
print(math.sqrt(2))      # 1.4142135623730951, 제곱근
print(math.pow(2, 3))    # 8.0, 거듭제곱 함수
print(math.floor(9.81))  # 9, 내림
print(math.ceil(9.81))   # 10, 올림
print(math.log10(100))   # 2, 밑이 10인 로그
```

이제 많은 함수를 가진 *math* 모듈을 임포트했습니다. 모듈이 가진 함수를 확인하려면 _help(math)_ 또는 _dir(math)_ 를 사용할 수 있습니다. 이것은 모듈에서 사용 가능한 함수를 표시합니다. 모듈에서 특정 함수만 임포트하려면 다음과 같이 임포트합니다:

```py
from math import pi
print(pi)
```

여러 함수를 한 번에 임포트하는 것도 가능합니다.

```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

하지만 math 모듈의 모든 함수를 임포트하려면 \*를 사용할 수 있습니다.

```py
from math import *
print(pi)                  # 3.141592653589793, pi 상수
print(sqrt(2))             # 1.4142135623730951, 제곱근
print(pow(2, 3))           # 8.0, 거듭제곱
print(floor(9.81))         # 9, 내림
print(ceil(9.81))          # 10, 올림
print(math.log10(100))     # 2
```

임포트할 때 함수의 이름을 변경할 수도 있습니다.

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### String Module

string 모듈은 다양한 용도로 유용한 모듈입니다. 아래 예제는 string 모듈의 몇 가지 사용법을 보여줍니다.

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Random Module

이제 여러분은 모듈을 임포트하는 것에 익숙해졌을 것입니다. 더 익숙해지기 위해 하나 더 임포트해봅시다. 0과 0.9999... 사이의 난수를 제공하는 _random_ 모듈을 임포트해봅시다. _random_ 모듈에는 많은 함수가 있지만 이 섹션에서는 _random_ 과 _randint_ 만 사용하겠습니다.

```py
from random import random, randint
print(random())   # 인자를 받지 않으며 0과 0.9999 사이의 값을 반환합니다
print(randint(5, 20)) # [5, 20] 범위 내의 랜덤 정수를 반환합니다 (양쪽 끝 포함)
```

🌕 멀리까지 나아가고 있습니다. 계속하세요! 12일차 도전을 완료했으며 위대함을 향한 12걸음 앞에 있습니다. 이제 여러분의 뇌와 근육을 위한 운동을 하세요.

## 💻 Exercises: Day 12

### Exercises: Level 1

1. 6자리/문자의 random_user_id를 생성하는 함수를 작성합니다.
   ```py
     print(random_user_id()) 
     '1ee33d'
   ```
2. 이전 과제를 수정합니다. user_id_gen_by_user라는 함수를 선언합니다. 매개변수를 받지 않지만 input()을 사용하여 두 개의 입력을 받습니다. 하나는 문자 수이고 두 번째 입력은 생성할 ID의 수입니다.
   
```py
print(user_id_gen_by_user()) # 사용자 입력: 5 5
# 출력:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. rgb_color_gen이라는 함수를 작성합니다. rgb 색상을 생성합니다 (각각 0에서 255 사이의 3개 값).
   
```py
print(rgb_color_gen())
# rgb(125,244,255) - 출력은 이 형태여야 합니다
```

### Exercises: Level 2

1. 배열에 임의의 수의 16진수 색상을 반환하는 list_of_hexa_colors 함수를 작성합니다 (# 뒤에 6개의 16진수 숫자. 16진수 체계는 16개의 기호(0-9와 알파벳의 처음 6글자 a-f)로 이루어져 있습니다. 출력 예시는 과제 6을 확인하세요).
1. 배열에 임의의 수의 RGB 색상을 반환하는 list_of_rgb_colors 함수를 작성합니다.
1. 임의의 수의 hexa 또는 rgb 색상을 생성할 수 있는 generate_colors 함수를 선언합니다.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

### Exercises: Level 3

1. shuffle_list 함수를 호출합니다. 리스트를 매개변수로 받아 섞인 리스트를 반환합니다.
1. 0-9 범위에서 7개의 고유한 랜덤 숫자 배열을 반환하는 함수를 작성합니다.

🎉 CONGRATULATIONS ! 🎉

[<< Day 11](../11_Day_Functions/11_functions.md) | [Day 13>>](../13_Day_List_comprehension/13_list_comprehension.md)

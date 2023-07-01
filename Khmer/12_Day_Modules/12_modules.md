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
</div>

[<< Day 11](../11_Day_Functions/11_functions.md) | [Day 13>>](../13_Day_List_comprehension/13_list_comprehension.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

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

# 📘 Day 12

## Modules

### What is a Module
Module គឺជាឯកសារដែលមានកូដ ឬមុខងារមួយចំនួនដែលអាចបញ្ចូលទៅក្នុងកម្មវិធី។ Module អាចជាឯកសារដែលមានចម្រុះតែមួយ, function ឬមូលដ្ឋានកូដធំ។
### Creating a Module

ដើម្បីបង្កើត module យើងសរសេរកូដរបស់យើងក្នុង Python script ហើយយើងទុកវាជា.py file បង្កើតឯកសារដែលមានឈ្មោះ mymodule.py នៅក្នុងឯកសារគម្រោងរបស់អ្នក។ សូមយើងសរសេរកូដមួយចំនួននៅក្នុងឯកសារនេះ

```py
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

បង្កើតឯកសារ main.py នៅក្នុងបញ្ជីគម្រោងរបស់អ្នក ហើយនាំចូលឯកសារ mymodule.py ។

### Importing a Module

ដើម្បីនាំចូលឯកសារយើងប្រើពាក្យគន្លឹះ _import_ និងឈ្មោះឯកសារប៉ុណ្ណោះ។

```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### Import Functions from a Module
យើង អាច មាន មុខងារ ជាច្រើន ក្នុង ឯកសារ ហើយ យើង អាច នាំចូល មុខងារ ទាំងអស់ ផ្សេងៗ

```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Import Functions from a Module and Renaming

ក្នុងអំឡុងពេលនាំចូលយើងអាចប្តូរឈ្មោះម៉ូឌុល។
```py
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Import Built-in Modules

ដូចភាសាកម្មវិធីផ្សេងទៀតយើងក៏អាចនាំចូលម៉ូឌុលដោយនាំចូលឯកសារ / មុខងារដោយប្រើពាក្យគន្លឹះ _import_ ។ សូម នាំចូល ម៉ូឌុល រួម យើង នឹង ប្រើប្រាស់ ភាគច្រើន នៃ ពេលវេលា ។ មួយចំនួននៃម៉ូឌុលរួមបញ្ចូលរួមគ្នា: _math_, _datetime_, _os_,_sys_, _random_, _statistics_, _collections_, _json_,_re_
### OS Module

ដោយប្រើ python _os_ module វាអាចធ្វើបានដោយស្វ័យប្រវត្តិដើម្បីធ្វើការងារប្រព័ន្ធប្រតិបត្តិការជាច្រើន។ ម៉ូឌុល OS នៅក្នុង Python ផ្តល់មុខងារសម្រាប់បង្កើត, ការផ្លាស់ប្តូរ directory ការងារបច្ចុប្បន្ន, និងការលុប directory (folder) មួយ, ទាញយកខ្លឹមសាររបស់វា, ការផ្លាស់ប្តូរនិងកំណត់អត្តសញ្ញាណ directory បច្ចុប្បន្ន។

```py
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

### Sys Module

ម៉ូឌុល sys ផ្តល់មុខងារ និងចម្រុះដែលប្រើដើម្បីកែប្រែផ្នែកផ្សេងគ្នានៃPython runtime environment ។ Function sys.argv វិលត្រឡប់បញ្ជីបញ្ជា line arguments ដែលត្រូវបានផ្ទេរទៅ Python script ។ ចំណុចនៅ index 0 នៅក្នុងបញ្ជីនេះគឺជាឈ្មោះរបស់ script នៅ index 1 គឺជាពាក្យដែលត្រូវបានផ្ទេរចេញពី command line ។

Example of a script.py file:

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

ឥឡូវនេះដើម្បីពិនិត្យមើលថា តើ script នេះដំណើរការយ៉ាងម៉េច ខ្ញុំបានសរសេរនៅក្នុង command line:
```sh
python script.py Asabeneh 30DaysOfPython
```

The result:

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge! 
```

Some useful sys commands:

```py
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

### Statistics Module

ម៉ូឌុលស្តង់ដារផ្តល់មុខងារសម្រាប់ស្តង់ដារគណិតវិទ្យានៃទិន្នន័យលេខ។ តួនាទីស្តង់ដារដែលពេញនិយមដែលត្រូវបានកំណត់នៅក្នុងម៉ូឌុលនេះ: _mean_, _median_, _mode_, _stdev_ ជាដើម

```py
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Math Module

ម៉ូឌុលដែលមានប្រតិបត្តិការគណិតវិទ្យាជាច្រើននិងកម្រិត។

```py
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
```

ឥឡូវនេះយើងបាននាំចូលម៉ូឌុល _math_ ដែលមានមុខងារជាច្រើនដែលអាចជួយយើងក្នុងការធ្វើគណិតវិទ្យា ដើម្បីពិនិត្យមើលថា តើម៉ូឌុលនេះមានមុខងារអ្វីខ្លះ យើងអាចប្រើ _help (math)_ ឬ _dir (math)_ ។ នេះនឹងបង្ហាញមុខងារដែលមាននៅក្នុងម៉ូឌុល។ ប្រសិនបើយើងចង់នាំចូលមុខងារណាមួយពីម៉ូឌុលយើងនាំចូលដូចខាងក្រោម:

```py
from math import pi
print(pi)
```

វាក៏អាចនាំចូលមុខងារជាច្រើនក្នុងពេលតែមួយ
```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

ប៉ុន្តែបើយើងចង់នាំចូលលក្ខខណ្ឌទាំងអស់នៅក្នុងម៉ូឌុលគណិតវិទ្យាយើងអាចប្រើ \* ។
```py
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
```

នៅពេលដែលយើងនាំចូលយើងក៏អាចប្តូរឈ្មោះ function ផងដែរ។
```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### String Module

ម៉ូឌុល string គឺជាម៉ូឌុលដែលមានប្រយោជន៍សម្រាប់គោលបំណងជាច្រើន។ ឧទាហរណ៍ខាងក្រោមនេះបង្ហាញនូវការប្រើម៉ូឌុល string ។
```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Random Module

ឥឡូវនេះអ្នកបានស្គាល់អំពីការនាំចូលម៉ូឌុល។ សូមយើងធ្វើការនាំចូលមួយទៀត ដើម្បីយល់ដឹងច្បាស់លាស់។ សូមយើងនាំចូល _random_ module ដែលផ្តល់ឱ្យយើងជាចំនួនរលូនរវាង 0 និង 0.9999.... _random_ module មានមុខងារជាច្រើន ប៉ុន្តែនៅក្នុងផ្នែកនេះយើងនឹងប្រើ _random_ និង _randint_ តែប៉ុណ្ណោះ

```py
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
```

🌕អ្នកនឹងទៅឆ្ងាយ។ បន្តទៅ! អ្នក ទើបតែ បញ្ចប់ ការប្រឈម ថ្ងៃទី១២ ហើយ អ្នកមាន ១២ ជំហាន ទៅរក ភាពអស្ចារ្យ។ ឥឡូវ ធ្វើ លំ ហាត់ប្រាណ ខ្លះ សម្រាប់ ខួរក្បាល និង សាច់ដុំ របស់ អ្នក ។



🎉 CONGRATULATIONS ! 🎉

[<< Day 11](../11_Day_Functions/11_functions.md) | [Day 13>>](../13_Day_List_comprehension/13_list_comprehension.md)

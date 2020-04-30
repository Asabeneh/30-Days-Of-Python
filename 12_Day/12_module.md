<div align="center">
  <h1> 30 Days Of Python: Day 11 - Modules </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> First Edition: Nov 22 - Dec 22, 2019</small>
</sub>

</div>
</div>

[<< Day 11](../11_Day/11_function.md) | [Day 13>>](../13_Day/13_list_comprehension.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 12](#%f0%9f%93%98-day-12)
  - [Module](#module)
    - [What is a module](#what-is-a-module)
    - [Creating a module](#creating-a-module)
    - [Importing a module](#importing-a-module)
    - [Import functions from a module](#import-functions-from-a-module)
    - [Import functions from a module and renaming](#import-functions-from-a-module-and-renaming)
  - [Import Builtin Modules](#import-builtin-modules)
    - [OS Module](#os-module)
    - [Sys Module](#sys-module)
    - [Statistics Module](#statistics-module)
    - [Math Module](#math-module)
    - [Random Module](#random-module)
  - [💻 Exercises: Day 12](#%f0%9f%92%bb-exercises-day-12)

# 📘 Day 12

## Module

### What is a module

A module is a file containing set of codes or a set of function which can be included to an application. A module could be a file containing a single variable, or function, a big code base.

### Creating a module

To create a module we write our codes in a python script and we save it as .py file. Create a file named mymodule.py inside your project folder. Let write code on this file.

```py
# mymodule.py file
def generate_full_name(firstname, lastname):
      space = ' '
      fullname = firstname + space + lastname
      return fullname
```

Create main.py file in your project directory and import the mymodule.py file.

### Importing a module

To import the file we use the _import_ keyword and the name of the file only.

```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))
```

### Import functions from a module

We can have many functions in a file and we can import all the functions differently.

```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetay'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Import functions from a module and renaming

During importing we can rename the name of the module.

```py
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1,9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Import Builtin Modules

Like other programming languages we can also import modules by importing the file/function using the key word _import_. Lets import the common module we will use most of the time. Some of the common builtin modules _math_, _datetime_, _os_,_sys_, _random_, _statistics_, _collections_, _json_,_re_

### OS Module

Using python _os_ module it is possible to automatically perform many operating system tasks.The OS module in Python provides functions for creating, changing current working directory, and removing a directory (folder), fetching its contents, changing and identifying the current directory.

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

The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is argument passed from the command line.

```py
import sys
print(sys.argv[0], argv[1],sys.argv[2])
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
output
Welcome Asabeneh. Enjoy  30DayOfPython challenge!

# to exist syst
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
syst.path
# To know the version of python you are using
sys.version
```

### Statistics Module

The statistics module provides functions to mathematical statistics of numeric data. The popular statistical functions which are defined in this module _mean_, _median_, _mode_, _stdev_ etc.

```py
from statistics import * # importing all the statistics module
print(mean(ages))       # 22.4
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # 2.3
```

### Math Module

```py
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2
```

Now, we have imported the math module which contains lots of function which can help us to perform mathematical calculations.To check what functions the module has, you can use _help(math)_, or dir(math) and this will display the available functions in the module. If we want to import only a specific function from a module we import as follow:

```py
from math import pi
print(pi)
```

It is also possible to import multiple functions at once

```py

from math import pi, sqrt, pow, floor, ceil,log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

But if we want to import all the function in math module we can use \* .

```py
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
```

When we import we can also rename the name of the function.

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### Random Module

By now you are familiar with importing modules. Lets do another more import to be very familiar with importing. Let's import _random_ module which can gives random number between 0 and 0.9999.... The _random_ module has lots of functions but in this section we will only see _random_ and _randint_.

```py
from random import random, randint
print(random())   # it doesn't take argument and return 0 to 0.9999
print(randint(5, 20)) # it returns a random number between 5 and 20
```

## 💻 Exercises: Day 12

1. Writ a function which generates a six digit random_user_id.
   ```py
     print(random_user_id());
     '1ee33d'
   ```
2. Modify question number above . Declare a function name user_id_gen_by_user. It doesn’t take any parameter but it takes two inputs using input(). One of the input is the number of characters and the second input is the number of ids which are supposed to be generated.
   ```py
   user_id_gen_by_user()
   "kcsy2
   SMFYb
   bWmeq
   ZXOYh
   2Rgxf
   "
   user_id_gen_by_user()
   "1GCSgPLMaBAVQZ26
   YD7eFwNQKNs7qXaT
   ycArC5yrRupyG00S
   UbGxOFI7UXSWAyKN
   dIV0SSUTgAdKwStr
   "
   ```
3. Write a function name rgb_color_gen and it generates rgb colors.
   ```py
         print(rgb_color_gen())
       # rgb(125,244,255)
   ```
4. Write a function list_of_hexa_colors which return any number of hexadecimal colors in an array.
5. Write a function list_of_rgb_colors which return any number of RGB colors in an array.
   Write a function generate_colors which can generate any number of hexa or rgb colors.
   `py generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] generate_colors('hexa', 1) # '#b334ef' generate_colors('rgb', 3) # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] generate_colors('rgb', 1) # 'rgb(33,79, 176)'`
6. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
7. Write a function which returns array of seven random numbers in a range of 0-9. All the numbers must be unique.

🎉 CONGRATULATIONS ! 🎉

[<< Day 11](../11_Day/11_function.md) | [Day 13>>](../13_Day/13_list_comprehension.md)

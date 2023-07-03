<div align="center">
  <h1> 30 Days Of Python: Day 15 - Python Type Errors </h1>
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

[<< Day 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Day 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 15](#-day-15)
  - [Python Error Types](#python-error-types)
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexerror)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)

# 📘 Day 15

## Python Error Types

ពេល​យើង​សរសេរ​កូដ វា​ជា​រឿង​ធម្មតា​ដែល​យើង​ធ្វើ​ការ​វាយ​អក្សរ ឬ​កំហុស​ទូទៅ​មួយ​ចំនួន​ផ្សេង​ទៀត។ ប្រសិនបើកូដរបស់យើងមិនអាចដំណើរការបានទេ អ្នកបកប្រែ Python នឹងបង្ហាញសារមួយដែលមានមតិកែលម្អជាមួយនឹងព័ត៌មានអំពីកន្លែងដែលបញ្ហាកើតឡើង និងប្រភេទនៃកំហុស។ ពេលខ្លះ វាក៏នឹងផ្តល់ឱ្យយើងនូវការណែនាំអំពីការជួសជុលដែលអាចកើតមានផងដែរ។ ការយល់ដឹងអំពីប្រភេទផ្សេងៗនៃកំហុសនៅក្នុងភាសាសរសេរកម្មវិធីនឹងជួយយើងក្នុងការបំបាត់កំហុសកូដរបស់យើងបានយ៉ាងឆាប់រហ័ស ហើយវាក៏ធ្វើឱ្យយើងកាន់តែប្រសើរឡើងចំពោះអ្វីដែលយើងធ្វើផងដែរ។

អនុញ្ញាតឱ្យយើងមើលប្រភេទកំហុសទូទៅបំផុតម្តងមួយៗ។ ដំបូងអនុញ្ញាតឱ្យយើងបើកសែលអន្តរកម្ម Python របស់យើង។ ចូលទៅកាន់ស្ថានីយកុំព្យូទ័ររបស់អ្នក ហើយសរសេរ 'python' ។ សែលអន្តរកម្ម python នឹងត្រូវបានបើក។

### SyntaxError

**Example 1: SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

ដូចដែលអ្នកអាចឃើញ យើងបានធ្វើឱ្យមានកំហុសវាក្យសម្ព័ន្ធមួយ ដោយសារតែយើងភ្លេចបិទខ្សែអក្សរជាមួយនឹងវង់ក្រចក ហើយ Python បានណែនាំដំណោះស្រាយរួចហើយ។ អនុញ្ញាតឱ្យយើងជួសជុលវា។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

កំហុសគឺ _SyntaxError_ ។ បន្ទាប់ពីការជួសជុលកូដរបស់យើងត្រូវបានប្រតិបត្តិដោយគ្មានបញ្ហា។ អនុញ្ញាតឱ្យមើលប្រភេទកំហុសជាច្រើនទៀត។

### NameError

**Example 1: NameError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

ដូចដែលអ្នកអាចឃើញពីសារខាងលើ អាយុឈ្មោះមិនត្រូវបានកំណត់ទេ។ បាទ វាជាការពិតដែលយើងមិនបានកំណត់អថេរអាយុទេ ប៉ុន្តែយើងកំពុងព្យាយាមបោះពុម្ពវាចេញ ហាក់ដូចជាយើងបានប្រកាសវា។ ឥឡូវនេះ សូមជួសជុលវាដោយប្រកាសវា និងកំណត់តម្លៃ។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

ប្រភេទនៃកំហុសគឺ _NameError_ ។ យើងបានបំបាត់កំហុសដោយកំណត់ឈ្មោះអថេរ។

### IndexError

**Example 1: IndexError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

ក្នុងឧទាហរណ៍ខាងលើ Python បានលើកឡើង _IndexError_ ពីព្រោះបញ្ជីមានតែសន្ទស្សន៍ពី 0 ដល់ 4 ដូច្នេះវានៅក្រៅជួរ។

### ModuleNotFoundError

**Example 1: ModuleNotFoundError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

ក្នុងឧទាហរណ៍ខាងលើ ខ្ញុំបានបន្ថែម s បន្ថែមទៅគណិតវិទ្យាដោយចេតនា ហើយ _ModuleNotFoundError_ ត្រូវបានលើកឡើង។ អនុញ្ញាតឱ្យជួសជុលវាដោយយក s បន្ថែមចេញពីគណិតវិទ្យា។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

យើងបានជួសជុលវា ដូច្នេះ ចូរយើងប្រើមុខងារមួយចំនួនពីម៉ូឌុលគណិតវិទ្យា។

### AttributeError

**Example 1: AttributeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

ដូច​អ្នក​ឃើញ​ហើយ ខ្ញុំ​បាន​ធ្វើ​ខុស​ម្ដង​ទៀត! ជំនួសឱ្យ pi ខ្ញុំបានព្យាយាមហៅមុខងារ PI ពីម៉ូឌុលគណិតវិទ្យា។ វាលើកឡើងនូវកំហុសគុណលក្ខណៈ វាមានន័យថាមុខងារមិនមាននៅក្នុងម៉ូឌុលទេ។ អនុញ្ញាតឱ្យជួសជុលវាដោយការផ្លាស់ប្តូរពី PI ទៅ pi ។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

ឥឡូវនេះនៅពេលដែលយើងហៅ pi ពីម៉ូឌុលគណិតវិទ្យាយើងទទួលបានលទ្ធផល។

### KeyError

**Example 1: KeyError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

ដូចដែលអ្នកអាចឃើញមានការវាយអក្សរនៅក្នុងសោដែលប្រើដើម្បីទទួលបានតម្លៃវចនានុក្រម។ ដូច្នេះ នេះ​ជា​កំហុស​សំខាន់ ហើយ​ការ​ជួសជុល​គឺ​ត្រង់​ទៅ​មុខ។ តោះ​នាំ​គ្នា​ធ្វើ!

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

យើងបានបំបាត់កំហុស លេខកូដរបស់យើងដំណើរការ ហើយយើងទទួលបានតម្លៃ។

### TypeError

**Example 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

ក្នុងឧទាហរណ៍ខាងលើ TypeError ត្រូវបានលើកឡើង ពីព្រោះយើងមិនអាចបន្ថែមលេខទៅខ្សែអក្សរបានទេ។ ដំណោះស្រាយដំបូងគឺការបំប្លែងខ្សែអក្សរទៅជា int ឬ float ។ ដំណោះ​ស្រាយ​មួយ​ទៀត​នឹង​ត្រូវ​បំប្លែង​លេខ​ទៅ​ជា​ខ្សែ​អក្សរ (លទ្ធផល​បន្ទាប់​មក​នឹង​ជា '43')។ ចូរយើងធ្វើតាមការកែតម្រូវដំបូង។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

កំហុសត្រូវបានដកចេញ ហើយយើងទទួលបានលទ្ធផលដែលយើងរំពឹងទុក។

### ImportError

**Example 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

មិនមានមុខងារហៅថាថាមពលនៅក្នុងម៉ូឌុលគណិតវិទ្យាទេ វាមានឈ្មោះផ្សេង៖ _pow_។ តោះកែវា៖

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### ValueError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

ក្នុង​ករណី​នេះ យើង​មិន​អាច​ប្ដូរ​ខ្សែ​ដែល​បាន​ផ្ដល់​ទៅ​ជា​លេខ​បាន​ទេ ដោយសារ​អក្សរ 'a' នៅ​ក្នុង​វា។

### ZeroDivisionError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

យើងមិនអាចចែកលេខដោយសូន្យបានទេ។

យើងបានគ្របដណ្តប់មួយចំនួននៃប្រភេទកំហុស python ប្រសិនបើអ្នកចង់ពិនិត្យមើលបន្ថែមទៀតអំពីវា សូមពិនិត្យមើលឯកសារ python អំពីប្រភេទកំហុស python ។
ប្រសិនបើអ្នកពូកែអានប្រភេទ error នោះអ្នកនឹងអាចជួសជុល bugs របស់អ្នកបានលឿន ហើយអ្នកក៏នឹងក្លាយជា programmer ល្អជាងមុនផងដែរ។


🎉 CONGRATULATIONS ! 🎉

[<< Day 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Day 16 >>](../16_Day_Python_date_time/16_python_datetime.md)
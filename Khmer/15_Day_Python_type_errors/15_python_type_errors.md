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
  - [💻 Exercises: Day 15](#-exercises-day-15)

# 📘 Day 15

## Python Error Types

នៅពេលយើងសរសេរកូដវាជារឿងធម្មតាដែលយើងសរសេរពាក្យខុសឬកំហុសផ្សេងៗ ប្រសិនបើកូដរបស់យើងមិនអាចដំណើរការបាន​​​ Python នឹងបង្ហាញសារ ដែលឆ្លើយតបជាមួយនឹងព័ត៌មានអំពីកន្លែងដែលមានបញ្ហាកើតឡើង និងប្រភេទនៃកំហុស។ វាក៏អាចផ្តល់យោបល់ដល់យើងអំពីការដោះស្រាយដែលអាចធ្វើបានដែរ។ ការយល់ដឹងពីកំហុសផ្សេងៗក្នុងភាសាកម្មវិធីនឹងជួយយើងក្នុងការ debug កូដរបស់យើងឲ្យបានឆាប់រហ័សហើយវាក៏ធ្វើអោយយើងល្អជាងគេនៅក្នុងអ្វីដែលយើងធ្វើ។

សូមមើលប្រភេទកំហុសដែលទូទៅបំផុតមួយៗ។ ដំបូងយើងត្រូវបើក shell Python ចូលទៅក្នុងកុំព្យូទ័រ​ Terminal របស់អ្នក ហើយសរសេរថា "python" កញ្ចប់ Python នឹងត្រូវបើក។

### SyntaxError

**Example 1: SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: ខ្វះខាតវង់ក្រចកនៅក្នុងការហៅទៅ 'print'. តើអ្នកមានន័យថា print('hello world')?
>>>
```

ដូចដែលអ្នកអាចមើលបានយើងបានធ្វើកំហុស syntax ព្រោះយើងបានភ្លេចបិទ string ជាមួយ វង់ក្រច ហើយ Python បានបង្ហាញដំណោះស្រាយរួចហើយ សូមឱ្យយើងដោះស្រាយវា។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: ខ្វះខាតវង់ក្រចកនៅក្នុងការហៅទៅ 'print'. តើអ្នកមានន័យថា print('hello world')?
>>> print('hello world')
hello world
>>>
```

កំហុសគឺ _SyntaxError_ បន្ទាប់ពីការកែប្រែលេខកូដរបស់យើងត្រូវបានអនុវត្តដោយគ្មានបញ្ហា។ សូមមើលប្រភេទ Error បន្ថែមទៀត

### NameError

**Example 1: NameError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> print(age)
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
NameError: ឈ្មោះ 'age' មិនត្រូវបានកំណត់
>>>
```

ដូចដែលអ្នកអាចមើលឃើញពីសារខាងលើ ឈ្មោះអាយុមិនត្រូវបានកំណត់។ ពិតណាស់ យើងមិនបានកំណត់​​ age variable​ ​ទេ។ ប៉ុន្តែយើងកំពុងព្យាយាមបោះពុម្ពចេញដូចយើងបានប្រកាសវា។ ឥឡូវនេះ, យើងត្រូវដោះស្រាយវាដោយប្រកាសវា និងកំណត់តម្លៃ។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> print(age)
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
NameError: ឈ្មោះ 'age' មិនត្រូវបានកំណត់
>>> age = 25
>>> print(age)
25
>>>
```

ប្រភេទកំហុសគឺ _NameError_ ។ យើងបានដោះស្រាយកំហុសដោយកំណត់ឈ្មោះរបស់ variable ។

### IndexError

**Example 1: IndexError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
IndexError: លើសការកំណត់ក្នុងបញ្ជីបញ្ជី​
>>>
```

នៅក្នុងឧទាហរណ៍ខាងលើនេះ Python បានលើកឡើងថា _IndexError_ ដោយសារតែបញ្ជីមានត្រឹមតែកម្រិតពី 0 ដល់ 4 ដូច្នេះវានៅក្រៅកម្រិត។

### ModuleNotFoundError

**Example 1: ModuleNotFoundError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> import maths
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: គ្មានម៉ូឌុលដែលមានឈ្មោះ 'maths'
>>>
```

នៅក្នុងឧទាហរណ៍ខាងលើនេះ ខ្ញុំបានបន្ថែម s បន្ថែមទៅលើគណិតវិទ្យាដោយចេតនាហើយ _ModuleNotFoundError_ ត្រូវបានលើកឡើង។ សូមដោះស្រាយវាដោយលុប s បន្ថែមពីគណិតវិទ្យា

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> import maths
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: គ្មានម៉ូឌុលដែលមានឈ្មោះ 'maths'
>>> import math
>>>
```

យើងបានដោះស្រាយវារួចហើយ ដូច្នេះយើងត្រូវប្រើប្រាស់មុខងារខ្លះពីម៉ូឌុលគណិតវិទ្យា

### AttributeError

**Example 1: AttributeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> import maths
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: គ្មានម៉ូឌុលដែលមានឈ្មោះ 'maths'
>>> import math
>>> math.PI
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
AttributeError: ម៉ូឌុល 'math' គ្មានលក្ខណៈសម្បត្តិ 'PI'
>>>
```

ដូច ដែល អ្នក អាច មើល បាន ខ្ញុំ បាន ធ្វើ កំហុស ម្តង ទៀត! ជំនួសពី pi ខ្ញុំព្យាយាមហៅ function PI ពីម៉ូឌុលគណិតវិទ្យា វាបានលើកឡើងពីកំហុសលក្ខណៈសម្បត្តិ ដែលមានន័យថា តួនាទីនេះមិនមាននៅក្នុងម៉ូឌុល។ យើងកែវាដោយផ្លាស់ប្តូរពី PI ទៅ pi

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> import maths
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: គ្មានម៉ូឌុលដែលមានឈ្មោះ 'maths'
>>> import math
>>> math.PI
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
AttributeError: ម៉ូឌុល 'math' គ្មានលក្ខណៈសម្បត្តិ 'PI'
>>> math.pi
3.141592653589793
>>>
```

ឥឡូវនេះ, នៅពេលដែលយើងហៅ pi ពីម៉ូឌុលគណិតវិទ្យាយើងទទួលបានលទ្ធផល។

### KeyError

**Example 1: KeyError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

ដូចដែលអ្នកបានឃើញ គឺមានកំហុសក្នុង Key ដែលប្រើដើម្បីទទួលបានតម្លៃនៃ Dictionary ដូច្នេះវាជា Key Error ហើយការកែប្រែគឺងាយស្រួល។ សូមធ្វើវា!

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

យើងបានកែប្រែកំហុស, កូដរបស់យើងបានដំណើរការ ហើយយើងទទួលបានតម្លៃ។

### TypeError

**Example 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> 4 + '3'
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
TypeError: operand មិនគាំទ្រ type(s) for +: 'int' and 'str'
>>>
```

នៅក្នុងឧទាហរណ៍ខាងលើ, TypeError ត្រូវបានលើកឡើងដោយសារយើងមិនអាចបន្ថែមលេខទៅលើ string ។ ដំណោះស្រាយដំបូងគឺដើម្បីបម្លែង string ទៅ int ឬ float ។ ដំណោះស្រាយមួយទៀតគឺការបម្លែងចំនួនទៅជាខ្សែ (លទ្ធផលបន្ទាប់មកគឺ '43') ។ សូមយើងតាមដានការកែប្រែដំបូង។

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> 4 + '3'
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
TypeError: operand មិនគាំទ្រ type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

កំហុសត្រូវបានដោះស្រាយហើយយើងទទួលបានលទ្ធផលដែលយើងរំពឹងទុក។

### ImportError

**Example 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> from math import power
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ImportError: មិនអាចនាំចូលឈ្មោះ 'power' from 'math'
>>>
```

មិនមានលក្ខខណ្ឌដែលមានឈ្មោះថា power នៅក្នុងម៉ូឌុលគណិតវិទ្យាទេ វាមានឈ្មោះផ្សេងគ្នាគឺ _pow_ ។ សូមជម្រាបថា ៖

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> from math import power
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ImportError: មិនអាចនាំចូលឈ្មោះ 'power' from 'math'
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
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> int('12a')
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ValueError: អក្សរមិនត្រឹមត្រូវសម្រាប់ int() with base 10: '12a'
>>>
```

ក្នុងករណីនេះយើងមិនអាចប្ដូរ string ទៅជាលេខបានទេ ព្រោះមានអក្សរ 'a' នៅក្នុងវា

### ZeroDivisionError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
សរសេរ "help", "copyright", "credits" or "license" សម្រាប់ព័ត៌មានបន្ថែម។
>>> 1/0
កំណត់ត្រា (ការហៅចុងក្រោយបំផុត):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: ការបែងចែកដោយសូន្យ
>>>
```

យើងមិនអាចបែងចែកលេខដោយសូន្យបានទេ។

យើងបានពិនិត្យមើលប្រភេទកំហុស Python មួយចំនួន ប្រសិនបើអ្នកចង់ពិនិត្យបន្ថែមអំពីវា សូមមើលឯកសារ Python អំពីប្រភេទកំហុស Python ។
ប្រសិនបើអ្នកចេះអានប្រភេទកំហុសនោះ អ្នកនឹងអាចដោះស្រាយកំហុសរបស់អ្នកបានលឿនហើយ អ្នកក៏នឹងក្លាយជាអ្នក រៀបចំ កម្មវិធីល្អជាង ។

🌕 អ្នកពិតជាអស្ចារ្យណាស់ អ្នកបានធ្វើវាដល់ពាក់កណ្តាលនៃផ្លូវរបស់អ្នកទៅរកភាពធំធេង។ ឥឡូវធ្វើ លំ ហាត់ប្រាណ ខ្លះសម្រាប់ខួរក្បាលនិងសាច់ដុំរបស់អ្នក ។

## 💻 Exercises: Day 15

1. បើក Python Interactive Shell របស់អ្នក ហើយសាកល្បងឧទាហរណ៍ទាំងអស់ដែលពាក់ព័ន្ធនឹងផ្នែកនេះ។

🎉 សូមអបអរសាទរ ! 🎉

[<< Day 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Day 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

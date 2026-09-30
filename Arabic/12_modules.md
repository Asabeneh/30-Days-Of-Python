<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 12 - الوحدات (Modules)</h1>
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

[<< اليوم 11](./11_functions.md) | [اليوم 13 >>](./13_list_comprehension.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 12](#-اليوم-12)
  - [الوحدات (Modules)](#الوحدات-modules)
    - [ما هي الوحدة](#ما-هي-الوحدة)
    - [إنشاء وحدة](#إنشاء-وحدة)
    - [استيراد وحدة](#استيراد-وحدة)
    - [استيراد دوال من وحدة](#استيراد-دوال-من-وحدة)
    - [استيراد دوال من وحدة وإعادة تسميتها](#استيراد-دوال-من-وحدة-وإعادة-تسميتها)
  - [استيراد الوحدات المضمنة](#استيراد-الوحدات-المضمنة)
    - [وحدة OS](#وحدة-os)
    - [وحدة Sys](#وحدة-sys)
    - [وحدة Statistics](#وحدة-statistics)
    - [وحدة Math](#وحدة-math)
    - [وحدة String](#وحدة-string)
    - [وحدة Random](#وحدة-random)
  - [💻 تمارين: اليوم 12](#-تمارين-اليوم-12)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 12

## الوحدات (Modules)

### ما هي الوحدة

الوحدة (module) هي ملف يحتوي على مجموعة من الأكواد أو مجموعة من الدوال التي يمكن تضمينها في تطبيق. يمكن أن تكون الوحدة ملفًا يحتوي على متغير واحد أو دالة أو قاعدة كود كبيرة.

### إنشاء وحدة

لإنشاء وحدة نكتب أكوادنا في سكريبت بايثون ونحفظه كملف .py. أنشئ ملفًا باسم mymodule.py داخل مجلد مشروعك. دعنا نكتب بعض الكود في هذا الملف.

```py
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

أنشئ ملف main.py في دليل مشروعك واستورد ملف mymodule.py.

### استيراد وحدة

لاستيراد الملف نستخدم الكلمة المفتاحية 'import' واسم الملف فقط.

```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### استيراد دوال من وحدة

يمكن أن يكون لدينا العديد من الدوال في ملف ويمكننا استيراد كل الدوال بشكل مختلف.

```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### استيراد دوال من وحدة وإعادة تسميتها

أثناء الاستيراد يمكننا إعادة تسمية اسم الوحدة.

```py
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## استيراد الوحدات المضمنة

مثل لغات البرمجة الأخرى يمكننا أيضًا استيراد الوحدات باستيراد الملف/الدالة باستخدام الكلمة المفتاحية 'import'. دعنا نستورد الوحدة الشائعة التي سنستخدمها في معظم الأوقات. بعض الوحدات المضمنة الشائعة: 'math'، 'datetime'، 'os'، 'sys'، 'random'، 'statistics'، 'collections'، 'json'، 're'

### وحدة OS

باستخدام وحدة 'os' في بايثون يمكن تنفيذ العديد من مهام نظام التشغيل تلقائيًا. توفر وحدة OS في بايثون دوالًا لإنشاء وتغيير دليل العمل الحالي، وإزالة دليل (مجلد)، وجلب محتوياته، وتغيير وتحديد الدليل الحالي.

```py
# استيراد الوحدة
import os
# إنشاء دليل
os.mkdir('directory_name')
# تغيير الدليل الحالي
os.chdir('path')
# الحصول على دليل العمل الحالي
os.getcwd()
# إزالة دليل
os.rmdir()
```

### وحدة Sys

توفر وحدة sys دوالًا ومتغيرات تستخدم للتعامل مع أجزاء مختلفة من بيئة تشغيل بايثون. دالة sys.argv تعيد قائمة من وسائط سطر الأوامر الممررة إلى سكريبت بايثون. العنصر في الفهرس 0 في هذه القائمة هو دائمًا اسم السكريبت، وفي الفهرس 1 هو الوسيطة الممررة من سطر الأوامر.

مثال على ملف script.py:

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # هذا السطر سيطبع: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

الآن للتحقق من كيفية عمل هذا السكريبت كتبت في سطر الأوامر:

```sh
python script.py Asabeneh 30DaysOfPython
```

النتيجة:

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge!
```

بعض أوامر sys المفيدة:

```py
# للخروج من sys
sys.exit()
# لمعرفة أكبر متغير عدد صحيح يمكنه استيعابه
sys.maxsize
# لمعرفة مسار البيئة
sys.path
# لمعرفة إصدار بايثون الذي تستخدمه
sys.version
```

### وحدة Statistics

توفر وحدة statistics دوالًا للإحصاء الرياضي للبيانات الرقمية. الدوال الإحصائية الشائعة المعرفة في هذه الوحدة: 'mean'، 'median'، 'mode'، 'stdev' إلخ.

```py
from statistics import * # استيراد جميع وحدات الإحصاء
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### وحدة Math

وحدة تحتوي على العديد من العمليات والثوابت الرياضية.

```py
import math
print(math.pi)           # 3.141592653589793، ثابت pi
print(math.sqrt(2))      # 1.4142135623730951، الجذر التربيعي
print(math.pow(2, 3))    # 8.0، دالة الأس
print(math.floor(9.81))  # 9، تقريب إلى الأدنى
print(math.ceil(9.81))   # 10، تقريب إلى الأعلى
print(math.log10(100))   # 2، لوغاريتم بالأساس 10
```

الآن، استوردنا وحدة *math* التي تحتوي على الكثير من الدوال التي يمكن أن تساعدنا في إجراء العمليات الحسابية. للتحقق من الدوال التي تحتويها الوحدة، يمكننا استخدام _help(math)_، أو _dir(math)_. سيعرض هذا الدوال المتاحة في الوحدة. إذا أردنا استيراد دالة محددة فقط من الوحدة نستوردها كما يلي:

```py
from math import pi
print(pi)
```

من الممكن أيضًا استيراد عدة دوال دفعة واحدة

```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

ولكن إذا أردنا استيراد جميع الدوال في وحدة math يمكننا استخدام \* .

```py
from math import *
print(pi)                  # 3.141592653589793، ثابت pi
print(sqrt(2))             # 1.4142135623730951، الجذر التربيعي
print(pow(2, 3))           # 8.0، الأس
print(floor(9.81))         # 9، تقريب إلى الأدنى
print(ceil(9.81))          # 10، تقريب إلى الأعلى
print(math.log10(100))     # 2
```

عند الاستيراد يمكننا أيضًا إعادة تسمية اسم الدالة.

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### وحدة String

وحدة string وحدة مفيدة للعديد من الأغراض. المثال أدناه يوضح بعض استخدامات وحدة string.

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### وحدة Random

حتى الآن أصبحت معتادًا على استيراد الوحدات. دعنا نقوم باستيراد آخر للتعرف عليها أكثر. دعنا نستورد وحدة 'random' التي تعطينا رقمًا عشوائيًا بين 0 و 0.9999.... تحتوي وحدة 'random' على الكثير من الدوال لكن في هذا القسم سنستخدم فقط _random_ و 'randint'.

```py
from random import random, randint
print(random())   # لا تأخذ أي وسيطات؛ تعيد قيمة بين 0 و 0.9999
print(randint(5, 20)) # تعيد عددًا صحيحًا عشوائيًا بين [5, 20] شاملًا
```

🌕 أنت تتقدم بعيدًا. استمر! لقد أكملت للتو تحديات اليوم الثاني عشر وأنت على بعد 12 خطوة في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 12

### تمارين: المستوى 1

1. اكتب دالة تولد random_user_id من ستة أرقام/أحرف.
   ```py
     print(random_user_id())
     '1ee33d'
   ```
2. عدّل المهمة السابقة. أعلن دالة باسم user_id_gen_by_user. لا تأخذ أي بارامترات لكنها تأخذ مدخلين باستخدام input(). أحد المدخلات هو عدد الأحرف والمدخل الثاني هو عدد المعرفات التي يفترض توليدها.

```py
print(user_id_gen_by_user()) # إدخال المستخدم: 5 5
#المخرجات:
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

3. اكتب دالة باسم rgb_color_gen. ستولد ألوان rgb (3 قيم تتراوح من 0 إلى 255 لكل منها).

```py
print(rgb_color_gen())
# rgb(125,244,255) - يجب أن يكون المخرج في هذا الشكل
```

### تمارين: المستوى 2

1. اكتب دالة list_of_hexa_colors تعيد أي عدد من الألوان الست عشرية في مصفوفة (ستة أرقام ست عشرية مكتوبة بعد #. يتكون النظام العددي الست عشري من 16 رمزًا، 0-9 وأول 6 أحرف من الأبجدية، a-f. تحقق من المهمة 6 لأمثلة المخرجات).
2. اكتب دالة list_of_rgb_colors تعيد أي عدد من ألوان RGB في مصفوفة.
3. اكتب دالة generate_colors يمكنها توليد أي عدد من الألوان الست عشرية أو rgb.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

### تمارين: المستوى 3

1. استدعِ دالتك shuffle_list، تأخذ قائمة كبارامتر وتعيد قائمة مخففة
2. اكتب دالة تعيد مصفوفة من سبعة أرقام عشوائية في نطاق 0-9. يجب أن تكون كل الأرقام فريدة.

🎉 مبروك! 🎉

[<< اليوم 11](./11_functions.md) | [اليوم 13 >>](./13_list_comprehension.md)
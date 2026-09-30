<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 10 - الحلقات التكرارية (Loops)</h1>
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

[<< اليوم 9](./09_conditionals.md) | [اليوم 11 >>](./11_functions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 10](#-اليوم-10)
  - [الحلقات التكرارية (Loops)](#الحلقات-التكرارية-loops)
    - [حلقة While](#حلقة-while)
    - [Break و Continue - الجزء 1](#break-و-continue---الجزء-1)
    - [حلقة For](#حلقة-for)
    - [Break و Continue - الجزء 2](#break-و-continue---الجزء-2)
    - [دالة Range](#دالة-range)
    - [حلقة For المتداخلة](#حلقة-for-المتداخلة)
    - [For مع Else](#for-مع-else)
    - [Pass](#pass)
  - [💻 تمارين: اليوم 10](#-تمارين-اليوم-10)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 10

## الحلقات التكرارية (Loops)

الحياة مليئة بالروتين. في البرمجة نقوم أيضًا بالكثير من المهام المتكررة. للتعامل مع المهام المتكررة تستخدم لغات البرمجة الحلقات (loops). توفر لغة برمجة بايثون أيضًا نوعين من الحلقات:

1. حلقة while
2. حلقة for

### حلقة While

نستخدم الكلمة المحجوزة 'while' لإنشاء حلقة while. تُستخدم لتنفيذ كتلة من العبارات بشكل متكرر حتى يتم استيفاء شرط معين. عندما يصبح الشرط خاطئًا، ستستمر أسطر الكود بعد الحلقة في التنفيذ.

```py
  # الصيغة
while condition:
    code goes here
```

**مثال:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#يطبع من 0 إلى 4
```

في حلقة while أعلاه، يصبح الشرط خاطئًا عندما يكون count يساوي 5. عندها تتوقف الحلقة.
إذا كنا مهتمين بتشغيل كتلة من الكود مرة واحدة عندما لا يكون الشرط صحيحًا بعد الآن، يمكننا استخدام 'else'.

```py
  # الصيغة
while condition:
    code goes here
else:
    code goes here
```

**مثال:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

شرط الحلقة أعلاه سيكون خاطئًا عندما يكون count يساوي 5 وتتوقف الحلقة، ويبدأ التنفيذ من عبارة else. كنتيجة لذلك ستتم طباعة 5.

### Break و Continue - الجزء 1

- Break: نستخدم break عندما نرغب في الخروج أو إيقاف الحلقة.

```py
# الصيغة
while condition:
    code goes here
    if another_condition:
        break
```

**مثال:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

حلقة while أعلاه تطبع فقط 0, 1, 2، ولكن عندما تصل إلى 3 تتوقف.

- Continue: بعبارة continue يمكننا تخطي التكرار الحالي، والاستمرار مع التالي:

```py
  # الصيغة
while condition:
    code goes here
    if another_condition:
        continue
```

**مثال:**

```py
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

حلقة while أعلاه تطبع فقط 0, 1, 2 و 4 (تتخطى 3).

### حلقة For

تُستخدم الكلمة المفتاحية 'for' لإنشاء حلقة for، مشابهة للغات البرمجة الأخرى، ولكن مع بعض الاختلافات في الصياغة. تُستخدم الحلقة للتكرار على متابعة (sequence) (أي قائمة أو توبل أو قاموس أو مجموعة أو نص).

- استخدام حلقة For على قائمة

```py
# الصيغة
for iterator in lst:
    code goes here
```

**مثال:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number هو اسم مؤقت للإشارة إلى عناصر القائمة، صالح فقط داخل هذه الحلقة
    print(number)       # ستتم طباعة الأرقام سطرًا بسطر، من 0 إلى 5
```

- استخدام حلقة For على نص

```py
# الصيغة
for iterator in string:
    code goes here
```

**مثال:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- استخدام حلقة For على توبل

```py
# الصيغة
for iterator in tpl:
    code goes here
```

**مثال:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- حلقة For مع قاموس
  التكرار عبر قاموس يعطيك مفاتيح القاموس.

```py
  # الصيغة
for iterator in dct:
    code goes here
```

**مثال:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # بهذه الطريقة نحصل على كل من المفاتيح والقيم مطبوعة
```

- استخدام حلقة For مع مجموعة (set)

```py
# الصيغة
for iterator in st:
    code goes here
```

**مثال:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break و Continue - الجزء 2

تذكير قصير:
'Break': نستخدم break عندما نرغب في إيقاف حلقتنا قبل اكتمالها.

```py
# الصيغة
for iterator in sequence:
    code goes here
    if condition:
        break
```

**مثال:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

في المثال أعلاه، تتوقف الحلقة عندما تصل إلى 3.

Continue: نستخدم continue عندما نرغب في تخطي بعض الخطوات في تكرار الحلقة.

```py
  # الصيغة
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**مثال:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # للشروط المختصرة تحتاج كلاً من عبارتي if و else
print('outside the loop')
```

في المثال أعلاه، إذا كان الرقم يساوي 3، يتم تخطي الخطوة _بعد_ الشرط (ولكن داخل الحلقة) ويستمر تنفيذ الحلقة إذا بقيت أي تكرارات.

### دالة Range

تُستخدم دالة 'range()' لإرجاع قائمة من الأرقام. تأخذ 'range(start, end, step)' ثلاث بارامترات: البدء والانتهاء والزيادة. بشكل افتراضي تبدأ من 0 والزيادة 1. تسلسل range يحتاج ما لا يقل عن وسيطة واحدة (end).
إنشاء تسلسلات باستخدام range

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # وسيطتان تشيران إلى بداية ونهاية التسلسل، الخطوة مضبوطة على الافتراضي 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# للتكرار للخلف من البداية إلى النهاية
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

```py
# الصيغة
for iterator in range(start, end, step):
```

**مثال:**

```py
for number in range(11):
    print(number)   # يطبع 0 إلى 10، دون تضمين 11
```

### حلقة For المتداخلة

يمكننا كتابة حلقات داخل حلقة.

```py
# الصيغة
for x in y:
    for t in x:
        print(t)
```

**مثال:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For مع Else

إذا أردنا تنفيذ رسالة ما عندما تنتهي الحلقة، نستخدم else.

```py
# الصيغة
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**مثال:**

```py
for number in range(11):
    print(number)   # يطبع 0 إلى 10، دون تضمين 11
else:
    print('The loop stops at', number)
```

### Pass

في بايثون عندما تكون العبارة مطلوبة (بعد النقطتين)، لكننا لا نرغب في تنفيذ أي كود هناك، يمكننا كتابة كلمة 'pass' لتجنب الأخطاء. يمكننا أيضًا استخدامها كمكان مؤقت، لعبارات مستقبلية.

**مثال:**

```py
for number in range(6):
    pass
```

🌕 لقد حققت إنجازًا كبيرًا، أنت لا يمكن إيقافك. استمر! لقد أكملت للتو تحديات اليوم العاشر وأنت على بعد 10 خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 10

### تمارين: المستوى 1

1. كرر من 0 إلى 10 باستخدام حلقة for، وقم بنفس الشيء باستخدام حلقة while.
2. كرر من 10 إلى 0 باستخدام حلقة for، وقم بنفس الشيء باستخدام حلقة while.
3. اكتب حلقة تقوم بسبع استدعاءات للدالة print()، حتى نحصل في المخرجات على المثلث التالي:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. استخدم حلقات متداخلة لإنشاء ما يلي:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. اطبع النمط التالي:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. كرر عبر القائمة ['Python', 'Numpy','Pandas','Django', 'Flask'] باستخدام حلقة for واطبع العناصر.
7. استخدم حلقة for للتكرار من 0 إلى 100 واطبع الأرقام الزوجية فقط
8. استخدم حلقة for للتكرار من 0 إلى 100 واطبع الأرقام الفردية فقط

### تمارين: المستوى 2

1. استخدم حلقة for للتكرار من 0 إلى 100 واطبع مجموع كل الأرقام.

```sh
The sum of all numbers is 5050.
```

2. استخدم حلقة for للتكرار من 0 إلى 100 واطبع مجموع الأرقام الزوجية ومجموع الأرقام الفردية.

   ```sh
   The sum of all evens is 2550. And the sum of all odds is 2500.
   ```

### تمارين: المستوى 3

1. انتقل إلى مجلد data واستخدم ملف [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py). قم بالتكرار عبر الدول واستخرج جميع الدول التي تحتوي على كلمة 'land'.
2. هذه قائمة فواكه ['banana', 'orange', 'mango', 'lemon'] اعكس الترتيب باستخدام حلقة.
3. انتقل إلى مجلد data واستخدم ملف [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
   1. ما العدد الإجمالي للغات في البيانات
   2. جد اللغات العشر الأكثر تحدثًا من البيانات
   3. جد الدول العشرة الأكثر سكانًا في العالم

🎉 مبروك! 🎉

[<< اليوم 9](./09_conditionals.md) | [اليوم 11 >>](./11_functions.md)
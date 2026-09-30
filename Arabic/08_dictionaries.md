<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 8 - القواميس (Dictionaries)</h1>
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

[<< اليوم 7](./07_sets.md) | [اليوم 9 >>](./09_conditionals.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 8](#-اليوم-8)
  - [القواميس (Dictionaries)](#القواميس-dictionaries)
    - [إنشاء قاموس](#إنشاء-قاموس)
    - [طول القاموس](#طول-القاموس)
    - [الوصول إلى عناصر القاموس](#الوصول-إلى-عناصر-القاموس)
    - [إضافة عناصر إلى قاموس](#إضافة-عناصر-إلى-قاموس)
    - [تعديل عناصر في قاموس](#تعديل-عناصر-في-قاموس)
    - [التحقق من المفاتيح في قاموس](#التحقق-من-المفاتيح-في-قاموس)
    - [إزالة أزواج المفتاح والقيمة من قاموس](#إزالة-أزواج-المفتاح-والقيمة-من-قاموس)
    - [تحويل القاموس إلى قائمة من العناصر](#تحويل-القاموس-إلى-قائمة-من-العناصر)
    - [مسح قاموس](#مسح-قاموس)
    - [حذف قاموس](#حذف-قاموس)
    - [نسخ قاموس](#نسخ-قاموس)
    - [الحصول على مفاتيح القاموس كقائمة](#الحصول-على-مفاتيح-القاموس-كقائمة)
    - [الحصول على قيم القاموس كقائمة](#الحصول-على-قيم-القاموس-كقائمة)
  - [💻 تمارين: اليوم 8](#-تمارين-اليوم-8)

# 📘 اليوم 8

## القواميس (Dictionaries)

القاموس (dictionary) هو مجموعة من نوع بيانات غير مرتب، وقابل للتغيير (mutable)، ومقترن (key: value).

### إنشاء قاموس

لإنشاء قاموس نستخدم الأقواس المعقوفة {} أو الدالة المضمنة 'dict()'.

```py
# الصيغة
empty_dict = {}
# قاموس بقيم بيانات
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
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
```

يُظهر القاموس أعلاه أن القيمة يمكن أن تكون من أي نوع بيانات: نص، قيمة منطقية، قائمة، توبل، مجموعة أو قاموس.

### طول القاموس

يتحقق من عدد أزواج 'key: value' في القاموس.

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**مثال:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

```

### الوصول إلى عناصر القاموس

يمكننا الوصول إلى عناصر القاموس بالإشارة إلى اسم المفتاح الخاص بها.

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
```

الوصول إلى عنصر باسم المفتاح يثير خطأً إذا كان المفتاح غير موجود. لتجنب هذا الخطأ يجب أولاً التحقق مما إذا كان المفتاح موجودًا أو يمكننا استخدام طريقة 'get'. طريقة get تعيد None، وهو نوع بيانات كائن NoneType، إذا كان المفتاح غير موجود.

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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### إضافة عناصر إلى قاموس

يمكننا إضافة أزواج مفتاح وقيمة جديدة إلى قاموس

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

### تعديل عناصر في قاموس

يمكننا تعديل عناصر في قاموس

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### التحقق من المفاتيح في قاموس

نستخدم عامل 'in' للتحقق مما إذا كان مفتاح موجودًا في قاموس

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### إزالة أزواج المفتاح والقيمة من قاموس

- _pop(key)_: يزيل العنصر باسم المفتاح المحدد:
- 'popitem()': يزيل آخر عنصر
- 'del': يزيل عنصرًا باسم المفتاح المحدد

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # يزيل عنصر key1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # يزيل آخر عنصر
del dct['key2'] # يزيل عنصر key2
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
person.pop('first_name')        # يزيل عنصر الاسم الأول
person.popitem()                # يزيل عنصر العنوان
del person['is_married']        # يزيل عنصر is_married
```

### تحويل القاموس إلى قائمة من العناصر

طريقة 'items()' تحول القاموس إلى قائمة من التوبلات.

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### مسح قاموس

إذا لم نرغب في عناصر القاموس يمكننا مسحها باستخدام طريقة 'clear()'

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### حذف قاموس

إذا لم نستخدم القاموس يمكننا حذفه بالكامل

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### نسخ قاموس

يمكننا نسخ قاموس باستخدام طريقة 'copy()'. باستخدام copy يمكننا تجنب تعديل القاموس الأصلي.

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### الحصول على مفاتيح القاموس كقائمة

طريقة 'keys()' تعطينا جميع مفاتيح القاموس كقائمة.

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### الحصول على قيم القاموس كقائمة

طريقة 'values' تعطينا جميع قيم القاموس كقائمة.

```py
# الصيغة
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 أنت مذهل. الآن، أنت مشحون بقوة القواميس. لقد أكملت للتو تحديات اليوم الثامن وأنت على بعد 8 خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 8

1. أنشئ قاموسًا فارغًا اسمه dog
2. أضف name، color، breed، legs، age إلى قاموس dog
3. أنشئ قاموس student وأضف first_name، last_name، gender، age، marital status، skills، country، city و address كمفاتيح للقاموس
4. احصل على طول قاموس student
5. احصل على قيمة skills وتحقق من نوع البيانات، يجب أن تكون قائمة
6. عدّل قيم skills بإضافة مهارة أو مهارتين
7. احصل على مفاتيح القاموس كقائمة
8. احصل على قيم القاموس كقائمة
9. حوّل القاموس إلى قائمة من التوبلات باستخدام طريقة 'items()'
10. احذف أحد العناصر من القاموس
11. احذف أحد القواميس

🎉 مبروك! 🎉

[<< اليوم 7](./07_sets.md) | [اليوم 9 >>](./09_conditionals.md)
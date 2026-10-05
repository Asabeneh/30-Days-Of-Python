<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 8 — ڈکشنریز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../08_Day_Dictionaries/08_dictionaries.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 7](./07_sets.md) | [فہرست](./readme.md) | [اگلا دن: 9](./09_conditionals.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 8](#day-8-section-1)
  - [ڈکشنریز](#day-8-section-2)
    - [ڈکشنری بنانا](#day-8-section-3)
    - [ڈکشنری کی لمبائی](#day-8-section-4)
    - [ڈکشنری کے عناصر تک رسائی](#day-8-section-5)
    - [ڈکشنری میں عناصر شامل کرنا](#day-8-section-6)
    - [ڈکشنری کے عناصر بدلنا](#day-8-section-7)
    - [کلید کی موجودگی جانچنا](#day-8-section-8)
    - [کلید اور قدر کے جوڑے ہٹانا](#day-8-section-9)
    - [ڈکشنری کے جوڑے حاصل کرنا](#day-8-section-10)
    - [ڈکشنری خالی کرنا](#day-8-section-11)
    - [ڈکشنری حذف کرنا](#day-8-section-12)
    - [ڈکشنری کی نقل بنانا](#day-8-section-13)
    - [ڈکشنری کی کلیدیں حاصل کرنا](#day-8-section-14)
    - [ڈکشنری کی قدریں حاصل کرنا](#day-8-section-15)
  - [💻 مشقیں — دن 8](#day-8-section-16)

<a id="day-8-section-1"></a>

# 📘 دن 8

<a id="day-8-section-2"></a>

## ڈکشنریز

ڈکشنری کلید اور قدر (`key: value`) کے جوڑوں کا قابلِ تبدیلی مجموعہ ہے۔ اصل متن اسے غیر مرتب کہتا ہے؛ پائتھن 3.7 اور بعد میں اندراج کی ترتیب برقرار رہتی ہے۔

<a id="day-8-section-3"></a>

### ڈکشنری بنانا

گھنگریالی قوسین `{}` یا بلٹ اِن `dict()` استعمال کریں۔

<div dir="ltr">

```py
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

</div>

**مثال:**

<div dir="ltr">

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

</div>

قدر کسی بھی قسم کی ہو سکتی ہے، مثلاً سٹرنگ، بولین، لسٹ، ٹپل، سیٹ یا دوسری ڈکشنری۔

<a id="day-8-section-4"></a>

### ڈکشنری کی لمبائی

لمبائی سے کلید اور قدر کے جوڑوں کی تعداد معلوم ہوتی ہے۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

</div>

**مثال:**

<div dir="ltr">

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

</div>

<a id="day-8-section-5"></a>

### ڈکشنری کے عناصر تک رسائی

کلید کے نام سے متعلقہ قدر حاصل کریں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
```

</div>

**مثال:**

<div dir="ltr">

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

</div>

مربع قوسین میں ایسی کلید دیں جو موجود نہ ہو تو خرابی آتی ہے۔ پہلے موجودگی جانچیں یا `get()` استعمال کریں۔ کلید نہ ملنے پر `get()` عموماً `None` دیتا ہے، جس کی قسم `NoneType` ہے۔

<div dir="ltr">

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

</div>

<a id="day-8-section-6"></a>

### ڈکشنری میں عناصر شامل کرنا

کلید اور قدر کا نیا جوڑا شامل کیا جا سکتا ہے۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

</div>

**مثال:**

<div dir="ltr">

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

</div>

<a id="day-8-section-7"></a>

### ڈکشنری کے عناصر بدلنا

موجودہ کلید کی قدر تبدیل کر سکتے ہیں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
```

</div>

**مثال:**

<div dir="ltr">

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

</div>

<a id="day-8-section-8"></a>

### کلید کی موجودگی جانچنا

`in` سے جانچیں کہ ڈکشنری میں کلید موجود ہے یا نہیں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

</div>

<a id="day-8-section-9"></a>

### کلید اور قدر کے جوڑے ہٹانا

- `pop(key)`: مخصوص کلید کا عنصر ہٹاتا ہے۔
- `popitem()`: آخری شامل کردہ جوڑا ہٹاتا ہے۔
- `del`: مخصوص کلید کا عنصر حذف کرتا ہے۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
```

</div>

**مثال:**

<div dir="ltr">

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
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item
```

</div>

<a id="day-8-section-10"></a>

### ڈکشنری کے جوڑے حاصل کرنا

`items()` کلید اور قدر کے ٹپلز کا ایک view دیتا ہے۔ پائتھن 3 میں لسٹ چاہیے تو `list(dictionary.items())` استعمال کریں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

</div>

<a id="day-8-section-11"></a>

### ڈکشنری خالی کرنا

تمام جوڑے ہٹانے کے لیے `clear()` استعمال کریں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

</div>

<a id="day-8-section-12"></a>

### ڈکشنری حذف کرنا

ضرورت نہ ہو تو ڈکشنری کا متغیر حذف کر سکتے ہیں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

</div>

<a id="day-8-section-13"></a>

### ڈکشنری کی نقل بنانا

`copy()` سطحی نقل بناتا ہے، تاکہ اوپری سطح کے جوڑوں میں تبدیلی اصل ڈکشنری کو نہ بدلے۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

</div>

<a id="day-8-section-14"></a>

### ڈکشنری کی کلیدیں حاصل کرنا

`keys()` تمام کلیدوں کا view دیتا ہے۔ لسٹ کے لیے اسے `list()` میں دیں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

</div>

<a id="day-8-section-15"></a>

### ڈکشنری کی قدریں حاصل کرنا

`values()` تمام قدروں کا view دیتا ہے۔ لسٹ کے لیے اسے `list()` میں دیں۔

<div dir="ltr">

```py
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

</div>

🌕 آپ نے آٹھویں دن کا چیلنج مکمل کر لیا! اب ڈکشنریز کی مشق کریں۔

<a id="day-8-section-16"></a>

## 💻 مشقیں — دن 8

1. `dog` نام کی خالی ڈکشنری بنائیں۔
2. اس میں `name`، `color`، `breed`، `legs` اور `age` شامل کریں۔
3. طالب علم کی ڈکشنری بنائیں جس میں `first_name`، `last_name`، `gender`، `age`، `is_married` (ازدواجی حیثیت)، `skills`، `country`، `city` اور `address` کی کلیدیں ہوں۔
4. اس کی لمبائی معلوم کریں۔
5. `skills` کی قدر اور قسم جانچیں؛ یہ لسٹ ہونی چاہیے۔
6. ایک یا دو نئی مہارتیں شامل کریں۔
7. کلیدوں کی لسٹ حاصل کریں۔
8. قدروں کی لسٹ حاصل کریں۔
9. `items()` اور `list()` سے جوڑوں کے ٹپلز کی لسٹ بنائیں۔
10. ایک عنصر حذف کریں۔
11. ایک ڈکشنری کا متغیر حذف کریں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 7](./07_sets.md) | [فہرست](./readme.md) | [اگلا دن: 9](./09_conditionals.md)

</div>

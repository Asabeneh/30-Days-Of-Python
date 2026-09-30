<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 17 - معالجة الاستثناءات</h1>
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

[<< اليوم 16](./16_python_datetime.md) | [اليوم 18 >>](./18_regular_expressions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 17](#-اليوم-17)
  - [معالجة الاستثناءات](#معالجة-الاستثناءات)
  - [التعبئة وفك التعبئة للوسائط في بايثون](#التعبئة-وفك-التعبئة-للوسائط-في-بايثون)
    - [فك التعبئة](#فك-التعبئة)
      - [فك تعبئة القوائم](#فك-تعبئة-القوائم)
      - [فك تعبئة القواميس](#فك-تعبئة-القواميس)
    - [التعبئة](#التعبئة)
      - [تعبئة القوائم](#تعبئة-القوائم)
      - [تعبئة القواميس](#تعبئة-القواميس)
  - [الانتشار في بايثون](#الانتشار-في-بايثون)
  - [التعداد](#التعداد)
  - [الدمج](#الدمج)
  - [💻 تمارين: اليوم 17](#-تمارين-اليوم-17)

# 📘 اليوم 17

## معالجة الاستثناءات

تستخدم بايثون كتل 'try' و 'except' للتعامل مع الأخطاء بلباقة. معالجة الأخطاء بلباقة هو مبدأ برمجي بسيط - بحيث يكتشف البرنامج حالة خطأ ويتعامل معها بطريقة محكومة ومدروسة. غالبًا ما يطبع البرنامج رسالة خطأ وصفية إلى الطرفية أو السجل كجزء من هذه المعالجة، وهذا يجعل تطبيقنا أكثر متانة. سبب الاستثناء غالبًا ما يكون خارجيًا للبرنامج نفسه. من أمثلة الاستثناءات: إدخال غير صحيح، اسم ملف خاطئ، عدم إمكانية العثور على ملف، أو جهاز إدخال/إخراج معطل. معالجة الأخطاء بلباقة تمنع تطبيقاتنا من التعطل.

لقد غطينا أنواع أخطاء بايثون المختلفة في القسم السابق. إذا استخدمنا كتل 'try' و 'except' في برنامجنا، فلن تُثار أخطاء في تلك الكتل.

![Try and Except](../images/try_except.png)

```py
try:
    كود في هذه الكتلة إذا سارت الأمور جيدًا
except:
    كود في هذه الكتلة يعمل إذا سارت الأمور بشكل خاطئ
```

**مثال:**

```py
try:
    print(10 + '5')
except:
    print('شيء ما حدث بشكل خاطئ')
```

في المثال أعلاه، المعامل الثاني هو نص. يمكننا تحويله إلى 'float' أو 'int' لإضافته إلى الرقم ليجعل الأمر يعمل. لكن دون أي تغييرات، سيتم تنفيذ الكتلة الثانية، كتلة 'except'.

**مثال:**

```py
try:
    name = input('أدخل اسمك:')
    year_born = input('السنة التي وُلدت فيها:')
    age = 2019 - year_born
    print(f'أنت {name}. وعمرك {age}.')
except:
    print('شيء ما حدث بشكل خاطئ')
```

```sh
شيء ما حدث بشكل خاطئ
```

في المثال أعلاه، ستعمل كتلة الاستثناء ولا نعرف بالضبط المشكلة. لتحليل المشكلة، يمكننا استخدام أنواع الأخطاء المختلفة مع 'except'.

في المثال التالي، سيعالج الخطأ وسيخبرنا أيضًا بنوع الخطأ المُثار.

```py
try:
    name = input('أدخل اسمك:')
    year_born = input('السنة التي وُلدت فيها:')
    age = 2019 - year_born
    print(f'أنت {name}. وعمرك {age}.')
except TypeError:
    print('حدث خطأ في النوع')
except ValueError:
    print('حدث خطأ في القيمة')
except ZeroDivisionError:
    print('حدث خطأ القسمة على صفر')
```

```sh
أدخل اسمك:Asabeneh
السنة التي وُلدت فيها:1920
حدث خطأ في النوع
```

في الكود أعلاه الناتج سيكون 'TypeError'.
الآن، دعنا نضيف كتلة إضافية:

```py
try:
    name = input('أدخل اسمك:')
    year_born = input('السنة التي وُلدت فيها:')
    age = 2019 - int(year_born)
    print(f'أنت {name}. وعمرك {age}.')
except TypeError:
    print('حدث خطأ في النوع')
except ValueError:
    print('حدث خطأ في القيمة')
except ZeroDivisionError:
    print('حدث خطأ القسمة على صفر')
else:
    print('عادةً أنا أعمل مع كتلة try')
finally:
    print('أنا أعمل دائمًا.')
```

```sh
أدخل اسمك:Asabeneh
السنة التي وُلدت فيها:1920
أنت Asabeneh. وعمرك 99.
عادةً أنا أعمل مع كتلة try
أنا أعمل دائمًا.
```

يمكن أيضًا اختصار الكود أعلاه كما يلي:

```py
try:
    name = input('أدخل اسمك:')
    year_born = input('السنة التي وُلدت فيها:')
    age = 2019 - int(year_born)
    print(f'أنت {name}. وعمرك {age}.')
except Exception as e:
    print(e)

```

## التعبئة وفك التعبئة للوسائط في بايثون

نستخدم عاملين:

- \* للتوبل (tuples)
- \*\* للقواميس (dictionaries)

لنأخذ مثالًا أدناه. تأخذ الدالة فقط وسائط لكن لدينا قائمة. يمكننا فك تعبئة القائمة وتحويلها إلى وسائط.

### فك التعبئة

#### فك تعبئة القوائم

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

عند تشغيل هذا الكود، فإنه يثير خطأ، لأن هذه الدالة تأخذ أرقامًا (وليس قائمة) كوسائط. دعنا نفك تعبئة القائمة.

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

يمكننا أيضًا استخدام فك التعبئة في الدالة المضمنة 'range' التي تتوقع بداية ونهاية.

```py
numbers = range(2, 7)  # استدعاء عادي بوسائط منفصلة
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # استدعاء بوسائط مفكوكة من قائمة
print(numbers)      # [2, 3, 4, 5,6]

```

يمكن أيضًا فك تعبئة قائمة أو توبل هكذا:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### فك تعبئة القواميس

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} يعيش في {country}, {city}. عمره {age} سنة.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh يعيش في Finland, Helsinki. عمره 250 سنة.
```

### التعبئة

أحيانًا لا نعرف مسبقًا كم عدد الوسائط التي يجب تمريرها إلى دالة بايثون. يمكننا استخدام طريقة التعبئة للسماح لدالتنا بأخذ عدد غير محدود أو عدد عشوائي من الوسائط.

### تعبئة القوائم

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### تعبئة القواميس

```py
def packing_person_info(**kwargs):
    # تحقق من نوع kwargs وهو نوع قاموس
    # print(type(kwargs))
    # طباعة عناصر القاموس
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

## الانتشار في بايثون

مثل 'JavaScript'، الانتشار ممكن في بايثون. دعنا نتحقق منه في مثال أدناه:

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## التعداد

إذا كنا مهتمين بفهرس قائمة، فإننا نستخدم الدالة المضمنة 'enumerate' للحصول على فهرس كل عنصر في القائمة.

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'تم العثور على الدولة {i} في الفهرس {index}')
```

```sh
تم العثور على الدولة Finland في الفهرس 0.
```

## الدمج

أحيانًا نرغب في دمج القوائم أثناء التكرار عبرها. انظر المثال أدناه:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

🌕 أنت مصمم. أنت متقدم بـ 17 خطوة في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 17

1. `names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']`. فك تعبئة أول خمس دول وخزّنها في متغير 'nordic_countries'، وخزّن 'Estonia' و 'Russia' في 'es' و 'ru' على التوالي.

🎉 مبروك! 🎉

[<< اليوم 16](./16_python_datetime.md) | [اليوم 18 >>](./18_regular_expressions.md)
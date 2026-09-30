<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 15 - أخطاء الأنواع في بايثون</h1>
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

[<< اليوم 14](./14_higher_order_functions.md) | [اليوم 16 >>](./16_python_datetime.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 15](#-اليوم-15)
  - [أنواع الأخطاء في بايثون](#أنواع-الأخطاء-في-بايثون)
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
  - [💻 تمارين: اليوم 15](#-تمارين-اليوم-15)

# 📘 اليوم 15

## أنواع الأخطاء في بايثون

عندما نكتب كودًا، من الشائع أن نرتكب خطأً إملائيًّا أو بعض الأخطاء الشائعة الأخرى. إذا فشل كودنا في التشغيل، سيعرض مفسر بايثون رسالة تحتوي على معلومات عن مكان حدوث المشكلة ونوع الخطأ. سيعطينا أيضًا أحيانًا اقتراحات عن إصلاح محتمل. فهم الأنواع المختلفة من الأخطاء في لغات البرمجة يساعدنا في تنقيح كودنا بسرعة كما يجعلنا مبرمجين أفضل في عملنا.

دعنا نرى أكثر أنواع الأخطاء شيوعًا واحدًا تلو الآخر. أولاً دعنا نفتح 'شل بايثون التفاعلي'. اذهب إلى 'terminal' لجهازك واكتب 'python'. سيُفتح شل بايثون التفاعلي.

### SyntaxError

**مثال 1: SyntaxError**

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

كما ترى ارتكبنا خطأ صياغة، لأننا نسينا تضمين النص بين أقواس، وبايثون يقترح الحل بالفعل. دعنا نصلحه.

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

كان الخطأ 'SyntaxError'. بعد الإصلاح تم تنفيذ كودنا دون عقبات. دعنا نرى المزيد من أنواع الأخطاء.

### NameError

**مثال 1: NameError**

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

كما ترى من الرسالة أعلاه، الاسم 'age' غير معرّف. لم نعرّف المتغير 'age' بعد، لكننا حاولنا طباعته كأننا أعلناه بالفعل. الآن، دعنا نصلح هذا بإعلان المتغير وتعيينه بقيمة.

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

كان نوع الخطأ 'NameError'. قمنا بتنقيح الخطأ بتعريف اسم المتغير.

### IndexError

**مثال 1: IndexError**

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

في المثال أعلاه، أثار بايثون 'IndexError'، لأن القائمة تحتوي فقط على فهارس من 0 إلى 4، لذا كان الوصول خارج النطاق.

### ModuleNotFoundError

**مثال 1: ModuleNotFoundError**

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

في المثال أعلاه، أضفت حرف 's' إضافيًا إلى 'math' عمدًا، فتم إثارة 'ModuleNotFoundError'. دعنا نصلح ذلك بإزالة حرف 's' الإضافي من 'math'.

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

أصلحناها، لذلك دعنا نستخدم بعض الدوال من وحدة 'math'.

### AttributeError

**مثال 1: AttributeError**

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

كما ترى، ارتكبت خطأً مرة أخرى! بدلاً من 'pi'، حاولت استدعاء الثابت 'PI' من وحدة 'math'. أثار هذا خطأ في السمة، أي أن السمة غير موجودة في الوحدة. دعنا نصلحه بتغيير 'PI' إلى 'pi'.

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

الآن، عندما نستدعي 'pi' من وحدة 'math' حصلنا على النتيجة.

### KeyError

**مثال 1: KeyError**

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

كما ترى، كان هناك خطأ إملائي في المفتاح المستخدم للحصول على قيمة القاموس. هذا خطأ 'KeyError'، والإصلاح بسيط جدًا. دعنا نقوم بذلك!

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

تم تنقيح الخطأ، فعمل كودنا وحصلنا على القيمة.

### TypeError

**مثال 1: TypeError**

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

في المثال أعلاه، يتم إثارة 'TypeError' لأننا لا يمكننا إضافة رقم إلى نص. الحل الأول سيكون تحويل النص إلى 'int' أو 'float'. حل آخر سيكون تحويل الرقم إلى نص (ستكون النتيجة حينها '43'). دعنا نتبع الإصلاح الأول.

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

أُزيل الخطأ وحصلنا على النتيجة التي توقعناها.

### ImportError

**مثال 1: ImportError**

```py
asabeneh@Asabeneh:~$ python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

لا توجد دالة باسم 'power' في وحدة 'math'، إنها تأتي باسم مختلف وهو 'pow'. دعنا نصححها:

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

في هذه الحالة لا يمكننا تحويل النص المعطى إلى رقم، بسبب حرف 'a' الموجود فيه.

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

لا يمكننا قسمة رقم على صفر.

لقد غطينا أهم أنواع أخطاء بايثون. إذا أردت معرفة المزيد، تحقق من [وثائق بايثون عن أنواع الأخطاء](https://docs.python.org/3/tutorial/errors.html).

إذا كنت جيدًا في قراءة رسائل الأخطاء، فستتمكن من إصلاح أخطائك بسرعة وستصبح مبرمجًا أفضل.

🌕 أنت متفوق. وصلت إلى منتصف الطريق نحو عظمتك. الآن قم ببعض التمارين لعقلك ولعضلاتك.

## 💻 تمارين: اليوم 15

1. افتح 'شل بايثون التفاعلي' وجرب جميع الأمثلة المغطاة في هذا القسم.

🎉 مبروك! 🎉

[<< اليوم 14](./14_higher_order_functions.md) | [اليوم 16 >>](./16_python_datetime.md)
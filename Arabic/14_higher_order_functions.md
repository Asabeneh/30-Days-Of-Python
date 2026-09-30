<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 14 - دوال الرتبة العليا (Higher Order Functions)</h1>
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

[<< اليوم 13](./13_list_comprehension.md) | [اليوم 15 >>](./15_python_type_errors.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 14](#-اليوم-14)
  - [دوال الرتبة العليا](#دوال-الرتبة-العليا)
    - [دالة كبارامتر](#دالة-كبارامتر)
    - [دالة كقيمة إرجاع](#دالة-كقيمة-إرجاع)
  - [الإغلاقات في بايثون (Closures)](#الإغلاقات-في-بايثون-closures)
  - [المزخرفات في بايثون (Decorators)](#المزخرفات-في-بايثون-decorators)
    - [إنشاء المزخرفات](#إنشاء-المزخرفات)
    - [تطبيق عدة مزخرفات على دالة واحدة](#تطبيق-عدة-مزخرفات-على-دالة-واحدة)
    - [قبول بارامترات في دوال المزخرفات](#قبول-بارامترات-في-دوال-المزخرفات)
  - [دوال الرتبة العليا المضمنة](#دوال-الرتبة-العليا-المضمنة)
    - [دالة Map في بايثون](#دالة-map-في-بايثون)
    - [دالة Filter في بايثون](#دالة-filter-في-بايثون)
    - [دالة Reduce في بايثون](#دالة-reduce-في-بايثون)
  - [💻 تمارين: اليوم 14](#-تمارين-اليوم-14)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 14

## دوال الرتبة العليا

في بايثون تُعامل الدوال كمواطنين من الدرجة الأولى، مما يسمح لك بإجراء العمليات التالية على الدوال:

- يمكن للدالة أن تأخذ دالة أو أكثر كبارامترات
- يمكن إرجاع دالة كنتيجة لدالة أخرى
- يمكن تعديل دالة
- يمكن تعيين دالة إلى متغير

في هذا القسم، سنغطي:

1. التعامل مع الدوال كبارامترات
2. إرجاع الدوال كقيمة إرجاع من دوال أخرى
3. استخدام الإغلاقات والمزخرفات في بايثون

### دالة كبارامتر

```py
def sum_numbers(nums):  # دالة عادية
    return sum(nums)    # دالة تستخدم الدالة المضمنة sum

def higher_order_function(f, lst):  # دالة كبارامتر
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### دالة كقيمة إرجاع

```py
def square(x):          # دالة التربيع
    return x ** 2

def cube(x):            # دالة التكعيب
    return x ** 3

def absolute(x):        # دالة القيمة المطلقة
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # دالة رتبة عليا تعيد دالة
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

يمكنك أن ترى من المثال أعلاه أن دالة الرتبة العليا تعيد دوالًا مختلفة اعتمادًا على البارامتر الممرر.

## الإغلاقات في بايثون (Closures)

تسمح بايثون لدالة متداخلة بالوصول إلى النطاق الخارجي للدالة المحتوية عليها. يعرف هذا باسم الإغلاق (Closure). دعنا نلقي نظرة على كيفية عمل الإغلاقات في بايثون. في بايثون، يُنشأ الإغلاق بتداخل دالة داخل دالة أخرى مغلفة ثم إرجاع الدالة الداخلية. انظر المثال أدناه.

**مثال:**

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## المزخرفات في بايثون (Decorators)

المزخرف (decorator) هو نمط تصميم في بايثون يسمح للمستخدم بإضافة وظائف جديدة إلى كائن موجود دون تعديل هيكله. تُستدعى المزخرفات عادةً قبل تعريف الدالة التي تريد تزيينها.

### إنشاء المزخرفات

لإنشاء دالة مزخرفة، نحتاج إلى دالة خارجية مع دالة غلاف داخلية.

**مثال:**

```py
# دالة عادية
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## دعنا ننفذ المثال أعلاه بمزخرف

'''دالة المزخرف هذه هي دالة رتبة عليا
تأخذ دالة كبارامتر'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

### تطبيق عدة مزخرفات على دالة واحدة

```py

'''دوال المزخرف هذه هي دوال رتبة عليا
تأخذ دوال كبارامترات'''

# المزخرف الأول
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# المزخرف الثاني
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

#سيتم تنفيذ المزخرفات من الأسفل إلى الأعلى
@split_string_decorator
@uppercase_decorator     # الترتيب مع المزخرفات مهم في هذه الحالة - دالة .upper() لا تعمل مع القوائم
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### قبول بارامترات في دوال المزخرفات

في معظم الأوقات نحتاج إلى دالاتنا لتأخذ بارامترات، لذا قد نحتاج إلى تعريف مزخرف يقبل بارامترات.

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## دوال الرتبة العليا المضمنة

بعض دوال الرتبة العليا المضمنة التي سنغطيها في هذا الجزء هي 'map()'، 'filter' و 'reduce'.
يمكن تمرير دالة lambda كبارامتر وأفضل حالة استخدام لدوال lambda هي في دوال مثل map و filter و reduce.

### دالة Map في بايثون

دالة map() هي دالة مضمنة تأخذ دالة ومتابعة (iterable) كبارامترات.

```py
    # الصيغة
    map(function, iterable)
```

**مثال:1**

```py
numbers = [1, 2, 3, 4, 5] # متابعة (iterable)
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# دعنا نطبقها مع دالة lambda
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**مثال:2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # متابعة (iterable)
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**مثال:3**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # متابعة (iterable)

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# دعنا نطبقها مع دالة lambda
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

ما تفعله map فعليًا هو التكرار عبر قائمة. على سبيل المثال، تغير الأسماء إلى أحرف كبيرة وتعيد قائمة جديدة.

### دالة Filter في بايثون

دالة filter() تستدعي الدالة المحددة التي تعيد قيمة منطقية لكل عنصر من المتابعة (القائمة) المحددة. إنها تفلتر العناصر التي تلبي معايير التصفية.

```py
    # الصيغة
    filter(function, iterable)
```

**مثال:1**

```py
# دعنا نفلتر الأرقام الزوجية فقط
numbers = [1, 2, 3, 4, 5]  # متابعة (iterable)

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**مثال:2**

```py
numbers = [1, 2, 3, 4, 5]  # متابعة (iterable)

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# تصفية الاسم الطويل
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # متابعة (iterable)
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### دالة Reduce في بايثون

دالة 'reduce()' معرّفة في وحدة functools ويجب أن نستوردها من هذه الوحدة. مثل map و filter تأخذ بارامترين، دالة ومتابعة (iterable). ومع ذلك، لا تعيد متابعة أخرى، بل تعيد قيمة واحدة.
**مثال:1**

```py
numbers_str = ['1', '2', '3', '4', '5']  # متابعة (iterable)
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 تمارين: اليوم 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### تمارين: المستوى 1

1. اشرح الفرق بين map و filter و reduce.
2. اشرح الفرق بين دالة الرتبة العليا والإغلاق والمزخرف
3. عرّف دالة استدعاء قبل map أو filter أو reduce، انظر الأمثلة.
4. استخدم حلقة for لطباعة كل دولة في قائمة البلدان.
5. استخدم for لطباعة كل اسم في قائمة الأسماء.
6. استخدم for لطباعة كل رقم في قائمة الأرقام.

### تمارين: المستوى 2

1. استخدم map لإنشاء قائمة جديدة بتغيير كل دولة إلى أحرف كبيرة في قائمة البلدان
2. استخدم map لإنشاء قائمة جديدة بتغيير كل رقم إلى مربعه في قائمة الأرقام
3. استخدم map لتغيير كل اسم إلى أحرف كبيرة في قائمة الأسماء
4. استخدم filter لتصفية البلدان التي تحتوي على 'land'.
5. استخدم filter لتصفية البلدان التي تحتوي بالضبط على ستة أحرف.
6. استخدم filter لتصفية البلدان التي تحتوي على ستة أحرف أو أكثر في قائمة البلدان.
7. استخدم filter لتصفية البلدان التي تبدأ بحرف 'E'
8. اربط مكررات قائمة أو أكثر (مثل: arr.map(callback).filter(callback).reduce(callback))
9. أعلن دالة باسم get_string_lists تأخذ قائمة كبارامتر ثم تعيد قائمة تحتوي على عناصر نصية فقط.
10. استخدم reduce لجمع كل الأرقام في قائمة الأرقام.
11. استخدم reduce لدمج كل البلدان ولإنتاج هذه الجملة: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
12. أعلن دالة باسم categorize_countries تعيد قائمة من البلدان بنمط مشترك (يمكنك العثور على [قائمة البلدان](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) في هذا المستودع كما في countries.js (مثل 'land', 'ia', 'island', 'stan')).
13. أنشئ دالة تعيد قاموسًا، حيث تمثل المفاتيح حروف البلدان الأولى والقيم هي عدد أسماء البلدان التي تبدأ بذلك الحرف.
14. أعلن دالة get_first_ten_countries - تعيد قائمة من أول عشر بلدان من قائمة countries.js في مجلد البيانات.
15. أعلن دالة get_last_ten_countries تعيد آخر عشر بلدان في قائمة البلدان.

### تمارين: المستوى 3

1. استخدم ملف countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) واتبع المهام أدناه:
   - رتب البلدان حسب الاسم، حسب العاصمة، حسب عدد السكان
   - رتب اللغات العشر الأكثر تحدثًا حسب الموقع.
   - رتب البلدان العشر الأكثر سكانًا.

🎉 مبروك! 🎉

[<< اليوم 13](./13_list_comprehension.md) | [اليوم 15 >>](./15_python_type_errors.md)
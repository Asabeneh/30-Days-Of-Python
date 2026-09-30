<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 2 - المتغيرات والدوال المضمنة</h1>
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

[<< اليوم 1](./readme.md) | [اليوم 3 >>](./03_operators.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 2](#-اليوم-2)
  - [الدوال المضمنة (Built-in Functions)](#الدوال-المضمنة-built-in-functions)
  - [المتغيرات](#المتغيرات)
    - [تعريف عدة متغيرات في سطر واحد](#تعريف-عدة-متغيرات-في-سطر-واحد)
  - [أنواع البيانات](#أنواع-البيانات)
  - [التحقق من أنواع البيانات وتحويلها (Casting)](#التحقق-من-أنواع-البيانات-وتحويلها-casting)
  - [الأعداد](#الأعداد)
  - [💻 تمارين - اليوم 2](#-تمارين---اليوم-2)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)

# 📘 اليوم 2

## الدوال المضمنة (Built-in Functions)

في بايثون لدينا الكثير من الدوال المضمنة (built-in functions). الدوال المضمنة متاحة عالميًا للاستخدام، مما يعني أنه يمكنك استخدامها دون الحاجة إلى استيرادها أو تكوينها. بعض من أكثر دوال بايثون المضمنة شيوعًا هي: 'print()'، 'len()'، 'type()'، 'int()'، 'float()'، 'str()'، 'input()'، 'list()'، 'dict()'، 'min()'، 'max()'، 'sum()'، 'sorted()'، 'open()'، 'file()'، 'help()'، و 'dir()'. في الجدول التالي سترى قائمة شاملة بدوال بايثون المضمنة المأخوذة من [وثائق بايثون](https://docs.python.org/3/library/functions.html).

![الدوال المضمنة](../images/builtin-functions.png)

دعنا نفتح شل بايثون ونبدأ باستخدام بعض من أكثر الدوال المضمنة شيوعًا.

![الدوال المضمنة](../images/builtin-functions_practice.png)

دعنا نتدرب أكثر باستخدام دوال مضمنة مختلفة.

![دوال Help و Dir المضمنة](../images/help_and_dir_builtin.png)

كما ترى من 'terminal' أعلاه، بايثون لديها كلمات محجوزة (reserved words). لا نستخدم الكلمات المحجوزة لتعريف المتغيرات أو الدوال. سنغطي المتغيرات في القسم التالي.

أعتقد أنك الآن أصبحت على دراية بالدوال المضمنة. دعنا نقوم بتمرين آخر على الدوال المضمنة ثم ننتقل إلى القسم التالي.

![Min Max Sum](../images/builtin-functional-final.png)

## المتغيرات

المتغيرات تخزن البيانات في ذاكرة الكمبيوتر. يُوصى باستخدام المتغيرات التذكيرية ('mnemonic') في العديد من لغات البرمجة. المتغير التذكيري هو اسم متغير يمكن تذكره وربطه بسهولة. المتغير يشير إلى عنوان في الذاكرة حيث يتم تخزين البيانات.
الرقم في البداية، الحرف الخاص، والواصلة غير مسموح بها عند تسمية متغير. يمكن أن يكون للمتغير اسم قصير (مثل x, y, z)، ولكن الاسم الوصفي (firstname, lastname, age, country) موصى به بشدة.

قواعد تسمية المتغيرات في بايثون:

- يجب أن يبدأ اسم المتغير بحرف أو شرطة سفلية (\_)
- لا يمكن أن يبدأ اسم المتغير برقم
- يمكن أن يحتوي اسم المتغير فقط على أحرف أبجدية رقمية وشرطات سفلية (A-z, 0-9, و \_)
- أسماء المتغيرات حساسة لحالة الأحرف (firstname, Firstname, FirstName و FIRSTNAME متغيرات مختلفة)

فيما يلي بعض الأمثلة على أسماء المتغيرات الصالحة:

```shell
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # إذا أردنا استخدام كلمة محجوزة كمتغير
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

أسماء متغيرات غير صالحة:

```shell
first-name
first@name
first$name
num-1
1num
```

سنستخدم نمط تسمية متغيرات بايثون القياسي الذي تبناه العديد من مطوري بايثون. يستخدم مطورو بايثون اصطلاح تسمية 'snake case' ('snake_case'). نستخدم شرطة سفلية بعد كل كلمة لمتغير يحتوي على أكثر من كلمة (مثل first_name, last_name, engine_rotation_speed). المثال أدناه هو مثال على التسمية القياسية للمتغيرات، الشرطة السفلية مطلوبة عندما يكون اسم المتغير أكثر من كلمة.

عندما نخصص نوع بيانات معين لمتغير، يُسمى ذلك تعريف متغير (variable declaration). على سبيل المثال في المثال أدناه، تم تعيين اسمي الأول إلى متغير first_name. علامة التساوي هي عامل تعيين (assignment operator). التعيين يعني تخزين البيانات في المتغير. علامة التساوي في بايثون ليست المساواة كما في الرياضيات.

_مثال:_

```py
# المتغيرات في بايثون
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

دعنا نستخدم الدوال المضمنة 'print()' و 'len()'. دالة print تأخذ عددًا غير محدود من الوسائط (arguments). الوسيط (argument) هو قيمة يمكن تمريرها أو وضعها داخل أقواس الدالة، انظر المثال أدناه.

**مثال:**

```py
print('Hello, World!') # النص Hello, World! هو وسيط
print('Hello',',', 'World','!') # يمكن أن تأخذ عدة وسائط، تم تمرير أربع وسائط
print(len('Hello, World!')) # تأخذ وسيطًا واحدًا فقط
```

دعنا نطبع ونجد أيضًا طول المتغيرات التي تم تعريفها أعلاه:

**مثال:**

```py
# طباعة القيم المخزنة في المتغيرات

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### تعريف عدة متغيرات في سطر واحد

يمكن أيضًا تعريف عدة متغيرات في سطر واحد:

**مثال:**

```py
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

الحصول على إدخال المستخدم باستخدام الدالة المضمنة 'input()'. دعنا نخصص البيانات التي نحصل عليها من المستخدم إلى متغيري first_name و age.
**مثال:**

```py
first_name = input('ما اسمك: ')
age = input('كم عمرك؟ ')

print(first_name)
print(age)
```

## أنواع البيانات

هناك عدة أنواع من البيانات في بايثون. لتحديد نوع البيانات نستخدم الدالة المضمنة 'type'. أود أن أطلب منك التركيز على فهم أنواع البيانات المختلفة جيدًا. عندما يتعلق الأمر بالبرمجة، فإن الأمر كله يتعلق بأنواع البيانات. لقد قدمت أنواع البيانات في البداية وتأتي مرة أخرى، لأن كل موضوع مرتبط بأنواع البيانات. سنغطي أنواع البيانات بمزيد من التفصيل في أقسامها الخاصة.

## التحقق من أنواع البيانات وتحويلها (Casting)

- التحقق من أنواع البيانات: للتحقق من نوع بيانات معينة/متغير نستخدم الدالة 'type'
  **أمثلة:**

```py
# أنواع بيانات بايثون المختلفة
# دعنا نعلن عن متغيرات بأنواع بيانات متنوعة

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int، هذا ليس عمري الحقيقي، لا تقلق بشأنه

# طباعة الأنواع
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip
```

- التحويل (Casting): تحويل نوع بيانات إلى نوع بيانات آخر. نستخدم 'int()'، 'float()'، 'str()'، 'list'، 'set'
  عندما نقوم بعمليات حسابية، يجب أولاً تحويل الأعداد النصية إلى int أو float وإلا سيعيد خطأ. إذا قمنا بدمج (concatenate) رقم مع نص، يجب أولاً تحويل الرقم إلى نص. سنتحدث عن الدمج في قسم النصوص (Strings).

  **أمثلة:**

```py
# تحويل int إلى float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# تحويل float إلى int
gravity = 9.81
print(int(gravity))             # 9

# تحويل int إلى str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# تحويل str إلى int أو float
num_str = '10.6'
num_float = float(num_str)  # تحويل النص إلى float أولاً
num_int = int(num_float)    # ثم تحويل float إلى int
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# تحويل str إلى list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

## الأعداد

أنواع البيانات الرقمية في بايثون:

1. الأعداد الصحيحة (Integers): أعداد صحيحة (سلبية، صفر، وإيجابية)
   مثال:
   ... -3, -2, -1, 0, 1, 2, 3 ...

2. أعداد الفاصلة العائمة (Floating Point Numbers) (أعداد عشرية)
   مثال:
   ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3. الأعداد المركبة (Complex Numbers)
   مثال:
   1 + j, 2 + 4j, 1 - 1j

🌕 أنت رائع. لقد أكملت للتو تحديات اليوم الثاني وأنت على بعد خطوتين في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين - اليوم 2

### تمارين: المستوى 1

1. داخل 30DaysOfPython أنشئ مجلدًا باسم day_2. داخل هذا المجلد أنشئ ملفًا باسم variables.py
2. اكتب تعليقًا (comment) في بايثون يقول 'Day 2: 30 Days of python programming'
3. عرّف متغيرًا للاسم الأول (first name) وأسند إليه قيمة
4. عرّف متغيرًا لاسم العائلة (last name) وأسند إليه قيمة
5. عرّف متغيرًا للاسم الكامل (full name) وأسند إليه قيمة
6. عرّف متغيرًا للبلد (country) وأسند إليه قيمة
7. عرّف متغيرًا للمدينة (city) وأسند إليه قيمة
8. عرّف متغيرًا للعمر (age) وأسند إليه قيمة
9. عرّف متغيرًا للسنة (year) وأسند إليه قيمة
10. عرّف متغيرًا is_married وأسند إليه قيمة
11. عرّف متغيرًا is_true وأسند إليه قيمة
12. عرّف متغيرًا is_light_on وأسند إليه قيمة
13. عرّف عدة متغيرات في سطر واحد

### تمارين: المستوى 2

1. تحقق من نوع البيانات لجميع متغيراتك باستخدام الدالة المضمنة type()
2. باستخدام الدالة المضمنة 'len()'، ابحث عن طول اسمك الأول
3. قارن طول اسمك الأول واسم عائلتك
4. عرّف 5 كـ num_one و 4 كـ num_two
5. اجمع num_one و num_two وأسند القيمة إلى متغير total
6. اطرح num_two من num_one وأسند القيمة إلى متغير diff
7. اضرب num_two و num_one وأسند القيمة إلى متغير product
8. اقسم num_one على num_two وأسند القيمة إلى متغير division
9. استخدم باقي القسمة لإيجاد num_two مقسومًا على num_one وأسند القيمة إلى متغير remainder
10. احسب num_one أس num_two وأسند القيمة إلى متغير exp
11. جد ناتج القسمة الصحيحة (floor division) لـ num_one على num_two وأسند القيمة إلى متغير floor_division
12. نصف قطر (radius) دائرة هو 30 مترًا.
    1. احسب مساحة الدائرة وأسند القيمة إلى متغير باسم 'area_of_circle'
    2. احسب محيط الدائرة وأسند القيمة إلى متغير باسم 'circum_of_circle'
    3. خذ نصف القطر كإدخال من المستخدم واحسب المساحة.
13. استخدم دالة الإدخال المضمنة input() للحصول على الاسم الأول، اسم العائلة، البلد والعمر من المستخدم وخزّن القيمة في أسماء المتغيرات المقابلة
14. شغّل help('keywords') في شل بايثون أو في ملفك للتحقق من الكلمات المحجوزة أو الكلمات المفتاحية في بايثون

🎉 مبروك! 🎉

[<< اليوم 1](./readme.md) | [اليوم 3 >>](./03_operators.md)

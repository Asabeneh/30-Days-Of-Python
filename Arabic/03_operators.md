<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 3 - العوامل (Operators)</h1>
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

[<< اليوم 2](./02_variables_builtin_functions.md) | [اليوم 4 >>](./04_strings.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 3](#-اليوم-3)
  - [القيم المنطقية (Boolean)](#القيم-المنطقية-boolean)
  - [العوامل (Operators)](#العوامل-operators)
    - [عوامل التعيين](#عوامل-التعيين)
    - [العوامل الحسابية:](#العوامل-الحسابية)
    - [عوامل المقارنة](#عوامل-المقارنة)
    - [العوامل المنطقية](#العوامل-المنطقية)
  - [💻 تمارين - اليوم 3](#-تمارين---اليوم-3)

# 📘 اليوم 3

## القيم المنطقية (Boolean)

نوع البيانات المنطقية (boolean) يمثل إحدى القيمتين: 'True' أو 'False'. ستتضح استخدامات هذه الأنواع من البيانات عندما نبدأ باستخدام عامل المقارنة. الحرف الأول **T** لـ True و **F** لـ False يجب أن يكون كبيرًا، على عكس جافا سكريبت.
**مثال: القيم المنطقية**

```py
print(True)
print(False)
```

## العوامل (Operators)

لغة بايثون تدعم عدة أنواع من العوامل (operators). في هذا القسم، سنركز على بعض منها.

### عوامل التعيين

تُستخدم عوامل التعيين (Assignment operators) لتعيين قيم للمتغيرات. لنأخذ = كمثال. علامة التساوي في الرياضيات تُظهر أن قيمتين متساويتان، ولكن في بايثون تعني أننا نخزن قيمة في متغير معين ونسميها تعيينًا أو إسناد قيمة لمتغير. الجدول أدناه يوضح الأنواع المختلفة لعوامل التعيين في بايثون، مأخوذ من [w3school](https://www.w3schools.com/python/python_operators.asp).

![عوامل التعيين](../images/assignment_operators.png)

### العوامل الحسابية:

- الجمع (+): a + b
- الطرح (-): a - b
- الضرب (\*): a \* b
- القسمة (/): a / b
- باقي القسمة (%): a % b
- قسمة الأرض (//): a // b
- الأس (\*\*): a \*\* b

![العوامل الحسابية](../images/arithmetic_operators.png)

**مثال: الأعداد الصحيحة**

```py
# العمليات الحسابية في بايثون
# الأعداد الصحيحة

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  القسمة في بايثون تعطي رقمًا عشريًا
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3, بدون الجزء العشري أو الباقي
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, يعطي الباقي
print('Exponentiation: ', 2 ** 3) # 8 تعني 2 * 2 * 2
```

**مثال: الأعداد العشرية**

```py
# الأعداد العشرية
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
```

**مثال: الأعداد المركبة**

```py
# الأعداد المركبة
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

دعنا نعرف متغيرًا ونخصص له نوع بيانات رقمي. سأستخدم متغيرًا من حرف واحد ولكن تذكر لا تطور عادة تعريف مثل هذه الأنواع من المتغيرات. يجب أن تكون أسماء المتغيرات دائمًا تذكيرية (mnemonic).

**مثال:**

```python
# تعريف المتغير في الأعلى أولاً

a = 3 # a اسم متغير و 3 هو نوع بيانات عدد صحيح
b = 2 # b اسم متغير و 2 هو نوع بيانات عدد صحيح

# العمليات الحسابية وتعيين النتيجة لمتغير
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# كان يجب أن أستخدم sum بدلاً من total ولكن sum دالة مضمنة - حاول تجنب تجاوز الدوال المضمنة
print(total) # إذا لم تضع تصنيفًا لطباعتك بنص ما، لن تعرف أبدًا من أين تأتي النتيجة
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
```

**مثال:**

```py
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# تعريف القيم وتنظيمها معًا
num_one = 3
num_two = 4

# العمليات الحسابية
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# طباعة القيم مع تصنيف
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
```

دعنا نبدأ في ربط النقاط والبدء في استخدام ما نعرفه بالفعل لحساب (المساحة، الحجم، الكثافة، الوزن، المحيط، المسافة، القوة).

**مثال:**

```py
# حساب مساحة دائرة
radius = 10                                 # نصف قطر الدائرة
area_of_circle = 3.14 * radius ** 2         # علامتا * تعنيان الأس أو القوة
print('Area of a circle:', area_of_circle)

# حساب مساحة مستطيل
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# حساب وزن جسم
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # إضافة وحدة للوزن

# حساب كثافة سائل
mass = 75 # بالكيلوجرام
volume = 0.075 # بالمتر المكعب
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3') # إضافة وحدة للكثافة

```

### عوامل المقارنة

في البرمجة نقارن القيم، نستخدم عوامل المقارنة (comparison operators) لمقارنة قيمتين. نتحقق مما إذا كانت القيمة أكبر أو أقل أو تساوي قيمة أخرى. الجدول التالي يوضح عوامل المقارنة في بايثون والتي تم أخذها من [w3shool](https://www.w3schools.com/python/python_operators.asp).

![عوامل المقارنة](../images/comparison_operators.png)
**مثال: عوامل المقارنة**

```py
print(3 > 2)     # True, لأن 3 أكبر من 2
print(3 >= 2)    # True, لأن 3 أكبر من 2
print(3 < 2)     # False, لأن 3 أكبر من 2
print(2 < 3)     # True, لأن 2 أصغر من 3
print(2 <= 3)    # True, لأن 2 أصغر من 3
print(3 == 2)    # False, لأن 3 لا يساوي 2
print(3 != 2)    # True, لأن 3 لا يساوي 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False


# مقارنة شيء ما يعطي إما True أو False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```

بالإضافة إلى عوامل المقارنة أعلاه، تستخدم بايثون:

- 'is': يرجع True إذا كان كلا المتغيرين هما نفس الكائن (x is y)
- 'is not': يرجع True إذا كان كلا المتغيرين ليسا نفس الكائن (x is not y)
- 'in': يرجع True إذا كانت القائمة المُستَفسَر عنها تحتوي على عنصر معين (x in y)
- 'not in': يرجع True إذا كانت القائمة المُستَفسَر عنها لا تحتوي على عنصر معين (x not in y)

```py
print('1 is 1', 1 is 1)                   # True - لأن قيم البيانات هي نفسها
print('1 is not 2', 1 is not 2)           # True - لأن 1 ليس 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A موجود في النص
print('B not in Asabeneh', 'B' in 'Asabeneh') # False - لا يوجد B كبير
print('coding' in 'coding for all') # True - لأن coding for all تحتوي على كلمة coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
```

### العوامل المنطقية

على عكس لغات البرمجة الأخرى، تستخدم بايثون الكلمات المفتاحية 'and' و 'or' و 'not' للعوامل المنطقية (logical operators). تُستخدم العوامل المنطقية لدمج العبارات الشرطية:

![العوامل المنطقية](../images/logical_operators.png)

```py
print(3 > 2 and 4 > 3) # True - لأن كلا العبارتين صحيحة
print(3 > 2 and 4 < 3) # False - لأن العبارة الثانية خاطئة
print(3 < 2 and 4 < 3) # False - لأن كلا العبارتين خاطئة
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - لأن كلا العبارتين صحيحة
print(3 > 2 or 4 < 3)  # True - لأن إحدى العبارتين صحيحة
print(3 < 2 or 4 < 3)  # False - لأن كلا العبارتين خاطئة
print('True or False:', True or False)
print(not 3 > 2)     # False - لأن 3 > 2 صحيحة، إذًا not True تعطي False
print(not True)      # False - النفي، عامل not يحول true إلى false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

```

🌕 لديك طاقة لا حدود لها. لقد أكملت للتو تحديات اليوم الثالث وأنت على بعد ثلاث خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين - اليوم 3

1. عرّف عمرك كمتغير من نوع عدد صحيح (integer)
2. عرّف طولك كمتغير من نوع عشري (float)
3. عرّف متغيرًا يخزن عددًا مركبًا (complex number)
4. اكتب سكريبتًا يطلب من المستخدم إدخال قاعدة وارتفاع المثلث ويحسب مساحة هذا المثلث (area = 0.5 x b x h).

```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```

5. اكتب سكريبتًا يطلب من المستخدم إدخال الضلع a والضلع b والضلع c للمثلث. احسب محيط المثلث (perimeter = a + b + c).

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

6. احصل على طول وعرض مستطيل باستخدام prompt. احسب مساحته (area = length x width) ومحيطه (perimeter = 2 x (length + width))
7. احصل على نصف قطر دائرة باستخدام prompt. احسب المساحة (area = pi x r x r) والمحيط (c = 2 x pi x r) حيث pi = 3.14.
8. احسب الميل (slope) والتقاطع مع المحور x والتقاطع مع المحور y لـ y = 2x -2
9. الميل (m = y2-y1/x2-x1). جد الميل و[المسافة الإقليدية](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) بين النقطة (2, 2) والنقطة (6,10)
10. قارن بين الميلين في المهمتين 8 و 9.
11. احسب قيمة y (y = x^2 + 6x + 9). جرب قيم x مختلفة واكتشف عند أي قيمة x تصبح y تساوي 0.
12. جد طول 'python' و 'dragon' واجعل عبارة مقارنة خاطئة (falsy).
13. استخدم عامل 'and' للتحقق مما إذا كانت 'on' موجودة في كل من 'python' و 'dragon'
14. _I hope this course is not full of jargon_. استخدم عامل 'in' للتحقق مما إذا كانت _jargon_ موجودة في الجملة.
15. لا يوجد 'on' في كل من dragon و python
16. جد طول النص 'python' وحوّل القيمة إلى 'float' ثم حوّلها إلى 'string'
17. الأعداد الزوجية تقبل القسمة على 2 والباقي صفر. كيف تتحقق مما إذا كان الرقم زوجيًا أم لا باستخدام بايثون؟
18. تحقق مما إذا كانت قسمة الأرض (floor division) لـ 7 على 3 تساوي القيمة المحوّلة إلى int لـ 2.7.
19. تحقق مما إذا كان نوع '10' يساوي نوع 10
20. تحقق مما إذا كان int('9.8') يساوي 10
21. اكتب سكريبتًا يطلب من المستخدم إدخال ساعات العمل والأجر لكل ساعة. احسب أجر الشخص؟

```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

22. اكتب سكريبتًا يطلب من المستخدم إدخال عدد السنوات. احسب عدد الثواني التي يمكن للشخص أن يعيشها. افترض أن الشخص يمكنه أن يعيش مئة سنة

```py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
```

23. اكتب سكريبت بايثون يعرض الجدول التالي

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

🎉 مبروك! 🎉

[<< اليوم 2](./02_variables_builtin_functions.md) | [اليوم 4 >>](./04_strings.md)

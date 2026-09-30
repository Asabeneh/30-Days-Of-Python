<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 4 - النصوص (Strings)</h1>
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

[<< اليوم 3](./03_operators.md) | [اليوم 5 >>](./05_lists.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 4](#-اليوم-4)
  - [النصوص (Strings)](#النصوص-strings)
    - [إنشاء نص](#إنشاء-نص)
    - [دمج النصوص (Concatenation)](#دمج-النصوص-concatenation)
    - [تسلسلات الهروب في النصوص (Escape Sequences)](#تسلسلات-الهروب-في-النصوص-escape-sequences)
    - [تنسيق النصوص](#تنسيق-النصوص)
      - [التنسيق القديم (% Operator)](#التنسيق-القديم--operator)
      - [التنسيق الجديد (str.format)](#التنسيق-الجديد-strformat)
      - [f-Strings (Python 3.6+)](#f-strings-python-36)
    - [النصوص في بايثون كمتابعات من الأحرف](#النصوص-في-بايثون-كمتابعات-من-الأحرف)
      - [تفكيك الأحرف (Unpacking)](#تفكيك-الأحرف-unpacking)
      - [الوصول إلى الأحرف في النصوص بواسطة الفهرس](#الوصول-إلى-الأحرف-في-النصوص-بواسطة-الفهرس)
      - [تقطيع النصوص (Slicing)](#تقطيع-النصوص-slicing)
      - [عكس النص](#عكس-النص)
      - [تخطي الأحرف أثناء التقطيع](#تخطي-الأحرف-أثناء-التقطيع)
    - [دوال النصوص (String Methods)](#دوال-النصوص-string-methods)
  - [💻 تمارين - اليوم 4](#-تمارين---اليوم-4)

# 📘 اليوم 4

## النصوص (Strings)

النص هو نوع بيانات نصي. أي نوع بيانات يُكتب كنص هو نص (string). أي بيانات تحت علامات اقتباس مفردة أو مزدوجة أو ثلاثية هي نصوص. هناك دوال نصية مختلفة ودوال مضمنة للتعامل مع أنواع البيانات النصية. للتحقق من طول النص استخدم دالة 'len()'.

### إنشاء نص

```py
letter = 'P'                # النص يمكن أن يكون حرفًا واحدًا أو مجموعة نصوص
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # يمكن إنشاء النص باستخدام علامة اقتباس مفردة أو مزدوجة
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
```

يتم إنشاء النص متعدد الأسطر باستخدام علامات اقتباس ثلاثية مفردة (''') أو ثلاثية مزدوجة ("""). انظر المثال أدناه.

```py
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# طريقة أخرى لفعل الشيء نفسه
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```

### دمج النصوص (Concatenation)

يمكننا ربط النصوص معًا. يُسمى دمج أو ربط النصوص بالدمج (concatenation). انظر المثال أدناه:

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# التحقق من طول النص باستخدام دالة len() المضمنة
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```

### تسلسلات الهروب في النصوص (Escape Sequences)

في بايثون ولغات البرمجة الأخرى، \ متبوعة بحرف هي تسلسل هروب. دعنا نرى أشهر أحرف الهروب:

- \n: سطر جديد
- \t: مسافة تاب تعادل 8 مسافات
- \\: شرطة مائلة للخلف (Back slash)
- \': اقتباس مفرد (')
- \": اقتباس مزدوج (")

الآن، دعنا نرى استخدام تسلسلات الهروب أعلاه مع أمثلة.

```py
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # فاصل سطر
print('Days\tTopics\tExercises') # إضافة مسافة تاب أو 4 مسافات
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # لكتابة شرطة مائلة للخلف
print('In every programming language it starts with \"Hello, World!\"') # لكتابة اقتباس مزدوج داخل اقتباس مفرد

# المخرجات
I hope every one is enjoying the Python Challenge.
Are you ?
Days  Topics  Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

### تنسيق النصوص

#### التنسيق القديم (% Operator)

في بايثون هناك طرق عديدة لتنسيق النصوص. في هذا القسم سنغطي بعضًا منها.
عامل "%" يُستخدم لتنسيق مجموعة من المتغيرات المحصورة في "tuple" (قائمة ذات حجم ثابت)، مع سلسلة تنسيق تحتوي على نص عادي مع "محددات وسيطات"، رموز خاصة مثل "%s", "%d", "%f", "%.<small>عدد الأرقام</small>f".

- %s - نص (أو أي كائن يمثل كنص، مثل الأرقام)
- %d - أعداد صحيحة
- %f - أعداد عشرية
- "%.<small>عدد الأرقام</small>f" - أعداد عشرية بدقة محددة

```py
# نصوص فقط
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# نصوص وأرقام
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 تشير إلى رقمين بعد الفاصلة

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
```

#### التنسيق الجديد (str.format)

تم تقديم هذا التنسيق في إصدار بايثون 3.

```py

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # يحدد رقمين بعد الفاصلة
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# المخرجات
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# نصوص وأرقام
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # رقمين بعد الفاصلة
print(formated_string)

```

#### f-Strings (Python 3.6+)

طريقة جديدة أخرى لتنسيق النصوص هي f-strings. النصوص تبدأ بـ f ويمكننا حقن البيانات في مواضعها المقابلة.

```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

### النصوص في بايثون كمتابعات من الأحرف

نصوص بايثون هي متابعات (sequences) من الأحرف، وتشارك طرق الوصول الأساسية مع كائنات بايثون المرتبة الأخرى - القوائم والتوبل. أبسط طريقة لاستخراج أحرف مفردة من النصوص (وأعضاء فرديين من أي متابعة) هي تفكيكها إلى متغيرات مقابلة.

#### تفكيك الأحرف (Unpacking)

```
language = 'Python'
a,b,c,d,e,f = language # تفكيك أحرف المتابعة إلى متغيرات
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

#### الوصول إلى الأحرف في النصوص بواسطة الفهرس

في البرمجة، العد يبدأ من الصفر. لذلك الحرف الأول من النص يكون في الفهرس صفر وآخر حرف في النص يكون طول النص ناقص واحد.

![فهرس النص](../images/string_index.png)

```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

إذا أردنا البدء من الطرف الأيمن يمكننا استخدام الفهرسة السالبة (negative indexing). -1 هو آخر فهرس.

```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

#### تقطيع النصوص (Slicing)

في بايثون يمكننا تقطيع النصوص إلى نصوص فرعية.

```py
language = 'Python'
first_three = language[0:3] # يبدأ من الفهرس صفر حتى 3 ولكن لا يشمل 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# طريقة أخرى
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

#### عكس النص

يمكننا عكس النصوص بسهولة في بايثون.

```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

#### تخطي الأحرف أثناء التقطيع

من الممكن تخطي الأحرف أثناء التقطيع بتمرير وسيطة الخطوة (step) لطريقة التقطيع.

```py
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```

### دوال النصوص (String Methods)

هناك العديد من دوال النصوص التي تسمح لنا بتنسيق النصوص. انظر بعض دوال النصوص في المثال التالي:

- capitalize(): يحول الحرف الأول من النص إلى حرف كبير

```py
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```

- count(): يعيد عدد مرات ظهور النص الفرعي في النص، count(substring, start=.., end=..). start هو فهرس البداية للعد و end هو آخر فهرس للعد.

```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`
```

- endswith(): يتحقق مما إذا كان النص ينتهي بنهاية محددة

```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

- expandtabs(): يستبدل حرف التاب (tab) بمسافات، حجم التاب الافتراضي هو 8. يأخذ وسيطة حجم التاب

```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```

- find(): يعيد فهرس أول ظهور لنص فرعي، إذا لم يتم العثور عليه يعيد -1

```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```

- rfind(): يعيد فهرس آخر ظهور لنص فرعي، إذا لم يتم العثور عليه يعيد -1

```py
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
```

- format(): ينسق النص إلى مخرجات أجمل
   للمزيد عن تنسيق النصوص تحقق من هذا [الرابط](https://www.programiz.com/python-programming/methods/string/format)

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```

- index(): يعيد أقل فهرس لنص فرعي، الوسائط الإضافية تشير إلى فهرس البداية والنهاية (الافتراضي 0 وطول النص - 1). إذا لم يتم العثور على النص الفرعي يثير ValueError.

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
```

- rindex(): يعيد أعلى فهرس لنص فرعي، الوسائط الإضافية تشير إلى فهرس البداية والنهاية (الافتراضي 0 وطول النص - 1)

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19
```

- isalnum(): يتحقق من الأحرف الأبجدية الرقمية

```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False، المسافة ليست حرفًا أبجديًا رقميًا

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```

- isalpha(): يتحقق مما إذا كانت جميع عناصر النص أحرفًا أبجدية (a-z و A-Z)

```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # False، المسافة مستبعدة مرة أخرى
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```

- isdecimal(): يتحقق مما إذا كانت جميع الأحرف في النص أرقامًا عشرية (0-9)

```py
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
challenge = '12 3'
print(challenge.isdecimal())  # False، المسافة غير مسموح بها
```

- isdigit(): يتحقق مما إذا كانت جميع الأحرف في النص أرقامًا (0-9 وبعض أحرف اليونيكود الأخرى للأرقام)

```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

- isnumeric(): يتحقق مما إذا كانت جميع الأحرف في النص أرقامًا أو متعلقة بالأرقام (مثل isdigit()، لكنه يقبل رموزًا أكثر، مثل ½)

```py
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

- isidentifier(): يتحقق من معرف صالح - يتحقق مما إذا كان النص اسم متغير صالحًا

```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False، لأنه يبدأ برقم
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

- islower(): يتحقق مما إذا كانت جميع الأحرف الأبجدية في النص صغيرة

```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```

- isupper(): يتحقق مما إذا كانت جميع الأحرف الأبجدية في النص كبيرة

```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

- join(): يعيد نصًا مدمجًا

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
```

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

- strip(): يزيل جميع الأحرف المعطاة بدءًا من بداية ونهاية النص

```py
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
```

- replace(): يستبدل النص الفرعي بنص معين

```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```

- split(): يقسم النص، باستخدام النص المعطى أو المسافة كفاصل

```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```

- title(): يعيد نصًا بعنوان (الحرف الأول من كل كلمة كبير)

```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```

- swapcase(): يحول جميع الأحرف الكبيرة إلى صغيرة وجميع الأحرف الصغيرة إلى كبيرة

```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```

- startswith(): يتحقق مما إذا كان النص يبدأ بنص محدد

```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```

🌕 أنت شخص استثنائي ولديك إمكانات رائعة. لقد أكملت للتو تحديات اليوم الرابع وأنت على بعد أربع خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين - اليوم 4

1. ادمج النصوص 'Thirty', 'Days', 'Of', 'Python' في نص واحد 'Thirty Days Of Python'.
2. ادمج النصوص 'Coding', 'For', 'All' في نص واحد 'Coding For All'.
3. أعلن متغيرًا اسمه company وقم بتعيينه للقيمة الأولية "Coding For All".
4. اطبع المتغير company باستخدام 'print()'.
5. اطبع طول نص company باستخدام دالة 'len()' و 'print()'.
6. غيّر جميع الأحرف إلى أحرف كبيرة باستخدام دالة 'upper()'.
7. غيّر جميع الأحرف إلى أحرف صغيرة باستخدام دالة 'lower()'.
8. استخدم دوال capitalize(), title(), swapcase() لتنسيق قيمة النص _Coding For All_.
9. اقطع (slice) أول كلمة من نص _Coding For All_.
10. تحقق مما إذا كان نص _Coding For All_ يحتوي على كلمة Coding باستخدام طريقة index أو find أو طرق أخرى.
11. استبدل كلمة coding في النص 'Coding For All' إلى Python.
12. غيّر "Python for Everyone" إلى "Python for All" باستخدام طريقة replace أو طرق أخرى.
13. اقسم النص 'Coding For All' باستخدام المسافة كفاصل (split()).
14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" اقسم النص عند الفاصلة.
15. ما هو الحرف في الفهرس 0 في النص _Coding For All_.
16. ما هو آخر فهرس في النص _Coding For All_.
17. ما الحرف الموجود في الفهرس 10 في النص "Coding For All".
18. أنشئ اختصارًا (acronym) للاسم 'Python For Everyone'.
19. أنشئ اختصارًا (acronym) للاسم 'Coding For All'.
20. استخدم index لتحديد موضع أول ظهور لـ C في Coding For All.
21. استخدم index لتحديد موضع أول ظهور لـ F في Coding For All.
22. استخدم rfind لتحديد موضع آخر ظهور لـ l في Coding For All People.
23. استخدم index أو find لإيجاد موضع أول ظهور لكلمة 'because' في الجملة التالية: 'You cannot end a sentence with because because because is a conjunction'
24. استخدم rindex لإيجاد موضع آخر ظهور لكلمة because في الجملة التالية: 'You cannot end a sentence with because because because is a conjunction'
25. اقطع العبارة 'because because because' من الجملة التالية: 'You cannot end a sentence with because because because is a conjunction'
26. جد موضع أول ظهور لكلمة 'because' في الجملة التالية: 'You cannot end a sentence with because because because is a conjunction'
27. اقطع العبارة 'because because because' من الجملة التالية: 'You cannot end a sentence with because because because is a conjunction'
28. هل 'Coding For All' تبدأ بالنص الفرعي _Coding_؟
29. هل 'Coding For All' تنتهي بالنص الفرعي _coding_؟
30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;، أزل المسافات الزائدة من اليسار واليمين في النص المعطى.
31. أي من المتغيرات التالية يعيد True عند استخدام طريقة isidentifier():
    - 30DaysOfPython
    - thirty_days_of_python
32. القائمة التالية تحتوي على أسماء بعض مكتبات بايثون: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. اربط القائمة بـ "# " (هاش مع مسافة).
33. استخدم تسلسل الهروب للسطر الجديد لفصل الجمل التالية.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. استخدم تسلسل الهروب للتاب (tab) لكتابة الأسطر التالية.
    ```py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
    ```
35. استخدم طريقة تنسيق النصوص لعرض ما يلي:

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```

36. قم بعمل التالي باستخدام طرق تنسيق النصوص:

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```

🎉 مبروك! 🎉

[<< اليوم 3](./03_operators.md) | [اليوم 5 >>](./05_lists.md)

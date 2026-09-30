<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 9 - الجمل الشرطية (Conditionals)</h1>
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

[<< اليوم 8](./08_dictionaries.md) | [اليوم 10 >>](./10_loops.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 9](#-اليوم-9)
  - [الجمل الشرطية (Conditionals)](#الجمل-الشرطية-conditionals)
    - [شرط If](#شرط-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [الكتابة المختصرة (Short Hand)](#الكتابة-المختصرة-short-hand)
    - [الشروط المتداخلة (Nested Conditions)](#الشروط-المتداخلة-nested-conditions)
    - [شرط If والعوامل المنطقية](#شرط-if-والعوامل-المنطقية)
    - [If والعامل المنطقي Or](#if-والعامل-المنطقي-or)
  - [💻 تمارين: اليوم 9](#-تمارين-اليوم-9)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 9

## الجمل الشرطية (Conditionals)

بشكل افتراضي، تُنفذ العبارات في سكريبت بايثون بالتسلسل من الأعلى إلى الأسفل. إذا تطلبت منطق المعالجة ذلك، يمكن تغيير تدفق التنفيذ التسلسلي بطريقتين:

- التنفيذ الشرطي: سيتم تنفيذ كتلة من عبارة واحدة أو أكثر إذا كان تعبير معين صحيحًا
- التنفيذ التكراري: سيتم تنفيذ كتلة من عبارة واحدة أو أكثر بشكل تكراري طالما كان تعبير معين صحيحًا. في هذا القسم، سنغطي عبارات 'if'، 'else'، 'elif'. عوامل المقارنة والمنطق التي تعلمناها في الأقسام السابقة ستكون مفيدة هنا.

### شرط If

في بايثون ولغات البرمجة الأخرى تُستخدم الكلمة المفتاحية 'if' للتحقق مما إذا كان الشرط صحيحًا ولتنفيذ كتلة الكود. تذكر المسافة البادئة بعد النقطتين.

```py
# الصيغة
if condition:
    this part of code runs for truthy conditions
```

**مثال: 1**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

كما ترى في المثال أعلاه، 3 أكبر من 0. كان الشرط صحيحًا وتم تنفيذ كتلة الكود. ومع ذلك، إذا كان الشرط خاطئًا، لا نرى النتيجة. لرؤية نتيجة الشرط الخاطئ، يجب أن يكون لدينا كتلة أخرى، وهي ستكون _else_.

### If Else

إذا كان الشرط صحيحًا سيتم تنفيذ الكتلة الأولى، إذا لم يكن كذلك سيعمل شرط else.

```py
# الصيغة
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**مثال:**

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

الشرط أعلاه ثبت أنه خاطئ، لذلك تم تنفيذ كتلة else. ماذا لو كان شرطنا أكثر من اثنين؟ يمكننا استخدام 'elif'.

### If Elif Else

في حياتنا اليومية، نتخذ القرارات على أساس يومي. نتخذ القرارات ليس بفحص شرط أو شرطين بل شروط متعددة. كما هو مشابه للحياة، البرمجة أيضًا مليئة بالشروط. نستخدم 'elif' عندما يكون لدينا شروط متعددة.

```py
# الصيغة
if condition:
    code
elif condition:
    code
else:
    code

```

**مثال:**

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### الكتابة المختصرة (Short Hand)

```py
# الصيغة
code if condition else code
```

**مثال:**

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # تحقق الشرط الأول، ستتم طباعة 'A is positive'
```

### الشروط المتداخلة (Nested Conditions)

يمكن أن تكون الشروط متداخلة

```py
# الصيغة
if condition:
    code
    if condition:
    code
```

**مثال:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

```

يمكننا تجنب كتابة الشروط المتداخلة باستخدام العامل المنطقي 'and'.

### شرط If والعوامل المنطقية

```py
# الصيغة
if condition and condition:
    code
```

**مثال:**

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

### If والعامل المنطقي Or

```py
# الصيغة
if condition or condition:
    code
```

**مثال:**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

🌕 أنت تقوم بعمل رائع. لا تستسلم أبدًا لأن الأشياء العظيمة تحتاج وقتًا. لقد أكملت للتو تحديات اليوم التاسع وأنت على بعد 9 خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 9

### تمارين: المستوى 1

1. احصل على إدخال المستخدم باستخدام input("أدخل عمرك: "). إذا كان عمر المستخدم 18 أو أكبر، أعطِ ردًا: أنت كبير بما يكفي لقيادة السيارة. إذا كان أقل من 18 أعطِ ردًا للانتظار لعدد السنوات المتبقية. الناتج:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. قارن قيم my_age و your_age باستخدام if ... else. من الأكبر (أنا أم أنت)؟ استخدم input("أدخل عمرك: ") للحصول على العمر كمدخل. يمكنك استخدام شرط متداخل لطباعة 'year' لفرق سنة واحدة في العمر، 'years' للفروق الأكبر، ونص مخصص إذا كان my_age = your_age. الناتج:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

3. احصل على رقمين من المستخدم باستخدام موجه الإدخال. إذا كان a أكبر من b أعِد a أكبر من b، إذا كان a أصغر من b أعِد a أصغر من b، وإلا a يساوي b. الناتج:

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

### تمارين: المستوى 2

1. اكتب كودًا يعطي درجة للطلاب وفقًا لعلاماتهم:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

2. احصل على الشهر من إدخال المستخدم ثم تحقق مما إذا كان الفصل خريفًا أو شتاءً أو ربيعًا أو صيفًا. إذا كان إدخال المستخدم:
    سبتمبر أو أكتوبر أو نوفمبر، الفصل هو الخريف.
    ديسمبر أو يناير أو فبراير، الفصل هو الشتاء.
    مارس أو أبريل أو مايو، الفصل هو الربيع
    يونيو أو يوليو أو أغسطس، الفصل هو الصيف
3. القائمة التالية تحتوي على بعض الفواكه:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    إذا لم تكن الفاكهة موجودة في القائمة أضفها إلى القائمة واطبع القائمة المعدلة. إذا كانت الفاكهة موجودة اطبع('That fruit already exist in the list')

### تمارين: المستوى 3

1. هنا لدينا قاموس شخص. لا تتردد في تعديله!

```py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

     * تحقق مما إذا كان قاموس الشخص يحتوي على مفتاح skills، إذا كان كذلك اطبع المهارة الوسطى في قائمة skills.
     * تحقق مما إذا كان قاموس الشخص يحتوي على مفتاح skills، إذا كان كذلك تحقق مما إذا كان الشخص لديه مهارة 'Python' واطبع النتيجة.
     * إذا كانت مهارات الشخص تحتوي فقط على JavaScript و React، اطبع('He is a front end developer')، إذا كانت مهارات الشخص تحتوي على Node و Python و MongoDB، اطبع('He is a backend developer')، إذا كانت مهارات الشخص تحتوي على React و Node و MongoDB، اطبع('He is a fullstack developer')، وإلا اطبع('unknown title') - للحصول على نتائج أكثر دقة يمكن تداخل المزيد من الشروط!
     * إذا كان الشخص متزوجًا وإذا كان يعيش في فنلندا، اطبع المعلومات بالتنسيق التالي:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 مبروك! 🎉

[<< اليوم 8](./08_dictionaries.md) | [اليوم 10 >>](./10_loops.md)
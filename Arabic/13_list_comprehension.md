<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 13 - تعبيرات القوائم (List Comprehension)</h1>
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

[<< اليوم 12](./12_modules.md) | [اليوم 14 >>](./14_higher_order_functions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 13](#-اليوم-13)
  - [تعبيرات القوائم (List Comprehension)](#تعبيرات-القوائم-list-comprehension)
  - [دالة Lambda](#دالة-lambda)
    - [إنشاء دالة Lambda](#إنشاء-دالة-lambda)
    - [دالة Lambda داخل دالة أخرى](#دالة-lambda-داخل-دالة-أخرى)
  - [💻 تمارين: اليوم 13](#-تمارين-اليوم-13)

# 📘 اليوم 13

## تعبيرات القوائم (List Comprehension)

تعبير القائمة (list comprehension) في بايثون هو طريقة مدمجة لإنشاء قائمة من متابعة (sequence). إنها طريقة قصيرة لإنشاء قائمة جديدة. تعبير القائمة أسرع بشكل ملحوظ من معالجة قائمة باستخدام حلقة 'for'.

```py
# الصيغة
[expression for i in iterable if condition]
```

**مثال:1**

على سبيل المثال إذا أردت تغيير نص إلى قائمة من الأحرف. يمكنك استخدام عدة طرق. دعنا نرى بعضًا منها:

```py
# طريقة واحدة
language = 'Python'
lst = list(language) # تغيير النص إلى قائمة
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# الطريقة الثانية: تعبير القائمة
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**مثال:2**

على سبيل المثال إذا أردت توليد قائمة من الأرقام

```py
# توليد الأرقام
numbers = [i for i in range(11)]  # لتوليد أرقام من 0 إلى 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# من الممكن إجراء عمليات حسابية أثناء التكرار
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# من الممكن أيضًا إنشاء قائمة من التوبلات
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**مثال:3**

يمكن دمج تعبير القائمة مع تعبير if

```py
# توليد الأرقام الزوجية
even_numbers = [i for i in range(21) if i % 2 == 0]  # لتوليد قائمة أرقام زوجية في نطاق 0 إلى 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# توليد الأرقام الفردية
odd_numbers = [i for i in range(21) if i % 2 != 0]  # لتوليد أرقام فردية في نطاق 0 إلى 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# تصفية الأرقام: دعنا نفلتر الأرقام الزوجية الموجبة من القائمة أدناه
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# تسطيح مصفوفة ثنائية الأبعاد
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## دالة Lambda

دالة lambda هي دالة صغيرة مجهولة بدون اسم. يمكنها أخذ أي عدد من الوسائط، ولكن يمكن أن تحتوي فقط على تعبير واحد. دالة lambda مشابهة للدوال المجهولة في جافاسكريبت. نحتاجها عندما نرغب في كتابة دالة مجهولة داخل دالة أخرى.

### إنشاء دالة Lambda

لإنشاء دالة lambda نستخدم الكلمة المفتاحية 'lambda' متبوعة ببارامتر (بارامترات)، متبوعة بتعبير. انظر الصيغة والمثال أدناه. دالة lambda لا تستخدم return لكنها تعيد التعبير صراحةً.

```py
# الصيغة
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

**مثال:**

```py
# دالة مسماة
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# دعنا نغير الدالة أعلاه إلى دالة lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# دالة lambda ذاتية الاستدعاء
(lambda a, b: a + b)(2,3) # 5 - نحتاج إلى تغليفها في print() لرؤية النتيجة في الطرفية

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# متغيرات متعددة
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### دالة Lambda داخل دالة أخرى

استخدام دالة lambda داخل دالة أخرى.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # دالة power الآن تحتاج وسيطتين للتشغيل، في أقواس دائرية منفصلة
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32
```

🌕 حافظ على العمل الجيد. حافظ على الزخم، فالسماء هي الحد! لقد أكملت للتو تحديات اليوم الثالث عشر وأنت على بعد 13 خطوة في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 13

1. قم بتصفية الأرقام السالبة والصفر فقط في القائمة باستخدام تعبير القائمة
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. قم بتسطيح القائمة التالية من قوائم القوائم إلى قائمة أحادية البعد:

   ```py
   list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. باستخدام تعبير القائمة أنشئ قائمة التوبلات التالية:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. قم بتسطيح القائمة التالية إلى قائمة جديدة:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
5. غيّر القائمة التالية إلى قائمة من القواميس:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
6. غيّر القائمة التالية من القوائم إلى قائمة من النصوص المدمجة:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
7. اكتب دالة lambda يمكنها حل ميل أو مقطع y للدوال الخطية.

🎉 مبروك! 🎉

[<< اليوم 12](./12_modules.md) | [اليوم 14 >>](./14_higher_order_functions.md)
<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 11 - الدوال (Functions)</h1>
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

[<< اليوم 10](./10_loops.md) | [اليوم 12 >>](./12_modules.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 11](#-اليوم-11)
  - [الدوال (Functions)](#الدوال-functions)
    - [تعريف دالة](#تعريف-دالة)
    - [الإعلان عن دالة واستدعاؤها](#الإعلان-عن-دالة-واستدعاؤها)
    - [دالة بدون بارامترات](#دالة-بدون-بارامترات)
    - [دالة تعيد قيمة - الجزء 1](#دالة-تعيد-قيمة---الجزء-1)
    - [دالة مع بارامترات](#دالة-مع-بارامترات)
    - [تمرير الوسائط بمفتاح وقيمة](#تمرير-الوسائط-بمفتاح-وقيمة)
    - [دالة تعيد قيمة - الجزء 2](#دالة-تعيد-قيمة---الجزء-2)
    - [دالة مع بارامترات افتراضية](#دالة-مع-بارامترات-افتراضية)
    - [عدد تعسفي من الوسائط](#عدد-تعسفي-من-الوسائط)
    - [بارامترات افتراضية وتعسفية العدد في الدوال](#بارامترات-افتراضية-وتعسفية-العدد-في-الدوال)
    - [تفكيك القاموس](#تفكيك-القاموس)
    - [عدد تعسفي من الوسائط المسماة](#عدد-تعسفي-من-الوسائط-المسماة)
    - [دالة كبارامتر لدالة أخرى](#دالة-كبارامتر-لدالة-أخرى)
  - [شهادة](#شهادة)
  - [💻 تمارين: اليوم 11](#-تمارين-اليوم-11)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 11

## الدوال (Functions)

حتى الآن رأينا العديد من دوال بايثون المضمنة. في هذا القسم، سنركز على الدوال المخصصة. ما هي الدالة؟ قبل أن نبدأ في إنشاء الدوال، دعونا نتعلم ما هي الدالة ولماذا نحتاجها؟

### تعريف دالة

الدالة هي كتلة قابلة لإعادة الاستخدام من الكود أو عبارات برمجة مصممة لأداء مهمة معينة. لتعريف أو إعلان دالة، توفر بايثون الكلمة المفتاحية 'def'. التالي هو الصيغة لتعريف دالة. يتم تنفيذ كتلة كود الدالة فقط إذا تم استدعاء الدالة أو استدعاؤها.

### الإعلان عن دالة واستدعاؤها

عندما ننشئ دالة، نسمي ذلك إعلان دالة. عندما نبدأ في استخدامها، نسمي ذلك _استدعاء_ أو _استدعاء_ دالة. يمكن إعلان الدوال مع أو بدون بارامترات.

```py
# الصيغة
# الإعلان عن دالة
def function_name():
    codes
    codes
# استدعاء دالة
function_name()
```

### دالة بدون بارامترات

يمكن إعلان الدالة بدون بارامترات.

**مثال:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # استدعاء دالة

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### دالة تعيد قيمة - الجزء 1

الدوال تعيد قيمًا باستخدام عبارة 'return'. إذا لم يكن للدالة عبارة return، فإنها تعيد None. دعنا نعيد كتابة الدوال أعلاه باستخدام return. من الآن فصاعدًا، نحصل على قيمة من الدالة عندما نستدعيها ونطبعها.

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### دالة مع بارامترات

في الدالة يمكننا تمرير أنواع بيانات مختلفة (رقم، نص، قيمة منطقية، قائمة، توبل، قاموس أو مجموعة) كبارامترات.

- بارامتر واحد: إذا كانت دالتنا تأخذ بارامترًا يجب أن نستدعي دالتنا بوسيطة

```py
  # الصيغة
  # الإعلان عن دالة
  def function_name(parameter):
    codes
    codes
  # استدعاء دالة
  print(function_name(argument))
```

**مثال:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- بارامتران: قد تحتوي الدالة أو لا تحتوي على بارامتر أو بارامترات. قد تحتوي الدالة أيضًا على بارامترين أو أكثر. إذا كانت دالتنا تأخذ بارامترات يجب أن نستدعيها بوسائط. دعنا نتحقق من دالة ببارامترين:

```py
  # الصيغة
  # الإعلان عن دالة
  def function_name(para1, para2):
    codes
    codes
  # استدعاء دالة
  print(function_name(arg1, arg2))
```

**مثال:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # يجب تحويل القيمة إلى نص أولاً
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### تمرير الوسائط بمفتاح وقيمة

إذا مررنا الوسائط بمفتاح وقيمة، فإن ترتيب الوسائط لا يهم.

```py
# الصيغة
# الإعلان عن دالة
def function_name(para1, para2):
    codes
    codes
# استدعاء دالة
print(function_name(para1 = 'John', para2 = 'Doe')) # ترتيب الوسائط لا يهم هنا
```

**مثال:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # الترتيب لا يهم
```

### دالة تعيد قيمة - الجزء 2

إذا لم نعد قيمة مع دالة، فستعيد دالتنا 'None' افتراضيًا. لإعادة قيمة مع دالة نستخدم الكلمة المفتاحية 'return' متبوعة بالمتغير الذي نعيده. يمكننا إعادة أي نوع من أنواع البيانات من دالة.

- إعادة نص:
**مثال:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- إعادة رقم:

**مثال:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))
```

- إعادة قيمة منطقية:
  **مثال:**

```py
def is_even (n):
    if n % 2 == 0:
        return True    # return يوقف تنفيذ الدالة الإضافي، مشابه لـ break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- إعادة قائمة:
  **مثال:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### دالة مع بارامترات افتراضية

أحيانًا نمرر قيمًا افتراضية للبارامترات، عندما نستدعي الدالة. إذا لم نمرر وسائط عند استدعاء الدالة، فستُستخدم قيمها الافتراضية.

```py
# الصيغة
# الإعلان عن دالة
def function_name(param = value):
    codes
    codes
# استدعاء دالة
function_name()
function_name(arg)
```

**مثال:**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # يجب تحويل القيمة إلى نص أولاً
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - متوسط الجاذبية على سطح الأرض
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # الجاذبية على سطح القمر
```

### عدد تعسفي من الوسائط

إذا لم نعرف عدد الوسائط التي نمررها إلى دالتنا، يمكننا إنشاء دالة يمكنها أخذ عدد تعسفي من الوسائط بإضافة \* قبل اسم البارامتر.

```py
# الصيغة
# الإعلان عن دالة
def function_name(*args):
    codes
    codes
# استدعاء دالة
function_name(param1, param2, param3,..)
```

**مثال:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # نفس total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### بارامترات افتراضية وتعسفية العدد في الدوال

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

### تفكيك القاموس

يمكنك استدعاء دالة لديها وسائط مسماة باستخدام قاموس مع أسماء مفاتيح مطابقة. تفعل ذلك باستخدام ``**``.

```py
# تعريف دالة تأخذ وسيطتين: 'name' و 'location'
def greet(name, location):
    # طباعة رسالة ترحيبية باستخدام الوسائط المعطاة
    print("Hi there", name, "how is the weather in", location)

# استدعاء الدالة باستخدام وسائط مفتاحية
greet(name="Alice", location="New York")
# الناتج: Hi there Alice how is the weather in New York

# إنشاء قاموس بمفاتيح مطابقة لأسماء بارامترات الدالة
my_dict = {"name": "Alice", "location": "New York"}

# استدعاء الدالة باستخدام تفكيك القاموس
greet(**my_dict)
# عامل ** يفك القاموس، مررًا أزواج المفتاح والقيمة
# كوسائط مفتاحية للدالة.
# الناتج: Hi there Alice how is the weather in New York
```

### عدد تعسفي من الوسائط المسماة

يمكنك أيضًا تعريف دالة لقبول عدد تعسفي من الوسائط المسماة.

```py
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
```

تجنب هذا عمومًا إلا إذا كان مطلوبًا لأنه يجعل فهم ما تقبله الدالة وتفعله أصعب.

### دالة كبارامتر لدالة أخرى

```py
#يمكنك تمرير الدوال كبارامترات
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 لقد حققت الكثير حتى الآن. استمر! لقد أكملت للتو تحديات اليوم الحادي عشر وأنت على بعد 11 خطوة في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## شهادة

حان الوقت الآن للتعبير عن أفكارك حول المؤلف و30DaysOfPython. يمكنك ترك شهادتك على هذا [الرابط](https://testimonial-s3sw.onrender.com/)

## 💻 تمارين: اليوم 11

### تمارين: المستوى 1

1. أعلن دالة 'add_two_numbers'. تأخذ بارامترين وتعيد مجموعًا.
2. تُحسب مساحة الدائرة كما يلي: area = π x r x r. اكتب دالة تحسب 'area_of_circle'.
3. اكتب دالة باسم add_all_nums تأخذ عددًا تعسفيًا من الوسائط وتجمع كل الوسائط. تحقق مما إذا كانت جميع عناصر القائمة أنواع أرقام. إذا لم تكن كذلك، أعط ردًا معقولًا.
4. يمكن تحويل درجة الحرارة من °C إلى °F باستخدام هذه الصيغة: °F = (°C x 9/5) + 32. اكتب دالة تحول °C إلى °F، 'convert_celsius_to_fahrenheit'.
5. اكتب دالة باسم check_season، تأخذ بارامتر شهر وتعيد الفصل: الخريف أو الشتاء أو الربيع أو الصيف.
6. اكتب دالة باسم calculate_slope تعيد ميل معادلة خطية.
7. تُحسب المعادلة التربيعية كما يلي: ax² + bx + c = 0. اكتب دالة تحسب مجموعة حلول معادلة تربيعية، 'solve_quadratic_eqn'.
8. أعلن دالة باسم print_list. تأخذ قائمة كبارامتر وتطبع كل عنصر من عناصر القائمة.
9. أعلن دالة باسم reverse_list. تأخذ مصفوفة كبارامتر وتعيد عكس المصفوفة (استخدم الحلقات).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
```

10. أعلن دالة باسم capitalize_list_items. تأخذ قائمة كبارامتر وتعيد قائمة من العناصر بحرف كبير
11. أعلن دالة باسم add_item. تأخذ قائمة وعنصرًا كبارامترات. تعيد قائمة مع العنصر المضاف في النهاية.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. أعلن دالة باسم remove_item. تأخذ قائمة وعنصرًا كبارامترات. تعيد قائمة مع إزالة العنصر منها.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. أعلن دالة باسم sum_of_numbers. تأخذ بارامتر رقم وتضيف كل الأرقام في هذا النطاق.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. أعلن دالة باسم sum_of_odds. تأخذ بارامتر رقم وتضيف كل الأرقام الفردية في هذا النطاق.
15. أعلن دالة باسم sum_of_even. تأخذ بارامتر رقم وتضيف كل الأرقام الزوجية في ذلك النطاق.

### تمارين: المستوى 2

1. أعلن دالة باسم evens_and_odds. تأخذ عددًا صحيحًا موجبًا كبارامتر وتحسب عدد الأزواج والفردات في العدد.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

2. استدعِ دالتك factorial، تأخذ عددًا صحيحًا كبارامتر وتعيد مضروب العدد
3. استدعِ دالتك 'is_empty'، تأخذ بارامترًا وتتحقق مما إذا كان فارغًا أم لا
4. اكتب دوال مختلفة تأخذ قوائم. يجب أن تحسب calculate_mean، calculate_median، calculate_mode، calculate_range، calculate_variance، calculate_std (الانحراف المعياري).
5. اكتب دالة باسم 'greet' تأخذ وسيطة افتراضية، 'name'. إذا لم يتم توفير وسيطة يجب أن تطبع "Hello, Guest!"، وإلا يجب أن ترحب بالشخص باسمه.

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```

6. أنشئ دالة باسم 'show_args' تأخذ عددًا تعسفيًا من الوسائط المسماة وتطبع أسمائها وقيمها.

   ```py
   show_args(name="Alice", age=30, city="New York")
   # Received: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```

### تمارين: المستوى 3

1. اكتب دالة باسم is_prime، تتحقق مما إذا كان الرقم أوليًا.
2. اكتب دالة تتحقق مما إذا كانت جميع العناصر فريدة في القائمة.
3. اكتب دالة تتحقق مما إذا كانت جميع عناصر القائمة من نفس نوع البيانات.
4. اكتب دالة تتحقق مما إذا كان المتغير المقدم متغير بايثون صالحًا.
5. انتقل إلى مجلد البيانات وافتح ملف countries-data.py.

- أنشئ دالة باسم most_spoken_languages في العالم. يجب أن تعيد أكثر 10 أو 20 لغة تحدثًا في العالم بترتيب تنازلي
- أنشئ دالة باسم most_populated_countries. يجب أن تعيد أكثر 10 أو 20 دولة سكانًا بترتيب تنازلي.

🎉 مبروك! 🎉

[<< اليوم 10](./10_loops.md) | [اليوم 12 >>](./12_modules.md)
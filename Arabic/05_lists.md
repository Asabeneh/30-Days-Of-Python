<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 5 - القوائم (Lists)</h1>
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

[<< اليوم 4](./04_strings.md) | [اليوم 6 >>](./06_tuples.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 5](#-اليوم-5)
  - [القوائم (Lists)](#القوائم-lists)
    - [كيفية إنشاء قائمة](#كيفية-إنشاء-قائمة)
    - [الوصول إلى عناصر القائمة باستخدام الفهرسة الموجبة](#الوصول-إلى-عناصر-القائمة-باستخدام-الفهرسة-الموجبة)
    - [الوصول إلى عناصر القائمة باستخدام الفهرسة السالبة](#الوصول-إلى-عناصر-القائمة-باستخدام-الفهرسة-السالبة)
    - [تفكيك عناصر القائمة (Unpacking)](#تفكيك-عناصر-القائمة-unpacking)
    - [تقطيع عناصر من قائمة (Slicing)](#تقطيع-عناصر-من-قائمة-slicing)
    - [تعديل القوائم](#تعديل-القوائم)
    - [التحقق من العناصر في قائمة](#التحقق-من-العناصر-في-قائمة)
    - [إضافة عناصر إلى قائمة](#إضافة-عناصر-إلى-قائمة)
    - [إدراج عناصر في قائمة](#إدراج-عناصر-في-قائمة)
    - [إزالة عناصر من قائمة](#إزالة-عناصر-من-قائمة)
    - [إزالة عناصر باستخدام Pop](#إزالة-عناصر-باستخدام-pop)
    - [إزالة عناصر باستخدام Del](#إزالة-عناصر-باستخدام-del)
    - [مسح عناصر القائمة](#مسح-عناصر-القائمة)
    - [نسخ قائمة](#نسخ-قائمة)
    - [دمج القوائم](#دمج-القوائم)
    - [عد العناصر في قائمة](#عد-العناصر-في-قائمة)
    - [إيجاد فهرس عنصر](#إيجاد-فهرس-عنصر)
    - [عكس قائمة](#عكس-قائمة)
    - [ترتيب عناصر القائمة](#ترتيب-عناصر-القائمة)
  - [💻 تمارين: اليوم 5](#-تمارين-اليوم-5)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)

# 📘 اليوم 5

## القوائم (Lists)

هناك أربعة أنواع من بيانات المجموعات في بايثون:

- List (قائمة): مجموعة مرتبة وقابلة للتغيير. تسمح بالعناصر المكررة.
- Tuple (توبل): مجموعة مرتبة وغير قابلة للتغيير (immutable). تسمح بالعناصر المكررة.
- Set (مجموعة): مجموعة غير مرتبة، وغير مفهرسة، وغير قابلة للتغيير، ولكن يمكننا إضافة عناصر جديدة إليها. لا تسمح بالعناصر المكررة.
- Dictionary (قاموس): مجموعة غير مرتبة، وقابلة للتغيير، ومفهرسة. لا تسمح بالعناصر المكررة.

القائمة هي مجموعة من أنواع بيانات مختلفة وهي مرتبة وقابلة للتغيير (mutable). يمكن أن تكون القائمة فارغة أو قد تحتوي على عناصر من أنواع بيانات مختلفة.

### كيفية إنشاء قائمة

في بايثون يمكننا إنشاء القوائم بطريقتين:

- باستخدام الدالة المضمنة list()

```py
# الصيغة
lst = list()
```

```py
empty_list = list() # هذه قائمة فارغة، لا توجد عناصر فيها
print(len(empty_list)) # 0
```

- باستخدام الأقواس المربعة []

```py
# الصيغة
lst = []
```

```py
empty_list = [] # هذه قائمة فارغة، لا توجد عناصر فيها
print(len(empty_list)) # 0
```

قوائم بقيم أولية. نستخدم 'len()' لإيجاد طول القائمة.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # قائمة فواكه
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # قائمة خضروات
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # قائمة منتجات حيوانية
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # قائمة تقنيات ويب
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# طباعة القوائم وطولها
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```

```sh
output
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

- يمكن أن تحتوي القوائم على عناصر من أنواع بيانات مختلفة

```py
 lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # قائمة تحتوي على أنواع بيانات مختلفة
```

### الوصول إلى عناصر القائمة باستخدام الفهرسة الموجبة

نصل إلى كل عنصر في القائمة باستخدام الفهرس الخاص به. فهرس القائمة يبدأ من 0. الصورة أدناه توضح بوضوح أين يبدأ الفهرس.
![فهرس القائمة](../images/list_index.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # نصل إلى العنصر الأول باستخدام فهرسه
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# آخر فهرس
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

### الوصول إلى عناصر القائمة باستخدام الفهرسة السالبة

الفهرسة السالبة تعني البدء من النهاية، -1 يشير إلى آخر عنصر، -2 يشير إلى العنصر قبل الأخير.

![فهرس القائمة السالب](../images/list_negative_indexing.png)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

### تفكيك عناصر القائمة (Unpacking)

```py
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

```

```py
# المثال الأول
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# المثال الثاني عن تفكيك القائمة
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# المثال الثالث عن تفكيك القائمة
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

### تقطيع عناصر من قائمة (Slicing)

- الفهرسة الموجبة: يمكننا تحديد نطاق من الفهارس الموجبة بتحديد البداية والنهاية والخطوة، قيمة الإرجاع ستكون قائمة جديدة. (القيم الافتراضية: start = 0, end = len(lst) - 1 (آخر عنصر), step = 1)

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # يعيد جميع الفواكه
# هذا سيعطي نفس النتيجة
all_fruits = fruits[0:] # إذا لم نحدد أين نتوقف فإنه يأخذ كل الباقي
orange_and_mango = fruits[1:3] # لا يشمل الفهرس الأول
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # استخدمنا وسيطة ثالثة، الخطوة. ستأخذ كل عنصر ثاني - ['banana', 'mango']
```

- الفهرسة السالبة: يمكننا تحديد نطاق من الفهارس السالبة بتحديد البداية والنهاية والخطوة، قيمة الإرجاع ستكون قائمة جديدة.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # يعيد جميع الفواكه
orange_and_mango = fruits[-3:-1] # لا يشمل آخر فهرس، ['orange', 'mango']
orange_mango_lemon = fruits[-3:] # هذا سيعطي من -3 إلى النهاية، ['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # خطوة سالبة ستأخذ القائمة بترتيب عكسي، ['lemon', 'mango', 'orange', 'banana']
```

### تعديل القوائم

القائمة مجموعة قابلة للتغيير (mutable) من العناصر. دعنا نعدل قائمة الفواكه.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### التحقق من العناصر في قائمة

التحقق مما إذا كان عنصر ما عضوًا في قائمة باستخدام عامل *in*. انظر المثال أدناه.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### إضافة عناصر إلى قائمة

لإضافة عنصر إلى نهاية قائمة موجودة نستخدم طريقة *append()*.

```py
# الصيغة
lst = list()
lst.append(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

### إدراج عناصر في قائمة

يمكننا استخدام طريقة *insert()* لإدراج عنصر واحد في فهرس محدد في القائمة. لاحظ أن العناصر الأخرى تنتقل إلى اليمين. طريقة *insert()* تأخذ وسيطتين: الفهرس والعنصر المراد إدراجه.

```py
# الصيغة
lst = ['item1', 'item2']
lst.insert(index, item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # إدراج apple بين orange و mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

### إزالة عناصر من قائمة

طريقة الإزالة (remove) تزيل عنصرًا محددًا من القائمة.

```py
# الصيغة
lst = ['item1', 'item2']
lst.remove(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - هذه الطريقة تزيل أول ظهور للعنصر في القائمة
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

### إزالة عناصر باستخدام Pop

طريقة *pop()* تزيل العنصر في الفهرس المحدد (أو آخر عنصر إذا لم يتم تحديد فهرس):

```py
# الصيغة
lst = ['item1', 'item2']
lst.pop()       # آخر عنصر
lst.pop(index)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### إزالة عناصر باستخدام Del

الكلمة المفتاحية *del* تزيل العنصر في الفهرس المحدد ويمكن استخدامها أيضًا لحذف عناصر ضمن نطاق فهارس. يمكنها أيضًا حذف القائمة بالكامل.

```py
# الصيغة
lst = ['item1', 'item2']
del lst[index] # عنصر واحد فقط
del lst        # لحذف القائمة بالكامل
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # هذا يحذف العناصر بين الفهارس المعطاة، لذا لا يحذف العنصر ذو الفهرس 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # هذا يجب أن يعطي: NameError: name 'fruits' is not defined
```

### مسح عناصر القائمة

طريقة *clear()* تفرغ القائمة:

```py
# الصيغة
lst = ['item1', 'item2']
lst.clear()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

### نسخ قائمة

من الممكن نسخ قائمة بإعادة تعيينها إلى متغير جديد بالطريقة التالية: list2 = list1. الآن، list2 هي مرجع لـ list1، أي تغييرات نقوم بها في list2 ستعدل الأصل list1 أيضًا. ولكن هناك حالات كثيرة لا نرغب فيها بتعديل الأصل بل نريد نسخة مختلفة. إحدى طرق تجنب المشكلة أعلاه هي استخدام 'copy()'.

```py
# الصيغة
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### دمج القوائم

هناك عدة طرق لدمج أو ربط قائمتين أو أكثر في بايثون.

- عامل الجمع (+)

```py
# الصيغة
list3 = list1 + list2
```

```py
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- الدمج باستخدام طريقة extend()
  طريقة *extend()* تسمح بإلحاق قائمة بقائمة أخرى. انظر المثال أدناه.

```py
# الصيغة
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
```

```py
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### عد العناصر في قائمة

طريقة *count()* تعيد عدد المرات التي يظهر فيها عنصر في القائمة:

```py
# الصيغة
lst = ['item1', 'item2']
lst.count(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### إيجاد فهرس عنصر

طريقة *index()* تعيد فهرس عنصر في القائمة:

```py
# الصيغة
lst = ['item1', 'item2']
lst.index(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2، أول ظهور
```

### عكس قائمة

طريقة *reverse()* تعكس ترتيب القائمة.

```py
# الصيغة
lst = ['item1', 'item2']
lst.reverse()

```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

### ترتيب عناصر القائمة

لترتيب القوائم يمكننا استخدام طريقة 'sort()' أو الدالة المضمنة 'sorted()'. طريقة 'sort()' تعيد ترتيب عناصر القائمة بترتيب تصاعدي وتعدل القائمة الأصلية. إذا كانت وسيطة _sort()_ reverse تساوي true، فسترتب القائمة بترتيب تنازلي.

- sort(): هذه الطريقة تعدل القائمة الأصلية

  ```py
  # الصيغة
  lst = ['item1', 'item2']
  lst.sort()                # تصاعدي
  lst.sort(reverse=True)    # تنازلي
  ```

  **مثال:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits.sort()
  print(fruits)             # مرتبة أبجديًا، ['banana', 'lemon', 'mango', 'orange']
  fruits.sort(reverse=True)
  print(fruits) # ['orange', 'mango', 'lemon', 'banana']
  ages = [22, 19, 24, 25, 26, 24, 25, 24]
  ages.sort()
  print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

  ages.sort(reverse=True)
  print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
  ```

  sorted(): تعيد القائمة المرتبة دون تعديل القائمة الأصلية
  **مثال:**

  ```py
  fruits = ['banana', 'orange', 'mango', 'lemon']
  print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
  # ترتيب عكسي
  fruits = ['banana', 'orange', 'mango', 'lemon']
  fruits = sorted(fruits,reverse=True)
  print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
  ```

🌕 أنت مجتهد وقد حققت بالفعل الكثير. لقد أكملت للتو تحديات اليوم الخامس وأنت على بعد 5 خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 5

### تمارين: المستوى 1

1. أعلن قائمة فارغة
2. أعلن قائمة بأكثر من 5 عناصر
3. جد طول قائمتك
4. احصل على العنصر الأول والعنصر الأوسط وآخر عنصر في القائمة
5. أعلن قائمة باسم mixed_data_types، ضع فيها (اسمك، عمرك، طولك، الحالة الاجتماعية، عنوانك)
6. أعلن متغير قائمة باسم it_companies وقم بتعيين القيم الأولية Facebook, Google, Microsoft, Apple, IBM, Oracle و Amazon.
7. اطبع القائمة باستخدام 'print()'
8. اطبع عدد الشركات في القائمة
9. اطبع أول شركة وشركة وسط وآخر شركة
10. اطبع القائمة بعد تعديل إحدى الشركات
11. أضف شركة تقنية إلى it_companies
12. أدخل شركة تقنية في منتصف قائمة الشركات
13. غيّر اسم إحدى شركات it_companies إلى أحرف كبيرة (IBM مستثناة!)
14. اربط it_companies مع نص '#;&nbsp; '
15. تحقق مما إذا كانت شركة معينة موجودة في قائمة it_companies.
16. رتب القائمة باستخدام طريقة sort()
17. اعكس القائمة بترتيب تنازلي باستخدام طريقة reverse()
18. اقطع أول 3 شركات من القائمة
19. اقطع آخر 3 شركات من القائمة
20. اقطع الشركة أو الشركات الوسطى من القائمة
21. أزل أول شركة تقنية من القائمة
22. أزل الشركة أو الشركات الوسطى من القائمة
23. أزل آخر شركة تقنية من القائمة
24. أزل جميع الشركات التقنية من القائمة
25. احذف قائمة الشركات التقنية
26. ادمج القائمتين التاليتين:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```

27. بعد دمج القائمتين في السؤال 26. انسخ القائمة المدمجة وعيّنها لمتغير full_stack، ثم أدخل Python و SQL بعد Redux.

### تمارين: المستوى 2

1. التالية هي قائمة بأعمار 10 طلاب:

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

- رتب القائمة وجد أصغر وأكبر عمر
- أضف أصغر عمر وأكبر عمر مرة أخرى إلى القائمة
- جد العمر الوسيط (عنصر وسطي واحد أو عنصرين وسيطين مقسومين على اثنين)
- جد متوسط العمر (مجموع كل العناصر مقسومًا على عددها)
- جد نطاق الأعمار (أكبر عمر ناقص أصغر عمر)
- قارن قيمة (أصغر عمر - المتوسط) و (أكبر عمر - المتوسط)، استخدم 'abs()'

2. جد الدولة/الدول الوسطى في [قائمة الدول](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
3. قسم قائمة الدول إلى قائمتين متساويتين إذا كان العدد زوجيًا، وإن لم يكن كذلك فدولة إضافية للنصف الأول.
4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. افك أول ثلاث دول والباقي كدول اسكندنافية.

🎉 مبروك! 🎉

[<< اليوم 4](./04_strings.md) | [اليوم 6 >>](./06_tuples.md)

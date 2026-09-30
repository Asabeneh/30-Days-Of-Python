<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 7 - المجموعات (Sets)</h1>
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

[<< اليوم 6](./06_tuples.md) | [اليوم 8 >>](./08_dictionaries.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 7](#-اليوم-7)
  - [المجموعات (Sets)](#المجموعات-sets)
    - [إنشاء مجموعة](#إنشاء-مجموعة)
    - [الحصول على طول المجموعة](#الحصول-على-طول-المجموعة)
    - [الوصول إلى عناصر المجموعة](#الوصول-إلى-عناصر-المجموعة)
    - [التحقق من عنصر](#التحقق-من-عنصر)
    - [إضافة عناصر إلى مجموعة](#إضافة-عناصر-إلى-مجموعة)
    - [إزالة عناصر من مجموعة](#إزالة-عناصر-من-مجموعة)
    - [مسح عناصر المجموعة](#مسح-عناصر-المجموعة)
    - [حذف مجموعة](#حذف-مجموعة)
    - [تحويل قائمة إلى مجموعة](#تحويل-قائمة-إلى-مجموعة)
    - [دمج المجموعات](#دمج-المجموعات)
    - [إيجاد عناصر التقاطع](#إيجاد-عناصر-التقاطع)
    - [التحقق من المجموعة الفرعية والمجموعة الفائقة](#التحقق-من-المجموعة-الفرعية-والمجموعة-الفائقة)
    - [التحقق من الفرق بين مجموعتين](#التحقق-من-الفرق-بين-مجموعتين)
    - [إيجاد الفرق المتماثل بين مجموعتين](#إيجاد-الفرق-المتماثل-بين-مجموعتين)
    - [دمج المجموعات](#دمج-المجموعات-1)
  - [💻 تمارين: اليوم 7](#-تمارين-اليوم-7)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 7

## المجموعات (Sets)

المجموعة (set) هي مجموعة من العناصر. دعني أعيدك إلى درس الرياضيات في المدرسة الابتدائية أو الثانوية. تعريف المجموعة في الرياضيات يمكن تطبيقه أيضًا في بايثون. المجموعة هي مجموعة من العناصر المتميزة غير المرتبة وغير المفهرسة. في بايثون، تُستخدم المجموعة لتخزين العناصر الفريدة، ومن الممكن إيجاد _الدمج (union)_، _التقاطع (intersection)_، _الفرق (difference)_، _الفرق المتماثل (symmetric difference)_، _المجموعة الفرعية (subset)_، _المجموعة الفائقة (superset)_ و _المجموعة المنفصلة (disjoint set)_ بين المجموعات.

### إنشاء مجموعة

لإنشاء مجموعة فارغة، نستخدم الدالة set(). الأقواس المعقوفة الفارغة {} تنشئ قاموسًا (dictionary).

- إنشاء مجموعة فارغة

```py
# الصيغة
st = set()
```

- إنشاء مجموعة بعناصر أولية

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
```

**مثال:**

```py
# الصيغة
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### الحصول على طول المجموعة

نستخدم طريقة **len()** لإيجاد طول المجموعة.

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

### الوصول إلى عناصر المجموعة

نستخدم الحلقات (loops) للوصول إلى العناصر. سنرى ذلك في قسم الحلقات.

### التحقق من عنصر

للتحقق مما إذا كان عنصر موجودًا في مجموعة نستخدم عامل العضوية 'in'.

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
print("هل المجموعة st تحتوي على item3؟ ", 'item3' in st) # هل المجموعة st تحتوي على item3؟ True
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### إضافة عناصر إلى مجموعة

بمجرد إنشاء مجموعة، لا يمكننا تغيير أي عنصر ولكن يمكننا إضافة عناصر إضافية.

- إضافة عنصر واحد باستخدام 'add()'

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

- إضافة عناصر متعددة باستخدام 'update()'
  تسمح 'update()' بإضافة عناصر متعددة إلى مجموعة. تأخذ 'update()' وسيطة قائمة.

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### إزالة عناصر من مجموعة

يمكننا إزالة عنصر من مجموعة باستخدام طريقة 'remove()'. إذا لم يتم العثور على العنصر، ستثير طريقة 'remove()' خطأً، لذا من الجيد التحقق مما إذا كان العنصر موجودًا في المجموعة. ومع ذلك، طريقة 'discard()' لا تثير أي أخطاء.

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

طريقة pop() تزيل عنصرًا عشوائيًا من المجموعة وتعيد العنصر الذي تمت إزالته.

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # يزيل عنصرًا عشوائيًا من المجموعة

```

إذا كنا مهتمين بالعنصر الذي تمت إزالته.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
```

### مسح عناصر المجموعة

إذا أردنا مسح أو تفريغ المجموعة نستخدم طريقة 'clear'.

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### حذف مجموعة

إذا أردنا حذف المجموعة نفسها نستخدم عامل 'del'.

```py
# الصيغة
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### تحويل قائمة إلى مجموعة

يمكننا تحويل قائمة إلى مجموعة ومجموعة إلى قائمة. تحويل القائمة إلى مجموعة يزيل التكرارات ويتم الاحتفاظ فقط بالعناصر الفريدة.

```py
# الصيغة
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - الترتيب عشوائي، لأن المجموعات بشكل عام غير مرتبة
```

**مثال:**

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### دمج المجموعات

يمكننا دمج مجموعتين باستخدام طريقة 'union()' أو 'update()' أو الرمز '|'.

- Union
  هذه الطريقة تعيد مجموعة جديدة

```py
# الصيغة
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) # st3 = st1 | st2
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# أو باستخدام: print(fruits | vegetables)
```

- Update
  هذه الطريقة تُدرج مجموعة في مجموعة معطاة

```py
# الصيغة
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # محتويات st2 تضاف إلى st1
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

### إيجاد عناصر التقاطع

التقاطع (intersection) يعيد مجموعة من العناصر الموجودة في كلتا المجموعتين أو باستخدام الرمز _&_. انظر المثال.

```py
# الصيغة
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# أو باستخدام: st1 & st2
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon
```

### التحقق من المجموعة الفرعية والمجموعة الفائقة

يمكن أن تكون مجموعة مجموعة فرعية (subset) أو مجموعة فائقة (superset) لمجموعات أخرى:

- مجموعة فرعية: 'issubset()'
- مجموعة فائقة: 'issuperset()'

```py
# الصيغة
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False، لأنها مجموعة فائقة
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### التحقق من الفرق بين مجموعتين

يعيد الفرق بين مجموعتين أو باستخدام الرمز _-_.

```py
# الصيغة
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'} - النتيجة غير مرتبة (خاصية المجموعات)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python
```

### إيجاد الفرق المتماثل بين مجموعتين

يعيد الفرق المتماثل (symmetric difference) بين مجموعتين. يعني أنه يعيد مجموعة تحتوي على جميع العناصر من كلتا المجموعتين، باستثناء العناصر الموجودة في كلتا المجموعتين، رياضيًا: (A\B) ∪ (B\A)

```py
# الصيغة
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# يعني (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon
```

### دمج المجموعات

إذا لم يكن لمجموعتين عنصر مشترك أو عناصر مشتركة، نسميهما مجموعتين منفصلتين (disjoint sets). يمكننا التحقق مما إذا كانت المجموعتان منفصلتين أم لا باستخدام طريقة 'isdisjoint()'.

```py
# الصيغة
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

**مثال:**

```py
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True، لأنه لا توجد عناصر مشتركة

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False، هناك عناصر مشتركة {'o', 'n'}
```

🌕 أنت نجم صاعد. لقد أكملت للتو تحديات اليوم السابع وأنت على بعد 7 خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 7

```py
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### تمارين: المستوى 1

1. جد طول المجموعة it_companies
2. أضف 'Twitter' إلى it_companies
3. أدخل عدة شركات تقنية مرة واحدة إلى المجموعة it_companies
4. أزل إحدى الشركات من المجموعة it_companies
5. ما الفرق بين remove و discard

### تمارين: المستوى 2

1. ادمج A و B
2. جد تقاطع A و B
3. هل A مجموعة فرعية من B
4. هل A و B مجموعتان منفصلتان
5. ادمج A مع B و B مع A
6. ما الفرق المتماثل بين A و B
7. احذف المجموعتين بالكامل

### تمارين: المستوى 3

1. حوّل الأعمار إلى مجموعة وقارن طول القائمة والمجموعة، أيهما أكبر؟
2. اشرح الفرق بين أنواع البيانات التالية: string، list، tuple و set
3. _I am a teacher and I love to inspire and teach people._ كم كلمة فريدة تم استخدامها في الجملة؟ استخدم طرق split والمجموعة للحصول على الكلمات الفريدة.

🎉 مبروك! 🎉

[<< اليوم 6](./06_tuples.md) | [اليوم 8 >>](./08_dictionaries.md)

<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 6 - التوبل (Tuples)</h1>
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

[<< اليوم 5](./05_lists.md) | [اليوم 7 >>](./07_sets.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 6](#-اليوم-6)
  - [التوبل (Tuples)](#التوبل-tuples)
    - [إنشاء توبل](#إنشاء-توبل)
    - [طول التوبل](#طول-التوبل)
    - [الوصول إلى عناصر التوبل](#الوصول-إلى-عناصر-التوبل)
    - [تقطيع التوبل](#تقطيع-التوبل)
    - [تحويل التوبل إلى قائمة](#تحويل-التوبل-إلى-قائمة)
    - [التحقق من عنصر في توبل](#التحقق-من-عنصر-في-توبل)
    - [دمج التوبل](#دمج-التوبل)
    - [حذف التوبل](#حذف-التوبل)
  - [💻 تمارين: اليوم 6](#-تمارين-اليوم-6)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)

# 📘 اليوم 6

## التوبل (Tuples)

التوبل (tuple) هو مجموعة من أنواع بيانات مختلفة وهي مرتبة وغير قابلة للتغيير (immutable). تُكتب التوبل بين قوسين دائريين (). بمجرد إنشاء توبل، لا يمكننا تغيير قيمها. لا يمكننا استخدام طرق add، insert، remove في التوبل لأنها غير قابلة للتعديل (mutable). على عكس القائمة، التوبل لديها طرق قليلة. الطرق المتعلقة بالتوبل:

- tuple(): لإنشاء توبل فارغ
- count(): لعد عدد عنصر محدد في التوبل
- index(): لإيجاد فهرس عنصر محدد في التوبل
- عامل `+`: لدمج توبلين أو أكثر وإنشاء توبل جديد

### إنشاء توبل

- توبل فارغ: إنشاء توبل فارغ

  ```py
  # الصيغة
  empty_tuple = ()
  # أو باستخدام مُنشئ التوبل
  empty_tuple = tuple()
  ```

- توبل بقيم أولية

  ```py
  # الصيغة
  tpl = ('item1', 'item2','item3')
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  ```

### طول التوبل

نستخدم طريقة 'len()' للحصول على طول التوبل.

```py
# الصيغة
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### الوصول إلى عناصر التوبل

- الفهرسة الموجبة
  مشابه لنوع بيانات القائمة، نستخدم الفهرسة الموجبة أو السالبة للوصول إلى عناصر التوبل.
  ![الوصول إلى عناصر التوبل](../images/tuples_index.png)

  ```py
  # الصيغة
  tpl = ('item1', 'item2', 'item3')
  first_item = tpl[0]
  second_item = tpl[1]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[0]
  second_fruit = fruits[1]
  last_index =len(fruits) - 1
  last_fruit = fruits[last_index]
  ```

- الفهرسة السالبة
  الفهرسة السالبة تعني البدء من النهاية، -1 يشير إلى آخر عنصر، -2 يشير إلى العنصر قبل الأخير وسالب طول القائمة/التوبل يشير إلى العنصر الأول.
  ![فهرسة التوبل السالبة](../images/tuple_negative_indexing.png)

  ```py
  # الصيغة
  tpl = ('item1', 'item2', 'item3','item4')
  first_item = tpl[-4]
  second_item = tpl[-3]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[-4]
  second_fruit = fruits[-3]
  last_fruit = fruits[-1]
  ```

### تقطيع التوبل

يمكننا تقطيع توبل فرعي بتحديد نطاق من الفهارس حيث نبدأ وأين ننتهي في التوبل، قيمة الإرجاع ستكون توبل جديد بالعناصر المحددة.

- نطاق الفهارس الموجبة

  ```py
  # الصيغة
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # جميع العناصر
  all_items = tpl[0:]         # جميع العناصر
  middle_two_items = tpl[1:3]  # لا يشمل العنصر في الفهرس 3
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # جميع العناصر
  all_fruits= fruits[0:]      # جميع العناصر
  orange_mango = fruits[1:3]  # لا يشمل العنصر في الفهرس 3
  orange_to_the_rest = fruits[1:]
  ```

- نطاق الفهارس السالبة

  ```py
  # الصيغة
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # جميع العناصر
  middle_two_items = tpl[-3:-1]  # لا يشمل العنصر في الفهرس 3 (-1)
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # جميع العناصر
  orange_mango = fruits[-3:-1]  # لا يشمل العنصر في الفهرس 3
  orange_to_the_rest = fruits[-3:]
  ```

### تحويل التوبل إلى قائمة

يمكننا تحويل التوبل إلى قائمة والقائمة إلى توبل. التوبل غير قابل للتغيير، إذا أردنا تعديل توبل يجب تحويله إلى قائمة.

```py
# الصيغة
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### التحقق من عنصر في توبل

يمكننا التحقق مما إذا كان عنصر موجودًا أم لا في التوبل باستخدام 'in'، يعيد قيمة منطقية.

```py
# الصيغة
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

### دمج التوبل

يمكننا دمج توبلين أو أكثر باستخدام عامل +

```py
# الصيغة
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

### حذف التوبل

ليس من الممكن إزالة عنصر واحد من توبل ولكن من الممكن حذف التوبل نفسه باستخدام 'del'.

```py
# الصيغة
tpl1 = ('item1', 'item2', 'item3')
del tpl1

```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

🌕 أنت شجاع جدًا، لقد وصلت إلى هذا الحد. لقد أكملت للتو تحديات اليوم السادس وأنت على بعد 6 خطوات في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك ولعضلاتك.

## 💻 تمارين: اليوم 6

### تمارين: المستوى 1

1. أنشئ توبل فارغًا
2. أنشئ توبل يحتوي على أسماء أخواتك وإخوتك (الأشقاء الوهميون مقبولون)
3. ادمج توبل الإخوة وتوبل الأخوات وعيّن الناتج إلى siblings
4. كم عدد الأشقاء لديك؟
5. عدّل توبل siblings وأضف اسم والدك ووالدتك وعيّن الناتج إلى family_members

### تمارين: المستوى 2

1. افك الأشقاء والوالدين من family_members
2. أنشئ توبل للفواكه والخضروات والمنتجات الحيوانية. ادمج التوبلات الثلاثة وعيّنها لمتغير اسمه food_stuff_tp.
3. حوّل توبل food_stuff_tp إلى قائمة food_stuff_lt
4. اقطع العنصر أو العناصر الوسطى من توبل food_stuff_tp أو قائمة food_stuff_lt.
5. اقطع العناصر الثلاثة الأولى والعناصر الثلاثة الأخيرة من قائمة food_stuff_lt
6. احذف توبل food_stuff_tp بالكامل
7. تحقق مما إذا كان عنصر موجودًا في التوبل:

- تحقق مما إذا كانت 'Estonia' دولة نوردية
- تحقق مما إذا كانت 'Iceland' دولة نوردية

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```

[<< اليوم 5](./05_lists.md) | [اليوم 7 >>](./07_sets.md)

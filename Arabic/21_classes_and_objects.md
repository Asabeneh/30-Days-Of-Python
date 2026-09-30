<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 21 - الفئات والكائنات</h1>
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

[<< اليوم 20](./20_python_package_manager.md) | [اليوم 22 >>](./22_web_scraping.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 21](#-اليوم-21)
  - [الفئات والكائنات](#الفئات-والكائنات)
    - [إنشاء فئة](#إنشاء-فئة)
    - [إنشاء كائن](#إنشاء-كائن)
    - [منشئ الفئة](#منشئ-الفئة)
    - [طرق الكائن](#طرق-الكائن)
    - [الطرق الافتراضية للكائن](#الطرق-الافتراضية-للكائن)
    - [طريقة لتعديل القيم الافتراضية للفئة](#طريقة-لتعديل-القيم-الافتراضية-للفئة)
    - [الوراثة](#الوراثة)
    - [استبدال طريقة الفئة الأم](#استبدال-طريقة-الفئة-الأم)
  - [💻 تمارين: اليوم 21](#-تمارين-اليوم-21)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)

# 📘 اليوم 21

## الفئات والكائنات

بايثون هي لغة برمجة كائنية التوجه. كل شيء في بايثون هو كائن، بخصائصه وطرقه. الرقم والنص والقائمة والقاموس والتوبل والمجموعة إلخ. المستخدمة في برنامج هي كائن من فئة مضمنة مقابلة. ننشئ فئة لإنشاء كائن. الفئة تشبه منشئ الكائن، أو "مخططًا" ('blueprint') لإنشاء الكائنات. نقوم بإنشاء كائن من فئة ('instantiate') لإنشاء كائن. الفئة تحدد السمات وسلوك الكائن، بينما الكائن، من ناحية أخرى، يمثل الفئة.

لقد كنا نعمل مع الفئات والكائنات منذ بداية هذا التحدي دون أن نعلم. كل عنصر في برنامج بايثون هو كائن من فئة.
دعنا نتحقق مما إذا كان كل شيء في بايثون فئة:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### إنشاء فئة

لإنشاء فئة نحتاج إلى الكلمة المفتاحية 'class' متبوعة بالاسم والنقطتين. يجب أن يكون اسم الفئة بأسلوب 'CamelCase'.

```sh
# صيغة
class ClassName:
  الكود هنا
```

**مثال:**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### إنشاء كائن

يمكننا إنشاء كائن عن طريق استدعاء الفئة.

```py
p = Person()
print(p)
```

### منشئ الفئة

في الأمثلة أعلاه، أنشأنا كائنًا من فئة 'Person'. ومع ذلك، فإن الفئة بدون منشئ ليست مفيدة حقًا في التطبيقات الحقيقية. دعنا نستخدم دالة المنشئ لجعل فئتنا أكثر فائدة. مثل دالة المنشئ في جافا أو جافا سكريبت، لدى بايثون أيضًا دالة منشئ مضمنة **__init__**(). دالة المنشئ **__init__** لها وسيلة 'self' والتي تمثل مرجعًا للمثيل الحالي للفئة.

**أمثلة:**

```py
class Person:
      def __init__ (self, name):
        # self يسمح بربط الوسيلة بالفئة
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# المخرجات
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

دعنا نضيف المزيد من الوسائط لدالة المنشئ.

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# المخرجات
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### طرق الكائن

يمكن أن يكون للكائنات طرق. الطرق هي دوال تنتمي إلى الكائن.

**مثال:**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# المخرجات
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

### الطرق الافتراضية للكائن

أحيانًا، قد ترغب في الحصول على قيم افتراضية لطرق الكائن الخاصة بك. إذا أعطينا قيمًا افتراضية للوسائط في المنشئ، يمكننا تجنب الأخطاء عندما نستدعي أو ننشئ فئتنا دون وسائط. دعنا نرى كيف يبدو ذلك:

**مثال:**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# المخرجات
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

### طريقة لتعديل القيم الافتراضية للفئة

في المثال أدناه، فئة 'person'، جميع وسائط المنشئ لها قيم افتراضية. بالإضافة إلى ذلك، لدينا وسيلة 'skills'، والتي يمكننا الوصول إليها باستخدام طريقة. دعنا ننشئ طريقة 'add_skill' لإضافة مهارات إلى قائمة 'skills'.

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# المخرجات
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### الوراثة

باستخدام الوراثة يمكننا إعادة استخدام كود الفئة الأم. تسمح لنا الوراثة بتعريف فئة ترث جميع الطرق والخصائص من الفئة الأم. الفئة الأم أو super أو الفئة الأساسية هي الفئة التي تعطي جميع الطرق والخصائص. الفئة الفرعية (Child class) هي الفئة التي ترث من فئة أخرى أو فئة الأم.
دعنا ننشئ فئة طالب (Student) بوراثة من فئة person.

```py
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

```sh
المخرجات
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

لم نستدع منشئ **__init__**() في الفئة الفرعية. إذا لم نستدعه، فلا يزال بإمكاننا الوصول إلى جميع الخصائص من الفئة الأم. لكن إذا استدعينا المنشئ، يمكننا الوصول إلى خصائص الفئة الأم باستدعاء 'super()'.
يمكننا إضافة طريقة جديدة إلى الفئة الفرعية أو يمكننا استبدال طرق الفئة الأم بإنشاء نفس اسم الطريقة في الفئة الفرعية. عندما نضيف دالة **__init__**()، لن ترث الفئة الفرعية بعد الآن دالة **__init__**() الخاصة بالفئة الأم.

### استبدال طريقة الفئة الأم

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

يمكننا استخدام الدالة المضمنة 'super()' أو اسم الفئة الأم 'Person' ليرث تلقائيًا الطرق والخصائص من فئته الأم. في المثال أعلاه قمنا باستبدال طريقة الفئة الأم. طريقة الفئة الفرعية لها ميزة مختلفة، يمكنها تحديد ما إذا كان الجنس ذكرًا أم أنثى وتعيين الضمير المناسب ('He/She').

🌕 الآن، أنت مشحون بالكامل بقوة برمجة خارقة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 21

### تمارين: المستوى 1

1. لدى بايثون وحدة تسمى 'statistics' ويمكننا استخدام هذه الوحدة للقيام بجميع الحسابات الإحصائية. ومع ذلك، لتعلم كيفية إنشاء دالة وإعادة استخدامها، دعنا نحاول تطوير برنامج يحسب مقياس النزعة المركزية لعينة (المتوسط، الوسيط، المنوال) ومقياس التباين (المدى، التباين، الانحراف المعياري). بالإضافة إلى تلك المقاييس، أوجد الحد الأدنى والحد الأقصى والعدد والمئين وتوزيع التكرار للعينة. يمكنك إنشاء فئة تسمى 'Statistics' وإنشاء جميع الدوال التي تقوم بحسابات إحصائية كطرق لفئة 'Statistics'. تحقق من المخرجات أدناه.

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# يجب أن تبدو مخرجاتك هكذا
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### تمارين: المستوى 2

1. أنشئ فئة تسمى 'PersonAccount'. لديها خصائص 'firstname' و 'lastname' و 'incomes' و 'expenses' ولديها طرق 'total_income' و 'total_expense' و 'account_info' و 'add_income' و 'add_expense' و 'account_balance'. 'Incomes' هي مجموعة من الدخول ووصفها. نفس الشيء بالنسبة للـ 'expenses'.

🎉 مبروك! 🎉

[<< اليوم 20](./20_python_package_manager.md) | [اليوم 22 >>](./22_web_scraping.md)
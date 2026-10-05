<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 21 — کلاسز اور آبجیکٹس</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 20](./20_python_package_manager.md) | [فہرست](./readme.md) | [اگلا دن: 22](./22_web_scraping.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 21](#day-21-section-1)
  - [کلاسز اور آبجیکٹس](#day-21-section-2)
    - [کلاس بنانا](#day-21-section-3)
    - [آبجیکٹ بنانا](#day-21-section-4)
    - [کلاس کی ابتدا: constructor](#day-21-section-5)
    - [آبجیکٹ میتھڈز](#day-21-section-6)
    - [طے شدہ قدروں والے میتھڈز](#day-21-section-7)
    - [آبجیکٹ کی قدریں بدلنے والا میتھڈ](#day-21-section-8)
    - [وراثت: Inheritance](#day-21-section-9)
    - [والدین کلاس کے میتھڈ کا متبادل](#day-21-section-10)
  - [💻 مشقیں — دن 21](#day-21-section-11)
    - [مشقیں: درجہ 1](#day-21-section-12)
    - [مشقیں: درجہ 2](#day-21-section-13)

<a id="day-21-section-1"></a>

# 📘 دن 21

<a id="day-21-section-2"></a>

## کلاسز اور آبجیکٹس

پائتھن آبجیکٹ اورینٹڈ پروگرامنگ کی حمایت کرتا ہے۔ پروگرام میں استعمال ہونے والے اعداد، سٹرنگز، لسٹس، ڈکشنریز، ٹپلز اور سیٹس اپنی متعلقہ کلاسز کے آبجیکٹس ہیں۔ ہر آبجیکٹ کے اوصاف اور میتھڈ ہو سکتے ہیں۔ کلاس آبجیکٹ بنانے کا خاکہ ہے؛ اس سے instance بنا کر آبجیکٹ حاصل کرتے ہیں۔ کلاس اوصاف اور رویہ بیان کرتی ہے، جبکہ آبجیکٹ اس کی مخصوص مثال ہوتا ہے۔

اس چیلنج کے آغاز سے ہم کلاسز اور آبجیکٹس استعمال کر رہے ہیں، چاہے یہ اصطلاحیں پہلے معلوم نہ تھیں۔ مختلف قدروں کی کلاس دیکھیں۔

<div dir="ltr">

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

</div>

<a id="day-21-section-3"></a>

### کلاس بنانا

`class` کے بعد نام اور کولن لکھیں۔ کلاس کے نام کے لیے **CamelCase** انداز استعمال کریں۔

<div dir="ltr">

```sh
# syntax
class ClassName:
  code goes here
```

</div>

**مثال:**

<div dir="ltr">

```py
class Person:
  pass
print(Person)
```

</div>

<div dir="ltr">

```sh
<__main__.Person object at 0x10804e510>
```

</div>

<a id="day-21-section-4"></a>

### آبجیکٹ بنانا

کلاس کو کال کر کے آبجیکٹ بنا سکتے ہیں۔

<div dir="ltr">

```py
p = Person()
print(p)
```

</div>

<a id="day-21-section-5"></a>

### کلاس کی ابتدا: constructor

اوپر `Person` سے آبجیکٹ بنایا۔ آبجیکٹ کی ابتدائی قدریں مقرر کرنے کے لیے `__init__()` لکھیں۔ اسے عام طور پر constructor کہا جاتا ہے، اگرچہ تکنیکی طور پر یہ نئے instance کو initialize کرتا ہے۔ اس کا `self` پیرامیٹر موجودہ instance کا حوالہ ہے۔

**مثالیں:**

<div dir="ltr">

```py
class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

</div>

<div dir="ltr">

```sh
# output
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

</div>

مزید پیرامیٹرز شامل کریں۔

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
# output
Asabeneh
Yetayeh
250
Finland
Helsinki
```

</div>

<a id="day-21-section-6"></a>

### آبجیکٹ میتھڈز

آبجیکٹ سے متعلق فنکشنز کو میتھڈز کہتے ہیں۔

**مثال:**

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

</div>

<a id="day-21-section-7"></a>

### طے شدہ قدروں والے میتھڈز

`__init__()` کے پیرامیٹرز کو طے شدہ قدریں دیں تو بعض آرگیومنٹس کے بغیر بھی instance بن سکتا ہے۔

**مثال:**

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

</div>

<a id="day-21-section-8"></a>

### آبجیکٹ کی قدریں بدلنے والا میتھڈ

اگلی مثال میں ابتدائی پیرامیٹرز کی طے شدہ قدریں ہیں، اور `skills` لسٹ بھی ہے۔ `add_skill()` سے اس میں نئی مہارت شامل کریں۔

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

</div>

<a id="day-21-section-9"></a>

### وراثت: Inheritance

وراثت سے بنیادی یا والدین (*parent/base/super*) کلاس کا کوڈ دوبارہ استعمال ہوتا ہے۔ نئی یا اولاد (*child*) کلاس اس کے میتھڈز اور رویہ حاصل کرتی ہے۔ `Person` سے `Student` بنائیں۔

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
output
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

</div>

اگر child کلاس اپنا `__init__()` نہ لکھے تو parent والا استعمال ہو سکتا ہے۔ اپنا لکھنے پر parent کی ابتدائی ترتیب خود نہیں چلتی؛ ضرورت ہو تو `super().__init__()` بلائیں۔ نیا میتھڈ شامل کر سکتے ہیں یا اسی نام سے parent میتھڈ کا متبادل لکھ سکتے ہیں۔

<a id="day-21-section-10"></a>

### والدین کلاس کے میتھڈ کا متبادل

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

</div>

`super()` یا parent کلاس کے نام سے متعلقہ parent میتھڈ بلا سکتے ہیں۔ مثال میں child میتھڈ جنس کے مطابق `He` یا `She` منتخب کرتا ہے۔

🌕 آپ نے کلاسز اور آبجیکٹس کا سبق مکمل کر لیا! اب مشق کریں۔

<a id="day-21-section-11"></a>

## 💻 مشقیں — دن 21

<a id="day-21-section-12"></a>

### مشقیں: درجہ 1

1. شماریاتی حساب کے لیے پائتھن میں `statistics` ماڈیول موجود ہے، مگر فنکشنز بنانے اور دوبارہ استعمال کرنے کی مشق کے لیے اپنی `Statistics` کلاس بنائیں۔ نمونے کے مرکزی رجحان کے پیمانے، یعنی اوسط (*mean*)، میڈین اور موڈ، اور پھیلاؤ کے پیمانے، یعنی حد (*range*)، ویرینس اور معیاری انحراف نکالنے والے میتھڈز لکھیں۔ کم سے کم، زیادہ سے زیادہ، تعداد، percentile اور تعدادی تقسیم بھی معلوم کریں۔ متوقع نتائج دیکھیں۔

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
# you output should look like this
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

</div>

<a id="day-21-section-13"></a>

### مشقیں: درجہ 2

1. `PersonAccount` بنائیں۔ اس کے اوصاف `firstname`، `lastname`، `incomes` اور `expenses` ہوں۔ میتھڈز `total_income`، `total_expense`، `account_info`، `add_income`، `add_expense` اور `account_balance` ہوں۔ آمدنی اور اخراجات میں رقم کے ساتھ تفصیل بھی رکھیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 20](./20_python_package_manager.md) | [فہرست](./readme.md) | [اگلا دن: 22](./22_web_scraping.md)

</div>

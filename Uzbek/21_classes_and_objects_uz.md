<div align="center">
  <h1> 30 kunlik Python: 21-kun — Klass va Obyektlar</h1>
</div>

[<< 20-kun](./20_python_package_manager_uz.md) | [22-kun >>](./22_web_scraping_uz.md)

- [📘 21-kun](#-21-kun)
  - [Klass va obyekt nima](#klass-va-obyekt-nima)
  - [Klass yaratish](#klass-yaratish)
  - [Konstruktor](#konstruktor)
  - [Obyekt metodlari](#obyekt-metodlari)
  - [Standart (default) qiymatlar](#standart-default-qiymatlar)
  - [Meros olish (Inheritance)](#meros-olish-inheritance)
  - [💻 Mashqlar — 21-kun](#-mashqlar--21-kun)

# 📘 21-kun

## Klass va obyekt nima

Python — obyektga yo'naltirilgan til. Aslida siz boshidan beri **bilmasdan** klass va obyektlar bilan ishlagansiz — har bir son, satr, ro'yxat — bularning barchasi tegishli ichki klassning obyekti:

```python
>>> type(10)        # <class 'int'>
>>> type('matn')    # <class 'str'>
>>> type([])         # <class 'list'>
```

> 🟢 Agar siz JavaScriptda **`class`** kalit so'zini ko'rgan bo'lsangiz (ES6'dan beri mavjud), bu mavzu sizga tanish bo'ladi — Python'dagi klasslar **xuddi shu g'oyaga** asoslangan: klass — obyekt yaratish uchun "andoza (blueprint)".

> 🟡 **Analogiya:** Klass — **uy qurish chizmasi (loyihasi)**. Chizmaning o'zi uy emas, lekin shu chizma asosida ko'plab haqiqiy uylar (obyektlar) qurish mumkin. Har bir uy o'z rangi, o'z xonalar soniga ega bo'lishi mumkin — xuddi klassdan yaratilgan har bir obyekt o'z qiymatlariga ega bo'lgani kabi.

## Klass yaratish

```javascript
// JavaScript
class Person {}
const p = new Person();
```

```python
# Python — klass nomi CamelCase bilan yoziladi
class Person:
    pass

p = Person()    # JS'dagi 'new' kalit so'zi shart emas!
```

> 🟡 Farqi: JS'da obyekt yaratish uchun **`new`** kalit so'zi kerak (`new Person()`). Python'da esa **`new` yo'q** — klass nomini shunchaki funksiya kabi chaqirasiz: `Person()`.

## Konstruktor

JS'dagi `constructor()` metodi — Python'da **`__init__()`** deyiladi:

```javascript
// JavaScript
class Person {
  constructor(name) {
    this.name = name;     // 'this' — joriy obyektga ishora
  }
}
const p = new Person('Asabeneh');
console.log(p.name);
```

```python
# Python
class Person:
    def __init__(self, name):    # self — joriy obyektga ishora (JS'dagi 'this')
        self.name = name

p = Person('Asabeneh')
print(p.name)   # Asabeneh
```

> 🟡 **Eng katta farq:** JS'da `this` so'zi **avtomatik** mavjud. Python'da esa **`self`**ni har bir metodning **birinchi parametri** sifatida **qo'lda yozishingiz** kerak. `self` — JS'dagi `this` bilan bir xil vazifani bajaradi, faqat yashirin emas, oshkora yoziladi.

To'liq misol:

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)   # Asabeneh
print(p.age)         # 250
```

## Obyekt metodlari

Klass ichida oddiy funksiyalar — **metod** deyiladi, ular ham `self` parametrini oladi:

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):    # metod — birinchi parametr har doim self
        return f'{self.firstname} {self.lastname} {self.age} yoshda. U {self.city}, {self.country}da yashaydi.'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

## Standart (default) qiymatlar

11-kunda ko'rgan default parametrlar klass konstruktorida ham ishlaydi:

```python
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []                  # bo'sh ro'yxat — keyinroq to'ldiriladi

    def person_info(self):
        return f'{self.firstname} {self.lastname} {self.age} yoshda.'

    def add_skill(self, skill):           # ro'yxatga element qo'shuvchi metod
        self.skills.append(skill)

p1 = Person()                              # standart qiymatlar bilan
p1.add_skill('HTML')
p1.add_skill('Python')
print(p1.skills)    # ['HTML', 'Python']

p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.skills)    # [] — har bir obyekt o'zining mustaqil ro'yxatiga ega!
```

## Meros olish (Inheritance)

JS'dagi **`extends`** kalit so'zi bilan bir xil mantiq — Python'da klass nomi qavs ichida yoziladi:

```javascript
// JavaScript
class Student extends Person {}
```

```python
# Python
class Student(Person):    # Person — ota-klass (parent), Student — bola-klass (child)
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
print(s1.person_info())   # ota-klassning metodidan to'g'ridan-to'g'ri foydalanadi
s1.add_skill('Python')
print(s1.skills)            # ['Python']
```

> 🟡 **Analogiya:** Ota-klass — ota-ona, bola-klass — farzand. Farzand ota-onasining xususiyatlarini (metod va atributlarini) **avtomatik meros oladi**, hech narsa qayta yozmasdan.

**Ota-klass metodini "qayta yozish" (override) va `super()`:**

JS'dagi `super()` chaqiruvi bilan bir xil — bola-klass o'z konstruktoriga ega bo'lsa, ota-klass konstruktorini ishga tushirish uchun `super()` kerak:

```javascript
// JavaScript
class Student extends Person {
  constructor(firstname, lastname, age, country, city, gender) {
    super(firstname, lastname, age, country, city);  // ota-klass konstruktorini chaqirish
    this.gender = gender;
  }
}
```

```python
# Python
class Student(Person):
    def __init__(self, firstname, lastname, age, country, city, gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)   # ota-klass konstruktori

    def person_info(self):    # ota-klassning metodini "qayta yozish" (override)
        olmoshi = 'U (erkak)' if self.gender == 'male' else 'U (ayol)'
        return f'{self.firstname} {self.lastname} {self.age} yoshda. {olmoshi} {self.city}, {self.country}da yashaydi.'

s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s2.person_info())
```

> 🟡 Diqqat: agar bola-klassda o'zining `__init__()` bo'lsa, u ota-klassning `__init__()`ini **avtomatik chaqirmaydi** — buni `super().__init__(...)` orqali o'zingiz qo'lda chaqirishingiz kerak. Bu JS'dagi `super(...)` chaqiruvi bilan bir xil qoida.

🌕 Endi siz dasturlashning super kuchiga ega bo'ldingiz! 21-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 21-kun

### 1-daraja

1. `Statistics` nomli klass yarating — ichida statistik hisob-kitoblarni bajaruvchi metodlar bo'lsin: `count()`, `sum()`, `min()`, `max()`, `range()`, `mean()`, `median()`, `mode()`, `std()` (standart og'ish), `var()` (dispersiya), `freq_dist()` (chastota taqsimoti):

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Soni:', data.count())        # 25
print('Yig\'indi: ', data.sum())     # 744
print('Min: ', data.min())            # 24
print('Max: ', data.max())            # 38
print('O\'rtacha: ', data.mean())     # 30
print('Mediana: ', data.median())     # 29
print('Moda: ', data.mode())          # {'mode': 26, 'count': 5}
print('Standart og\'ish: ', data.std())  # 4.2
```

### 2-daraja

1. `PersonAccount` nomli klass yarating — `firstname`, `lastname`, `incomes`, `expenses` xususiyatlariga va `total_income`, `total_expense`, `account_info`, `add_income`, `add_expense`, `account_balance` metodlariga ega bo'lsin. `incomes` va `expenses` — tavsif bilan birga keladigan kirim/chiqim to'plamlari.

🎉 TABRIKLAYMIZ! 🎉

[<< 20-kun](./20_python_package_manager_uz.md) | [22-kun >>](./22_web_scraping_uz.md)

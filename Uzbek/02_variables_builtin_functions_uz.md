<div align="center">
  <h1> 30 kunlik Python: 2-kun — O'zgaruvchilar, ichki (built-in) funksiyalar</h1>
</div>

[<< 1-kun](./01_introduction_uz.md) | [3-kun >>](./03_operators_uz.md)

- [📘 2-kun](#-2-kun)
  - [Ichki funksiyalar](#ichki-funksiyalar)
  - [O'zgaruvchilar](#ozgaruvchilar)
  - [Ma'lumot turlari](#malumot-turlari)
  - [Ma'lumot turini tekshirish va o'zgartirish (casting)](#malumot-turini-tekshirish-va-ozgartirish-casting)
  - [Sonlar](#sonlar)
  - [💻 Mashqlar — 2-kun](#-mashqlar--2-kun)

# 📘 2-kun

## Ichki funksiyalar

JavaScriptda `console.log()`, `parseInt()`, `Array.isArray()` kabi tayyor (built-in) funksiyalardan foydalangansiz — ularni import qilmasdan, hech narsa sozlamasdan to'g'ridan-to'g'ri chaqirgan bo'lardingiz. Pythonda ham xuddi shunday — bular **ichki funksiyalar (built-in functions)** deyiladi va doim "qo'l ostida" turadi.

Eng ko'p ishlatiladigan ichki funksiyalar: `print()`, `len()`, `type()`, `int()`, `float()`, `str()`, `input()`, `list()`, `dict()`, `min()`, `max()`, `sum()`, `sorted()`, `open()`, `help()`, `dir()`. To'liq ro'yxatni [Python hujjatlarida](https://docs.python.org/3/library/functions.html) ko'rishingiz mumkin.

> 🟡 Eslatma: Python'da `len('Hello')` deb yozamiz — JavaScriptdagi `'Hello'.length` (xususiyat) o'rniga, Pythonda uzunlikni **funksiya** orqali olamiz: `len()`.

## O'zgaruvchilar

O'zgaruvchilar — ma'lumotni kompyuter xotirasida saqlaydigan nom. Bu tushuncha JavaScriptdagi bilan bir xil, faqat e'lon qilish usuli farq qiladi:

```javascript
// JavaScript
let firstName = 'Asabeneh';
const age = 250;
```

```python
# Python
first_name = 'Asabeneh'
age = 250
```

**Asosiy farqlar:**

- Pythonda `let`, `const`, `var` kabi kalit so'zlar **yo'q**. Shunchaki nomini yozib, `=` qo'yib, qiymatini berasiz.
- JavaScriptda o'zgaruvchi nomlari **camelCase** (`firstName`, `lastName`) tarzida yoziladi. Pythonda esa **snake_case** qabul qilingan — so'zlar orasiga pastki chiziqcha (`_`) qo'yiladi: `first_name`, `last_name`.
- `=` belgisi matematikadagi "tenglik" emas, balki **"qiymat berish (assignment)"** degani — bu JavaScriptdagi `=` bilan bir xil mantiq.

### O'zgaruvchi nomlash qoidalari

- Nom harf yoki pastki chiziqcha (`_`) bilan boshlanishi kerak
- Raqam bilan boshlanishi mumkin emas
- Faqat harf, raqam va pastki chiziqcha bo'lishi mumkin (chiziqcha `-` yoki maxsus belgilar bo'lmaydi)
- Katta-kichik harfga sezgir: `firstname`, `Firstname`, `FirstName` — bularning barchasi **boshqa-boshqa** o'zgaruvchi hisoblanadi (xuddi JavaScriptdagidek)

**To'g'ri nomlar:**

```shell
first_name
last_name
age
country
city
_if            # agar zaxiralangan so'zni o'zgaruvchi sifatida ishlatish kerak bo'lsa
year_2021
num1
```

**Noto'g'ri nomlar:**

```shell
first-name     # chiziqcha bo'lmaydi
first@name     # maxsus belgi bo'lmaydi
1num           # raqamdan boshlanmaydi
```

**Misol:**

```python
# Python'da o'zgaruvchilar
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']     # JS'dagi array kabi
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}    # JS'dagi object kabi
```

`print()` cheksiz miqdordagi argument qabul qiladi — JavaScriptdagi `console.log()` ham xuddi shunday ishlaydi:

```python
print('Hello, World!')                 # bitta argument
print('Hello', ',', 'World', '!')      # to'rt argument — vergul bilan ajratiladi
print(len('Hello, World!'))            # len() — satr uzunligini qaytaradi
```

### Bir qatorda bir nechta o'zgaruvchi e'lon qilish

JavaScriptda buni destructuring deb atashgan bo'lardingiz (`let [a, b] = [1, 2]`). Pythonda bu yanada sodda:

```python
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsinki', 250, True

print(first_name, last_name, country, age, is_married)
```

### Foydalanuvchidan ma'lumot olish — `input()`

Brauzerda `prompt()` funksiyasini ishlatgansiz — foydalanuvchidan matn so'rab, javobini qaytarib beradi. Python'da bunga **`input()`** mos keladi (lekin terminalda ishlaydi, brauzerda emas):

```python
first_name = input('Ismingiz nima: ')
age = input('Yoshingiz nechida? ')

print(first_name)
print(age)
```

> 🟡 Diqqat: `input()` doim **satr (string)** qaytaradi — agar son kerak bo'lsa, uni `int()` yoki `float()` orqali o'zgartirish kerak. Bu JavaScriptdagi `prompt()` bilan bir xil xatti-harakat.

## Ma'lumot turlari

Pythonda bir necha ma'lumot turi mavjud (1-kunda ko'rgan edik). Ma'lumot turini bilish — dasturlashning markazida turadi, shuning uchun bu mavzu keyingi kunlarda yana-yana qaytadi.

## Ma'lumot turini tekshirish va o'zgartirish (casting)

**Turini tekshirish** — `type()` funksiyasi orqali:

```python
first_name = 'Asabeneh'    # str
age = 250                  # int

print(type(first_name))           # <class 'str'>
print(type(age))                  # <class 'int'>
print(type(3.14))                 # <class 'float'>
print(type(1 + 1j))               # <class 'complex'>
print(type(True))                 # <class 'bool'>
print(type([1, 2, 3, 4]))         # <class 'list'>
print(type({'name': 'Asabeneh'})) # <class 'dict'>
print(type((1, 2)))               # <class 'tuple'>
print(type(zip([1, 2], [3, 4]))) # <class 'zip'> — ikki ro'yxatni juftlab birlashtiradi
```

**Turini o'zgartirish (casting)** — JavaScriptda `Number('10')`, `String(10)`, `parseInt('10')` kabi funksiyalardan foydalangansiz. Pythonda bu vazifani `int()`, `float()`, `str()`, `list()` bajaradi:

```python
# int dan float ga
num_int = 10
num_float = float(num_int)
print(num_float)            # 10.0

# float dan int ga
gravity = 9.81
print(int(gravity))         # 9  — kasr qismi shunchaki tashlab yuboriladi (yaxlitlanmaydi!)

# int dan str ga
num_int = 10
num_str = str(num_int)
print(num_str)               # '10'

# str dan int yoki float ga
num_str = '10.6'
print(float(num_str))        # 10.6
print(int(float(num_str)))   # 10  — avval float, keyin int qilinadi

# str dan list ga
first_name = 'Asabeneh'
print(list(first_name))      # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

> ⚠️ **Muhim eslatma:** Agar son va matnni JavaScriptda `+` bilan qo'shsangiz, JS avtomatik ravishda ularni birlashtirib (concatenation) matnga aylantiradi (`5 + '5'` → `'55'`). **Python bunday avtomatik o'zgartirishni qilmaydi!** `5 + '5'` Python'da xatolik (`TypeError`) beradi. Avval `str()` yoki `int()` bilan turlarni mos qilib olishingiz kerak.

## Sonlar

Pythonda son turlari (1-kunda ko'rgan edik, eslatib o'tamiz):

1. **Integer** — butun sonlar: `... -3, -2, -1, 0, 1, 2, 3 ...`
2. **Float** — kasr sonlar: `... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...`
3. **Complex** — kompleks sonlar: `1 + j, 2 + 4j, 1 - 1j`

🌕 Zo'r ishladingiz! 2-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 2-kun

### 1-daraja

1. `30DaysOfPython` papkasi ichida `day_2` papkasini yarating. Uning ichida `variables.py` faylini yarating.
2. Izoh yozing: `'2-kun: 30 kunlik Python dasturlash'`
3. Ism o'zgaruvchisini e'lon qilib, qiymat bering
4. Familiya o'zgaruvchisini e'lon qilib, qiymat bering
5. To'liq ism o'zgaruvchisini e'lon qilib, qiymat bering
6. Davlat o'zgaruvchisini e'lon qilib, qiymat bering
7. Shahar o'zgaruvchisini e'lon qilib, qiymat bering
8. Yosh o'zgaruvchisini e'lon qilib, qiymat bering
9. Yil o'zgaruvchisini e'lon qilib, qiymat bering
10. `is_married` o'zgaruvchisini e'lon qilib, qiymat bering
11. `is_true` o'zgaruvchisini e'lon qilib, qiymat bering
12. `is_light_on` o'zgaruvchisini e'lon qilib, qiymat bering
13. Bir qatorda bir nechta o'zgaruvchini e'lon qiling

### 2-daraja

1. Barcha o'zgaruvchilaringizning turini `type()` orqali tekshiring
2. `len()` funksiyasi orqali ismingiz uzunligini toping
3. Ismingiz va familiyangiz uzunligini taqqoslang
4. `num_one = 5` va `num_two = 4` deb e'lon qiling
5. `num_one` va `num_two`ni qo'shib, natijani `total` ga yozing
6. `num_one`dan `num_two`ni ayirib, natijani `diff` ga yozing
7. `num_one` va `num_two`ni ko'paytirib, natijani `product` ga yozing
8. `num_one`ni `num_two`ga bo'lib, natijani `division` ga yozing
9. `num_two`ni `num_one`ga modul bo'lib, natijani `remainder` ga yozing
10. `num_one`ning `num_two`-darajasini hisoblab, natijani `exp` ga yozing
11. `num_one`ni `num_two`ga butun qismli bo'lib, natijani `floor_division` ga yozing
12. Doiraning radiusi 30 metr:
    1. Doira yuzini hisoblab, `area_of_circle` ga yozing
    2. Doira aylanasini hisoblab, `circum_of_circle` ga yozing
    3. Radiusni foydalanuvchidan `input()` orqali olib, yuzini hisoblang
13. `input()` orqali foydalanuvchidan ism, familiya, davlat va yoshini so'rab, mos o'zgaruvchilarga yozing
14. Python shell'da yoki faylingizda `help('keywords')` ni ishga tushirib, zaxiralangan so'zlarni ko'ring

🎉 TABRIKLAYMIZ! 🎉

[<< 1-kun](./01_introduction_uz.md) | [3-kun >>](./03_operators_uz.md)

<div align="center">
  <h1> 30 kunlik Python: 3-kun — Operatorlar</h1>
</div>

[<< 2-kun](./02_variables_builtin_functions_uz.md) | [4-kun >>](./04_strings_uz.md)

- [📘 3-kun](#-3-kun)
  - [Boolean](#boolean)
  - [Operatorlar](#operatorlar)
    - [Qiymat berish operatorlari](#qiymat-berish-operatorlari)
    - [Arifmetik operatorlar](#arifmetik-operatorlar)
    - [Taqqoslash operatorlari](#taqqoslash-operatorlari)
    - [Mantiqiy operatorlar](#mantiqiy-operatorlar)
  - [💻 Mashqlar — 3-kun](#-mashqlar--3-kun)

# 📘 3-kun

## Boolean

Boolean — `True` yoki `False` qiymatlardan birini ifodalaydi. JavaScriptdan farqli o'laroq, Python'da bu so'zlarning **birinchi harfi katta** yoziladi: `True`, `False` (JS'da `true`, `false` — kichik harf).

```python
print(True)
print(False)
```

## Operatorlar

### Qiymat berish operatorlari

`=` belgisi — matematikadagi "tenglik" emas, balki **qiymat berish (assignment)**. Bu JavaScriptdagi `=` bilan bir xil mantiqda ishlaydi. Python'da ham `+=`, `-=`, `*=`, `/=` kabi qisqartirilgan operatorlar mavjud — JS'dagilar bilan bir xil:

```python
x = 5
x += 3   # x = x + 3 bilan bir xil -> 8
x -= 2   # -> 6
```

### Arifmetik operatorlar

- Qo'shish (+): `a + b`
- Ayirish (-): `a - b`
- Ko'paytirish (*): `a * b`
- Bo'lish (/): `a / b`
- Modul / qoldiq (%): `a % b`
- Butun qismli bo'lish (//): `a // b`
- Daraja (**): `a ** b`

Bularning aksariyati JavaScript bilan bir xil. Faqat oxirgi ikkisi (`//` va `**`) JS'da boshqacha yoziladi (`Math.floor(a/b)` va `a ** b` — aslida `**` JS'da ham mavjud ES2016'dan beri!).

**Misol: Butun sonlar**

```python
# Python'da arifmetik amallar — butun sonlar

print('Qo\'shish: ', 1 + 2)        # 3
print('Ayirish: ', 2 - 1)          # 1
print('Ko\'paytirish: ', 2 * 3)    # 6
print('Bo\'lish: ', 4 / 2)         # 2.0  — Python'da bo'lish doim float qaytaradi!
print('Bo\'lish: ', 7 / 2)         # 3.5
print('Qoldiqsiz bo\'lish: ', 7 // 2)   # 3  — kasr/qoldiq qismi tashlanadi
print('Modul: ', 3 % 2)            # 1  — qoldiqni qaytaradi
print('Daraja: ', 2 ** 3)          # 8  — bu 2 * 2 * 2 degani
```

> 🟡 **Diqqat:** JavaScriptda `4 / 2` natijasi `2` (butun) bo'lib chiqadi, chunki JS sonlarni ajratmaydi. **Python'da esa `/` doim float qaytaradi** — `4 / 2` natijasi `2.0` bo'ladi, `2` emas! Agar butun natija kerak bo'lsa, `//` dan foydalaning.

**Misol: Kasr va kompleks sonlar**

```python
print('Pi soni:', 3.14)
print('Tortilish kuchi:', 9.81)

print('Kompleks son: ', 1 + 1j)
print('Kompleks sonlarni ko\'paytirish: ', (1 + 1j) * (1 - 1j))
```

**Misol: O'zgaruvchilar bilan amallar**

```python
a = 3   # a — o'zgaruvchi nomi, 3 — integer qiymat
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)
```

Endi bilganlarimizni real hayotdagi hisob-kitoblarga (yuza, hajm, og'irlik, masofa) qo'llab ko'ramiz:

```python
# Doira yuzini hisoblash
radius = 10
area_of_circle = 3.14 * radius ** 2     # ** belgisi daraja (kvadratga oshirish)
print('Doira yuzi:', area_of_circle)

# To'rtburchak yuzini hisoblash
length = 10
width = 20
area_of_rectangle = length * width
print('To\'rtburchak yuzi:', area_of_rectangle)

# Jismning og'irligini hisoblash
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')   # natijaga o'lchov birligini qo'shamiz
```

### Taqqoslash operatorlari

Ikki qiymatni solishtirish uchun ishlatiladi — natija doim `True` yoki `False`. Bu JavaScriptdagi bilan deyarli bir xil:

```python
print(3 > 2)     # True
print(3 >= 2)    # True
print(3 < 2)     # False
print(3 == 2)    # False — teng emas
print(3 != 2)    # True — teng emas
print(len('mango') == len('avocado'))  # False
print(len('python') > len('dragon'))   # False
```

> ⚠️ **Muhim farq:** JavaScriptda ikki xil tenglik bor edi — `==` (turini hisobga olmaydi, masalan `'5' == 5` → `true`) va `===` (qattiq tenglik, turini ham tekshiradi). **Python'da faqat bitta tenglik operatori bor — `==`, va u har doim qattiq taqqoslaydi** (turi boshqa bo'lsa, `False` qaytaradi: `'5' == 5` → `False`). Python'da `===` umuman mavjud emas — chunki unga ehtiyoj yo'q.

Python'da yana qo'shimcha to'rt operator bor, JavaScriptda to'g'ridan-to'g'ri o'xshashi yo'q:

- **`is`** — ikki o'zgaruvchi xotirada **xuddi bir xil obyekt**ligini tekshiradi (`x is y`)
- **`is not`** — ikkisi bir xil obyekt emasligini tekshiradi
- **`in`** — qiymat ro'yxat/satr ichida bor-yo'qligini tekshiradi (`x in y`)
- **`not in`** — qiymat ro'yxat/satr ichida yo'qligini tekshiradi

> 🟡 **Analogiya:** `==` — ikki odamning **yuzi bir xil ko'rinishini** tekshiradi (qiymat bir xil). `is` esa ikkisi **bir xil shaxsligini** tekshiradi (xotiradagi bir xil "joy"). JavaScriptda `in` operatori ham bor, lekin u obyektning **kalitlarini** tekshiradi (`'a' in {a: 1}`), ro'yxat elementini emas — Python'dagi `in` esa list, string, dict — barchasida elementni qidiradi.

```python
print('1 is 1', 1 is 1)                       # True
print('A in Asabeneh', 'A' in 'Asabeneh')     # True — 'A' satr ichida bor
print('coding' in 'coding for all')           # True
```

### Mantiqiy operatorlar

JavaScriptda `&&`, `||`, `!` belgilaridan foydalangansiz. **Python'da esa bu belgilar o'rniga so'zlar ishlatiladi: `and`, `or`, `not`.**

| JavaScript | Python | Ma'no |
|---|---|---|
| `&&` | `and` | ikkisi ham rost bo'lsa True |
| `\|\|` | `or` | kamida bittasi rost bo'lsa True |
| `!` | `not` | qiymatni teskarisiga aylantiradi |

```python
print(3 > 2 and 4 > 3)   # True — ikkisi ham rost
print(3 > 2 and 4 < 3)   # False — ikkinchisi yolg'on
print(3 > 2 or 4 < 3)    # True — kamida bittasi rost
print(not 3 > 2)         # False — 3 > 2 rost, not uni False ga aylantiradi
print(not not True)      # True
```

🌕 Zo'r ishladingiz! 3-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 3-kun

1. Yoshingizni integer o'zgaruvchi sifatida e'lon qiling
2. Bo'yingizni float o'zgaruvchi sifatida e'lon qiling
3. Kompleks sonni saqlaydigan o'zgaruvchi e'lon qiling
4. Foydalanuvchidan uchburchakning asosi va balandligini so'rab oluvchi va yuzini hisoblaydigan (`yuza = 0.5 x b x h`) skript yozing.

```py
    Asosni kiriting: 20
    Balandlikni kiriting: 10
    Uchburchak yuzi: 100
```

5. Foydalanuvchidan uchburchakning a, b, c tomonlarini so'rab oluvchi va perimetrini hisoblaydigan (`perimetr = a + b + c`) skript yozing.
6. To'rtburchakning uzunligi va kengligini foydalanuvchidan so'rab, yuzini (`yuza = uzunlik x kenglik`) va perimetrini (`perimetr = 2 x (uzunlik + kenglik)`) hisoblang.
7. Doiraning radiusini foydalanuvchidan so'rab, yuzini (`yuza = pi x r x r`) va aylanasini (`c = 2 x pi x r`, `pi = 3.14`) hisoblang.
8. `y = 2x - 2` tenglamasining burchak koeffitsienti (slope), x- va y-kesishuvchi nuqtalarini hisoblang.
9. Burchak koeffitsienti `m = (y2-y1)/(x2-x1)` formulasi orqali (2, 2) va (6, 10) nuqtalar orasidagi burchak koeffitsienti va [Yevklid masofasini](https://en.wikipedia.org/wiki/Euclidean_distance) toping.
10. 8- va 9-topshiriqdagi burchak koeffitsientlarini taqqoslang.
11. `y = x^2 + 6x + 9` ning qiymatini turli `x` lar uchun hisoblang va `y` qachon 0 bo'lishini toping.
12. `'python'` va `'dragon'` so'zlarining uzunligini solishtiring (False natija beradigan taqqoslash yozing).
13. `and` operatori orqali `'on'` so'zi ham `'python'`, ham `'dragon'` ichida bor-yo'qligini tekshiring.
14. `in` operatori orqali gapda `'jargon'` so'zi bor-yo'qligini tekshiring.
15. `'python'` so'zining uzunligini topib, uni float'ga, keyin string'ga aylantiring.
16. Juft sonlar 2 ga bo'linganda qoldiq nol bo'ladi. Pythonda bir sonning juft ekanligini qanday tekshirasiz?
17. `7 // 3` ning natijasi `int(2.7)` ga teng ekanligini tekshiring.
18. `type('10')` ning `type(10)` ga teng ekanligini tekshiring.
19. `int('9.8')` ning `10` ga teng ekanligini tekshiring.
20. Foydalanuvchidan ish soati va soatlik to'lovni so'rab, oylik maoshni hisoblaydigan skript yozing.
21. Foydalanuvchidan necha yil yashaganini so'rab, shuncha yil necha soniyaga teng ekanligini hisoblang (1 yil = 100 ga yaxlitlangan deb hisoblang).
22. Quyidagi jadvalni chiqaradigan skript yozing:

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

🎉 TABRIKLAYMIZ! 🎉

[<< 2-kun](./02_variables_builtin_functions_uz.md) | [4-kun >>](./04_strings_uz.md)

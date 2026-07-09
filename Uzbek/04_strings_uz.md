<div align="center">
  <h1> 30 kunlik Python: 4-kun — Satrlar (Strings)</h1>
</div>

[<< 3-kun](./03_operators_uz.md) | [5-kun >>](./05_lists_uz.md)

- [📘 4-kun](#-4-kun)
  - [Satr yaratish](#satr-yaratish)
  - [Satrlarni birlashtirish (Concatenation)](#satrlarni-birlashtirish-concatenation)
  - [Maxsus belgilar (Escape Sequences)](#maxsus-belgilar-escape-sequences)
  - [Satrlarni formatlash](#satrlarni-formatlash)
  - [Satr — belgilar ketma-ketligi sifatida](#satr--belgilar-ketma-ketligi-sifatida)
  - [Satr metodlari](#satr-metodlari)
  - [💻 Mashqlar — 4-kun](#-mashqlar--4-kun)

# 📘 4-kun

## Satrlar

Matn — bu **string (satr)** ma'lumot turi. Bir, ikki yoki uchlik tirnoq ichidagi har qanday narsa satr hisoblanadi. Bu tushuncha JavaScriptdagi `string` bilan to'liq bir xil.

### Satr yaratish

```python
letter = 'P'                # satr bir belgidan ham, ko'p so'zdan ham iborat bo'lishi mumkin
print(letter)                # P
print(len(letter))           # 1
greeting = 'Hello, World!'   # bir yoki qo'sh tirnoq bilan yozish mumkin
print(greeting)
sentence = "Men 30 kunlik Python challenge'idan zavqlanyapman"
print(sentence)
```

Ko'p qatorli satr uchlik tirnoq (`'''` yoki `"""`) bilan yaratiladi:

```python
multiline_string = '''Men o'qituvchiman va o'qitishni yaxshi ko'raman.
Odamlarga kuch berishdan ko'ra qoniqarli narsa topmadim.
Shu sababli 30 kunlik Python'ni yaratdim.'''
print(multiline_string)
```

> 🟡 JavaScriptda ko'p qatorli matn uchun **template literal** (`` ` `` — orqaga qaytish belgisi) ishlatilardi. Pythonda buning o'rnini uchlik tirnoq bosadi.

### Satrlarni birlashtirish (Concatenation)

Ikki satrni birlashtirish — `+` operatori bilan, xuddi JavaScriptdagidek:

```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name + space + last_name
print(full_name)             # Asabeneh Yetayeh
print(len(first_name) > len(last_name))  # True
```

### Maxsus belgilar (Escape Sequences)

Teskari chiziq (`\`) dan keyin keladigan belgi — **maxsus belgi (escape sequence)** deyiladi. Bu JavaScriptdagi bilan bir xil:

- `\n` — yangi qator
- `\t` — tab (8 bo'sh joy)
- `\\` — orqaga chiziq belgisining o'zi
- `\'` — bir tirnoq
- `\"` — qo'sh tirnoq

```python
print('Hammaga Python challenge yoqayotganiga ishonaman.\nSizga ham yoqdimi?')
print('Kunlar\tMavzular\tMashqlar')
print('1-kun\t5\t5')
print('Bu orqaga chiziq belgisi (\\)')
print('Har bir dasturlash tili \"Hello, World!\" bilan boshlanadi')
```

### Satrlarni formatlash

Pythonda satr ichiga o'zgaruvchi qiymatini "joylashtirish" uchun bir necha usul bor. Eng muhimi — **f-string** usuli, chunki u JavaScriptdagi **template literal**ga juda o'xshaydi.

**Eski usul (% operatori)** — buni kamdan-kam ko'rasiz, lekin eski kodlarda uchraydi:

```python
first_name = 'Asabeneh'
language = 'Python'
formated_string = 'Mening ismim %s. Men %s o\'qitaman' % (first_name, language)
print(formated_string)
```

**Yangi usul (`.format()`):**

```python
a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} / {} = {:.2f}'.format(a, b, a / b))   # nuqtadan keyin 2 xona
```

**f-string usuli (Python 3.6+) — eng qulayi, JS'dagi template literalga to'g'ridan-to'g'ri mos keladi:**

```javascript
// JavaScript
const a = 4, b = 3;
console.log(`${a} + ${b} = ${a + b}`);
```

```python
# Python — f harfi va jingalak qavs ichida o'zgaruvchi
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} / {b} = {a / b:.2f}')   # :.2f -> 2 xonali kasr qilib ko'rsatadi
```

> 🟡 Farq: JS'da `${ }` ichiga o'zgaruvchi yoziladi va satr `` ` `` belgisi bilan boshlanadi. Python'da `{ }` ichiga yoziladi va satr oldida `f` harfi turadi: `f'...'`.

### Satr — belgilar ketma-ketligi sifatida

Python'da satr — bu belgilar ketma-ketligi (sequence), xuddi massiv kabi indekslash mumkin. Bu JavaScriptdagi `'Python'[0]` bilan bir xil ishlaydi!

#### Belgilarni o'zgaruvchilarga "yoyish" (Unpacking)

```python
language = 'Python'
a, b, c, d, e, f = language    # har bir belgi alohida o'zgaruvchiga yoyiladi
print(a)  # P
print(f)  # n
```

> 🟡 Bu JavaScriptdagi destructuring'ga o'xshaydi: `const [a, b, c] = 'Python'`.

#### Indeks orqali belgiga murojaat

Dasturlashda sanash **noldan** boshlanadi — JS'dagi kabi.

```python
language = 'Python'
print(language[0])   # P — birinchi belgi
print(language[1])   # y
print(language[-1])  # n — manfiy indeks oxiridan sanaydi
print(language[-2])  # o
```

> 🟡 JavaScriptda satrning oxirgi belgisini olish uchun `'Python'[str.length - 1]` deb yozardingiz. Python'da esa shunchaki `language[-1]` — manfiy indekslash to'g'ridan-to'g'ri "oxiridan sanash" degani, bu juda qulay.

#### Slicing (Bo'lakka kesish)

```python
language = 'Python'
print(language[0:3])   # Pyt — 0-indeksdan 3-gacha (3 kirmaydi)
print(language[3:])    # hon — 3-indeksdan oxirigacha
print(language[-3:])   # hon — oxirgi 3 belgi
```

> 🟡 Bu JavaScriptdagi `'Python'.slice(0, 3)` bilan bir xil mantiqda ishlaydi, faqat Python'da kvadrat qavs ichida `:` belgisi orqali yoziladi: `[boshlanish:tugash]`.

#### Satrni teskari aylantirish

```python
greeting = 'Hello, World!'
print(greeting[::-1])   # !dlroW ,olleH
```

> 🟡 JavaScriptda bunday qisqa yo'l yo'q — odatda `greeting.split('').reverse().join('')` deb uzun yozardingiz. Python'da `[::-1]` "oxiridan boshigacha, -1 qadam bilan" degani — bitta amalda teskari aylantiradi.

#### Slicing'da belgilarni o'tkazib yuborish

```python
language = 'Python'
print(language[0:6:2])   # Pto — har 2-belgini oladi
```

## Satr metodlari

Quyida eng ko'p ishlatiladigan satr metodlari, JavaScript bilan taqqoslagan holda:

| Python metodi | JavaScript'dagi o'xshashi | Vazifasi |
|---|---|---|
| `.upper()` | `.toUpperCase()` | katta harfga o'tkazadi |
| `.lower()` | `.toLowerCase()` | kichik harfga o'tkazadi |
| `.strip()` | `.trim()` | boshi-oxiridagi bo'sh joyni olib tashlaydi |
| `.split()` | `.split()` | satrni bo'lib, ro'yxat (list) qaytaradi — bir xil ishlaydi |
| `.replace()` | `.replace()` | ⚠️ **Farqi bor!** Python `.replace()` — **barcha** mosliklarni almashtiradi. JS `.replace()` — faqat **birinchisini** (hammasi uchun `replaceAll()` yoki `/g` flag kerak) |
| `.startswith()` | `.startsWith()` | satr shu bilan boshlanadimi |
| `.endswith()` | `.endsWith()` | satr shu bilan tugaydimi |
| `.find()` / `.index()` | `.indexOf()` | qism-satrning indeksini topadi (`.find()` topilmasa `-1`, `.index()` esa xatolik beradi) |
| `' '.join(list)` | `list.join(' ')` | ⚠️ **Teskari!** JS'da array o'zi `.join()` chaqiradi. Python'da **ajratuvchi satr** `.join()` ni chaqiradi: `'ajratuvchi'.join(ro'yxat)` |

```python
challenge = 'thirty days of python'

print(challenge.capitalize())    # 'Thirty days of python' — birinchi harfni katta qiladi
print(challenge.count('y'))      # 3 — 'y' necha marta uchraydi
print(challenge.endswith('on'))  # True
print(challenge.find('y'))       # 5 — 'y' birinchi qaysi indeksda
print(challenge.title())         # 'Thirty Days Of Python' — har bir so'zni katta harf qiladi
print(challenge.swapcase())      # katta-kichik harflarni almashtiradi
print(challenge.replace('python', 'coding'))   # 'thirty days of coding'
print(challenge.split())         # ['thirty', 'days', 'of', 'python']

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
print(' '.join(web_tech))        # 'HTML CSS JavaScript React'

print('30DaysOfPython'.isidentifier())       # False — raqamdan boshlanadi
print('thirty_days_of_python'.isidentifier()) # True — to'g'ri o'zgaruvchi nomi
print('123'.isdigit())           # True — barcha belgilar raqam
print('thirty'.isalpha())        # True — barcha belgilar harf
```

🌕 Siz ajoyibsiz! 4-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 4-kun

1. `'Thirty'`, `'Days'`, `'Of'`, `'Python'` satrlarini birlashtirib, `'Thirty Days Of Python'` hosil qiling.
2. `'Coding'`, `'For'`, `'All'` satrlarini birlashtirib, `'Coding For All'` hosil qiling.
3. `company` nomli o'zgaruvchi e'lon qilib, qiymatini `"Coding For All"` qiling.
4. `company` o'zgaruvchisini `print()` orqali chiqaring.
5. `len()` orqali `company` satrining uzunligini chiqaring.
6. `.upper()` orqali barcha harflarni katta qiling.
7. `.lower()` orqali barcha harflarni kichik qiling.
8. `.capitalize()`, `.title()`, `.swapcase()` metodlarini `'Coding For All'` ustida sinab ko'ring.
9. `'Coding For All'` dan birinchi so'zni kesib (slice) oling.
10. `.index()`, `.find()` yoki boshqa metod orqali `'Coding For All'` ichida `'Coding'` so'zi bor-yo'qligini tekshiring.
11. `'Coding For All'` ichidagi `'Coding'` so'zini `'Python'` ga almashtiring.
12. `.replace()` yoki boshqa metod orqali `"Python for Everyone"`ni `"Python for All"`ga aylantiring.
13. `'Coding For All'` ni bo'sh joy bo'yicha bo'lib (`.split()`), ro'yxatga aylantiring.
14. `"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"` ni vergul bo'yicha bo'ling.
15. `'Coding For All'` da 0-indeksdagi belgi qanday?
16. `'Coding For All'` ning oxirgi indeksi nechiga teng?
17. `'Coding For All'` da 10-indeksdagi belgi qanday?
18. `'Python For Everyone'` uchun qisqartma (abbreviatura) yarating.
19. `'Coding For All'` uchun qisqartma yarating.
20. `.index()` orqali `'Coding For All'` da birinchi `'C'` qaysi indeksda ekanini toping.
21. `.index()` orqali birinchi `'F'` qaysi indeksda ekanini toping.
22. `.rfind()` orqali `'Coding For All People'` da oxirgi `'l'` qaysi indeksda ekanini toping.
23. `'You cannot end a sentence with because because because is a conjunction'` jumlasida `'because'` so'zining birinchi o'rnini `.index()` yoki `.find()` orqali toping.
24. Xuddi shu jumlada `'because'`ning oxirgi o'rnini `.rindex()` orqali toping.
25. Shu jumladan `'because because because'` qismini kesib (slice) oling.
26. `'Coding For All'` `'Coding'` so'zi bilan boshlanadimi (`.startswith()`)?
27. `'Coding For All'` `'coding'` so'zi bilan tugaydimi (`.endswith()`)?
28. `'   Coding For All    '` satridagi chap va o'ng tomondagi bo'sh joylarni olib tashlang (`.strip()`).
29. Quyidagi o'zgaruvchilardan qaysi biri `.isidentifier()` da `True` qaytaradi: `30DaysOfPython` yoki `thirty_days_of_python`?
30. `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']` ro'yxatini `'# '` bilan birlashtiring (`.join()`).
31. `\n` maxsus belgisi orqali quyidagi gaplarni alohida qatorda chiqaring:
    ```py
    Men bu challenge'dan zavqlanyapman.
    Qiziq, keyin nima bo'lar ekan.
    ```
32. `\t` maxsus belgisi orqali quyidagi jadvalni chiqaring:
    ```py
    Ism       Yosh    Davlat     Shahar
    Asabeneh  250     Finland    Helsinki
    ```
33. f-string orqali quyidagini chiqaring: `"Radiusi 10 bo'lgan doiraning yuzi 314 kvadrat metr."`
34. f-string orqali quyidagi hisob-kitobni chiqaring:
    ```sh
    8 + 6 = 14
    8 - 6 = 2
    8 * 6 = 48
    8 / 6 = 1.33
    8 % 6 = 2
    8 // 6 = 1
    8 ** 6 = 262144
    ```

🎉 TABRIKLAYMIZ! 🎉

[<< 3-kun](./03_operators_uz.md) | [5-kun >>](./05_lists_uz.md)

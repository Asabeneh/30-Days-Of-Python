<div align="center">
  <h1> 30 kunlik Python: 10-kun — Sikllar (Loops)</h1>
</div>

[<< 9-kun](./09_conditionals_uz.md) | [11-kun >>](./11_functions_uz.md)

- [📘 10-kun](#-10-kun)
  - [While sikli](#while-sikli)
  - [Break va Continue](#break-va-continue)
  - [For sikli](#for-sikli)
  - [range() funksiyasi](#range-funksiyasi)
  - [Ichma-ich for sikli](#ichma-ich-for-sikli)
  - [For Else](#for-else)
  - [Pass](#pass)
  - [💻 Mashqlar — 10-kun](#-mashqlar--10-kun)

# 📘 10-kun

## Sikllar (Loops)

JavaScriptda `while` va `for` sikllarini ishlatgansiz. Pythonda ham xuddi shu ikki turi bor, lekin **`for` sikli butunlay boshqacha yoziladi** — bu eng katta farq bo'ladi.

## While sikli

Bu deyarli JavaScriptdagi bilan bir xil — faqat qavs va jingalak qavs yo'q:

```javascript
// JavaScript
let count = 0;
while (count < 5) {
  console.log(count);
  count = count + 1;
}
```

```python
# Python
count = 0
while count < 5:
    print(count)
    count = count + 1
# 0, 1, 2, 3, 4 ni chiqaradi
```

Python'da yana qiziq bir xususiyat bor — `while` bilan `else` ishlatish mumkin: sikl **shartsiz** tugaganda (break orqali emas) ishga tushadi:

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)   # sikl tabiiy tugaganda ishlaydi -> 5
```

## Break va Continue

Bu ikkisi **JavaScriptdagi bilan bir xil so'zlar va bir xil ma'noda** ishlaydi — bu yerda yangilik yo'q!

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break       # siklni butunlay to'xtatadi — JS'dagi break bilan bir xil
```

```python
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue    # shu qadamni o'tkazib, davom etadi — JS'dagi continue bilan bir xil
    print(count)
    count = count + 1
```

## For sikli

**Mana eng katta farq shu yerda.** JavaScriptda klassik `for (let i = 0; i < 5; i++)` yoki `for...of` ishlatgansiz:

```javascript
// JavaScript — array bo'yicha aylanish
const numbers = [0, 1, 2, 3, 4, 5];
for (const number of numbers) {
  console.log(number);
}
```

```python
# Python — for...of'ga juda o'xshaydi!
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:    # JS'dagi "for...of" bilan deyarli bir xil mantiq
    print(number)
```

> 🟢 **Yaxshi xabar:** Python'da `for` sikli aslida JavaScriptdagi **`for...of`** singari ishlaydi — to'g'ridan-to'g'ri elementlar bo'yicha aylanadi, indeks hisoblash shart emas. Python'da klassik `for (i=0; i<n; i++)` uslubi **umuman yo'q**.

`for` sikli list, tuple, string, set, dictionary — barchasida ishlaydi:

```python
language = 'Python'
for letter in language:        # satr bo'yicha aylanish
    print(letter)

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:         # tuple bo'yicha aylanish
    print(number)
```

**Dictionary bo'yicha aylanish** — JS'dagi `for...in` ga o'xshaydi (u ham kalitlarni beradi):

```python
person = {'first_name': 'Asabeneh', 'country': 'Finland'}

for key in person:                  # faqat kalitlarni beradi
    print(key)

for key, value in person.items():   # kalit va qiymatni birga olish uchun .items()
    print(key, value)
```

> 🟡 JS'da kalit-qiymatni birga olish uchun `Object.entries(obj)` bilan `for...of` birga ishlatilardi: `for (const [key, value] of Object.entries(obj))`. Python'da bu vazifani `.items()` bajaradi.

## range() funksiyasi

JavaScriptda klassik son oralig'i kerak bo'lganda `for (let i = 0; i < 10; i++)` deb yozardingiz. Python'da bu vazifani **`range()`** funksiyasi bajaradi — u sonlar ketma-ketligini yaratadi:

```python
for number in range(11):     # 0 dan 10 gacha (11 kirmaydi)
    print(number)

for number in range(0, 11, 2):   # 0 dan 10 gacha, 2 qadam bilan -> 0,2,4,6,8,10
    print(number)

for number in range(11, 0, -1):  # 11 dan 1 gacha, teskari -> kamayish bilan sanash
    print(number)
```

> 🟡 `range(start, end, step)` — `start` va `step` ixtiyoriy (standart `0` va `1`), `end` esa majburiy va **natijaga kirmaydi**, xuddi slicing'dagi kabi.

## Ichma-ich for sikli

JS'dagi kabi, bir sikl ichida ikkinchisini yozish mumkin:

```python
person = {
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
}

for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

## For Else

`while`dagi kabi, `for` sikli ham `else` bilan ishlay oladi — sikl **break qilinmasdan** tugagandan keyin ishga tushadi (JS'da bunga to'g'ridan-to'g'ri o'xshashi yo'q):

```python
for number in range(11):
    print(number)
else:
    print('Sikl', number, 'da to\'xtadi')
```

## Pass

Python'da kod bloki **majburiy** (bo'sh qoldirib bo'lmaydi), lekin hali kod yozmagan bo'lsangiz, **`pass`** so'zini "joy egallovchi (placeholder)" sifatida yozasiz:

```python
for number in range(6):
    pass    # hali hech narsa qilmaymiz, lekin xatolik chiqmasligi uchun shart
```

> 🟡 JS'da bo'sh blok `{}` deb qoldirish mumkin edi — Python'da bo'sh blok xato beradi, shu sababli `pass` kerak.

🌕 Siz katta bosqichni bosib o'tdingiz, to'xtamang! 10-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 10-kun

### 1-daraja

1. `for` sikli orqali 0 dan 10 gacha sanang, xuddi shuni `while` sikli bilan ham bajaring
2. `for` sikli orqali 10 dan 0 gacha sanang, xuddi shuni `while` sikli bilan ham bajaring
3. 7 marta `print()` chaqirib, quyidagi uchburchakni hosil qiling:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Ichma-ich sikllar orqali quyidagini hosil qiling:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. Quyidagi ko'paytirish jadvalini chiqaring:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   ...
   10 x 10 = 100
   ```

6. `['Python', 'Numpy', 'Pandas', 'Django', 'Flask']` ro'yxati bo'yicha `for` sikli orqali aylanib, har birini chiqaring
7. `for` sikli orqali 0 dan 100 gacha faqat juft sonlarni chiqaring
8. `for` sikli orqali 0 dan 100 gacha faqat toq sonlarni chiqaring

### 2-daraja

1. `for` sikli orqali 0 dan 100 gacha barcha sonlar yig'indisini chiqaring:

   ```sh
   Barcha sonlar yig'indisi: 5050
   ```

2. `for` sikli orqali 0 dan 100 gacha juft va toq sonlar yig'indisini alohida chiqaring.

### 3-daraja

1. [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) faylidagi davlatlar ro'yxati bo'yicha aylanib, nomida `'land'` so'zi bor barcha davlatlarni topib chiqaring.
2. `['banana', 'orange', 'mango', 'lemon']` mevalar ro'yxatini sikl orqali teskari tartibda chiqaring.
3. [countries-data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) faylidan foydalanib:
   - Ma'lumotlardagi tillarning umumiy sonini toping
   - Eng ko'p gaplashiladigan 10 tilni toping
   - Dunyodagi eng aholisi ko'p 10 davlatni toping

🎉 TABRIKLAYMIZ! 🎉

[<< 9-kun](./09_conditionals_uz.md) | [11-kun >>](./11_functions_uz.md)

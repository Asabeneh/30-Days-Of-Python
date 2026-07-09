<div align="center">
  <h1> 30 kunlik Python: 12-kun — Modullar</h1>
</div>

[<< 11-kun](./11_functions_uz.md) | [13-kun >>](./13_list_comprehension_uz.md)

- [📘 12-kun](#-12-kun)
  - [Modul nima](#modul-nima)
  - [Modul yaratish](#modul-yaratish)
  - [Modulni import qilish](#modulni-import-qilish)
  - [Modulning ichki (built-in) turlari](#modulning-ichki-built-in-turlari)
  - [💻 Mashqlar — 12-kun](#-mashqlar--12-kun)

# 📘 12-kun

## Modul nima

JavaScriptda kodni alohida fayllarga bo'lib, `import`/`export` orqali ulashgansiz. Python'da bu tushuncha **modul** deyiladi — ichida funksiya, o'zgaruvchi yoki katta kod bazasi bo'lgan oddiy `.py` fayl.

## Modul yaratish

`mymodule.py` nomli fayl yaratamiz:

```python
# mymodule.py fayli
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname

gravity = 9.81
person = {
    'firstname': 'Asabeneh',
    'age': 250,
    'country': 'Finland'
}
```

## Modulni import qilish

```javascript
// JavaScript (ES modules)
import * as myModule from './mymodule.js';
console.log(myModule.generateFullName('Asabeneh', 'Yetayeh'));
```

```python
# Python — main.py fayli
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))
```

> 🟡 Farqi: Python'da fayl kengaytmasi (`.py`) yozilmaydi, faqat modul nomi: `import mymodule` (`mymodule.py` faylidan).

**Faqat kerakli funksiyalarni import qilish** — JS'dagi `import { func } from './module.js'` ga to'g'ridan-to'g'ri mos keladi:

```javascript
// JavaScript
import { generateFullName, sumTwoNums, gravity } from './mymodule.js';
```

```python
# Python
from mymodule import generate_full_name, sum_two_nums, gravity
print(generate_full_name('Asabeneh', 'Yetayeh'))
```

**Import qilganda nom o'zgartirish** — JS'dagi `import { func as newName }` bilan bir xil mantiq, faqat `as` so'zi oxirida yoziladi:

```javascript
// JavaScript
import { generateFullName as fullname } from './mymodule.js';
```

```python
# Python
from mymodule import generate_full_name as fullname, gravity as g
print(fullname('Asabeneh', 'Yetayeh'))
```

## Modulning ichki (built-in) turlari

Pythonda tayyor modullar bor — JavaScriptdagi Node.js'ning ichki modullariga o'xshaydi (`fs`, `path`, `crypto` kabi). Eng ko'p ishlatiladiganlari:

**`math`** — matematik amallar va konstantalar (JS'dagi global `Math` obyektiga o'xshaydi):

```python
import math
print(math.pi)            # 3.14159... — JS'da Math.PI
print(math.sqrt(2))       # kvadrat ildiz — JS'da Math.sqrt(2)
print(math.floor(9.81))   # pastga yaxlitlash — JS'da Math.floor(9.81)
print(math.ceil(9.81))    # yuqoriga yaxlitlash — JS'da Math.ceil(9.81)
```

Faqat kerakli funksiyani olish mumkin: `from math import pi, sqrt`. Hammasini olish uchun `from math import *` (lekin bu usul tavsiya etilmaydi — qaysi funksiya qayerdan kelganini bilish qiyinlashadi).

**`random`** — tasodifiy son generatsiyasi (JS'dagi `Math.random()` ga o'xshaydi):

```python
from random import random, randint
print(random())        # 0 va 0.999... orasida tasodifiy son — JS'dagi Math.random()
print(randint(5, 20))   # 5 dan 20 gacha (ikkisi ham kiradi) tasodifiy butun son
```

**`statistics`** — statistik hisob-kitoblar uchun (JS'da bunga tayyor modul yo'q, qo'lda yozish kerak bo'lardi):

```python
from statistics import mean, median, mode, stdev
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))     # o'rtacha arifmetik
print(median(ages))   # mediana
```

**`os`** — operatsion tizim bilan ishlash (Node.js'dagi `fs`/`path` modullariga o'xshaydi):

```python
import os
os.mkdir('papka_nomi')   # papka yaratish
os.getcwd()                # joriy papka yo'lini olish
```

🌕 Siz uzoqqa ketyapsiz, davom eting! 12-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 12-kun

### 1-daraja

1. `random_user_id` funksiyasini yozing — 6 xonali/belgili tasodifiy ID generatsiya qilsin:
   ```py
   print(random_user_id())
   '1ee33d'
   ```
2. `user_id_gen_by_user` funksiyasini yozing — parametr olmaydi, lekin `input()` orqali ikki narsani so'raydi: belgilar soni va nechta ID kerakligi.
3. `rgb_color_gen` funksiyasini yozing — 0 dan 255 gacha 3 ta qiymatdan iborat RGB rang generatsiya qilsin:
   ```py
   print(rgb_color_gen())
   # rgb(125,244,255)
   ```

### 2-daraja

1. `list_of_hexa_colors` funksiyasini yozing — istalgan miqdordagi hex rang qaytarsin.
2. `list_of_rgb_colors` funksiyasini yozing — istalgan miqdordagi RGB rang qaytarsin.
3. `generate_colors` funksiyasini yozing — hex yoki rgb ranglarni istalgan miqdorda generatsiya qilsin:
   ```py
   generate_colors('hexa', 3)   # ['#a3e12f', '#03ed55', '#eb3d2b']
   generate_colors('rgb', 1)    # ['rgb(33,79,176)']
   ```

### 3-daraja

1. `shuffle_list` funksiyasini yozing — list oladi va aralashtirilgan holatini qaytaradi.
2. 0-9 oralig'idagi 7 ta **noyob** tasodifiy sondan iborat ro'yxat qaytaruvchi funksiya yozing.

🎉 TABRIKLAYMIZ! 🎉

[<< 11-kun](./11_functions_uz.md) | [13-kun >>](./13_list_comprehension_uz.md)

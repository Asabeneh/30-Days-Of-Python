<div align="center">
  <h1> 30 kunlik Python: 20-kun — PIP (Python paket menejeri)</h1>
</div>

[<< 19-kun](./19_file_handling_uz.md) | [21-kun >>](./21_classes_and_objects_uz.md)

- [📘 20-kun](#-20-kun)
  - [PIP nima](#pip-nima)
  - [Paketlarni o'rnatish](#paketlarni-ornatish)
  - [URL'dan ma'lumot o'qish](#urldan-malumot-oqish)
  - [Paket (package) yaratish](#paket-package-yaratish)
  - [💻 Mashqlar — 20-kun](#-mashqlar--20-kun)

# 📘 20-kun

## PIP nima

**PIP — JavaScriptdagi `npm`ning to'liq o'xshashi!** Bu — boshqa dasturchilar yaratgan tayyor kod to'plamlarini (paketlarni) o'rnatish vositasi. Har bir utilitani o'zingiz yozish shart emas — paket o'rnatib, uni import qilishingiz mumkin.

| | JavaScript (npm) | Python (pip) |
|---|---|---|
| Paket o'rnatish | `npm install paket_nomi` | `pip install paket_nomi` |
| Paketni o'chirish | `npm uninstall paket_nomi` | `pip uninstall paket_nomi` |
| O'rnatilgan paketlar ro'yxati | `npm list` | `pip list` |
| Loyihaning bog'liqliklari fayli | `package.json` | `requirements.txt` |
| Versiyani tekshirish | `npm --version` | `pip --version` |

## Paketlarni o'rnatish

Mashina o'qitish va ma'lumotlar tahlilida eng mashhur paketlardan biri — **NumPy**ni o'rnatib ko'ramiz:

```sh
pip install numpy
```

```python
>>> import numpy
>>> lst = [1, 2, 3, 4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr * 2
array([2, 4, 6, 8, 10])
```

**Paketni o'chirish:**

```sh
pip uninstall numpy
```

**O'rnatilgan paketlar haqida ma'lumot:**

```sh
pip list                  # barcha o'rnatilgan paketlar
pip show pandas           # bitta paket haqida batafsil
pip freeze                # paketlar va versiyalari ro'yxati (requirements.txt uchun)
```

> 🟡 `pip freeze > requirements.txt` — bu xuddi `package.json`dagi `dependencies` ro'yxatini saqlashga o'xshaydi. Boshqa kompyuterda `pip install -r requirements.txt` orqali hammasi qayta o'rnatiladi — `npm install` qanday `package.json`dan o'qisa, shunga o'xshash.

## URL'dan ma'lumot o'qish

JavaScriptda tarmoqdan ma'lumot olish uchun **`fetch()`** ishlatgansiz. Python'da bu vazifani **`requests`** paketi bajaradi (avval o'rnatish kerak: `pip install requests`):

```javascript
// JavaScript
const response = await fetch(url);
const data = await response.json();
```

```python
# Python
import requests

response = requests.get(url)        # tarmoqqa so'rov yuborish
print(response.status_code)           # 200 — muvaffaqiyatli
data = response.json()                 # JSON javobni dictionary/listga aylantirish
```

| Metod/xususiyat | Vazifasi |
|---|---|
| `.get(url)` | URL'ga so'rov yuborish (JS'dagi `fetch(url)`) |
| `.status_code` | javob holati (200 — muvaffaqiyat) |
| `.headers` | javob sarlavhalari |
| `.text` | javobni oddiy matn sifatida olish |
| `.json()` | javobni JSON'dan dictionary/listga aylantirish (JS'dagi `response.json()`) |

```python
import requests

url = 'https://restcountries.com/v3.1/all'
response = requests.get(url)
countries = response.json()
print(countries[0]['name'])
```

## Paket (package) yaratish

JS'da bir nechta modulni papkaga joylab, `index.js` orqali eksport qilgansiz. Python'da bu **paket (package)** deyiladi — ichida `__init__.py` (bo'sh fayl bo'lishi mumkin) bo'lgan oddiy papka:

```sh
mypackage/
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

> 🟡 `__init__.py` — bu papkani Python "bu shunchaki papka emas, bu **paket**" deb tanishi uchun kerak bo'lgan maxsus fayl. Bo'sh bo'lsa ham bo'ladi.

```python
from mypackage import arithmetic
print(arithmetic.add_numbers(1, 2, 3, 5))   # 11

from mypackage import greet
print(greet.greet_person('Asabeneh', 'Yetayeh'))
```

🌕 Siz doimo rivojlanmoqdasiz, 20 qadam oldindasiz! 20-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 20-kun

1. `http://www.gutenberg.org/files/1112/1112.txt` manzilidan "Romeo va Julyetta" matnini o'qib, eng ko'p uchraydigan 10 so'zni toping.
2. `https://api.thecatapi.com/v1/breeds` API'sidan ma'lumot olib:
   - Mushuklar vazni bo'yicha min, max, o'rtacha, mediana va standart og'ishini toping
   - Mushuklar umr ko'rish davomiyligi bo'yicha xuddi shularni toping
   - Davlat va zot bo'yicha chastota jadvalini tuzing
3. [Davlatlar API](https://restcountries.com/v3.1/all)dan foydalanib:
   - Eng katta 10 davlatni toping
   - Eng ko'p gaplashiladigan 10 tilni toping
   - API'dagi tillar umumiy sonini toping

🎉 TABRIKLAYMIZ! 🎉

[<< 19-kun](./19_file_handling_uz.md) | [21-kun >>](./21_classes_and_objects_uz.md)

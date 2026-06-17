<div align="center">
  <h1> 30 kunlik Python: 16-kun — Sana va vaqt (datetime)</h1>
</div>

[<< 15-kun](./15_python_type_errors_uz.md) | [17-kun >>](./17_exception_handling_uz.md)

- [📘 16-kun](#-16-kun)
  - [datetime modulidan ma'lumot olish](#datetime-modulidan-malumot-olish)
  - [Sanani formatlash — strftime](#sanani-formatlash--strftime)
  - [Satrni sanaga aylantirish — strptime](#satrni-sanaga-aylantirish--strptime)
  - [date va time obyektlari](#date-va-time-obyektlari)
  - [Ikki sana orasidagi farq](#ikki-sana-orasidagi-farq)
  - [💻 Mashqlar — 16-kun](#-mashqlar--16-kun)

# 📘 16-kun

## datetime modulidan ma'lumot olish

JavaScriptda sana bilan ishlash uchun **`new Date()`** ishlatgansiz. Python'da bu vazifani **`datetime`** moduli bajaradi:

```javascript
// JavaScript
const now = new Date();
console.log(now.getDate(), now.getMonth() + 1, now.getFullYear());
```

```python
# Python
from datetime import datetime
now = datetime.now()
print(now)              # 2021-07-08 07:34:46.549883

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute

print(f'{day}/{month}/{year}, {hour}:{minute}')   # 8/7/2021, 7:38
```

> 🟡 Farqi: JS'da `getMonth()` 0-dan boshlanadi (Yanvar = 0), shuning uchun `+1` qo'shish kerak edi. **Python'da oy raqami to'g'ridan-to'g'ri 1-dan boshlanadi** — `month` xususiyati Yanvar uchun `1` qaytaradi, qo'shimcha hisoblash kerak emas.

**Timestamp** — 1970-yil 1-yanvardan beri o'tgan soniyalar soni:

```python
print(now.timestamp())
```

> 🟡 JS'da `Date.now()` millisekundlarda qaytaradi, Python'dagi `.timestamp()` esa **soniyalarda** qaytaradi — 1000 ga ko'paytirish kerak bo'lsa, solishtirayotganda esda tuting.

## Sanani formatlash — strftime

JS'da sanani chiroyli formatda chiqarish uchun `toLocaleDateString()` yoki qo'lda formatlashardingiz. Python'da **`.strftime()`** metodi maxsus belgilar orqali ishlaydi:

```python
from datetime import datetime
now = datetime.now()

t = now.strftime("%H:%M:%S")
print('vaqt:', t)                              # 18:21:40

time_one = now.strftime("%d/%m/%Y, %H:%M:%S")    # kun/oy/yil, soat:minut:soniya
print('format 1:', time_one)                     # 28/06/2022, 18:21:40
```

Eng ko'p ishlatiladigan belgilar: `%d` (kun), `%m` (oy), `%Y` (yil, 4 xonali), `%H` (soat), `%M` (minut), `%S` (soniya), `%B` (oy nomi to'liq).

## Satrni sanaga aylantirish — strptime

Bu `strftime`ning teskarisi — matnni `datetime` obyektiga aylantiradi:

```python
from datetime import datetime
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)   # 2019-12-05 00:00:00
```

> 🟡 JS'da bunga eng yaqini `new Date('5 December, 2019')` — lekin JS bu formatni avtomatik "taxmin qilib" o'qiydi, Python'da esa formatni **aniq ko'rsatishingiz kerak**, bu esa xatolarni kamaytiradi.

## date va time obyektlari

Agar faqat sana (vaqtsiz) yoki faqat vaqt (sanasiz) kerak bo'lsa:

```python
from datetime import date, time

d = date(2020, 1, 1)
print(d)                  # 2020-01-01
print(date.today())       # bugungi sana

t = time(10, 30, 50)       # faqat vaqt: soat, minut, soniya
print(t)                   # 10:30:50
```

## Ikki sana orasidagi farq

Python'da ikki sanani **to'g'ridan-to'g'ri `-` bilan ayirish** mumkin — bu juda qulay (JS'da millisekundlarga aylantirib, qo'lda hisoblash kerak edi):

```python
from datetime import date, datetime, timedelta

today = date(year=2019, month=12, day=5)
new_year = date(year=2020, month=1, day=1)
print(new_year - today)   # 27 days, 0:00:00

t1 = timedelta(weeks=12, days=10, hours=4)
t2 = timedelta(days=7, hours=5)
print(t1 - t2)              # timedelta — vaqt oralig'ini ifodalaydi
```

> 🟢 JS'da: `(newYear - today) / (1000 * 60 * 60 * 24)` deb millisekundlarni kunlarga aylantirish kerak edi. Python'da `datetime`/`date` obyektlarini ayirish natijasi avtomatik **`timedelta`** (vaqt oralig'i) obyektini beradi — qo'shimcha hisoblash shart emas.

🌕 Siz ajoyibsiz, 16 qadam oldindasiz! 16-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 16-kun

1. `datetime` modulidan joriy kun, oy, yil, soat, minut va timestamp'ni olib chiqing.
2. Joriy sanani `"%m/%d/%Y, %H:%M:%S"` formatida chiqaring.
3. `"5 December, 2019"` satrini `datetime` obyektiga aylantiring.
4. Hozirgi vaqt va Yangi yil orasidagi farqni hisoblang.
5. 1970-yil 1-yanvar va hozirgi vaqt orasidagi farqni hisoblang.
6. O'ylab ko'ring: `datetime` modulini qayerda ishlatish mumkin? Masalan:
   - Vaqt qatorlari (time series) tahlili
   - Ilovadagi har bir harakatning vaqt belgisini (timestamp) olish
   - Blogga post qo'shish vaqti

🎉 TABRIKLAYMIZ! 🎉

[<< 15-kun](./15_python_type_errors_uz.md) | [17-kun >>](./17_exception_handling_uz.md)

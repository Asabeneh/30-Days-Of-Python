<div align="center">
  <h1> 30 kunlik Python: 18-kun — Regulyar ifodalar (Regex)</h1>
</div>

[<< 17-kun](./17_exception_handling_uz.md) | [19-kun >>](./19_file_handling_uz.md)

- [📘 18-kun](#-18-kun)
  - [Regulyar ifodalar nima](#regulyar-ifodalar-nima)
  - [re modulidagi metodlar](#re-modulidagi-metodlar)
  - [Matnni regex orqali bo'lish va almashtirish](#matnni-regex-orqali-bolish-va-almashtirish)
  - [Regex qoliplarini yozish](#regex-qoliplarini-yozish)
  - [💻 Mashqlar — 18-kun](#-mashqlar--18-kun)

# 📘 18-kun

## Regulyar ifodalar nima

**Regulyar ifoda (RegEx)** — matnda qoliplarni (pattern) topish uchun maxsus belgilar ketma-ketligi. **Yaxshi xabar: JavaScript ham regulyar ifodalarni qo'llab-quvvatlaydi va sintaksis deyarli bir xil!** Asosiy farq — yozilish tarzida.

```javascript
// JavaScript — regex slash (/) orasida yoziladi
const pattern = /apple/i;     // i — katta-kichik harfni farqlamaslik flagi
const found = 'I love Apple'.match(pattern);
```

```python
# Python — regex satr sifatida yoziladi, oldidan 'r' qo'yiladi
import re
pattern = r'apple'
found = re.search(pattern, 'I love Apple', re.I)   # re.I — katta-kichik harfni farqlamaslik flagi
```

> 🟡 `r'...'` — "raw string" degani, bu yerda teskari chiziq (`\`) belgilari maxsus ma'noda ishlatilishi uchun kerak. JS'da regex `/.../ ` belgilar orasida yoziladi, Python'da esa oddiy satr (lekin `r` prefiksi bilan).

## re modulidagi metodlar

Pythonda regex bilan ishlash uchun **`re`** modulini import qilish kerak (JS'da bu o'rnatilgan, `RegExp` global obyekti orqali ishlaydi):

| Python | JavaScript'dagi o'xshashi | Vazifasi |
|---|---|---|
| `re.match(pattern, text)` | `text.match(/^pattern/)` | faqat matn **boshidan** qidiradi |
| `re.search(pattern, text)` | `text.match(pattern)` | matnning istalgan joyidan **birinchi** moslikni topadi |
| `re.findall(pattern, text)` | `text.match(/pattern/g)` | **barcha** mosliklarni ro'yxat qilib qaytaradi |
| `re.sub(pattern, new, text)` | `text.replace(/pattern/g, new)` | moslikni almashtiradi |
| `re.split(pattern, text)` | `text.split(/pattern/)` | matnni qolip bo'yicha bo'ladi |

**`match()`** — faqat matn boshini tekshiradi:

```python
import re
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)             # <re.Match object; span=(0, 15), match='I love to teach'>
print(match.span())      # (0, 15) — boshlanish va tugash indekslari
```

**`search()`** — matnning istalgan joyidan qidiradi (`match()`dan ko'proq ishlatiladi):

```python
txt = 'Python eng chiroyli til. Men birinchi til sifatida pythonni tavsiya qilaman'
match = re.search('birinchi', txt, re.I)
print(match.span())   # (26, 34)
```

**`findall()`** — barcha mosliklarni ro'yxat qilib qaytaradi (eng ko'p ishlatiladigan):

```python
txt = 'Python chiroyli til. python juda mashhur til.'
matches = re.findall('python', txt, re.I)
print(matches)   # ['Python', 'python'] — re.I tufayli ikkisi ham topiladi
```

## Matnni regex orqali bo'lish va almashtirish

**`sub()`** — qolipga mos kelgan qismni almashtiradi:

```python
txt = 'Men %P%y%t%h%on dasturlash tilini yaxshi ko\'raman'
cleaned = re.sub('%', '', txt)    # barcha % belgilarini olib tashlash
print(cleaned)   # Men Python dasturlash tilini yaxshi ko'raman
```

**`split()`** — qolip bo'yicha matnni bo'laklarga ajratadi:

```python
txt = '''Birinchi qator
Ikkinchi qator
Uchinchi qator'''
print(re.split('\n', txt))   # ['Birinchi qator', 'Ikkinchi qator', 'Uchinchi qator']
```

## Regex qoliplarini yozish

Regulyar ifoda belgilari **JavaScript bilan deyarli 100% bir xil** — bu sizning ulkan afzalligingiz! Quyidagi jadval ikkisida ham bir xil ishlaydi:

| Belgi | Ma'nosi |
|---|---|
| `[abc]` | a, b yoki c dan biri |
| `[a-z]` | a dan z gacha istalgan kichik harf |
| `[A-Z]` | A dan Z gacha istalgan katta harf |
| `[0-9]` | istalgan raqam |
| `\d` | raqam (digit) |
| `\D` | raqam emas |
| `.` | qator ko'chirishdan tashqari istalgan belgi |
| `^` | shu bilan boshlanadi |
| `$` | shu bilan tugaydi |
| `*` | oldingi belgi 0 yoki undan ko'p marta |
| `+` | oldingi belgi 1 yoki undan ko'p marta |
| `?` | oldingi belgi 0 yoki 1 marta (ixtiyoriy) |
| `{3}` | aynan 3 marta |
| `{3,8}` | 3 dan 8 martagacha |
| `\|` | yoki (alternativ) |
| `()` | guruhlash |

**Misollar:**

```python
import re

# Kvadrat qavs — bir nechta variantdan biri
matches = re.findall(r'[Aa]pple', 'Apple va apple mevalar')   # ['Apple', 'apple']

# \d — raqamlarni topish
txt = 'Bu misol 6-dekabr 2019-yilda va 8-iyul 2021-yilda yaratilgan'
matches = re.findall(r'\d+', txt)   # ['6', '2019', '8', '2021'] — '+' bir yoki undan ko'p raqam degani

# {4} — aniq 4 ta belgi
matches = re.findall(r'\d{4}', txt)   # ['2019', '2021'] — faqat 4 xonali sonlar

# ^ — boshlanish
matches = re.findall(r'^Bu', txt)   # ['Bu']

# [^...] — inkor (negation): A-Z, a-z va bo'sh joydan boshqa hammasi
matches = re.findall(r'[^A-Za-z ]+', txt)
```

> 🟢 JS'da xuddi shu qoliplarni `/[Aa]pple/`, `/\d+/`, `/\d{4}/`, `/^Bu/`, `/[^A-Za-z ]+/` deb yozardingiz — **belgilarning o'zi bir xil**, faqat qaysi qiyshiq chiziq ichiga olinishi farq qiladi.

🌕 Davom etayotganingiz zo'r! 18-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 18-kun

### 1-daraja

1. Quyidagi paragrafda eng ko'p uchraydigan so'z qaysi?

   ```py
   paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
   ```

2. X-o'qida zarrachalarning joylashuvi: -12, -4, -3, -1 (manfiy tomonda), 0 (markazda), 4 va 8 (musbat tomonda). Bu raqamlarni matndan regex orqali ajratib olib, eng uzoq ikki zarracha orasidagi masofani toping.

### 2-daraja

1. Satrning to'g'ri Python o'zgaruvchi nomi ekanligini tekshiruvchi regex qolip yozing:
   ```sh
   is_valid_variable('first_name')   # True
   is_valid_variable('first-name')   # False
   is_valid_variable('1first_name')  # False
   ```

### 3-daraja

1. Quyidagi matnni "tozalang" (keraksiz belgilarni olib tashlang) va eng ko'p uchraydigan 3 so'zni toping:

   ```py
   sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding...'''
   ```

🎉 TABRIKLAYMIZ! 🎉

[<< 17-kun](./17_exception_handling_uz.md) | [19-kun >>](./19_file_handling_uz.md)

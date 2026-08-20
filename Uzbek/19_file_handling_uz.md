<div align="center">
  <h1> 30 kunlik Python: 19-kun — Fayllar bilan ishlash</h1>
</div>

[<< 18-kun](./18_regular_expressions_uz.md) | [20-kun >>](./20_python_package_manager_uz.md)

- [📘 19-kun](#-19-kun)
  - [Faylni ochish va o'qish](#faylni-ochish-va-oqish)
  - [Faylga yozish](#faylga-yozish)
  - [Faylni o'chirish](#faylni-ochirish)
  - [Fayl turlari](#fayl-turlari)
  - [💻 Mashqlar — 19-kun](#-mashqlar--19-kun)

# 📘 19-kun

## Faylni ochish va o'qish

> 🟡 **Eslatma:** Agar siz JavaScript'ni faqat brauzerda ishlatgan bo'lsangiz, fayllar bilan to'g'ridan-to'g'ri ishlash sizga unchalik tanish bo'lmasligi mumkin (brauzer xavfsizlik sababli kompyuterdagi fayllarga erkin kira olmaydi). Bu — Node.js'dagi **`fs`** moduliga o'xshaydi (`fs.readFile()`, `fs.writeFile()`), faqat Python'da bu imkoniyat tilning o'zida tayyor holda keladi.

Fayllar bilan ishlash uchun Python'da **`open()`** ichki funksiyasi ishlatiladi:

```python
f = open('fayl_nomi', mode)   # mode: 'r' (o'qish), 'w' (yozish), 'a' (qo'shish), 'x' (yaratish)
```

| Rejim | Vazifasi |
|---|---|
| `'r'` | O'qish (standart). Fayl mavjud bo'lmasa, xatolik beradi |
| `'w'` | Yozish. Mavjud bo'lsa, **tarkibini o'chirib**, qaytadan yozadi; mavjud bo'lmasa, yaratadi |
| `'a'` | Qo'shish (append). Faylning oxiriga qo'shadi; mavjud bo'lmasa, yaratadi |
| `'x'` | Yangi fayl yaratish. Fayl mavjud bo'lsa, xatolik beradi |

**Faylni o'qish:**

```python
f = open('./files/reading_file_example.txt')
txt = f.read()           # butun matnni satr sifatida o'qiydi
print(txt)
f.close()                 # faylni yopish — muhim!
```

| Metod | Vazifasi |
|---|---|
| `.read()` | butun matnni bitta satr sifatida o'qiydi |
| `.readline()` | faqat birinchi qatorni o'qiydi |
| `.readlines()` | har bir qatorni ro'yxat elementi sifatida qaytaradi |

> ⚠️ Faylni ochgandan keyin **`.close()`** bilan yopishni unutmaslik kerak — bu xuddi Node.js'da fayl ochib, ishlatib bo'lgach yopish kerakligi kabi.

**`with` bilan ishlash — tavsiya etiladigan usul:**

Faylni yopishni unutib qo'yish — keng tarqalgan xato. **`with`** kalit so'zi faylni **avtomatik yopadi**, hatto xatolik yuz bersa ham:

```python
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(lines)
# bu yerga kelganda fayl avtomatik yopilgan bo'ladi
```

> 🟢 Bu JS'dagi `try...finally { file.close() }` blokini yozishdan qutqaradi — Python buni sizning o'rningizga avtomatik bajaradi.

## Faylga yozish

```python
with open('./files/writing_file_example.txt', 'w') as f:
    f.write('Bu matn yangi yaratilgan faylga yoziladi')

with open('./files/reading_file_example.txt', 'a') as f:
    f.write('Bu matn faylning oxiriga qo\'shiladi')
```

## Faylni o'chirish

```python
import os

if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('Bunday fayl mavjud emas')
```

## Fayl turlari

### JSON fayllar

**JSON — JavaScript Object Notation.** Bu format aslida **sizga juda tanish** — JS'da `JSON.parse()` va `JSON.stringify()` orqali ishlatgan bo'lsangiz kerak!

| JavaScript | Python | Vazifasi |
|---|---|---|
| `JSON.parse(jsonStr)` | `json.loads(json_str)` | JSON satrini obyekt/dictionary'ga aylantiradi |
| `JSON.stringify(obj)` | `json.dumps(dct)` | obyekt/dictionary'ni JSON satriga aylantiradi |
| `fs.writeFile(path, JSON.stringify(obj))` | `json.dump(dct, f)` | dictionary'ni to'g'ridan-to'g'ri faylga JSON qilib yozadi |

```python
import json

# JSON satrini dictionary'ga aylantirish — JS'dagi JSON.parse() bilan bir xil
person_json = '{"name": "Asabeneh", "country": "Finland"}'
person_dct = json.loads(person_json)
print(person_dct['name'])    # Asabeneh

# Dictionary'ni JSON satriga aylantirish — JS'dagi JSON.stringify() bilan bir xil
person = {'name': 'Asabeneh', 'country': 'Finland', 'skills': ['JS', 'Python']}
person_json = json.dumps(person, indent=4)   # indent — chiroyli formatlash uchun
print(person_json)

# To'g'ridan-to'g'ri faylga JSON qilib saqlash
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

### CSV fayllar

**CSV (Comma Separated Values)** — jadval ma'lumotlarini saqlash uchun oddiy format (Excel jadvaliga o'xshaydi). JS'da bunga tayyor modul yo'q, qo'lda satrlarni vergul bo'yicha bo'lish kerak bo'lardi.

```python
import csv

with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        print(row)   # har bir qator — ro'yxat (list) sifatida keladi
```

### XML fayllar

XML — HTML'ga o'xshash, teglar orqali tartiblangan format. JS'da `DOMParser` bilan o'qilardi, Python'da `xml.etree.ElementTree` moduli ishlatiladi:

```python
import xml.etree.ElementTree as ET

tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Asosiy teg:', root.tag)
for child in root:
    print('Maydon:', child.tag)
```

🌕 Siz katta muvaffaqiyatga erishyapsiz, davom eting! 19-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 19-kun

### 1-daraja

1. Matndagi qatorlar va so'zlar sonini sanovchi funksiya yozing. Barcha fayllar `data` papkasida:
   - `obama_speech.txt` faylini o'qib, qator va so'zlar sonini sanang
   - `michelle_obama_speech.txt`, `donald_speech.txt`, `melina_trump_speech.txt` fayllari uchun ham xuddi shuni bajaring
2. `data` papkasidagi `countries_data.json` faylini o'qib, eng ko'p gaplashiladigan 10 tilni topuvchi funksiya yozing.
3. Xuddi shu fayldan eng aholisi ko'p 10 davlatni topuvchi funksiya yozing.

### 2-daraja

1. `email_exchange_big.txt` faylidan barcha kiruvchi email manzillarini ro'yxat qilib ajratib oling.
2. `find_most_common_words` funksiyasini yozing — matn (yoki fayl) va son oladi, eng ko'p uchraydigan so'zlarni kamayish tartibida qaytaradi.
3. `find_most_frequent_words` funksiyasi orqali Obama, Michelle, Trump va Melaniyaning nutqlaridagi eng ko'p ishlatilgan 10 so'zni toping.
4. Ikki matn orasidagi o'xshashlikni tekshiruvchi dastur yozing (matnni tozalash, "to'siq so'zlar"ni olib tashlash va o'xshashlikni hisoblash funksiyalari kerak bo'ladi).
5. `romeo_and_juliet.txt` faylida eng ko'p takrorlangan 10 so'zni toping.
6. `hacker_news.csv` faylini o'qib:
   - "python" yoki "Python" so'zi bor qatorlar sonini sanang
   - "JavaScript" so'zi bor qatorlar sonini sanang
   - "Java" bor, lekin "JavaScript" bo'lmagan qatorlar sonini sanang

🎉 TABRIKLAYMIZ! 🎉

[<< 18-kun](./18_regular_expressions_uz.md) | [20-kun >>](./20_python_package_manager_uz.md)

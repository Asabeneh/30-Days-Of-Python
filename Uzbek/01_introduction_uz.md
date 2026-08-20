<div align="center">
  <h1> 30 kunlik Python: 1-kun - Kirish</h1>
</div>

> 📌 **Eslatma:** Bu material JavaScript asoslarini (oddiy ma'lumot turlari, matematik amallar, if/else mantiqi) biladigan o'quvchilar uchun moslashtirilgan. Har bir yangi Python tushunchasi JavaScriptdagi mos keladigan narsa bilan solishtiriladi.

## Xush kelibsiz

**Tabriklaymiz** — siz *30 kunlik Python* dasturlash challenge'iga qatnashishga qaror qildingiz. Siz JavaScript orqali dasturlashning asosiy mantiqini (o'zgaruvchilar, agar/aks holda, matematik amallar) allaqachon bilasiz. Demak, bu yerda siz butunlay yangidan boshlamaysiz — siz allaqachon bilgan tushunchalarni **yangi tilning sintaksisi (yozilish qoidalari)** bilan tanishtirib boramiz.

## Kirish: Python nima?

Python — bu umumiy maqsadlar uchun yuqori darajadagi (high-level) dasturlash tili. JavaScript kabi, Python ham:

- **Interpretatsiya qilinadigan til** — kod oldindan "compile" qilinmaydi, qator-qator ishga tushiriladi (xuddi siz brauzer konsolida JavaScript yozganingizda bo'lgani kabi).
- **Ochiq manbali (open source)** — bepul va kodi ochiq.
- **Obyektga yo'naltirilgan (object-oriented)** — JavaScriptdagi kabi obyektlar bilan ishlash mumkin.

Pythonni golland dasturchisi Gvido van Rossum yaratgan. Tilning nomi mashhur britaniyalik komediya seriali *Monty Python's Flying Circus*dan olingan (ilon — pythonga aloqasi yo'q!). Birinchi versiyasi 1991-yil 20-fevralda chiqqan.

Bu challenge 30 kunga bo'lingan, lekin asosiysi — shoshilmang. To'liq tushunib, mashq qilib o'tish 30 kundan 100 kungacha vaqt olishi mumkin, va bu normal holat.

## Nega Python?

Python inson tiliga juda yaqin yoziladi, shu sababli o'rganish va o'qish oson. Google kabi kompaniyalar undan veb-ilovalar, desktop dasturlar, tizim boshqaruvi va mashinaviy o'qitish (machine learning) kutubxonalarini yaratishda foydalanadi.

**JavaScript bilan qisqacha taqqoslash:**

| | JavaScript | Python |
|---|---|---|
| Asosan qayerda ishlatiladi | Brauzer, Node.js (server) | Server, ma'lumotlar tahlili, AI/ML, avtomatlashtirish, skriptlar |
| Qatorni tugatish | `;` (ixtiyoriy) | Kerak emas |
| Kod blokini belgilash | `{ }` (qavslar) | Bo'sh joy — **indentatsiya** (pastda tushuntiramiz) |
| Konsolga chiqarish | `console.log()` | `print()` |
| O'zgaruvchi e'lon qilish | `let`, `const`, `var` | Shunchaki nom yozasiz (kalit so'zsiz) |

## Muhitni sozlash

### Pythonni o'rnatish

Python kodini ishga tushirish uchun avval Pythonni kompyuteringizga o'rnatishingiz kerak — xuddi JavaScript uchun Node.js'ni o'rnatganingizdek. [python.org](https://www.python.org/) saytidan yuklab oling.

O'rnatilganini tekshirish uchun terminalga yozing:

```shell
python3 --version
```

Versiya 3.6 yoki undan yuqori bo'lishi kerak.

### Python Shell (interaktiv qobiq)

JavaScriptda brauzer konsoli yoki Node.js'ning REPL rejimida (`node` deb yozib) bitta buyruqni yozib, natijani darrov ko'rishingiz mumkin edi, eslaysizmi? Pythonda ham xuddi shunday narsa bor — u **Python Shell** deyiladi.

Terminalga shuni yozing:

```shell
python3
```

Shundan so'ng `>>>` belgisi chiqadi — bu Python sizdan kod kutayotganini bildiradi (xuddi brauzer konsolidagi `>` belgisiga o'xshaydi). Shelldan chiqish uchun `exit()` deb yozing.

**Izoh yozish:** JavaScriptda izoh `//` bilan boshlanadi. Pythonda esa **hash (#)** belgisi bilan boshlanadi:

```python
# bu Python'dagi izoh — JavaScriptdagi // o'rnini bosadi
# Python bu qatorni umuman ishga tushirmaydi
```

Keling, matematik amallarni Python shellda sinab ko'ramiz (bular JavaScriptdagidek ishlaydi):

- `2 + 3` → `5`
- `3 - 2` → `1`
- `3 * 2` → `6`
- `3 / 2` → `1.5`
- `3 ** 2` → `9` (daraja — JavaScriptda bu `Math.pow(3, 2)` yoki `3 ** 2`)

Pythonda yana ikki qo'shimcha amal bor, JavaScriptda kamroq ishlatiladi:

- `3 % 2` → `1` — **modul (qoldiq)**. JavaScriptda xuddi shu `%` belgisi bilan ishlaydi, demak bu tanish bo'lishi kerak.
- `3 // 2` → `1` — **butun qismli bo'lish (floor division)**. Bu natijani pastga yaxlitlab, faqat butun qismini qaytaradi. JavaScriptda bunga to'g'ridan-to'g'ri belgi yo'q, odatda `Math.floor(3 / 2)` deb yozardik.

### Visual Studio Code o'rnatish

Shell kichik kodlarni sinash uchun yaxshi, lekin katta loyihalar uchun kod muharriri (code editor) kerak bo'ladi. Biz [Visual Studio Code](https://code.visualstudio.com/) dan foydalanamiz — agar siz JavaScript yozishda VS Code ishlatgan bo'lsangiz, interfeysi tanish bo'ladi.

Desktopingizda `30DaysOfPython` nomli papka yarating, uni VS Code orqali oching va ichida `helloworld.py` faylini yarating. Python fayllari **`.py`** kengaytmasi bilan tugaydi — xuddi JavaScript fayllari `.js` bilan tugaganidek.

## Python asoslari

### Python sintaksisi

Python kodini ham interaktiv shell'da, ham `.py` kengaytmali faylda yozish mumkin.

### Indentatsiya — eng katta farqlardan biri!

JavaScriptda kod blokini (masalan, `if` ichidagi kodni) jingalak qavslar `{ }` bilan belgilaymiz:

```javascript
if (yosh > 18) {
  console.log("Katta odam");
}
```

Qavslar ichidagi bo'sh joy (indentatsiya) shunchaki o'qish uchun chiroyli ko'rinish beradi — siz uni olib tashlasangiz ham kod ishlayveradi.

**Pythonda esa bunday emas.** Pythonda jingalak qavslar umuman yo'q. Blok qaerdan boshlanib, qaerda tugashini **faqat bo'sh joy (indentatsiya)** ko'rsatadi:

```python
if yosh > 18:
    print("Katta odam")  # bu qator 4 bo'sh joy bilan ichkariga surilgan
```

Bu yerda 4 bo'sh joy (yoki bitta Tab) — xuddi jingalak qavs ichidagi kodga teng. Agar bu bo'sh joyni noto'g'ri qo'ysangiz, Python xato beradi. Buni shunday tasavvur qiling: JavaScriptda qutilarni qavs bilan "yopib qo'ysak", Pythonda qutilarni faqat **kerakli darajada ichkariga surib** ajratamiz — qutining "chegarasi" jingalak qavs emas, balki **necha qadam ichkarida turgani**.

### Izohlar (Comments)

Yakka qatorli izoh:

```python
# Bu birinchi izoh
# Bu ikkinchi izoh
# Python dunyoni egallayapti
```

Ko'p qatorli izoh uchun uchlik qo'shtirnoq ishlatiladi (agar o'zgaruvchiga bog'lanmagan bo'lsa):

```python
"""Bu ko'p qatorli izoh
bir necha qatorni egallaydi
Python dunyoni egallayapti
"""
```

### Ma'lumot turlari (Data Types)

JavaScriptda asosiy ma'lumot turlarini bilasiz: `number`, `string`, `boolean`, `array`, `object`. Pythonda ham shunga o'xshash turlar bor, lekin ba'zilari biroz farq qiladi. Keling, ularni birma-bir ko'rib chiqamiz.

#### Raqamlar (Number)

JavaScriptda barcha raqamlar bitta tur — `number` hisoblanadi (`5` ham, `5.5` ham). **Pythonda esa raqamlar uchta alohida turga bo'linadi:**

- **Integer (butun son):** manfiy, nol va musbat butun sonlar.
    Misol: `... -3, -2, -1, 0, 1, 2, 3 ...`
- **Float (kasr son):** o'nlik kasr sonlar.
    Misol: `... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...`
- **Complex (kompleks son):** matematikada uchraydigan, haqiqiy va mavhum qismdan iborat son. Boshlang'ich bosqichda buni chuqur bilish shart emas.
    Misol: `1 + 2j`

> 🟡 **Tasavvur qiling:** JavaScriptda barcha raqamlar bitta "qutida" saqlanadi. Pythonda esa raqamlar uchun ikkita alohida quti bor: biri faqat butun sonlar uchun (Integer), ikkinchisi kasr sonlar uchun (Float).

#### Satr (String)

Bir yoki bir nechta belgilar to'plami, bir tirnoq (`'...'`) yoki qo'sh tirnoq (`"..."`) ichida — xuddi JavaScriptdagidek ishlaydi.

```python
'Asabeneh'
'Finland'
'Python'
'Men o\'qitishni yaxshi ko\'raman'
```

#### Mantiqiy qiymat (Boolean)

JavaScriptda `true` va `false` — kichik harf bilan yoziladi. **Pythonda esa bu so'zlar katta harf bilan boshlanadi: `True` va `False`.** Bu eng ko'p uchraydigan xatolardan biri, ehtiyot bo'ling!

```python
True   # Chiroq yonib turibdimi? Agar yonib tursa — True
False  # Chiroq yonib turibdimi? Agar o'chiq bo'lsa — False
```

#### Ro'yxat (List)

Python'dagi **list** — JavaScriptdagi **array (massiv)** bilan bevosita bir xil tushuncha. Tartiblangan elementlar to'plami, kvadrat qavs `[ ]` ichida yoziladi, va turli xil ma'lumot turlarini bir vaqtda saqlashi mumkin.

```python
[0, 1, 2, 3, 4, 5]                          # raqamlar ro'yxati
['Banan', 'Apelsin', 'Mango', 'Avokado']    # mevalar ro'yxati (satrlar)
['O\'zbekiston', 'Finlandiya', 'Shvetsiya'] # davlatlar ro'yxati
['Banan', 10, False, 9.81]                  # aralash turlar — satr, integer, boolean, float
```

#### Lug'at (Dictionary)

Python'dagi **dictionary** — JavaScriptdagi **object (obyekt)**ga juda o'xshaydi: kalit (key) va qiymat (value) juftliklarida ma'lumot saqlaydi, faqat tartibsiz to'plam hisoblanadi.

```python
{
    'ism': 'Asabeneh',
    'familiya': 'Yetayeh',
    'davlat': 'Finlandiya',
    'yosh': 25,
    'turmush_qurgan': True,
    'koonikmalar': ['JS', 'React', 'Node', 'Python']
}
```

JavaScriptda buni shunga o'xshash yozardingiz: `{ ism: 'Asabeneh', yosh: 25 }`. Farq shundaki, Python dictionary'sida kalitlar odatda tirnoq bilan yoziladi.

#### Tuple — JavaScriptda to'g'ridan-to'g'ri o'xshashi yo'q!

**Tuple** — list kabi tartiblangan to'plam, lekin **yaratilgandan keyin uni o'zgartirib bo'lmaydi** (immutable). Yumaloq qavs `( )` bilan yoziladi.

> 🟡 **Analogiya:** Listni — siz istalgan vaqt narsalarni solib-chiqarib turadigan **ochiq quti** deb tasavvur qiling. Tuple esa — bir marta narsalarni solib, **muhrlab yopilgan quti**. Ichidagilarni ko'rish mumkin, lekin almashtirish, qo'shish yoki olib tashlash mumkin emas. JavaScriptda buning eng yaqin o'xshashi — `Object.freeze()` qilingan massiv, lekin Pythonda bu tayyor, alohida tur sifatida mavjud.

```python
('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya')  # ismlar — tuple
```

#### Set (to'plam)

Aslida JavaScriptda ham `Set` mavjud — agar siz u bilan ishlagan bo'lsangiz, bu tushuncha tanish bo'ladi! Set — list va tuple'ga o'xshash, lekin tartiblanmagan va **faqat takrorlanmaydigan (unique) elementlarni** saqlaydi — xuddi matematikadagi to'plam kabi.

```python
{2, 4, 3, 5}
{3.14, 9.81, 2.7}  # tartib muhim emas
```

### Ma'lumot turini tekshirish

Biror ma'lumotning turini bilish uchun **`type()`** funksiyasidan foydalanamiz. JavaScriptda buning o'xshashi — `typeof` operatori (`typeof 10` kabi), faqat Pythonda bu funksiya ko'rinishida chaqiriladi: `type(10)`.

### Python fayli yaratish

`30DaysOfPython` papkasi ichida `helloworld.py` faylini yarating. Python interaktiv shell'da natija avtomatik chiqadi, lekin `.py` faylida natijani ko'rish uchun **`print()`** ichki (built-in) funksiyasidan foydalanishimiz kerak — bu xuddi JavaScriptdagi **`console.log()`** bilan bir xil vazifani bajaradi.

```python
print('argument1', 'argument2', 'argument3')
```

Faylni ishga tushirish uchun VS Code'dagi yashil tugmani bosing yoki terminalda shu buyruqni yozing:

```shell
python3 helloworld.py
```

🌕 Ajoyib! Siz 1-kun challenge'ini tugatdingiz va katta yutuqlar tomon yo'l olyapsiz. Endi miya va mushaklarni mustahkamlash uchun mashqlar bajaring.

## 💻 Mashqlar — 1-kun

### 1-daraja

1. Siz ishlatayotgan Python versiyasini tekshiring (`python3 --version`).
2. Python interaktiv shellni oching va quyidagi amallarni bajaring. Sonlar 3 va 4:
   - qo'shish (+)
   - ayirish (-)
   - ko'paytirish (*)
   - modul / qoldiq (%)
   - bo'lish (/)
   - daraja (**)
   - butun qismli bo'lish (//)
3. Python shellda quyidagi satrlarni yozing:
   - Ismingiz
   - Familiyangiz
   - Davlatingiz
   - "Men 30 kunlik Python challenge'idan zavqlanyapman"
4. Quyidagi ma'lumotlarning turini (`type()` orqali) tekshiring:
   - `10`
   - `9.8`
   - `3.14`
   - `4 - 4j`
   - `['Asabeneh', 'Python', 'Finland']`
   - Ismingiz
   - Familiyangiz
   - Davlatingiz

### 2-daraja

1. `30DaysOfPython` papkasi ichida `day_1` nomli papka yarating. Uning ichida `helloworld.py` faylini yarating va 1, 2, 3, 4-savollarni shu faylda qaytaring. `.py` faylida ishlayotganda natijani ko'rish uchun `print()` dan foydalanishni unutmang. Faylni saqlangan joyga o'tib, ishga tushiring.

### 3-daraja

1. Har xil Python ma'lumot turlariga (Integer, Float, Complex, String, Boolean, List, Tuple, Set, Dictionary) misol yozing.
2. (2, 3) va (10, 8) nuqtalar orasidagi [Yevklid masofasini](https://en.wikipedia.org/wiki/Euclidean_distance) hisoblang.

🎉 TABRIKLAYMIZ! 🎉

➡️ Keyingi qadam: **2-kun — O'zgaruvchilar va ichki funksiyalar** (tarjima jarayonida).

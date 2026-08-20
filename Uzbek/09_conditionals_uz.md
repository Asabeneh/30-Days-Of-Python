<div align="center">
  <h1> 30 kunlik Python: 9-kun — Shartlar (Conditionals)</h1>
</div>

[<< 8-kun](./08_dictionaries_uz.md) | [10-kun >>](./10_loops_uz.md)

- [📘 9-kun](#-9-kun)
  - [If shart](#if-shart)
  - [If Else](#if-else)
  - [If Elif Else](#if-elif-else)
  - [Qisqa yozilish (Short Hand)](#qisqa-yozilish-short-hand)
  - [Ichma-ich shartlar](#ichma-ich-shartlar)
  - [Shart va mantiqiy operatorlar](#shart-va-mantiqiy-operatorlar)
  - [💻 Mashqlar — 9-kun](#-mashqlar--9-kun)

# 📘 9-kun

## Shartlar (Conditionals)

Bu mavzu sizga **eng tanish bo'lishi kerak** — JavaScriptda `if`, `else if`, `else` bilan qancha ishlagansiz! Yaxshi xabar: **mantiq xuddi bir xil**, faqat yozilish tarzi (sintaksis) farq qiladi.

```javascript
// JavaScript
if (a > 0) {
  console.log('A musbat son');
} else if (a < 0) {
  console.log('A manfiy son');
} else {
  console.log('A nolga teng');
}
```

```python
# Python — xuddi shu mantiq
a = 0
if a > 0:
    print('A musbat son')
elif a < 0:
    print('A manfiy son')
else:
    print('A nolga teng')
```

**Asosiy farqlar:**

| | JavaScript | Python |
|---|---|---|
| Blokni belgilash | `{ }` | `:` va indentatsiya (1-kunda ko'rgan edik) |
| "Aks holda agar" | `else if` | `elif` (bitta so'z!) |
| Shartni qavsga olish | majburiy: `if (a > 0)` | shart emas: `if a > 0:` |

### If shart

```python
a = 3
if a > 0:
    print('A musbat son')
# A musbat son
```

### If Else

```python
a = 3
if a < 0:
    print('A manfiy son')
else:
    print('A musbat son')
```

### If Elif Else

Bir nechta shartni tekshirish kerak bo'lganda `elif` ishlatiladi (JS'dagi `else if` o'rnida, lekin bitta so'z sifatida yoziladi):

```python
a = 0
if a > 0:
    print('A musbat son')
elif a < 0:
    print('A manfiy son')
else:
    print('A nolga teng')
```

### Qisqa yozilish (Short Hand)

JavaScriptda **ternary operator** ishlatgansiz: `condition ? 'rost' : 'yolg\'on'`. Pythonda buning o'xshashi bor, lekin **tartibi teskari** — avval natija, keyin shart:

```javascript
// JavaScript
console.log(a > 0 ? 'A musbat' : 'A manfiy');
```

```python
# Python — natija va shart joyini almashtiradi!
a = 3
print('A musbat') if a > 0 else print('A manfiy')
```

> 🟡 Diqqat: Python'da `?` va `:` belgilari yo'q. O'rniga `condition_natija if shart else boshqa_natija` tartibida yoziladi — "natija, agar shart bo'lsa, aks holda boshqa natija" deb o'qing.

### Ichma-ich shartlar

JS'dagi kabi, `if` ichida yana `if` yozish mumkin:

```python
a = 0
if a > 0:
    if a % 2 == 0:
        print('A musbat va juft son')
    else:
        print('A musbat son')
elif a == 0:
    print('A nolga teng')
else:
    print('A manfiy son')
```

Ichma-ich shartni `and` operatori orqali qisqartirish mumkin (3-kunda ko'rgan edik: JS'dagi `&&`):

### Shart va mantiqiy operatorlar

```python
a = 0
if a > 0 and a % 2 == 0:
    print('A musbat va juft son')
elif a > 0 and a % 2 != 0:
    print('A musbat son')
elif a == 0:
    print('A nolga teng')
else:
    print('A manfiy son')
```

`or` operatori (JS'dagi `||`):

```python
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Kirish ruxsat etildi!')
else:
    print('Kirish rad etildi!')
```

🌕 Zo'r ketyapsiz! Katta narsalar vaqt talab qiladi, hech qachon taslim bo'lmang. 9-kun challenge'ini tugatdingiz. Endi mashqlarni bajaring.

## 💻 Mashqlar — 9-kun

### 1-daraja

1. `input("Yoshingizni kiriting: ")` orqali foydalanuvchidan yosh so'rang. Agar 18 yoshdan katta bo'lsa: "Siz haydovchilik guvohnomasi olish uchun yetarli yoshdasiz" deb chiqaring. Aks holda, necha yil kutishi kerakligini ayting:

    ```sh
    Yoshingizni kiriting: 30
    Siz haydovchilik guvohnomasi olish uchun yetarli yoshdasiz.

    Yoshingizni kiriting: 15
    Sizga yana 3 yil kerak.
    ```

2. `my_age` va `your_age`ni `if...else` orqali solishtiring — kim kattaroq (men yoki siz)? Ikkalasini ham `input()` orqali so'rang. 1 yillik farq uchun "yil", undan ko'p farq uchun "yillar" so'zini ishlatib, ichma-ich shart yozing; agar tengbo'lsa alohida xabar chiqaring.

    ```sh
    Yoshingizni kiriting: 30
    Siz mendan 5 yosh kattasiz.
    ```

3. Foydalanuvchidan ikki son so'rang. Agar `a` dan `b` katta bo'lsa — "a, b dan katta" deb, kichik bo'lsa — "a, b dan kichik" deb, teng bo'lsa — "a, b ga teng" deb chiqaring:

```sh
Birinchi sonni kiriting: 4
Ikkinchi sonni kiriting: 3
4, 3 dan katta
```

### 2-daraja

1. Talabalarga ballariga qarab baho qo'yadigan kod yozing:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

2. Foydalanuvchidan oyni so'rab, fasl Kuz, Qish, Bahor yoki Yozligini aniqlang:
   - Sentyabr, Oktyabr, Noyabr — Kuz
   - Dekabr, Yanvar, Fevral — Qish
   - Mart, Aprel, May — Bahor
   - Iyun, Iyul, Avgust — Yoz

3. Quyidagi mevalar ro'yxati berilgan:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

   Agar meva ro'yxatda bo'lmasa, ro'yxatga qo'shing va yangi ro'yxatni chiqaring. Agar mavjud bo'lsa, `'Bu meva ro\'yxatda allaqachon bor'` deb chiqaring.

### 3-daraja

1. Quyida `person` dictionary berilgan (xohlasangiz o'zgartiring):

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
```

   - `person` dictionary'da `skills` kaliti bor-yo'qligini tekshirib, bor bo'lsa `skills` ro'yxatining o'rtadagi elementini chiqaring.
   - `skills` kaliti bor-yo'qligini tekshirib, bor bo'lsa, ichida `'Python'` bor-yo'qligini tekshirib natijani chiqaring.
   - Agar `skills`da faqat `JavaScript` va `React` bo'lsa — `'U frontend dasturchi'`, agar `Node`, `Python`, `MongoDB` bo'lsa — `'U backend dasturchi'`, agar `React`, `Node`, `MongoDB` bo'lsa — `'U fullstack dasturchi'`, aks holda `'noma\'lum kasb'` deb chiqaring (aniqroq natija uchun ichma-ich shartlardan foydalaning).
   - Agar shaxs turmush qurgan bo'lsa va Finlandiyada yashasa, quyidagi formatda chiqaring:

```py
    Asabeneh Yetayeh Finlandiyada yashaydi. U turmush qurgan.
```

🎉 TABRIKLAYMIZ! 🎉

[<< 8-kun](./08_dictionaries_uz.md) | [10-kun >>](./10_loops_uz.md)

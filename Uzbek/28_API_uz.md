<div align="center">
  <h1> 30 kunlik Python: 28-kun — API va HTTP</h1>
</div>

[<< 27-kun](./27_python_with_mongodb_uz.md) | [29-kun >>](./29_building_API_uz.md)

- [📘 28-kun](#-28-kun)
  - [API nima](#api-nima)
  - [HTTP nima](#http-nima)
  - [HTTP so'rov tuzilmasi](#http-so-rov-tuzilmasi)
  - [HTTP metodlari (CRUD)](#http-metodlari-crud)
  - [Status kodlari](#status-kodlari)
  - [💻 Mashqlar — 28-kun](#-mashqlar--28-kun)

# 📘 28-kun

## API nima

**API** (Application Programming Interface — Dasturiy ta'minot interfeysi) — dasturlar o'rtasida ma'lumot almashish uchun kelishilgan "shartnoma". Veb-API'lar tarmoq orqali (HTTP protokoli) ishlaydi.

> 🟡 **JS bilan taqqoslash:** Siz JavaScript'da `fetch('https://api.example.com/data')` yozib, API'dan ma'lumot olgansiz. Xuddi shu ish Python'da `requests.get('https://api.example.com/data')` bilan bajariladi. API — bu tashqi tizimning "qo'ng'iroq raqami" desa ham bo'ladi: to'g'ri raqamni terganingizda, to'g'ri javob olasiz.

Veb-API misollari:
- Mamlakatlar API: `https://restcountries.eu/rest/v2/all`
- Mushuklar zotlari: `https://api.thecatapi.com/v1/breeds`

**RESTful API** — HTTP metodlaridan foydalanib CRUD (yaratish, o'qish, yangilash, o'chirish) amallarini bajaruvchi API turi. Bugungi kunda eng keng tarqalgan API standarti.

## HTTP nima

**HTTP** (Hypertext Transfer Protocol — Gipermatn uzatish protokoli) — brauzer (mijoz) va server o'rtasidagi muloqot qoidalari to'plami.

**So'rov-javob sikli:**

```
Brauzer ---[GET /api/students]--> Server
Brauzer <--[200 OK + JSON ma'lumot]-- Server
```

> 🟡 Siz brauzerda `fetch()` yozganingizda, huddi shu jarayon yuz beradi: brauzer serverga so'rov yuboradi, server javob qaytaradi. Python'da ham bir xil mexanizm — faqat brauzer o'rnida Python kod bor.

## HTTP so'rov tuzilmasi

Har bir HTTP xabari (so'rov va javob) bir xil tuzilmaga ega:

```
1. Birinchi qator (boshlang'ich qator)
2. Sarlavhalar (Headers) — nol yoki ko'proq qator
3. Bo'sh qator
4. Xabar tanasi (Body) — ixtiyoriy
```

**So'rov misoli:**

```
GET /api/v1/talabalar HTTP/1.1
Host: localhost:5000
Accept: application/json
```

**Javob misoli:**

```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 245

[{"ism": "Ali", "yosh": 25}, ...]
```

### Sarlavhalar (Headers)

Sarlavhalar so'rov yoki javob haqida qo'shimcha ma'lumot beradi:

- `Content-Type: application/json` — xabar tanasi JSON formatida
- `Content-Length: 245` — tananing bayt soni
- `Authorization: Bearer token123` — autentifikatsiya tokeni

## HTTP metodlari (CRUD)

| HTTP metodi | CRUD amali | Maqsad | Misol |
|-------------|------------|--------|-------|
| **GET** | O'qish (Read) | Ma'lumot olish | `GET /talabalar` |
| **POST** | Yaratish (Create) | Yangi ma'lumot qo'shish | `POST /talabalar` |
| **PUT** | Yangilash (Update) | Mavjud ma'lumotni o'zgartirish | `PUT /talabalar/123` |
| **DELETE** | O'chirish (Delete) | Ma'lumotni o'chirish | `DELETE /talabalar/123` |

> 🟡 Bu metodlar `fetch()` da ham xuddi shunday ishlatiladi:
> ```javascript
> // JS'da GET
> fetch('/api/talabalar')
>
> // JS'da POST
> fetch('/api/talabalar', {
>   method: 'POST',
>   body: JSON.stringify({ism: 'Ali'})
> })
> ```
>
> Python'da `requests` kutubxonasi bilan:
> ```python
> import requests
>
> # GET
> r = requests.get('http://localhost:5000/api/talabalar')
>
> # POST
> r = requests.post('http://localhost:5000/api/talabalar',
>                   json={'ism': 'Ali'})
> ```

## Status kodlari

Server javobining birinchi qatoridagi raqam — **status kod** — so'rov natijasini bildiradi:

| Kod | Ma'no | Qachon ishlatiladi |
|-----|-------|-------------------|
| **200** OK | Muvaffaqiyatli | GET so'rovi bajarildi |
| **201** Created | Yaratildi | POST bilan yangi resurs yaratildi |
| **400** Bad Request | Noto'g'ri so'rov | Foydalanuvchi xato ma'lumot yubordi |
| **401** Unauthorized | Ruxsat yo'q | Token kerak, lekin berilmagan |
| **404** Not Found | Topilmadi | So'ralgan resurs mavjud emas |
| **500** Server Error | Server xatosi | Serverdagi kod xatosi |

> 🟡 Siz JavaScript'da `fetch()` dan keyin `.then(r => r.status)` bilan bu kodlarni tekshirgansiz. 19-kunda `requests.get(url).status_code` orqali ham ko'rgan edik.

**API so'rov manzili (endpoint) tuzilmasi:**

```
https://api.kompaniya.com/v1/resurslar
          |              |  |
          domen          |  resurs nomi
                     versiya
```

Misol: `https://api.twitter.com/1.1/lists/members.json`

**API sinov vositalari:**

Brauzer faqat GET so'rovlarini qo'llab-quvvatlaydi. POST, PUT, DELETE so'rovlarni sinovdan o'tkazish uchun maxsus vositalar kerak:

- **Postman** — grafik interfeysi bor, eng mashhuri
- **Insomnia** — Postman'ga alternativa
- **curl** — terminal orqali (Linux/Mac'da o'rnatilgan)

```sh
# curl bilan GET
curl http://localhost:5000/api/v1/talabalar

# curl bilan POST
curl -X POST http://localhost:5000/api/v1/talabalar \
  -H "Content-Type: application/json" \
  -d '{"ism": "Ali", "yosh": 25}'
```

🌕 API dunyosini tushunarli qildingiz! Ertaga siz o'zingizning API'ingizni qurasiz. 28-kun challenge'ini yakunladingiz.

## 💻 Mashqlar — 28-kun

1. API va HTTP haqida yuqoridagi materiallarni o'qib chiqing.
2. Brauzeringizda `https://restcountries.eu/rest/v2/all` ga kiring va javobni ko'ring — bu JSON formatidagi API javobi.
3. Postman yoki Insomnia'ni yuklab o'rnating.

🎉 TABRIKLAYMIZ! 🎉

[<< 27-kun](./27_python_with_mongodb_uz.md) | [29-kun >>](./29_building_API_uz.md)

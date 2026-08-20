<div align="center">
  <h1> 30 kunlik Python: 27-kun — Python va MongoDB</h1>
</div>

[<< 26-kun](./26_python_web_uz.md) | [28-kun >>](./28_API_uz.md)

- [📘 27-kun](#-27-kun)
  - [MongoDB nima](#mongodb-nima)
  - [SQL va NoSQL farqi](#sql-va-nosql-farqi)
  - [MongoDB Atlas — bulutli baza](#mongodb-atlas--bulutli-baza)
  - [Flask'ni MongoDB'ga ulash](#flaskni-mongodbga-ulash)
  - [Ma'lumot qo'shish](#ma-lumot-qo-shish)
  - [Ma'lumot o'qish — find()](#ma-lumot-o-qish--find)
  - [Shartli so'rov](#shartli-so-rov)
  - [Saralash va cheklash](#saralash-va-cheklash)
  - [Ma'lumot yangilash — update()](#ma-lumot-yangilash--update)
  - [Ma'lumot o'chirish — delete()](#ma-lumot-o-chirish--delete)
  - [💻 Mashqlar — 27-kun](#-mashqlar--27-kun)

# 📘 27-kun

## MongoDB nima

**MongoDB** — NoSQL ma'lumotlar bazasi. Ma'lumotlarni **JSON-ga o'xshash hujjat (document)** ko'rinishida saqlaydi — jadval va qatorlar (SQL) o'rniga.

> 🟡 **JS bilan taqqoslash:** MongoDB hujjati — JS'dagi oddiy `{}` obyektiga o'xshaydi. Siz allaqachon bunday tuzilmani bilasiz! Farqi — bu obyektlar diskda saqlanadi va milliardlab bo'lishi mumkin.

## SQL va NoSQL farqi

| SQL (MySQL, PostgreSQL) | NoSQL (MongoDB) |
|------------------------|-----------------|
| Jadval (Table) | Kolleksiya (Collection) |
| Qator (Row) | Hujjat (Document) |
| Ustun (Column) | Maydon (Field) |
| Schema majburiy | Schema ixtiyoriy |
| `SELECT * FROM ...` | `find({})` |
| `INSERT INTO ...` | `insert_one({})` |
| `UPDATE ... SET ...` | `update_one({}, {$set:{}})` |
| `DELETE FROM ...` | `delete_one({})` |

## MongoDB Atlas — bulutli baza

MongoDB'ni bulutda bepul ishlatish uchun [mongodb.com](https://www.mongodb.com/) saytida ro'yxatdan o'ting, cluster yarating va connection string oling:

```
mongodb+srv://foydalanuvchi:parol@cluster.mongodb.net/test?retryWrites=true&w=majority
```

**PyMongo o'rnatish:**

```sh
pip install pymongo dnspython
```

> `dnspython` — MongoDB'ning `+srv://` URL formatini tushunish uchun kerak.

## Flask'ni MongoDB'ga ulash

```python
from flask import Flask
import pymongo
import os

MONGODB_URI = 'mongodb+srv://foydalanuvchi:parol@cluster.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

# Mavjud bazalarni ko'rish
print(client.list_database_names())   # ['admin', 'local']

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## Ma'lumot qo'shish

### Baza va kolleksiya yaratish

MongoDB'da baza va kolleksiya — ularga birinchi marta yozilganda avtomatik yaratiladi:

```python
# Baza va kolleksiyaga murojaat
db = client['otuz_kun_python']          # baza nomi
# yoki: db = client.otuz_kun_python

# insert_one() — bitta hujjat qo'shish
db.talabalar.insert_one({
    'ism': 'Ali',
    'mamlakat': 'Uzbekistan',
    'shahar': 'Toshkent',
    'yosh': 25
})
print(client.list_database_names())   # endi 'otuz_kun_python' ham bor
```

### Ko'p hujjat qo'shish

```python
talabalar = [
    {'ism': 'Behruz', 'mamlakat': 'Uzbekistan', 'shahar': 'Samarqand', 'yosh': 22},
    {'ism': 'Malika', 'mamlakat': 'Uzbekistan', 'shahar': 'Buxoro', 'yosh': 28},
    {'ism': 'Jasur',  'mamlakat': 'Uzbekistan', 'shahar': 'Namangan', 'yosh': 30},
]
for talaba in talabalar:
    db.talabalar.insert_one(talaba)

# yoki bir qatorda:
# db.talabalar.insert_many(talabalar)
```

## Ma'lumot o'qish — find()

### find_one() — birinchi mos yozuvni topish

```python
talaba = db.talabalar.find_one()   # birinchi hujjatni qaytaradi
print(talaba)
# {'_id': ObjectId('...'), 'ism': 'Ali', 'mamlakat': 'Uzbekistan', ...}
```

> 🟡 Har bir MongoDB hujjatida `_id` maydoni avtomatik qo'shiladi — bu noyob identifikator (JS'da `id` ni o'zingiz belgilashingiz kerak edi).

### find() — barcha mos yozuvlar

```python
barcha = db.talabalar.find()     # kursor (cursor) qaytaradi
for talaba in barcha:
    print(talaba)
```

### Faqat kerakli maydonlarni ko'rsatish

```python
# 0 = ko'rsatma, 1 = ko'rsat
talabalar = db.talabalar.find({}, {"_id": 0, "ism": 1, "mamlakat": 1})
for t in talabalar:
    print(t)
# {'ism': 'Ali', 'mamlakat': 'Uzbekistan'}
# ...
```

## Shartli so'rov

```python
# Faqat Uzbekistanliklar
query = {"mamlakat": "Uzbekistan"}
talabalar = db.talabalar.find(query)

# Yoshi 25 dan katta
query = {"yosh": {"$gt": 25}}   # $gt = greater than (katta)
# $lt = less than (kichik), $gte = >=, $lte = <=, $eq = ==, $ne = !=

# Bir necha shart
query = {"mamlakat": "Uzbekistan", "shahar": "Toshkent"}
```

> 🟡 MongoDB operatorlari (`$gt`, `$lt`, `$eq`) — SQL'dagi `WHERE yosh > 25` ga o'xshaydi. `$` belgisi MongoDB operator ekanligini bildiradi.

## Saralash va cheklash

```python
# Ism bo'yicha o'sish tartibida (1 = o'sish, -1 = kamayish)
talabalar = db.talabalar.find().sort('ism')
talabalar_teskari = db.talabalar.find().sort('ism', -1)

# Yosh bo'yicha
yoshlar_tartibida = db.talabalar.find().sort('yosh')

# Faqat 3 ta natija
db.talabalar.find().limit(3)
```

> 🟡 `.sort().limit()` — JS'da `data.sort().slice(0, 3)` ga o'xshaydi, lekin bu amallar baza ichida (serverda) bajariladi — samaraliroq.

## Ma'lumot yangilash — update()

```python
# update_one() — bitta hujjatni yangilash
# Birinchi argument: qaysi hujjatni topish
# Ikkinchi argument: nima o'zgartirish ($set operatori bilan)
query = {"ism": "Ali"}
yangi_qiymat = {"$set": {"yosh": 26}}
db.talabalar.update_one(query, yangi_qiymat)

# Natijani tekshirish
for t in db.talabalar.find():
    print(t)

# Ko'p hujjatni yangilash
# db.talabalar.update_many({"mamlakat": "Uzbekistan"}, {"$set": {"til": "uzbek"}})
```

> 🟡 `$set` — faqat ko'rsatilgan maydonlarni o'zgartiradi, boshqalarini saqlab qoladi. `$set` siz ishlatsangiz, hujjatning barchasi almashtirilib ketishi mumkin.

## Ma'lumot o'chirish — delete()

```python
# Bitta hujjatni o'chirish
query = {"ism": "Jasur"}
db.talabalar.delete_one(query)

# Ko'p hujjatni o'chirish
# db.talabalar.delete_many({"mamlakat": "UK"})

# Barcha hujjatlarni o'chirish
# db.talabalar.delete_many({})

# Butun kolleksiyani o'chirish
# db.talabalar.drop()
```

**CRUD amallar xulosa jadvali:**

| Amal | MongoDB metodi | SQL ekvivalenti |
|------|----------------|-----------------|
| Yaratish | `insert_one({})` | `INSERT INTO` |
| O'qish | `find({})` | `SELECT` |
| Yangilash | `update_one({}, {$set:{}})` | `UPDATE SET` |
| O'chirish | `delete_one({})` | `DELETE WHERE` |

🌕 Endi siz ma'lumotlar bazasi bilan ishlashni bilasiz! Maqsadga 3 kun qoldi. 27-kun challenge'ini tugatdingiz.

## 💻 Mashqlar — 27-kun

1. MongoDB Atlas'da bepul cluster oching va Python orqali ulaning.
2. `talabalar` kolleksiyasi yarating — 5 ta hujjat qo'shing.
3. `find()`, `update_one()`, `delete_one()` metodlarini sinab ko'ring.

🎉 TABRIKLAYMIZ! 🎉

[<< 26-kun](./26_python_web_uz.md) | [28-kun >>](./28_API_uz.md)

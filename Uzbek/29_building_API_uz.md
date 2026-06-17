<div align="center">
  <h1> 30 kunlik Python: 29-kun — RESTful API Yaratish</h1>
</div>

[<< 28-kun](./28_API_uz.md) | [30-kun >>](./30_conclusions_uz.md)

- [📘 29-kun](#-29-kun)
  - [API tuzilmasi](#api-tuzilmasi)
  - [GET — ma'lumot olish](#get--ma-lumot-olish)
  - [GET — bitta hujjatni ID bo'yicha olish](#get--bitta-hujjatni-id-bo-yicha-olish)
  - [POST — yangi ma'lumot yaratish](#post--yangi-ma-lumot-yaratish)
  - [PUT — ma'lumotni yangilash](#put--ma-lumotni-yangilash)
  - [DELETE — ma'lumotni o'chirish](#delete--ma-lumotni-o-chirish)
  - [To'liq app.py](#to-liq-apppy)
  - [💻 Mashqlar — 29-kun](#-mashqlar--29-kun)

# 📘 29-kun

## API tuzilmasi

28-kunda HTTP va API nazariyasini o'rgandik. Bugun Flask + MongoDB yordamida haqiqiy **RESTful API** quramiz.

API endpoint'lari (manzillar) quyidagicha bo'ladi:

```
GET    /api/v1.0/talabalar          — barcha talabalar ro'yxati
GET    /api/v1.0/talabalar/<id>     — bitta talaba (ID bo'yicha)
POST   /api/v1.0/talabalar          — yangi talaba qo'shish
PUT    /api/v1.0/talabalar/<id>     — talabani yangilash
DELETE /api/v1.0/talabalar/<id>     — talabani o'chirish
```

> 🟡 Bu tuzilma — REST arxitekturasining standart shakli. JS'da Express.js bilan bir xil: `app.get('/api/users', ...)`, `app.post('/api/users', ...)`.

**Kerakli paketlar:**

```sh
pip install Flask pymongo dnspython
```

## GET — ma'lumot olish

Avval sinov ma'lumotlari (dummy data) bilan boshlaylik:

```python
from flask import Flask, Response
import json
import os

app = Flask(__name__)

@app.route('/api/v1.0/talabalar', methods=['GET'])
def talabalar():
    talabalar_royxati = [
        {
            'ism': 'Ali',
            'mamlakat': 'Uzbekistan',
            'shahar': 'Toshkent',
            'ko\'nikmalar': ['HTML', 'CSS', 'JavaScript', 'Python']
        },
        {
            'ism': 'Malika',
            'mamlakat': 'Uzbekistan',
            'shahar': 'Samarqand',
            'ko\'nikmalar': ['Python', 'MongoDB']
        },
        {
            'ism': 'Behruz',
            'mamlakat': 'Uzbekistan',
            'shahar': 'Buxoro',
            'ko\'nikmalar': ['Java', 'C#']
        }
    ]
    return Response(json.dumps(talabalar_royxati, ensure_ascii=False),
                    mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

> 🟡 `Response(json.dumps(...), mimetype='application/json')` — Express'dagi `res.json(data)` ga o'xshaydi. `ensure_ascii=False` — o'zbek harflari to'g'ri chiqishi uchun.

Ishga tushirib, brauzerda `http://localhost:5000/api/v1.0/talabalar` ga kiring — JSON javob ko'rasiz.

## GET — bitta hujjatni ID bo'yicha olish

```python
from flask import Flask, Response
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
import json
import os

app = Flask(__name__)

MONGODB_URI = 'mongodb+srv://foydalanuvchi:parol@cluster.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['otuz_kun_python']

@app.route('/api/v1.0/talabalar', methods=['GET'])
def talabalar():
    barcha = list(db.talabalar.find())
    return Response(dumps(barcha), mimetype='application/json')

@app.route('/api/v1.0/talabalar/<id>', methods=['GET'])
def bitta_talaba(id):
    # <id> — URL'dan olinadi, masalan: /api/v1.0/talabalar/5df68a21...
    talaba = db.talabalar.find({'_id': ObjectId(id)})
    return Response(dumps(talaba), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

> 🟡 `<id>` — URL parametri. Flask'da `<o'zgaruvchi_nomi>` bilan belgilanadi, funksiya parametri sifatida qabul qilinadi. Express'da `:id` yoziladi: `app.get('/users/:id', (req, res) => req.params.id)`.
>
> `ObjectId(id)` — string'ni MongoDB ID turига aylantirish. MongoDB ID'si oddiy string emas, maxsus tur.

## POST — yangi ma'lumot yaratish

```python
from flask import Flask, Response, request
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

MONGODB_URI = 'mongodb+srv://foydalanuvchi:parol@cluster.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['otuz_kun_python']

@app.route('/api/v1.0/talabalar', methods=['GET'])
def talabalar():
    barcha = list(db.talabalar.find())
    return Response(dumps(barcha), mimetype='application/json')

@app.route('/api/v1.0/talabalar', methods=['POST'])
def talaba_yaratish():
    # Forma yoki JSON tanasidan ma'lumot olish
    ism = request.form['ism']
    mamlakat = request.form['mamlakat']
    shahar = request.form['shahar']
    konikma = request.form['konikma'].split(', ')   # "Python, Flask" -> ['Python', 'Flask']
    bio = request.form['bio']
    tugilgan_yil = request.form['tugilgan_yil']
    yaratilgan = datetime.now()

    talaba = {
        'ism': ism,
        'mamlakat': mamlakat,
        'shahar': shahar,
        'tugilgan_yil': tugilgan_yil,
        'konikma': konikma,
        'bio': bio,
        'yaratilgan': str(yaratilgan)
    }
    db.talabalar.insert_one(talaba)
    return Response(dumps({'xabar': 'Talaba muvaffaqiyatli qo\'shildi'}),
                    mimetype='application/json', status=201)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

> 🟡 `request.form['ism']` — Express'dagi `req.body.ism` ga o'xshaydi (body-parser bilan). Status `201` — "Created" (yaratildi) ma'nosini bildiradi.

**Postman bilan sinash:**
1. Postman'ni oching
2. Metod: `POST`
3. URL: `http://localhost:5000/api/v1.0/talabalar`
4. Body → form-data → `ism`, `mamlakat`, `shahar` va boshqa maydonlarni kiriting
5. `Send` tugmasini bosing

## PUT — ma'lumotni yangilash

```python
@app.route('/api/v1.0/talabalar/<id>', methods=['PUT'])
def talabani_yangilash(id):
    query = {"_id": ObjectId(id)}

    yangi_ma_lumot = {
        'ism': request.form['ism'],
        'mamlakat': request.form['mamlakat'],
        'shahar': request.form['shahar'],
        'konikma': request.form['konikma'].split(', '),
        'bio': request.form['bio'],
        'tugilgan_yil': request.form['tugilgan_yil'],
        'yangilangan': str(datetime.now())
    }

    db.talabalar.update_one(query, {"$set": yangi_ma_lumot})
    return Response(dumps({'xabar': 'Talaba yangilandi'}),
                    mimetype='application/json')
```

> 🟡 PUT — to'liq ma'lumotni almashtiradi. PATCH — faqat bir qismini o'zgartiradi. Oddiy loyihalarda PUT yetarli.

## DELETE — ma'lumotni o'chirish

```python
@app.route('/api/v1.0/talabalar/<id>', methods=['DELETE'])
def talabani_ochirish(id):
    db.talabalar.delete_one({"_id": ObjectId(id)})
    return Response(dumps({'xabar': 'Talaba o\'chirildi'}),
                    mimetype='application/json')
```

## To'liq app.py

Barcha CRUD amallarini birlashtirgan to'liq fayl:

```python
from flask import Flask, Response, request
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import json
import os

app = Flask(__name__)

MONGODB_URI = 'mongodb+srv://foydalanuvchi:parol@cluster.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['otuz_kun_python']

# GET — barcha talabalar
@app.route('/api/v1.0/talabalar', methods=['GET'])
def talabalar():
    barcha = list(db.talabalar.find())
    return Response(dumps(barcha), mimetype='application/json')

# GET — bitta talaba
@app.route('/api/v1.0/talabalar/<id>', methods=['GET'])
def bitta_talaba(id):
    talaba = db.talabalar.find({'_id': ObjectId(id)})
    return Response(dumps(talaba), mimetype='application/json')

# POST — yangi talaba yaratish
@app.route('/api/v1.0/talabalar', methods=['POST'])
def talaba_yaratish():
    talaba = {
        'ism': request.form['ism'],
        'mamlakat': request.form['mamlakat'],
        'shahar': request.form['shahar'],
        'konikma': request.form['konikma'].split(', '),
        'bio': request.form['bio'],
        'tugilgan_yil': request.form['tugilgan_yil'],
        'yaratilgan': str(datetime.now())
    }
    db.talabalar.insert_one(talaba)
    return Response(dumps({'xabar': 'Yaratildi'}), mimetype='application/json', status=201)

# PUT — talabani yangilash
@app.route('/api/v1.0/talabalar/<id>', methods=['PUT'])
def talabani_yangilash(id):
    yangi = {
        'ism': request.form['ism'],
        'mamlakat': request.form['mamlakat'],
        'shahar': request.form['shahar'],
        'konikma': request.form['konikma'].split(', '),
        'bio': request.form['bio'],
        'tugilgan_yil': request.form['tugilgan_yil'],
        'yangilangan': str(datetime.now())
    }
    db.talabalar.update_one({"_id": ObjectId(id)}, {"$set": yangi})
    return Response(dumps({'xabar': 'Yangilandi'}), mimetype='application/json')

# DELETE — talabani o'chirish
@app.route('/api/v1.0/talabalar/<id>', methods=['DELETE'])
def talabani_ochirish(id):
    db.talabalar.delete_one({"_id": ObjectId(id)})
    return Response(dumps({'xabar': 'O\'chirildi'}), mimetype='application/json')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

**CRUD amallar va HTTP metodlari xulosa:**

| Amal | HTTP | Flask dekorator | MongoDB |
|------|------|-----------------|---------|
| Yaratish | POST | `methods=['POST']` | `insert_one()` |
| O'qish | GET | `methods=['GET']` | `find()` |
| Yangilash | PUT | `methods=['PUT']` | `update_one()` |
| O'chirish | DELETE | `methods=['DELETE']` | `delete_one()` |

🌕 Siz haqiqiy backend dasturchi bo'ldingiz! Endi o'z API'ingizni qurishingiz mumkin. 29-kun challenge'ini yakunladingiz.

## 💻 Mashqlar — 29-kun

1. Yuqoridagi to'liq `app.py`ni ishga tushiring.
2. Postman yordamida barcha 5 ta endpoint'ni sinab ko'ring: GET (hammasi), GET (bitta), POST, PUT, DELETE.
3. Ilovani Heroku'ga joylashtiring (26-kunda ko'rgan deployment qadamlari bilan).

🎉 TABRIKLAYMIZ! 🎉

[<< 28-kun](./28_API_uz.md) | [30-kun >>](./30_conclusions_uz.md)

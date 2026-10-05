<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 29 — API بنانا</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../29_Day_Building_API/29_building_API.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 28](./28_API.md) | [فہرست](./readme.md) | [اگلا دن: 30](./30_conclusions.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

  - [دن 29](#day-29-section-1)
  - [API بنانا](#day-29-section-2)
    - [API کی ساخت](#day-29-section-3)
    - [GET سے ڈیٹا حاصل کرنا](#day-29-section-4)
    - [شناخت سے ایک document حاصل کرنا](#day-29-section-5)
    - [POST سے ڈیٹا بنانا](#day-29-section-6)
    - [PUT سے تبدیلی](#day-29-section-7)
    - [DELETE سے document حذف کرنا](#day-29-section-8)
  - [💻 مشقیں — دن 29](#day-29-section-9)

<a id="day-29-section-1"></a>

## دن 29

<a id="day-29-section-2"></a>

## API بنانا

اس حصے میں RESTful API بنائیں گے جو HTTP کے GET، PUT، POST اور DELETE طریقوں سے ڈیٹا پڑھ، بدل، بنا اور حذف کر سکے۔

پائتھن، Flask اور MongoDB کے پچھلے اسباق کو ملا کر CRUD ایپلی کیشن تیار کریں گے۔ API سے ڈیٹابیس کے وسائل پر یہ چاروں کام ہوں گے۔

براؤزر کے address bar سے عام طور پر GET بھیجتے ہیں۔ دوسری اقسام کی درخواستیں آسانی سے آزمانے کے لیے API tool استعمال کریں۔ براؤزر خود بھی فارم یا JavaScript کے ذریعے دوسرے طریقے بھیج سکتا ہے۔

API کی مثالیں:

- [ممالک کی API](https://restcountries.eu/rest/v2/all)
- [بلیوں کی نسلوں کی API](https://api.thecatapi.com/v1/breeds)

[Postman](https://www.getpostman.com/) API کی تیاری اور جانچ کا معروف اوزار ہے۔ اسے [ڈاؤن لوڈ](https://www.getpostman.com/) کر سکتے ہیں؛ [Insomnia](https://insomnia.rest/download) ایک متبادل ہے۔

![Postman](../images/postman.png)

<a id="day-29-section-3"></a>

### API کی ساخت

Endpoint ایسا URL ہے جس کے ذریعے وسیلہ حاصل، بنایا، بدلا یا حذف کیا جاتا ہے۔ اصل مثال `https://api.twitter.com/1.1/lists/members.json` کسی فہرست کے ارکان دیتی تھی۔ نجی فہرست کے لیے مناسب تصدیق اور اختیار درکار تھا۔ URL میں خدمت کا نام، API ورژن اور مطلوبہ وسیلے کا path نظر آتا ہے۔

وسائل پر کام کرنے کے HTTP طریقے:

<div dir="ltr">

```sh
GET        Used for object retrieval
POST       Used for object creation and object actions
PUT        Used for object update
DELETE     Used for object deletion
```

</div>

30DaysOfPython کے طلبہ کی API بنائیں۔ نام، ملک، شہر، تاریخِ پیدائش، مہارتیں اور تعارف محفوظ کریں۔ اوزار:

- Postman
- Python
- Flask
- MongoDB

<a id="day-29-section-4"></a>

### GET سے ڈیٹا حاصل کرنا

پہلے فرضی ڈیٹا JSON کی صورت میں واپس کریں۔ `json` اور Flask کا `Response` استعمال ہو گا۔

<div dir="ltr">

```py
# let's import the flask

from flask import Flask,  Response
import json
import os

app = Flask(__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

براؤزر میں `http://localhost:5000/api/v1.0/students` کھولنے پر:

![براؤزر میں GET](../images/get_on_browser.png)

اسی URL کو Postman میں GET کرنے پر:

![Postman میں GET](../images/get_on_postman.png)

اب فرضی ڈیٹا کے بجائے Flask کو MongoDB سے جوڑیں۔

<div dir="ltr">

```py
# let's import the flask

from flask import Flask,  Response
import json
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

`thirty_days_of_python` کی `students` collection سے ڈیٹا حاصل ہو سکتا ہے۔

<div dir="ltr">

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 38
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8c"
        },
        "name": "David",
        "country": "UK",
        "city": "London",
        "age": 34
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8e"
        },
        "name": "Sami",
        "country": "Finland",
        "city": "Helsinki",
        "age": 25
    }
]
```

</div>

<a id="day-29-section-5"></a>

### شناخت سے ایک document حاصل کرنا

شناخت سے ایک document مانگیں۔ Asabeneh کی مثال:

`http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b`

<div dir="ltr">

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 38
    }
]
```

</div>

<a id="day-29-section-6"></a>

### POST سے ڈیٹا بنانا

نئے ڈیٹا کے لیے POST درخواست استعمال کریں۔

<div dir="ltr">

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return ;
def update_student (id):
if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<a id="day-29-section-7"></a>

### PUT سے تبدیلی

<div dir="ltr">

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # this decorator create the home route
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
def update_student (id):
if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<a id="day-29-section-8"></a>

### DELETE سے document حذف کرنا

<div dir="ltr">

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # this decorator create the home route
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # this decorator create the home route
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return ;
@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":ObjectId(id)})
    return
if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<a id="day-29-section-9"></a>

## 💻 مشقیں — دن 29

1. اوپر کی مثال نافذ کریں اور [اصل نمونے](https://thirtydayofpython-api.herokuapp.com/) جیسی API بنائیں۔ یہ پرانا hosted نمونہ ہے؛ اس کی دستیابی مختلف ہو سکتی ہے۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 28](./28_API.md) | [فہرست](./readme.md) | [اگلا دن: 30](./30_conclusions.md)

</div>

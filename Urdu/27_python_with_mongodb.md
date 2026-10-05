<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 27 — MongoDB کے ساتھ پائتھن</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../27_Day_Python_with_mongodb/27_python_with_mongodb.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 26](./26_python_web.md) | [فہرست](./readme.md) | [اگلا دن: 28](./28_API.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 27](#day-27-section-1)
- [MongoDB کے ساتھ پائتھن](#day-27-section-2)
  - [MongoDB](#day-27-section-3)
    - [SQL اور NoSQL کا موازنہ](#day-27-section-4)
    - [کنکشن سٹرنگ: MongoDB URI](#day-27-section-5)
    - [Flask کو MongoDB cluster سے جوڑنا](#day-27-section-6)
    - [ڈیٹابیس اور collection بنانا](#day-27-section-7)
    - [کئی documents شامل کرنا](#day-27-section-8)
    - [MongoDB میں تلاش](#day-27-section-9)
    - [شرط کے ساتھ تلاش](#day-27-section-10)
    - [آپریٹر کے ساتھ مزید تلاش](#day-27-section-11)
    - [نتائج کی تعداد محدود کرنا](#day-27-section-12)
    - [نتائج ترتیب دینا](#day-27-section-13)
    - [شرط کے مطابق تبدیلی](#day-27-section-14)
    - [document حذف کرنا](#day-27-section-15)
    - [collection حذف کرنا](#day-27-section-16)
  - [💻 مشقیں — دن 27](#day-27-section-17)

<a id="day-27-section-1"></a>

# 📘 دن 27

<a id="day-27-section-2"></a>

# MongoDB کے ساتھ پائتھن

پائتھن کو بیک اینڈ پر SQL اور NoSQL دونوں طرح کے ڈیٹابیسز سے جوڑا جا سکتا ہے۔ اس حصے میں NoSQL ڈیٹابیس MongoDB کے ساتھ رابطہ بنائیں گے۔

<a id="day-27-section-3"></a>

## MongoDB

MongoDB ڈیٹا کو JSON جیسے documents میں محفوظ کرتا ہے، جس سے مختلف ساختوں کے ڈیٹا کے ساتھ کام کرنا آسان ہوتا ہے۔ SQL اور NoSQL کی اصطلاحات کا فرق جدول میں دیکھیں۔

<a id="day-27-section-4"></a>

### SQL اور NoSQL کا موازنہ

![SQL اور NoSQL](../images/mongoDB/sql-vs-nosql.png)

[MongoDB](https://www.mongodb.com/) پر sign in اور پھر register سے اکاؤنٹ بنائیں۔ یہاں اسکرین شاٹس اصل کورس کے ہیں؛ موجودہ انٹرفیس مختلف ہو سکتا ہے۔

![MongoDB میں رجسٹریشن](../images/mongoDB/mongodb-signup-page.png)

خانے پُر کر کے آگے بڑھیں۔

![رجسٹریشن فارم](../images/mongoDB/mongodb-register.png)

اصل مثال مفت منصوبہ منتخب کرتی ہے۔

![منصوبے کا انتخاب](../images/mongoDB/mongodb-free.png)

قریب کا دستیاب خطہ منتخب کریں اور cluster کا نام رکھیں۔

![cluster کا نام](../images/mongoDB/mongodb-cluster-name.png)

اس کے بعد sandbox بن جاتا ہے۔

![MongoDB sandbox](../images/mongoDB/mongodb-sandbox.png)

اپنی مشین کے IP پتے کو رسائی دیں۔

![IP رسائی کی ترتیب](../images/mongoDB/mongodb-allow-ip-access.png)

صارف اور پاس ورڈ بنائیں۔

![ڈیٹابیس صارف شامل کرنا](../images/mongoDB/mongodb-add-user.png)

MongoDB URI بنائیں۔

![رابطے کی URI بنانا](../images/mongoDB/mongodb-create-uri.png)

اصل مثال میں Python 3.6 یا بعد کا driver منتخب کیا گیا ہے۔

![پائتھن driver](../images/mongoDB/mongodb-python-driver.png)

<a id="day-27-section-5"></a>

### کنکشن سٹرنگ: MongoDB URI

کنکشن سٹرنگ نقل کریں؛ اس کی صورت کچھ ایسی ہو گی:

<div dir="ltr">

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

</div>

یہ URL ایپلی کیشن کو MongoDB سے جوڑتا ہے۔ پاس ورڈ کی جگہ اپنے ڈیٹابیس صارف کا پاس ورڈ دیں۔

**مثال:**

<div dir="ltr">

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

</div>

اصل مثال کا پاس ورڈ `123123` اور ڈیٹابیس نام `thirty_days_python` ہے۔ یہ صرف مثال ہے؛ اپنا مضبوط پاس ورڈ استعمال کریں۔ حقیقی کنکشن سٹرنگ کو عوامی repository میں نہ رکھیں؛ اسے ماحول کے متغیر میں محفوظ رکھیں۔

پائتھن کو MongoDB driver چاہیے۔ منصوبے میں `pymongo` اور `dnspython` انسٹال کریں۔

<div dir="ltr">

```sh
pip install pymongo dnspython
```

</div>

`mongodb+srv://` URI کے لیے DNS معاونت درکار ہے۔ `dnspython` پائتھن کی DNS toolkit ہے جو متعدد record اقسام سنبھالتی ہے۔

<a id="day-27-section-6"></a>

### Flask کو MongoDB cluster سے جوڑنا

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

</div>

کوڈ چلانے پر اصل مثال میں یہ ڈیٹابیسز ملتے ہیں:

<div dir="ltr">

```sh
['admin', 'local']
```

</div>

<a id="day-27-section-7"></a>

### ڈیٹابیس اور collection بنانا

`thirty_days_of_python` ڈیٹابیس اور `students` collection بنائیں۔ پہلے موجود نہ ہوں تو ڈیٹا داخل کرتے وقت بن جائیں گے۔

<div dir="ltr">

```sh
db = client.name_of_databse # we can create a database like this or the second way
db = client['name_of_database']
```

</div>

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

`insert_one()` سے ایک document شامل کیا گیا۔ اب cluster میں ڈیٹابیس، collection اور اس کا document نظر آنا چاہیے۔

<div dir="ltr">

```sh
['thirty_days_of_python', 'admin', 'local']
```

</div>

اس طرح کا نتیجہ کامیابی کی علامت ہے۔

![ڈیٹابیس اور collection](../images/mongoDB/mongodb-creating_database.png)

Document میں لمبی `_id` بنیادی کلید کا کام کرتی ہے۔ خود `_id` نہ دیں تو MongoDB منفرد شناخت پیدا کرتا ہے۔

<a id="day-27-section-8"></a>

### کئی documents شامل کرنا

`insert_one()` ایک document شامل کرتا ہے۔ کئی کے لیے `insert_many()` یا لوپ استعمال کر سکتے ہیں۔ مثال میں لوپ ہے۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<a id="day-27-section-9"></a>

### MongoDB میں تلاش

PyMongo کے `find()` اور `find_one()`، SQL کے `SELECT` جیسے کام کرتے ہیں۔ پہلے `find_one()` دیکھیں۔

- `find_one()` بغیر شرط پہلا document دیتا ہے۔ مخصوص شناخت کے لیے `find_one({'_id': ObjectId('id')})` جیسی شرط دیں۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
student = db.students.find_one()
print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

</div>

اب David کو اس کی مثال والی شناخت `ObjectId('5df68a23f106fe2d315bbc8c')` سے حاصل کریں۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
from bson.objectid import ObjectId # id object
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

</div>

اب `find()` دیکھیں۔

- شرط نہ ہو تو تمام documents کا cursor دیتا ہے؛ اس پر لوپ چلایا جا سکتا ہے۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

`find({}, {})` کے دوسرے آرگیومنٹ سے واپس آنے والے خانے منتخب کریں۔ `1` شامل اور `0` خارج کرتا ہے۔ عام طور پر دونوں انداز نہیں ملاتے؛ `_id` مستثنیٰ ہے۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

</div>

<a id="day-27-section-10"></a>

### شرط کے ساتھ تلاش

query آبجیکٹ سے مطلوبہ documents منتخب کریں۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

آپریٹرز والی شرط:

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

<a id="day-27-section-11"></a>

### آپریٹر کے ساتھ مزید تلاش

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

مزید شرطیں:

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

</div>

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

<a id="day-27-section-12"></a>

### نتائج کی تعداد محدود کرنا

`limit()` سے واپس آنے والے documents کی تعداد محدود کریں۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
db.students.find().limit(3)
```

</div>

<a id="day-27-section-13"></a>

### نتائج ترتیب دینا

طے شدہ ترتیب بڑھتی ہوتی ہے؛ `-1` سے گھٹتی ترتیب لیں۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
students = db.students.find().sort('name')
for student in students:
    print(student)


students = db.students.find().sort('name',-1)
for student in students:
    print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age',-1)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

بڑھتی ترتیب:

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

گھٹتی ترتیب:

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

</div>

<a id="day-27-section-14"></a>

### شرط کے مطابق تبدیلی

`update_one()` کو تلاش کی شرط اور تبدیلی کا آبجیکٹ دیں۔ Asabeneh کی مثال والی غیر معمولی عمر درست کریں۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

کئی documents بدلنے کے لیے `update_many()` استعمال کریں۔

<a id="day-27-section-15"></a>

### document حذف کرنا

`delete_one()` دی گئی شرط کا پہلا مماثل document حذف کرتا ہے۔ John کا ایک اندراج ہٹائیں۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

</div>

<div dir="ltr">

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

</div>

John کا اندراج ہٹ گیا۔ کئی documents کے لیے `delete_many()` استعمال ہوتا ہے۔ خالی شرط `delete_many({})` collection کے **تمام** documents حذف کرتی ہے۔

<a id="day-27-section-16"></a>

### collection حذف کرنا

`drop()` سے پوری collection حذف ہوتی ہے۔

<div dir="ltr">

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accessing the database
db.students.drop()
```

</div>

اب `students` collection حذف ہو چکی ہے۔

<a id="day-27-section-17"></a>

## 💻 مشقیں — دن 27

اصل سبق اس عنوان کے تحت الگ سوال نہیں دیتا؛ اوپر کی مثالیں سبق کا عملی حصہ ہیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 26](./26_python_web.md) | [فہرست](./readme.md) | [اگلا دن: 28](./28_API.md)

</div>

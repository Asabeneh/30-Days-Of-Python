<div align="center">
  <h1> 30 يوماً من بايثون: اليوم 27 - بايثون مع MongoDB </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>المؤلف:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> الطبعة الثانية: يوليو، 2021</small>
</sub>

</div>

[<< اليوم 26](./26_python_web.md) | [اليوم 28 >>](./28_API.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 27](#-day-27)
- [بايثون مع MongoDB](#python-with-mongodb)
  - [MongoDB](#mongodb)
    - [SQL مقابل NoSQL](#sql-versus-nosql)
    - [الحصول على رش strings الاتصال (MongoDB URI)](#getting-connection-stringmongodb-uri)
    - [ربط تطبيق 'Flask' بـ 'MongoDB Cluster'](#connecting-flask-application-to-mongodb-cluster)
    - [إنشاء قاعدة بيانات ومجموعة](#creating-a-database-and-collection)
    - [إدراج العديد من المستندات إلى المجموعة](#inserting-many-documents-to-collection)
    - [البحث في MongoDB](#mongodb-find)
    - [البحث باستعلام](#find-with-query)
    - [استعلام البحث مع معدّل](#find-query-with-modifier)
    - [تحديد عدد المستندات](#limiting-documents)
    - [البحث مع الترتيب](#find-with-sort)
    - [التحديث باستعلام](#update-with-query)
    - [حذف مستند](#delete-document)
    - [حذف مجموعة](#drop-a-collection)
  - [💻 تمارين: اليوم 27](#-exercises-day-27)

# 📘 اليوم 27

# بايثون مع MongoDB

'Python' هو تقنية تعتمد على الخادم ويمكن ربطه بتطبيقات قواعد البيانات المختلفة. يمكن ربطه بقواعد بيانات 'SQL' و'NoSQL'. في هذا القسم، نقوم بربط 'Python' مع قاعدة بيانات 'MongoDB' وهي قاعدة بيانات من نوع 'NoSQL'.

## MongoDB

'MongoDB' هو قاعدة بيانات من نوع 'NoSQL'. يخزن 'MongoDB' البيانات في مستندات شبيهة بـ 'JSON' مما يجعله مرنًا وقابلًا للتوسع بشكل كبير. دعنا نرى المصطلحات المختلفة لقواعد بيانات 'SQL' و'NoSQL'. ستبين الجدول التالي الفرق بين قواعد بيانات 'SQL' و'NoSQL'.

### SQL مقابل NoSQL

![SQL versus NoSQL](../images/mongoDB/sql-vs-nosql.png)

في هذا القسم، س tậpركز على قاعدة بيانات 'NoSQL' وهي 'MongoDB'. لنقم بالتسجيل على [mongoDB](https://www.mongodb.com/) بالنقر على زر تسجيل الدخول ثم النقر على 'register' في الصفحة التالية.

![MongoDB Sign up pages](../images/mongoDB/mongodb-signup-page.png)

قم بملء الحقول والنقر على متابعة

![Mongodb register](../images/mongoDB/mongodb-register.png)

اختر الخطة المجانية

![Mongodb free plan](../images/mongoDB/mongodb-free.png)

اختر المنطقة الحرة القريبة وأعطِ أي اسم لمجموعتك.

![Mongodb cluster name](../images/mongoDB/mongodb-cluster-name.png)

الآن، تم إنشاء بيئة اختبار مجانية

![Mongodb sandbox](../images/mongoDB/mongodb-sandbox.png)

السماح بالوصول من جميع الكتب المضيفة المحلية

![Mongodb allow ip access](../images/mongoDB/mongodb-allow-ip-access.png)

إضافة مستخدم وكلمة مرور

![Mongodb add user](../images/mongoDB/mongodb-add-user.png)

إنشاء رابط 'MongoDB URI'

![Mongodb create uri](../images/mongoDB/mongodb-create-uri.png)

اختر محرك 'Python' 3.6 أو أعلى

![Mongodb python driver](../images/mongoDB/mongodb-python-driver.png)

### الحصول على رش string الاتصال (MongoDB URI)

انسخ رابط 'connection string' وستحصل على شيء مثل هذا:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

لا تقلق بشأن الرابط، إنه وسيلة لربط تطبيقك بـ 'MongoDB'.
دعنا نستبدل نائبة كلمة المرور بكلمة المرور التي استخدمتها لإضافة مستخدم.

**مثال:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

الآن، قمت باستبدال كل شيء وكلمة المرور هي 123123123 واسم قاعدة البيانات هو *thirty_days_python*. هذا مجرد مثال، يجب أن تكون كلمة مرورك أقوى من كلمة المرور في المثال.

تحتاج 'Python' إلى محرك 'MongoDB' للوصول إلى قاعدة بيانات 'MongoDB'. سنستخدم _pymongo_ مع _dnspython_ لربط تطبيقنا بقاعدة بيانات 'MongoDB'. داخل مجلد مشروعك قم بتثبيت 'pymongo' و'dnspython'.

```sh
pip install pymongo dnspython
```

يجب تثبيت وحدة "dnspython" لاستخدام روابط 'mongodb+srv://'. إن 'dnspython' هي أدوات 'DNS' لـ 'Python'. تدعم جميع أنواع السجلات تقريبًا.

### ربط تطبيق Flask بمجموعة MongoDB

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

عند تشغيل الكود أعلاه نحصل على قواعد بيانات 'MongoDB' الافتراضية.

```sh
['admin', 'local']
```

### إنشاء قاعدة بيانات ومجموعة

دعنا نقوم بإنشاء قاعدة بيانات، سيتم إنشاء قاعدة البيانات والمجموعة في 'MongoDB' إذا لم تكونا موجودتين. لنقم بإنشاء قاعدة بيانات باسم *thirty_days_of_python* ومجموعة *students*.

لاستخدام قاعدة بيانات:

```sh
db = client.name_of_databse # we can create a database like this or the second way
db = client['name_of_database']
```

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

بعد إنشاء قاعدة البيانات، أنشأنا أيضًا مجموعة 'students' واستخدمنا الدالة *insert_one()* لإدراج مستند واحد.
الآن، تم إنشاء قاعدة البيانات *thirty_days_of_python* ومجموعة *students* وتم إدراج المستند.
تحقق من مجموعة 'MongoDB' الخاصة بك وسترى قاعدة البيانات والمجموعة. داخل المجموعة، سيكون هناك مستند.

```sh
['thirty_days_of_python', 'admin', 'local']
```

إذا رأيت هذا في مجموعة 'MongoDB'، فهذا يعني أنك نجحت في إنشاء قاعدة بيانات ومجموعة.

![Creating database and collection](../images/mongoDB/mongodb-creating_database.png)

كما ترى في الشكل، تم إنشاء المستند بمعرّف طويل يعمل كمعرّف رئيسي. في كل مرة نقوم فيها بإنشاء مستند، يقوم 'MongoDB' بإنشاء معرّف فريد له.

### إدراج العديد من المستندات إلى المجموعة

دالة *insert_one()* تُدرج عنصرًا واحدًا في كل مرة. إذا أردنا إدراج العديد من المستندات في آن واحد، نستخدم الدالة *insert_many()* أو حلقة التكرار.
يمكننا استخدام حلقة التكرار لإدراج العديد من المستندات في آن واحد.

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

### البحث في MongoDB

دالتا *find()* و *findOne()* هما الدالتان الشائعتان للبحث عن البيانات في مجموعة في قاعدة بيانات 'MongoDB'. هما متشابهتان مع جملة 'SELECT' في قاعدة بيانات 'MySQL'.
دعنا نستخدم الدالة _find_one()_ للحصول على مستند في مجموعة قاعدة البيانات.

- \*find_one({"\_id": ObjectId("id"}): تحصل على الحدث الأول إذا لم يتم توفير معرّف.

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

الاستعلام أعلاه يُعيد السجل الأول لكن يمكننا استهداف مستند محدد باستخدام \_id محدد. دعنا ن做一个 مثال، استخدم معرّف 'David' للحصول على كائن 'David'.
'\_id':ObjectId('5df68a23f106fe2d315bbc8c')

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

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

لقد رأينا كيفية استخدام _find_one()_ باستخدام الأمثلة أعلاه. دعنا ننتقل إلى _find()_

- _find()_: يُعيد جميع الأحداث من مجموعة إذا لم نمرر كائن استعلام. الكائن هو كائن 'pymongo.cursor'.

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

يمكننا تحديد أي حقول يجب إرجاعها عن طريق تمرير الكائن الثاني في _find({}, {})_. القيمة 0 تعني عدم تضمين والقيمة 1 تعني تضمين لكن لا يمكن خلط 0 و 1، باستثناء \_id.

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

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### البحث باستعلام

في 'MongoDB' تأخذ الدالة 'find' كائن استعلام. يمكننا تمرير كائن استعلام وcanfiltrer المستندات التي نريد تصفية الإخراج منها.

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

استعلام مع معدّلات

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### استعلام البحث مع معدّل

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

استعلام مع معدّلات

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

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

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### تحديد عدد المستندات

يمكننا تحديد عدد المستندات المُعادة باستخدام الدالة _limit()_.

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

### البحث مع الترتيب

بشكل افتراضي، يكون الترتيب تصاعديًا. يمكننا تغيير الترتيب إلى تناقصي عن طريق إضافة المعلمة -1.

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

الترتيب التصاعدي

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

الترتيب التناقصي

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### التحديث باستعلام

سنستخدم الدالة *update_one()* لتحديث عنصر واحد. تأخذ كائنين أحدهما استعلام والآخر الكائن الجديد.
الشخص الأول، 'Asabeneh' لديه عمر غير مرجح. دعنا نقوم بتحديث عمر 'Asabeneh'.

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

عندما نريد تحديث العديد من المستندات في آن واحد نستخدم الدالة *update_many()*.

### حذف مستند

دالة *delete_one()* تحذف مستندًا واحدًا. تأخذ الدالة *delete_one()* كائن استعلام كمعامل. تزيل الحدث الأول فقط.
دعنا نزيل 'John' واحدًا من المجموعة.

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

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

كما ترى، تم إزالة 'John' من المجموعة.

عندما نريد حذف العديد من المستندات نستخدم الدالة *delete_many()*، تأخذ كائن استعلام. إذا مررنا كائن استعلام فارغ إلى *delete_many({})* فسيحذف جميع المستندات في المجموعة.

### حذف مجموعة

باستخدام الدالة _drop()_ يمكننا حذف مجموعة من قاعدة البيانات.

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

الآن، قمنا بحذف مجموعة 'students' من قاعدة البيانات.

## 💻 تمارين: اليوم 27

🎉 مبروك ! 🎉

[<< اليوم 26](./26_python_web.md) | [اليوم 28 >>](./28_API.md)

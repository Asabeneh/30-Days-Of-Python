<div align="center">
  <h1> 30 يوماً من البايثون: اليوم 29 - بناء 'API' </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>المؤلف:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>الطبعة الثانية: يوليو، 2021</small>
</sub>

</div>

[<< اليوم 28](../28_Day_API/28_API.md) | [اليوم 29 >>](../30_Day_Conclusions/30_conclusions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [اليوم 29](#day-29)
- [بناء 'API'](#building-api)
  - [هيكل 'API'](#structure-of-an-api)
  - [استرجاع البيانات باستخدام 'get'](#retrieving-data-using-get)
  - [الحصول على مستند بواسطة 'id'](#getting-a-document-by-id)
  - [إنشاء البيانات باستخدام 'POST'](#creating-data-using-post)
  - [التحديث باستخدام 'PUT'](#updating-using-put)
  - [حذف مستند باستخدام 'Delete'](#deleting-a-document-using-delete)
- [💻 تمارين: اليوم 29](#-exercises-day-29)

## اليوم 29

## بناء 'API'


في هذا القسم، سنغطي 'RESTful API' الذي يستخدم طرق طلبات 'HTTP' للحصول على البيانات ('GET')، وتحديثها ('PUT')، وإنشائها ('POST')، وحذفها ('DELETE').

'RESTful API' هو واجهة برمجة تطبيقات (API) تستخدم طلبات 'HTTP' للحصول على البيانات وتحديثها وإنشائها وحذفها. في الأقسام السابقة، تعلمنا عن بايثون وفلاسك وموngoDB. سنستخدم المعرفة التي اكتسبناها لتطوير 'RESTful API' باستخدام 'Python Flask' و'MongoDB'. كل تطبيق لديه عملية CRUD (إنشاء، قراءة، تحديث، حذف) لديه 'API' لإنشاء البيانات والحصول على البيانات وتحديثها أو حذفها من قاعدة البيانات.

يمكن للمتصفح التعامل مع طلب 'get' فقط. لذلك، يجب أن يكون لدينا أداة يمكنها مساعدتنا في التعامل مع جميع طرق الطلبات ('GET'، 'POST'، 'PUT'، 'DELETE').

أمثلة على 'API'

- 'Countries API': https://restcountries.eu/rest/v2/all
- 'Cats breed API': https://api.thecatapi.com/v1/breeds

'Postman' هو أداة شهيرة للغاية عندما يتعلق الأمر بتطوير 'API'. لذلك، إذا كنت تريد القيام بهذا القسم، تحتاج إلى [تنزيل postman](https://www.getpostman.com/). بديل 'Postman' هو [Insomnia](https://insomnia.rest/download).

![Postman](../images/postman.png)

### هيكل 'API'

نقطة نهاية 'API' هي عنوان 'URL' يمكنها المساعدة في استرجاع أو إنشاء أو تحديث أو حذف مورد. الهيكل يبدو هكذا:
مثال:
https://api.twitter.com/1.1/lists/members.json
يعيد أعضاء القائمة المحددة. لن يتم عرض أعضاء القائمة الخاصة إلا إذا كان المستخدم المصادق عليه يملك القائمة المحددة.
اسم الشركة متبوعاً بالإصدار متبوعاً ب目的 من 'API'.
الطرق:
طرق 'HTTP' و'URLs'

يستخدم 'API' طرق 'HTTP' التالية لمعالجة الكائنات:

```sh
GET        Used for object retrieval
POST       Used for object creation and object actions
PUT        Used for object update
DELETE     Used for object deletion
```

دعنا نبني 'API' يجمع معلومات عن طلاب '30DaysOfPython'. سنجمع الاسم والدولة والمدينة وتاريخ الميلاد والمهارات والسيرة الذاتية.

لتنفيذ هذا 'API'، سنستخدم:

- 'Postman'
- 'Python'
- 'Flask'
- 'MongoDB'

### استرجاع البيانات باستخدام 'get'

في هذه الخطوة، دعنا نستخدم بيانات وهمية ونعيدها كـ 'JSON'. لعيدها كـ 'JSON'، سنستخدم وحدة 'json' ووحدة 'Response'.

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

عندما تطلب عنوان 'URL' http://localhost:5000/api/v1.0/students على المتصفح ستحصل على هذا:

![Get on browser](../images/get_on_browser.png)

عندما تطلب عنوان 'URL' http://localhost:5000/api/v1.0/students على المتصفح ستحصل على هذا:

![Get on postman](../images/get_on_postman.png)

بدلاً من عرض البيانات الوهمية، دعنا نربط تطبيق فласك مع 'MongoDB' ونحصل على البيانات من قاعدة بيانات 'mongoDB'.

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

بربط فласك، يمكننا جلب بيانات مجموعة الطلاب من قاعدة بيانات 'thirty_days_of_python'.

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

### الحصول على مستند بواسطة 'id'

يمكننا الوصول إلى مستند واحد باستخدام 'id'، دعنا نصل إلى 'Asabeneh' باستخدام معرفه.
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

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

### إنشاء البيانات باستخدام 'POST'

نستخدم طريقة طلب 'POST' لإنشاء البيانات

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

### التحديث باستخدام 'PUT'

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

### حذف مستند باستخدام 'Delete'

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

## 💻 تمارين: اليوم 29

1. قم بتنفيذ المثال أعلاه وطور [هذا](https://thirtydayofpython-api.herokuapp.com/)

🎉 مبروك! 🎉

[<< اليوم 28](./28_API.md) | [اليوم 30 >>](./30_conclusions.md)

<div align="center">
  <h1> 30 Days Of Python: Day 29 - Building an API </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 28](../28_Day_API/28_API.md) | [Day 29 >>](../30_Day_Conclusions/30_conclusions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Day 29](#day-29)
- [Building API](#building-api)
  - [Structure of an API](#structure-of-an-api)
  - [Retrieving data using get](#retrieving-data-using-get)
  - [Getting a document by id](#getting-a-document-by-id)
  - [Creating data using POST](#creating-data-using-post)
  - [Updating using PUT](#updating-using-put)
  - [Deleting a document using Delete](#deleting-a-document-using-delete)

## Day 29

## Building API

នៅក្នុងផ្នែកនេះ យើងនឹងពិភាក្សាអំពី RESTful API ដែកប្រើ HTTP request methods ដើម្បី GET, PUT, POST និង DELETE data។

RESTful API គឺជា application program interface (API) ដែលប្រើ HTTP requests ដើម្បី GET, PUT, POST និង DELETE data។ នៅក្នុងផ្នែកមុននេះយើងបានរៀនអំពី Python, flask និង mongoDB។ យើងនឹងប្រើចំណេះដឹងដែលយើងទទួលបានដើម្បីបង្កើត RESTful API ដោយប្រើ Python flask និង mongoDB database។ កម្មវិធីដែលមាន CRUD(Create, Read, Update, Delete) operation មាន API ដើម្បី create data, ដើម្បី get data, ដើម្បី update data ឬ ដើម្បី delete data ពី database។

Browser អាចតែយកបាន request. ដូច្នេះ, យើងត្រូវមានឧបករណ៍ដែលអាចជួយយើងក្នុងការគ្រប់គ្រង request methods(GET, POST, PUT, DELETE)។

ឧទាហរណ៍ API

- Countries API: https://restcountries.eu/rest/v2/all
- Cats breed API: https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/) ជាឧបករណ៍ដ៏ពេញនិយមសម្រាប់ការបង្កើត API ។ ដូច្នេះ, ប្រសិនបើអ្នកចង់ធ្វើផ្នែកនេះអ្នកត្រូវបញ្ចូល [download postman](https://www.getpostman.com/). ជម្រើសមួយទៀតគឺ [Insomnia](https://insomnia.rest/download).

![Postman](../images/postman.png)

### Structure of an API

API end point គឺជា URL ដែលអាចជួយដល់ការ retrieve, create, update ឬ delete ធនធានណាមួយ។ រចនាសម្ព័ន្ធនេះមានរូបរាងដូចខាងក្រោម៖
ឧទាហរណ៍:
https://api.twitter.com/1.1/lists/members.json
បញ្ជូនសមាជិកនៃបញ្ជីដែលបានកំណត់។ Private list នៃសមាជិក នឹងត្រូវបានបង្ហាញតែប្រសិនបើអ្នកប្រើប្រាស់ដែលត្រូវបានបញ្ជាក់ជាម្ចាស់បញ្ជីដែលបានកំណត់។
ឈ្មោះនៃឈ្មោះក្រុមហ៊ុនបន្តដោយ version បន្តដោយ គោយដៅនៃ API។
The methods:
HTTP methods & URLs

API ប្រើប្រាស់ដូចខាងក្រោមនៃ HTTP methods សម្រាប់ការកែប្រែ object:

```sh
GET        Used for object retrieval ប្រើសម្រាប់ទាញយកវត្ថុ
POST       Used for object creation and object actions ប្រើសម្រាប់ការបង្កើតវត្ថុ និងសកម្មភាពរបស់វត្ថុ
PUT        Used for object update ប្រើសម្រាបការកែប្រែ
DELETE     Used for object deletion ប្រើសម្រាប់ការលុប
```

សូមយើងបង្កើត API ដែលប្រមូលព័ត៌មានអំពី 30DaysOfPython students។ យើងនឹងប្រមូល name, country, city, date of birth, skills និង bio.

ដើម្បីអនុវត្ត API នេះយើងនឹងប្រើ:

- Postman
- Python
- Flask
- MongoDB

### Retrieving data using get

Iនៅក្នុងជំហាននេះ, យើងត្រូវប្រើទិន្នន័យខ្លែងខ្លាយ ហើយត្រឡប់មកវិញជា json។ ដើម្បីត្រឡប់មកវិញជា json, នឹងប្រើ json module និង Response module។

```py
# let's import the flask

from flask import Flask,  Response
import json

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

នៅពេលដែលអ្នកសុំ URL http://localhost:5000/api/v1.0/students នៅលើ browser អ្នកនឹងទទួលបាននេះ:

![Get on browser](../images/get_on_browser.png)

នៅពេលដែលអ្នកសុំ URL http://localhost:5000/api/v1.0/students នៅលើ browser អ្នកនឹងទទួលបាននេះ:

![Get on postman](../images/get_on_postman.png)

ក្រៅពីការប្រើទិន្នន័យខ្លែងខ្លាយ សូមយើងភ្ជាប់កម្មវិធី flask ជាមួយ MongoDB និងទទួលបានទិន្នន័យពី MongoDB database ។

```py
# let's import the flask

from flask import Flask,  Response
import json
import pymongo


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

ដោយភ្ជាប់ flask, យើងអាចទាញយកទិន្នន័យការប្រមូលយករបស់សិស្សពីមូលដ្ឋានទិន្នន័យ thirty_days_of_python ។

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

### Getting a document by id

យើងអាចយកបាន document មួយដោយប្រើ id, តោះនាំយើងយក Asabeneh ដោយប្រើ id.
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo


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

### Creating data using POST

យើងអាចប្រើ POST request method ដើម្បី create data

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime


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

### Updating using PUT

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime


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

### Deleting a document using Delete

```py
# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime


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

[<< Day 28](../28_Day_API/28_API.md) | [Day 30 >>](../30_Day_Conclusions/30_conclusions.md)

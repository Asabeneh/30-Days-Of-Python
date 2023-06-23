<div align="center">
  <h1> 30 Days Of Python: Day 27 - Python with MongoDB </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>

</div>

[<< Day 26](../26_Day_Python_web/26_python_web.md) | [Day 28 >>](../28_Day_API/28_API.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 27](#-day-27)
- [Python with MongoDB](#python-with-mongodb)
  - [MongoDB](#mongodb)
    - [SQL versus NoSQL](#sql-versus-nosql)
    - [Getting Connection String(MongoDB URI)](#getting-connection-stringmongodb-uri)
    - [Connecting Flask application to MongoDB Cluster](#connecting-flask-application-to-mongodb-cluster)
    - [Creating a database and collection](#creating-a-database-and-collection)
    - [Inserting many documents to collection](#inserting-many-documents-to-collection)
    - [MongoDB Find](#mongodb-find)
    - [Find with Query](#find-with-query)
    - [Find query with modifier](#find-query-with-modifier)
    - [Limiting documents](#limiting-documents)
    - [Find with sort](#find-with-sort)
    - [Update with query](#update-with-query)
    - [Delete Document](#delete-document)
    - [Drop a collection](#drop-a-collection)
  - [💻 Exercises: Day 27](#-exercises-day-27)

# 📘 Day 27

# Python with MongoDB

Python គឺជា backend technology ហើយវាអាចភ្ជាប់ជាមួយ data base ផ្សេងៗ។ វាអាចភ្ជាប់ទៅនឹង SQL និង noSQL databases។ នៅក្នុងផ្នែកនេះ យើងនឹងភ្ជាប់ Python ជាមួយនឹង MongoDB database ដែលជា database noSQL។

## MongoDB

MongoDB គឺជា NoSQL database។ MongoDB រក្សាទុកទិន្នន័យនៅក្នុងឯកសារ JSON ដែលធ្វើអោយ MongoDB មានភាពរលូន និងអាចកែច្នៃបាន។ សូមមើលពាក្យសម្ដី ផ្សេងៗនៃ SQL និង NoSQL databases។ តារាងខាងក្រោមនេះនឹងបង្ហាញពីភាពខុសគ្នារវាង SQL versus NoSQL databases ។

### SQL versus NoSQL

![SQL versus NoSQL](../images/mongoDB/sql-vs-nosql.png)

នៅក្នុងផ្នែកនេះយើងនឹងផ្តោតលើមូលដ្ឋានទិន្នន័យ NoSQL MongoDB ។ សូមចុះឈ្មោះ [mongoDB](https://www.mongodb.com/) ចុចលើប៊ូតុង Sign in រួចចុច Register នៅទំព័របន្ទាប់។
![MongoDB Sign up pages](../images/mongoDB/mongodb-signup-page.png)

បំពេញនិងចុចបន្ត

![Mongodb register](../images/mongoDB/mongodb-register.png)

ជ្រើសរើសផែនការឥតគិតថ្លៃ

![Mongodb free plan](../images/mongoDB/mongodb-free.png)

ជ្រើសរើសតំបន់ និងផ្តល់ឈ្មោះ cluster។

![Mongodb cluster name](../images/mongoDB/mongodb-cluster-name.png)

Now, a free sandbox is created
ឥឡូវនេះ, free sandbox ត្រូវបានបង្កើតឡើង

![Mongodb sandbox](../images/mongoDB/mongodb-sandbox.png)

គ្រប់ local host access

![Mongodb allow ip access](../images/mongoDB/mongodb-allow-ip-access.png)

ដាក់ user និង password

![Mongodb add user](../images/mongoDB/mongodb-add-user.png)

បង្តើត mongoDB uri link

![Mongodb create uri](../images/mongoDB/mongodb-create-uri.png)

ជ្រើសរើស Python 3.6 ឬ ខ្ពស់ជាងនឹង

![Mongodb python driver](../images/mongoDB/mongodb-python-driver.png)

### Getting Connection String(MongoDB URI)

ចម្លង connection string link ហើយអ្នកនឹងទទួលបានអ្វីមួយដូចនេះ

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

កុំបារម្ភអំពី url, វាជាមធ្យោបាយមួយដើម្បីភ្ជាប់កម្មវិធីរបស់អ្នកទៅ MongoDB។
សូមយើងជំនួស password placeholder ជាមួយនឹង password ដែលអ្នកប្រើសម្រាប់ user។

**Example:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

ឥឡូវនេះ ខ្ញុំបានជំនួសអ្វីទាំងអស់ និង password គឺ 123123 និងឈ្មោះរបស់ database គឺ thirty_days_python។ នេះគ្រាន់តែជាឧទាហរណ៍មួយប៉ុណ្ណោះ, password របស់អ្នកត្រូវតែខ្លាំងជាងនេះបន្តិច។

Python ត្រូវការ mongoDB driver ការចូលទៅកាន់ mongoDB database។ យើងនឹងប្រើ _pymongo_ ជាមួយ _dnspython_ ដើម្បីភ្ជាប់កម្មវិធីរបស់យើងជាមួយ mongoDB base។ នៅខាងក្នុង project directory បញ្ចូល pymongo និង dnspython។

```sh
pip install pymongo dnspython
```

"dnspython" module ត្រូវមានសម្រាប់ប្រើ mongodb+srv:// URIs។ dnspython គឺ DNS toolkit សម្រាប់ Python។ វាគាំទ្រប្រភេទឯកសារទាំងអស់។

### Connecting Flask application to MongoDB Cluster

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

ពេលយើង run code, យើងទទួលបាន default mongoDB databases.

```sh
['admin', 'local']
```

### Creating a database and collection

សូមយើងបង្កើត database និង collection ក្នុង mongoDB, នឹងត្រូវបានបង្កើតឡើង ប្រសិនបើវាមិនមាន។ សូមបង្កើត data base ឈ្នោះ _thirty_days_of_python_ និង _students_ collection។
ដើម្បីបង្កើត database

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

បន្ទាប់ពីយើងបង្កើត database, យើងក៏បានបង្កើត students collection និងយើងប្រើ *insert_one()* method ដើម្បីបញ្ចូល document។
ឥឡូវនេះ database *thirty_days_of_python* និង *students* collection ត្រូវបានបង្កើតឡើង ហើយ document ត្រូវបានបញ្ចូល។
ពិនិត្យមើល mongoDB cluster ហើយអ្នកនឹងឃើញ database និង collection។ ក្នុង collection, នឹងមាន document។

```sh
['thirty_days_of_python', 'admin', 'local']
```

ប្រសិនបើអ្នកឃើញនេះនៅលើ mongoDB cluster, វាមានន័យថា អ្នកបានបង្កើត database និង collection.

![Creating database and collection](../images/mongoDB/mongodb-creating_database.png)

ប្រសិនបើអ្នកបានឃើញនៅលើរូបភាព, document ត្រូវបានបង្កើតឡើងដោយមាន id វែងដែលធ្វើជា primary key។ រាល់ពេលដែលយើងបង្កើត document, mongoDB និងបង្កើត ID ពិសេសសម្រាប់វា។

### Inserting many documents to collection

*insert_one()*  method បញ្ចូល item ក្នុងពេលតែមួយ, ប្រសិនបើយើងចង់បញ្ចូលច្រើន documents ភ្លាមៗយើងប្រើ *insert_many()* method ឬ for loop។
យើងអាចប្រើ for loop ដើម្បីបញ្ចូលច្រើន documents ភ្លាមៗ។

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

### MongoDB Find

*find()* និង *findOne()* methods ជាវិធីទូទៅដើម្បីរកទិន្នន័យនៅក្នុង collection ក្នុង mongoDB database។ វាស្រដៀងនឹង SELECT statement ក្នុង MySQL database។
សូមយើងប្រើ _find_one()_ method ដើម្បីទទួលបាន document ក្នុង database collection។

- \*find_one({"\_id": ObjectId("id"}): ទទួលបានការកើតឡើងដំបូង ប្រសិនបើ ID មិនត្រូវបានផ្តល់

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

Query ខាងលើបានត្រឡប់មកលេខដំបូង ប៉ុន្តែយើងអាចផ្តោតលើ document ណាមួយដោយប្រើ \_id។ សូមយើងធ្វើឧទាហរណ៍មួយ, ប្រើ id របស់ David ដើម្បីបាន David object។
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

យើងបានឃើញការប្រើ _find_one()_ ដោយប្រើឧទាហរណ៍ខាងលើ។ សូមចល័តមួយទៅ _find()_

- _find()_: ផ្តល់នូវការកើតឡើងទាំងអស់ពី collection ប្រសិនបើយើងមិនដាក់ query object។ Object គឺ pymongo.cursor object។

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

យើងអាចកំណត់ Field ដែលត្រូវត្រឡប់មកវិញ ដោយផ្ទេរ Object ទីពីរនៅក្នុង _find({}, {})_។ 0 មានន័យថាមិនរួមបញ្ចូល និង 1 មានន័យថាបញ្ចូល ប៉ុន្តែយើងមិនអាចលាយឡំគ្នា 0 និង 1, លើកលែងតែ \_id។

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

### Find with Query

ក្នុង mongoDB find យក query object។ យើងអាចប្រើ query object និង យើងអាចតម្រង documents យើងចង់តម្រង។

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

Query ជាមួយ modifiers

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

### Find query with modifier

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

Query ជាមួយ modifiers

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

### Limiting documents

យើងអាចកំណត់ចំនួន documents យើងត្រឡប់មកវិញ ដោយប្រើ _limit()_ method។

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

### Find with sort

ដោយ default, sort គឺមាននៅក្នុងលំដាប់ឡើង។ យើងអាចផ្លាស់ប្ដូរការ sort ទៅតាមលំដាប់ចុះដោយបន្ថែម parameter -1 ។

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

Ascending order

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Descending order

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### Update with query

យើងនឹងប្រើ *update_one()* method ដើម្បីប្តូរ item មួយ។ វាត្រូវការ object ពីរ, មួយជា query និង ពីរជា object ថ្មី។
មនុស្សទីមួយ, Asabeneh មានអាយុមិនគួរឲ្យជឿ។ នាំយើងប្តូរអាយុរបស់ Asabeneh។

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

នៅពេលដែលយើងចង់ប្តូរ documents ច្រើនភ្លាមៗ យើងប្រើ *upate_many()* method។

### Delete Document

*delete_one()* លុបមួយ document។ *delete_one()* ត្រូវការ query object parameter។ វាគ្រាន់តែលុបចោលការកើតឡើងដំបូង។
យើងត្រូវដក John ម្នាក់ចេញពី collection។

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

ដូចដែលអ្នកអាចមើលបាន John ត្រូវបានដកចេញពី collection។

When we want to delete many documents we use *delete_many()* method, it takes a query object. If we pass an empty query object to *delete_many({})* it will delete all the documents in the collection.

### Drop a collection

ការប្រើ _drop()_ method យើងអាចលុប collection ពី database។

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

ឥឡូវនេះយើងបានលុបចោល students collection ពី database។

🎉 CONGRATULATIONS ! 🎉

[<< Day 26](../26_Day_Python_web/26_python_web.md) | [Day 28 >>](../28_Day_API/28_API.md)

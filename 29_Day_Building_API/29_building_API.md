<div align="center">
  <h1> 30 дней Python: День 29 - Разработка API </h1>
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

[<< День 28](../28_Day_API/28_API.md) | [День 29 >>](../30_Day_Conclusions/30_conclusions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [День 29](#день-29)
- [Разработка API](#разработка-api)
  - [Структура API](#структура-api)
  - [Получение данных с использованием GET](#получение-данных-с-использованием-get)
  - [Получение документа по идентификатору](#получение-документа-по-идентификатору)
  - [Создание данных с использованием POST](#создание-данных-с-использованием-post)
  - [Обновление данных с использованием PUT](#обновление-данных-с-использованием-put)
  - [Удаление документа с использованием DELETE](#удаление-документа-с-использованием-delete)
- [Упражнения: День 29](#упражнения-день-29)

## День 29

## Разработка API

В этом разделе мы разберем RESTful API, который использует методы запросов HTTP для получения (GET), обновления (PUT), создания (POST) и удаления (DELETE) данных.

RESTful API представляет собой интерфейс прикладного программирования (API), который использует HTTP-запросы для выполнения операций GET, PUT, POST и DELETE с данными. В предыдущих разделах мы изучили Python, Flask и MongoDB. Мы воспользуемся полученными знаниями, чтобы разработать RESTful API с использованием Python, Flask и MongoDB. Каждое приложение, имеющее операции CRUD (Create, Read, Update, Delete), имеет API для создания данных, получения данных, обновления данных или удаления данных из базы данных.

Браузер может обрабатывать только запросы GET. Поэтому нам необходимо использовать инструмент, который поможет нам обрабатывать все методы запросов (GET, POST, PUT, DELETE).

Примеры API:

- API стран: https://restcountries.eu/rest/v2/all
- API пород кошек: https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/) это очень популярный инструмент для разработки API. Поэтому, если вы хотите продолжить этот раздел, вам следует скачать [Postman](https://www.getpostman.com/). Альтернативой Postman является [Insomnia](https://insomnia.rest/download).

![Postman](../images/postman.png)

### Структура API

API endpoint (конечная точка API) - это URL-адрес, который позволяет получать, создавать, обновлять или удалять ресурс. Его структура выглядит следующим образом:

https://api.twitter.com/1.1/lists/members.json

Этот пример возвращает участников указанного списка. Частные участники будут отображены только в том случае, если аутентифицированный пользователь является владельцем указанного списка. В URL-адресе указывается имя компании, за которым следует версия API, а затем назначение API.

API использует следующие методы HTTP для манипуляции объектами::

```sh
GET        Используется для извлечения объекта
POST       Используется для создания объекта и выполнения действий с объектом
PUT        Используется для обновления объекта
DELETE     Используется для удаления объекта
```

Давайте создадим API, которое собирает информацию о студентах ThirtyDaysOfPython. Мы будем собирать имя, страну, город, дату рождения, навыки и информация о себе.

Для реализации этого API мы будем использовать следующее:

- Postman
- Python
- Flask
- MongoDB

### Получение данных с использованием GET

На этом шаге давайте использовать фиктивные данные и возвращать их в формате JSON. Чтобы вернуть данные в формате JSON, мы будем использовать модуль json и модуль Response.

```py
# импортируем flask

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
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Когда вы запросите URL http://localhost:5000/api/v1.0/students в браузере, вы получите следующий результат:

![Get on browser](../images/get_on_browser.png)

Когда вы запросите URL http://localhost:5000/api/v1.0/students в Postman, вы получите следующий результат:

![Get on postman](../images/get_on_postman.png)

Вместо отображения фиктивных данных давайте свяжем приложение Flask с MongoDB и получим данные из базы данных MongoDB.

```py
# импортируем flask

from flask import Flask,  Response
import json
import pymongo


app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # lдоступ к базе данных

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Подключив Flask, мы можем получить данные коллекции "students" из базы данных "thirty_days_of_python".

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

### Получение документа по идентификатору

Мы можем получить доступ к отдельному документу, используя его идентификатор. Давайте получим доступ к документу Asabeneh, используя его идентификатор: 
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# импортируем flask

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
db = client['thirty_days_of_python'] # доступ к базе данных

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
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

### Создание данных с использованием POST

Мы можем использовать метод запроса POST для создания данных.

```py
# импортируем flask

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
db = client['thirty_days_of_python'] # доступ к базе данных

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
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Обновление данных с использованием PUT

```py
# импортируем flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime


app = Flask(__name__)

MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # этот декоратор создает маршрут home
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
    # возвращает Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
def update_student (id):
if __name__ == '__main__':
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Удаление документа с использованием DELETE

```py
# импортируем flask

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
db = client['thirty_days_of_python'] # доступ к базе данных

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # этот декоратор создает маршрут home
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
    # возвращает Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # этот декоратор создает маршрут home
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
    # возвращает Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":ObjectId(id)})
    return
if __name__ == '__main__':
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## Упражнения: День 29

1. Реализуйте приведенный выше пример и разработайте [веб-приложение](https://thirtydayofpython-api.herokuapp.com/)

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 28](../28_Day_API/28_API.md) | [День 30 >>](../30_Day_Conclusions/30_conclusions.md)

<div align="center">
  <h1> 30 Days Of Python: День 29 - Создание API </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Второе издание: июль 2021</small>
</sub>

</div>

[<< День 28](./28_API_ru.md) | [День 29 >>](./30_conclusions_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [День 29](#день-29)
- [Создание API](#создание-api)
  - [Структура API](#структура-api)
  - [Получение данных с помощью get](#получение-данных-с-помощью-get)
  - [Получение документа по id](#получение-документа-по-id)
  - [Создание данных с помощью POST](#создание-данных-с-помощью-post)
  - [Обновление с помощью PUT](#обновление-с-помощью-put)
  - [Удаление документа с помощью Delete](#удаление-документа-с-помощью-delete)
- [💻 Упражнения: День 29](#-упражнения-день-29)

## День 29

## Создание API


В этом разделе мы рассмотрим RESTful API, который использует HTTP-методы запросов для GET, PUT, POST и DELETE данных.

RESTful API — это интерфейс программирования приложений (API), который использует HTTP-запросы для GET, PUT, POST и DELETE данных. В предыдущих разделах мы изучили Python, Flask и MongoDB. Мы используем полученные знания, чтобы разработать RESTful API с помощью Python Flask и MongoDB. Каждое приложение, в котором есть операция CRUD (Create, Read, Update, Delete), имеет API для создания данных, получения данных, обновления данных или удаления данных из базы данных.

Браузер может обрабатывать только запрос get. Поэтому нам нужен инструмент, который поможет нам обрабатывать все методы запросов (GET, POST, PUT, DELETE).

Примеры API

- API стран: https://restcountries.eu/rest/v2/all
- API пород кошек: https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/) — очень популярный инструмент, когда речь идёт о разработке API. Так что, если вы хотите пройти этот раздел, вам нужно [скачать Postman](https://www.getpostman.com/). Альтернатива Postman — [Insomnia](https://insomnia.rest/download).

![Postman](../images/postman.png)

### Структура API

Эндпоинт API — это URL, который помогает получать, создавать, обновлять или удалять ресурс. Структура выглядит так:
Пример:
https://api.twitter.com/1.1/lists/members.json
Возвращает участников указанного списка. Участники закрытого списка будут показаны, только если аутентифицированный пользователь владеет указанным списком.
Название компании, за ним версия, за ней назначение API.
Методы:
HTTP-методы и URL

API использует следующие HTTP-методы для работы с объектами:

```sh
GET        Используется для получения объекта
POST       Используется для создания объекта и действий с объектом
PUT        Используется для обновления объекта
DELETE     Используется для удаления объекта
```

Давайте создадим API, который собирает информацию о студентах 30DaysOfPython. Мы будем собирать имя, страну, город, дату рождения, навыки и биографию.

Чтобы реализовать этот API, мы будем использовать:

- Postman
- Python
- Flask
- MongoDB

### Получение данных с помощью get

На этом шаге давайте использовать фиктивные данные и вернуть их в виде json. Чтобы вернуть их в виде json, мы используем модуль json и модуль Response.

```py
# давайте импортируем flask

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
    # для развёртывания
    # чтобы это работало и в production, и в development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Когда вы запросите адрес http://localhost:5000/api/v1.0/students в браузере, вы получите это:

![Get в браузере](../images/get_on_browser.png)

Когда вы запросите адрес http://localhost:5000/api/v1.0/students в браузере, вы получите это:

![Get в Postman](../images/get_on_postman.png)

Вместо отображения фиктивных данных давайте подключим приложение flask к MongoDB и получим данные из базы данных mongoDB.

```py
# давайте импортируем flask

from flask import Flask,  Response
import json
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # для развёртывания
    # чтобы это работало и в production, и в development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Подключив flask, мы можем получить данные коллекции students из базы данных thirty_days_of_python.

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

### Получение документа по id

Мы можем получить доступ к отдельному документу по id; давайте получим доступ к Asabeneh по его id.
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# давайте импортируем flask

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
db = client['thirty_days_of_python'] # доступ к базе данных

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # для развёртывания
    # чтобы это работало и в production, и в development
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

### Создание данных с помощью POST

Мы используем метод запроса POST для создания данных

```py
# давайте импортируем flask

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
    # для развёртывания
    # чтобы это работало и в production, и в development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Обновление с помощью PUT

```py
# давайте импортируем flask

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # этот декоратор создаёт домашний маршрут
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
    # для развёртывания
    # чтобы это работало и в production, и в development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Удаление документа с помощью Delete

```py
# давайте импортируем flask

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # этот декоратор создаёт домашний маршрут
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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # этот декоратор создаёт домашний маршрут
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
    # для развёртывания
    # чтобы это работало и в production, и в development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## 💻 Упражнения: День 29

1. Реализуйте приведённый выше пример и разработайте [это](https://thirtydayofpython-api.herokuapp.com/)

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 28](./28_API_ru.md) | [День 30 >>](./30_conclusions_ru.md)

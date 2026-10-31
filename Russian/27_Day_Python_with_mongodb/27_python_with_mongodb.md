<div align="center">
  <h1> 30 дней Python: День 27 - Python с MongoDB </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Асабенех Йетаех</a><br>
<small> Второе издание: июль 2021</small>
</sub>

</div>

[<< День 26](../26_Day_Python_web/26_python_web.md) | [День 28 >>](../28_Day_API/28_API.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 27](#-день-27)
- [Python с MongoDB](#python-с-mongodb)
  - [MongoDB](#mongodb)
    - [SQL против NoSQL](#sql-против-nosql)
    - [Получение строки подключения (URI MongoDB)](#получение-строки-подключенияuri-mongodb)
    - [Подключение приложения Flask к кластеру MongoDB](#подключение-приложения-flask-к-кластеру-mongodb)
    - [Создание базы данных и коллекции](#создание-базы-данных-и-коллекции)
    - [Вставка множества документов в коллекцию](#вставка-множества-документов-в-коллекцию)
    - [MongoDB Find](#mongodb-find)
    - [Поиск с запросом](#поиск-с-запросом)
    - [Запрос find с модификатором](#запрос-find-с-модификатором)
    - [Ограничение документов](#ограничение-документов)
    - [Поиск с сортировкой](#поиск-с-сортировкой)
    - [Обновление с запросом](#обновление-с-запросом)
    - [Удаление документа](#удаление-документа)
    - [Удаление коллекции (Drop)](#удаление-коллекции-drop)
  - [💻 Упражнения: День 27](#-упражнения-день-27)

# 📘 День 27

# Python с MongoDB

Python - это серверная технология, и её можно подключить к разным системам управления базами данных. Её можно подключить как к SQL, так и к noSQL базам данных. В этом разделе мы подключим Python к базе данных MongoDB, которая является noSQL базой данных.

## MongoDB

MongoDB - это база данных NoSQL. MongoDB хранит данные в документе, похожем на JSON, что делает MongoDB очень гибкой и масштабируемой. Давайте рассмотрим различные терминологии баз данных SQL и NoSQL. Следующая таблица покажет разницу между базами данных SQL и NoSQL.

### SQL против NoSQL

![SQL против NoSQL](../../images/mongoDB/sql-vs-nosql.png)

В этом разделе мы сосредоточимся на NoSQL базе данных MongoDB. Давайте зарегистрируемся на [mongoDB](https://www.mongodb.com/), нажав кнопку входа, а затем нажмите «зарегистрироваться» на следующей странице.

![Страницы регистрации MongoDB](../../images/mongoDB/mongodb-signup-page.png)

Заполните поля и нажмите «продолжить»

![Регистрация MongoDB](../../images/mongoDB/mongodb-register.png)

Выберите бесплатный план

![Бесплатный план MongoDB](../../images/mongoDB/mongodb-free.png)

Выберите ближайший бесплатный регион и дайте любое имя вашему кластеру.

![Имя кластера MongoDB](../../images/mongoDB/mongodb-cluster-name.png)

Теперь создана бесплатная песочница

![Песочница MongoDB](../../images/mongoDB/mongodb-sandbox.png)

Весь доступ с локальных хостов

![Доступ по IP MongoDB](../../images/mongoDB/mongodb-allow-ip-access.png)

Добавьте пользователя и пароль

![Добавление пользователя MongoDB](../../images/mongoDB/mongodb-add-user.png)

Создайте ссылку URI mongoDB

![Создание URI MongoDB](../../images/mongoDB/mongodb-create-uri.png)

Выберите драйвер Python 3.6 или выше

![Драйвер Python MongoDB](../../images/mongoDB/mongodb-python-driver.png)

### Получение строки подключения (URI MongoDB)

Скопируйте ссылку строки подключения, и вы получите что-то вроде этого:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Не беспокойтесь об url, это средство для подключения вашего приложения к mongoDB.
Давайте заменим плейсхолдер пароля на пароль, который вы использовали для добавления пользователя.

**Пример:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Теперь я заменил всё, и пароль - 123123, а имя базы данных - *thirty_days_python*. Это просто пример, ваш пароль должен быть надёжнее, чем пароль из примера.

Python нуждается в драйвере mongoDB для доступа к базе данных mongoDB. Мы будем использовать _pymongo_ с _dnspython_ для подключения нашего приложения к базе mongoDB. Внутри каталога вашего проекта установите pymongo и dnspython.

```sh
pip install pymongo dnspython
```

Модуль "dnspython" должен быть установлен для использования URI mongodb+srv://. dnspython - это DNS-инструментарий для Python. Он поддерживает почти все типы записей.

### Подключение приложения Flask к кластеру MongoDB

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

Когда мы запускаем приведённый выше код, мы получаем базы данных mongoDB по умолчанию.

```sh
['admin', 'local']
```

### Создание базы данных и коллекции

Давайте создадим базу данных; база данных и коллекция в mongoDB будут созданы, если их не существует. Давайте создадим базу данных с именем *thirty_days_of_python* и коллекцию *students*.

Чтобы создать базу данных:

```sh
db = client.name_of_databse # мы можем создать базу данных так, или вторым способом
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

После создания базы данных мы также создали коллекцию students и использовали метод *insert_one()* для вставки документа.
Теперь база данных *thirty_days_of_python* и коллекция *students* созданы, и документ вставлен.
Проверьте ваш кластер mongoDB, и вы увидите и базу данных, и коллекцию. Внутри коллекции будет документ.

```sh
['thirty_days_of_python', 'admin', 'local']
```

Если вы видите это в кластере mongoDB, значит, вы успешно создали базу данных и коллекцию.

![Создание базы данных и коллекции](../../images/mongoDB/mongodb-creating_database.png)

Если вы видели на рисунке, документ создан с длинным id, который действует как первичный ключ. Каждый раз, когда мы создаём документ, mongoDB создаёт для него уникальный id.

### Вставка множества документов в коллекцию

Метод *insert_one()* вставляет один элемент за раз; если мы хотим вставить много документов сразу, мы используем метод *insert_many()* или цикл for.
Мы можем использовать цикл for, чтобы вставить много документов сразу.

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

Методы *find()* и *findOne()* - это распространённые методы для поиска данных в коллекции базы данных mongoDB. Это похоже на оператор SELECT в базе данных MySQL.
Давайте используем метод _find_one()_, чтобы получить документ в коллекции базы данных.

- \*find_one({"\_id": ObjectId("id"}): Получает первое вхождение, если id не указан

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

Приведённый выше запрос возвращает первую запись, но мы можем нацелиться на конкретный документ, используя конкретный \_id. Давайте сделаем один пример: используйте id Дэвида, чтобы получить объект Дэвида.
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

Мы увидели, как использовать _find_one()_ на приведённых выше примерах. Давайте перейдём к _find()_

- _find()_: возвращает все вхождения из коллекции, если мы не передаём объект запроса. Объект - это объект pymongo.cursor.

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

Мы можем указать, какие поля возвращать, передав второй объект в _find({}, {})_. 0 означает не включать, а 1 означает включать, но мы не можем смешивать 0 и 1, кроме как для \_id.

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

### Поиск с запросом

В mongoDB find принимает объект запроса. Мы можем передать объект запроса и отфильтровать документы, которые хотим отфильтровать.

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

Запрос с модификаторами

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

### Запрос find с модификатором

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

Запрос с модификаторами

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

### Ограничение документов

Мы можем ограничить количество возвращаемых документов, используя метод _limit()_.

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

### Поиск с сортировкой

По умолчанию сортировка выполняется в порядке возрастания. Мы можем изменить сортировку на убывающую, добавив параметр -1.

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

Порядок возрастания

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Порядок убывания

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### Обновление с запросом

Мы будем использовать метод *update_one()* для обновления одного элемента. Он принимает два объекта: один - это запрос, а второй - новый объект.
Первый человек, Асабенех, получил очень неправдоподобный возраст. Давайте обновим возраст Асабенеха.

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

Когда мы хотим обновить много документов сразу, мы используем метод *upate_many()*.

### Удаление документа

Метод *delete_one()* удаляет один документ. *delete_one()* принимает параметр объекта запроса. Он удаляет только первое вхождение.
Давайте удалим одного Джона из коллекции.

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

Как вы видите, Джон был удалён из коллекции.

Когда мы хотим удалить много документов, мы используем метод *delete_many()*, он принимает объект запроса. Если мы передадим пустой объект запроса в *delete_many({})*, это удалит все документы в коллекции.

### Удаление коллекции (Drop)

Используя метод _drop()_, мы можем удалить коллекцию из базы данных.

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

Теперь мы удалили коллекцию students из базы данных.

## 💻 Упражнения: День 27

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 26](../26_Day_Python_web/26_python_web.md) | [День 28 >>](../28_Day_API/28_API.md)

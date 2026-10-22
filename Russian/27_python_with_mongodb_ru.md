<div align="center">
  <h1> 30 Days Of Python: День 27 - Python с MongoDB </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Второе издание: июль 2021</small>
</sub>

</div>

[<< День 26](./26_python_web_ru.md) | [День 28 >>](./28_API_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 27](#-день-27)
- [Python с MongoDB](#python-с-mongodb)
  - [MongoDB](#mongodb)
    - [SQL против NoSQL](#sql-против-nosql)
    - [Получение строки подключения (MongoDB URI)](#получение-строки-подключения-mongodb-uri)
    - [Подключение приложения Flask к кластеру MongoDB](#подключение-приложения-flask-к-кластеру-mongodb)
    - [Создание базы данных и коллекции](#создание-базы-данных-и-коллекции)
    - [Вставка множества документов в коллекцию](#вставка-множества-документов-в-коллекцию)
    - [MongoDB Find](#mongodb-find)
    - [Find с запросом](#find-с-запросом)
    - [Запрос Find с модификатором](#запрос-find-с-модификатором)
    - [Ограничение числа документов](#ограничение-числа-документов)
    - [Find с сортировкой](#find-с-сортировкой)
    - [Обновление по запросу](#обновление-по-запросу)
    - [Удаление документа](#удаление-документа)
    - [Удаление коллекции](#удаление-коллекции)
  - [💻 Упражнения: День 27](#-упражнения-день-27)

# 📘 День 27

# Python с MongoDB

Python — это бэкенд-технология, и его можно подключать к разным приложениям баз данных. Его можно подключить как к SQL, так и к noSQL базам данных. В этом разделе мы подключим Python к базе данных MongoDB, которая является базой данных noSQL.

## MongoDB

MongoDB — это база данных NoSQL. MongoDB хранит данные в документе, похожем на JSON, что делает MongoDB очень гибкой и масштабируемой. Давайте рассмотрим различные терминологии баз данных SQL и NoSQL. Следующая таблица покажет разницу между базами данных SQL и NoSQL.

### SQL против NoSQL

![SQL против NoSQL](../images/mongoDB/sql-vs-nosql.png)

В этом разделе мы сосредоточимся на базе данных NoSQL MongoDB. Давайте зарегистрируемся на [mongoDB](https://www.mongodb.com/), нажав на кнопку входа, а затем нажмём register на следующей странице.

![Страницы регистрации MongoDB](../images/mongoDB/mongodb-signup-page.png)

Заполните поля и нажмите continue

![Регистрация MongoDB](../images/mongoDB/mongodb-register.png)

Выберите бесплатный план

![Бесплатный план MongoDB](../images/mongoDB/mongodb-free.png)

Выберите ближайший бесплатный регион и дайте любое имя вашему кластеру.

![Имя кластера MongoDB](../images/mongoDB/mongodb-cluster-name.png)

Теперь бесплатная песочница создана

![Песочница MongoDB](../images/mongoDB/mongodb-sandbox.png)

Доступ со всех локальных хостов

![Разрешение доступа по IP в MongoDB](../images/mongoDB/mongodb-allow-ip-access.png)

Добавьте пользователя и пароль

![Добавление пользователя MongoDB](../images/mongoDB/mongodb-add-user.png)

Создайте ссылку uri mongoDB

![Создание uri в MongoDB](../images/mongoDB/mongodb-create-uri.png)

Выберите драйвер Python 3.6 или выше

![Драйвер Python для MongoDB](../images/mongoDB/mongodb-python-driver.png)

### Получение строки подключения (MongoDB URI)

Скопируйте ссылку строки подключения, и вы получите что-то вроде этого:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Не беспокойтесь об url, это средство для подключения вашего приложения к mongoDB.
Давайте заменим заполнитель пароля на пароль, который вы использовали при добавлении пользователя.

**Пример:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Теперь я заменил всё, и пароль — 123123, а имя базы данных — *thirty_days_python*. Это всего лишь пример, ваш пароль должен быть надёжнее, чем пароль из примера.

Python нужен драйвер mongoDB для доступа к базе данных mongoDB. Мы будем использовать _pymongo_ с _dnspython_, чтобы подключить наше приложение к базе данных mongoDB. Внутри каталога проекта установите pymongo и dnspython.

```sh
pip install pymongo dnspython
```

Модуль "dnspython" должен быть установлен для использования URI mongodb+srv://. dnspython — это набор инструментов DNS для Python. Он поддерживает почти все типы записей.

### Подключение приложения Flask к кластеру MongoDB

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

Когда мы запускаем приведённый выше код, мы получаем базы данных mongoDB по умолчанию.

```sh
['admin', 'local']
```

### Создание базы данных и коллекции

Давайте создадим базу данных, база данных и коллекция в mongoDB будут созданы, если их не существует. Давайте создадим базу данных с именем *thirty_days_of_python* и коллекцию *students*.

Чтобы создать базу данных:

```sh
db = client.name_of_databse # мы можем создать базу данных так или вторым способом
db = client['name_of_database']
```

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# Создание базы данных
db = client.thirty_days_of_python
# Создание коллекции students и вставка документа
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

После создания базы данных мы также создали коллекцию students и использовали метод *insert_one()* для вставки документа.
Теперь база данных *thirty_days_of_python* и коллекция *students* созданы, а документ вставлен.
Проверьте ваш кластер mongoDB, и вы увидите и базу данных, и коллекцию. Внутри коллекции будет документ.

```sh
['thirty_days_of_python', 'admin', 'local']
```

Если вы видите это в кластере mongoDB, это значит, что вы успешно создали базу данных и коллекцию.

![Создание базы данных и коллекции](../images/mongoDB/mongodb-creating_database.png)

Если вы посмотрели на рисунок, документ был создан с длинным id, который действует как первичный ключ. Каждый раз, когда мы создаём документ, mongoDB создаёт для него уникальный id.

### Вставка множества документов в коллекцию

Метод *insert_one()* вставляет один элемент за раз, если мы хотим вставить много документов сразу, мы используем метод *insert_many()* или цикл for.
Мы можем использовать цикл for, чтобы вставить много документов сразу.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
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
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### MongoDB Find

Методы *find()* и *findOne()* — это распространённые методы поиска данных в коллекции базы данных mongoDB. Это похоже на оператор SELECT в базе данных MySQL.
Давайте используем метод _find_one()_, чтобы получить документ в коллекции базы данных.

- \*find_one({"\_id": ObjectId("id"}): получает первое вхождение, если id не указан

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
student = db.students.find_one()
print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

Приведённый выше запрос возвращает первую запись, но мы можем нацелиться на конкретный документ, используя конкретный \_id. Давайте сделаем один пример, используем id David, чтобы получить объект David.
'\_id':ObjectId('5df68a23f106fe2d315bbc8c')

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
from bson.objectid import ObjectId # объект id
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

Мы увидели, как использовать _find_one()_ на приведённых выше примерах. Перейдём к _find()_

- _find()_: возвращает все вхождения из коллекции, если мы не передаём объект запроса. Объект — это pymongo.cursor.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
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
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 означает не включать, а 1 означает включать
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### Find с запросом

В mongoDB find принимает объект запроса. Мы можем передать объект запроса и отфильтровать документы так, как нам нужно.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Запрос с модификаторами

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Запрос Find с модификатором

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Запрос с модификаторами

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Ограничение числа документов

Мы можем ограничить число возвращаемых документов с помощью метода _limit()_.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
db.students.find().limit(3)
```

### Find с сортировкой

По умолчанию сортировка идёт по возрастанию. Мы можем изменить сортировку на убывание, добавив параметр -1.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
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
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

По возрастанию

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

По убыванию

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### Обновление по запросу

Мы будем использовать метод *update_one()* для обновления одного элемента. Он принимает два объекта: один — запрос, второй — новый объект.
У первого человека, Asabeneh, очень неправдоподобный возраст. Давайте обновим возраст Asabeneh.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# проверим результат, изменился ли возраст
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
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
Давайте удалим одного John из коллекции.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# проверим результат, изменился ли возраст
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Как видите, John был удалён из коллекции.

Когда мы хотим удалить много документов, мы используем метод *delete_many()*, он принимает объект запроса. Если мы передадим пустой объект запроса в *delete_many({})*, он удалит все документы в коллекции.

### Удаление коллекции

С помощью метода _drop()_ мы можем удалить коллекцию из базы данных.

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
db.students.drop()
```

Теперь мы удалили коллекцию students из базы данных.

## 💻 Упражнения: День 27

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 26](./26_python_web_ru.md) | [День 28 >>](./28_API_ru.md)

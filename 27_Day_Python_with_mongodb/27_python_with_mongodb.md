<div align="center">
  <h1> 30 дней Python: День 27 - Python и MongoDB </h1>
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

[<< День 26](../26_Day_Python_web/26_python_web.md) | [День 28 >>](../28_Day_API/28_API.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 27](#-день-27)
- [Python и MongoDB](#python-и-mongodb)
  - [MongoDB](#mongodb)
    - [SQL против NoSQL](#sql-против-nosql)
    - [Получение строки подключения (MongoDB URI)](#получение-строки-подключения-mongodb-uri)
    - [Подключение Flask-приложения к кластеру MongoDB](#подключение-flask-приложения-к-кластеру-mongodb)
    - [Создание базы данных и коллекции](#создание-базы-данных-и-коллекции)
    - [Вставка нескольких документов в коллекцию](#вставка-нескольких-документов-в-коллекцию)
    - [Поиск данных в MongoDB](#поиск-данных-в-mongodb)
    - [Поиск с использованием запроса](#поиск-с-использованием-запроса)
    - [Поиск с использованием модификатора запроса](#поиск-с-использованием-модификатора-запроса)
    - [Ограничение документов](#ограничение-документов)
    - [Поиск с сортировкой](#поиск-с-сортировкой)
    - [Обновление с использованием запроса](#обновление-с-использованием-запроса)
    - [Удаление документа](#удаление-документа)
    - [Удаление коллекции](#удаление-коллекции)
  - [Упражнения: День 27](#упражнения-день-27)

# 📘 День 27

# Python и MongoDB

Python является технологией для разработки серверной части и может быть связан с различными приложениями баз данных. Он может быть подключен как к реляционным базам данных (SQL), так и к нереляционным базам данных (NoSQL). В данном разделе мы подключаем Python к базе данных MongoDB, которая является NoSQL базой данных.

## MongoDB

MongoDB - это база данных типа NoSQL. MongoDB хранит данные в формате документов, похожих на JSON, что делает ее очень гибкой и масштабируемой. Давайте рассмотрим различные термины SQL и NoSQL баз данных. Следующая таблица покажет различия между базами данных SQL и NoSQL.

### SQL против NoSQL

![SQL против NoSQL](../images/mongoDB/sql-vs-nosql.png)

В этом разделе мы сосредоточимся на базе данных NoSQL MongoDB. Давайте зарегистрируемся на [mongoDB](https://www.mongodb.com/) - для этого нажмите кнопку "Try Free".

![MongoDB Sign up pages](../images/mongoDB/mongodb-signup-page.png)

Заполните поля и нажмите "Продолжить".

![Mongodb register](../images/mongoDB/mongodb-register.png)

Выберите ближайший свободный регион и назначьте любое имя для вашего кластера.

![Mongodb cluster name](../images/mongoDB/mongodb-cluster-name.png)

Бесплатная песочница (sandbox) создана.

![Mongodb sandbox](../images/mongoDB/mongodb-sandbox.png)

Добавьте доступ к локальному хосту в MongoDB.

![Mongodb allow ip access](../images/mongoDB/mongodb-allow-ip-access.png)

Добавьте пользователя и задайте пароль.

![Mongodb add user](../images/mongoDB/mongodb-add-user.png)

Создайте ссылку URI для MongoDB

![Mongodb create uri](../images/mongoDB/mongodb-create-uri.png)

Выберите драйвер для Python версии 3.12 или выше.

![Mongodb python driver](../images/mongoDB/mongodb-python-driver.png)

### Получение строки подключения (MongoDB URI)

Скопируйте ссылку соединения (connection string), и вы получите что-то подобное:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Не беспокойтесь о ссылке (URL), это средство для подключения вашего приложения к MongoDB.
Давайте добавим пароль, который вы использовали при добавлении пользователя.

**Example:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Теперь я заменил все необходимые значения. Пароль - 123123, а имя базы данных - thirty_days_python. Это всего лишь пример, ваш пароль должен быть более надежным, чем этот.

Python нуждается в драйвере MongoDB для доступа к базе данных MongoDB. Мы будем использовать библиотеку _pymongo_ с _dnspython_ для подключения нашего приложения к базе данных MongoDB. Внутри директории вашего проекта установите pymongo и dnspython.

```sh
pip install pymongo dnspython
```

Для использования URI вида mongodb+srv:// необходимо установить модуль "dnspython". Dnspython - это инструментарий DNS для Python, который поддерживает практически все типы записей DNS.

### Подключение Flask-приложения к кластеру MongoDB

```py
# импортируем Flask
from flask import Flask, render_template
import os # импорт модуля операционной системы
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

Когда мы запускаем вышеприведенный код, мы получаем стандартные базы данных MongoDB.

```sh
['admin', 'local']
```

### Создание базы данных и коллекции

Давайте создадим базу данных. Если база данных и коллекция не существуют в MongoDB, то они будут созданы. Давайте создадим базу данных с именем _thirty_days_of_python_ и коллекцию с именем _students_.
Для создания базы данных вы можете использовать следующий код:

```sh
db = client.name_of_databse # Мы можем создать базу данных двумя способами
db = client['name_of_database']
```

```py
# импортируем Flask
from flask import Flask, render_template
import os # импорт модуля операционной системы
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# Создание базы данных
db = client.thirty_days_of_python
# Создание коллекции "students" и добавление документа. 
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # для развертывания мы используем environ
    # чтобы сделать его работающим как для продакшн-среды, так и для разработки
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

После создания базы данных и коллекции "students" мы использовали метод *insert_one()* для вставки документа.

Теперь база данных *thirty_days_of_python* и коллекция *students* были созданы, а документ был вставлен. Проверьте свой кластер MongoDB, и вы увидите как базу данных, так и коллекцию. Внутри коллекции будет находиться вставленный документ.

```sh
['thirty_days_of_python', 'admin', 'local']
```

Если вы видите это в кластере MongoDB, значит, вы успешно создали базу данных и коллекцию.

![Creating database and collection](../images/mongoDB/mongodb-creating_database.png)

На скриншоте видно, что документ был создан с длинным идентификатором, который выступает в качестве первичного ключа. Каждый раз, когда мы создаем документ, MongoDB создает для него уникальный идентификатор.

### Вставка нескольких документов в коллекцию

Метод *insert_one()* вставляет один документ за раз. Если мы хотим вставить несколько документов одновременно, мы можем использовать метод *insert_many()* или цикл for.

Для вставки нескольких документов сразу можно использовать цикл for.

```py
from flask import Flask, render_template
import os
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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Поиск данных в MongoDB

Методы *find()* и *findOne()* являются распространенными способами поиска данных в коллекции базы данных MongoDB. Они аналогичны оператору SELECT в базе данных MySQL.

Давайте воспользуемся методом _find_one()_ для получения документа из коллекции базы данных.

- \*find_one({"\_id": ObjectId("id"}): Если не указан идентификатор, метод find_one() возвращает первое вхождение.

```py
from flask import Flask, render_template
import os
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
student = db.students.find_one()
print(student)


app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

Вышеуказанный запрос возвращает первую запись, но мы также можем выбрать конкретный документ, используя определенный идентификатор \_id. Давайте рассмотрим пример, где мы используем идентификатор David, чтобы получить объект David.
'\_id':ObjectId('5df68a23f106fe2d315bbc8c')

```py
from flask import Flask, render_template
import os
from bson.objectid import ObjectId # идентификатор объекта
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

Мы рассмотрели, как использовать метод _find_one()_ в приведенных выше примерах. Перейдем к методу _find()_.

- Метод _find()_ возвращает все вхождения из коллекции, если мы не передаем объект запроса. Объект, который он возвращает, является объектом типа pymongo.cursor.

```py
from flask import Flask, render_template
import os

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Мы можем указать, какие поля вернуть, передавая второй объект в метод _find({}, {})._ Значение 0 означает, что поле не будет включено в результат, а значение 1 означает, что поле будет включено. Однако мы не можем комбинировать значения 0 и 1 для одного и того же поля, за исключением поля \_id.

```py
from flask import Flask, render_template
import os

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # Значение 0 означает, что поле не будет включено в результат, а значение 1 означает, что поле будет включено.
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### Поиск с использованием запроса

В MongoDB метод find() принимает объект запроса (query object). Мы можем передать этот объект запроса для фильтрации документов, которые мы хотим получить.

```py
from flask import Flask, render_template
import os

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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Запросы с модификаторами

```py
from flask import Flask, render_template
import os
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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Поиск с использованием модификатора запроса

```py
from flask import Flask, render_template
import os
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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Запросы с модификаторами

```py
from flask import Flask, render_template
import os
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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

```py
from flask import Flask, render_template
import os
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

### Ограничение документов

Мы можем ограничить количество возвращаемых документов с помощью метода _limit()_.

```py
from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']
db.students.find().limit(3)
```

### Поиск с сортировкой

По умолчанию сортировка происходит в порялке возрастания. Чтобы изменить сортировку на порядок убывания, можно добавить параметр -1.

```py
from flask import Flask, render_template
import os
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

### Обновление с использованием запроса

Мы будем использовать метод update_one() для обновления одного элемента. Он принимает два объекта: запрос (query) и новый объект (new object).
Предположим, что первый человек, Asabeneh, имеет очень неправдоподобный возраст. Давайте обновим возраст Asabeneh.

```py
from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# давайте проверим результат, чтобы убедиться, что возраст был изменен
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Когда нам нужно обновить несколько документов одновременно, мы используем метод *update_many()*.

### Удаление документа

Метод *delete_one()* удаляет один документ. Он принимает объект запроса в качестве параметра. Этот метод удаляет только первое вхождение документа, удовлетворяющего запросу.
Давайте удалим одного студента по имени John из коллекции.

```py
from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# давайте проверим результат 
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Как вы можете видеть, John был удален из коллекции.

Когда нам нужно удалить несколько документов одновременно, мы используем метод *delete_many()*. Он принимает объект запроса в качестве параметра. Если мы передадим пустой объект запроса *delete_many({})*, то будут удалены все документы в коллекции.

### Удаление коллекции

С помощью метода _drop()_ мы можем удалить коллекцию из базы данных.

```py
from flask import Flask, render_template
import os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # доступ к базе данных
db.students.drop()
```

Теперь мы удалили коллекцию "students" из базы данных.

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 26](../26_Day_Python_web/26_python_web.md) | [День 28 >>](../28_Day_API/28_API.md)
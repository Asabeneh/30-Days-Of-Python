# Reto de 30 días de Python: Día 27 - Python y MongoDB

- [Día 27](#-día-27)
- [Python y MongoDB](#python-y-mongodb)
  - [MongoDB](#mongodb)
    - [Comparación entre SQL y NoSQL](#comparación-entre-sql-y-nosql)
    - [Obtener la cadena de conexión (URI de MongoDB)](#obtener-la-cadena-de-conexión-uri-de-mongodb)
    - [Conectar una aplicación Flask a un clúster de MongoDB](#conectar-una-aplicación-flask-a-un-clúster-de-mongodb)
    - [Crear base de datos y colecciones](#crear-base-de-datos-y-colecciones)
    - [Insertar múltiples documentos en una colección](#insertar-múltiples-documentos-en-una-colección)
    - [Consultas en MongoDB](#consultas-en-mongodb)
    - [Buscar usando una consulta](#buscar-usando-una-consulta)
    - [Buscar con modificadores](#buscar-con-modificadores)
    - [Limitar la cantidad de documentos](#limitar-la-cantidad-de-documentos)
    - [Buscar con ordenamiento](#buscar-con-ordenamiento)
    - [Actualizar usando una consulta](#actualizar-usando-una-consulta)
    - [Eliminar documentos](#eliminar-documentos)
    - [Eliminar una colección](#eliminar-una-colección)
  - [💻 Ejercicio: Día 27](#-ejercicio-día-27)

# 📘 Día 27

# Python y MongoDB

Python es una tecnología backend que puede conectarse a distintas bases de datos. Puede conectarse a bases de datos SQL y NoSQL. En esta sección conectaremos Python con la base de datos MongoDB, que es una base de datos NoSQL.

## MongoDB

MongoDB es una base de datos NoSQL. MongoDB almacena datos en documentos tipo JSON, lo que hace a MongoDB muy flexible y escalable. Veamos la terminología que difiere entre bases de datos SQL y NoSQL. La siguiente tabla mostrará la diferencia entre SQL y NoSQL.

### Comparación entre SQL y NoSQL

![SQL vs NoSQL](../images/mongoDB/sql-vs-nosql.png)

En esta sección nos centraremos en la base de datos NoSQL MongoDB. Regístrate en [MongoDB](https://www.mongodb.com/) haciendo clic en registrarse y luego en la página siguiente confirma el registro.

![Página de registro de MongoDB](../images/mongoDB/mongodb-signup-page.png)

Rellena el formulario y haz clic en continuar..

![Registro MongoDB](../images/mongoDB/mongodb-register.png)

Elige el plan gratuito

![Plan gratuito de MongoDB](../images/mongoDB/mongodb-free.png)

Elige la región gratuita más cercana y ponle un nombre a tu clúster.

![Nombre del clúster de MongoDB](../images/mongoDB/mongodb-cluster-name.png)

Ahora se ha creado un sandbox gratuito

![Sandbox de MongoDB](../images/mongoDB/mongodb-sandbox.png)

Permitir el acceso desde todos los hosts locales

![Permitir acceso IP en MongoDB](../images/mongoDB/mongodb-allow-ip-access.png)

Agregar usuario y contraseña

![Agregar usuario en MongoDB](../images/mongoDB/mongodb-add-user.png)

Crear enlace URI de MongoDB

![Crear URI de MongoDB](../images/mongoDB/mongodb-create-uri.png)

Selecciona el driver para Python 3.6 o superior

![Driver Python para MongoDB](../images/mongoDB/mongodb-python-driver.png)

### Obtener la cadena de conexión (URI de MongoDB)

Copia la cadena de conexión; obtendrás algo similar a esto:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

No te preocupes por esta URL; es la forma de conectar tu aplicación con MongoDB.
Reemplaza el marcador de contraseña con la contraseña que creaste al añadir el usuario.

Ejemplo:

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

En este ejemplo reemplacé todo y la contraseña es 123123123; el nombre de la base de datos es *thirty_days_python*. Esto solo es un ejemplo; tu contraseña debe ser más segura.

Python necesita drivers para acceder a MongoDB. Usaremos _pymongo_ y _dnspython_ para conectar nuestra aplicación con la base de MongoDB. Instala pymongo y dnspython en tu directorio de proyecto:

```sh
pip install pymongo dnspython
```

Para usar el URI mongodb+srv:// debes instalar el módulo "dnspython". dnspython es un paquete de utilidades DNS para Python que soporta prácticamente todos los tipos de registros.

### Conectar una aplicación Flask a un clúster de MongoDB

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Al ejecutar el código anterior obtendremos las bases de datos por defecto de MongoDB.

```sh
['admin', 'local']
```

### Crear base de datos y colecciones

Creemos una base de datos; si la base de datos y la colección no existen en MongoDB, se crearán. Crearemos una base de datos llamada *thirty_days_of_python* y una colección *students*.

Formas de crear la base de datos:

```sh
db = client.name_of_database # podemos crear la base de datos así, o usar la segunda forma
db = client['name_of_database']
```

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# crear la base de datos
db = client.thirty_days_of_python
# crear la colección students e insertar un documento
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Después de crear la base de datos, también creamos la colección students y usamos *insert_one()* para insertar un documento.
Ahora la base de datos *thirty_days_of_python* y la colección *students* han sido creadas y el documento insertado.
Revisa tu clúster MongoDB y verás la base de datos y la colección, con un documento dentro.

```sh
['thirty_days_of_python', 'admin', 'local']
```

Si ves lo anterior en tu clúster, significa que has creado con éxito una base de datos y una colección.

![Crear base de datos y colección](../images/mongoDB/mongodb-creating_database.png)

Si ves la imagen anterior, el documento fue creado con un ID largo como clave primaria. Cada vez que incrustamos un documento, MongoDB le asigna un ID único.

### Insertar múltiples documentos en una colección

*insert_one()* inserta un elemento a la vez; si queremos insertar múltiples documentos de una vez podemos usar *insert_many()* o un bucle for.
Podemos usar un bucle for para insertar varios documentos a la vez.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
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
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Consultas en MongoDB

Los métodos *find()* y *findOne()* son formas comunes de buscar datos en una colección MongoDB. Son similares al SELECT en MySQL.
Usemos _find_one()_ para obtener un documento de la colección.

- *find_one({"_id": ObjectId("id")}): si no se proporciona id, devuelve la primera aparición.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
student = db.students.find_one()
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

La consulta anterior devuelve la primera entrada, pero podemos usar un _id_ específico para ubicar un documento concreto. Por ejemplo, usemos el id de David para obtener el objeto David.
'_id':ObjectId('5df68a23f106fe2d315bbc8c')

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
from bson.objectid import ObjectId # objeto id
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

Hemos visto cómo usar _find_one()_. Veamos ahora _find()_.

- _find()_: si no pasamos un objeto consulta devuelve todas las apariciones en la colección. El resultado es un objeto pymongo.cursor.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Podemos especificar los campos a devolver pasando un segundo objeto a _find({}, {})_. 0 significa excluir, 1 incluir; no se puede mezclar 0 y 1 excepto para _id.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 excluir, 1 incluir
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### Buscar usando una consulta

En MongoDB, find acepta un objeto de consulta. Podemos pasar ese objeto para filtrar los documentos que queremos.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Buscar con modificadores

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Buscar con modificadores (combinados)

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Ejemplos con operadores:

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
query = {"age":{"$lt":30}}
students = db.students.find(query)
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Limitar la cantidad de documentos

Podemos usar el método _limit()_ para restringir el número de documentos devueltos.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
db.students.find().limit(3)
```

### Buscar con ordenamiento

Por defecto el orden es ascendente. Podemos cambiar a descendente pasando -1.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
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
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Ascendente

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Descendente

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### Actualizar usando una consulta

Usaremos *update_one()* para actualizar un documento. Acepta dos objetos: la consulta y el nuevo valor.
La primera persona, Asabeneh, tenía una edad poco razonable. Actualicemos la edad de Asabeneh.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# verifiquemos el resultado para ver si la edad fue modificada
for student in db.students.find():
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Si queremos actualizar varios documentos a la vez usamos *update_many()*.

### Eliminar documentos

El método *delete_one()* elimina un documento. Acepta un objeto consulta y elimina la primera aparición.
Eliminemos a John de la colección.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# verifiquemos el resultado

app = Flask(__name__)
if __name__ == '__main__':
    # en despliegue usamos variables de entorno
    # para que funcione tanto en producción como en desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Como puedes ver, John ha sido eliminado de la colección.

Si queremos eliminar varios documentos usamos *delete_many()* con un objeto consulta. Si pasamos un objeto vacío *delete_many({})* eliminará todos los documentos en la colección.

### Eliminar una colección

Usando el método _drop()_ podemos eliminar una colección de la base de datos.

```py
# importar flask
from flask import Flask, render_template
import os # importar el módulo os
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acceder a la base de datos
db.students.drop()
```

Ahora hemos eliminado la colección students de la base de datos.

## 💻 Ejercicio: Día 27

🎉 ¡Felicidades! 🎉

[<< Día 26](./26_python_web_sp.md) | [Día 28 >>](./28_API_sp.md)
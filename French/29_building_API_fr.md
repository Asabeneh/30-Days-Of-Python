<div align="center">
  <h1> 30 Jours de Python : Jour 29 - Construire une API </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Auteur :
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Deuxième édition : juillet 2021</small>
</sub>

</div>

[<< Jour 28](./28_API_fr.md) | [Jour 30 >>](./30_conclusions_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Jour 29](#jour-29)
- [Construire une API](#construire-une-api)
  - [Structure d'une API](#structure-dune-api)
  - [Récupérer des données avec get](#récupérer-des-données-avec-get)
  - [Obtenir un document par son id](#obtenir-un-document-par-son-id)
  - [Créer des données avec POST](#créer-des-données-avec-post)
  - [Mettre à jour avec PUT](#mettre-à-jour-avec-put)
  - [Supprimer un document avec DELETE](#supprimer-un-document-avec-delete)
- [💻 Exercices : Jour 29](#-exercices-jour-29)

## Jour 29

## Construire une API

Dans cette section, nous couvrirons une API RESTful qui utilise les méthodes de requête HTTP pour GET, PUT, POST et DELETE les données.

Une API RESTful est une interface de programmation d'application qui utilise des requêtes HTTP pour GET, PUT, POST et DELETE les données. Dans les sections précédentes, nous avons appris Python, Flask et MongoDB. Nous utiliserons les connaissances acquises pour développer une API RESTful avec Python Flask et MongoDB. Chaque application qui a une opération CRUD (Create, Read, Update, Delete) a une API pour créer des données, obtenir des données, mettre à jour des données ou supprimer des données d'une base de données.

Le navigateur ne peut gérer que les requêtes GET. Par conséquent, nous devons avoir un outil qui peut nous aider à gérer toutes les méthodes de requête (GET, POST, PUT, DELETE).

Exemples d'API

- API des pays : https://restcountries.eu/rest/v2/all
- API des races de chats : https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/) est un outil très populaire en matière de développement d'API. Donc, si vous voulez faire cette section, vous devez [télécharger Postman](https://www.getpostman.com/). Une alternative à Postman est [Insomnia](https://insomnia.rest/download).

![Postman](../images/postman.png)

### Structure d'une API

Un point d'accès API (endpoint) est une URL qui peut aider à récupérer, créer, mettre à jour ou supprimer une ressource. La structure ressemble à ceci :
Exemple :
https://api.twitter.com/1.1/lists/members.json
Retourne les membres de la liste spécifiée. Les membres des listes privées ne seront affichés que si l'utilisateur authentifié possède la liste spécifiée.
Le nom de l'entreprise suivi de la version, suivi du but de l'API.
Les méthodes :
Méthodes HTTP et URLs

L'API utilise les méthodes HTTP suivantes pour la manipulation des objets :

```sh
GET        Utilisé pour la récupération d'objets
POST       Utilisé pour la création d'objets et les actions sur les objets
PUT        Utilisé pour la mise à jour d'objets
DELETE     Utilisé pour la suppression d'objets
```

Construisons une API qui collecte des informations sur les étudiants de 30DaysOfPython. Nous allons collecter le nom, le pays, la ville, la date de naissance, les compétences et la biographie.

Pour implémenter cette API, nous utiliserons :

- Postman
- Python
- Flask
- MongoDB

### Récupérer des données avec get

Dans cette étape, utilisons des données factices et retournons-les au format json. Pour les retourner en json, nous utiliserons le module json et le module Response.

```py
# importons flask

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
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Lorsque vous faites une requête à l'url http://localhost:5000/api/v1.0/students dans le navigateur, vous obtiendrez ceci :

![Get on browser](../images/get_on_browser.png)

Lorsque vous faites une requête à l'url http://localhost:5000/api/v1.0/students dans le navigateur, vous obtiendrez ceci :

![Get on postman](../images/get_on_postman.png)

Au lieu d'afficher des données factices, connectons l'application Flask avec MongoDB et récupérons les données de la base de données MongoDB.

```py
# importons flask

from flask import Flask,  Response
import json
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

En connectant Flask, nous pouvons récupérer les données de la collection students de la base de données thirty_days_of_python.

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

### Obtenir un document par son id

Nous pouvons accéder à un seul document en utilisant un id, accédons à Asabeneh en utilisant son id.
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# importons flask

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
db = client['thirty_days_of_python'] # accès à la base de données

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
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

### Créer des données avec POST

Nous utilisons la méthode de requête POST pour créer des données.

```py
# importons flask

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
db = client['thirty_days_of_python'] # accès à la base de données

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
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Mettre à jour avec PUT

```py
# importons flask

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
db = client['thirty_days_of_python'] # accès à la base de données

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # ce décorateur crée la route d'accueil
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
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Supprimer un document avec DELETE

```py
# importons flask

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
db = client['thirty_days_of_python'] # accès à la base de données

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # ce décorateur crée la route d'accueil
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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # ce décorateur crée la route d'accueil
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
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## 💻 Exercices : Jour 29

1. Implémentez l'exemple ci-dessus et développez [ceci](https://thirtydayofpython-api.herokuapp.com/)

🎉 FÉLICITATIONS ! 🎉

[<< Jour 28](./28_API_fr.md) | [Jour 30 >>](./30_conclusions_fr.md)

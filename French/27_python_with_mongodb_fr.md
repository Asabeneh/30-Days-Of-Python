<div align="center">
  <h1> 30 Jours de Python : Jour 27 - Python avec MongoDB </h1>
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

[<< Jour 26](./26_python_web_fr.md) | [Jour 28 >>](./28_API_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 27](#-jour-27)
- [Python avec MongoDB](#python-avec-mongodb)
  - [MongoDB](#mongodb)
    - [SQL versus NoSQL](#sql-versus-nosql)
    - [Obtenir la chaîne de connexion (URI MongoDB)](#obtenir-la-chaîne-de-connexion-uri-mongodb)
    - [Connecter l'application Flask au cluster MongoDB](#connecter-lapplication-flask-au-cluster-mongodb)
    - [Créer une base de données et une collection](#créer-une-base-de-données-et-une-collection)
    - [Insérer plusieurs documents dans une collection](#insérer-plusieurs-documents-dans-une-collection)
    - [Trouver avec MongoDB (Find)](#trouver-avec-mongodb-find)
    - [Recherche avec requête](#recherche-avec-requête)
    - [Requête avec modificateur](#requête-avec-modificateur)
    - [Limiter les documents](#limiter-les-documents)
    - [Recherche avec tri](#recherche-avec-tri)
    - [Mise à jour avec requête](#mise-à-jour-avec-requête)
    - [Supprimer un document](#supprimer-un-document)
    - [Supprimer une collection](#supprimer-une-collection)
  - [💻 Exercices : Jour 27](#-exercices-jour-27)

# 📘 Jour 27

# Python avec MongoDB

Python est une technologie back-end et peut être connecté à différentes applications de base de données. Il peut être connecté à la fois aux bases de données SQL et NoSQL. Dans cette section, nous connectons Python avec la base de données MongoDB qui est une base de données NoSQL.

## MongoDB

MongoDB est une base de données NoSQL. MongoDB stocke les données dans un document de type JSON, ce qui rend MongoDB très flexible et scalable. Voyons les différentes terminologies des bases de données SQL et NoSQL. Le tableau suivant montrera la différence entre SQL et NoSQL.

### SQL versus NoSQL

![SQL versus NoSQL](../images/mongoDB/sql-vs-nosql.png)

Dans cette section, nous nous concentrerons sur une base de données NoSQL : MongoDB. Inscrivons-nous sur [mongoDB](https://www.mongodb.com/) en cliquant sur le bouton sign in, puis cliquez sur register sur la page suivante.

![MongoDB Sign up pages](../images/mongoDB/mongodb-signup-page.png)

Remplissez les champs et cliquez sur continue.

![Mongodb register](../images/mongoDB/mongodb-register.png)

Sélectionnez le plan gratuit.

![Mongodb free plan](../images/mongoDB/mongodb-free.png)

Choisissez la région gratuite la plus proche et donnez un nom à votre cluster.

![Mongodb cluster name](../images/mongoDB/mongodb-cluster-name.png)

Maintenant, un sandbox gratuit est créé.

![Mongodb sandbox](../images/mongoDB/mongodb-sandbox.png)

Accès à tous les hôtes locaux.

![Mongodb allow ip access](../images/mongoDB/mongodb-allow-ip-access.png)

Ajoutez un utilisateur et un mot de passe.

![Mongodb add user](../images/mongoDB/mongodb-add-user.png)

Créez un lien URI mongoDB.

![Mongodb create uri](../images/mongoDB/mongodb-create-uri.png)

Sélectionnez le pilote Python 3.6 ou supérieur.

![Mongodb python driver](../images/mongoDB/mongodb-python-driver.png)

### Obtenir la chaîne de connexion (URI MongoDB)

Copiez le lien de la chaîne de connexion et vous obtiendrez quelque chose comme ceci :

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Ne vous inquiétez pas pour l'URL, c'est un moyen de connecter votre application à mongoDB.
Remplaçons le placeholder du mot de passe par le mot de passe que vous avez utilisé pour ajouter un utilisateur.

**Exemple :**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Maintenant, j'ai tout remplacé et le mot de passe est 123123 et le nom de la base de données est *thirty_days_python*. Ceci est juste un exemple, votre mot de passe doit être plus fort que l'exemple.

Python a besoin d'un pilote mongoDB pour accéder à la base de données mongoDB. Nous utiliserons _pymongo_ avec _dnspython_ pour connecter notre application à mongoDB. Dans votre dossier de projet, installez pymongo et dnspython.

```sh
pip install pymongo dnspython
```

Le module "dnspython" doit être installé pour utiliser les URI mongodb+srv://. Dnspython est une boîte à outils DNS pour Python. Il supporte presque tous les types d'enregistrements.

### Connecter l'application Flask au cluster MongoDB

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

Lorsque nous exécutons le code ci-dessus, nous obtenons les bases de données mongoDB par défaut.

```sh
['admin', 'local']
```

### Créer une base de données et une collection

Créons une base de données. La base de données et la collection dans mongoDB seront créées si elles n'existent pas. Créons une base de données nommée *thirty_days_of_python* et une collection *students*.

Pour créer une base de données :

```sh
db = client.nom_de_la_base # nous pouvons créer une base de données comme ceci ou la deuxième façon
db = client['nom_de_la_base']
```

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# Création de la base de données
db = client.thirty_days_of_python
# Création de la collection students et insertion d'un document
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Après avoir créé une base de données, nous avons également créé une collection students et nous avons utilisé la méthode *insert_one()* pour insérer un document.
Maintenant, la base de données *thirty_days_of_python* et la collection *students* ont été créées et le document a été inséré.
Vérifiez votre cluster mongoDB et vous verrez à la fois la base de données et la collection. Dans la collection, il y aura un document.

```sh
['thirty_days_of_python', 'admin', 'local']
```

Si vous voyez ceci sur le cluster mongoDB, cela signifie que vous avez créé avec succès une base de données et une collection.

![Creating database and collection](../images/mongoDB/mongodb-creating_database.png)

Si vous avez vu sur la figure, le document a été créé avec un long identifiant qui sert de clé primaire. Chaque fois que nous créons un document, mongoDB crée un identifiant unique pour celui-ci.

### Insérer plusieurs documents dans une collection

La méthode *insert_one()* insère un élément à la fois. Si nous voulons insérer plusieurs documents à la fois, nous utilisons soit la méthode *insert_many()*, soit une boucle for.
Nous pouvons utiliser une boucle for pour insérer plusieurs documents à la fois.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
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
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Trouver avec MongoDB (Find)

Les méthodes *find()* et *findOne()* sont des méthodes courantes pour trouver des données dans une collection de la base de données mongoDB. C'est similaire à l'instruction SELECT dans une base de données MySQL.
Utilisons la méthode _find_one()_ pour obtenir un document dans une collection de la base de données.

- \*find_one({"\_id": ObjectId("id"}): Obtient la première occurrence si un id n'est pas fourni

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
student = db.students.find_one()
print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

La requête ci-dessus retourne la première entrée, mais nous pouvons cibler un document spécifique en utilisant un \_id spécifique. Faisons un exemple, utilisons l'id de David pour obtenir l'objet David.
'\_id':ObjectId('5df68a23f106fe2d315bbc8c')

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
from bson.objectid import ObjectId # objet id
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

Nous avons vu comment utiliser _find_one()_ avec les exemples ci-dessus. Passons à _find()_.

- _find()_: retourne toutes les occurrences d'une collection si nous ne passons pas d'objet requête. L'objet est un objet curseur pymongo.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Nous pouvons spécifier les champs à retourner en passant un second objet dans _find({}, {})_. 0 signifie ne pas inclure et 1 signifie inclure, mais nous ne pouvons pas mélanger 0 et 1, sauf pour \_id.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 signifie ne pas inclure et 1 signifie inclure
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### Recherche avec requête

Dans mongoDB, find prend un objet requête. Nous pouvons passer un objet requête et filtrer les documents que nous souhaitons.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Requête avec modificateurs

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Requête avec modificateur

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Requête avec modificateurs

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Limiter les documents

Nous pouvons limiter le nombre de documents retournés en utilisant la méthode _limit()_.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
db.students.find().limit(3)
```

### Recherche avec tri

Par défaut, le tri est en ordre croissant. Nous pouvons changer le tri en ordre décroissant en ajoutant le paramètre -1.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
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
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Ordre croissant

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Ordre décroissant

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### Mise à jour avec requête

Nous utiliserons la méthode *update_one()* pour mettre à jour un élément. Elle prend deux objets : un pour la requête et le second pour le nouvel objet.
La première personne, Asabeneh, a un âge très peu plausible. Mettons à jour l'âge d'Asabeneh.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# vérifions le résultat si l'âge a été modifié
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Lorsque nous voulons mettre à jour plusieurs documents à la fois, nous utilisons la méthode *update_many()*.

### Supprimer un document

La méthode *delete_one()* supprime un document. La méthode *delete_one()* prend un objet requête en paramètre. Elle ne supprime que la première occurrence.
Supprimons John de la collection.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# vérifions le résultat si l'âge a été modifié
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Comme vous pouvez le voir, John a été supprimé de la collection.

Lorsque nous voulons supprimer plusieurs documents, nous utilisons la méthode *delete_many()*, qui prend un objet requête. Si nous passons un objet requête vide à *delete_many({})*, cela supprimera tous les documents de la collection.

### Supprimer une collection

En utilisant la méthode _drop()_, nous pouvons supprimer une collection d'une base de données.

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # accès à la base de données
db.students.drop()
```

Maintenant, nous avons supprimé la collection students de la base de données.

## 💻 Exercices : Jour 27

🎉 FÉLICITATIONS ! 🎉

[<< Jour 26](./26_python_web_fr.md) | [Jour 28 >>](./28_API_fr.md)

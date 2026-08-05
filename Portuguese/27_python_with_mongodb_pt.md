<div align="center">
  <h1> 30 Dias de Python: Dia 27 - Python com MongoDB </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Segunda edição: Julho, 2021</small>
</sub>

</div>

[<< Dia 26](./26_python_web_pt.md) | [Dia 28 >>](./28_API_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 27](#-dia-27)
- [Python com MongoDB](#python-com-mongodb)
  - [MongoDB](#mongodb)
    - [SQL versus NoSQL](#sql-versus-nosql)
    - [Obtendo a String de Conexão (URI do MongoDB)](#obtendo-a-string-de-conexão-uri-do-mongodb)
    - [Conectando a aplicação Flask ao Cluster MongoDB](#conectando-a-aplicação-flask-ao-cluster-mongodb)
    - [Criando um banco de dados e uma coleção](#criando-um-banco-de-dados-e-uma-coleção)
    - [Inserindo vários documentos em uma coleção](#inserindo-vários-documentos-em-uma-coleção)
    - [Find no MongoDB](#find-no-mongodb)
    - [Find com Query](#find-com-query)
    - [Query com modificador](#query-com-modificador)
    - [Limitando documentos](#limitando-documentos)
    - [Find com ordenação](#find-com-ordenação)
    - [Update com query](#update-com-query)
    - [Excluindo um documento](#excluindo-um-documento)
    - [Excluindo uma coleção](#excluindo-uma-coleção)
  - [💻 Exercícios: Dia 27](#-exercícios-dia-27)

# 📘 Dia 27

# Python com MongoDB

Python é uma tecnologia de backend e pode ser conectado a diferentes aplicações de banco de dados. Ele pode ser conectado tanto a bancos de dados SQL quanto NoSQL. Nesta seção, vamos conectar o Python com o banco de dados MongoDB, que é um banco de dados NoSQL.

## MongoDB

MongoDB é um banco de dados NoSQL. O MongoDB armazena dados em um documento no estilo JSON, o que torna o MongoDB muito flexível e escalável. Vamos ver as diferentes terminologias dos bancos de dados SQL e NoSQL. A tabela a seguir mostrará a diferença entre bancos de dados SQL e NoSQL.

### SQL versus NoSQL

![SQL versus NoSQL](../images/mongoDB/sql-vs-nosql.png)

Nesta seção, vamos focar em um banco de dados NoSQL, o MongoDB. Vamos nos cadastrar no [mongoDB](https://www.mongodb.com/) clicando no botão sign in e depois clicando em register na próxima página.

![MongoDB Sign up pages](../images/mongoDB/mongodb-signup-page.png)

Complete os campos e clique em continue

![Mongodb register](../images/mongoDB/mongodb-register.png)

Selecione o plano gratuito

![Mongodb free plan](../images/mongoDB/mongodb-free.png)

Escolha a região gratuita mais próxima e dê um nome ao seu cluster.

![Mongodb cluster name](../images/mongoDB/mongodb-cluster-name.png)

Agora, um sandbox gratuito é criado

![Mongodb sandbox](../images/mongoDB/mongodb-sandbox.png)

Acesso a todos os hosts locais

![Mongodb allow ip access](../images/mongoDB/mongodb-allow-ip-access.png)

Adicione um usuário e uma senha

![Mongodb add user](../images/mongoDB/mongodb-add-user.png)

Crie um link URI do mongoDB

![Mongodb create uri](../images/mongoDB/mongodb-create-uri.png)

Selecione o driver Python 3.6 ou superior

![Mongodb python driver](../images/mongoDB/mongodb-python-driver.png)

### Obtendo a String de Conexão (URI do MongoDB)

Copie o link da string de conexão e você obterá algo como isto:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Não se preocupe com a URL, ela é apenas um meio de conectar sua aplicação ao mongoDB.
Vamos substituir o placeholder da senha pela senha que você usou para adicionar um usuário.

**Exemplo:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

Agora, eu substituí tudo e a senha é 123123 e o nome do banco de dados é *thirty_days_python*. Isso é apenas um exemplo, sua senha deve ser mais forte do que a senha de exemplo.

O Python precisa de um driver mongoDB para acessar o banco de dados mongoDB. Usaremos _pymongo_ com _dnspython_ para conectar nossa aplicação com a base mongoDB. Dentro do diretório do seu projeto, instale o pymongo e o dnspython.

```sh
pip install pymongo dnspython
```

O módulo "dnspython" deve ser instalado para usar URIs mongodb+srv://. O dnspython é um toolkit de DNS para Python. Ele suporta quase todos os tipos de registros.

### Conectando a aplicação Flask ao Cluster MongoDB

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

Quando executamos o código acima, obtemos os bancos de dados padrão do mongoDB.

```sh
['admin', 'local']
```

### Criando um banco de dados e uma coleção

Vamos criar um banco de dados; o banco de dados e a coleção no mongoDB serão criados se ainda não existirem. Vamos criar um banco de dados chamado *thirty_days_of_python* e uma coleção *students*.

Para criar um banco de dados:

```sh
db = client.name_of_databse # podemos criar um banco de dados assim ou da segunda forma
db = client['name_of_database']
```

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# Criando o banco de dados
db = client.thirty_days_of_python
# Criando a coleção students e inserindo um documento
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Depois de criar um banco de dados, também criamos uma coleção students e usamos o método *insert_one()* para inserir um documento.
Agora, o banco de dados *thirty_days_of_python* e a coleção *students* foram criados e o documento foi inserido.
Verifique seu cluster mongoDB e você verá tanto o banco de dados quanto a coleção. Dentro da coleção, haverá um documento.

```sh
['thirty_days_of_python', 'admin', 'local']
```

Se você vir isso no cluster mongoDB, significa que você criou com sucesso um banco de dados e uma coleção.

![Creating database and collection](../images/mongoDB/mongodb-creating_database.png)

Se você viu na figura, o documento foi criado com um id longo que atua como chave primária. Toda vez que criamos um documento, o mongoDB cria um id único para ele.

### Inserindo vários documentos em uma coleção

O método *insert_one()* insere um item por vez; se quisermos inserir vários documentos de uma vez, usamos o método *insert_many()* ou um loop for.
Podemos usar um loop for para inserir vários documentos de uma vez.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
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
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### Find no MongoDB

Os métodos *find()* e *findOne()* são métodos comuns para encontrar dados em uma coleção no banco de dados mongoDB. É similar à instrução SELECT em um banco de dados MySQL.
Vamos usar o método _find_one()_ para obter um documento em uma coleção do banco de dados.

- \*find_one({"\_id": ObjectId("id"}): Obtém a primeira ocorrência se um id não for fornecido

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
student = db.students.find_one()
print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

A query acima retorna a primeira entrada, mas podemos direcionar um documento específico usando um \_id específico. Vamos fazer um exemplo, usar o id de David para obter o objeto de David.
'\_id':ObjectId('5df68a23f106fe2d315bbc8c')

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
from bson.objectid import ObjectId # objeto id
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

Vimos como usar _find_one()_ com os exemplos acima. Vamos passar para _find()_

- _find()_: retorna todas as ocorrências de uma coleção se não passarmos um objeto de query. O objeto é um objeto cursor do pymongo.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Podemos especificar quais campos retornar passando um segundo objeto em _find({}, {})_. 0 significa não incluir e 1 significa incluir, mas não podemos misturar 0 e 1, exceto para \_id.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 significa não incluir e 1 significa incluir
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### Find com Query

No mongoDB, find recebe um objeto de query. Podemos passar um objeto de query e filtrar os documentos que quisermos.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Query com modificadores

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Query com modificador

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Query com modificadores

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### Limitando documentos

Podemos limitar o número de documentos retornados usando o método _limit()_.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
db.students.find().limit(3)
```

### Find com ordenação

Por padrão, a ordenação é em ordem crescente. Podemos mudar a ordenação para decrescente adicionando o parâmetro -1.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
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
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Ordem crescente

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Ordem decrescente

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### Update com query

Usaremos o método *update_one()* para atualizar um item. Ele recebe dois objetos, um é a query e o segundo é o novo objeto.
A primeira pessoa, Asabeneh, tem uma idade muito implausível. Vamos atualizar a idade de Asabeneh.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# vamos verificar o resultado se a idade foi modificada
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Quando queremos atualizar vários documentos de uma vez, usamos o método *update_many()*.

### Excluindo um documento

O método *delete_one()* exclui um documento. O *delete_one()* recebe um objeto de query como parâmetro. Ele remove apenas a primeira ocorrência.
Vamos remover um John da coleção.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# vamos verificar o resultado se a idade foi modificada
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

Como você pode ver, John foi removido da coleção.

Quando queremos excluir vários documentos, usamos o método *delete_many()*, que recebe um objeto de query. Se passarmos um objeto de query vazio para *delete_many({})*, ele excluirá todos os documentos da coleção.

### Excluindo uma coleção

Usando o método _drop()_ podemos excluir uma coleção de um banco de dados.

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # acessando o banco de dados
db.students.drop()
```

Agora, excluímos a coleção students do banco de dados.

## 💻 Exercícios: Dia 27

🎉 PARABÉNS ! 🎉

[<< Dia 26](./26_python_web_pt.md) | [Dia 28 >>](./28_API_pt.md)

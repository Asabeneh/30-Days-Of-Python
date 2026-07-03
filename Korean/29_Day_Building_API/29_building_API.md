<div align="center">
  <h1> 30 Days Of Python: Day 29 - Building an API </h1>
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

[<< Day 28](../28_Day_API/28_API.md) | [Day 29 >>](../30_Day_Conclusions/30_conclusions.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [Day 29](#day-29)
- [API 구축하기](#api-구축하기)
  - [API의 구조](#api의-구조)
  - [GET을 사용한 데이터 조회](#get을-사용한-데이터-조회)
  - [ID로 문서 가져오기](#id로-문서-가져오기)
  - [POST를 사용한 데이터 생성](#post를-사용한-데이터-생성)
  - [PUT을 사용한 데이터 수정](#put을-사용한-데이터-수정)
  - [DELETE를 사용한 문서 삭제](#delete를-사용한-문서-삭제)
- [💻 연습문제: Day 29](#-연습문제-day-29)

## Day 29

## API 구축하기


이 섹션에서는 HTTP 요청 메서드를 사용하여 데이터를 GET, PUT, POST 및 DELETE하는 RESTful API를 다룰 것입니다.

RESTful API는 HTTP 요청을 사용하여 데이터를 GET, PUT, POST 및 DELETE하는 애플리케이션 프로그램 인터페이스(API)입니다. 이전 섹션에서 우리는 Python, Flask, MongoDB에 대해 학습했습니다. Python Flask와 MongoDB를 사용하여 RESTful API를 개발하기 위해 습득한 지식을 활용할 것입니다. CRUD(Create, Read, Update, Delete) 작업이 있는 모든 애플리케이션에는 데이터베이스에서 데이터를 생성, 조회, 수정 또는 삭제하기 위한 API가 있습니다.

브라우저는 GET 요청만 처리할 수 있습니다. 따라서 모든 요청 메서드(GET, POST, PUT, DELETE)를 처리하는 데 도움이 되는 도구가 필요합니다.

API 예시

- Countries API: https://restcountries.eu/rest/v2/all
- Cats breed API: https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/)은 API 개발에 있어서 매우 인기 있는 도구입니다. 따라서 이 섹션을 진행하려면 [Postman을 다운로드](https://www.getpostman.com/)해야 합니다. Postman의 대안으로 [Insomnia](https://insomnia.rest/download)가 있습니다.

![Postman](../../images/postman.png)

### API의 구조

API 엔드포인트는 리소스를 조회, 생성, 수정 또는 삭제할 수 있는 URL입니다. 구조는 다음과 같습니다:
예시:
https://api.twitter.com/1.1/lists/members.json
지정된 목록의 멤버를 반환합니다. 비공개 목록 멤버는 인증된 사용자가 지정된 목록을 소유한 경우에만 표시됩니다.
회사 이름 뒤에 버전이 오고 그 뒤에 API의 목적이 옵니다.
메서드:
HTTP 메서드 & URL

API는 객체 조작을 위해 다음과 같은 HTTP 메서드를 사용합니다:

```sh
GET        Used for object retrieval
POST       Used for object creation and object actions
PUT        Used for object update
DELETE     Used for object deletion
```

30DaysOfPython 학생들의 정보를 수집하는 API를 구축해 보겠습니다. 이름, 국가, 도시, 생년월일, 기술 및 자기소개를 수집할 것입니다.

이 API를 구현하기 위해 다음을 사용할 것입니다:

- Postman
- Python
- Flask
- MongoDB

### GET을 사용한 데이터 조회

이 단계에서는 더미 데이터를 사용하여 JSON으로 반환하겠습니다. JSON으로 반환하기 위해 json 모듈과 Response 모듈을 사용할 것입니다.

```py
# flask를 import합니다

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
    # 배포용
    # 프로덕션과 개발 환경 모두에서 작동하도록
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

브라우저에서 http://localhost:5000/api/v1.0/students URL을 요청하면 다음과 같은 결과를 얻을 수 있습니다:

![브라우저에서 GET 요청](../../images/get_on_browser.png)

브라우저에서 http://localhost:5000/api/v1.0/students URL을 요청하면 다음과 같은 결과를 얻을 수 있습니다:

![Postman에서 GET 요청](../../images/get_on_postman.png)

더미 데이터를 표시하는 대신 Flask 애플리케이션을 MongoDB에 연결하고 MongoDB 데이터베이스에서 데이터를 가져오겠습니다.

```py
# flask를 import합니다

from flask import Flask,  Response
import json
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스에 접근

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # 배포용
    # 프로덕션과 개발 환경 모두에서 작동하도록
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Flask를 연결하면 thirty_days_of_python 데이터베이스에서 학생 컬렉션 데이터를 가져올 수 있습니다.

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

### ID로 문서 가져오기

ID를 사용하여 단일 문서에 접근할 수 있습니다. Asabeneh의 ID를 사용하여 접근해 보겠습니다.
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# flask를 import합니다

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
db = client['thirty_days_of_python'] # 데이터베이스에 접근

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # 배포용
    # 프로덕션과 개발 환경 모두에서 작동하도록
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

### POST를 사용한 데이터 생성

POST 요청 메서드를 사용하여 데이터를 생성합니다.

```py
# flask를 import합니다

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
db = client['thirty_days_of_python'] # 데이터베이스에 접근

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
    # 배포용
    # 프로덕션과 개발 환경 모두에서 작동하도록
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### PUT을 사용한 데이터 수정

```py
# flask를 import합니다

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
db = client['thirty_days_of_python'] # 데이터베이스에 접근

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # 이 데코레이터는 홈 라우트를 생성합니다
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
    # 배포용
    # 프로덕션과 개발 환경 모두에서 작동하도록
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### DELETE를 사용한 문서 삭제

```py
# flask를 import합니다

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
db = client['thirty_days_of_python'] # 데이터베이스에 접근

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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # 이 데코레이터는 홈 라우트를 생성합니다
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
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # 이 데코레이터는 홈 라우트를 생성합니다
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
    # 배포용
    # 프로덕션과 개발 환경 모두에서 작동하도록
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## 💻 연습문제: Day 29

1. 위의 예제를 구현하고 [이것](https://thirtydayofpython-api.herokuapp.com/)을 개발해 보세요.

🎉 축하합니다! 🎉

[<< Day 28](../28_Day_API/28_API.md) | [Day 30 >>](../30_Day_Conclusions/30_conclusions.md)

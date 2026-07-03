<div align="center">
  <h1> 30 Days Of Python: Day 27 - Python과 MongoDB </h1>
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

[<< Day 26](../26_Day_Python_web/26_python_web.md) | [Day 28 >>](../28_Day_API/28_API.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 27](#-day-27)
- [Python과 MongoDB](#python과-mongodb)
  - [MongoDB](#mongodb)
    - [SQL과 NoSQL 비교](#sql과-nosql-비교)
    - [연결 문자열(MongoDB URI) 얻기](#연결-문자열mongodb-uri-얻기)
    - [Flask 애플리케이션을 MongoDB 클러스터에 연결하기](#flask-애플리케이션을-mongodb-클러스터에-연결하기)
    - [데이터베이스와 컬렉션 생성하기](#데이터베이스와-컬렉션-생성하기)
    - [컬렉션에 여러 문서 삽입하기](#컬렉션에-여러-문서-삽입하기)
    - [MongoDB Find](#mongodb-find)
    - [쿼리를 사용한 Find](#쿼리를-사용한-find)
    - [수정자를 사용한 Find 쿼리](#수정자를-사용한-find-쿼리)
    - [문서 수 제한하기](#문서-수-제한하기)
    - [정렬을 사용한 Find](#정렬을-사용한-find)
    - [쿼리를 사용한 Update](#쿼리를-사용한-update)
    - [문서 삭제하기](#문서-삭제하기)
    - [컬렉션 삭제하기](#컬렉션-삭제하기)
  - [💻 연습문제: Day 27](#-연습문제-day-27)

# 📘 Day 27

# Python과 MongoDB

Python은 백엔드 기술이며 다양한 데이터베이스 애플리케이션과 연결할 수 있습니다. SQL과 noSQL 데이터베이스 모두에 연결할 수 있습니다. 이 섹션에서는 noSQL 데이터베이스인 MongoDB 데이터베이스에 Python을 연결합니다.

## MongoDB

MongoDB는 NoSQL 데이터베이스입니다. MongoDB는 JSON과 유사한 문서 형태로 데이터를 저장하여 MongoDB를 매우 유연하고 확장 가능하게 만듭니다. SQL과 NoSQL 데이터베이스의 서로 다른 용어들을 살펴보겠습니다. 다음 표는 SQL과 NoSQL 데이터베이스의 차이점을 보여줍니다.

### SQL과 NoSQL 비교

![SQL versus NoSQL](../../images/mongoDB/sql-vs-nosql.png)

이 섹션에서는 NoSQL 데이터베이스인 MongoDB에 초점을 맞추겠습니다. 로그인 버튼을 클릭한 후 다음 페이지에서 등록을 클릭하여 [mongoDB](https://www.mongodb.com/)에 가입해 봅시다.

![MongoDB Sign up pages](../../images/mongoDB/mongodb-signup-page.png)

필드를 작성하고 계속하기를 클릭합니다

![Mongodb register](../../images/mongoDB/mongodb-register.png)

무료 플랜을 선택합니다

![Mongodb free plan](../../images/mongoDB/mongodb-free.png)

가까운 무료 리전을 선택하고 클러스터에 이름을 지정합니다.

![Mongodb cluster name](../../images/mongoDB/mongodb-cluster-name.png)

이제 무료 샌드박스가 생성되었습니다

![Mongodb sandbox](../../images/mongoDB/mongodb-sandbox.png)

모든 로컬호스트 접근 허용

![Mongodb allow ip access](../../images/mongoDB/mongodb-allow-ip-access.png)

사용자와 비밀번호를 추가합니다

![Mongodb add user](../../images/mongoDB/mongodb-add-user.png)

mongoDB uri 링크를 생성합니다

![Mongodb create uri](../../images/mongoDB/mongodb-create-uri.png)

Python 3.6 이상 드라이버를 선택합니다

![Mongodb python driver](../../images/mongoDB/mongodb-python-driver.png)

### 연결 문자열(MongoDB URI) 얻기

연결 문자열 링크를 복사하면 다음과 같은 것을 얻게 됩니다:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

URL에 대해 걱정하지 마세요, 이것은 애플리케이션을 mongoDB에 연결하는 수단입니다.
비밀번호 자리 표시자를 사용자를 추가할 때 사용한 비밀번호로 교체해 봅시다.

**예시:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

이제 모든 것을 교체했고 비밀번호는 123123이며 데이터베이스 이름은 *thirty_days_python*입니다. 이것은 단지 예시일 뿐이며, 여러분의 비밀번호는 예시 비밀번호보다 더 강력해야 합니다.

Python이 MongoDB 데이터베이스에 접근하려면 mongoDB 드라이버가 필요합니다. 우리는 _pymongo_와 _dnspython_을 사용하여 애플리케이션을 mongoDB에 연결할 것입니다. 프로젝트 디렉토리 안에서 pymongo와 dnspython을 설치합니다.

```sh
pip install pymongo dnspython
```

"dnspython" 모듈은 mongodb+srv:// URI를 사용하기 위해 설치해야 합니다. dnspython은 Python용 DNS 도구 키트입니다. 거의 모든 레코드 유형을 지원합니다.

### Flask 애플리케이션을 MongoDB 클러스터에 연결하기

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

위의 코드를 실행하면 기본 mongoDB 데이터베이스를 얻습니다.

```sh
['admin', 'local']
```

### 데이터베이스와 컬렉션 생성하기

데이터베이스를 생성해 봅시다. mongoDB에서 데이터베이스와 컬렉션은 존재하지 않으면 자동으로 생성됩니다. *thirty_days_of_python*이라는 데이터베이스와 *students* 컬렉션을 생성해 봅시다.

데이터베이스를 생성하려면:

```sh
db = client.name_of_databse # 이렇게 데이터베이스를 생성하거나 두 번째 방법을 사용할 수 있습니다
db = client['name_of_database']
```

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# 데이터베이스 생성
db = client.thirty_days_of_python
# students 컬렉션 생성 및 문서 삽입
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

데이터베이스를 생성한 후, students 컬렉션도 생성하고 *insert_one()* 메서드를 사용하여 문서를 삽입했습니다.
이제 *thirty_days_of_python* 데이터베이스와 *students* 컬렉션이 생성되었고 문서가 삽입되었습니다.
mongoDB 클러스터를 확인하면 데이터베이스와 컬렉션을 모두 볼 수 있습니다. 컬렉션 안에는 문서가 있을 것입니다.

```sh
['thirty_days_of_python', 'admin', 'local']
```

mongoDB 클러스터에서 이것을 보면 데이터베이스와 컬렉션을 성공적으로 생성한 것입니다.

![Creating database and collection](../../images/mongoDB/mongodb-creating_database.png)

그림에서 보셨듯이, 문서는 기본 키 역할을 하는 긴 id로 생성되었습니다. 문서를 생성할 때마다 mongoDB는 고유한 id를 생성합니다.

### 컬렉션에 여러 문서 삽입하기

*insert_one()* 메서드는 한 번에 하나의 항목을 삽입합니다. 한 번에 여러 문서를 삽입하려면 *insert_many()* 메서드를 사용하거나 for 루프를 사용합니다.
for 루프를 사용하여 한 번에 여러 문서를 삽입할 수 있습니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
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
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### MongoDB Find

*find()*와 *findOne()* 메서드는 mongoDB 데이터베이스의 컬렉션에서 데이터를 찾는 일반적인 메서드입니다. MySQL 데이터베이스의 SELECT 문과 유사합니다.
_find_one()_ 메서드를 사용하여 데이터베이스 컬렉션에서 문서를 가져와 봅시다.

- \*find_one({"\_id": ObjectId("id"}): id가 제공되지 않으면 첫 번째 항목을 가져옵니다

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
student = db.students.find_one()
print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

위의 쿼리는 첫 번째 항목을 반환하지만, 특정 \_id를 사용하여 특정 문서를 대상으로 할 수 있습니다. 한 가지 예를 해봅시다. David의 id를 사용하여 David 객체를 가져옵니다.
'\_id':ObjectId('5df68a23f106fe2d315bbc8c')

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
from bson.objectid import ObjectId # id 객체
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

위의 예제들을 사용하여 _find_one()_을 어떻게 사용하는지 살펴보았습니다. _find()_로 넘어가 봅시다.

- _find()_: 쿼리 객체를 전달하지 않으면 컬렉션에서 모든 항목을 반환합니다. 객체는 pymongo.cursor 객체입니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

_find({}, {})_에서 두 번째 객체를 전달하여 반환할 필드를 지정할 수 있습니다. 0은 포함하지 않음을 의미하고 1은 포함을 의미하지만, \_id를 제외하고는 0과 1을 혼합할 수 없습니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0은 포함하지 않음, 1은 포함을 의미합니다
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### 쿼리를 사용한 Find

mongoDB에서 find는 쿼리 객체를 받습니다. 쿼리 객체를 전달하여 원하는 문서를 필터링할 수 있습니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

수정자를 사용한 쿼리

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### 수정자를 사용한 Find 쿼리

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

수정자를 사용한 쿼리

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### 문서 수 제한하기

_limit()_ 메서드를 사용하여 반환되는 문서의 수를 제한할 수 있습니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
db.students.find().limit(3)
```

### 정렬을 사용한 Find

기본적으로 정렬은 오름차순입니다. -1 매개변수를 추가하여 정렬을 내림차순으로 변경할 수 있습니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
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
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

오름차순

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

내림차순

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### 쿼리를 사용한 Update

*update_one()* 메서드를 사용하여 하나의 항목을 업데이트합니다. 이 메서드는 두 개의 객체를 받는데, 하나는 쿼리이고 두 번째는 새로운 객체입니다.
첫 번째 사람인 Asabeneh의 나이가 매우 비현실적입니다. Asabeneh의 나이를 업데이트해 봅시다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# 나이가 수정되었는지 결과를 확인합니다
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

한 번에 여러 문서를 업데이트하려면 *update_many()* 메서드를 사용합니다.

### 문서 삭제하기

*delete_one()* 메서드는 하나의 문서를 삭제합니다. *delete_one()*은 쿼리 객체 매개변수를 받습니다. 첫 번째 항목만 제거합니다.
컬렉션에서 John을 제거해 봅시다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# 나이가 수정되었는지 결과를 확인합니다
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

보시다시피 John이 컬렉션에서 제거되었습니다.

여러 문서를 삭제하려면 *delete_many()* 메서드를 사용합니다. 이 메서드는 쿼리 객체를 받습니다. *delete_many({})* 에 빈 쿼리 객체를 전달하면 컬렉션의 모든 문서를 삭제합니다.

### 컬렉션 삭제하기

_drop()_ 메서드를 사용하여 데이터베이스에서 컬렉션을 삭제할 수 있습니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # 데이터베이스 접근
db.students.drop()
```

이제 데이터베이스에서 students 컬렉션을 삭제했습니다.

## 💻 연습문제: Day 27

🎉 축하합니다 ! 🎉

[<< Day 26](../26_Day_Python_web/26_python_web.md) | [Day 28 >>](../28_Day_API/28_API.md)

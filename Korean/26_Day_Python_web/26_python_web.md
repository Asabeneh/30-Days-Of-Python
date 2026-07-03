<div align="center">
  <h1> 30 Days Of Python: Day 26 - Python for web </h1>
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
</div>

[<< Day 25 ](../25_Day_Pandas/25_pandas.md) | [Day 27 >>](../27_Day_Python_with_mongodb/27_python_with_mongodb.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 26](#-day-26)
  - [웹을 위한 Python](#웹을-위한-python)
    - [Flask](#flask)
      - [폴더 구조](#폴더-구조)
    - [프로젝트 디렉토리 설정하기](#프로젝트-디렉토리-설정하기)
    - [라우트 생성하기](#라우트-생성하기)
    - [템플릿 생성하기](#템플릿-생성하기)
    - [Python 스크립트](#python-스크립트)
    - [내비게이션](#내비게이션)
    - [레이아웃 생성하기](#레이아웃-생성하기)
      - [정적 파일 제공하기](#정적-파일-제공하기)
    - [배포](#배포)
      - [Heroku 계정 생성하기](#heroku-계정-생성하기)
      - [Heroku 로그인](#heroku-로그인)
      - [requirements와 Procfile 생성하기](#requirements와-procfile-생성하기)
      - [프로젝트를 Heroku에 푸시하기](#프로젝트를-heroku에-푸시하기)
  - [연습 문제: Day 26](#연습-문제-day-26)

# 📘 Day 26

## 웹을 위한 Python

Python은 범용 프로그래밍 언어이며 다양한 분야에서 사용할 수 있습니다. 이 섹션에서는 Python을 웹에서 어떻게 사용하는지 살펴보겠습니다. Python 웹 프레임워크는 많이 있습니다. Django와 Flask가 가장 인기 있는 프레임워크입니다. 오늘은 웹 개발을 위해 Flask를 어떻게 사용하는지 알아보겠습니다.

### Flask

Flask는 Python으로 작성된 웹 개발 프레임워크입니다. Flask는 Jinja2 템플릿 엔진을 사용합니다. Flask는 React와 같은 다른 최신 프론트엔드 라이브러리와 함께 사용할 수도 있습니다.

아직 virtualenv 패키지를 설치하지 않았다면 먼저 설치하세요. 가상 환경을 사용하면 프로젝트 의존성을 로컬 머신의 의존성과 분리할 수 있습니다.

#### 폴더 구조

모든 단계를 완료한 후, 프로젝트 파일 구조는 다음과 같아야 합니다:

```sh

├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html
```

### 프로젝트 디렉토리 설정하기

Flask를 시작하려면 다음 단계를 따르세요.

Step 1: 다음 명령어를 사용하여 virtualenv를 설치합니다.

```sh
pip install virtualenv
```

Step 2:

```sh
asabeneh@Asabeneh:~/Desktop$ mkdir python_for_web
asabeneh@Asabeneh:~/Desktop$ cd python_for_web/
asabeneh@Asabeneh:~/Desktop/python_for_web$ virtualenv venv
asabeneh@Asabeneh:~/Desktop/python_for_web$ source venv/bin/activate
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip install Flask
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$
```

python_for_web이라는 프로젝트 디렉토리를 생성했습니다. 프로젝트 내부에 *venv*라는 가상 환경을 생성했는데, 이름은 아무거나 가능하지만 저는 _venv_로 부르는 것을 선호합니다. 그런 다음 가상 환경을 활성화했습니다. pip freeze를 사용하여 프로젝트 디렉토리에 설치된 패키지를 확인했습니다. 아직 패키지가 설치되지 않았기 때문에 pip freeze의 결과는 비어 있었습니다.

이제 프로젝트 디렉토리에 app.py 파일을 만들고 다음 코드를 작성해 봅시다. app.py 파일이 프로젝트의 메인 파일이 됩니다. 다음 코드에는 flask 모듈과 os 모듈이 포함되어 있습니다.

### 라우트 생성하기

홈 라우트입니다.

```py
# flask를 임포트합니다
from flask import Flask
import os # 운영 체제 모듈 임포트

app = Flask(__name__)

@app.route('/') # 이 데코레이터가 홈 라우트를 생성합니다
def home ():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Flask 애플리케이션을 실행하려면, Flask 애플리케이션의 메인 디렉토리에서 python app.py를 입력하세요.

_python app.py_를 실행한 후 로컬 호스트 5000번 포트를 확인하세요.

추가 라우트를 만들어 봅시다.
about 라우트를 생성합니다.

```py
# flask를 임포트합니다
from flask import Flask
import os # 운영 체제 모듈 임포트

app = Flask(__name__)

@app.route('/') # 이 데코레이터가 홈 라우트를 생성합니다
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

위 코드에서 about 라우트를 추가했습니다. 문자열 대신 HTML 파일을 렌더링하고 싶다면 어떻게 해야 할까요? *render_template* 함수를 사용하면 HTML 파일을 렌더링할 수 있습니다. 프로젝트 디렉토리에 templates라는 폴더를 만들고 그 안에 home.html과 about.html을 생성합시다. 또한 flask에서 *render_template* 함수를 임포트합시다.

### 템플릿 생성하기

templates 폴더 안에 HTML 파일을 생성합니다.

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
  </head>

  <body>
    <h1>Welcome Home</h1>
  </body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About</title>
  </head>

  <body>
    <h1>About Us</h1>
  </body>
</html>
```

### Python 스크립트

app.py

```py
# flask를 임포트합니다
from flask import Flask, render_template
import os # 운영 체제 모듈 임포트

app = Flask(__name__)

@app.route('/') # 이 데코레이터가 홈 라우트를 생성합니다
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # 배포를 위해 environ을 사용합니다
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

보시다시피, 다른 페이지로 이동하거나 내비게이션하려면 내비게이션이 필요합니다. 각 페이지에 링크를 추가하거나, 모든 페이지에서 사용할 레이아웃을 만들어 봅시다.

### 내비게이션

```html
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
```

이제 위의 링크를 사용하여 페이지 간 이동이 가능합니다. 폼 데이터를 처리하는 추가 페이지를 만들어 봅시다. 아무 이름이나 지을 수 있지만, 저는 post.html이라고 부르는 것을 좋아합니다.

Jinja2 템플릿 엔진을 사용하여 HTML 파일에 데이터를 주입할 수 있습니다.

```py
# flask를 임포트합니다
from flask import Flask, render_template, request, redirect, url_for
import os # 운영 체제 모듈 임포트

app = Flask(__name__)

@app.route('/') # 이 데코레이터가 홈 라우트를 생성합니다
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post')
def post():
    name = 'Text Analyzer'
    return render_template('post.html', name = name, title = name)


if __name__ == '__main__':
    # 배포를 위해
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

템플릿도 살펴봅시다:

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
  </head>

  <body>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
    <h1>Welcome to {{name}}</h1>
     <ul>
    {% for tech in techs %}
      <li>{{tech}}</li>
    {% endfor %}
    </ul>
  </body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About Us</title>
  </head>

  <body>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
    <h1>About Us</h1>
    <h2>{{name}}</h2>
  </body>
</html>
```

### 레이아웃 생성하기

템플릿 파일에는 반복되는 코드가 많습니다. 레이아웃을 작성하면 반복을 제거할 수 있습니다. templates 폴더 안에 layout.html을 생성합시다.
레이아웃을 생성한 후 모든 파일에 임포트할 것입니다.

#### 정적 파일 제공하기

프로젝트 디렉토리에 static 폴더를 생성합니다. static 폴더 안에 CSS 또는 styles 폴더를 만들고 CSS 스타일시트를 생성합니다. 정적 파일을 제공하기 위해 *url_for* 모듈을 사용합니다.

layout.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://fonts.googleapis.com/css?family=Lato:300,400|Nunito:300,400|Raleway:300,400,500&display=swap"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/main.css') }}"
    />
    {% if title %}
    <title>30 Days of Python - {{ title}}</title>
    {% else %}
    <title>30 Days of Python</title>
    {% endif %}
  </head>

  <body>
    <header>
      <div class="menu-container">
        <div>
          <a class="brand-name nav-link" href="/">30DaysOfPython</a>
        </div>
        <ul class="nav-lists">
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('home') }}">Home</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('about') }}">About</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('post') }}"
              >Text Analyzer</a
            >
          </li>
        </ul>
      </div>
    </header>
    <main>
      {% block content %} {% endblock %}
    </main>
  </body>
</html>
```

이제 다른 템플릿 파일에서 모든 반복 코드를 제거하고 layout.html을 임포트합시다. href는 각 내비게이션 라우트를 연결하기 위해 라우트 함수의 이름과 함께 _url_for_ 함수를 사용합니다.

home.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>Welcome to {{name}}</h1>
  <p>
    This application clean texts and analyse the number of word, characters and
    most frequent words in the text. Check it out by click text analyzer at the
    menu. You need the following technologies to build this web application:
  </p>
  <ul class="tech-lists">
    {% for tech in techs %}
    <li class="tech">{{tech}}</li>

    {% endfor %}
  </ul>
</div>

{% endblock %}
```

about.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>About {{name}}</h1>
  <p>
    This is a 30 days of python programming challenge. If you have been coding
    this far, you are awesome. Congratulations for the job well done!
  </p>
</div>
{% endblock %}
```

post.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>Text Analyzer</h1>
  <form action="https://thirtydaysofpython-v1.herokuapp.com/post" method="POST">
    <div>
      <textarea rows="25" name="content" autofocus></textarea>
    </div>
    <div>
      <input type="submit" class="btn" value="Process Text" />
    </div>
  </form>
</div>

{% endblock %}
```

요청 메서드에는 여러 가지가 있으며, GET, POST, PUT, DELETE가 CRUD(Create, Read, Update, Delete) 작업을 수행할 수 있게 해주는 일반적인 요청 메서드입니다.

post 라우트에서는 요청 유형에 따라 GET과 POST 메서드를 번갈아 사용합니다. 아래 코드에서 어떻게 보이는지 확인하세요. request 메서드는 요청 메서드를 처리하고 폼 데이터에 접근하는 함수입니다.
app.py

```py
# flask를 임포트합니다
from flask import Flask, render_template, request, redirect, url_for
import os # 운영 체제 모듈 임포트

app = Flask(__name__)
# 정적 파일 캐싱을 중지합니다
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') # 이 데코레이터가 홈 라우트를 생성합니다
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    # 배포를 위해
    # 프로덕션과 개발 환경 모두에서 작동하도록 합니다
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

지금까지 템플릿 사용 방법, 템플릿에 데이터를 주입하는 방법, 공통 레이아웃을 만드는 방법을 살펴보았습니다.
이제 정적 파일을 처리해 봅시다. 프로젝트 디렉토리에 static이라는 폴더를 만들고 그 안에 css라는 폴더를 생성합니다. css 폴더 안에 main.css를 만듭니다. main.css 파일은 layout.html에 연결됩니다.

CSS 파일을 직접 작성할 필요 없이, 복사해서 사용하세요. 이제 배포로 넘어가겠습니다.

### 배포

#### Heroku 계정 생성하기

Heroku는 프론트엔드와 풀스택 애플리케이션 모두를 위한 무료 배포 서비스를 제공합니다. [heroku](https://www.heroku.com/)에서 계정을 생성하고, 사용하는 컴퓨터에 맞는 heroku [CLI](https://devcenter.heroku.com/articles/heroku-cli)를 설치하세요.
heroku를 설치한 후 다음 명령어를 입력하세요.

#### Heroku 로그인

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

키보드에서 아무 키나 눌러 결과를 확인해 봅시다. 키보드에서 아무 키나 누르면 heroku 로그인 페이지가 열리고, 로그인 페이지를 클릭합니다. 그러면 로컬 머신이 원격 heroku 서버에 연결됩니다. 원격 서버에 연결되면 다음과 같이 표시됩니다.

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

#### requirements와 Procfile 생성하기

코드를 원격 서버에 푸시하기 전에 다음이 필요합니다.

- requirements.txt
- Procfile

```sh
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch requirements.txt
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze > requirements.txt
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ cat requirements.txt
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch Procfile
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ ls
Procfile          env/              static/
app.py            requirements.txt  templates/
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$
```

Procfile에는 웹 서버에서 애플리케이션을 실행하는 명령어가 들어 있으며, 여기서는 Heroku에서 실행합니다.

```sh
web: python app.py
```

#### 프로젝트를 Heroku에 푸시하기

이제 배포할 준비가 되었습니다. Heroku에 애플리케이션을 배포하는 단계는 다음과 같습니다.

1. git init
2. git add .
3. git commit -m "commit message"
4. heroku create '앱 이름을 한 단어로'
5. git push heroku master
6. heroku open (배포된 애플리케이션을 실행하기 위해)

이 단계를 완료하면 [이것](http://thirdaysofpython-practice.herokuapp.com/)과 같은 애플리케이션을 얻게 됩니다.

## 연습 문제: Day 26

1. [이 애플리케이션](https://thirtydaysofpython-v1-final.herokuapp.com/)을 만들어 보세요. 텍스트 분석기 부분만 남아 있습니다.


🎉 축하합니다 ! 🎉

[<< Day 25 ](../25_Day_Pandas/25_pandas.md) | [Day 27 >>](../27_Day_Python_with_mongodb/27_python_with_mongodb.md)

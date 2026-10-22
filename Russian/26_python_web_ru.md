<div align="center">
  <h1> 30 Days Of Python: День 26 - Python для веб </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Автор:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>Второе издание: июль 2021</small>
  </sub>
</div>
</div>

[<< День 25 ](./25_pandas_ru.md) | [День 27 >>](./27_python_with_mongodb_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 26](#-день-26)
  - [Python для веба](#python-для-веба)
    - [Flask](#flask)
      - [Структура папок](#структура-папок)
    - [Настройка каталога проекта](#настройка-каталога-проекта)
    - [Создание маршрутов](#создание-маршрутов)
    - [Создание шаблонов](#создание-шаблонов)
    - [Python-скрипт](#python-скрипт)
    - [Навигация](#навигация)
    - [Создание макета](#создание-макета)
      - [Отдача статических файлов](#отдача-статических-файлов)
    - [Развёртывание](#развёртывание)
      - [Создание аккаунта Heroku](#создание-аккаунта-heroku)
      - [Вход в Heroku](#вход-в-heroku)
      - [Создание requirements и Procfile](#создание-requirements-и-procfile)
      - [Отправка проекта на Heroku](#отправка-проекта-на-heroku)
  - [Упражнения: День 26](#упражнения-день-26)

# 📘 День 26

## Python для веба

Python — это язык программирования общего назначения, и его можно применять во многих местах. В этом разделе мы увидим, как используем Python для веба. Существует много Python веб-фреймворков. Django и Flask — самые популярные из них. Сегодня мы увидим, как использовать Flask для веб-разработки.

### Flask

Flask — это веб-фреймворк, написанный на Python. Flask использует шаблонизатор Jinja2. Flask также можно использовать с другими современными фронтенд-библиотеками, такими как React.

Если вы ещё не установили пакет virtualenv, сначала установите его. Виртуальное окружение позволит изолировать зависимости проекта от зависимостей локальной машины.

#### Структура папок

После выполнения всех шагов структура файлов вашего проекта должна выглядеть так:

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

### Настройка каталога проекта

Выполните следующие шаги, чтобы начать работу с Flask.

Шаг 1: установите virtualenv с помощью следующей команды.

```sh
pip install virtualenv
```

Шаг 2:

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

Мы создали каталог проекта с именем python_for_web. Внутри проекта мы создали виртуальное окружение *venv*, которое может называться как угодно, но я предпочитаю называть его _venv_. Затем мы активировали виртуальное окружение. Мы использовали pip freeze, чтобы проверить установленные пакеты в каталоге проекта. Результат pip freeze был пустым, потому что пакет ещё не был установлен.

Теперь давайте создадим файл app.py в каталоге проекта и напишем следующий код. Файл app.py будет главным файлом в проекте. В следующем коде есть модуль flask и модуль os.

### Создание маршрутов

Маршрут главной страницы.

```py
# импортируем flask
from flask import Flask
import os # импортируем модуль операционной системы

app = Flask(__name__)

@app.route('/') # этот декоратор создаёт маршрут главной страницы
def home ():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Чтобы запустить приложение flask, напишите python app.py в главном каталоге приложения flask.

После запуска _python app.py_ проверьте локальный хост 5000.

Давайте добавим дополнительный маршрут.
Создание маршрута about

```py
# импортируем flask
from flask import Flask
import os # импортируем модуль операционной системы

app = Flask(__name__)

@app.route('/') # этот декоратор создаёт маршрут главной страницы
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Теперь мы добавили маршрут about в приведённом выше коде. А что, если мы хотим отрендерить HTML-файл вместо строки? Отрендерить HTML-файл можно с помощью функции *render_template*. Давайте создадим папку с именем templates и создадим в каталоге проекта home.html и about.html. Также импортируем функцию *render_template* из flask.

### Создание шаблонов

Создайте HTML-файлы внутри папки templates.

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

### Python-скрипт

app.py

```py
# импортируем flask
from flask import Flask, render_template
import os # импортируем модуль операционной системы

app = Flask(__name__)

@app.route('/') # этот декоратор создаёт маршрут главной страницы
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # для развёртывания мы используем environ
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Как видите, чтобы переходить на разные страницы, нужна навигация. Давайте добавим ссылку на каждую страницу или создадим макет, который будем использовать на каждой странице.

### Навигация

```html
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
```

Теперь мы можем переходить между страницами по приведённой выше ссылке. Давайте создадим дополнительную страницу, которая обрабатывает данные формы. Вы можете назвать её как угодно, мне нравится называть её post.html.

Мы можем внедрять данные в HTML-файлы с помощью шаблонизатора Jinja2.

```py
# импортируем flask
from flask import Flask, render_template, request, redirect, url_for
import os # импортируем модуль операционной системы

app = Flask(__name__)

@app.route('/') # этот декоратор создаёт маршрут главной страницы
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
    # для развёртывания
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Давайте посмотрим и на шаблоны:

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

### Создание макета

В файлах шаблонов много повторяющегося кода, мы можем написать макет и убрать повторения. Давайте создадим layout.html внутри папки templates.
После создания макета мы импортируем его в каждый файл.

#### Отдача статических файлов

Создайте папку static в каталоге проекта. Внутри папки static создайте папку CSS или styles и создайте таблицу стилей CSS. Мы используем модуль *url_for*, чтобы отдавать статический файл.

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

Теперь давайте удалим весь повторяющийся код в других файлах шаблонов и импортируем layout.html. В href используется функция _url_for_ с именем функции маршрута, чтобы связать каждый маршрут навигации.

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

Методы запросов. Существуют разные методы запросов (GET, POST, PUT, DELETE) — это распространённые методы запросов, которые позволяют выполнять операции CRUD (Create, Read, Update, Delete).

В маршруте post мы будем использовать методы GET и POST в зависимости от типа запроса, посмотрите, как это выглядит в коде ниже. Метод запроса — это функция для обработки методов запросов, а также для доступа к данным формы.
app.py

```py
# импортируем flask
from flask import Flask, render_template, request, redirect, url_for
import os # импортируем модуль операционной системы

app = Flask(__name__)
# чтобы остановить кеширование статического файла
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') # этот декоратор создаёт маршрут главной страницы
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
    # для развёртывания
    # чтобы это работало и в продакшене, и при разработке
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Пока что мы увидели, как использовать шаблон и как внедрять данные в шаблон, как сделать общий макет.
Теперь давайте займёмся статическим файлом. Создайте папку с именем static в каталоге проекта и создайте папку с именем css. Внутри папки css создайте main.css. Ваш файл main.css будет связан с layout.html.

Вам не нужно писать файл css, скопируйте и используйте его. Перейдём к развёртыванию.

### Развёртывание

#### Создание аккаунта Heroku

Heroku предоставляет бесплатный сервис развёртывания как для фронтенд-, так и для fullstack-приложений. Создайте аккаунт на [heroku](https://www.heroku.com/) и установите heroku [CLI](https://devcenter.heroku.com/articles/heroku-cli) для вашей машины.
После установки heroku напишите следующую команду

#### Вход в Heroku

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

Давайте посмотрим на результат, нажав любую клавишу на клавиатуре. Когда вы нажмёте любую клавишу на клавиатуре, откроется страница входа heroku, и нажмите на странице входа. Затем ваша локальная машина будет подключена к удалённому серверу heroku. Если вы подключены к удалённому серверу, вы увидите это.

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

#### Создание requirements и Procfile

Прежде чем отправить наш код на удалённый сервер, нам нужны requirements

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

В Procfile будет команда, которая запускает приложение на веб-сервере, в нашем случае на Heroku.

```sh
web: python app.py
```

#### Отправка проекта на Heroku

Теперь всё готово к развёртыванию. Шаги для развёртывания приложения на heroku

1. git init
2. git add .
3. git commit -m "commit message"
4. heroku create 'name of the app as one word'
5. git push heroku master
6. heroku open(чтобы запустить развёрнутое приложение)

После этого шага вы получите приложение, как [здесь](http://thirdaysofpython-practice.herokuapp.com/)

## Упражнения: День 26

1. Вы построите [это приложение](https://thirtydaysofpython-v1-final.herokuapp.com/). Осталась только часть с анализатором текста


🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 25 ](./25_pandas_ru.md) | [День 27 >>](./27_python_with_mongodb_ru.md)

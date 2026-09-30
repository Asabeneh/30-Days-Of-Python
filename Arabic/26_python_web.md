<div align="center">
  <h1> 30 يوماً من بايثون: اليوم 26 - بايثون للويب </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>المؤلف:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">أسابينيه يتاييه</a><br>
  <small>الطبعة الثانية: يوليو، 2021</small>
  </sub>
</div>
</div>

[<< اليوم 25](./25_pandas.md) | [اليوم 27 >>](./27_python_with_mongodb.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 26](#-day-26)
  - [بايثون للويب](#python-for-web)
    - [Flask](#flask)
      - [هيكل المجلدات](#folder-structure)
    - [إعداد مجلد المشروع](#setting-up-your-project-directory)
    - [إنشاء المسارات](#creating-routes)
    - [إنشاء القوالب](#creating-templates)
    - [سكربت بايثون](#python-script)
    - [التنقل](#navigation)
    - [إنشاء تخطيط](#creating-a-layout)
      - [تقديم ملفات ثابتة](#serving-static-file)
    - [النشر](#deployment)
      - [إنشاء حساب Heroku](#creating-heroku-account)
      - [تسجيل الدخول إلى Heroku](#login-to-heroku)
      - [إنشاء ملفات 'requirements' و 'Procfile'](#create-requirements-and-procfile)
      - [دفع المشروع إلى Heroku](#pushing-project-to-heroku)
  - [تمارين: اليوم 26](#exercises-day-26)

# 📘 اليوم 26

## بايثون للويب

بايثون هي لغة برمجة متعددة الاستخدامات ويمكن استخدامها في العديد من المجالات. في هذا القسم، سنرى كيف نستخدم بايثون للويب. توجد العديد من أطر عمل بايثون للويب. 'Django' و 'Flask' هما الأكثر شيوعاً. اليوم سنرى كيفية استخدام 'Flask' لتطوير الويب.

### Flask

'Flask' هو إطار عمل لتطوير الويب مكتوب بلغة بايثون. يستخدم 'Flask' محرك قوالب 'Jinja2'. يمكن أيضًا استخدام 'Flask' مع مكتبات الواجهة الأمامية الحديثة الأخرى مثل 'React'.

إذا لم تقم بتثبيت حزمة 'virtualenv' بعد، قم بتثبيتها أولاً. ستيح لك 'البيئة الافتراضية' عزل تبعيات المشروع عن تبعيات الجهاز المحلي.

#### هيكل المجلدات

بعد إكمال جميع الخطوات، يجب أن يبدو هيكل ملفات مشروعك هكذا:

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

### إعداد مجلد المشروع

اتبع الخطوات التالية للبدء في العمل مع 'Flask'.

الخطوة 1: قم بتثبيت 'virtualenv' باستخدام الأمر التالي.

```sh
pip install virtualenv
```

الخطوة 2:

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

أنشأنا مجلد مشروع باسم 'python_for_web'. داخل المشروع أنشأنا بيئة افتراضية '*venv*' يمكن أن يكون لها أي اسم ولكنني أفضّل تسميتها '_venv_'. ثم قمنا بتفعيل البيئة الافتراضية. استخدمنا 'pip freeze' للتحقق من الحزم المثبتة في مجلد المشروع. كانت نتيجة 'pip freeze' فارغة لأن الحزمة لم تُثبَّت بعد.

الآن، دعنا ننشئ ملف 'app.py' في مجلد المشروع ونكتب الكود التالي. سيكون ملف 'app.py' الملف الرئيسي في المشروع. يحتوي الكود التالي على وحدة 'flask' ووحدة 'os'.

### إنشاء المسارات

مسار الصفحة الرئيسية.

```py
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

لتشغيل تطبيق 'Flask'، اكتب 'python app.py' في المجلد الرئيسي لتطبيق 'Flask'.

بعد تشغيل '_python app.py_' تحقق من 'local host' على المنفذ 5000.

دعنا نضيف مساراً إضافياً.
إنشاء مسار 'about'

```py
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

الآن، أضفنا مسار 'about' في الكود أعلاه. ماذا لو أردنا عرض ملف 'HTML' بدلاً من نص؟ من الممكن عرض ملف 'HTML' باستخدام الدالة '*render_template*'. دعنا ننشئ مجلداً يسمى 'templates' وننشئ ملفات 'home.html' و 'about.html' في مجلد المشروع. دعنا أيضاً نستورد الدالة '*render_template*' من 'flask'.

### إنشاء القوالب

أنشئ ملفات 'HTML' داخل مجلد 'templates'.

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

### سكربت بايثون

app.py

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

كما ترى، للانتقال بين الصفحات أو للتنقل نحتاج إلى شريط تنقل. دعنا نضيف رابطاً لكل صفحة أو دعنا ننشئ تخطيطاً نستخدمه لكل صفحة.

### التنقل

```html
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
```

الآن، يمكننا التنقل بين الصفحات باستخدام الرابط أعلاه. دعنا ننشئ صفحة إضافية تتعامل مع بيانات النماذج. يمكنك تسميتها بأي اسم، أحب تسميتها 'post.html'.

يمكننا حقن البيانات في ملفات 'HTML' باستخدام محرك قوالب 'Jinja2'.

```py
# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
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
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

دعنا نرى القوالب أيضاً:

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

### إنشاء تخطيط

في ملفات القالب، هناك الكثير من الكود المكرر، يمكننا كتابة تخطيط وإزالة التكرار. دعنا ننشئ 'layout.html' داخل مجلد 'templates'.
بعد إنشاء التخطيط سنستورده لكل ملف.

#### تقديم ملفات ثابتة

أنشئ مجلداً يسمى 'static' في مجلد مشروعك. داخل مجلد 'static' أنشئ مجلد 'CSS' أو 'styles' وأنشئ ملف 'CSS'. نستخدم وحدة '*url_for*' لتقديم الملفات الثابتة.

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

الآن، دعنا نزيل جميع أكواد المكررة في ملفات القوالب الأخرى ونستورد 'layout.html'. يستخدم '_href_' الدالة '_url_for_' مع اسم دالة المسار لربط كل مسار تنقل.

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

طرق الطلبات، توجد طرق طلب مختلفة مثل 'GET' و 'POST' و 'PUT' و 'DELETE' وهي طرق الطلبات الشائعة التي تتيح لنا تنفيذ عمليات 'CRUD' ('Create'، 'Read'، 'Update'، 'Delete').

في مسار 'post' سنستخدم طريقة 'GET' و 'POST' بالتناوب حسب نوع الطلب، تحقق من كيف يبدو ذلك في الكود أدناه. طريقة 'request' هي دالة للتعامل مع طرق الطلبات والوصول أيضاً إلى بيانات النماذج.
app.py

```py
# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') # this decorator create the home route
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
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

حتى الآن، رأينا كيفية استخدام القوالب وحقن البيانات فيها وكيفية إنشاء تخطيط مشترك.
الآن، دعنا نتعامل مع الملفات الثابتة. أنشئ مجلداً يسمى 'static' في مجلد المشروع وأنشئ مجلداً يسمى 'css'. داخل مجلد 'css' أنشئ ملف 'main.css'. سيتم ربط ملف 'main.css' بملف 'layout.html'.

لا يجب عليك كتابة ملف 'CSS'، قم بالنسخ والاستخدام. لننتقل إلى النشر.

### النشر

#### إنشاء حساب Heroku

يوفر 'Heroku' خدمة نشر مجانية لتطبيقات الواجهة الأمامية والتطبيقات الكاملة. أنشئ حساباً على [heroku](https://www.heroku.com/) وقم بتثبيت أداة سطر أوامر [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) لجهازك.
بعد تثبيت 'heroku' اكتب الأمر التالي

#### تسجيل الدخول إلى Heroku

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

دعنا نرى النتيجة بالضغط على أي مفتاح من لوحة المفاتيح. عند الضغط على أي مفتاح من لوحة المفاتيح سيُفتح صفحة تسجيل الدخول في 'Heroku' واضغط على صفحة تسجيل الدخول. ثم سيتم الاتصال بجهازك المحلي بخادم 'Heroku' البعيد. إذا كنت متصلًا بالخادم البعيد، سترى هذا.

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

#### إنشاء ملفات 'requirements' و 'Procfile'

قبل دفع الكود إلى الخادم البعيد، نحتاج إلى ملفات 'requirements'

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

سيحتوي ملف 'Procfile' على الأمر الذي يشغّل التطبيق على خادم الويب، في حالتنا على 'Heroku'.

```sh
web: python app.py
```

#### دفع المشروع إلى Heroku

الآن، المشروع جاهز للنشر. خطوات نشر التطبيق على 'Heroku'

1. git init
2. git add .
3. git commit -m "commit message"
4. heroku create 'name of the app as one word'
5. git push heroku master
6. heroku open (لتشغيل التطبيق المنشور)

بعد هذه الخطوة ستحصل على تطبيق مثل [هذا](http://thirdaysofpython-practice.herokuapp.com/)

## تمارين: اليوم 26

1. ستبني [هذا التطبيق](https://thirtydaysofpython-v1-final.herokuapp.com/). لم يتبقَ سوى جزء محلل النصوص


🎉 مبروك ! 🎉

[<< اليوم 25](./25_pandas.md) | [اليوم 27 >>](./27_python_with_mongodb.md)
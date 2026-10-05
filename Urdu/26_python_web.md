<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 26 — ویب کے لیے پائتھن</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../26_Day_Python_web/26_python_web.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 25](./25_pandas.md) | [فہرست](./readme.md) | [اگلا دن: 27](./27_python_with_mongodb.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 26](#day-26-section-1)
  - [ویب کے لیے پائتھن](#day-26-section-2)
    - [Flask](#day-26-section-3)
      - [فولڈروں کی ساخت](#day-26-section-4)
    - [منصوبے کا فولڈر تیار کرنا](#day-26-section-5)
    - [روٹس بنانا](#day-26-section-6)
    - [ٹیمپلیٹس بنانا](#day-26-section-7)
    - [پائتھن اسکرپٹ](#day-26-section-8)
    - [نیویگیشن](#day-26-section-9)
    - [مشترک layout بنانا](#day-26-section-10)
      - [جامد فائلیں فراہم کرنا](#day-26-section-11)
    - [ایپلی کیشن شائع کرنا](#day-26-section-12)
      - [Heroku اکاؤنٹ بنانا](#day-26-section-13)
      - [Heroku میں لاگ اِن](#day-26-section-14)
      - [requirements اور Procfile بنانا](#day-26-section-15)
      - [منصوبہ Heroku پر بھیجنا](#day-26-section-16)
  - [مشقیں — دن 26](#day-26-section-17)

<a id="day-26-section-1"></a>

# 📘 دن 26

<a id="day-26-section-2"></a>

## ویب کے لیے پائتھن

پائتھن عام مقاصد کی زبان ہے اور ویب ایپلی کیشنز میں بھی استعمال ہوتی ہے۔ اس کے بہت سے ویب فریم ورک ہیں، جن میں Django اور Flask معروف ہیں۔ اس سبق میں Flask استعمال کریں گے۔

<a id="day-26-section-3"></a>

### Flask

Flask پائتھن کا ویب فریم ورک ہے۔ یہ Jinja2 template engine استعمال کرتا ہے اور React جیسی فرنٹ اینڈ لائبریریوں کے ساتھ بھی کام کر سکتا ہے۔

اگر `virtualenv` انسٹال نہیں تو پہلے انسٹال کریں۔ ورچوئل ماحول منصوبے کے پیکیجز کو دوسرے منصوبوں سے الگ رکھتا ہے۔

<a id="day-26-section-4"></a>

#### فولڈروں کی ساخت

تمام مراحل کے بعد ساخت کچھ یوں ہو گی:

<div dir="ltr">

```sh

├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html
```

</div>

<a id="day-26-section-5"></a>

### منصوبے کا فولڈر تیار کرنا

Flask کے لیے یہ مراحل انجام دیں۔

مرحلہ 1: `virtualenv` انسٹال کریں۔

<div dir="ltr">

```sh
pip install virtualenv
```

</div>

مرحلہ 2:

<div dir="ltr">

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

</div>

`python_for_web` منصوبے میں `venv` نام کا ماحول بنایا اور فعال کیا گیا۔ نام کوئی اور بھی ہو سکتا ہے۔ `pip freeze` سے پیکیجز دیکھے؛ اصل مثال میں ابھی کوئی پیکیج نہ ہونے کی وجہ سے نتیجہ خالی تھا۔

اب منصوبے کی مرکزی فائل `app.py` بنائیں۔ درج ذیل کوڈ میں `flask` اور `os` استعمال ہوئے ہیں۔

<a id="day-26-section-6"></a>

### روٹس بنانا

ہوم روٹ:

<div dir="ltr">

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

</div>

منصوبے کے مرکزی فولڈر میں `python app.py` چلائیں، پھر براؤزر میں `http://localhost:5000` کھولیں۔

ایک اور روٹ، یعنی about، شامل کریں۔

<div dir="ltr">

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

</div>

سٹرنگ کی جگہ HTML فائل دکھانے کے لیے `render_template()` استعمال کریں۔ `templates` فولڈر میں `home.html` اور `about.html` بنائیں اور Flask سے `render_template` امپورٹ کریں۔

<a id="day-26-section-7"></a>

### ٹیمپلیٹس بنانا

HTML فائلیں `templates` میں رکھیں۔

`home.html`:

<div dir="ltr">

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

</div>

`about.html`:

<div dir="ltr">

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

</div>

<a id="day-26-section-8"></a>

### پائتھن اسکرپٹ

`app.py`:

<div dir="ltr">

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

</div>

صفحوں کے درمیان جانے کے لیے روابط چاہییں۔ ہر صفحے پر رابطے شامل کر سکتے ہیں یا سب کے لیے مشترک layout بنا سکتے ہیں۔

<a id="day-26-section-9"></a>

### نیویگیشن

<div dir="ltr">

```html
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
```

</div>

اب روابط سے دوسرے صفحے پر جا سکتے ہیں۔ فارم کے لیے مزید صفحہ `post.html` بنائیں۔ Jinja2 سے HTML میں ڈیٹا بھیجا جا سکتا ہے۔

<div dir="ltr">

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

</div>

ٹیمپلیٹس دیکھیں۔

`home.html`:

<div dir="ltr">

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

</div>

`about.html`:

<div dir="ltr">

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

</div>

<a id="day-26-section-10"></a>

### مشترک layout بنانا

ٹیمپلیٹس میں دہرایا گیا کوڈ `templates/layout.html` میں رکھیں اور باقی صفحات میں استعمال کریں۔

<a id="day-26-section-11"></a>

#### جامد فائلیں فراہم کرنا

منصوبے میں `static`، پھر اس میں `css` یا `styles` فولڈر اور stylesheet بنائیں۔ جامد فائل کا URL بنانے کے لیے `url_for()` استعمال کریں۔

`layout.html`:

<div dir="ltr">

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

</div>

دوسرے ٹیمپلیٹس سے دہرایا ہوا حصہ نکال کر layout استعمال کریں۔ روابط میں `url_for()` کو روٹ فنکشن کا نام دیں۔

`home.html`:

<div dir="ltr">

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

</div>

`about.html`:

<div dir="ltr">

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

</div>

`post.html`:

<div dir="ltr">

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

</div>

GET، POST، PUT اور DELETE عام HTTP طریقے ہیں جن سے ڈیٹا پڑھنے، بنانے، بدلنے اور حذف کرنے کے کام ہوتے ہیں۔

`post` روٹ درخواست کی قسم کے مطابق GET یا POST سنبھالتا ہے۔ Flask کا `request` آبجیکٹ درخواست کا طریقہ اور فارم کی قدریں حاصل کرنے میں مدد دیتا ہے۔

`app.py`:

<div dir="ltr">

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

</div>

اب ٹیمپلیٹ، ڈیٹا اور مشترک layout کا استعمال دیکھ چکے ہیں۔ `static/css/main.css` بنائیں اور اسے `layout.html` سے جوڑیں۔ اصل منصوبے کی CSS نقل کر کے استعمال کر سکتے ہیں۔ اب deployment دیکھیں۔

<a id="day-26-section-12"></a>

### ایپلی کیشن شائع کرنا

<a id="day-26-section-13"></a>

#### Heroku اکاؤنٹ بنانا

اصل سبق Heroku کی اُس وقت کی مفت سروس استعمال کرتا ہے۔ یہ تاریخی رہنمائی ہے؛ موجودہ دستیابی اور قیمت [Heroku](https://www.heroku.com/) پر دیکھیں۔ اکاؤنٹ اور مناسب منصوبہ منتخب کر کے اپنی مشین پر [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) انسٹال کریں۔

<a id="day-26-section-14"></a>

#### Heroku میں لاگ اِن

<div dir="ltr">

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

</div>

کوئی کلید دبانے پر لاگ اِن صفحہ کھلتا ہے۔ لاگ اِن مکمل ہونے پر مقامی CLI اکاؤنٹ کے ساتھ منسلک ہو جاتا ہے۔ اصل مثال کا نتیجہ:

<div dir="ltr">

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

</div>

<a id="day-26-section-15"></a>

#### requirements اور Procfile بنانا

سرور پر بھیجنے سے پہلے یہ فائلیں تیار کریں:

- `requirements.txt`
- `Procfile`

<div dir="ltr">

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

</div>

`Procfile` میں سرور پر ایپ چلانے کی کمانڈ ہوتی ہے۔

<div dir="ltr">

```sh
web: python app.py
```

</div>

<a id="day-26-section-16"></a>

#### منصوبہ Heroku پر بھیجنا

اصل سبق کے deployment مراحل:

1. `git init`
2. `git add .`
3. `git commit -m "commit message"`
4. `heroku create 'name of the app as one word'` — اپنی ایپ کا ایک لفظی نام دیں۔
5. `git push heroku master`
6. `heroku open` — شائع شدہ ایپ کھولنے کے لیے۔

اس کے بعد [اصل نمونے](http://thirdaysofpython-practice.herokuapp.com/) جیسی ایپ ملتی ہے؛ پرانے نمونوں کی موجودہ دستیابی مختلف ہو سکتی ہے۔

<a id="day-26-section-17"></a>

## مشقیں — دن 26

1. [اس نمونے](https://thirtydaysofpython-v1-final.herokuapp.com/) جیسی ایپ بنائیں۔ متن کا تجزیہ کرنے والا حصہ آپ نے مکمل کرنا ہے۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 25](./25_pandas.md) | [فہرست](./readme.md) | [اگلا دن: 27](./27_python_with_mongodb.md)

</div>

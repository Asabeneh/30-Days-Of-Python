<div align="center">
  <h1> 30 kunlik Python: 26-kun — Python va Web (Flask)</h1>
</div>

[<< 25-kun](./25_pandas_uz.md) | [27-kun >>](./27_python_with_mongodb_uz.md)

- [📘 26-kun](#-26-kun)
  - [Flask nima](#flask-nima)
  - [Loyiha sozlash](#loyiha-sozlash)
  - [Marshrut (Route) yaratish](#marshrut-route-yaratish)
  - [HTML shablonlar](#html-shablonlar)
  - [Ma'lumot uzatish: Python -> HTML](#ma-lumot-uzatish-python---html)
  - [Layout yaratish](#layout-yaratish)
  - [Form bilan ishlash (POST so'rov)](#form-bilan-ishlash-post-so-rov)
  - [Deployment (Nashr qilish)](#deployment-nashr-qilish)
  - [💻 Mashqlar — 26-kun](#-mashqlar--26-kun)

# 📘 26-kun

## Flask nima

**Flask** — Python'da yozilgan yengil veb-freymvork (web framework). Django'ga nisbatan soddaroq — kichik loyihalar va API yaratish uchun ideal.

> 🟡 **JS bilan taqqoslash:** Flask — Node.js + Express.js juftligiga o'xshaydi. `@app.route()` dekoratori — Express'dagi `app.get('/', (req, res) => ...)` ga, `render_template()` — EJS/Handlebars shablon tizimiga o'xshaydi.

Flask **Jinja2** shablon tizimidan foydalanadi — u Python kod va HTML'ni birlashtiradi.

## Loyiha sozlash

**Papka tuzilmasi (yakuniy ko'rinish):**

```
python_for_web/
├── app.py           # Asosiy Python fayl
├── requirements.txt # Paketlar ro'yxati
├── venv/            # Virtual muhit (23-kun)
├── static/
│   └── css/
│       └── main.css
└── templates/
    ├── layout.html
    ├── home.html
    ├── about.html
    └── post.html
```

**O'rnatish:**

```sh
mkdir python_for_web
cd python_for_web
virtualenv venv
source venv/bin/activate    # Mac/Linux
pip install Flask
```

## Marshrut (Route) yaratish

`app.py` — loyihaning asosiy fayli:

```python
from flask import Flask
import os

app = Flask(__name__)   # __name__ — joriy fayl nomi

@app.route('/')         # '/' — bosh sahifa manzili
def home():
    return '<h1>Xush kelibsiz!</h1>'

@app.route('/about')
def about():
    return '<h1>Biz haqimizda</h1>'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

> 🟡 `@app.route('/')` — bu **dekorator** (14-kunda ko'rgan edik). Express.js'dagi `app.get('/', handler)` bilan bir xil vazifani bajaradi. `debug=True` — kod o'zgarganda server avtomatik qayta ishga tushadi (Node'dagi `nodemon` kabi).

**Ishga tushirish:**

```sh
python app.py
# http://localhost:5000 manziliga kiring
```

## HTML shablonlar

Matn o'rniga HTML fayl qaytarish uchun `render_template()` va `templates/` papkasi kerak:

**templates/home.html:**

```html
<!DOCTYPE html>
<html lang="uz">
  <head>
    <meta charset="UTF-8" />
    <title>Bosh sahifa</title>
  </head>
  <body>
    <h1>Xush kelibsiz!</h1>
  </body>
</html>
```

**app.py:**

```python
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')   # templates/ papkasidan izlaydi

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## Ma'lumot uzatish: Python -> HTML

Flask **Jinja2** orqali Python o'zgaruvchilarini HTML'ga uzatadi — JS'dagi template literal `` `${var}` `` mantig'iga o'xshaydi:

**app.py:**

```python
@app.route('/')
def home():
    texnologiyalar = ['HTML', 'CSS', 'Flask', 'Python']
    nom = '30 kunlik Python'
    return render_template('home.html', texlar=texnologiyalar, nom=nom, title='Bosh sahifa')
```

**templates/home.html:**

```html
<!DOCTYPE html>
<html lang="uz">
  <head><title>Bosh sahifa</title></head>
  <body>
    <h1>Xush kelibsiz, {{nom}}!</h1>
    <ul>
      {% for tex in texlar %}
        <li>{{tex}}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

> 🟡 Jinja2 sintaksisi:
> - `{{o'zgaruvchi}}` — qiymatni chiqarish (JS'da `${variable}`)
> - `{% for ... %}...{% endfor %}` — sikl (JS'da `.map()` yoki `{% for %}`)
> - `{% if ... %}...{% endif %}` — shart

## Layout yaratish

Har bir sahifada takrorlanuvchi kodni oldini olish uchun **umumiy layout** yaratiladi — xuddi React'dagi Layout component'ga o'xshaydi:

**templates/layout.html:**

```html
<!DOCTYPE html>
<html lang="uz">
  <head>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" />
    {% if title %}
      <title>30 Kunlik Python — {{ title }}</title>
    {% else %}
      <title>30 Kunlik Python</title>
    {% endif %}
  </head>
  <body>
    <header>
      <nav>
        <a href="{{ url_for('home') }}">Bosh sahifa</a>
        <a href="{{ url_for('about') }}">Biz haqimizda</a>
        <a href="{{ url_for('post') }}">Matn tahlili</a>
      </nav>
    </header>
    <main>
      {% block content %}{% endblock %}
    </main>
  </body>
</html>
```

> 🟡 `{% block content %}{% endblock %}` — layout'dagi "bo'sh joy". Farzand shablonlar shu joyni to'ldiradi. React'dagi `{children}` props'iga o'xshaydi.

**templates/home.html (layout'dan meros oladi):**

```html
{% extends 'layout.html' %}
{% block content %}
<div class="container">
  <h1>Xush kelibsiz, {{nom}}!</h1>
  <ul>
    {% for tex in texlar %}
      <li>{{tex}}</li>
    {% endfor %}
  </ul>
</div>
{% endblock %}
```

> 🟡 `{% extends 'layout.html' %}` — JS'dagi `class Child extends Parent` kabi: farzand shablon ota-shablonning tuzilmasini meros oladi.

## Form bilan ishlash (POST so'rov)

**templates/post.html:**

```html
{% extends 'layout.html' %}
{% block content %}
<div class="container">
  <h1>Matn tahlili</h1>
  <form action="/post" method="POST">
    <textarea rows="10" name="content" autofocus></textarea>
    <input type="submit" value="Tahlil qilish" />
  </form>
</div>
{% endblock %}
```

**app.py — GET va POST so'rovlarni boshqarish:**

```python
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0   # statik fayllarni keshlamaslik

@app.route('/')
def home():
    texnologiyalar = ['HTML', 'CSS', 'Flask', 'Python']
    nom = '30 Kunlik Python'
    return render_template('home.html', texlar=texnologiyalar, nom=nom, title='Bosh sahifa')

@app.route('/about')
def about():
    return render_template('about.html', title='Biz haqimizda')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods=['GET', 'POST'])   # har ikki metodga ruxsat
def post():
    nom = 'Matn tahlili'
    if request.method == 'GET':
        return render_template('post.html', nom=nom, title=nom)
    if request.method == 'POST':
        content = request.form['content']  # formdan ma'lumot olish
        print(content)
        return redirect(url_for('result'))  # natija sahifasiga yo'naltirish

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

> 🟡 `request.form['content']` — JS'da `req.body.content` (Express'da body-parser bilan) ga o'xshaydi. `redirect(url_for('result'))` — Express'dagi `res.redirect('/result')` ga mos.

## Deployment (Nashr qilish)

Ilovani internetga chiqarish uchun **Heroku** platformasi ishlatiladi (bepul tier):

**1. requirements.txt yaratish:**

```sh
pip freeze > requirements.txt
```

**2. Procfile yaratish** (Heroku uchun):

```
web: gunicorn app:app
```

**3. Heroku CLI orqali nashr:**

```sh
heroku login
heroku create
git add .
git commit -m "Flask ilovasi"
git push heroku master
heroku open
```

> 🟡 Bu jarayon Node.js ilovasini Heroku'ga nashr qilish bilan bir xil. `gunicorn` — Python'dagi produksiya serveri (Node'dagi `pm2`'ga o'xshaydi).

🌕 Endi siz Python'da veb-sayt yarata olasiz! Maqsadga 4 kun qoldi. 26-kun challenge'ini tugatdingiz.

## 💻 Mashqlar — 26-kun

1. Flask o'rnatib, bosh sahifa (`/`) va `/about` sahifalari bilan oddiy ilova yarating.
2. Python ro'yxatini HTML shablonga uzatib, `{% for %}` bilan chiqaring.
3. Forma yarating — foydalanuvchi matn kiritsa, uning harflar sonini qaytaring.

🎉 TABRIKLAYMIZ! 🎉

[<< 25-kun](./25_pandas_uz.md) | [27-kun >>](./27_python_with_mongodb_uz.md)

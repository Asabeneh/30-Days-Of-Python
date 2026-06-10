<div align="center">
  <h1> 30 Jours de Python : Jour 26 - Python pour le web </h1>
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

[<< Jour 25](./25_pandas_fr.md) | [Jour 27 >>](./27_python_with_mongodb_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 26](#-jour-26)
  - [Python pour le web](#python-pour-le-web)
    - [Flask](#flask)
      - [Structure des dossiers](#structure-des-dossiers)
    - [Configurer votre dossier de projet](#configurer-votre-dossier-de-projet)
    - [Créer des routes](#créer-des-routes)
    - [Créer des templates](#créer-des-templates)
    - [Script Python](#script-python)
    - [Navigation](#navigation)
    - [Créer une mise en page](#créer-une-mise-en-page)
      - [Servir des fichiers statiques](#servir-des-fichiers-statiques)
    - [Déploiement](#déploiement)
      - [Créer un compte Heroku](#créer-un-compte-heroku)
      - [Se connecter à Heroku](#se-connecter-à-heroku)
      - [Créer requirements et Procfile](#créer-requirements-et-procfile)
      - [Pousser le projet vers heroku](#pousser-le-projet-vers-heroku)
  - [Exercices : Jour 26](#exercices-jour-26)

# 📘 Jour 26

## Python pour le web

Python est un langage de programmation généraliste et peut être utilisé dans de nombreux domaines. Dans cette section, nous verrons comment utiliser Python pour le web. Il existe de nombreux frameworks web Python. Django et Flask sont les plus populaires. Aujourd'hui, nous allons voir comment utiliser Flask pour le développement web.

### Flask

Flask est un framework de développement web écrit en Python. Flask utilise le moteur de template Jinja2. Flask peut également être utilisé avec d'autres bibliothèques front modernes telles que React.

Si vous n'avez pas encore installé le paquet virtualenv, installez-le d'abord. L'environnement virtuel permettra d'isoler les dépendances du projet de celles de la machine locale.

#### Structure des dossiers

Après avoir terminé toutes les étapes, la structure de votre projet devrait ressembler à ceci :

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

### Configurer votre dossier de projet

Suivez les étapes suivantes pour commencer avec Flask.

Étape 1 : installez virtualenv en utilisant la commande suivante.

```sh
pip install virtualenv
```

Étape 2 :

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

Nous avons créé un dossier de projet nommé python_for_web. Dans le projet, nous avons créé un environnement virtuel *venv* (qui pourrait avoir n'importe quel nom mais je préfère l'appeler _venv_). Ensuite, nous avons activé l'environnement virtuel. Nous avons utilisé pip freeze pour vérifier les paquets installés dans le dossier du projet. Le résultat de pip freeze était vide car aucun paquet n'était encore installé.

Maintenant, créons le fichier app.py dans le dossier du projet et écrivons le code suivant. Le fichier app.py sera le fichier principal du projet. Le code suivant a le module flask et le module os.

### Créer des routes

La route d'accueil.

```py
# importons flask
from flask import Flask
import os # importation du module système d'exploitation

app = Flask(__name__)

@app.route('/') # ce décorateur crée la route d'accueil
def home ():
    return '<h1>Bienvenue</h1>'

if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Pour exécuter l'application Flask, tapez python app.py dans le répertoire principal de l'application Flask.

Après avoir exécuté _python app.py_, vérifiez le localhost 5000.

Ajoutons une route supplémentaire.
Création de la route about

```py
# importons flask
from flask import Flask
import os # importation du module système d'exploitation

app = Flask(__name__)

@app.route('/') # ce décorateur crée la route d'accueil
def home ():
    return '<h1>Bienvenue</h1>'

@app.route('/about')
def about():
    return '<h1>À propos</h1>'

if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Maintenant, nous avons ajouté la route about dans le code ci-dessus. Et si nous voulions afficher un fichier HTML au lieu d'une chaîne ? Il est possible d'afficher un fichier HTML en utilisant la fonction *render_template*. Créons un dossier appelé templates et créons les fichiers home.html et about.html dans le dossier du projet. Importons également la fonction *render_template* depuis flask.

### Créer des templates

Créez les fichiers HTML dans le dossier templates.

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Accueil</title>
  </head>

  <body>
    <h1>Bienvenue</h1>
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
    <title>À propos</title>
  </head>

  <body>
    <h1>À propos de nous</h1>
  </body>
</html>
```

### Script Python

app.py

```py
# importons flask
from flask import Flask, render_template
import os # importation du module système d'exploitation

app = Flask(__name__)

@app.route('/') # ce décorateur crée la route d'accueil
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # pour le déploiement nous utilisons environ
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Comme vous pouvez le voir, pour accéder à différentes pages ou naviguer, nous avons besoin d'une navigation. Ajoutons un lien vers chaque page ou créons une mise en page que nous utiliserons pour chaque page.

### Navigation

```html
<ul>
  <li><a href="/">Accueil</a></li>
  <li><a href="/about">À propos</a></li>
</ul>
```

Maintenant, nous pouvons naviguer entre les pages en utilisant le lien ci-dessus. Créons une page supplémentaire qui gère les données de formulaire. Vous pouvez l'appeler comme vous voulez, j'aime l'appeler post.html.

Nous pouvons injecter des données dans les fichiers HTML en utilisant le moteur de template Jinja2.

```py
# importons flask
from flask import Flask, render_template, request, redirect, url_for
import os # importation du module système d'exploitation

app = Flask(__name__)

@app.route('/') # ce décorateur crée la route d'accueil
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Accueil')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'À propos')

@app.route('/post')
def post():
    name = 'Analyseur de texte'
    return render_template('post.html', name = name, title = name)


if __name__ == '__main__':
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Voyons aussi les templates :

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Accueil</title>
  </head>

  <body>
    <ul>
      <li><a href="/">Accueil</a></li>
      <li><a href="/about">À propos</a></li>
    </ul>
    <h1>Bienvenue sur {{name}}</h1>
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
    <title>À propos</title>
  </head>

  <body>
    <ul>
      <li><a href="/">Accueil</a></li>
      <li><a href="/about">À propos</a></li>
    </ul>
    <h1>À propos de nous</h1>
    <h2>{{name}}</h2>
  </body>
</html>
```

### Créer une mise en page

Dans les fichiers templates, il y a beaucoup de code répété, nous pouvons écrire une mise en page et supprimer la répétition. Créons layout.html dans le dossier templates.
Après avoir créé la mise en page, nous l'importerons dans chaque fichier.

#### Servir des fichiers statiques

Créez un dossier static dans votre dossier de projet. Dans le dossier static, créez un dossier CSS ou styles et créez une feuille de style CSS. Nous utilisons le module *url_for* pour servir les fichiers statiques.

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
            <a class="nav-link active" href="{{ url_for('home') }}">Accueil</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('about') }}">À propos</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('post') }}"
              >Analyseur de texte</a
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

Maintenant, supprimons tout le code répété dans les autres fichiers templates et importons layout.html. Le href utilise la fonction _url_for_ avec le nom de la fonction de route pour connecter chaque route de navigation.

home.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>Bienvenue sur {{name}}</h1>
  <p>
    Cette application nettoie les textes et analyse le nombre de mots, de caractères et
    les mots les plus fréquents dans le texte. Essayez-la en cliquant sur analyseur de texte dans le
    menu. Vous avez besoin des technologies suivantes pour construire cette application web :
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
  <h1>À propos {{name}}</h1>
  <p>
    Ceci est un défi de programmation de 30 jours de Python. Si vous avez codé
    jusqu'ici, vous êtes génial. Félicitations pour le travail accompli !
  </p>
</div>
{% endblock %}
```

post.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>Analyseur de texte</h1>
  <form action="https://thirtydaysofpython-v1.herokuapp.com/post" method="POST">
    <div>
      <textarea rows="25" name="content" autofocus></textarea>
    </div>
    <div>
      <input type="submit" class="btn" value="Traiter le texte" />
    </div>
  </form>
</div>

{% endblock %}
```

Les méthodes de requête, il existe différentes méthodes de requête (GET, POST, PUT, DELETE) qui sont les méthodes de requête courantes permettant d'effectuer des opérations CRUD (Create, Read, Update, Delete).

Dans la route post, nous utiliserons les méthodes GET et POST de manière alternative selon le type de requête, regardez à quoi cela ressemble dans le code ci-dessous. La méthode request est une fonction pour gérer les méthodes de requête et aussi pour accéder aux données du formulaire.
app.py

```py
# importons flask
from flask import Flask, render_template, request, redirect, url_for
import os # importation du module système d'exploitation

app = Flask(__name__)
# pour arrêter la mise en cache des fichiers statiques
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') # ce décorateur crée la route d'accueil
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Accueil')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'À propos')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Analyseur de texte'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    # pour le déploiement
    # pour que ça fonctionne à la fois en production et en développement
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Jusqu'à présent, nous avons vu comment utiliser un template, comment injecter des données dans un template, et comment créer une mise en page commune.
Maintenant, gérons les fichiers statiques. Créez un dossier appelé static dans le dossier du projet et créez un dossier appelé css. Dans le dossier css, créez main.css. Votre fichier main.css sera lié au layout.html.

Vous n'avez pas besoin d'écrire le fichier css, copiez-le et utilisez-le. Passons au déploiement.

### Déploiement

#### Créer un compte Heroku

Heroku fournit un service de déploiement gratuit pour les applications front-end et full-stack. Créez un compte sur [heroku](https://www.heroku.com/) et installez le [CLI](https://devcenter.heroku.com/articles/heroku-cli) heroku pour votre machine.
Après avoir installé heroku, tapez la commande suivante :

#### Se connecter à Heroku

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

Voyons le résultat en cliquant sur n'importe quelle touche du clavier. Lorsque vous appuyez sur n'importe quelle touche, cela ouvrira la page de connexion heroku et cliquez sur le bouton de connexion. Ensuite, votre machine locale sera connectée au serveur distant heroku. Si vous êtes connecté au serveur distant, vous verrez ceci.

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

#### Créer requirements et Procfile

Avant de pousser notre code vers le serveur distant, nous avons besoin de :

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

Le Procfile contiendra la commande qui exécute l'application sur le serveur web, dans notre cas sur Heroku.

```sh
web: python app.py
```

#### Pousser le projet vers heroku

Maintenant, il est prêt à être déployé. Étapes pour déployer l'application sur heroku :

1. git init
2. git add .
3. git commit -m "message du commit"
4. heroku create 'nom de l'application en un mot'
5. git push heroku master
6. heroku open (pour lancer l'application déployée)

Après cette étape, vous obtiendrez une application comme [celle-ci](http://thirdaysofpython-practice.herokuapp.com/).

## Exercices : Jour 26

1. Vous allez construire [cette application](https://thirtydaysofpython-v1-final.herokuapp.com/). Seule la partie analyseur de texte reste à faire.


🎉 FÉLICITATIONS ! 🎉

[<< Jour 25](./25_pandas_fr.md) | [Jour 27 >>](./27_python_with_mongodb_fr.md)

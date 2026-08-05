<div align="center">
  <h1> 30 Dias de Python: Dia 26 - Python para a web </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Autor:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>Segunda edição: Julho, 2021</small>
  </sub>
</div>

[<< Dia 25](./25_pandas_pt.md) | [Dia 27 >>](./27_python_with_mongodb_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 26](#-dia-26)
  - [Python para a web](#python-para-a-web)
    - [Flask](#flask)
      - [Estrutura de pastas](#estrutura-de-pastas)
    - [Configurando o diretório do seu projeto](#configurando-o-diretório-do-seu-projeto)
    - [Criando rotas](#criando-rotas)
    - [Criando templates](#criando-templates)
    - [Script Python](#script-python)
    - [Navegação](#navegação)
    - [Criando um layout](#criando-um-layout)
      - [Servindo arquivos estáticos](#servindo-arquivos-estáticos)
    - [Deploy](#deploy)
      - [Criando uma conta no Heroku](#criando-uma-conta-no-heroku)
      - [Login no Heroku](#login-no-heroku)
      - [Criar requirements e Procfile](#criar-requirements-e-procfile)
      - [Enviando o projeto para o heroku](#enviando-o-projeto-para-o-heroku)
  - [Exercícios: Dia 26](#exercícios-dia-26)

# 📘 Dia 26

## Python para a web

Python é uma linguagem de programação de uso geral e pode ser usada em muitos lugares. Nesta seção, veremos como usar o Python para a web. Existem muitos frameworks web em Python. Django e Flask são os mais populares. Hoje, veremos como usar o Flask para desenvolvimento web.

### Flask

Flask é um framework de desenvolvimento web escrito em Python. O Flask usa o motor de templates Jinja2. O Flask também pode ser usado com outras bibliotecas front-end modernas, como o React.

Se você ainda não instalou o pacote virtualenv, instale-o primeiro. O ambiente virtual permitirá isolar as dependências do projeto das dependências da máquina local.

#### Estrutura de pastas

Depois de concluir todas as etapas, a estrutura de arquivos do seu projeto deve ficar assim:

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

### Configurando o diretório do seu projeto

Siga os passos abaixo para começar com o Flask.

Passo 1: instale o virtualenv usando o comando abaixo.

```sh
pip install virtualenv
```

Passo 2:

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

Criamos um diretório de projeto chamado python_for_web. Dentro do projeto criamos um ambiente virtual *venv*, que poderia ter qualquer nome, mas prefiro chamá-lo de _venv_. Em seguida, ativamos o ambiente virtual. Usamos o pip freeze para verificar os pacotes instalados no diretório do projeto. O resultado do pip freeze estava vazio porque nenhum pacote havia sido instalado ainda.

Agora, vamos criar o arquivo app.py no diretório do projeto e escrever o código abaixo. O arquivo app.py será o arquivo principal do projeto. O código a seguir usa o módulo flask e o módulo os.

### Criando rotas

A rota home.

```py
# vamos importar o flask
from flask import Flask
import os # importando o módulo do sistema operacional

app = Flask(__name__)

@app.route('/') # este decorador cria a rota home
def home ():
    return '<h1>Bem-vindo</h1>'

if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Para executar a aplicação flask, escreva python app.py no diretório principal da aplicação flask.

Depois de executar _python app.py_, verifique o localhost 5000.

Vamos adicionar uma rota adicional.
Criando a rota about

```py
# vamos importar o flask
from flask import Flask
import os # importando o módulo do sistema operacional

app = Flask(__name__)

@app.route('/') # este decorador cria a rota home
def home ():
    return '<h1>Bem-vindo</h1>'

@app.route('/about')
def about():
    return '<h1>Sobre nós</h1>'

if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Agora, adicionamos a rota about no código acima. E se quisermos renderizar um arquivo HTML em vez de uma string? É possível renderizar um arquivo HTML usando a função *render_template*. Vamos criar uma pasta chamada templates e criar os arquivos home.html e about.html no diretório do projeto. Vamos também importar a função *render_template* do flask.

### Criando templates

Crie os arquivos HTML dentro da pasta templates.

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
    <h1>Bem-vindo ao Home</h1>
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
    <title>Sobre</title>
  </head>

  <body>
    <h1>Sobre nós</h1>
  </body>
</html>
```

### Script Python

app.py

```py
# vamos importar o flask
from flask import Flask, render_template
import os # importando o módulo do sistema operacional

app = Flask(__name__)

@app.route('/') # este decorador cria a rota home
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # para o deploy usamos o environ
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Como você pode ver, para ir a diferentes páginas ou para navegar precisamos de uma navegação. Vamos adicionar um link para cada página ou criar um layout que usaremos em cada página.

### Navegação

```html
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
```

Agora, podemos navegar entre as páginas usando o link acima. Vamos criar uma página adicional que trata dados de formulário. Você pode chamá-la de qualquer nome, eu gosto de chamá-la de post.html.

Podemos injetar dados nos arquivos HTML usando o motor de templates Jinja2.

```py
# vamos importar o flask
from flask import Flask, render_template, request, redirect, url_for
import os # importando o módulo do sistema operacional

app = Flask(__name__)

@app.route('/') # este decorador cria a rota home
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
    # para o deploy
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Vamos ver também os templates:

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
    <h1>Bem-vindo a {{name}}</h1>
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
    <h1>Sobre nós</h1>
    <h2>{{name}}</h2>
  </body>
</html>
```

### Criando um layout

Nos arquivos de template, há muito código repetido; podemos escrever um layout e remover a repetição. Vamos criar o layout.html dentro da pasta templates.
Depois de criar o layout, vamos importá-lo em cada arquivo.

#### Servindo arquivos estáticos

Crie uma pasta static no diretório do seu projeto. Dentro da pasta static, crie uma pasta CSS ou styles e crie uma folha de estilo CSS. Usamos o módulo *url_for* para servir o arquivo estático.

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

Agora, vamos remover todo o código repetido nos outros arquivos de template e importar o layout.html. O href está usando a função _url_for_ com o nome da função da rota para conectar cada rota de navegação.

home.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>Bem-vindo a {{name}}</h1>
  <p>
    Esta aplicação limpa textos e analisa o número de palavras, caracteres e
    as palavras mais frequentes no texto. Confira clicando em text analyzer no
    menu. Você precisa das seguintes tecnologias para construir esta aplicação web:
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
  <h1>Sobre {{name}}</h1>
  <p>
    Este é um desafio de programação de 30 dias de Python. Se você tem codado
    até aqui, você é incrível. Parabéns pelo trabalho bem feito!
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

Métodos de requisição: existem diferentes métodos de requisição (GET, POST, PUT, DELETE) que são os métodos de requisição comuns que nos permitem realizar operações CRUD (Create, Read, Update, Delete).

Na rota post, usaremos os métodos GET e POST alternadamente dependendo do tipo de requisição; veja como isso fica no código abaixo. O método request é uma função para tratar os métodos de requisição e também para acessar os dados do formulário.
app.py

```py
# vamos importar o flask
from flask import Flask, render_template, request, redirect, url_for
import os # importando o módulo do sistema operacional

app = Flask(__name__)
# para impedir o cache de arquivos estáticos
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') # este decorador cria a rota home
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
    # para o deploy
    # para que funcione tanto em produção quanto em desenvolvimento
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Até agora, vimos como usar templates, como injetar dados em templates e como criar um layout comum.
Agora, vamos tratar arquivos estáticos. Crie uma pasta chamada static no diretório do projeto e crie uma pasta chamada css. Dentro da pasta css, crie o main.css. Seu arquivo main.css será vinculado ao layout.html.

Você não precisa escrever o arquivo css, copie-o e use-o. Vamos passar para o deploy.

### Deploy

#### Criando uma conta no Heroku

O Heroku fornece um serviço de deploy gratuito tanto para aplicações front-end quanto para aplicações fullstack. Crie uma conta no [heroku](https://www.heroku.com/) e instale a [CLI](https://devcenter.heroku.com/articles/heroku-cli) do heroku na sua máquina.
Depois de instalar o heroku, escreva o comando abaixo

#### Login no Heroku

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

Vamos ver o resultado clicando em qualquer tecla do teclado. Quando você pressionar qualquer tecla do teclado, isso abrirá a página de login do heroku e você deve clicar na página de login. Depois disso, sua máquina local será conectada ao servidor remoto do heroku. Se você estiver conectado ao servidor remoto, você verá isto.

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

#### Criar requirements e Procfile

Antes de enviarmos nosso código para o servidor remoto, precisamos de:

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

O Procfile terá o comando que executa a aplicação no servidor web, em nosso caso no Heroku.

```sh
web: python app.py
```

#### Enviando o projeto para o heroku

Agora, ele está pronto para ser implantado (deploy). Passos para implantar a aplicação no heroku:

1. git init
2. git add .
3. git commit -m "mensagem do commit"
4. heroku create 'nome da aplicação em uma palavra'
5. git push heroku master
6. heroku open (para abrir a aplicação implantada)

Depois desse passo você obterá uma aplicação como [esta](http://thirdaysofpython-practice.herokuapp.com/)

## Exercícios: Dia 26

1. Você vai construir [esta aplicação](https://thirtydaysofpython-v1-final.herokuapp.com/). Falta apenas a parte do analisador de texto


🎉 PARABÉNS ! 🎉

[<< Dia 25](./25_pandas_pt.md) | [Dia 27 >>](./27_python_with_mongodb_pt.md)

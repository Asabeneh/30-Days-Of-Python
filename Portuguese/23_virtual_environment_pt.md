<div align="center">
  <h1> 30 Dias de Python: Dia 23 - Ambiente Virtual </h1>
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

[<< Dia 22](./22_web_scraping_pt.md) | [Dia 24 >>](./24_statistics_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 23](#-dia-23)
  - [Configurando Ambientes Virtuais](#configurando-ambientes-virtuais)
  - [💻 Exercícios: Dia 23](#-exercícios-dia-23)

# 📘 Dia 23

## Configurando Ambientes Virtuais

Para começar um projeto, é melhor ter um ambiente virtual. Um ambiente virtual pode nos ajudar a criar um ambiente isolado ou separado. Isso vai nos ajudar a evitar conflitos de dependências entre projetos. Se você digitar pip freeze no seu terminal, verá todos os pacotes instalados no seu computador. Se usarmos o virtualenv, teremos acesso apenas aos pacotes específicos daquele projeto. Abra o seu terminal e instale o virtualenv

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

Dentro da pasta 30DaysOfPython, crie uma pasta flask_project.

Depois de instalar o pacote virtualenv, vá até a pasta do seu projeto e crie um ambiente virtual escrevendo:

Para Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

```

Para Windows:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

Eu prefiro chamar o novo projeto de venv, mas sinta-se livre para nomeá-lo de outra forma. Vamos verificar se o venv foi criado usando o comando ls (ou dir no prompt de comando do Windows).

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

Vamos ativar o ambiente virtual escrevendo o seguinte comando na pasta do nosso projeto.

Para Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
A ativação do ambiente virtual no Windows pode variar entre o Windows PowerShell e o git bash.

Para Windows PowerShell:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

Para Windows Git bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

Depois de escrever o comando de ativação, o diretório do seu projeto vai começar com venv. Veja o exemplo abaixo.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

Agora, vamos verificar os pacotes disponíveis neste projeto escrevendo pip freeze. Você não vai ver nenhum pacote.

Vamos fazer um pequeno projeto com flask, então vamos instalar o pacote flask neste projeto.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

Agora, vamos escrever pip freeze para ver a lista de pacotes instalados no projeto:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

Quando terminar, você deve desativar o projeto ativo usando _deactivate_.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

Os módulos necessários para trabalhar com flask estão instalados. Agora, o diretório do seu projeto está pronto para um projeto flask. Você deve incluir o venv no seu arquivo .gitignore para não enviá-lo ao github.

## 💻 Exercícios: Dia 23

1. Crie um diretório de projeto com um ambiente virtual, com base no exemplo dado acima.

🎉 PARABÉNS ! 🎉

[<< Dia 22](./22_web_scraping_pt.md) | [Dia 24 >>](./24_statistics_pt.md)

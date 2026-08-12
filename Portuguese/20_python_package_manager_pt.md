<div align="center">
  <h1> 30 Dias de Python: Dia 20 - PIP </h1>
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

[<< Dia 19](./19_file_handling_pt.md) | [Dia 21 >>](./21_classes_and_objects_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 20](#-dia-20)
  - [Python PIP - Gerenciador de Pacotes do Python](#python-pip---gerenciador-de-pacotes-do-python)
    - [O que é PIP?](#o-que-é-pip)
    - [Instalando o PIP](#instalando-o-pip)
    - [Instalando pacotes usando pip](#instalando-pacotes-usando-pip)
    - [Desinstalando Pacotes](#desinstalando-pacotes)
    - [Lista de Pacotes](#lista-de-pacotes)
    - [Mostrar Pacote](#mostrar-pacote)
    - [PIP Freeze](#pip-freeze)
    - [Lendo de uma URL](#lendo-de-uma-url)
    - [Criando um Pacote](#criando-um-pacote)
    - [Mais Informações sobre Pacotes](#mais-informações-sobre-pacotes)
  - [Exercícios: Dia 20](#exercícios-dia-20)

# 📘 Dia 20

## Python PIP - Gerenciador de Pacotes do Python

### O que é PIP?

PIP significa Preferred Installer Program (Programa de Instalação Preferido). Usamos o _pip_ para instalar diferentes pacotes Python.
Um pacote é um módulo Python que pode conter um ou mais módulos ou outros pacotes. Um módulo ou módulos que podemos instalar em nossa aplicação é um pacote.
Na programação, não precisamos escrever todo utilitário do zero; em vez disso, instalamos pacotes e os importamos em nossas aplicações.

### Instalando o PIP

Se você ainda não instalou o pip, vamos instalá-lo agora. Vá até o seu terminal ou prompt de comando e copie e cole isto:

```sh
asabeneh@Asabeneh:~$ pip install pip
```

Verifique se o pip está instalado escrevendo

```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

Como você pode ver, estou usando o pip versão 21.1.3; se você ver algum número um pouco abaixo ou acima disso, significa que você tem o pip instalado.

Vamos verificar alguns dos pacotes usados na comunidade Python para diferentes propósitos. Só para você saber que existem muitos pacotes disponíveis para uso em diferentes aplicações.

### Instalando pacotes usando pip

Vamos tentar instalar o _numpy_, chamado numeric python (python numérico). É um dos pacotes mais populares na comunidade de machine learning e ciência de dados.

- NumPy é o pacote fundamental para computação científica com Python. Ele contém, entre outras coisas:
  - um poderoso objeto de array N-dimensional
  - funções sofisticadas (broadcasting)
  - ferramentas para integrar código C/C++ e Fortran
  - recursos úteis de álgebra linear, transformada de Fourier e números aleatórios

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

Vamos começar a usar o numpy. Abra seu shell interativo do python, escreva python e então importe o numpy da seguinte forma:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>
```

Pandas é uma biblioteca de código aberto, licenciada sob BSD, que fornece estruturas de dados e ferramentas de análise de dados de alto desempenho e fáceis de usar para a linguagem de programação Python. Vamos instalar o irmão mais velho do numpy, o _pandas_:

```sh
asabeneh@Asabeneh:~$ pip install pandas
```

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

Esta seção não é sobre numpy nem sobre pandas; aqui estamos tentando aprender como instalar pacotes e como importá-los. Se necessário, falaremos sobre diferentes pacotes em outras seções.

Vamos importar um módulo de navegador web, que pode nos ajudar a abrir qualquer website. Não precisamos instalar este módulo, ele já vem instalado por padrão com o Python 3. Por exemplo, se você quiser abrir qualquer número de websites em qualquer momento ou se quiser agendar algo, este módulo _webbrowser_ pode ser usado.

```py
import webbrowser # módulo de navegador web para abrir websites

# lista de urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# abre a lista de websites acima em abas diferentes
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### Desinstalando Pacotes

Se você não quiser manter os pacotes instalados, pode removê-los usando o seguinte comando.

```sh
pip uninstall packagename
```

### Lista de Pacotes

Para ver os pacotes instalados em nossa máquina, podemos usar pip seguido de list.

```sh
pip list
```

### Mostrar Pacote

Para mostrar informações sobre um pacote

```sh
pip show packagename
```

```sh
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

Se quisermos ainda mais detalhes, basta adicionar --verbose

```sh
asabeneh@Asabeneh:~$ pip show --verbose pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

Gera os pacotes Python instalados com suas versões, e a saída é adequada para ser usada em um arquivo requirements. Um arquivo requirements.txt é um arquivo que deve conter todos os pacotes Python instalados em um projeto Python.

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

O pip freeze nos deu os pacotes usados, instalados e sua versão. Usamos isso com o arquivo requirements.txt para deploy.

### Lendo de uma URL

Até agora você já está familiarizado com a forma de ler ou escrever em um arquivo localizado em sua máquina local. Às vezes, gostaríamos de ler um website usando uma url ou a partir de uma API.
API significa Application Program Interface (Interface de Programação de Aplicações). É um meio de intercambiar dados estruturados entre servidores, principalmente como dados json. Para abrir uma conexão de rede, precisamos de um pacote chamado _requests_ - ele permite abrir uma conexão de rede e implementar operações CRUD (create, read, update e delete). Nesta seção, vamos abordar apenas a parte de leitura (get) do CRUD.

Vamos instalar o _requests_:

```py
asabeneh@Asabeneh:~$ pip install requests
```

Veremos os métodos _get_, _status_code_, _headers_, _text_ e _json_ do módulo _requests_:
  - _get()_: abre uma rede e busca dados de uma url - retorna um objeto de resposta
  - _status_code_: depois de buscarmos os dados, podemos verificar o status da operação (sucesso, erro, etc.)
  - _headers_: para verificar os tipos de cabeçalho
  - _text_: para extrair o texto do objeto de resposta obtido
  - _json_: para extrair dados json
Vamos ler um arquivo txt deste website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # importando o módulo requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # texto de um website

response = requests.get(url) # abrindo uma rede e buscando os dados
print(response)
print(response.status_code) # código de status, sucesso:200
print(response.headers)     # informações do cabeçalho
print(response.text) # dá todo o texto da página
```

```sh
<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

- Vamos ler a partir de uma API. API significa Application Program Interface. É um meio de intercambiar dados estruturados entre servidores, principalmente dados json. Um exemplo de API: https://restcountries.eu/rest/v2/all. Vamos ler essa API usando o módulo _requests_.

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # api de países
response = requests.get(url)  # abrindo uma rede e buscando os dados
print(response) # objeto de resposta
print(response.status_code)  # código de status, sucesso:200
countries = response.json()
print(countries[:1])  # cortamos apenas o primeiro país, remova o corte para ver todos os países
```

```sh
<Response [200]>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
```

Usamos o método _json()_ do objeto de resposta, se estivermos buscando dados JSON. Para txt, html, xml e outros formatos de arquivo podemos usar _text_.

### Criando um Pacote

Organizamos um grande número de arquivos em diferentes pastas e subpastas com base em algum critério, para que possamos encontrá-los e gerenciá-los facilmente. Como você sabe, um módulo pode conter múltiplos objetos, como classes, funções, etc. Um pacote pode conter um ou mais módulos relevantes. Um pacote é, na verdade, uma pasta contendo um ou mais arquivos de módulo. Vamos criar um pacote chamado mypackage, usando os seguintes passos:

Crie uma nova pasta chamada mypackage dentro da pasta 30DaysOfPython
Crie um arquivo **__init__**.py vazio na pasta mypackage.
Crie os módulos arithmetic.py e greet.py com o seguinte código:

```py
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
```

```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```

A estrutura de pastas do seu pacote deve ficar assim:

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

Agora, vamos abrir o shell interativo do python e testar o pacote que criamos:

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Asabeneh', 'Yetayeh')
'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'
>>>
```

Como você pode ver, nosso pacote funciona perfeitamente. A pasta do pacote contém um arquivo especial chamado **__init__**.py - ele armazena o conteúdo do pacote. Se colocarmos **__init__**.py na pasta do pacote, o python começa a reconhecê-la como um pacote.
O **__init__**.py expõe recursos específicos de seus módulos para serem importados em outros arquivos python. Um arquivo **__init__**.py vazio torna todas as funções disponíveis quando um pacote é importado. O **__init__**.py é essencial para que a pasta seja reconhecida pelo Python como um pacote.

### Mais Informações sobre Pacotes

- Banco de Dados
  - SQLAlchemy ou SQLObject - acesso orientado a objetos a vários sistemas de banco de dados diferentes
    - _pip install SQLAlchemy_
- Desenvolvimento Web
  - Django - framework web de alto nível.
    - _pip install django_
  - Flask - micro framework para Python baseado em Werkzeug, Jinja 2. (Licenciado sob BSD)
    - _pip install flask_
- Parser de HTML
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - parser de HTML/XML projetado para projetos rápidos, como screen-scraping; aceita markup malformado.
    - _pip install beautifulsoup4_
  - PyQuery - implementa jQuery em Python; aparentemente mais rápido que o BeautifulSoup.

- Processamento de XML
  - ElementTree - O tipo Element é um objeto container simples, porém flexível, projetado para armazenar estruturas de dados hierárquicas, como infosets XML simplificados, em memória. --Nota: Python 2.5 e superior já possui ElementTree na Biblioteca Padrão
- GUI (Interface Gráfica)
  - PyQt - Bindings para o framework Qt multiplataforma.
  - TkInter - O kit de ferramentas de interface de usuário tradicional do Python.
- Análise de Dados, Ciência de Dados e Machine Learning
  - Numpy: Numpy (numeric python) é conhecida como uma das bibliotecas de machine learning mais populares em Python.
  - Pandas: é uma biblioteca de análise de dados, ciência de dados e machine learning em Python que fornece estruturas de dados de alto nível e uma grande variedade de ferramentas para análise.
  - SciPy: SciPy é uma biblioteca de machine learning para desenvolvedores de aplicações e engenheiros. A biblioteca SciPy contém módulos para otimização, álgebra linear, integração, processamento de imagens e estatística.
  - Scikit-Learn: É construída sobre NumPy e SciPy. É considerada uma das melhores bibliotecas para trabalhar com dados complexos.
  - TensorFlow: é uma biblioteca de machine learning construída pelo Google.
  - Keras: é considerada uma das bibliotecas de machine learning mais interessantes em Python. Ela fornece um mecanismo mais fácil para expressar redes neurais. O Keras também fornece alguns dos melhores utilitários para compilar modelos, processar conjuntos de dados, visualizar gráficos e muito mais.
- Rede:
  - requests: é um pacote que podemos usar para enviar requisições a um servidor (GET, POST, DELETE, PUT)
    - _pip install requests_

🌕 Você está sempre progredindo e está vinte passos à frente no seu caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## Exercícios: Dia 20

1. Leia esta url e encontre as 10 palavras mais frequentes. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
2. Leia a API de gatos cats_api = 'https://api.thecatapi.com/v1/breeds' e encontre:
   1. o mínimo, máximo, média, mediana e desvio padrão do peso dos gatos em unidades métricas.
   2. o mínimo, máximo, média, mediana e desvio padrão do tempo de vida dos gatos em anos.
   3. Crie uma tabela de frequência de país e raça dos gatos
3. Leia a [API de países](https://restcountries.eu/rest/v2/all) e encontre
   1. os 10 maiores países
   2. as 10 línguas mais faladas
   3. o número total de línguas na API de países
4. UCI é um dos lugares mais comuns para obter conjuntos de dados para ciência de dados e machine learning. Leia o conteúdo do UCL (https://archive.ics.uci.edu/ml/datasets.php). Sem bibliotecas adicionais será difícil, então você pode tentar com o BeautifulSoup4

🎉 PARABÉNS ! 🎉

[<< Dia 19](./19_file_handling_pt.md) | [Dia 21 >>](./21_classes_and_objects_pt.md)

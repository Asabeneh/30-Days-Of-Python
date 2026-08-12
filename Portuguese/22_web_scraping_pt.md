<div align="center">
  <h1> 30 Dias de Python: Dia 22 - Web Scraping </h1>
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

[<< Dia 21](./21_classes_and_objects_pt.md) | [Dia 23 >>](./23_virtual_environment_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 22](#-dia-22)
  - [Web Scraping com Python](#web-scraping-com-python)
    - [O que é Web Scraping](#o-que-é-web-scraping)
  - [💻 Exercícios: Dia 22](#-exercícios-dia-22)

# 📘 Dia 22

## Web Scraping com Python

### O que é Web Scraping

A internet está repleta de uma enorme quantidade de dados que podem ser usados para diferentes propósitos. Para coletar esses dados, precisamos saber como extrair (fazer scraping) dados de um website.

Web scraping é o processo de extrair e coletar dados de websites e armazená-los em uma máquina local ou em um banco de dados.

Nesta seção, usaremos os pacotes beautifulsoup e requests para extrair dados. A versão do pacote que estamos usando é o beautifulsoup 4.

Para começar a fazer scraping de websites você precisa de _requests_, _beautifoulSoup4_ e um _website_.

```sh
pip install requests
pip install beautifulsoup4
```

Para extrair dados de websites, é necessário um entendimento básico de tags HTML e seletores CSS. Direcionamos o conteúdo de um website usando tags HTML, classes e/ou ids.
Vamos importar os módulos requests e BeautifulSoup

```py
import requests
from bs4 import BeautifulSoup
```

Vamos declarar a variável url para o website que vamos extrair.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Vamos usar o método get do requests para buscar os dados da url

response = requests.get(url)
# vamos verificar o status
status = response.status_code
print(status) # 200 significa que a busca foi bem-sucedida
```

```sh
200
```

Usando o beautifulSoup para analisar o conteúdo da página

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # obtemos todo o conteúdo do website
soup = BeautifulSoup(content, 'html.parser') # o beautiful soup vai nos dar a chance de analisar (parsear)
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # retorna toda a página do website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# Estamos buscando a tabela com o atributo cellpadding com o valor 3
# Podemos selecionar usando id, class ou tag HTML; para mais informações, consulte a documentação do beautifulsoup
table = tables[0] # o resultado é uma lista, estamos extraindo os dados dela
for td in table.find('tr').find_all('td'):
    print(td.text)
```

Se você executar este código, verá que a extração está apenas parcialmente concluída. Você pode continuar fazendo isso, pois faz parte do exercício 1.
Para referência, consulte a [documentação do beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🌕 Você é muito especial, você está progredindo todos os dias. Faltam apenas oito dias no seu caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 22

1. Extraia o seguinte website e armazene os dados como um arquivo json (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
1. Extraia a tabela desta url (https://archive.ics.uci.edu/ml/datasets.php) e converta-a em um arquivo json
2. Extraia a tabela de presidentes e armazene os dados como json (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). A tabela não é muito bem estruturada e a extração pode levar bastante tempo.

🎉 PARABÉNS ! 🎉

[<< Dia 21](./21_classes_and_objects_pt.md) | [Dia 23 >>](./23_virtual_environment_pt.md)

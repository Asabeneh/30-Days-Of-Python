<div align="center">
  <h1> 30 Jours de Python : Jour 22 - Web Scraping </h1>
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

[<< Jour 21](./21_classes_and_objects_fr.md) | [Jour 23 >>](./23_virtual_environment_fr.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Jour 22](#-jour-22)
  - [Python Web Scraping](#python-web-scraping)
    - [Qu'est-ce que le Web Scraping ?](#quest-ce-que-le-web-scraping-)
  - [💻 Exercices : Jour 22](#-exercices-jour-22)

# 📘 Jour 22

## Python Web Scraping

### Qu'est-ce que le Web Scraping ?

L'internet contient une énorme quantité de données qui peuvent être utilisées à différentes fins. Pour collecter ces données, nous devons savoir comment extraire des données d'un site web.

Le web scraping est le processus d'extraction et de collecte de données à partir de sites web, et de leur stockage sur une machine locale ou dans une base de données.

Dans cette section, nous utiliserons les paquets beautifulsoup et requests pour extraire des données. La version du paquet que nous utilisons est beautifulsoup 4.

Pour commencer à scraper des sites web, vous avez besoin de _requests_, _beautifulSoup4_ et d'un _site web_.

```sh
pip install requests
pip install beautifulsoup4
```

Pour extraire des données de sites web, une compréhension de base des balises HTML et des sélecteurs CSS est nécessaire. Nous ciblons le contenu d'un site web en utilisant des balises HTML, des classes ou/et des identifiants.
Importons les modules requests et BeautifulSoup.

```py
import requests
from bs4 import BeautifulSoup
```

Déclarons une variable url pour le site web que nous allons scraper.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Utilisons la méthode get de requests pour récupérer les données depuis l'url

response = requests.get(url)
# vérifions le statut
status = response.status_code
print(status) # 200 signifie que la récupération a réussi
```

```sh
200
```

Utilisation de BeautifulSoup pour analyser le contenu de la page.

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # nous obtenons tout le contenu du site web
soup = BeautifulSoup(content, 'html.parser') # beautiful soup nous permettra de l'analyser
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # donne la page entière du site
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# Nous ciblons la table avec l'attribut cellpadding ayant la valeur 3
# Nous pouvons sélectionner en utilisant id, class ou une balise HTML, pour plus d'informations consultez la doc beautifulsoup
table = tables[0] # le résultat est une liste, nous en extrayons les données
for td in table.find('tr').find_all('td'):
    print(td.text)
```

Si vous exécutez ce code, vous verrez que l'extraction est à moitié faite. Vous pouvez continuer car cela fait partie de l'exercice 1.
Pour référence, consultez la [documentation beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🌕 Vous êtes si spécial, vous progressez chaque jour. Il ne vous reste plus que huit jours avant d'atteindre la grandeur. Faites maintenant quelques exercices pour votre cerveau et vos muscles.

## 💻 Exercices : Jour 22

1. Scrapez le site web suivant et stockez les données sous forme de fichier json (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
1. Extrayez la table de cette url (https://archive.ics.uci.edu/ml/datasets.php) et convertissez-la en fichier json.
2. Scrapez la table des présidents et stockez les données sous forme de json (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). La table n'est pas très structurée et le scraping peut prendre beaucoup de temps.

🎉 FÉLICITATIONS ! 🎉

[<< Jour 21](./21_classes_and_objects_fr.md) | [Jour 23 >>](./23_virtual_environment_fr.md)

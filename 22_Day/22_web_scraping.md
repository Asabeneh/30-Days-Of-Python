<div align="center">
  <h1> 30 Days Of Python: Day 22 - Web Scraping </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> First Edition: Nov 22 - Dec 22, 2019</small>
  </sub>
</div>
</div>

[<< Day 21](../21_Day/21_class_and_object.md) | [Day 23 >>](../23_Day/23_virtual_environment.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Day 22](#%f0%9f%93%98-day-22)
  - [Python Web Scraping](#python-web-scraping)
    - [What is web scrapping](#what-is-web-scrapping)
  - [💻 Exercises: Day 22](#%f0%9f%92%bb-exercises-day-22)
# 📘 Day 22

## Python Web Scraping

### What is web scrapping

The internet is full huge amount of data which can be used for different uses. To collect this data we need to know how scrape data on a website.

Web scraping is the process of extracting and collecting data from websites and storing the data into a local machine or into a database.

In this section, we will use beautifulsoup and requests package to scape data. The beautifulsoup package we are using beautifulsoup 4.

To start scraping a website you need _requests_, _beautifoulSoup4_ and _website_ to be scrapped.

```sh
pip install requests
pip installl install beautifulsoup4
```

To scrape a data on a website it needs basic understanding of HTML tags and css selectors. We target content from a website using HTML tag, class or an id.
Let's import the requests and BeautifulSoup module

```py
import requests
from bs4 import BeautifulSoup
```

Let's declare url variable for the website which we are going to scrape.

```py

import requests
from bs4 import BeautifulSoup
url = 'http://mlr.cs.umass.edu/ml/datasets.html'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful
```

```sh
200
```

Using beautifulSoup to parse content from the page

```py
import requests
from bs4 import BeautifulSoup
url = 'http://mlr.cs.umass.edu/ml/datasets.html'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
# print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute and the attribute value
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is list, we are taking out from the list
for td in table.find('tr').find_all('td'):
    print(td.text)
```

If you run the above code, you can see that the extraction is half done. You can continue doing it because it is part of exercise 1.
For reference check the beautiful [soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

## 💻 Exercises: Day 22

1. Extract the table in this url (http://mlr.cs.umass.edu/ml/datasets.html) and change it to a json file
2. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States)


🎉 CONGRATULATIONS ! 🎉

[<< Day 21](../21_Day/21_class_and_object.md) | [Day 23 >>](../23_Day/23_virtual_environment.md)
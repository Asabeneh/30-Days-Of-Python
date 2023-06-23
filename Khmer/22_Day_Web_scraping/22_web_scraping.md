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
<small> Second Edition: July, 2021</small>
</sub>
</div>

[<< Day 21](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 22](#-day-22)
  - [Python Web Scraping](#python-web-scraping)
    - [What is Web Scrapping](#what-is-web-scrapping)

# 📘 Day 22

## Python Web Scraping

### What is Web Scrapping


អ៊ីនធឺណិតពោរពេញទៅដោយទិន្នន័យដ៏ច្រើន ដែលអាចប្រើប្រាស់សម្រាប់គោលដៅផ្សេងៗ ។ ដើម្បីប្រមូលទិន្នន័យនេះយើងត្រូវដឹងពីរបៀបរុករក (scrape) ទិន្នន័យពីគេហទំព័រ ។

ការរុករកវេបសាយ គឺជាដំណើរការនៃការទាញយកនិងប្រមូលទិន្នន័យពីគេហទំព័រ និងរក្សាទុកវានៅលើម៉ាស៊ីនឬក្នុងទិន្នន័យ។

នៅក្នុងផ្នែកនេះយើងនឹងប្រើ beautifulsoup និង request package ដើម្បីរុករកទិន្នន័យ។ ប្រភេទកញ្ចប់ដែលយើងកំពុងប្រើគឺ beautifulsoup 4 ។

ដើម្បីចាប់ផ្ដើមរុករកគេហទំព័រ អ្នកត្រូវការ _requests_, _beautifoulSoup4_ and a _website_.

```sh
pip install requests
pip install beautifulsoup4
```

ដើម្បីរុករកទិន្នន័យពីគេហទំព័រ ការយល់ដឹងជាមូលដ្ឋាននៃ HTML tags និង CSS selectors ត្រូវការ។ យើងបានចាប់យកមាតិកាពីគេហទំព័រមួយ ដោយប្រើ HTML tags, classes ឬ/និង ids ។

សូមយើងនាំចូល (import) requests និង BeautifulSoup module

```py
import requests
from bs4 import BeautifulSoup
```

យើងត្រូវប្រកាសថា url variable សម្រាប់ website ដែលយើងនឹងរុករក ។

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful
```

```sh
200
```

ប្រើ beautifulSoup ដើម្បីពិនិត្យមាតិកាពីទំព័រ

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is a list, we are taking out data from it
for td in table.find('tr').find_all('td'):
    print(td.text)
```

ប្រសិនបើអ្នករត់កូដនេះ អ្នកអាចមើលឃើញថា ការទាញយកគឺបានបញ្ចប់ពាក់កណ្តាល ។ អ្នកអាចបន្តធ្វើវាបាន
សម្រាប់ការណែនាំ សូមមើល [beautifulsoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🎉 CONGRATULATIONS ! 🎉

[<< Day 21](../21_Day_Web_scraping/21_class_and_object.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)

<div align="center">
  <h1> 30 дней Python: День 22 - Веб-скрапинг </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Асабенех Йетаех</a><br>
<small>Второе издание: июль 2021</small>
</sub>
</div>

[<< День 21](../21_Day_Classes_and_objects/21_classes_and_objects.md) | [День 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 22](#-день-22)
  - [Веб-скрапинг на Python](#веб-скрапинг-на-python)
    - [Что такое веб-скрапинг](#что-такое-веб-скрапинг)
  - [💻 Упражнения: День 22](#-упражнения-день-22)

# 📘 День 22

## Веб-скрапинг на Python

### Что такое веб-скрапинг

Интернет полон огромного количества данных, которые можно использовать для разных целей. Чтобы собирать эти данные, нам нужно знать, как извлекать данные с веб-сайта.

Веб-скрапинг - это процесс извлечения и сбора данных с веб-сайтов и их сохранения на локальной машине или в базе данных.

В этом разделе мы будем использовать пакеты beautifulsoup и requests для извлечения данных. Версия пакета, которую мы используем, - beautifulsoup 4.

Чтобы начать извлекать данные с веб-сайтов, вам нужны _requests_, _beautifoulSoup4_ и _веб-сайт_.

```sh
pip install requests
pip install beautifulsoup4
```

Для извлечения данных с веб-сайтов необходимо базовое понимание HTML-тегов и CSS-селекторов. Мы нацеливаемся на содержимое веб-сайта с помощью HTML-тегов, классов и/или id.
Давайте импортируем модули requests и BeautifulSoup

```py
import requests
from bs4 import BeautifulSoup
```

Давайте объявим переменную url для веб-сайта, с которого мы будем извлекать данные.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Давайте используем метод get модуля requests, чтобы получить данные по url

response = requests.get(url)
# давайте проверим статус
status = response.status_code
print(status) # 200 означает, что получение данных прошло успешно
```

```sh
200
```

Используем beautifulSoup для разбора содержимого страницы

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # получаем всё содержимое с веб-сайта
soup = BeautifulSoup(content, 'html.parser') # beautiful soup даёт возможность разбирать (parse)
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # выдаёт всю страницу веб-сайта
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# Мы нацеливаемся на таблицу с атрибутом cellpadding и значением 3
# Мы можем выбирать, используя id, класс или HTML-тег, для получения дополнительной информации посмотрите документацию beautifulsoup
table = tables[0] # результат - это список, мы берём данные из него
for td in table.find('tr').find_all('td'):
    print(td.text)
```

Если вы запустите этот код, вы увидите, что извлечение выполнено наполовину. Вы можете продолжить, потому что это часть упражнения 1.
Для справки ознакомьтесь с [документацией beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🌕 Вы особенный, вы прогрессируете каждый день. Вам осталось всего восемь дней на пути к величию. Теперь выполните несколько упражнений для своего мозга и мышц.

## 💻 Упражнения: День 22

1. Извлеките данные со следующего веб-сайта и сохраните данные в виде json файла (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
1. Извлеките таблицу по этому url (https://archive.ics.uci.edu/ml/datasets.php) и преобразуйте её в json файл
2. Извлеките таблицу президентов и сохраните данные как json (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). Таблица не очень структурирована, и извлечение может занять очень много времени.

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 21](../21_Day_Web_scraping/21_class_and_object.md) | [День 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)

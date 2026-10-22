<div align="center">
  <h1> 30 Days Of Python: День 22 - Веб-скрапинг </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Второе издание: июль 2021</small>
</sub>
</div>

[<< День 21](./21_classes_and_objects_ru.md) | [День 23 >>](./23_virtual_environment_ru.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 22](#-день-22)
  - [Python веб-скрапинг](#python-веб-скрапинг)
    - [Что такое веб-скрапинг](#что-такое-веб-скрапинг)
  - [💻 Упражнения: День 22](#-упражнения-день-22)

# 📘 День 22

## Python веб-скрапинг

### Что такое веб-скрапинг

Интернет полон огромного количества данных, которые можно использовать для разных целей. Чтобы собрать эти данные, нам нужно знать, как скрапить данные с сайта.

Веб-скрапинг — это процесс извлечения и сбора данных с сайтов и сохранения их на локальной машине или в базе данных.

В этом разделе мы будем использовать пакеты beautifulsoup и requests для скрапинга данных. Используемая нами версия пакета — beautifulsoup 4.

Чтобы начать скрапить сайты, вам нужны _requests_, _beautifoulSoup4_ и _сайт_.

```sh
pip install requests
pip install beautifulsoup4
```

Чтобы скрапить данные с сайтов, нужно базовое понимание HTML-тегов и CSS-селекторов. Мы выбираем контент с сайта с помощью HTML-тегов, классов или/и id.
Давайте импортируем модули requests и BeautifulSoup

```py
import requests
from bs4 import BeautifulSoup
```

Давайте объявим переменную url для сайта, который мы собираемся скрапить.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Используем метод get из requests, чтобы получить данные по url

response = requests.get(url)
# проверим статус
status = response.status_code
print(status) # 200 означает, что получение данных прошло успешно
```

```sh
200
```

Используем beautifulSoup, чтобы разобрать контент страницы

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # получаем весь контент с сайта
soup = BeautifulSoup(content, 'html.parser') # beautiful soup даёт возможность разобрать
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # возвращает всю страницу сайта
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# Мы нацеливаемся на таблицу с атрибутом cellpadding со значением 3
# Мы можем выбирать с помощью id, class или HTML-тега, для получения дополнительной информации смотрите документацию beautifulsoup
table = tables[0] # результат — список, мы извлекаем из него данные
for td in table.find('tr').find_all('td'):
    print(td.text)
```

Если вы запустите этот код, то увидите, что извлечение сделано наполовину. Вы можете продолжить его, потому что это часть упражнения 1.
Для справки смотрите [документацию beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🌕 Вы такие особенные, вы продвигаетесь каждый день. Вам осталось всего восемь дней на пути к величию. Теперь сделайте несколько упражнений для мозга и мышц.

## 💻 Упражнения: День 22

1. Скрапьте следующий сайт и сохраните данные в json-файл (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
1. Извлеките таблицу по этому url (https://archive.ics.uci.edu/ml/datasets.php) и преобразуйте её в json-файл
2. Скрапьте таблицу президентов и сохраните данные в json (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). Таблица не очень структурирована, и скрапинг может занять очень много времени.

🎉 ПОЗДРАВЛЯЕМ ! 🎉

[<< День 21](./21_classes_and_objects_ru.md) | [День 23 >>](./23_virtual_environment_ru.md)

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

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 22](#-day-22)
  - [Python 웹 스크래핑](#python-웹-스크래핑)
    - [웹 스크래핑이란?](#웹-스크래핑이란)
  - [💻 연습문제: Day 22](#-연습문제-day-22)

# 📘 Day 22

## Python 웹 스크래핑

### 웹 스크래핑이란?

인터넷에는 다양한 목적으로 사용할 수 있는 방대한 양의 데이터가 있습니다. 이 데이터를 수집하려면 웹사이트에서 데이터를 스크래핑하는 방법을 알아야 합니다.

웹 스크래핑은 웹사이트에서 데이터를 추출하고 수집하여 로컬 머신이나 데이터베이스에 저장하는 프로세스입니다.

이 섹션에서는 beautifulsoup와 requests 패키지를 사용하여 데이터를 스크래핑할 것입니다. 사용하는 패키지 버전은 beautifulsoup 4입니다.

웹사이트 스크래핑을 시작하려면 _requests_, _beautifoulSoup4_ 및 _website_가 필요합니다.

```sh
pip install requests
pip install beautifulsoup4
```

웹사이트에서 데이터를 스크래핑하려면 HTML 태그와 CSS 선택자에 대한 기본적인 이해가 필요합니다. HTML 태그, 클래스 또는/그리고 id를 사용하여 웹사이트의 콘텐츠를 대상으로 합니다.
requests와 BeautifulSoup 모듈을 임포트해 봅시다.

```py
import requests
from bs4 import BeautifulSoup
```

스크래핑할 웹사이트의 url 변수를 선언해 봅시다.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# requests의 get 메서드를 사용하여 url에서 데이터를 가져옵니다

response = requests.get(url)
# 상태를 확인합니다
status = response.status_code
print(status) # 200은 가져오기가 성공했음을 의미합니다
```

```sh
200
```

beautifulSoup를 사용하여 페이지의 콘텐츠를 파싱합니다

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # 웹사이트에서 모든 콘텐츠를 가져옵니다
soup = BeautifulSoup(content, 'html.parser') # beautiful soup가 파싱할 수 있게 해줍니다
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # 웹사이트의 전체 페이지를 제공합니다
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# cellpadding 속성 값이 3인 테이블을 대상으로 합니다
# id, class 또는 HTML 태그를 사용하여 선택할 수 있습니다. 자세한 정보는 beautifulsoup 문서를 확인하세요
table = tables[0] # 결과는 리스트이므로 데이터를 꺼냅니다
for td in table.find('tr').find_all('td'):
    print(td.text)
```

이 코드를 실행하면 추출이 절반만 완료된 것을 볼 수 있습니다. 이것은 연습문제 1의 일부이므로 계속 진행할 수 있습니다.
참고로 [beautifulsoup 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)를 확인하세요.

🌕 당신은 정말 특별합니다. 매일 발전하고 있습니다. 위대함을 향한 여정에서 이제 8일만 남았습니다. 이제 두뇌와 근육을 위한 연습을 해보세요.

## 💻 연습문제: Day 22

1. 다음 웹사이트를 스크래핑하고 데이터를 json 파일로 저장하세요(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
1. 이 url(https://archive.ics.uci.edu/ml/datasets.php)의 테이블을 추출하여 json 파일로 변환하세요.
2. 대통령 테이블을 스크래핑하고 데이터를 json으로 저장하세요(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 테이블이 잘 구조화되어 있지 않아 스크래핑에 매우 오랜 시간이 걸릴 수 있습니다.

🎉 축하합니다! 🎉

[<< Day 21](../21_Day_Web_scraping/21_class_and_object.md) | [Day 23 >>](../23_Day_Virtual_environment/23_virtual_environment.md)

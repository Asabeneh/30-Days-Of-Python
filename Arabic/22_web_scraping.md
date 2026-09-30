<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 22 - استخراج بيانات الويب</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="متابعة في تويتر" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>المؤلف:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>الطبعة الثانية: يوليو 2021</small>
  </sub>
</div>

[<< اليوم 21](./21_classes_and_objects.md) | [اليوم 23 >>](./23_virtual_environment.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 22](#-اليوم-22)
  - [استخراج بيانات الويب مع بايثون](#استخراج-بيانات-الويب-مع-بايثون)
    - [ما هو استخراج بيانات الويب](#ما-هو-استخراج-بيانات-الويب)
  - [💻 تمارين: اليوم 22](#-تمارين-اليوم-22)

# 📘 اليوم 22

## استخراج بيانات الويب مع بايثون

### ما هو استخراج بيانات الويب

الإنترنت مليء بكمية هائلة من البيانات التي يمكن استخدامها لأغراض مختلفة. لجمع هذه البيانات نحتاج إلى معرفة كيفية استخراج البيانات من موقع ويب.

استخراج بيانات الويب ('Web scraping') هو عملية استخراج وجمع البيانات من مواقع الويب وتخزينها على جهاز محلي أو في قاعدة بيانات.

في هذا القسم، سنستخدم حزمتي 'beautifulsoup' و 'requests' لاستخراج البيانات. إصدار الحزمة الذي نستخدمه هو 'beautifulsoup' 4.

لبدء استخراج مواقع الويب تحتاج إلى 'requests' و 'beautifulSoup4' و 'موقع ويب'.

```sh
pip install requests
pip install beautifulsoup4
```

لاستخراج البيانات من مواقع الويب، هناك حاجة إلى فهم أساسي لوسوم 'HTML' ومحددات 'CSS'. نستهدف المحتوى من موقع ويب باستخدام وسوم 'HTML' أو فئات أو/و معرّفات.
دعنا نستورد وحدتي 'requests' و 'BeautifulSoup'

```py
import requests
from bs4 import BeautifulSoup
```

دعنا نعلن متغير 'url' للموقع الذي سنقوم باستخراج البيانات منه.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# لنستخدم طريقة 'get' من 'requests' لجلب البيانات من 'url'

response = requests.get(url)
# لنفحص الحالة
status = response.status_code
print(status) # 200 يعني أن الجلب كان ناجحًا
```

```sh
200
```

باستخدام 'beautifulSoup' لتحليل المحتوى من الصفحة

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # نحصل على كل المحتوى من الموقع
soup = BeautifulSoup(content, 'html.parser') # beautiful soup ستتيح لنا فرصة التحليل
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # يعطي الصفحة بأكملها على الموقع
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# نستهدف الجدول بسمة cellpadding بقيمة 3
# يمكننا التحديد باستخدام 'id' أو 'class' أو وسم 'HTML'، لمزيد من المعلومات تحقق من توثيق 'beautifulsoup'
table = tables[0] # النتيجة قائمة، نأخذ البيانات منها
for td in table.find('tr').find_all('td'):
    print(td.text)
```

إذا قمت بتشغيل هذا الكود، يمكنك أن ترى أن الاستخراج قد اكتمل في منتصفه. يمكنك مواصلة القيام به لأنه جزء من التمرين 1.
كمرجع تحقق من [توثيق 'beautifulsoup'](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

🌕 أنت مميز جدًا، أنت تتقدم كل يوم. لم يتبقَّ لك سوى ثمانية أيام في طريقك إلى العظمة. الآن قم ببعض التمارين لعقلك وعضلاتك.

## 💻 تمارين: اليوم 22

1. استخرج الموقع التالي وخزّن البيانات كملف json (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
2. استخرج الجدول في هذا الرابط (https://archive.ics.uci.edu/ml/datasets.php) وحوّله إلى ملف json
3. استخرج جدول الرؤساء وخزّن البيانات كـ 'json' (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). الجدول ليس منظمًا جدًا وقد يستغرق الاستخراج وقتًا طويلًا جدًا.

🎉 مبروك! 🎉

[<< اليوم 21](./21_classes_and_objects.md) | [اليوم 23 >>](./23_virtual_environment.md)
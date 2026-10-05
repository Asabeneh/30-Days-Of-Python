<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 22 — ویب اسکریپنگ</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../22_Day_Web_scraping/22_web_scraping.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 21](./21_classes_and_objects.md) | [فہرست](./readme.md) | [اگلا دن: 23](./23_virtual_environment.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 22](#day-22-section-1)
  - [پائتھن سے ویب اسکریپنگ](#day-22-section-2)
    - [ویب اسکریپنگ کیا ہے؟](#day-22-section-3)
  - [💻 مشقیں — دن 22](#day-22-section-4)

<a id="day-22-section-1"></a>

# 📘 دن 22

<a id="day-22-section-2"></a>

## پائتھن سے ویب اسکریپنگ

<a id="day-22-section-3"></a>

### ویب اسکریپنگ کیا ہے؟

انٹرنیٹ پر بہت سا ڈیٹا موجود ہے۔ ویب سائٹس سے مطلوبہ ڈیٹا نکالنے، جمع کرنے اور مقامی فائل یا ڈیٹابیس میں محفوظ کرنے کو ویب اسکریپنگ کہتے ہیں۔

اس حصے میں `requests` اور Beautiful Soup 4 استعمال کریں گے۔ آغاز کے لیے یہ پیکیجز اور ایک ویب سائٹ درکار ہے۔

<div dir="ltr">

```sh
pip install requests
pip install beautifulsoup4
```

</div>

HTML ٹیگز اور CSS selectors کی بنیادی سمجھ ضروری ہے۔ ٹیگ، class یا id سے مطلوبہ مواد منتخب کرتے ہیں۔ `requests` اور `BeautifulSoup` امپورٹ کریں۔

<div dir="ltr">

```py
import requests
from bs4 import BeautifulSoup
```

</div>

مطلوبہ ویب سائٹ کا URL متغیر میں رکھیں۔

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
200
```

</div>

صفحے کا مواد Beautiful Soup سے پڑھیں۔

<div dir="ltr">

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

</div>

یہ مثال ڈیٹا نکالنے کا آغاز کرتی ہے۔ باقی کام پہلی مشق میں مکمل کریں۔ مزید کے لیے [Beautiful Soup کی دستاویزات](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start) دیکھیں۔

🌕 اب صرف آٹھ دن باقی ہیں! مشق جاری رکھیں۔

<a id="day-22-section-4"></a>

## 💻 مشقیں — دن 22

1. `http://www.bu.edu/president/boston-university-facts-stats/` سے ڈیٹا نکال کر JSON فائل میں محفوظ کریں۔
2. [UCI کے اصل سبق والے صفحے](https://archive.ics.uci.edu/ml/datasets.php) کی جدول JSON میں بدلیں۔
3. [امریکی صدور کی فہرست](https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States) کی جدول JSON میں محفوظ کریں۔ جدول کی پیچیدہ ساخت کی وجہ سے وقت لگ سکتا ہے۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 21](./21_classes_and_objects.md) | [فہرست](./readme.md) | [اگلا دن: 23](./23_virtual_environment.md)

</div>

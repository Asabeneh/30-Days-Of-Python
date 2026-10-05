<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 23 — ورچوئل ماحول</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../23_Day_Virtual_environment/23_virtual_environment.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 22](./22_web_scraping.md) | [فہرست](./readme.md) | [اگلا دن: 24](./24_statistics.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 23](#day-23-section-1)
  - [ورچوئل ماحول تیار کرنا](#day-23-section-2)
  - [💻 مشقیں — دن 23](#day-23-section-3)

<a id="day-23-section-1"></a>

# 📘 دن 23

<a id="day-23-section-2"></a>

## ورچوئل ماحول تیار کرنا

نئے منصوبے کے لیے الگ ورچوئل ماحول بنانا مفید ہے۔ اس سے مختلف منصوبوں کے پیکیجز اور ورژن ایک دوسرے سے نہیں ٹکراتے۔ `pip freeze` موجودہ ماحول کے پیکیجز دکھاتا ہے۔ ورچوئل ماحول فعال ہو تو اسی منصوبے کے پیکیجز تک رسائی ہوتی ہے۔ ٹرمینل میں `virtualenv` انسٹال کریں۔

<div dir="ltr">

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

</div>

`30DaysOfPython` کے اندر `flask_project` بنائیں۔ اس فولڈر میں جا کر ورچوئل ماحول بنائیں۔

Mac/Linux کے لیے:

<div dir="ltr">

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

```

</div>

ونڈوز کے لیے:

<div dir="ltr">

```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

</div>

یہاں ماحول کا نام `venv` رکھا گیا ہے؛ کوئی اور نام بھی رکھ سکتے ہیں۔ `ls` یا ونڈوز کمانڈ پرامپٹ میں `dir` سے فولڈر کی موجودگی جانچیں۔

<div dir="ltr">

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

</div>

منصوبے کے فولڈر میں رہ کر ماحول فعال کریں۔

Mac/Linux:

<div dir="ltr">

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```

</div>

ونڈوز میں PowerShell اور Git Bash کی کمانڈز مختلف ہیں۔

Windows PowerShell:

<div dir="ltr">

```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

</div>

Windows Git Bash:

<div dir="ltr">

```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

</div>

فعال ہونے پر ٹرمینل کے prompt میں `venv` نظر آئے گا۔

<div dir="ltr">

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

</div>

`pip freeze` سے منصوبے کے پیکیجز دیکھیں۔ اصل مثال کے نئے ماحول میں فہرست خالی ہے۔

ایک چھوٹے Flask منصوبے کے لیے Flask انسٹال کریں۔

<div dir="ltr">

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

</div>

دوبارہ `pip freeze` سے فہرست دیکھیں۔

<div dir="ltr">

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

</div>

کام ختم ہونے پر `deactivate` سے ماحول غیر فعال کریں۔

<div dir="ltr">

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

</div>

اب Flask منصوبے کے لیے ضروری پیکیجز موجود ہیں۔ `venv` کو `.gitignore` میں شامل کریں تاکہ ماحول کی فائلیں GitHub پر اپ لوڈ نہ ہوں۔

<a id="day-23-section-3"></a>

## 💻 مشقیں — دن 23

1. اوپر کی مثال کے مطابق ورچوئل ماحول والا منصوبہ بنائیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 22](./22_web_scraping.md) | [فہرست](./readme.md) | [اگلا دن: 24](./24_statistics.md)

</div>

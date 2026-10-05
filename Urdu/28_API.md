<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 28 — API کا تعارف</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../28_Day_API/28_API.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 27](./27_python_with_mongodb.md) | [فہرست](./readme.md) | [اگلا دن: 29](./29_building_API.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 28](#day-28-section-1)
- [ایپلی کیشن پروگرامنگ انٹرفیس: API](#day-28-section-2)
  - [API](#day-28-section-3)
  - [API بنانا](#day-28-section-4)
  - [HTTP: Hypertext Transfer Protocol](#day-28-section-5)
  - [HTTP کی ساخت](#day-28-section-6)
  - [درخواست کی ابتدائی سطر](#day-28-section-7)
    - [جواب کی ابتدائی سطر: Status Line](#day-28-section-8)
    - [Header خانے](#day-28-section-9)
    - [پیغام کی body](#day-28-section-10)
    - [درخواست کے طریقے](#day-28-section-11)
  - [💻 مشقیں — دن 28](#day-28-section-12)

<a id="day-28-section-1"></a>

# 📘 دن 28

<a id="day-28-section-2"></a>

# ایپلی کیشن پروگرامنگ انٹرفیس: API

<a id="day-28-section-3"></a>

## API

API کا مطلب Application Programming Interface ہے۔ اس حصے میں Web APIs دیکھیں گے۔ ویب API متعین کرتی ہے کہ کسی خدمت اور اسے استعمال کرنے والی ایپلی کیشن کے درمیان رابطہ کیسے ہو گا، کون سے کام دستیاب ہوں گے اور کن URLs پر درخواست بھیجنی ہے۔ خدمت کی شرائط یا SLA دستیابی اور ذمہ داریوں کو الگ سے بیان کر سکتے ہیں۔

ویب ڈیولپمنٹ میں API درخواستوں، مثلاً HTTP پیغامات، اور جواب کی ساخت کی وضاحت کرتی ہے۔ جواب عموماً JSON یا XML میں ہوتا ہے۔

اصل سبق ویب خدمات کے SOAP اور SOA سے REST طرز کے وسائل کی طرف رجحان بیان کرتا ہے۔ مختلف خدمات میں مختلف طرز استعمال ہوتے ہیں۔

سوشل میڈیا کی APIs سے مختلف پلیٹ فارم اور برادریاں مواد اور ڈیٹا کا تبادلہ کر سکتی ہیں۔ ایک جگہ بنایا گیا مواد API کے ذریعے دوسری جگہوں پر شائع یا تازہ کیا جا سکتا ہے۔

اصل سبق کی مثال میں Twitter کی REST API بنیادی ڈیٹا اور Search API تلاش اور رجحانات تک رسائی دیتی تھی۔ یہ تاریخی مثال ہے؛ کسی سروس کی موجودہ API اور رسائی کی شرائط الگ جانچیں۔

مزید مثالیں [ممالک کی API](https://restcountries.eu/rest/v2/all) اور [بلیوں کی نسلوں کی API](https://api.thecatapi.com/v1/breeds) ہیں۔

یہاں RESTful API میں GET، PUT، POST اور DELETE سے ڈیٹا کے ساتھ کام کریں گے۔

<a id="day-28-section-4"></a>

## API بنانا

RESTful API میں HTTP درخواستوں سے وسائل حاصل، تخلیق، تبدیل اور حذف کیے جاتے ہیں۔ پچھلے اسباق میں پائتھن، Flask اور MongoDB پڑھ چکے ہیں۔ انہیں ملا کر CRUD، یعنی Create، Read، Update اور Delete، والی API بنائیں گے۔

اس سے پہلے HTTP اور درخواست/جواب کا چکر سمجھنا مفید ہے۔

<a id="day-28-section-5"></a>

## HTTP: Hypertext Transfer Protocol

HTTP کلائنٹ اور سرور کے درمیان رابطے کا پروٹوکول ہے۔ اس مثال میں براؤزر کلائنٹ ہے اور سرور وسائل فراہم کرتا ہے۔ وسائل HTML، تصاویر، تلاش کے نتائج، اسکرپٹس یا دوسری فائلیں ہو سکتے ہیں۔

براؤزر HTTP سرور کو درخواست بھیجتا ہے اور سرور جواب واپس دیتا ہے۔

<a id="day-28-section-6"></a>

## HTTP کی ساخت

HTTP کلائنٹ–سرور نمونہ استعمال کرتا ہے۔ کلائنٹ درخواست اور سرور جواب بھیجتا ہے۔ اصل سبق اتصال بند ہونے کی سادہ صورت دکھاتا ہے؛ عملی طور پر ایک اتصال کئی درخواستوں کے لیے برقرار بھی رہ سکتا ہے۔

![HTTP درخواست اور جواب کا چکر](../images/http_request_response_cycle.png)

HTTP/1.x درخواست اور جواب کے پیغامات کی عمومی ساخت:

- ابتدائی سطر۔
- صفر یا زیادہ header سطریں۔
- ایک خالی سطر، یعنی CRLF۔
- اختیاری body، مثلاً فائل، بھیجا ہوا ڈیٹا یا نتیجہ۔

[اصل نمونہ ایپ](https://thirtydaysofpython-v1-final.herokuapp.com/) میں درخواست اور جواب دیکھیں۔ اسے اصل کورس میں Heroku کے مفت dyno پر رکھا گیا تھا؛ اس پرانے نمونے کی مسلسل دستیابی کی ضمانت نہیں۔ مصنف نے سرور جاری رکھنے کے لیے تعاون کی درخواست کی ہے۔

![درخواست اور جواب کے headers](../images/request_response_header.png)

<a id="day-28-section-7"></a>

## درخواست کی ابتدائی سطر

درخواست کی پہلی سطر جواب کی status line سے مختلف ہے۔ اس کے تین حصے خالی جگہ سے الگ ہوتے ہیں:

- طریقہ، مثلاً GET، POST یا HEAD۔
- مطلوبہ وسیلے کا path۔
- HTTP ورژن۔

مثال: `GET / HTTP/1.1`۔ GET عام طور پر وسیلہ پڑھنے اور POST ڈیٹا بھیجنے یا وسیلہ بنانے کے لیے ہوتا ہے۔

<a id="day-28-section-8"></a>

### جواب کی ابتدائی سطر: Status Line

جواب کی سطر میں HTTP ورژن، status code اور اس کی مختصر وجہ ہوتی ہے۔ مثالیں:

- `HTTP/1.0 200 OK`
- `HTTP/1.0 404 Not Found`

`200 OK` کامیابی ظاہر کرتا ہے؛ مطلوبہ نتیجہ عموماً body میں ملتا ہے۔ `500` سرور کی اندرونی خرابی ہے۔ مزید codes [اس فہرست](https://httpstatuses.com/) یا [تصویری مثالوں](https://httpstatusdogs.com/) میں دیکھیں۔

<a id="day-28-section-9"></a>

### Header خانے

Headers درخواست، جواب یا body کے مواد کے بارے میں معلومات دیتے ہیں۔

<div dir="ltr">

```sh
GET / HTTP/1.1
Host: thirtydaysofpython-v1-final.herokuapp.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Referer: https://thirtydaysofpython-v1-final.herokuapp.com/post
Accept-Encoding: gzip, deflate, br
Accept-Language: en-GB,en;q=0.9,fi-FI;q=0.8,fi;q=0.7,en-CA;q=0.6,en-US;q=0.5,fr;q=0.4
```

</div>

<a id="day-28-section-10"></a>

### پیغام کی body

Headers کے بعد body میں ڈیٹا آ سکتا ہے۔ جواب میں مطلوبہ وسیلہ یا خرابی کی وضاحت، جبکہ درخواست میں صارف کا ان پٹ یا اپ لوڈ کی گئی فائل ہو سکتی ہے۔

متعلقہ headers body کی وضاحت کرتے ہیں:

- `Content-Type`: MIME قسم، مثلاً `text/html`، `application/json`، `text/plain`، `text/css` یا `image/gif`۔
- `Content-Length`: body کے bytes کی تعداد، جب یہ header موجود ہو۔

<a id="day-28-section-11"></a>

### درخواست کے طریقے

ہم API کے CRUD کاموں کے لیے یہ طریقے استعمال کریں گے:

1. **GET:** دی گئی URI سے معلومات حاصل کرنا؛ اس سے سرور کا ڈیٹا تبدیل نہیں ہونا چاہیے۔
2. **POST:** سرور کو ڈیٹا بھیجنا، مثلاً نئی پوسٹ یا فارم/فائل اپ لوڈ کرنا۔
3. **PUT:** مطلوبہ وسیلے کی نمائندگی دیے گئے مواد سے بدلنا۔
4. **DELETE:** وسیلہ حذف کرنا۔

<a id="day-28-section-12"></a>

## 💻 مشقیں — دن 28

1. API اور HTTP کے بارے میں پڑھیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 27](./27_python_with_mongodb.md) | [فہرست](./readme.md) | [اگلا دن: 29](./29_building_API.md)

</div>

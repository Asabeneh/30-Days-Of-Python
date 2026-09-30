<div align="center">
  <h1> 30 يوماً من بايثون: اليوم 28 - واجهة برمجة التطبيقات </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>المؤلف:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>الطبعة الثانية: يوليو 2021</small>
</sub>

</div>
</div>

[<< اليوم 27](./27_python_with_mongodb.md) | [اليوم 29 >>](./29_building_API.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 28](#-day-28)
- [واجهة برمجة التطبيقات 'API'](#application-programming-interfaceapi)
  - ['API'](#api)
  - [بناء 'API'](#building-api)
  - ['HTTP' (بروتوكول نقل النص الفائق)](#httphypertext-transfer-protocol)
  - [هيكل 'HTTP'](#structure-of-http)
  - [سطر الطلب الأولي (سطر الحالة)](#initial-request-linestatus-line)
    - [سطر الاستجابة الأولي (سطر الحالة)](#initial-response-linestatus-line)
    - [حقول الرأس](#header-fields)
    - [جسم الرسالة](#the-message-body)
    - [طرق الطلب](#request-methods)
  - [💻 التمارين: اليوم 28](#-exercises-day-28)

# 📘 اليوم 28

# واجهة برمجة التطبيقات 'API'

## 'API'

'API' تعني 'Application Programming Interface' أو واجهة برمجة التطبيقات. نوع 'API' الذي سنغطيه في هذا القسم سيكون 'Web APIs' أو واجهات برمجة تطبيقات الويب.
واجهات برمجة تطبيقات الويب هي الواجهات المحددة التي تحدث من خلالها التفاعلات بين المؤسسات والتطبيقات التي تستخدم أصولها، وهي أيضاً اتفاقية مستوى الخدمة 'SLA' لتحديد المزود الوظيفي وعرض مسار الخدمة أو 'URL' لمستخدمي 'API' الخاص به.

في سياق تطوير الويب، يتم تعريف 'API' كمجموعة من المواصفات، مثل رسائل طلب 'HTTP' أو 'Hypertext Transfer Protocol' (بروتوكول نقل النص الفائق)، مع تعريف لهيكل رسائل الاستجابة، عادةً بتنسيق 'XML' أو 'JSON' أو 'JavaScript Object Notation'.

انتقلت 'Web API' من خدمات الويب القائمة على 'SOAP' أو 'Simple Object Access Protocol' وهندسة الخدمات الموجهة 'SOA' نحو موارد الويب الأكثر مباشرة بنمط 'REST' أو 'Representational State Transfer'.

خدمات وسائل التواصل الاجتماعي، سمحت 'Web APIs' لمجتمعات الويب بمشاركة المحتوى والبيانات بين المجتمعات والمنصات المختلفة.

باستخدام 'API'، يمكن لنشر وتحديث المحتوى الذي يتم إنشاؤه في مكان واحد ديناميكياً في مواقع متعددة على الويب.

على سبيل المثال، تتيح 'REST API' الخاصة بتويتر للمطورين الوصول إلى بيانات تويتر الأساسية، وتوفر 'Search API' طرقاً للمطورين للتفاعل مع بيانات بحث تويتر والاتجاهات.

توفر العديد من التطبيقات نقاط نهاية لـ 'API'. بعض الأمثلة على 'API' مثل [API](https://restcountries.eu/rest/v2/all) للدول، و [API](https://api.thecatapi.com/v1/breeds) لسلالات القطط.

في هذا القسم، سنغطي 'RESTful API' التي تستخدم طرق طلب 'HTTP' للحصول على البيانات و 'PUT' و 'POST' وحذف البيانات.

## بناء 'API'

'RESTful API' هي واجهة برنامج تطبيقات (API) تستخدم طلبات 'HTTP' للحصول على البيانات و 'PUT' و 'POST' وحذف البيانات. في الأقسام السابقة، تعلمنا عن 'Python' و 'Flask' و 'MongoDB'. سنستخدم المعرفة التي اكتسبناها لتطوير 'RESTful API' باستخدام 'Python Flask' وقاعدة بيانات 'MongoDB'. كل تطبيق لديه عملية 'CRUD' (إنشاء، قراءة، تحديث، حذف) لديه 'API' لإنشاء البيانات، والحصول على البيانات، أو تحديث البيانات، أو حذف البيانات من قاعدة بيانات.

لبناء 'API'، من الجيد فهم بروتوكول 'HTTP' ودورة طلب و استجابة 'HTTP'.

## 'HTTP' (بروتوكول نقل النص الفائق)

'HTTP' هو بروتوكول تواصل موثوق بين العميل والخادم. العميل في هذه الحالة هو المتصفح والخادم هو المكان الذي تصل منه إلى البيانات. 'HTTP' هو بروتوكول شبكة مستخدم لتوصيل الموارد التي قد تكون ملفات على الويب العالمية، سواء كانت ملفات HTML أو صور أو نتائج استعلامات أو نصوص برمجية أو أنواع ملفات أخرى.

المتصفح هو عميل 'HTTP' لأنه يرسل طلبات إلى خادم 'HTTP' (خادم الويب)، الذي يرسل بدوره الاستجابات إلى العميل.

## هيكل 'HTTP'

يستخدم 'HTTP' نموذج العميل-الخادم. يفتح عميل 'HTTP' اتصالاً ويرسل رسالة طلب إلى خادم 'HTTP' ويرد خادم 'HTTP' برسالة استجابة وهي الموارد المطلوبة. عند اكتمال دورة طلب-استجابة، يغلق الخادم الاتصال.

![دورة طلب واستجابة HTTP](../images/http_request_response_cycle.png)

تنسيق رسائل الطلب والاستجابة متشابه. كلا النوعين من الرسائل يحتويان على

- سطر أولي،
- صفر أو أكثر من خطوط الرأس،
- سطر فارغ (أي CRLF بمفرده)، و
- جسم رسالة اختياري (مثل ملف، أو بيانات استعلام، أو مخرجات استعلام).

دعنا نأخذ مثالاً على رسائل الطلب والاستجابة من خلال زيارة هذا الموقع: https://thirtydaysofpython-v1-final.herokuapp.com/. تم نشر هذا الموقع على 'Heroku free dyno' وقد لا يعمل خلال بعض الأشهر بسبب كثرة الطلبات. ادعم هذا العمل ليبقى الخادم يعمل طوال الوقت.

![طلب واستجابة الرأس](../images/request_response_header.png)

## سطر الطلب الأولي (سطر الحالة)

يختلف سطر الطلب الأولي عن الاستجابة.
يحتوي سطر الطلب على ثلاثة أجزاء، مفصولة بمسافات:

- اسم الطريقة 'GET' أو 'POST' أو 'HEAD'
- مسار المورد المطلوب،
- إصدار 'HTTP' المستخدم. مثال 'GET / HTTP/1.1'

'GET' هو أكثر 'HTTP' شيوعاً للحصول على المورد أو قراءته، و 'POST' هي طريقة طلب شائعة لإنشاء المورد.

### سطر الاستجابة الأولي (سطر الحالة)

يحتوي سطر الاستجابة الأولي، المسمى بسطر الحالة، على ثلاثة أجزاء أيضاً مفصولة بمسافات:

- إصدار 'HTTP'
- رمز حالة الاستجابة الذي ي给出 نتيجة الطلب، وسبب يصف رمز الحالة. أمثلة على أسطر الحالة:
  'HTTP/1.0 200 OK'
  أو
  'HTTP/1.0 404 Not Found'
  ملاحظات:

أكثر رموز الحالة شيوعاً هي:
'200 OK': نجح الطلب، ويتم إرجاع المورد الناتج (مثل ملف أو مخرجات نص برمجي) في جسم الرسالة.
'500 Server Error'
يمكن العثور على قائمة كاملة برموز حالة 'HTTP' من [هنا](https://httpstatuses.com/). يمكن العثور عليها أيضاً من [هنا](https://httpstatusdogs.com/).

### حول الرأس

كما رأيت في لقطة الشاشة أعلاه، توفر خطوط الرأس معلومات حول الطلب أو الاستجابة، أو حول الكائن المرسل في جسم الرسالة.

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

### جسم الرسالة

قد تحتوي رسالة 'HTTP' على جسم بيانات يُرسل بعد خطوط الرأس. في الاستجابة، هنا يتم إرجاع المورد المطلوب إلى العميل (الاستخدام الأكثر شيوعاً لجسم الرسالة)، أو ربما نص توضيحي في حالة وجود خطأ. في الطلب، هنا يتم إرسال بيانات المستخدم المدخلة أو الملفات المرفوعة إلى الخادم.

إذا كانت رسالة 'HTTP' تشمل جسداً، فعادةً ما تكون هناك خطوط الرأس في الرسالة التي تصف الجسم. وبشكل خاص:

/header 'Content-Type'': يعطي نوع البيانات في الجسم ('text/html'، 'application/json'، 'text/plain'، 'text/css'، 'image/gif').
/header 'Content-Length'': يعطي عدد البايتات في الجسم.

### طرق الطلب

'GET' و 'POST' و 'PUT' و 'DELETE' هي طرق طلب 'HTTP' التي سنقوم بتنفيذ 'API' أو تطبيق عملية 'CROOT' باستخدامها.

1. 'GET': تُستخدم طريقة 'GET' لاسترجاع والحصول على المعلومات من الخادم المحدد باستخدام 'URI' معين. الطلبات التي تستخدم 'GET' يجب فقط استرجاع البيانات ولا يجب أن يكون لها أي تأثير آخر على البيانات.

2. 'POST': يُستخدم طلب 'POST' لإنشاء البيانات وإرسالها إلى الخادم، على سبيل المثال، إنشاء منشور جديد، أو رفع ملف، إلخ. باستخدام نماذج 'HTML'.

3. 'PUT': يستبدل جميع التمثيلات الحالية للمورد المستهدف بالمحتوى المرفق، ونستخدمه لتعديل أو تحديث البيانات.

4. 'DELETE': يحذف البيانات

## 💻 التمارين: اليوم 28

1. اقرأ عن 'API' و 'HTTP'

🎉 تهانينا! 🎉

[<< اليوم 27](./27_python_with_mongodb.md) | [اليوم 29 >>](./29_building_API.md)
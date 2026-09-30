<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 23 - البيئة الافتراضية </h1>
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

[<< اليوم 22](./22_web_scraping.md) | [اليوم 24 >>](./24_statistics.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 23](#-اليوم-23)
  - [إعداد البيئات الافتراضية](#إعداد-البيئات-الافتراضية)
  - [💻 تمارين: اليوم 23](#-تمارين-اليوم-23)

# 📘 اليوم 23

## إعداد البيئات الافتراضية

للبدء في مشروع، من الأفضل أن يكون لديك بيئة افتراضية. البيئة الافتراضية يمكن أن تساعدنا في إنشاء بيئة معزولة أو منفصلة. سيساعدنا ذلك في تجنب التعارضات في التبعيات عبر المشاريع. إذا كتبت 'pip freeze' في 'terminal' الخاص بك، سترى جميع الحزم المثبتة على جهازك. إذا استخدمنا 'virtualenv'، سنصل فقط إلى الحزم الخاصة بذلك المشروع. افتح 'terminal' الخاص بك وقم بتثبيت 'virtualenv'

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

داخل مجلد 30DaysOfPython، أنشئ مجلدًا باسم flask_project.

بعد تثبيت حزمة 'virtualenv'، اذهب إلى مجلد مشروعك وأنشئ بيئة افتراضية عن طريق كتابة:

لـ Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

```

لـ Windows:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

أفضل تسمية المشروع الجديد بـ 'venv'، لكن لا تتردد في تسميته بشكل مختلف. دعنا نتحقق مما إذا تم إنشاء 'venv' باستخدام أمر 'ls' (أو 'dir' لسطر أوامر Windows).

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

لتنشيط البيئة الافتراضية عن طريق كتابة الأمر التالي في مجلد مشروعك.

لـ Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
تنشيط البيئة الافتراضية في Windows قد يختلف بين Windows Power shell و git bash.

لـ Windows Power Shell:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

لـ Windows Git bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

بعد كتابة أمر التنشيط، سيبدأ مجلد مشروعك بـ 'venv'. راقب المثال أدناه.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

الآن، دعنا نتحقق من الحزم المتاحة في هذا المشروع عن طريق كتابة 'pip freeze'. لن ترى أي حزم.

سنقوم بعمل مشروع flask صغير لذا دعنا نقوم بتثبيت حزمة 'flask' في هذا المشروع.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

الآن، دعنا نكتب 'pip freeze' لرؤية قائمة الحزم المثبتة في المشروع:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

عند الانتهاء يجب عليك إلغاء تنشيط المشروع النشط باستخدام 'deactivate'.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

الوحدات اللازمة للعمل مع 'flask' مثبتة. الآن، مجلد مشروعك جاهز لمشروع 'flask'. يجب عليك تضمين 'venv' في ملف '.gitignore' الخاص بك حتى لا تقوم بدفعه إلى 'github'.

## 💻 تمارين: اليوم 23

1. أنشئ مجلدًا للمشروع ببيئة افتراضية بناءً على المثال المقدم أعلاه.

🎉 مبروك! 🎉

[<< اليوم 22](./22_web_scraping.md) | [اليوم 24 >>](./24_statistics.md)

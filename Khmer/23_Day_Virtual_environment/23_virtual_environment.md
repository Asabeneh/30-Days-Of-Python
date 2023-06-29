<div align="center">
  <h1> 30 Days Of Python: Day 23 - Virtual Environment </h1>
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

[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 23](#-day-23)
  - [Setting up Virtual Environments](#setting-up-virtual-environments)

# 📘 Day 23

## Setting up Virtual Environments

ដើម្បីចាប់ផ្តើមជាមួយ project វាល្អប្រសិនបើអ្នកមាន Virtual environment ។ Virtual environment អាចជួយយើងបង្កើត environment ដែលនៅដាច់ដោយឡែក ឬបែកគ្នា ។
នេះនឹងជួយឱ្យយើងចៀសវាងជម្លោះនៅក្នុងការពឹងផ្អែក (dependencies) លើ project ។ ប្រសិនបើអ្នកសរសេរ pip freeze នៅលើ terminal របស់អ្នក អ្នកនឹងឃើញកម្មវិធីទាំងអស់ដែលបានដំឡើងនៅលើកុំព្យូទ័ររបស់អ្នក ។
ប្រសិនបើយើងប្រើ virtualnv យើងនឹងទទួលបានតែ packages ដែលជាក់លាក់សម្រាប់ project នោះ ។ បើក terminal របស់លោកអ្នកហើយដំឡើង virtualalenv

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

នៅក្នុង folder 30DaysOfPython បង្កើត folder flask_project ។

ក្រោយពីបានដំឡើងកម្មវិធី virtualenv សូមចូលទៅក្នុង folder របស់អ្នក ហើយបង្កើត virtualenv ដោយសរសេរថា

សម្រាប់ Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

```

សម្រាប់ Windows:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

ខ្ញុំចូលចិត្តហៅ project ថ្មីនេះថា venv, ប៉ុន្តែអ្នកអាចដាក់ឈ្មោះផ្សេងទៀត ។ សូមយើងពិនិត្យមើលថាតើ venv ត្រូវបានបង្កើតដោយប្រើ ls command (ឬ dir សម្រាប់ windows command prompt) ។

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

អនុញ្ញាតឱ្យយើងធ្វើសកម្ម virtual environment ដោយសរសេរបញ្ជាដូចខាងក្រោមនៅក្នុង folder project របស់យើង។

សម្រាប់ Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
ការបើក virtual environment ក្នុង Windows អាចនឹងខូចនៅលើ Windows Power shell និង git bash ។

សម្រាប់ Windows Power Shell:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

សម្រាប់ Windows Git bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

បន្ទាប់ពីអ្នកសរសេរបញ្ជា activation, project directory របស់អ្នកនឹងចាប់ផ្តើមជាមួយ venv ។ សូមមើលឧទាហរណ៍ខាងក្រោម។

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

ឥឡូវនេះ, សូមមើល package ដែលមាននៅក្នុង project នេះដោយសរសេរ pip freeze អ្នកនឹងមិនឃើញនូវកញ្ចប់ណាមួយទេ ។

យើងនឹងធ្វើ flask project ដូច្នេះយើងត្រូវដំឡើង flask package នេះទៅលើ project នេះ។

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

ឥឡូវនេះយើងសរសេរ pip freeze ដើម្បីមើលបញ្ជីនៃកម្មវិធីដែលបានដំឡើងនៅក្នុង project :

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

នៅពេលដែលអ្នកបានបញ្ចប់អ្នកគួរតែបិទសកម្ម project ដោយប្រើ _deactivate_ ។

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

ម៉ូឌុលដែលចាំបាច់ដើម្បីធ្វើការជាមួយ flask បានដំឡើង ។ ឥឡូវនេះ, project directory របស់អ្នក បានត្រៀមខ្លួនរួចរាល់សម្រាប់ flask project ។អ្នកគួរបញ្ចូល venv ទៅក្នុងឯកសារ.gitignore របស់អ្នក មិនត្រូវជំរុញវាទៅ Github ទេ ។

🎉 CONGRATULATIONS ! 🎉

[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)

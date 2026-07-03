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

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 23](#-day-23)
  - [가상 환경 설정하기](#가상-환경-설정하기)
  - [💻 연습문제: Day 23](#-연습문제-day-23)

# 📘 Day 23

## 가상 환경 설정하기

프로젝트를 시작할 때 가상 환경을 사용하는 것이 좋습니다. 가상 환경은 격리된 또는 별도의 환경을 만들 수 있도록 도와줍니다. 이를 통해 프로젝트 간의 종속성 충돌을 피할 수 있습니다. 터미널에서 pip freeze를 입력하면 컴퓨터에 설치된 모든 패키지를 볼 수 있습니다. virtualenv를 사용하면 해당 프로젝트에 특정한 패키지만 접근할 수 있습니다. 터미널을 열고 virtualenv를 설치하세요.

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

30DaysOfPython 폴더 안에 flask_project 폴더를 만드세요.

virtualenv 패키지를 설치한 후 프로젝트 폴더로 이동하여 다음과 같이 입력하여 가상 환경을 만드세요:

Mac/Linux의 경우:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

```

Windows의 경우:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

새 프로젝트를 venv라고 부르는 것을 선호하지만, 다른 이름을 자유롭게 지정해도 됩니다. ls(또는 Windows 명령 프롬프트의 경우 dir) 명령을 사용하여 venv가 생성되었는지 확인해 봅시다.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

프로젝트 폴더에서 다음 명령을 입력하여 가상 환경을 활성화해 봅시다.

Mac/Linux의 경우:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
Windows에서 가상 환경 활성화는 Windows Power Shell과 git bash에 따라 다를 수 있습니다.

Windows Power Shell의 경우:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

Windows Git bash의 경우:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

활성화 명령을 입력하면 프로젝트 디렉토리가 venv로 시작됩니다. 아래 예시를 확인하세요.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

이제 pip freeze를 입력하여 이 프로젝트에서 사용 가능한 패키지를 확인해 봅시다. 어떤 패키지도 보이지 않을 것입니다.

작은 flask 프로젝트를 만들 것이므로 이 프로젝트에 flask 패키지를 설치해 봅시다.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

이제 pip freeze를 입력하여 프로젝트에 설치된 패키지 목록을 확인해 봅시다:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

작업을 마치면 _deactivate_를 사용하여 활성 프로젝트를 비활성화해야 합니다.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

flask와 작업하는 데 필요한 모듈이 설치되었습니다. 이제 프로젝트 디렉토리가 flask 프로젝트를 위한 준비가 되었습니다. venv를 .gitignore 파일에 포함시켜 github에 푸시하지 않도록 해야 합니다.

## 💻 연습문제: Day 23

1. 위에 주어진 예시를 기반으로 가상 환경이 있는 프로젝트 디렉토리를 만드세요.

🎉 축하합니다! 🎉

[<< Day 22](../22_Day_Web_scraping/22_web_scraping.md) | [Day 24 >>](../24_Day_Statistics/24_statistics.md)

<div align="center">
  <h1> 30 дней Python: День 23 - Виртуальное окружение </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Автор:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Асабенех Йетаех</a><br>
<small>Второе издание: июль 2021</small>
</sub>
</div>

[<< День 22](../22_Day_Web_scraping/22_web_scraping.md) | [День 24 >>](../24_Day_Statistics/24_statistics.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 День 23](#-день-23)
  - [Настройка виртуальных окружений](#настройка-виртуальных-окружений)
  - [💻 Упражнения: День 23](#-упражнения-день-23)

# 📘 День 23

## Настройка виртуальных окружений

Чтобы начать работу над проектом, лучше иметь виртуальное окружение. Виртуальное окружение может помочь нам создать изолированную или отдельную среду. Это поможет нам избежать конфликтов в зависимостях между проектами. Если вы напишете pip freeze в терминале, вы увидите все пакеты, установленные на вашем компьютере. Если мы используем virtualenv, мы будем иметь доступ только к пакетам, которые специфичны для этого проекта. Откройте терминал и установите virtualenv

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

Внутри папки 30DaysOfPython создайте папку flask_project.

После установки пакета virtualenv перейдите в папку вашего проекта и создайте виртуальное окружение, написав:

Для Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

```

Для Windows:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

Я предпочитаю называть новый проект venv, но при желании вы можете назвать его по-другому. Давайте проверим, было ли создано venv, с помощью команды ls (или dir для командной строки Windows).

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

Давайте активируем виртуальное окружение, написав следующую команду в папке нашего проекта.

Для Mac/Linux:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
Активация виртуального окружения в Windows может различаться в Windows PowerShell и git bash.

Для Windows PowerShell:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

Для Windows Git bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

После того как вы напишете команду активации, ваш каталог проекта будет начинаться с venv. Смотрите пример ниже.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

Теперь давайте проверим доступные пакеты в этом проекте, написав pip freeze. Вы не увидите ни одного пакета.

Мы собираемся сделать небольшой проект на flask, поэтому давайте установим пакет flask в этот проект.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

Теперь давайте напишем pip freeze, чтобы увидеть список пакетов, установленных в проекте:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

Когда закончите, вы должны деактивировать активный проект с помощью _deactivate_.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

Необходимые модули для работы с flask установлены. Теперь ваш каталог проекта готов для проекта на flask. Вам следует добавить venv в ваш файл .gitignore, чтобы не отправлять его на github.

## 💻 Упражнения: День 23

1. Создайте каталог проекта с виртуальным окружением на основе примера, приведённого выше.

🎉 ПОЗДРАВЛЯЕМ! 🎉

[<< День 22](../22_Day_Web_scraping/22_web_scraping.md) | [День 24 >>](../24_Day_Statistics/24_statistics.md)

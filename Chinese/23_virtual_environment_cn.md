# 30天Python编程挑战：第23天 - 虚拟环境

- [第23天](#-第23天)
  - [设置虚拟环境](#设置虚拟环境)
  - [💻 练习：第23天](#-练习第23天)

# 📘 第23天

## 设置虚拟环境

开始项目时，最好有一个虚拟环境。虚拟环境可以帮助我们创建一个隔离或独立的环境。这将有助于避免不同项目之间的依赖冲突。如果你在终端上输入pip freeze，你将看到计算机上安装的所有包。如果我们使用virtualenv，我们将只能访问特定于该项目的包。打开你的终端并安装virtualenv：

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

在30DaysOfPython文件夹内创建一个flask_project文件夹。

安装virtualenv包后，进入项目文件夹并通过以下命令创建虚拟环境：

对于Mac/Linux：
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ virtualenv venv
```

对于Windows：
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

我喜欢将新项目称为venv，但你可以随意命名。让我们使用ls（或Windows命令提示符的dir）命令检查venv是否已创建。

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

让我们通过在项目文件夹中编写以下命令来激活虚拟环境。

对于Mac/Linux：
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```

Windows上虚拟环境的激活可能因Windows PowerShell和git bash而异。

对于Windows PowerShell：
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

对于Windows Git bash：
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

输入激活命令后，你的项目目录将以venv开头。请参见下面的示例。

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

现在，让我们通过输入pip freeze来检查这个项目中可用的包。你不会看到任何包。

我们将做一个小型flask项目，所以让我们为这个项目安装flask包。

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

现在，让我们输入pip freeze查看项目中已安装的包列表：

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

完成后，你应该使用_deactivate_来关闭活动项目。

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

使用flask所需的模块已经安装好了。现在，你的项目目录已经准备好用于flask项目。你应该将venv包含在.gitignore文件中，以避免将其推送到GitHub。

## 💻 练习：第23天

1. 根据上面给出的示例创建一个带有虚拟环境的项目目录。

🎉 恭喜！🎉

[<< 第 22 天](./22_web_scraping_cn.md) | [第 24 天 >>](./24_statistics_cn.md) 
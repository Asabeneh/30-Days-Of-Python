# 30天Python编程挑战：第20天 - PIP

- [第20天](#-第20天)
  - [Python PIP - Python包管理器](#python-pip---python包管理器)
    - [什么是PIP？](#什么是pip)
    - [安装PIP](#安装pip)
    - [使用pip安装包](#使用pip安装包)
    - [卸载包](#卸载包)
    - [包列表](#包列表)
    - [显示包信息](#显示包信息)
    - [PIP Freeze](#pip-freeze)
    - [从URL读取数据](#从url读取数据)
    - [创建包](#创建包)
    - [关于包的更多信息](#关于包的更多信息)
  - [练习：第20天](#练习第20天)

# 📘 第20天

## Python PIP - Python包管理器

### 什么是PIP？

PIP代表首选安装程序(Preferred installer program)。我们使用_pip_来安装不同的Python包。
包是一个Python模块，可以包含一个或多个模块或其他包。我们可以安装到应用程序中的模块或模块集合就是一个包。
在编程中，我们不必编写每个实用程序，而是安装包并将它们导入到我们的应用程序中。

### 安装PIP

如果你还没有安装pip，让我们现在安装它。转到你的终端或命令提示符，复制并粘贴：

```sh
asabeneh@Asabeneh:~$ pip install pip
```

通过以下命令检查pip是否已安装：

```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

如你所见，我正在使用pip 21.1.3版本，如果你看到的数字比这个稍低或稍高，说明你已经安装了pip。

让我们了解一下Python社区中用于不同目的的一些包。请注意，有很多可用于不同应用程序的包。

### 使用pip安装包

让我们尝试安装_numpy_，即数值Python。它是机器学习和数据科学社区中最流行的包之一。

- NumPy是Python科学计算的基础包。它包含以下内容：
  - 强大的N维数组对象
  - 复杂的（广播）函数
  - 用于集成C/C++和Fortran代码的工具
  - 有用的线性代数、傅里叶变换和随机数功能

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

让我们开始使用numpy。打开你的Python交互式shell，输入python，然后按如下方式导入numpy：

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst = [1, 2, 3,4, 5]
>>> np_arr = numpy.array(lst)
>>> np_arr
array([1, 2, 3, 4, 5])
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array([3, 4, 5, 6, 7])
>>>
```

Pandas是一个开源的、BSD许可的库，为Python编程语言提供高性能、易用的数据结构和数据分析工具。让我们安装numpy的"大兄弟"_pandas_：

```sh
asabeneh@Asabeneh:~$ pip install pandas
```

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

这一节不是关于numpy或pandas的，我们在这里尝试学习如何安装包以及如何导入它们。如果需要，我们将在其他章节讨论不同的包。

让我们导入一个Web浏览器模块，它可以帮助我们打开任何网站。我们不需要安装这个模块，它已经默认安装在Python 3中。例如，如果你想随时打开任意数量的网站，或者如果你想安排某些事情，可以使用这个_webbrowser_模块。

```py
import webbrowser # web浏览器模块用于打开网站

# 网址列表：Python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# 在不同的标签页中打开上面的网站列表
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### 卸载包

如果你不想保留已安装的包，可以使用以下命令删除它们。

```sh
pip uninstall packagename
```

### 包列表

要查看我们机器上已安装的包，我们可以使用pip后跟list。

```sh
pip list
```

### 显示包信息

要显示有关包的信息：

```sh
pip show packagename
```

```sh
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

如果我们想要更多的详细信息，只需添加--verbose

```sh
asabeneh@Asabeneh:~$ pip show --verbose pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

生成已安装的Python包及其版本，输出适合在requirements文件中使用。requirements.txt文件是一个包含Python项目中所有已安装的Python包的文件。

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

pip freeze给我们列出了使用的、已安装的包及其版本。我们将它与requirements.txt文件一起用于部署。

### 从URL读取数据

到目前为止，你已经熟悉了如何读取或写入位于本地机器上的文件。有时，我们想要使用url从网站或API读取数据。
API代表应用程序编程接口。它是一种在服务器之间交换结构化数据的方式，主要是json数据。要打开网络连接，我们需要一个名为_requests_的包——它允许打开网络连接并实现CRUD（创建、读取、更新和删除）操作。在本节中，我们将只涵盖CRUD的读取或获取部分。

让我们安装_requests_：

```py
asabeneh@Asabeneh:~$ pip install requests
```

我们将在_requests_模块中看到_get_、_status_code_、_headers_、_text_和_json_方法：
  - _get()_：打开网络并从url获取数据——它返回一个响应对象
  - _status_code_：在我们获取数据后，我们可以检查操作的状态（成功、错误等）
  - _headers_：检查头部类型
  - _text_：从获取的响应对象中提取文本
  - _json_：提取json数据
让我们从这个网站读取一个txt文件，https://www.w3.org/TR/PNG/iso_8859-1.txt。

```py
import requests # 导入请求模块

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # 来自网站的文本

response = requests.get(url) # 打开网络并获取数据
print(response)
print(response.status_code) # 状态码，成功时为200
print(response.headers)     # 获取响应的头部信息
print(response.text) # 获取文本数据
```

让我们读取一个API并得到一个json数据：

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # 包含关于250多个国家的信息的国家API
response = requests.get(url)  # 打开网络并获取数据
print(response) # 响应对象
print(response.status_code)  # 状态码，成功时为200
countries = response.json()
print(countries[:1])  # 我们只打印第一个国家信息，原始数据太大
```

我们用一个国家API示例获取了json数据。我们可以导入json模块，并使用json.loads(response.text)方法将文本转换为json格式。然而，我们也可以直接使用response.json()方法。

Let us see another example similar to the above but with a different API, world_bank_ethiopia data:
让我们看另一个类似于上面的例子，但使用不同的API，世界银行埃塞俄比亚数据：

```py
import requests
from pprint import pp # 导入pretty print，以美观地显示

url = 'http://api.worldbank.org/countries/et?format=json'  # 埃塞俄比亚经济数据API
response = requests.get(url)  # 打开网络并获取数据
print(response) # 响应对象
print(response.status_code)  # 状态码，成功时为200
# 让我们改变响应的JSON格式
ethiopia_data = response.json()
pp(ethiopia_data) # 用pretty print打印数据
```

### 创建包

我们可以创建自己的包，上传到Python包管理器仓库，并从那里下载它。让我们创建一个非常简单的包来演示。创建一个名为mypackage的目录，在该目录中创建一个名为__init__.py的空文件和以下文件：

```py
# mypackage/arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return (a - b)

def multiple(a, b):
    return a * b

def division(a, b):
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b
```

```py
# mypackage/greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```

__init__.py在python 3.3及更高版本中并非绝对必要，但对于兼容性，最好加上。

现在，让我们使用刚刚创建的包：

```py
from mypackage import arithmetics
print(arithmetics.add_numbers(1, 2, 3, 5))
print(arithmetics.subtract(5, 3))
print(arithmetics.multiple(5, 3))
print(arithmetics.division(5, 3))
print(arithmetics.remainder(5, 3))
print(arithmetics.power(5, 3))

from mypackage import greet
print(greet.greet_person('张', '三'))
```

### 关于包的更多信息

- Python有许多不同目的的内置包和模块，但有些不包含在内置包中，我们需要安装它们。
- 有多种方法可以安装包，但建议使用pip。
  - 使用 pip：pip是Python、PyPI和virtualenv推荐的安装和管理Python包的工具。
- 如何列出已安装的包：
  - pip list：列出机器中安装的所有包。
- 使用requirements.txt进行开发环境和生产环境：
  - 要生成已安装包的列表：pip freeze来本地生成已安装包的列表，以便用于开发环境和生产环境需求。
- 如何卸载包：
  - 要卸载，请使用pip：pip uninstall packagename。
  - 另一种方法：pip uninstall -r requirements.txt卸载在requirements.txt中列出的所有包。
- 使用virtualenv：
  - virtualenv是一个工具，用于创建隔离的Python环境。它创建一个在自己的目录树中包含所有必要的可执行文件，以使用指定版本的Python运行Python项目所需的包。
  - 原始的virtualenv工具可以通过
    - pip install virtualenv
    - 来安装。

## 练习：第20天

1. 阅读关于虚拟环境的更多信息，尝试创建虚拟环境并安装至少一个包

2. 使用一个国家API，获取所有国家信息，并找出前十个人口最多的国家

3. 从国家API数据中找出官方语言是英语(eng)的所有国家

4. 从国家API数据中获取数据，根据国家的面积找出前十个最大的国家

5. 从国家API数据中找出所有从新列出的国家，按他们的首都排序

🎉 恭喜！🎉

[<< 第 19 天](./19_file_handling_cn.md) | [第 21 天 >>](./21_classes_and_objects_cn.md) 
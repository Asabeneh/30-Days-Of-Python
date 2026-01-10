# 30天Python编程挑战：第22天 - 网页抓取

- [第22天](#-第22天)
  - [Python网页抓取](#python网页抓取)
    - [什么是网页抓取](#什么是网页抓取)
  - [💻 练习：第22天](#-练习第22天)

# 📘 第22天

## Python网页抓取

### 什么是网页抓取

互联网充满了大量的数据，这些数据可以用于不同的目的。要收集这些数据，我们需要知道如何从网站上抓取数据。

网页抓取是从网站提取和收集数据，并将其存储在本地机器或数据库中的过程。

在本节中，我们将使用beautifulsoup和requests包来抓取数据。我们使用的是beautifulsoup 4版本。

要开始抓取网站，你需要_requests_、_beautifoulSoup4_和一个_网站_。

```sh
pip install requests
pip install beautifulsoup4
```

要从网站抓取数据，需要基本了解HTML标签和CSS选择器。我们使用HTML标签、类或/和ID来定位网站上的内容。
让我们导入requests和BeautifulSoup模块：

```py
import requests
from bs4 import BeautifulSoup
```

让我们声明一个url变量，用于我们要抓取的网站。

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# 让我们使用requests的get方法从url获取数据
response = requests.get(url)
# 检查状态
status = response.status_code
print(status) # 200表示获取成功
```

```sh
200
```

使用beautifulSoup解析页面内容：

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # 我们从网站获取所有内容
soup = BeautifulSoup(content, 'html.parser') # beautiful soup将给我们一个解析的机会
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # 给出网站上的整个页面
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# 我们定位cellpadding属性值为3的表格
# 我们可以使用id、class或HTML标签进行选择，有关更多信息，请查看beautifulsoup文档
table = tables[0] # 结果是一个列表，我们从中提取数据
for td in table.find('tr').find_all('td'):
    print(td.text)
```

如果你运行这段代码，你会发现提取工作只完成了一半。你可以继续完成它，因为这是练习1的一部分。
参考[beautifulsoup文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)获取更多信息。

🌕 你非常特别，你每天都在进步。你只剩下八天就要达到伟大的境界了。现在做一些练习来锻炼你的大脑和肌肉。

## 💻 练习：第22天

1. 抓取以下网站并将数据存储为json文件（url = 'http://www.bu.edu/president/boston-university-facts-stats/'）。
2. 提取此url中的表格（https://archive.ics.uci.edu/ml/datasets.php）并将其更改为json文件。
3. 抓取总统表并将数据存储为json（https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States）。这个表格结构不是很规整，抓取可能需要很长时间。

🎉 恭喜！🎉

[<< 第 21 天](./21_classes_and_objects_cn.md) | [第 23 天 >>](./23_virtual_environment_cn.md) 
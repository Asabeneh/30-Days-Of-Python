# 30天Python编程挑战：第19天 - 文件处理

- [第19天](#-第19天)
  - [文件处理](#文件处理)
    - [打开文件进行读取](#打开文件进行读取)
    - [打开文件进行写入和更新](#打开文件进行写入和更新)
    - [删除文件](#删除文件)
  - [文件类型](#文件类型)
    - [带有txt扩展名的文件](#带有txt扩展名的文件)
    - [带有json扩展名的文件](#带有json扩展名的文件)
    - [将JSON转换为字典](#将json转换为字典)
    - [将字典转换为JSON](#将字典转换为json)
    - [保存为JSON文件](#保存为json文件)
    - [带有csv扩展名的文件](#带有csv扩展名的文件)
    - [带有xlsx扩展名的文件](#带有xlsx扩展名的文件)
    - [带有xml扩展名的文件](#带有xml扩展名的文件)
  - [💻 练习：第19天](#-练习第19天)
    - [练习：级别1](#练习级别1)
    - [练习：级别2](#练习级别2)
    - [练习：级别3](#练习级别3)

# 📘 第19天

## 文件处理

到目前为止，我们已经了解了不同的Python数据类型。我们通常在不同的文件格式中存储数据。除了处理文件外，在本节中我们还将看到不同的文件格式（.txt、.json、.xml、.csv、.tsv、.excel）。首先，让我们熟悉使用常见文件格式（.txt）处理文件。

文件处理是编程的重要部分，它允许我们创建、读取、更新和删除文件。在Python中，处理数据我们使用内置函数 _open()_。

```py
# 语法
open('filename', mode) # mode(r, a, w, x, t, b) 可以是读取、写入、更新
```

- "r" - 读取 - 默认值。打开文件进行读取，如果文件不存在则返回错误
- "a" - 追加 - 打开文件进行追加，如果文件不存在则创建文件
- "w" - 写入 - 打开文件进行写入，如果文件不存在则创建文件
- "x" - 创建 - 创建指定的文件，如果文件已存在则返回错误
- "t" - 文本 - 默认值。文本模式
- "b" - 二进制 - 二进制模式（例如图像）

### 打开文件进行读取

_open_ 的默认模式是读取，因此我们不必指定'r'或'rt'。我已经在files目录中创建并保存了一个名为reading_file_example.txt的文件。让我们看看它是如何完成的：

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

如上例所示，我打印了打开的文件，它提供了一些关于文件的信息。已打开的文件有不同的读取方法：_read()_、_readline_、_readlines_。打开的文件必须用 _close()_ 方法关闭。

- _read()_：将整个文本作为字符串读取。如果我们想限制想要读取的字符数，可以通过向 *read(number)* 方法传递int值来限制。

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# 输出
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

与其打印所有文本，不如打印文本文件的前10个字符。

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# 输出
<class 'str'>
This is an
```

- _readline()_：只读取第一行

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# 输出
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_：逐行读取所有文本，并返回一个行列表

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# 输出
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

获取所有行作为列表的另一种方法是使用 _splitlines()_：

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# 输出
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

在打开文件后，我们应该关闭它。我们很容易忘记关闭它们。有一种使用 _with_ 打开文件的新方法——它会自动关闭文件。让我们用 _with_ 方法重写前面的例子：

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# 输出
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### 打开文件进行写入和更新

要写入现有文件，我们必须向 _open()_ 函数添加模式作为参数：

- "a" - 追加 - 将在文件末尾追加，如果文件不存在则创建一个新文件。
- "w" - 写入 - 将覆盖任何现有内容，如果文件不存在则创建。

让我们在我们一直在读取的文件中追加一些文本：

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('此文本必须附加在末尾')
```

如果文件不存在，以下方法将创建一个新文件：

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('这段文本将被写入新创建的文件中')
```

### 删除文件

我们在前面的部分中已经看到，如何使用 _os_ 模块创建和删除目录。现在，如果我们想删除一个文件，我们也使用 _os_ 模块。

```py
import os
os.remove('./files/example.txt')

```

如果文件不存在，remove方法将引发错误，因此最好使用条件语句：

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('文件不存在')
```

## 文件类型

### 带有txt扩展名的文件

带有 _txt_ 扩展名的文件是一种非常常见的数据形式，我们已经在前面的部分中介绍了它。让我们转到JSON文件。

### 带有json扩展名的文件

JSON代表JavaScript对象表示法。实际上，它是一个字符串化的JavaScript对象或Python字典。

_示例:_

```py
# 字典
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}
# JSON: 字典的字符串形式
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# 我们使用三个引号并使其多行以使其更具可读性
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScript", "React","Python"]
}'''
```

### 将JSON转换为字典

要将JSON更改为字典，首先我们导入json模块，然后使用 _loads_ 方法。

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''
# 将JSON字符串更改为字典
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# 输出
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### 将字典转换为JSON

要将字典更改为JSON，我们使用 _dumps_ 方法。

```py
import json
# python字典
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
# 将字典转换为JSON字符串
person_json = json.dumps(person, indent=4) # indent可以是2, 4, 8. 它漂亮地打印了。
print(type(person_json))
print(person_json)
```

```sh
# 输出
<class 'str'>
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScript",
        "React",
        "Python"
    ]
}
```

### 保存为JSON文件

我们也可以将我们的数据保存为JSON文件。让我们使用前面的示例保存：

```py
import json
# python字典
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

在上面的代码中，我们使用了编码和确保_ascii参数。这些参数是为了保存非ASCII字符，如果我们想保存非英语字符。下面是一个包含非ASCII字符的示例：

```py
import json
# python字典
person = {
    "name": "张三",
    "country": "中国",
    "city": "北京",
    "skills": ["JavaScript", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

现在，让我们读取我们刚刚创建的json文件：

```py
import json
with open('./files/json_example.json', 'r', encoding='utf-8') as f:
    person = json.load(f)
    print(person)
```

```sh
# 输出
{'name': '张三', 'country': '中国', 'city': '北京', 'skills': ['JavaScript', 'React', 'Python']}
```

### 带有csv扩展名的文件

CSV代表逗号分隔值。CSV是一种简单的文件格式，用于存储表格数据，如电子表格或数据库。CSV是数据科学中非常常见的数据格式。

**示例：**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**示例：**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w+ 创建文件（如果不存在）
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'列名为: {", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]}来自{row[1]}的{row[2]}。 他了解{row[3]}')
            line_count += 1
    print(f'已处理{line_count}行。')
```

```sh
# 输出:
列名为: name, country, city, skills
Asabeneh来自Finland的Helsinki。 他了解JavaScript
已处理2行。
```

我们还可以使用相同的方法将数据写入csv文件

```py
import csv
with open('./files/csv_example.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # 写入列名
    writer.writerow(['name', 'country', 'city', 'skills'])
    # 写入数据
    writer.writerow(['Asabeneh', 'Finland', 'Helsinki', 'JavaScript'])
```

### 带有xlsx扩展名的文件

要读取Excel文件，我们需要安装xlrd包。我们将使用它来读取Excel文件。

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### 带有xml扩展名的文件

XML是一种元标记语言，非常类似于HTML。在XML中，我们可以使用自己的标签，从而使其更加灵活。我们使用XML主要是为了结构化数据。在Python中有少量的XML库。在本部分中，我们将使用xml.etree.ElementTree模块。

**示例：XML**

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScript</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

我们将使用xml.etree.ElementTree模块来解析XML文件。

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('字段: ', child.tag)
```

```sh
# 输出
Root tag: person
Attribute: {'gender': 'female'}
字段:  name
字段:  country
字段:  city
字段:  skills
```

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('字段: ', child.tag)
```

```sh
# 输出
Root tag: person
Attribute: {'gender': 'female'}
字段:  name
字段:  country
字段:  city
字段:  skills
```

让我们获取更多细节：

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
    if child.tag != 'skills':
        print(child.text)
    else:
        for skill in child:
            print(skill.text)
```

```sh
# 输出
Root tag: person
Attribute: {'gender': 'female'}
field:  name
Asabeneh
field:  country
Finland
field:  city
Helsinki
field:  skills
JavaScript
React
Python
```

## 💻 练习：第19天

### 练习：级别1

1. 编写一个函数，该函数需要一个参数（文件名）并统计文件中单词的数量
2. 阅读obama_speech.txt文件并计算单词数
3. 阅读michelle_obama_speech.txt文件并计算单词数
4. 阅读donald_speech.txt文件并计算单词数
5. 阅读melina_trump_speech.txt文件并计算单词数

### 练习：级别2

1. 从编程语言中提取所有Python目录文件：
   a) 处理30DaysOfPython文件夹，提取出所有python文件，并将它们的名称存储在files_list.txt文件中
   b) 创建一个名为find_python.py的脚本，可以通过命令行运行它
   c) 添加一个名为--version的标志来处理命令行参数

### 练习：级别3

1. 使用以下数据集创建一个JSON文件：
    ```py
    python_libraries = [
    {
        "库名称": "Django",
        "创建者": "Adrian Holovaty",
        "首次发布年份": 2005,
        "版本": "4.0.2",
        "用途": "Web开发",
        "描述": "Django让您可以快速构建更好的Web应用程序。"
    },
    {
        "库名称": "Flask",
        "创建者": "Armin Ronacher",
        "首次发布年份": 2010,
        "版本": "2.0.2",
        "用途": "Web开发",
        "描述": "Flask是一个轻量级的WSGI Web应用程序框架。"
    },
    {
        "库名称": "NumPy",
        "创建者": "Travis Oliphant",
        "首次发布年份": 2005,
        "版本": "1.22.0",
        "用途": "科学计算",
        "描述": "NumPy是Python中用于科学计算的基础包。"
    },
    {
        "库名称": "Pandas",
        "创建者": "Wes McKinney",
        "首次发布年份": 2008,
        "版本": "1.4.0",
        "用途": "数据分析",
        "描述": "pandas是一个用于数据分析和数据操作的开源库。"
    },
    {
        "库名称": "Matplotlib",
        "创建者": "John D. Hunter",
        "首次发布年份": 2003,
        "版本": "3.5.1",
        "用途": "数据可视化",
        "描述": "Matplotlib是一个用于在Python中创建静态、动画和交互式可视化的库。"
    }
    ]
    ```

🎉 恭喜！🎉

[<< 第 18 天](./18_regular_expressions_cn.md) | [第 20 天 >>](./20_python_package_manager_cn.md) 
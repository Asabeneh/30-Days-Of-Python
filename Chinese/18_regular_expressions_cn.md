# 30天Python编程挑战：第18天 - 正则表达式

- [第18天](#-第18天)
  - [正则表达式](#正则表达式)
    - [*re* 模块](#re-模块)
    - [*re* 模块中的方法](#re-模块中的方法)
      - [匹配](#匹配)
      - [搜索](#搜索)
      - [使用 *findall* 搜索所有匹配项](#使用-findall-搜索所有匹配项)
      - [替换子字符串](#替换子字符串)
  - [使用RegEx拆分文本](#使用regex拆分文本)
  - [编写RegEx模式](#编写regex模式)
    - [方括号](#方括号)
    - [RegEx中的转义字符(\\)](#regex中的转义字符)
    - [一次或多次(+)](#一次或多次)
    - [句点(.)](#句点)
    - [零次或多次(*)](#零次或多次)
    - [零次或一次(?)](#零次或一次)
    - [RegEx中的量词](#regex中的量词)
    - [脱字符(^)](#脱字符)
  - [💻 练习：第18天](#-练习第18天)
    - [练习：级别1](#练习级别1)
    - [练习：级别2](#练习级别2)
    - [练习：级别3](#练习级别3)

# 📘 第18天

## 正则表达式

正则表达式（RegEx）是一种特殊的文本字符串，有助于在数据中查找模式。RegEx可用于检查不同数据类型中是否存在某种模式。要在Python中使用RegEx，首先我们应该导入RegEx模块，该模块被称为*re*。

### *re* 模块

导入模块后，我们可以使用它来检测或查找模式。

```py
import re
```

### *re* 模块中的方法

要查找模式，我们使用不同的*re*字符集，这些字符集允许在字符串中搜索匹配项。

- *re.match()*：只在字符串的第一行开头搜索，如果找到则返回匹配的对象，否则返回None。
- *re.search*：如果字符串中的任何地方（包括多行字符串）有匹配项，则返回匹配对象。
- *re.findall*：返回包含所有匹配项的列表。
- *re.split*：接受一个字符串，在匹配点处分割，返回一个列表。
- *re.sub*：替换字符串中的一个或多个匹配项。

#### 匹配

```py
# 语法
re.search(substring, string, re.I)
# substring是一个字符串或模式，string是我们查找模式的文本，re.I是忽略大小写
```

```py
import re

txt = 'I love to teach python and javaScript'
# 它返回一个带有span和match的对象
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# 我们可以使用span获取匹配的起始和结束位置，作为元组
span = match.span()
print(span)     # (0, 15)
# 让我们从span中找到起始和结束位置
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```

从上面的例子可以看出，我们正在寻找的模式（或我们正在寻找的子字符串）是*I love to teach*。match函数**只有**在文本以该模式开头时才会返回一个对象。

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

该字符串不以*I like to teach*开头，因此没有匹配，match方法返回None。

#### 搜索

```py
# 语法
re.match(substring, string, re.I)
# substring是一个模式，string是我们查找模式的文本，re.I是忽略大小写标志
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# 它返回一个带有span和match的对象
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# 我们可以使用span获取匹配的起始和结束位置，作为元组
span = match.span()
print(span)     # (100, 105)
# 让我们从span中找到起始和结束位置
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

如你所见，search比match好得多，因为它可以在整个文本中查找模式。Search返回找到的第一个匹配项的匹配对象，否则返回*None*。更好的*re*函数是*findall*。此函数检查整个字符串中的模式，并将所有匹配项作为列表返回。

#### 使用 *findall* 搜索所有匹配项

*findall()* 将所有匹配项作为列表返回

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# 它返回一个列表
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

如你所见，单词*language*在字符串中被找到了两次。让我们再练习一些。
现在我们将在字符串中查找Python和python这两个单词：

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# 它返回一个列表
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

由于我们使用*re.I*，所以包含了大小写字母。如果我们没有re.I标志，那么我们将不得不以不同的方式编写我们的模式。让我们来看看：

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

#### 替换子字符串

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# 或者
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
```

让我们再添加一个例子。除非我们删除%符号，否则以下字符串真的很难阅读。用空字符串替换%将清理文本。

```py

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

```sh
I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people. 
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?
```

## 使用RegEx拆分文本

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # 使用\n分割 - 行尾符号
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## 编写RegEx模式

要声明字符串变量，我们使用单引号或双引号。要声明RegEx变量，使用*r''*。
以下模式仅识别小写的apple，要使其不区分大小写，我们应该重写模式或添加标志。

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# 要使其不区分大小写，添加标志'
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# 或者我们可以使用一组字符方法
regex_pattern = r'[Aa]pple'  # 这意味着第一个字母可以是Apple或apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```

* []:  一组字符
  - [a-c] 表示，a或b或c
  - [a-z] 表示，从a到z的任何字母
  - [A-Z] 表示，从A到Z的任何字符
  - [0-3] 表示，0或1或2或3
  - [0-9] 表示从0到9的任何数字
  - [A-Za-z0-9] 任何单个字符，即a到z，A到Z或0到9

### 方括号

让我们使用方括号练习更多的模式。记得，我们使用*re.I*作为标志，使搜索不区分大小写。

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # 这意味着Apple或apple或Banana或banana
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']

```

使用方括号和管道。
```py
regex_pattern = r'[a-zA-Z0-9]'  # 这个方括号表示 a 到 z, A 到 Z, 0 到 9
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['A', 'p', 'p', 'l', 'e', 'a', 'n', 'd', 'b', 'a', 'n', 'a', 'n', 'a', 'a', 'r', 'e',...]

regex_pattern = r'\d'  # d 是一个特殊字符，表示数字
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

regex_pattern = r'\d+'  # d 是一个特殊字符，表示数字，+ 表示一个或多个
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### RegEx中的转义字符(\\)

```py
regex_pattern = r'\d+'  # d 是一个特殊字符，表示数字，+ 表示一个或多个
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

要查找 \ 本身，我们应该使用双倍反斜杠：
```py
regex_pattern = r'\\d'  # 这意味着寻找 \d
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # []
```

当我们在字符串中没有任何与 \d 匹配的内容时，找不到任何匹配项。

### 一次或多次(+)

```py
regex_pattern = r'\d+'  # d 是一个特殊字符，表示数字，+ 表示一个或多个
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### 句点(.)

```py
regex_pattern = r'[a].'  # 这个方括号表示 a 和 . 表示任何字符，除了新行
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . 任何字符，+ 任何字符一次或多次
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### 零次或多次(*)

零次或多次。这个例子不太明显，所以请慢慢看。

```py
regex_pattern = r'[a].*'  # . 任何字符，* 任何字符零次或多次
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### 零次或一次(?)

零次或一次。它可以存在，也可以不存在。

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? 表示零次或一次
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### RegEx中的量词

使用大括号，我们可以指定模式的长度
```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # 正好有四位数的数字
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'   # 1到4位数的数字
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### 脱字符(^)

- 以什么开始

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ 表示以 This 开始
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

- 否定

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ 在方括号内表示否定，不是A-Z，不是a-z，不是空格
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8,', '2021']
```

## 💻 练习：第18天

### 练习：级别1

1. 什么是正则表达式？
2. 正则表达式的变量是什么？
3. 重新创建字符串模式，这些模式可以：
   a) 查找对带有*才能*的字符串的引用，在一本书中
   b) 找出日期格式为 _DD-MM-YYYY_，例如12-01-2021
   c) 找出文本中动词的时态为ing

### 练习：级别2

1. 编写一个模式，用于识别表示有效Python变量名的字符串
2. 从以下文本中清除HTML标签。
```python
text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''
```

### 练习：级别3

1. 清理以下文本。在清理过程后，计算最常见的三个单词是什么。

```python

    paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

```

2. 下面的文本包含了几个电子邮件地址。编写一个可以查找或提取电子邮件地址的模式。

```py
email_address = '''
asabeneh@gmail.com
alex@yahoo.com
kofi@yahoo.com
doe@arc.gov
asabeneh.com
asabeneh@gmail
alex@yahoo
'''
```

🎉 恭喜！🎉

[<< 第 17 天](./17_exception_handling_cn.md) | [第 19 天 >>](./19_file_handling_cn.md) 

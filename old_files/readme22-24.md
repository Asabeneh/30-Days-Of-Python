![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

🧳 [Part 1: Day 1 - 3](https://github.com/Asabeneh/30-Days-Of-Python)  
🧳 [Part 2: Day 4 - 6](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)  
🧳 [Part 3: Day 7 - 9](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)  
🧳 [Part 4: Day 10 - 12](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)  
🧳 [Part 5: Day 13 - 15](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)  
🧳 [Part 6: Day 16 - 18](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)  
🧳 [Part 7: Day 19 - 21](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)  
🧳 [Part 8: Day 22 - 24](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme22-24.md)  
🧳 [Part 9: Day 25 - 27](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme25-27.md)  
🧳 [Part 10: Day 28 - 30](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme28-30.md) 

---
- [📘 Day 22](#%f0%9f%93%98-day-22)
  - [Python Web Scraping](#python-web-scraping)
    - [What is web scrapping](#what-is-web-scrapping)
  - [💻 Exercises: Day 22](#%f0%9f%92%bb-exercises-day-22)
- [📘 Day 23](#%f0%9f%93%98-day-23)
  - [Setting up Virtual Environments](#setting-up-virtual-environments)
  - [💻 Exercises: Day 23](#%f0%9f%92%bb-exercises-day-23)
- [📘 Day 24](#%f0%9f%93%98-day-24)
  - [Python for Statistical Analysis](#python-for-statistical-analysis)
  - [Statistics](#statistics)
  - [Data](#data)
  - [Statistics Module](#statistics-module)
- [NumPy](#numpy)

GIVE FEEDBACK: http://thirtydayofpython-api.herokuapp.com/feedback
# 📘 Day 22

## Python Web Scraping

### What is web scrapping

The internet is full huge amount of data which can be used for different uses. To collect this data we need to know how scrape data on a website.

Web scraping is the process of extracting and collecting data from websites and storing the data into a local machine or into a database.

In this section, we will use beautifulsoup and requests package to scape data. The beautifulsoup package we are using beautifulsoup 4.

To start scraping a website you need _requests_, _beautifoulSoup4_ and _website_ to be scrapped.

```sh
pip install requests
pip installl install beautifulsoup4
```

To scrape a data on a website it needs basic understanding of HTML tags and css selectors. We target content from a website using HTML tag, class or an id.
Let's import the requests and BeautifulSoup module

```py
import requests
from bs4 import BeautifulSoup
```

Let's declare url variable for the website which we are going to scrape.

```py

import requests
from bs4 import BeautifulSoup
url = 'http://mlr.cs.umass.edu/ml/datasets.html'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
# lets check the status
status = response.status_code
print(status) # 200 means the fetching was successful
```

```sh
200
```

Using beautifulSoup to parse content from the page

```py
import requests
from bs4 import BeautifulSoup
url = 'http://mlr.cs.umass.edu/ml/datasets.html'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
# print(soup.body)
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# We are targeting the table with cellpadding attribute and the attribute value
# We can select using id, class or HTML tag , for more information check the beautifulsoup doc
table = tables[0] # the result is list, we are taking out from the list
for td in table.find('tr').find_all('td'):
    print(td.text)
```

If you run the above code, you can see that the extraction is half done. You can continue doing it because it is part of exercise 1.
For reference check the beautiful [soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start)

## 💻 Exercises: Day 22

1. Extract the table in this url (http://mlr.cs.umass.edu/ml/datasets.html) and change it to a json file
2. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States)

# 📘 Day 23

## Setting up Virtual Environments

To start with project, it would be better to have a virtual environment. Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. If you write pip freeze on your terminal you will see all the installed packages on your computer. If we use virtualenv, we will access only packages which are specific for that project. Open your terminal and install virtualenv

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install virtualenv
```

After installing the virtualenv package go to your project folder and create a virtual env by writing:
``sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv

````
The venv name could another name too but I prefer to call it venv. Let's check if the the venv is create by using ls command.
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
````

Let's activate the virtual environment by writing the following command at our project folder.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate

```

After you write the activation command, your project directory will start with venv. See the example below.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

Now, lets check the available package in this project by writing pip freeze. You will not see any package.

We are going to do a small flask project so let's install flask to this project.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

Now, let's write pip freeze to see the install packages in the project

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

When you finish you should dactivate active project using _deactivate_.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

The necessary modules to work on flask are installed. Now, you project directory is ready for flask project. You should include the venv to your .gitignore file not to push it to github.

## 💻 Exercises: Day 23
1. Create a project directory with a virtual environment based on the example give above.

# 📘 Day 24
## Python for Statistical Analysis
## Statistics

Statistics is the discipline that studies the _collection_, _organization_, _displaying_, _analysis_, _interpretation_ and _presentation_ of data.
Statistics is a branch of mathematics that is recommended to be a prerequisite for  data science and machine learning. Statistics is a very broad field but we will focus in this section only on the most relevant part.
After completing this challenge, you may go to web development, data analysis, machine learning and data science path. Whatever path you may follow, at some point in your career you will get data which you may work on. Having some statistical knowledge will help you to make decision based on data, *data tells as they say*.

## Data

What is data? Data is any set of characters that is gathered and translated for some purpose, usually analysis. It can be any character, including text and numbers, pictures, sound, or video. If data is not put into context, it doesn't give any sense to a human or computer. To make sense from data we need to work on the data using different tools.

The work flow of data analysis, data science or machine learning starts from data. Data can be provided from some data source or it can be created. There are structured and and unstructure data. 

Data can be found as small or big data format. Most of the data types we will get have been covered in the file handling section.

## Statistics Module

The python _statistics_ module provides functions for calculating mathematical statistics of numeric data. The module is not intended to be a competitor to third-party libraries such as NumPy, SciPy, or proprietary full-featured statistics packages aimed at professional statisticians such as Minitab, SAS and Matlab. It is aimed at the level of graphing and scientific calculators.

# NumPy

In the first section we defined python as a great general-purpose programming language on its own, but with the help of other popular libraries (numpy, scipy, matplotlib, pandas etc) it becomes a powerful environment for scientific computing.

Numpy is the core library for scientific computing in Python. It provides a high-performance multidimensional array object, and tools for working with arrays.

So far, we have been using vscode but from now on I would recommend using Jupyter Notebook. To access jupter notebook let's install [anaconda](https://www.anaconda.com/). If you are using anaconda most of the common packages are included and you don't have install packages if you installed anaconda.

[continue](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/numpy.md)


[<< Part 7 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md) | [Part 9 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme25-27.md)

---

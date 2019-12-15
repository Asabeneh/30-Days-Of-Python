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
🧳 [Part 10: Day 28 - 30](#) 🔒

- [📘 Day 25](#%f0%9f%93%98-day-25)
  - [Pandas](#pandas)
  - [Importing pandas](#importing-pandas)
    - [Creating Pandas Series with default index](#creating-pandas-series-with-default-index)
    - [Creating Pandas Series with custom index](#creating-pandas-series-with-custom-index)
    - [Creating Pandas Series from a dictionary](#creating-pandas-series-from-a-dictionary)
    - [Creating a constant pandas series](#creating-a-constant-pandas-series)
    - [Creating a pandas series using linspace](#creating-a-pandas-series-using-linspace)
  - [DataFrames](#dataframes)
    - [Creating DataFrames from list of lists](#creating-dataframes-from-list-of-lists)
    - [Creating DataFrame using Dictionary](#creating-dataframe-using-dictionary)
    - [Creating DataFrams from list of dictionaries](#creating-dataframs-from-list-of-dictionaries)
  - [Reading CSV File using pandas](#reading-csv-file-using-pandas)
    - [Data Exploration](#data-exploration)
  - [Exercises: Day 25](#exercises-day-25)
- [📘 Day 26](#%f0%9f%93%98-day-26)
  - [Python for Web](#python-for-web)
      - [Flask](#flask)
  - [Exercises: Day 26](#exercises-day-26)
# 📘 Day 25
## Pandas

Pandas is an open source,high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
Pandas adds data structures and tools designed to work with table-like data which is Series and Data Frames
Pandas provides tools for data manipulation: reshaping, merging, sorting, slicing, aggregation and imputation.
```py
pip install conda
conda install pandas
```
Pandas data structure is based on *Series* and *DataFrames*
A series is a column and a DataFrame is a multidimensional table made up of collection of series. In order to create a pandas series we should use numpy to create a one dimensional arrays.
An example of a series, names

![pandas series](images/pandas-series-1.png) 

Countries Series

![pandas series](images/pandas-series-2.png) 

Cities Series

![pandas series](images/pandas-series-3.png)

As you can see, pandas series is just one column data. If we want to have multiple columns we use data frames. The example below shows pandas DataFrames.

Let's see, an example of a pandas data frame:

![Pandas data frame](images/pandas-dataframe-1.png)

Data from is a collection of rows and columns. Look at the table below it has many columns than the above


![Pandas data frame](images/pandas-dataframe-2.png)

## Importing pandas


```python
import pandas as pd
import numpy  as np
```

### Creating Pandas Series with default index


```python
nums = [1, 2, 3,4,5]
s = pd.Series(nums)
```


```python
s
```




    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64



### Creating  Pandas Series with custom index


```python
fruits = ['Orange','Banana','Mangao']
fruits = pd.Series(fruits, index=[1, 2,3])
```


```python
fruits
```




    1    Orange
    2    Banana
    3    Mangao
    dtype: object



### Creating Pandas Series from a dictionary


```python
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
```


```python
s = pd.Series(dct)
```


```python
s
```




    name       Asabeneh
    country     Finland
    city       Helsinki
    dtype: object



### Creating a constant pandas series


```python
s = pd.Series(10, index = [1, 2,3])
```


```python
s
```




    1    10
    2    10
    3    10
    dtype: int64



### Creating a  pandas series using linspace


```python
s = pd.Series(np.linspace(5, 20, 10))
```


```python
s
```




    0     5.000000
    1     6.666667
    2     8.333333
    3    10.000000
    4    11.666667
    5    13.333333
    6    15.000000
    7    16.666667
    8    18.333333
    9    20.000000
    dtype: float64



## DataFrames

Pandas data frames can be created in different ways.

### Creating DataFrames from list of lists


```python
data = [["Asabeneh", "Finland", "Helsink"], [
    "David", "UK", "London"], ["John", "Sweden", "Stockholm"]]
df = pd.DataFrame(data, columns=['Names','Country','City'])

```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsink</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>
</div>



### Creating DataFrame using Dictionary


```python
data = {"Name": ["Asabeneh", "David", "John"], "Country":[
    "Finland", "UK", "Sweden"], "City": ["Helsiki", "London", "Stockholm"]}
df = pd.DataFrame(data)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsiki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>
</div>



### Creating DataFrams from list of dictionaries


```python
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>
</div>



## Reading CSV File using pandas


```python
import pandas as pd

df = pd.read_csv('./data/weight-height.csv')
```

### Data Exploration
Let's read only the first 5 rows using head()


```python
df.head() # give five rows we can increase the number of rows by passing argument to the head() method
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Male</td>
      <td>73.847017</td>
      <td>241.893563</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Male</td>
      <td>68.781904</td>
      <td>162.310473</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Male</td>
      <td>74.110105</td>
      <td>212.740856</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Male</td>
      <td>71.730978</td>
      <td>220.042470</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Male</td>
      <td>69.881796</td>
      <td>206.349801</td>
    </tr>
  </tbody>
</table>
</div>



As you can see the csv file has three rows:Gender, Height and Weight. But we don't know the number of rows. Let's use shape meathod.


```python
df.shape # as you can see 10000 rows and three columns
```




    (10000, 3)



Let's get all the columns using columns.



```python
df.columns
```




    Index(['Gender', 'Height', 'Weight'], dtype='object')



Let's read only the last 5 rows using tail()


```python
df.tail() # tails give the last five rows, we can increase the rows by passing argument to tail method
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>9995</td>
      <td>Female</td>
      <td>66.172652</td>
      <td>136.777454</td>
    </tr>
    <tr>
      <td>9996</td>
      <td>Female</td>
      <td>67.067155</td>
      <td>170.867906</td>
    </tr>
    <tr>
      <td>9997</td>
      <td>Female</td>
      <td>63.867992</td>
      <td>128.475319</td>
    </tr>
    <tr>
      <td>9998</td>
      <td>Female</td>
      <td>69.034243</td>
      <td>163.852461</td>
    </tr>
    <tr>
      <td>9999</td>
      <td>Female</td>
      <td>61.944246</td>
      <td>113.649103</td>
    </tr>
  </tbody>
</table>
</div>



Now, lets get specif colums using the column key



```python
heights = df['Height'] # this is now a a series
```


```python
heights
```




    0       73.847017
    1       68.781904
    2       74.110105
    3       71.730978
    4       69.881796
              ...    
    9995    66.172652
    9996    67.067155
    9997    63.867992
    9998    69.034243
    9999    61.944246
    Name: Height, Length: 10000, dtype: float64




```python
weights = df['Weight'] # this is now a series
```


```python
weights
```




    0       241.893563
    1       162.310473
    2       212.740856
    3       220.042470
    4       206.349801
               ...    
    9995    136.777454
    9996    170.867906
    9997    128.475319
    9998    163.852461
    9999    113.649103
    Name: Weight, Length: 10000, dtype: float64




```python
len(heights) == len(weights)
```




    True




```python
heights.describe() # give statisical information about height data
```




    count    10000.000000
    mean        66.367560
    std          3.847528
    min         54.263133
    25%         63.505620
    50%         66.318070
    75%         69.174262
    max         78.998742
    Name: Height, dtype: float64




```python
weights.describe()
```




    count    10000.000000
    mean       161.440357
    std         32.108439
    min         64.700127
    25%        135.818051
    50%        161.212928
    75%        187.169525
    max        269.989699
    Name: Weight, dtype: float64




```python
df.describe()  # describe can also give statistical information from a datafrom
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>66.367560</td>
      <td>161.440357</td>
    </tr>
    <tr>
      <td>std</td>
      <td>3.847528</td>
      <td>32.108439</td>
    </tr>
    <tr>
      <td>min</td>
      <td>54.263133</td>
      <td>64.700127</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>63.505620</td>
      <td>135.818051</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>66.318070</td>
      <td>161.212928</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>69.174262</td>
      <td>187.169525</td>
    </tr>
    <tr>
      <td>max</td>
      <td>78.998742</td>
      <td>269.989699</td>
    </tr>
  </tbody>
</table>
</div>



## Exercises: Day 25
1. Read the hacker_ness.csv file from data directory 
1. Get the first five rows
1. Get the last five rows
1. Get the title column as pandas series
1. Count the number of rows and columns
    * Filter the titles which contain python
    * Filter the titles which contain JavaScript
    * Explore the data and make sense of the data


# 📘 Day 26

## Python for Web

Python is a general purpose programming language and it can be used for many places. In this section, we will see how we use python for the web. There are many python web frame works. Django and Flask are the most popular ones. Today, we will see how to use Flask for web development.

#### Flask

Flask is a web development framework written in python. Flask uses Jinja2 template engine. Flask can be also used with other modern frond libraries such as react.
If you did not install the virtualenv package ye install it first. Virtual environment will allows to isolate project dependencies.

Follow, the following steps to get started with Flask

```sh
pip install virtualenv
```

```sh
asabeneh@Asabeneh:~/Desktop$ mkdir python_for_web
asabeneh@Asabeneh:~/Desktop$ cd python_for_web/
asabeneh@Asabeneh:~/Desktop/python_for_web$ virtualenv env
asabeneh@Asabeneh:~/Desktop/python_for_web$ source env/bin/activate
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip install Flask
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$
```

Now, let's create app.py file in the project directory and write the following code. The following code has flask module, os module.

The home route.

```py
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) # for deployment
    # to make it work for both production and development
    if port == 5000:
        app.run(debug=True)
    else:
        app.run(port = port) # to listen to the port
```

After you run _python app.py_ check local host 5000.

Let's add additional route.
Creating about route

```py
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) # for deployment
    # to make it work for both production and development
    if port == 5000:
        app.run(debug=True)
    else:
        app.run(port = port) # to listen to the port
```

Now, we added the about route in the above code. How about if we want to render an HTML file instead of string? It is possible to render HTML file using the function _render_templae_. Let's create a folder called templates and create home.html and about.html in the project directory. Let's also import the _render_template_ function from flask.

Create the HTML files inside templates folder.

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
  </head>

  <body>
    <h1>Welcome Home</h1>
  </body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About</title>
  </head>

  <body>
    <h1>About Us</h1>
  </body>
</html>
```

app.py

```py
# let's import the flask
from flask import Flask, render_template
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) # for deployment
    # to make it work for both production and development
    if port == 5000:
        app.run(debug=True)
    else:
        app.run(port = port) # to listen to the port
```

As you can see to go to different pages or to navigate we need a navigation. Let's add a link to each page or let's create a layout which we use to every page.

```html
<ul>
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
</ul>
```

Now, we can navigate between the pages using the above link. Let's create additional page which handle form data. You can call it any name, I like to call it post.html.

We can inject data to the HTML files using Jinja2 template engine.

```py
# let's import the flask
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    return render_template('post.html', name = name, title = name)


if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Let's see the templates too:

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Home</title>
  </head>

  <body>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
    <h1>Welcome to {{name}}</h1>
    {% for tech in techs %}
    <ul>
      <li>{{tech}}</li>
    </ul>
    {% endfor %}
  </body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>About Us</title>
  </head>

  <body>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
    <h1>About Us</h1>
    <h2>{{name}}</h2>
  </body>
</html>
```

In the template files, there are lots of repeated codes, we can write a layout and we can remove the repetition. Let's create layout.html inside the templates folder.
After we create the layout we will import to every file.

layout.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% if title %}
    <title>30 Days of Python - {{ title}}</title>
    {% else %}
    <title>30 Days of Python</title>
    {% endif %}
  </head>

  <body>
    <header>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/post">Text Analyzer</a></li>
      </ul>
    </header>
    <main>
      {% block content %} {% endblock %}
    </main>
  </body>
</html>
```

Now, lets remove all the repeated code in the other template files and import the layout.html

home.html

```html
{% extends 'layout.html' %} {% block content %}
<h1>Welcome to {{name}}</h1>
<p>You need the following technologies to build this web application:</p>
{% for tech in techs %}
<ul>
  <li>{{tech}}</li>
</ul>
{% endfor %} {% endblock %}
```

about.html

```html
{% extends 'layout.html' %} {% block content %}
<h1>About Us</h1>
<h2>{{name}}</h2>
{% endblock %}
```

post.html

```html
{% extends 'layout.html' %} {% block content %}
<h1>Text Analyzer</h1>
<textarea cols="50" rows="10"></textarea>
<br />
<button>Process Text</button>
{% endblock %}
```

So far, we have seen how to use template and how to inject data to template, how to a common layout.
Now, lets handle static file. Create a folder called static in the project director and create a folder called css. Inside css folder create main.css. Your main. css file will be linked to the layout.html.

You don't have to write the css file, copy and use it. Let's move on to deployment. Heroku provides a free deployment service for both front end and fullstack applications. Create an account on [heroku](https://www.heroku.com/) and install the heroku [CLI](https://devcenter.heroku.com/articles/heroku-cli) for you machine.
After installing heroku write the following command

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

Let's see the result by clicking any key from the keyboard. When you press any key from you keyboard it will open the heroku login page and click the login page. Then you will local machine will be connected to the remote heroku server. If you are connected to remote server, you will see this.

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

Before we push our code to remote server, we need requirements
* requirements.txt
* Procfile
  
```sh
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch requirements.txt
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze > requirements.txt 
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ cat requirements.txt 
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch Procfile
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ ls
Procfile          env/              static/
app.py            requirements.txt  templates/
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ 
```
The Procfile will have the command which run the application.
```sh
web: python app.py
```
Now, it is ready to be deployed. Steps to deploy the application on heroku
1. git init 
2. git add . 
3. git commit -m "commit message"
4. heroku create 'name of the app as one word'
5. git push heroku master
6. heroku open(to launch the deployed application)

After this  step you will get an application like [this](https://thirtydaysofpython-v1.herokuapp.com/post)
## Exercises: Day 26



[<< Part 8 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme22-24.md) | [Part 10 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme28-30.md)

---



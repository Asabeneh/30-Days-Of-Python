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

- [📘 Day 19](#%f0%9f%93%98-day-19)
  - [File handling](#file-handling)
    - [Opening File for reading](#opening-file-for-reading)
    - [Opening file for writing or updating](#opening-file-for-writing-or-updating)
    - [Deleting file](#deleting-file)
  - [File Types](#file-types)
    - [File with txt Extension](#file-with-txt-extension)
    - [File with json Extension](#file-with-json-extension)
    - [Changing JSON to dictionary](#changing-json-to-dictionary)
    - [Changing dictionary to JSON](#changing-dictionary-to-json)
    - [Saving as JSON file](#saving-as-json-file)
    - [File with csv Extension](#file-with-csv-extension)
    - [File with xlsx Extension](#file-with-xlsx-extension)
    - [File with xml Extension](#file-with-xml-extension)
  - [💻 Exercises: Day 19](#%f0%9f%92%bb-exercises-day-19)
- [📘 Day 20](#%f0%9f%93%98-day-20)
  - [Python PIP - Python Package Manager](#python-pip---python-package-manager)
    - [What is PIP ?](#what-is-pip)
    - [Installing pip](#installing-pip)
    - [Installing packages using pip](#installing-packages-using-pip)
    - [Uninstall packages](#uninstall-packages)
    - [List of packages](#list-of-packages)
    - [Show package](#show-package)
    - [PIP freeze](#pip-freeze)
    - [Reading from URL](#reading-from-url)
    - [Creating a package](#creating-a-package)
    - [Further information about packages](#further-information-about-packages)
  - [Exercises: Day 20](#exercises-day-20)
- [📘 Day 21](#%f0%9f%93%98-day-21)
  - [Classes and Objects](#classes-and-objects)
    - [Creating a Class](#creating-a-class)
    - [Creating an Object](#creating-an-object)
    - [Class Constructor](#class-constructor)
    - [Object Methods](#object-methods)
    - [Object default methods](#object-default-methods)
    - [Method to modify class default values](#method-to-modify-class-default-values)
    - [Inheritance](#inheritance)
    - [Overriding parent method](#overriding-parent-method)
  - [💻 Exercises: Day 21](#%f0%9f%92%bb-exercises-day-21)
GIVE FEEDBACK: http://thirtydayofpython-api.herokuapp.com/feedback
# 📘 Day 19

## File handling

So far we have seen different python data types. We usually store our data in a different file format. In addition to handling file, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) file formats in this section. First, let's get familiar with handling file with common file format(.txt).

File handling is an import part of programming which allows us to create, read, update and delete files. In python to handle data we use _open()_ builtin function.

```py
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b,  could be to read, write, update
```

- "r" - Read - Default value. Opens a file for reading, error if the file does not exist
- "a" - Append - Opens a file for appending, creates the file if it does not exist
- "w" - Write - Opens a file for writing, creates the file if it does not exist
- "x" - Create - Creates the specified file, returns an error if the file exists
- "t" - Text - Default value. Text mode
- "b" - Binary - Binary mode (e.g. images)

### Opening File for reading

The default mode of _open_ is reading, so we do not have to specify 'r' or 'rt'. I have created and saved a file named reading_file_example.txt in the files directory. Let see read this file.

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

As you can see in the above example, I printed the opened file and it gave me some information about the opened file. Opened file has different reading methods: _read()_, _readline_, _readlines_. An opened file has to be closed with _close()_ method.

- _read()_: read the whole text as string. If we want to limit the number of characters we read, we can limit it by passing int value to the methods.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

Instead of printing all the text, let see by printing the first 10 characters of the text in the file.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# output
<class 'str'>
This is an
```

- _readline()_: read only the first line

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# output
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: read all the text line by line and returns a list of lines

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Another way to get all the lines a list is using _splitlines()_:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

After we open a file, we should close the file but there is a high tendency to forget to close. There is a new way of opening method, _with_ which closes by itself. Let's write the above code with _with_.

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# output
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Opening file for writing or updating

To write to an existing file, we must add a mode as parameter to the _open()_ function:

- "a" - append - will append to the end of the file if the file does not exist it raise FileNotFoundError.
- "w" - write - will overwrite any existing content if the file does not exist it creates.

Let's append some text to the file, we have been reading

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

This method below, create a new file if the file does not exist.

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### Deleting file

We have seen in previous section, how to make and remove a directory using _os_ module. Again now, if we want to remove a file we use _os_ module.

```py
import os
os.remove('./files/example.txt')

```

If the file does not exist, the remove method will raise an error it is good to use condition.

```py
import os
if os.path.exist('./files/example.txt):
    os.remove('./files/example.txt')
else:
    os.remove('The file does not exist')
```

## File Types

### File with txt Extension

File with _txt_ extension is a very common form data and we have covered it in the previous section. Let's move to the JSON file

### File with json Extension

JSON stands for JavaScript Object Notation. Actually, it a stringified JavaScript object.
_Example:_

```py
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### Changing JSON to dictionary

To change a JSON to a dictionary we use _loads_ method.

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(person_dct)
print(person_dct['name'])
```

```sh
# output
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### Changing dictionary to JSON

To change a dictionary to a JSON we use _dumps_ method.

```py
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautify the json
print(type(person_json))
print(person_json)
```

```sh
# output
# when you it is printed it does not have the quote but actually it is a string
# JSON does not have type, it is a string type.
<class 'str'>
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
```

### Saving as JSON file

We can also save our data as a json file. Let's save it as a json file using the following steps.

```py
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

In the above code, we use encoding and indentation. Indentation makes the json file easy to read.

### File with csv Extension

CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.

**Example:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScrip"
```

**Example:**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

```sh
# output:
Column names are :name, country, city, skills
        Asabeneh is a teachers. He lives in Finland, Helsinki.
Number of lines:  2
```

### File with xlsx Extension

To read excel we need to install _xlrd_ package. We will cover this after we cover package installing using pip.

### File with xml Extension

XML is another structured data format which looks like HTML. In XML the tags are not predefined. The first line is an XML declaration. The person tag is the root of the XML. The person has a gender attribute.
**Example:XML**

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

How to read an XML file, for more information check the [documentation](https://docs.python.org/2/library/xml.etree.elementtree.html)

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```

```sh
# output
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

## 💻 Exercises: Day 19

1. Writ a function which count number of lines and number of words from a text. All the files are in data the folder:
   1. Read obama_speech.txt file and count number of lines and now of words
   2. Read michelle_obama_speech.txt file and count number of lines and now of words
   3. Read donald_speech.txt file and count number of lines and now of words
   4. Read melina_trump_speech.txt file and count number of lines and now of words
2. Read the countries_data.json data file in data directory, create a function which find the ten most spoken languages

   ```py
   # Your output should look like this
   print(most_spoken_languages(filename='./data/countries_data.json', 10))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic'),
   (24, 'Spanish'),
   (9, 'Russian'),
   (9, 'Portuguese'),
   (8, 'Dutch'),
   (7, 'German'),
   (5, 'Chinese'),
   (4, 'Swahili'),
   (4, 'Serbian')]

   # Your output should look like this
   print(most_spoken_languages(filename='./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. Read the countries_data.json data file in data directory,create a function which create the ten most populated countries

   ```py
   # Your output should look like this
   print(most_populated_countries(filename='./data/countries_data.json', 10))

   [{'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000},
   {'country': 'Indonesia', 'population': 258705000},
   {'country': 'Brazil', 'population': 206135893},
   {'country': 'Pakistan', 'population': 194125062},
   {'country': 'Nigeria', 'population': 186988000},
   {'country': 'Bangladesh', 'population': 161006790},
   {'country': 'Russian Federation', 'population': 146599183},
   {'country': 'Japan', 'population': 126960000}]

   # Your output should look like this

   print(most_populated_countries(filename='./data/countries_data.json', 3))
   [{'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}]
   ```

4. Extract all incoming emails from the email_exchange_big.txt file.
5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters which are a string or a file and a positive integer. Your function will return an array of tuples in descending order. Check the output

```py
    # Your output should look like this

    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

6. Use the function, find_most_frequent_words to find out:
   1. The ten most frequent words used in [Obama's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   2. The ten most frequent words used in [Michelle's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   3. The ten most frequent words used in [Trump's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   4. The ten most frequent words used in [Melina's speech](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
7. Write a python application which checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of [Michelle's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) and [Melina's](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) are in the data directory
8. Find the 10 most repeated words in the romeo_and_juliet.txt
9. Read the [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) file and find out:
   1. Count the number of lines containing python or Python
   2. Count the number lines containing JavaScript, javascript or Javascript
   3. Count the number lines containing Java not JavaScript

# 📘 Day 20

## Python PIP - Python Package Manager

### What is PIP ?

PIP stands for Preferred installer program. We use _pip_ to install different python packages.
Package is a python module which can contain one or more modules or other packages. A module or modules which we can install to our application is a package.
In programming, we do not have to write every utility programs instead we install packages and import the package to our applications.

### Installing pip

If you did not install pip, lets install pip. Go to your terminal or command prompt and copy and past this:

```sh
asabeneh@Asabeneh:~$ pip install pip
```

Check if it is installed by writing

```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 19.3.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```

As you can see, I am using pip version 19.3.1, if you see some number a bit below or above that mean you have pip installed.

Let's some of the package used in the python community for different purposes. Just to let you know that there are lots of package which are available for use with different applications.

### Installing packages using pip



Let's try to install _numpy_, which is called a numeric python. It is one of the most popular package in machine learning and data science community.

- NumPy is the fundamental package for scientific computing with Python. It contains among other things:
  - a powerful N-dimensional array object
  - sophisticated (broadcasting) functions
  - tools for integrating C/C++ and Fortran code
  - useful linear algebra, Fourier transform, and random number capabilities

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

Lets start using numpy. Open your python interactive shell, write python and then import numpy as follows:

```py
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.17.3'
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

Pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Lets install big brother of numpy _pandas_ as we did for _numpy_.

```sh
asabeneh@Asabeneh:~$ pip install pandas
```

```py
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

This section is not about numpy nor pandas, here we are trying to learn how to install packages and how to import them. If it is needed we will talk about different packages in other sections.

Let's import a web browser module, which can help us to open any website.You do not install this module, it is installed by default with python 3.  For instance if you like to open any number of website at any time or if you like to schedule something this *webbrowser* module can be use.
```py
import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://twitter.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### Uninstall packages

If you do not like to keep the installed packages, you can remove them.

```sh
pip uninstall packagename
```

### List of packages

To see the installed packages on our machine. We can use pip followed by lis.

```sh
pip list
```

### Show package

To show information about a package

```sh
pip show packagename
```

```sh
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 0.25.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

If we want even more detail than the above, just add --verbose

```sh
asabeneh@Asabeneh:~$ pip show --verbose pandas
Name: pandas
Version: 0.25.3
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

### PIP freeze

Generate output suitable for a requirements file.

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

The pip freeze gave us the packages use installed and their version. We use with requirements.txt file for deployment.

### Reading from URL

By now you are familiar with how to read or write on a file which is located in you local machine. Sometimes, we may like to read from a website using url or from an API.
API stands for Application Program Interface. It is a means to exchange structure data between servers primarily a json data. To open network, we need a package called _requests_ which allows to open network and to implement CRUD(create, read, update and delete) operation. In this section, we will cover only reading part of a CRUD.

Let's install _requests_

```py
asabeneh@Asabeneh:~$ pip install requests
```

We will see _get_, _status_code_, _headers_, _text_ and _json_ methods from _requests_ module
_ get(): to open a network and fetch data from url and it returns a response object
_ status_code: After we fetched, we check the status(succes, error, etc)
_ headers: To check the header types
_ text: to extract the text from the fetched response object \* json: to extract json data
Let's read a txt file form this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page
```

```sh
<Response [200]>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

- Lets read from an api. API stands for Application Program Interface. It is a means to exchange structure data between servers primarily a json data. An example of api:https://restcountries.eu/rest/v2/all. Let's read this API using _requests_ module.

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries
```

```sh
<Response [200]>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
```

We use _json()_ method from response object, if the we are fetching JSON data. For txt, html, xml and other file formats we can use _text_.

### Creating a package

We organize a large number of files in different folders and subfolders based on some criteria, so that we can find and manage them easily. As you know, a module can contain multiple objects, such as classes, functions, etc. A package can contain one or more relevant modules.A package is actually a folder containing one or more module files. Let's create a package named mypackage, using the following steps:

Create a new folder named mypacakge inside 30DaysOfPython folder
Create an empty **init**.py file in the mypackage folder.
Create modules arithmetic.py and greet.py with following code:

```py
# mypackage/arithmetics.py
# arithmetics.py
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
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```
The folder structure of your package should look like this:
```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```
Now let's open the python interactive shell and try the package we have created:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32) 
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1,2,3,5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Asabeneh', 'Yetayeh')
'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'
>>> 
```
As you can see our package works perfect. The package folder contains a special file called __init__.py which stores the package's content. If we put  __init__.py in the package folder, python start recognizes it as a package.
The __init__.py exposes specified resources from its modules to be imported to other python files. An empty __init__.py file makes all functions available when a package is imported. The __init__.py is essential for the folder to be recognized by Python as a package. 

### Further information about packages

- Database
  - SQLAlchemy or SQLObject - Object oriented access to several different database systems
    - _pip install SQLAlchemy_
- Web Development
  - Django - High-level web framework.
    - _pip install django_
  - Flask - microframework for Python based on Werkzeug, Jinja 2. (It's BSD licensed)
    - _pip install flask_
- HTML Parser

  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - HTML/XML parser designed for quick turnaround projects like screen-scraping, will accept bad markup.
    - _pip install beautifulsoup4_
  - PyQuery - implements jQuery in Python; faster than BeautifulSoup, apparently.

- XML Processing
  - ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. --Note: Python 2.5 and up has ElementTree in the Standard Library
- GUI
  - PyQt - Bindings for the cross-platform Qt framework.
  - TkInter - The traditional Python user interface toolkit.
- Data Analysis, Data Science and Machine learning
  - Numpy: Numpy(numeric python) is known as one of the most popular machine learning library in Python.
  - Pandas: is a machine learning library in Python that provides data structures of high-level and a wide variety of tools for analysis.
  - SciPy: SciPy is a machine learning library for application developers and engineers. SciPy library contains modules for optimization, linear algebra, integration, image processing, and statistics.
  - Scikit-Learn: It is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
  - TensorFlow: is a machine learning library built by Google.
  - Keras: is considered as one of the coolest machine learning libraries in Python. It provides an easier mechanism to express neural networks. Keras also provides some of the best utilities for compiling models, processing data-sets, visualization of graphs, and much more.
- Network:
  - requests: is a package which we can use to send requests to a server(GET, POST, DELETE, PUT)
    - _pip install requests_

## Exercises: Day 20

1. Read this url and find out the 10 most frequent words.romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
1. Read the cats api and cats_api = 'https://api.thecatapi.com/v1/breeds' and find the avarage weight of cat in metric unit.
1. Read the countries api and find out the 10 largest countries
1. UCI is one the most common place for get data set for data science and machine learning. Read the content of UCL(http://mlr.cs.umass.edu/ml/datasets.html). Without library it will be difficult, you may try it with BeautifulSoup4

# 📘 Day 21

## Classes and Objects

Python is an object oriented programming language. Everything in Python is an object, with its properties and methods. A number, string, list, dictionary,tuple, set etc. used in a program is an object of a corresponding built-in class. We create class to create an object. A Class is like an object constructor, or a "blueprint" for creating objects. We instantiate a class to create an object. The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.

We have been working with classes and objects right from the beginning of these challenge unknowingly. Every element in a Python program is an object of a class.
Let's check if everything in python is class:

```py
Last login: Tue Dec 10 09:35:28 on console
asabeneh@Asabeneh:~$ pyhton
-bash: pyhton: command not found
asabeneh@Asabeneh:~$ python
Python 3.7.5 (default, Nov  1 2019, 02:16:32)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### Creating a Class

To create a class we need the key word **class** followed by colon. Class name should be **CamelCase**.

```sh
# syntax
class ClassName:
  code goes here
```

**Example:**

```py
class Person:
  pass
```

```sh
<__main__.Person object at 0x10804e510>
```

### Creating an Object

We can create an object by calling the class.

```py
p = Person()
print(p)
```

### Class Constructor

In the above examples, we have created an object from the Person class. However, Class without a constructor is not really useful in real applications. Let's use constructor function to make our class more useful. Like the constructor function in Java or JavaScript, python has also a builtin _**init**()_ constructor function. The _**init**_ constructor function has self parameter which is a reference to the current instance of the class
**Examples:**

```py
class Person:
      def __init__ (self, name):
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# output
Asabeneh
```

Let's add more parameter to the constructor function.

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# output
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### Object Methods

Objects can have methods. The methods are functions which are belongs to the object.
**Example:**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}, {self.country}'


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# output
Asabeneh Yetayeh is 250 year old. He lives in Helsinki, Finland
```

### Object default methods

Sometimes, you may want to have a default values for you object methods. If we give a default values for the parameters in the constructor, we can avoid error when we call or instantiate our class without parameters. Let's see how it looks using example.

**Example:**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# output
Asabeneh Yetayeh is 250 year old. He lives in Helsinki, Finland.
John Doe is 30 year old. He lives in Noman city, Nomanland.
```

### Method to modify class default values

In the example below, the person class, all the constructor parameters have default values and in addition to that we have a skills default value which we can access it using method. Let's create add_skill method to add skill to the skills list.

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} year old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# output
Asabeneh Yetayeh is 250 year old. He lives in Helsinki, Finland.
John Doe is 30 year old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Inheritance

Using inheritance we can reuse parent class code. Inheritance allows us to define a class that inherits all the methods and properties from another class. The parent class or super or base class is the class which gives all the methods and properties. Child class is the class the inherits from another class.
Let's see create a student class by inheriting from person class.

```py
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

```sh
output
Eyob Yetayeh is 30 year old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 year old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

We didn't call the _**init**()_ constructor in the child class. If we didn't call it we can access all the properties but if we call it once we access the parent properties by calling _super_.  
We can write add a new method to the child or we can overwrite the parent class by creating the same method name in the child class. When we add the **init**() function, the child class will no longer inherit the parent's **init**() function.

### Overriding parent method

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} year old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
Eyob Yetayeh is 30 year old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 year old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

We can use super() function or the parent name Person to automatically inherit the methods and properties from its parent. In the above example, we override the parant method. The child method has a different feature, it can identify if the gender is male or female and assign the proper pronoun(He/She).

## 💻 Exercises: Day 21

1. Python has the module called _statistics_ and we can use this module to do all the statistical caluculations. Hower to challlenge ourselves, let's try to develop a program which calculate measure of central tendency of a sample(mean, median, mode) and measure of variability(range, variance, standard deviation). In addition to those measures find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions which do statistical calculations as method for the Statistics class. Check the output below.

```py
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ',data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Variance: ',data.var()) # 17.5
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ',data.var()) # 17.5
print('Frequency Distribution: ',data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# you output should look like this
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```
1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info,add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description and the same goes for expenses.
   
[<< Part 6 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md) | [Part 8 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme22-24.md)

---
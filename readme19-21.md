![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

🧳 [Part 1: Day 1 - 3](https://github.com/Asabeneh/30-Days-Of-Python)  
🧳 [Part 2: Day 4 - 6](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)  
🧳 [Part 3: Day 7 - 9](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)  
🧳 [Part 4: Day 10 - 12](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)  
🧳 [Part 5: Day 13 - 15](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)  
🧳 [Part 6: Day 16 - 18](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)  
🧳 [Part 7: Day 19 - 21](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)   
🧳 [Part 8: Day 22 - 24](#) 🔒  
🧳 [Part 9: Day 25 - 27](#) 🔒  
🧳 [Part 10: Day 28 - 30](#) 🔒

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
# 📘 Day 19
## File handling
So far we have seen different python data types. We usually store our data in a different file format. In addition to handling file, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) file formats in this section. First, let's get familiar with handling file with common file format(.txt).  

File handling is an import part of programming which allows us to create, read, update and delete files. In python to handle data we use *open()* builtin function.
```py
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b,  could be to read, write, update
```
* "r" - Read - Default value. Opens a file for reading, error if the file does not exist
* "a" - Append - Opens a file for appending, creates the file if it does not exist
* "w" - Write - Opens a file for writing, creates the file if it does not exist
* "x" - Create - Creates the specified file, returns an error if the file exists
* "t" - Text - Default value. Text mode
* "b" - Binary - Binary mode (e.g. images)
### Opening File for reading
The default mode of *open* is reading, so we do not have to specify 'r' or 'rt'. I have created and saved a file named reading_file_example.txt in the files directory. Let see read this file.
```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```
As you can see in the above example, I printed the opened file and it gave me some information about the opened file. Opened file has different reading methods: *read()*, *readline*, *readlines*. An opened file has to be closed with *close()* method.
* *read()*: read the whole text as string. If we want to limit the number of characters we read, we can limit it by passing int value to the methods.
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
* *readline()*: read only the first line
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
* *readlines()*: read all the text line by line and returns a list of lines
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
Another way to get all the lines a list is using *splitlines()*:
```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```
```sh
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```
After we open a file, we should close the file but there is a high tendency to forget to close. There is a new way of opening method, *with* which closes by itself. Let's write the above code with *with*.
```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```
```sh
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```
### Opening file for writing or updating
To write to an existing file, we  must add a mode as parameter to the *open()* function:
* "a" - append - will append to the end of the file if the file does not exist it raise FileNotFoundError.
* "w" - write - will overwrite any existing content if the file does not exist it creates.

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
###  Deleting file
We have seen in previous section, how to make and remove a directory using *os* module. Again now, if we want to remove a file we use *os* module.

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
File with *txt* extension is a very common form data and we have covered it in the previous section. Let's move to the JSON file
### File with json Extension
JSON stands for JavaScript Object Notation. Actually, it a stringified JavaScript object.
*Example:*
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
To change a JSON to a dictionary we use *loads* method.

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
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### Changing dictionary to JSON
To change a dictionary to a JSON we use *dumps* method.
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
Column names are :name, country, city, skills
        Asabeneh is a teachers. He lives in Finland, Helsinki.
Number of lines:  2
```
### File with xlsx Extension
To read excel we need to install *xlrd* package. We will cover this after we cover package installing using pip.
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
    print('field', child.tag)
```
```sh
Root tag: person
Attribute: {'gender': 'male'}
field name
field country
field city
field skills
```

## 💻 Exercises: Day 19
1. Writ a function which count number of lines and number of words from a text. All the files are in data the folder:
   1. Read obama_speech.txt file and count number of lines and now of words
   2. Read michelle_obama_speech.txt file and count number of lines and now of words
   3. Read donald_speech.txt file and count number of lines and now of words
   4. Read melina_trump_speech.txt file and count number of lines and now of words
2. Read the countries_data.json data file in data directory, create a function which find the ten most spoken languages
    ```py
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
    (4, 'Serbian')
    ]
    print(most_spoken_languages(filename='./data/countries_data.json', 3))

    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic')
    ]
    ```
3. Read the countries_data.json data file in data directory,create a function which create the ten most populated countries
    ```py
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

    print(most_populated_countries(filename='./data/countries_data.json', 3))

    [{'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000}]
    ```
4. Extract all incoming emails from the email_exchange_big.txt file. 
5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters which are a string or a file and a positive integer. Your function will return an array of tuples in descending order. Check the output
```py

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
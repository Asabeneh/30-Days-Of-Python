<div align="center">
  <h1> 30 Days Of Python: Day 18 - Regular Expressions </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Author:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> First Edition: Nov 22 - Dec 22, 2019</small>
  </sub>
</div>
</div>

[<< Day 17](../17_Day/17_exception_handling.md) | [Day 19>>](../19_Day/19_file_handling.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 18](#%f0%9f%93%98-day-18)
  - [Regular Expression](#regular-expression)
    - [Import re module](#import-re-module)
    - [re functions](#re-functions)
      - [Match](#match)
      - [Search](#search)
      - [Searching all matches using findall](#searching-all-matches-using-findall)
      - [Replacing a substring](#replacing-a-substring)
  - [Spliting text using RegEx split](#spliting-text-using-regex-split)
  - [Writing RegEx pattern](#writing-regex-pattern)
    - [Square Bracket](#square-bracket)
    - [Escape character(\\) in RegEx](#escape-character-in-regex)
    - [One or more times(+)](#one-or-more-times)
    - [Period(.)](#period)
    - [Zero or more times(*)](#zero-or-more-times)
    - [Zero or one times(?)](#zero-or-one-times)
    - [Quantifier in RegEx](#quantifier-in-regex)
    - [Cart ^](#cart)
  - [💻 Exercises: Day 18](#%f0%9f%92%bb-exercises-day-18)


# 📘 Day 18
## Regular Expression
A regular expression or RegEx is a small programming language that helps to find pattern in data. A RegEx can be used to check if some pattern exists in a different data type. To use RegEx in python first we should import the RegEx module which is *re*.

### Import re module
After importing the module we can use it to detect or find patterns.
```py
import re
```
### re functions
To find a pattern we use different set of *re* functions that allows to search a string for match.
* *re.match()*:searches only in the beginning of the first line of the string and return match object if found, else return none. 
* *re.search*:Returns a Match object if there is a match anywhere in the string including or in multiline string.
* *re.findall*:Returns a list containing all matches
* *re.split*:	Returns a list where the string has been split at each match
* *re.sub*:  Replaces one or many matches with a string

#### Match
```py
# syntac
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
```
```py
txt = 'I love to teach python or javaScript'
# It return an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```
As you can see from the above example, the pattern we are looking for or the substring *I love to teach* is the beginning of the text. The match function only returns an object if the text starts with the pattern.

#### Search
```py
# syntax
re.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag
```
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

# It return an object with span, and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```
As you can see search is much better than match because it can look for the pattern through out the text. Search return returns a match object right way a first match found. A much better *re* function is *findall*. This function check the pattern through the string and returns all the matches as a list.

#### Searching all matches using findall
*findall()* returns all the matches as a list

```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

```
As you can see, the word language found two times in the string. Let's practice more

Let's look for the word both Python and python in the string
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```
Since we are using *re.I* both lowercase and uppercase are included but if we don't have the flag, we write our pattern differently. Let's see that
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```
#### Replacing a substring
```py
txt = '''Python is the most beautiful language that a human begin has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human begin has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human begin has ever created.
```
Let's add one more example, the following string is really hard to read unless we remove the % symbol. Replacing the % with a empty string will clean the text.
```py

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as m%ore r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher.'''

matches = re.sub('%', '', txt)
print(matches)  # ['Python', 'python']
```
```sh
I am teacher and  I love teaching.
There is nothing as more rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher.
```
## Spliting text using RegEx split
```py
txt = '''I am teacher and  I love teaching.
There is nothing as more rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher.'''
print(re.split('\n', txt))
```
```sh
['I am teacher and  I love teaching.', 'There is nothing as more rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher.']
```
## Writing RegEx pattern
To declare a string variable we use a single or double quote. To declare RegEx variable *r''*.
The following pattern only identifies apple with lowercase, to make it case insensitive either we should rewrite our pattern or we should add a flag.  
```py
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```
* []:  A set of characters
  * [a-c] means, a or b or c
  * [a-z] means, any letter a to z
  * [A-Z] means, any character A to Z
  * [0-3] means, 0 or 1 or 2 or 3
  * [0-9] means any number 0 to 9
  * [A-Za-z0-9] any character which is a to z, A to Z, 0 to 9
* \\:  uses to escape special characters
  * \d mean:match where the string contains digits (numbers from 0-9)
  * \D mean: match where the string does not contain digits
* . : any character except new line character(\n)
* ^: starts with
  * r'^substring' eg r'^love', a sentence which starts with a word love
  * r'[^abc] mean not a, not b, not c.
* $: ends with
  * r'substring$' eg r'love$', sentence ends with a word love
* *: zero or more times
  * r'[a]*' means a optional or it can be occur many times.
* +: one or more times
  * r'[a]+' mean at least once or more times
* ?: zero or one times
  *  r'[a]?' mean zero times or once
* {3}: Exactly 3 characters
* {3,}: At least 3 character
* {3,8}: 3 to 8 characters
* |: Either or
  * r'apple|banana' mean either of an apple or a banana
* (): Capture and group

![Regular Expression cheat sheet](images/regex.png)

Let's use example to clarify the above meta characters
### Square Bracket
Let's use square bracket to include lower and upper case
```py
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```
If we want to look for the banana, we write the pattern as follows:
```py
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```
Using the square bracket and or operator , we manage to extract Apple, apple, Banana and banana.

### Escape character(\\) in RegEx
```py
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made in December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9'], this is not what we want

regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more
txt = 'This regular expression example was made in December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']
```
### One or more times(+)
```py
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made in December 6,  2019.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']
```

### Period(.)
```py
regex_pattern = r'[a].'  # this square bracket means a and . means any character except new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

```
### Zero or more times(*)
Zero or many times. The pattern could may not occur or it can occur many times.
```py

regex_pattern = r'[a].*'  # . any character, + any character one or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

```
### Zero or one times(?)
Zero or one times. The pattern could may not occur or it may occur once.
```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

```
### Quantifier in RegEx
We can specify the length of the substring we look for in a text, using a curly bracket. Lets imagine, we are interested in substring that their length are 4 characters
```py
txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019']

txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019']

```
### Cart ^
* Starts with
  
```py
txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'^This'  # ^ means starts with
print(matches)  # ['This']
```

* Negation
```py
txt = 'This regular expression example was made in December 6,  2019.'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```


## 💻 Exercises: Day 18
  1. What is the most frequent word in the following paragraph ?
```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```
```sh
    [(6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')]
```
2. The position of some particles on the horizontal x-axis -12, -4, -3 and  -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers and find the distance between the two furthest particles.
```py
points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 12
```
3. Write a pattern which identify if a string is a valid python variable
    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```
4. Clean the following text. After cleaning, count three most frequent words in the string.
    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```


    
🎉 CONGRATULATIONS ! 🎉

[<< Day 17](../17_Day/17_exception_handling.md) | [Day 19>>](../19_Day/19_file_handling.md)
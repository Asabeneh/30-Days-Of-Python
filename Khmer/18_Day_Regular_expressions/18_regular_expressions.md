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

[<< Day 17](../17_Day_Exception_handling/17_exception_handling.md) | [Day 19>>](../19_Day_File_handling/19_file_handling.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 18](#-day-18)
  - [Regular Expressions](#regular-expressions)
    - [The *re* Module](#the-re-module)
    - [Methods in *re* Module](#methods-in-re-module)
      - [Match](#match)
      - [Search](#search)
      - [Searching for All Matches Using *findall*](#searching-for-all-matches-using-findall)
      - [Replacing a Substring](#replacing-a-substring)
  - [Splitting Text Using RegEx Split](#splitting-text-using-regex-split)
  - [Writing RegEx Patterns](#writing-regex-patterns)
    - [Square Bracket](#square-bracket)
    - [Escape character(\\) in RegEx](#escape-character-in-regex)
    - [One or more times(+)](#one-or-more-times)
    - [Period(.)](#period)
    - [Zero or more times(\*)](#zero-or-more-times)
    - [Zero or one time(?)](#zero-or-one-time)
    - [Quantifier in RegEx](#quantifier-in-regex)
    - [Cart ^](#cart-)

# 📘 Day 18

## Regular Expressions

Regular expression ឬ RegEx ជាខ្សែអក្សរពិសេសដែលជួយរកគំរូនៅក្នុងទិន្នន័យ។ RegEx អាចប្រើដើម្បីពិនិត្យមើលថាតើមានគំរូណាមួយមាននៅក្នុងប្រភេទទិន្នន័យផ្សេងៗ។ ដើម្បីប្រើ RegEx ក្នុង Python ដំបូងយើងត្រូវនាំចូល Module RegEx ដែលហៅថា *re*។
Pattern = គំរូ

### The *re* Module

ក្រោយពីនាំចូល Module យើងអាចប្រើវាដើម្បីរកគំរូ។

```py
import re
```

### Methods in *re* Module

ដើម្បីរកគំរូយើងប្រើ set *re* ផ្សេងៗ ដែលអនុញ្ញាតឱ្យស្វែងរកភាពដូចគ្នាក្នុង String។

* *re.match()*: ស្វែងរកតែនៅដើមនៃ string និង បញ្ជូនមកវីញវត្ថុដែលដូចគ្នាប្រសិនរកឃើញ បើមិនរកឃើញនោះបញ្ជូនមកវិញ None ។
* *re.search*: បញ្ជូនមកវិញវត្ថដែលដូចគ្នាុ ប្រសិនបើវាមាននៅកន្លែងណាមួយនៅក្នុង string រួមទាំង string ដែលមានច្រើនជួរ។
* *re.findall*: បញ្ជូន list ដែលមានលក្ខណៈដូចគ្នាទាំងអស់។
* *re.split*: យក string, បំបែកវានៅចំណុចដូចគ្នា, វិលត្រឡប់ទៅ list។
* *re.sub*:  ជំនួសការដូុចគ្នាមួយឬច្រើននៅក្នុង string។

#### Match

```py
# syntac
re.match(substring, string, re.I)
# substring គឺជា string ឬគំរូ, string គឺអក្សរដែលយើងស្វែងរកជាគំរូ , re.I គឺករណីដែលយើងមិនខ្វល់
```

```py
import re

txt = 'I love to teach python and javaScript'
# វាត្រឡប់មកវិញនូវ object ជាមួយ span និង match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# យើងអាចទទួលបានតំណាងដើម និងទីបញ្ចប់នៃ match ជា tuple ដោយប្រើ span
span = match.span()
print(span)     # (0, 15)
# រកទីតាំងចាប់ផ្តើម និងឈប់ ពីតាម span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # ទទួលបាន 'I love to teach'
```

ដូចឧទាហរណ៍ខាងលើ គំរូដែលយើងកំពុងស្វែងរកគឺ *I love to teach* ។ វិធីសាស្រ្ត Match បានមកវិញនូវ object បើសិនអក្សរចាប់ផ្តើមដោយគំរូួ។

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

String មិនជាប់ជាមួយ *I like to teach*, ដូច្នេះគ្មានការដូចគ្នា ហើយវិធីសាស្រ្ត Match ត្រឡប់មកវិញថា None ។

#### Search

```py
# syntax
re.match(substring, string, re.I)
# substring គឺជា string ឬគំរូ, string គឺអក្សរដែលយើងស្វែងរកជាគំរូ , re.I គឺករណីដែលយើងមិនខ្វល់
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# វាត្រឡប់មកវិញ object ជាមួយ span និង match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# យើងអាចទទួលបានតំណាងដើម និងទីបញ្ចប់នៃ match ជា tuple ដោយប្រើ span
span = match.span()
print(span)     # (100, 105)
# វាត្រឡប់មកវិញនូវ object ជាមួយ span និង match
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # បាន first
```

As you can see, search is much better than match because it can look for the pattern throughout the text. Search returns a match object with a first match that was found, otherwise it returns _None_. A much better *re* function is *findall*. This function checks for the pattern through the whole string and returns all the matches as a list.

#### Searching for All Matches Using *findall*

*findall()* returns all the matches as a list

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

As you can see, the word *language* was found two times in the string. Let us practice some more.
Now we will look for both Python and python words in the string:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

Since we are using *re.I* both lowercase and uppercase letters are included. If we do not have the re.I flag, then we will have to write our pattern differently. Let us check it out:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

#### Replacing a Substring

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
```

Let us add one more example. The following string is really hard to read unless we remove the % symbol. Replacing the % with an empty string will clean the text.

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

## Splitting Text Using RegEx Split

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## Writing RegEx Patterns

To declare a string variable we use a single or double quote. To declare RegEx variable *r''*.
The following pattern only identifies apple with lowercase, to make it case insensitive either we should rewrite our pattern or we should add a flag.  

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# To make case insensitive adding flag '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# or we can use a set of characters method
regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```
* []:  A set of characters
  * [a-c] means, a or b or c
  * [a-z] means, any letter from a to z
  * [A-Z] means, any character from A to Z
  * [0-3] means, 0 or 1 or 2 or 3
  * [0-9] means any number from 0 to 9
  * [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
* \\:  uses to escape special characters
  * \d means: match where the string contains digits (numbers from 0-9)
  * \D means: match where the string does not contain digits
* . : any character except new line character(\n)
* ^: starts with
  * r'^substring' eg r'^love', a sentence that starts with a word love
  * r'[^abc] means not a, not b, not c.
* $: ends with
  * r'substring$' eg r'love$', sentence  that ends with a word love
* *: zero or more times
  * r'[a]*' means a optional or it can occur many times.
* +: one or more times
  * r'[a]+' means at least once (or more)
* ?: zero or one time
  *  r'[a]?' means zero times or once
* {3}: Exactly 3 characters
* {3,}: At least 3 characters
* {3,8}: 3 to 8 characters
* |: Either or
  * r'apple|banana' means either apple or a banana
* (): Capture and group

![Regular Expression cheat sheet](../images/regex.png)

Let us use examples to clarify the meta characters above 

### Square Bracket

Let us use square bracket to include lower and upper case

```py
regex_pattern = r'[Aa]pple' # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

If we want to look for the banana, we write the pattern as follows:

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # this square bracket means either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

Using the square bracket and or operator , we manage to extract Apple, apple, Banana and banana.

### Escape character(\\) in RegEx

```py
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
```

### One or more times(+)

```py
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!
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

### Zero or more times(\*)

Zero or many times. The pattern could may not occur or it can occur many times.

```py
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Zero or one time(?)

Zero or one time. The pattern may not occur or it may occur once.

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### Quantifier in RegEx

We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Cart ^

* Starts with
  
```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

* Negation

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

[<< Day 17](../17_Day_Exception_handling/17_exception_handling.md) | [Day 19>>](../19_Day_File_handling/19_file_handling.md)
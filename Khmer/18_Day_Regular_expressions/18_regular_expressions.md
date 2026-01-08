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

ដូចដែលអ្នកអាចមើលបាន search គឺល្អជាង match ព្រោះវាអាចស្វែងរកគំរូនៅទូទាំងអត្ថបទ។ Search ផ្តល់ object match ជាមួយនឹង match ដំបូងដែលត្រូវបានរកឃើញ បើមិនដូច្នោះទេវានឹងផ្ដល់ _None_ ។ function *re* ល្អជាងគឺ *findall*។ function នេះរួតពិនិត្យសម្រាប់គំរូក្នុង string ទាំងមូលនិងត្រឡប់មក match ទាំងអស់ជា list។

#### Searching for All Matches Using *findall*

*findall()* ត្រឡប់មក match ទាំងអស់ជា list

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

ដូចដែលអ្នកអាចមើលបាន ពាក្យ "language" ត្រូវបានរកឃើញពីរដងនៅក្នុង string ។
ឥឡូវយើងនឹងរកពាក្យ Python និង python ទាំងពីរនៅក្នុង string:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

ដោយសារយើងប្រើ *re.I* ទាំងអក្សរតូច និងអក្សរធំ ត្រូវបានបញ្ចូល។ បើសិនជាយើងគ្មាន re,I, នោះយើងនឹងត្រូវសរសេរគំរូរបស់យើងខុសពីមុន។ សូមយើងមើល:

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

សូមយើងបន្ថែមឧទាហរណ៍មួយទៀត។ String ទាំងនេះពិតជាពិបាកក្នុងការអានលើកលែងតែយើងលុបសញ្ញា % ចេញ។

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
print(re.split('\n', txt)) # ការបំបែក ដោយប្រើ \n - end of line symbol
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## Writing RegEx Patterns

ដើម្បីបង្កើត string variable, យើងប្រើ single ឬ double quote។ ដើម្បីបង្កើត RegEx variable *r''*។ គំរូខាងក្រោមនេះបង្ហាញថា Apple មានអក្សរតូចប៉ុណ្ណោះ ដើម្បីធ្វើឱ្យវាមិនខ្វល់អក្សរតូចឬធំ យើងត្រូវសរសេរគំរូថ្មី ឬយើងត្រូវបន្ថែម flag។

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

- []:  set នៃអក្សរ
  * [a-c] មានន័យ, a ឬ b ឬ c
  * [a-z] មានន័យ, អក្សរណាមួយពី a ទៅ z
  * [A-Z] មានន័យ, អក្សរណាមួយពី A ទៅ Z
  * [0-3] មានន័យ, 0 ឬ 1 ឬ 2 ឬ 3
  * [0-9] មានន័យ លេខណាមួយពី 0 ទៅ 9
  * [A-Za-z0-9] អក្សរតែមួយតង់, នេះគឺ a ទៅ z, A ទៅ Z ឬ 0 ទៅ 9
* \\:  ប្រើទៅ escape special characters
  * \d មានន័យ: match ដែល string មានលេខ (លេខពី 0-9)
  * \D មានន័យ: match ដែល string មិនមានលេខ
* . : អក្សរណាមួយ លើកលែងតែ new line character(\n)
* ^: ចាប់ផ្តើមដោយ
  * r'^substring' eg r'^love', ប្រយោគដែលចាប់ផ្តើមដោយពាក្យថា "love"
  * r'[^abc] មានន័យ មិនមែនជា a, មិនមែនជា b, មិនមែនជា c.
* $: បញ្ចប់ដោយ
  * r'substring$' eg r'love$', ប្រយោគដែលបញ្ចប់ដោយពាក្យថា "love"
* *: សូន្យ ឬ ច្រើនដងទៀត
  * r'[a]*' មានន័យ ជាជម្រើស ឬ វាអាចកើតឡើងច្រើនដង
* +: មួយ ឬ ច្រើនដងទៀត
  * r'[a]+' មានន័យ យ៉ាងហោចណាស់ម្តង (ឬ ច្រើនទៀត)
* ?: សូន្យ ឬ មួយដង
  *  r'[a]?' មានន័យ សូន្យដង ឬ ម្តង
* {3}: 3 តួអក្សរ
* {3,}: យ៉ាងហោចណាស់ 3 តួអក្សរ
* {3,8}: ពី 3 ទៅ 8 តួអក្សរ
* |: ឬក៏
  * r'apple|banana' មានន័យថា apple ឬ banana
* (): ចាប់យកនិងដាក់ក្រុម

![Regular Expression cheat sheet](../images/regex.png)

សូមយើងប្រើឧទាហរណ៍ដើម្បីយល់ meta characters ខាងលើ

### Square Bracket

យើងត្រូវប្រើតង្កៀបដើម្បីបញ្ចូលអក្សរតូច និងធំ

```py
regex_pattern = r'[Aa]pple' # តង្កៀបនេះមានន័យថា A ឬ a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

ប្រសិនបើយើងចង់ស្វែងរក banana យើងសរសេរគំរូដូចខាងក្រោម:

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # តង្កៀបនេះមានន័យថា A ឬ a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

Using the square bracket and or operator , we manage to extract Apple, apple, Banana and banana.

### Escape character(\\) in RegEx

```py
regex_pattern = r'\d'  # d គឺជាតួរអក្សរពិសេស ដែលមានន័យថាលេខ
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want
```

### One or more times(+)

```py
regex_pattern = r'\d+'  # d គឺជាតួរអក្សរពិសេស ដែលមានន័យថាលេខ, + មានន័យថាមួយ ឬច្រើនដង
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - ឥឡូវនេះវាប្រសើរជាង!
```

### Period(.)

```py
regex_pattern = r'[a].'  # តង្កៀបនេះមានន័យថា a និង . មានន័យថាតួអក្សរណាមួយ លើកលែងតែបន្ទាត់ថ្មី។
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . តួអក្សរទាំងអស់, + តួអក្សរណាមួយម្តង ឬច្រើនដង
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Zero or more times(\*)

Zero or many times. អាចនឹងមិនកើតឡើង ឬវាអាចកើតឡើងច្រើនដង។

```py
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Zero or one time(?)

Zero or one time. ប្រហែលជាមិនកើតឡើង ឬវាអាចកើតឡើងតែម្តង។

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? មានន័យថានៅទីនេះ '-' គឺមិនចាំបាច់
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### Quantifier in RegEx

We can specify the length of the substring we are looking for in a text, using a curly bracket. Let us imagine, we are interested in a substring with a length of 4 characters:

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # ៤ដង
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 ទៅ 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Cart ^

* ចាប់ផ្តើមដោយ
  
```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ មានន៏យថា ចាប់ផ្តើមដោយ
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

* Negation

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ ក្នុង set character មានន៏យថា negation, មិនមែន A ទៅ Z, មិនមែន a ទៅ z, គ្មានដកគ្លា
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

[<< Day 17](../17_Day_Exception_handling/17_exception_handling.md) | [Day 19>>](../19_Day_File_handling/19_file_handling.md)
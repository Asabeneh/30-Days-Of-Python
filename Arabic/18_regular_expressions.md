<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 18 - التعبيرات المنتظمة</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="متابعة في تويتر" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>المؤلف:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>الطبعة الثانية: يوليو 2021</small>
  </sub>
</div>

[<< اليوم 17](./17_exception_handling.md) | [اليوم 19 >>](./19_file_handling.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 18](#-اليوم-18)
  - [التعبيرات المنتظمة](#التعبيرات-المنتظمة)
    - [وحدة *re*](#وحدة-re)
    - [الدوال في وحدة *re*](#الدوال-في-وحدة-re)
      - [Match](#match)
      - [Search](#search)
      - [البحث عن جميع التطابقات باستخدام *findall*](#البحث-عن-جميع-التطابقات-باستخدام-findall)
      - [استبدال النص الفرعي](#استبدال-النص-الفرعي)
  - [تقسيم النص باستخدام RegEx Split](#تقسيم-النص-باستخدام-regex-split)
  - [كتابة أنماط RegEx](#كتابة-أنماط-regex)
    - [القوس المربع](#القوس-المربع)
    - [حرف الهروب (\\) في RegEx](#حرف-الهروب--في-regex)
    - [مرة واحدة أو أكثر (+)](#مرة-واحدة-أو-أكثر-)
    - [النقطة (.)](#النقطة-)
    - [صفر أو أكثر مرات (\*)](#صفر-أو-أكثر-مرات-)
    - [صفر أو مرة واحدة (?)](#صفر-أو-مرة-واحدة-)
    - [الكمّي في RegEx](#الكمّي-في-regex)
    - [الإطار ^](#الإطار-)
  - [💻 تمارين: اليوم 18](#-تمارين-اليوم-18)
    - [تمارين: المستوى 1](#تمارين-المستوى-1)
    - [تمارين: المستوى 2](#تمارين-المستوى-2)
    - [تمارين: المستوى 3](#تمارين-المستوى-3)

# 📘 اليوم 18

## التعبيرات المنتظمة

التعبير المنتظم أو 'RegEx' هو نص خاص يساعد في العثور على أنماط في البيانات. يمكن استخدام 'RegEx' للتحقق من وجود نمط معين في نوع بيانات مختلف. لاستخدام 'RegEx' في بايثون يجب علينا أولاً استيراد وحدة 'RegEx' التي تسمى 're'.

### وحدة *re*

بعد استيراد الوحدة يمكننا استخدامها لاكتشاف الأنماط أو العثور عليها.

```py
import re
```

### الدوال في وحدة *re*

للعثور على نمط نستخدم مجموعة مختلفة من مجموعات أحرف 're' التي تسمح بالبحث عن تطابق في نص.

- 're.match()': يبحث فقط في بداية السطر الأول من النص ويعيد كائنات مطابقة إذا وجدت، وإلا يعيد 'None'.
- 're.search': يعيد كائن تطابق إذا وجد واحد في أي مكان من النص، بما في ذلك النصوص متعددة الأسطر.
- 're.findall': يعيد قائمة تحتوي على جميع التطابقات.
- 're.split': يأخذ نصًا، ويقسمه عند نقاط التطابق، ويعيد قائمة.
- 're.sub': يستبدل تطابقًا واحدًا أو أكثر في نص.

#### Match

```py
# صيغة
re.match(substring, string, re.I)
# substring هو نص أو نمط، string هو النص الذي نبحث فيه عن نمط، re.I يعني تجاهل حالة الأحرف
```

```py
import re

txt = 'I love to teach python and javaScript'
# يعيد كائنًا به span و match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# يمكننا الحصول على موضع البداية والنهاية للتطابق كتوبل باستخدام span
span = match.span()
print(span)     # (0, 15)
# لنحصل على موضع البداية والنهاية من span
start, end = span
print(start, end)  # 0 15
substring = txt[start:end]
print(substring)       # I love to teach
```

كما ترى من المثال أعلاه، النمط الذي نبحث عنه (أو النص الفرعي الذي نبحث عنه) هو 'I love to teach'. دالة 'match' تعيد كائنًا **فقط** إذا بدأ النص بالنمط.

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

النص لا يبدأ بـ 'I like to teach'، لذا لم يكن هناك تطابق وأعادت دالة 'match' قيمة 'None'.

#### Search

```py
# صيغة
re.search(substring, string, re.I)
# substring هو نمط، string هو النص الذي نبحث فيه عن نمط، re.I هو علامة تجاهل حالة الأحرف
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# يعيد كائنًا به span و match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# يمكننا الحصول على موضع البداية والنهاية للتطابق كتوبل باستخدام span
span = match.span()
print(span)     # (100, 105)
# لنحصل على موضع البداية والنهاية من span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

كما ترى، البحث أفضل بكثير من 'match' لأنه يمكنه البحث عن النمط في جميع أنحاء النص. يعيد البحث كائن تطابق بأول تطابق يجده، وإلا يعيد 'None'. دالة 're' الأفضل بكثير هي 'findall'. هذه الدالة تتحقق من النمط في جميع أنحاء النص وتعيد جميع التطابقات كقائمة.

#### البحث عن جميع التطابقات باستخدام 'findall'

'findall()' يعيد جميع التطابقات كقائمة

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# يعيد قائمة
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

كما ترى، وجدت كلمة 'language' مرتين في النص. دعنا نتدرب أكثر.

الآن سنبحث عن كلمة Python و python في النص:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# يعيد قائمة
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

بما أننا نستخدم 're.I'، فالحروف الكبيرة والصغيرة مشمولة. إذا لم يكن لدينا علامة 're.I'، سنحتاج إلى كتابة نمطنا بشكل مختلف. دعنا نتحقق:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

#### استبدال النص الفرعي

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
# أو
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
```

لنضف مثالًا آخر. النص التالي صعب القراءة حقًا إلا إذا أزلنا رمز '%'. استبدال '%' بنص فارغ سينظف النص.

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

## تقسيم النص باستخدام RegEx Split

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # تقسيم باستخدام \n - رمز نهاية السطر
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## كتابة أنماط RegEx

لإعلان متغير نص نستخدم اقتباسًا مفردًا أو مزدوجًا. لإعلان متغير 'RegEx' نستخدم r''.
النمط التالي يتعرف فقط على apple بأحرف صغيرة، لجعله غير حساس للحالة يجب إعادة كتابة النمط أو إضافة علامة.

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# لجعله غير حساس للحالة بإضافة علامة
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# أو يمكننا استخدام طريقة مجموعة من الأحرف
regex_pattern = r'[Aa]pple'  # هذا يعني أن الحرف الأول يمكن أن يكون A أو a
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```

* []: مجموعة من الأحرف
  - [a-c] يعني a أو b أو c
  - [a-z] يعني أي حرف من a إلى z
  - [A-Z] يعني أي حرف من A إلى Z
  - [0-3] يعني 0 أو 1 أو 2 أو 3
  - [0-9] يعني أي رقم من 0 إلى 9
  - [A-Za-z0-9] أي حرف واحد، من a إلى z أو A إلى Z أو 0 إلى 9
- \\: يُستخدم للإفلات من الأحرف الخاصة
  - \d يعني: تطابق عندما يحتوي النص على أرقام (أرقام من 0-9)
  - \D يعني: تطابق عندما لا يحتوي النص على أرقام
- . : أي حرف باستثناء حرف السطر الجديد (\n)
- ^: يبدأ بـ
  - r'^substring' مثال r'^love'، جملة تبدأ بكلمة love
  - r'[^abc] يعني ليس a، ليس b، ليس c.
- $: ينتهي بـ
  - r'substring$' مثال r'love$'، جملة تنتهي بكلمة love
- *: صفر أو أكثر مرات
  - r'[a]*' يعني a اختياري أو يمكن أن يحدث عدة مرات.
- +: مرة واحدة أو أكثر
  - r'[a]+' يعني مرة واحدة على الأقل (أو أكثر)
- ?: صفر أو مرة واحدة
  - r'[a]?' يعني صفر مرات أو مرة واحدة
- {3}: بالضبط 3 أحرف
- {3,}: 3 أحرف على الأقل
- {3,8}: من 3 إلى 8 أحرف
- |: إما أو
  - r'apple|banana' يعني إما apple أو banana
- (): التقاط وتجميع

![ورقة غش التعبيرات المنتظمة](../images/regex.png)

لنستخدم أمثلة لتوضيح الرموز الوسيطة أعلاه

### القوس المربع

لنستخدم القوس المربع لتضمين الحروف الكبيرة والصغيرة

```py
regex_pattern = r'[Aa]pple' # هذا القوس المربع يعني إما A أو a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

إذا أردنا البحث عن banana، نكتب النمط كما يلي:

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # هذا القوس المربع يعني إما A أو a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

باستخدام القوس المربع وعامل أو، نجحنا في استخراج Apple و apple و Banana و banana.

### حرف الهروب (\\) في RegEx

```py
regex_pattern = r'\d'  # d حرف خاص يعني الأرقام
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']، هذا ليس ما نريده
```

### مرة واحدة أو أكثر (+)

```py
regex_pattern = r'\d+'  # d حرف خاص يعني الأرقام، + تعني مرة واحدة أو أكثر
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - الآن، هذا أفضل!
```

### النقطة (.)

```py
regex_pattern = r'[a].'  # هذا القوس المربع يعني a و . تعني أي حرف باستثناء السطر الجديد
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . أي حرف، + أي حرف مرة واحدة أو أكثر
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### صفر أو أكثر مرات (\*)

صفر أو عدة مرات. قد لا يحدث النمط أو يمكن أن يحدث عدة مرات.

```py
regex_pattern = r'[a].*'  # . أي حرف، * أي حرف صفر أو أكثر مرات
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### صفر أو مرة واحدة (?)

صفر أو مرة واحدة. قد لا يحدث النمط أو يحدث مرة واحدة.

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? تعني هنا أن '-' اختياري
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### الكمّي في RegEx

يمكننا تحديد طول النص الفرعي الذي نبحث عنه في نص باستخدام القوس المعقوف. لنتخيل أننا مهتمون بنص فرعي بطول 4 أحرف:

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # بالضبط أربع مرات
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### الإطار ^

- يبدأ بـ

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ تعني يبدأ بـ
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

- النفي

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ في مجموعة الأحرف تعني النفي، ليس A إلى Z، ليس a إلى z، لا مسافة
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

## 💻 تمارين: اليوم 18

### تمارين: المستوى 1

1. ما هي الكلمة الأكثر تكرارًا في الفقرة التالية؟

```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```sh
    [
    (6, 'love'),
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
    (1, 'If')
    ]
```

2. مواقع بعض الجسيمات على المحور الأفقي x هي -12 و -4 و -3 و -1 في الاتجاه السالب، و 0 عند الأصل، و 4 و 8 في الاتجاه الموجب. استخرج هذه الأرقام من هذا النص الكامل وحساب المسافة بين أبعد جسيمين.

```py
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20
```

### تمارين: المستوى 2

1. اكتب نمطًا يتعرف على ما إذا كان النص متغيرًا صالحًا في بايثون

    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```

### تمارين: المستوى 3

1. نظّف النص التالي. بعد التنظيف، احسب أكثر ثلاث كلمات تكرارًا في النص.

    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```

🎉 مبروك! 🎉

[<< اليوم 17](./17_exception_handling.md) | [اليوم 19 >>](./19_file_handling.md)
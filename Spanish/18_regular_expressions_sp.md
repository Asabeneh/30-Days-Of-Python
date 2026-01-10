# 30 Días de Python: Día 18 - Expresiones regulares

- [Día 18](#-día-18)
  - [Expresiones regulares](#expresiones-regulares)
    - [Módulo *re*](#módulo-re)
    - [Métodos en el módulo *re*](#métodos-en-el-módulo-re)
      - [Match (coincidencia al inicio)](#match-coincidencia-al-inicio)
      - [Search (búsqueda)](#search-búsqueda)
      - [Buscar todas las coincidencias con *findall*](#buscar-todas-las-coincidencias-con-findall)
      - [Reemplazar subcadenas](#reemplazar-subcadenas)
  - [Usar RegEx para dividir el texto](#usar-regex-para-dividir-texto)
  - [Construir patrones RegEx](#construir-patrones-regex)
    - [Corchetes](#corchetes)
    - [Caracteres de escape en RegEx (\\)](#caracteres-de-escape-en-regex)
    - [Una o más veces (+)](#una-o-más-veces-+)
    - [Punto (.)](#punto-)
    - [Cero o más veces (*)](#cero-o-más-veces-)
    - [Cero o una vez (?)](#cero-o-una-vez-?)
    - [Cuantificadores en RegEx](#cuantificadores-en-regex)
    - [Circunflejo (^) en RegEx](#circunflejo-^)
  - [💻 Ejercicios: Día 18](#-ejercicios-día-18)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)
    - [Ejercicios: Nivel 3](#ejercicios-nivel-3)

# 📘 Día 18

## Expresiones regulares

Las expresiones regulares (RegEx) son cadenas de texto especiales que ayudan a encontrar patrones en los datos. RegEx se puede usar para comprobar la existencia de ciertos patrones en diferentes tipos de datos. Para usar RegEx en Python debemos importar el módulo llamado *re*.

### Módulo *re*

Una vez importado el módulo, podemos usarlo para detectar o buscar patrones.

```py
import re
```

### Métodos en el módulo *re*

Para buscar patrones usamos diferentes conjuntos de caracteres y funciones de *re*, que permiten buscar coincidencias dentro de una cadena.

- *re.match()*: busca solo al inicio de la cadena; devuelve un objeto Match si hay coincidencia, sino None.
- *re.search*: busca en cualquier parte de la cadena (incluyendo textos multilínea); devuelve el primer objeto Match encontrado o None.
- *re.findall*: devuelve una lista con todas las coincidencias.
- *re.split*: acepta una cadena y la divide en los puntos donde hay coincidencia, devolviendo una lista.
- *re.sub*: reemplaza una o más coincidencias en una cadena.

#### Match (coincidencia al inicio)

```py
# sintaxis
re.match(substring, string, re.I)
# substring es una cadena o patrón, string es el texto donde buscamos, re.I indica ignorar mayúsculas/minúsculas
```

```py
import re

txt = 'I love to teach python and javaScript'
# Devuelve un objeto Match con span y match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# Podemos usar span para obtener la posición inicial y final como tupla
span = match.span()
print(span)     # (0, 15)
# Tomamos inicio y fin desde span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```

Del ejemplo anterior se ve que el patrón buscado es *I love to teach*. La función match **solo** devuelve un objeto si el texto comienza con ese patrón.

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

Esa cadena no comienza con *I like to teach*, por eso match devuelve None.

#### Search (búsqueda)

```py
# sintaxis
re.search(substring, string, re.I)
# substring es un patrón, string es el texto donde buscamos, re.I es la bandera para ignorar mayúsculas/minúsculas
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Devuelve un objeto Match con span y match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# Podemos usar span para obtener inicio y fin como tupla
span = match.span()
print(span)     # (100, 105)
# Tomamos inicio y fin
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

Como puedes ver, search es más potente que match porque busca en todo el texto. search devuelve la primera coincidencia; para obtener todas las coincidencias usamos findall.

#### Buscar todas las coincidencias con *findall*

*findall()* devuelve todas las coincidencias como una lista.

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Devuelve una lista
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

La palabra *language* aparece dos veces en el texto. Practiquemos más: vamos a buscar 'Python' y 'python' en el texto:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# Devuelve una lista
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']
```

Usando re.I se ignora mayúsculas/minúsculas. Si no usamos la bandera, podemos escribir el patrón de otras formas:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']
```

#### Reemplazar subcadenas

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# o bien
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
```

Otro ejemplo: el siguiente texto es difícil de leer por los símbolos '%'. Reemplazarlos por cadena vacía limpia el texto.

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

## Usar RegEx para dividir el texto

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # dividir usando \n - salto de línea
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## Construir patrones RegEx

Para declarar una cadena usamos comillas simples o dobles. Para declarar un patrón RegEx usamos una cadena raw, escrita como r''.
El siguiente patrón reconoce solo 'apple' en minúsculas; para ignorar mayúsculas/minúsculas reescribimos el patrón o añadimos la bandera re.I.

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# Para ignorar mayúsculas/minúsculas, añadimos la bandera
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# o podemos usar un conjunto de caracteres
regex_pattern = r'[Aa]pple'  # esto permite Apple o apple
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

* []: un conjunto de caracteres
  - [a-c] significa a o b o c
  - [a-z] cualquier letra de a a z
  - [A-Z] cualquier letra de A a Z
  - [0-3] 0 o 1 o 2 o 3
  - [0-9] cualquier dígito del 0 al 9
  - [A-Za-z0-9] cualquier carácter alfanumérico: a-z, A-Z o 0-9

### Corchetes

Practiquemos más con corchetes. Recuerda usar re.I para búsquedas sin distinción entre mayúsculas y minúsculas.

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # Apple o apple o Banana o banana
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

Usando corchetes y alternación:
```py
regex_pattern = r'[a-zA-Z0-9]'  # caracteres a-z, A-Z, 0-9
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['A', 'p', 'p', 'l', 'e', 'a', 'n', 'd', 'b', 'a', 'n', 'a', 'n', 'a', 'a', 'r', 'e',...]

regex_pattern = r'\d'  # \d es un metacarácter que representa dígitos
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

regex_pattern = r'\d+'  # \d+ dígitos uno o más
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Caracteres de escape en RegEx (\\)

```py
regex_pattern = r'\d+'  # \d dígito, + uno o más
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

Para buscar la barra invertida '\' en sí usamos doble backslash:
```py
regex_pattern = r'\\d'  # busca literal '\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # []
```

Si no hay '\d' literal en el texto, no se encuentran coincidencias.

### Una o más veces (+)

```py
regex_pattern = r'\d+'  # \d dígito, + uno o más
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Punto (.)

```py
regex_pattern = r'[a].'  # a seguido de cualquier carácter (excepto nueva línea)
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # a seguido de cualquier carácter una o más veces
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Cero o más veces (*)

Cero o más. Observa con atención el ejemplo.

```py
regex_pattern = r'[a].*'  # a seguido de cualquier carácter cero o más veces
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Cero o una vez (?)

Cero o una vez: puede existir o no.

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? indica cero o una vez
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### Cuantificadores en RegEx

Con llaves podemos especificar la longitud del patrón:
```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactamente 4 dígitos
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1,4}'   # entre 1 y 4 dígitos
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### Circunflejo (^) en RegEx

- Indicar inicio

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ indica que empieza con 'This'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

- Negación dentro de corchetes

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ dentro de [] significa negación: no A-Z, no a-z, no espacio
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8,', '2021']
```

## 💻 Ejercicios: Día 18

### Ejercicios: Nivel 1

1. ¿Qué es una expresión regular?
2. ¿Qué es una variable de expresión regular (regex variable)?
3. Recrea patrones que:
   a) Encuentren citas que contengan la palabra *talent* en un libro,
   b) Encuentren fechas en formato _DD-MM-YYYY_, por ejemplo 12-01-2021,
   c) Encuentren verbos en tiempo -ing en un texto.

### Ejercicios: Nivel 2

1. Escribe un patrón que valide un nombre de variable válido en Python.
2. Limpia el siguiente texto eliminando etiquetas HTML.
```python
text = '''
HTML
Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. It can be assisted by technologies such as Cascading Style Sheets (CSS) and scripting languages such as JavaScript.

Web browsers receive HTML documents from a web server or from local storage and render the documents into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document.

HTML elements are the building blocks of HTML pages. With HTML constructs, images and other objects such as interactive forms may be embedded into the rendered page. HTML provides a means to create structured documents by denoting structural semantics for text such as headings, paragraphs, lists, links, quotes and other items. HTML elements are delineated by tags, written using angle brackets. Tags such as <img /> and <input /> directly introduce content into the page. Other tags such as <p> surround and provide information about document text and may include other tags as sub-elements. Browsers do not display the HTML tags, but use them to interpret the content of the page.

HTML can embed programs written in a scripting language such as JavaScript, which affects the behavior and content of web pages. Inclusion of CSS defines the look and layout of content. The World Wide Web Consortium (W3C), former maintainer of the HTML and current maintainer of the CSS standards, has encouraged the use of CSS over explicit presentational HTML since 1997.
'''
```

### Ejercicios: Nivel 3

1. Limpia el siguiente texto y, tras limpiarlo, calcula las tres palabras más frecuentes:

```python
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''
```

2. El siguiente texto contiene varias direcciones de correo electrónico. Escribe un patrón que encuentre o extraiga las direcciones de email válidas:

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

🎉 ¡Felicidades! 🎉

[<< Día 17](./17_exception_handling_sp.md) | [Día 19 >>](./19_file_handling_sp.md)
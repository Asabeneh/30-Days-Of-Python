<div align="center">
  <h1> 30 Dias de Python: Dia 19 - Manipulação de Arquivos </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Segunda edição: Julho, 2021</small>
</sub>
</div>

[<< Dia 18](./18_regular_expressions_pt.md) | [Dia 20 >>](./20_python_package_manager_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 19](#-dia-19)
  - [Manipulação de Arquivos](#manipulação-de-arquivos)
    - [Abrindo Arquivos para Leitura](#abrindo-arquivos-para-leitura)
    - [Abrindo Arquivos para Escrita e Atualização](#abrindo-arquivos-para-escrita-e-atualização)
    - [Excluindo Arquivos](#excluindo-arquivos)
  - [Tipos de Arquivo](#tipos-de-arquivo)
    - [Arquivo com Extensão txt](#arquivo-com-extensão-txt)
    - [Arquivo com Extensão json](#arquivo-com-extensão-json)
    - [Convertendo JSON em Dicionário](#convertendo-json-em-dicionário)
    - [Convertendo Dicionário em JSON](#convertendo-dicionário-em-json)
    - [Salvando como Arquivo JSON](#salvando-como-arquivo-json)
    - [Arquivo com Extensão csv](#arquivo-com-extensão-csv)
    - [Arquivo com Extensão xlsx](#arquivo-com-extensão-xlsx)
    - [Arquivo com Extensão xml](#arquivo-com-extensão-xml)
  - [💻 Exercícios: Dia 19](#-exercícios-dia-19)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 19

## Manipulação de Arquivos

Até agora vimos diferentes tipos de dados em Python. Geralmente armazenamos nossos dados em diferentes formatos de arquivo. Além de manipular arquivos, veremos também diferentes formatos de arquivo (.txt, .json, .xml, .csv, .tsv, .excel) nesta seção. Primeiro, vamos nos familiarizar com a manipulação de arquivos no formato mais comum (.txt).

A manipulação de arquivos é uma parte importante da programação, que nos permite criar, ler, atualizar e excluir arquivos. Em Python, para manipular dados usamos a função integrada _open()_.

```py
# Sintaxe
open('filename', mode) # mode(r, a, w, x, t,b) pode ser para ler, escrever, atualizar
```

- "r" - Read (Leitura) - Valor padrão. Abre um arquivo para leitura, retorna um erro se o arquivo não existir
- "a" - Append (Anexar) - Abre um arquivo para anexar conteúdo, cria o arquivo se ele não existir
- "w" - Write (Escrita) - Abre um arquivo para escrita, cria o arquivo se ele não existir
- "x" - Create (Criar) - Cria o arquivo especificado, retorna um erro se o arquivo já existir
- "t" - Text (Texto) - Valor padrão. Modo texto
- "b" - Binary (Binário) - Modo binário (por exemplo, imagens)

### Abrindo Arquivos para Leitura

O modo padrão do _open_ é leitura, então não precisamos especificar 'r' ou 'rt'. Eu criei e salvei um arquivo chamado reading_file_example.txt no diretório files. Vamos ver como isso é feito:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

Como você pode ver no exemplo acima, eu imprimi o arquivo aberto e ele forneceu algumas informações sobre ele. Um arquivo aberto possui diferentes métodos de leitura: _read()_, _readline_, _readlines_. Um arquivo aberto precisa ser fechado com o método _close()_.

- _read()_: lê todo o texto como uma string. Se quisermos limitar o número de caracteres que queremos ler, podemos limitar passando um valor int ao método *read(número)*.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# saída
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

Em vez de imprimir todo o texto, vamos imprimir os primeiros 10 caracteres do arquivo de texto.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# saída
<class 'str'>
This is an
```

- _readline()_: lê apenas a primeira linha

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# saída
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: lê todo o texto linha por linha e retorna uma lista de linhas

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# saída
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

Outra forma de obter todas as linhas como uma lista é usando _splitlines()_:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# saída
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

Depois de abrirmos um arquivo, devemos fechá-lo. Há uma grande tendência de esquecer de fechá-los. Existe uma nova forma de abrir arquivos usando _with_ - que fecha os arquivos automaticamente. Vamos reescrever o exemplo anterior com o método _with_:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# saída
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Abrindo Arquivos para Escrita e Atualização

Para escrever em um arquivo existente, devemos adicionar um modo como parâmetro para a função _open()_:

- "a" - append (anexar) - vai anexar ao final do arquivo; se o arquivo não existir, ele cria um novo arquivo.
- "w" - write (escrever) - vai sobrescrever qualquer conteúdo existente; se o arquivo não existir, ele o cria.

Vamos anexar algum texto ao arquivo que temos lido:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

O método abaixo cria um novo arquivo, se o arquivo não existir:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### Excluindo Arquivos

Vimos na seção anterior como criar e remover um diretório usando o módulo _os_. Novamente agora, se quisermos remover um arquivo, usamos o módulo _os_.

```py
import os
os.remove('./files/example.txt')

```

Se o arquivo não existir, o método remove vai lançar um erro, então é uma boa prática usar uma condição como esta:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## Tipos de Arquivo

### Arquivo com Extensão txt

Um arquivo com extensão _txt_ é uma forma muito comum de dado e já cobrimos isso na seção anterior. Vamos passar para o arquivo JSON

### Arquivo com Extensão json

JSON significa JavaScript Object Notation (Notação de Objetos JavaScript). Na verdade, é um objeto JavaScript ou dicionário Python transformado em string.

_Exemplo:_

```py
# dicionário
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: uma string formada a partir de um dicionário
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# usamos três aspas e transformamos em múltiplas linhas para torná-lo mais legível
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### Convertendo JSON em Dicionário

Para converter um JSON em um dicionário, primeiro importamos o módulo json e depois usamos o método _loads_.

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# vamos converter o JSON em dicionário
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# saída
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### Convertendo Dicionário em JSON

Para converter um dicionário em um JSON usamos o método _dumps_ do módulo json.

```py
import json
# dicionário python
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# vamos convertê-lo em json
person_json = json.dumps(person, indent=4) # o indent pode ser 2, 4, 8. Ele deixa o json mais bonito e legível
print(type(person_json))
print(person_json)
```

```sh
# saída
# quando você imprime, ele não tem as aspas, mas na verdade é uma string
# JSON não tem um tipo próprio, é do tipo string.
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

### Salvando como Arquivo JSON

Também podemos salvar nossos dados como um arquivo json. Vamos salvá-lo como um arquivo json seguindo os passos a seguir. Para escrever um arquivo json, usamos o método json.dump(), que pode receber um dicionário, arquivo de saída, ensure_ascii e indent.

```py
import json
# dicionário python
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

No código acima, usamos codificação (encoding) e indentação. A indentação torna o arquivo json fácil de ler.

### Arquivo com Extensão csv

CSV significa comma separated values (valores separados por vírgula). CSV é um formato de arquivo simples usado para armazenar dados tabulares, como uma planilha ou banco de dados. CSV é um formato de dados muito comum em ciência de dados.

**Exemplo:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**Exemplo:**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # usamos o método reader para ler o csv
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
# saída:
Column names are :name, country, city, skills
Number of lines:  1
        Asabeneh is a teacher. He lives in Finland, Helsinki.
Number of lines:  2
```

### Arquivo com Extensão xlsx

Para ler arquivos excel precisamos instalar o pacote _xlrd_. Vamos abordar isso depois de cobrirmos a instalação de pacotes usando pip.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### Arquivo com Extensão xml

XML é outro formato de dados estruturado que se parece com HTML. Em XML as tags não são predefinidas. A primeira linha é uma declaração XML. A tag person é a raiz do XML. O person tem um atributo gender.
**Exemplo: XML**

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

Para mais informações sobre como ler um arquivo XML, consulte a [documentação](https://docs.python.org/2/library/xml.etree.elementtree.html)

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
# saída
Root tag: person
Attribute: {'gender': 'male'}
field: name
field: country
field: city
field: skills
```

🌕 Você está fazendo um grande progresso. Mantenha seu ritmo, continue com o bom trabalho. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 19

### Exercícios: Nível 1

1. Escreva uma função que conte o número de linhas e o número de palavras em um texto. Todos os arquivos estão na pasta data:
   1) Leia o arquivo obama_speech.txt e conte o número de linhas e palavras
   2) Leia o arquivo michelle_obama_speech.txt e conte o número de linhas e palavras
   3) Leia o arquivo donald_speech.txt e conte o número de linhas e palavras
   4) Leia o arquivo melina_trump_speech.txt e conte o número de linhas e palavras
2. Leia o arquivo de dados countries_data.json no diretório data e crie uma função que encontre as dez línguas mais faladas

   ```py
   # Sua saída deve ser parecida com esta
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

   # Sua saída deve ser parecida com esta
   print(most_spoken_languages(filename='./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. Leia o arquivo de dados countries_data.json no diretório data e crie uma função que crie uma lista dos dez países mais populosos

   ```py
   # Sua saída deve ser parecida com esta
   print(most_populated_countries(filename='./data/countries_data.json', 10))

   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000},
   {'country': 'Indonesia', 'population': 258705000},
   {'country': 'Brazil', 'population': 206135893},
   {'country': 'Pakistan', 'population': 194125062},
   {'country': 'Nigeria', 'population': 186988000},
   {'country': 'Bangladesh', 'population': 161006790},
   {'country': 'Russian Federation', 'population': 146599183},
   {'country': 'Japan', 'population': 126960000}
   ]

   # Sua saída deve ser parecida com esta

   print(most_populated_countries(filename='./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

### Exercícios: Nível 2

1. Extraia todos os endereços de email recebidos como uma lista a partir do arquivo email_exchange_big.txt.
2. Encontre as palavras mais comuns na língua inglesa. Chame sua função de find_most_common_words; ela receberá dois parâmetros - uma string ou um arquivo e um número inteiro positivo, indicando o número de palavras. Sua função vai retornar um array de tuplas em ordem decrescente. Verifique a saída

```py
    # Sua saída deve ser parecida com esta
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

    # Sua saída deve ser parecida com esta
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. Use a função find_most_frequent_words para encontrar:
   1) As dez palavras mais frequentes usadas no [discurso de Obama](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   2) As dez palavras mais frequentes usadas no [discurso de Michelle](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   3) As dez palavras mais frequentes usadas no [discurso de Trump](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   4) As dez palavras mais frequentes usadas no [discurso de Melina](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
4. Escreva uma aplicação python que verifique a similaridade entre dois textos. Ela recebe um arquivo ou uma string como parâmetro e vai avaliar a similaridade dos dois textos. Por exemplo, verifique a similaridade entre as transcrições do discurso de [Michelle](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) e de [Melina](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt). Você pode precisar de algumas funções, uma função para limpar o texto (clean_text), uma função para remover palavras de apoio (remove_support_words) e finalmente para verificar a similaridade (check_text_similarity). A lista de [stop words](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) está no diretório data
5. Encontre as 10 palavras mais repetidas em romeo_and_juliet.txt
6. Leia o arquivo [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) e descubra:
   1) Conte o número de linhas contendo python ou Python
   2) Conte o número de linhas contendo JavaScript, javascript ou Javascript
   3) Conte o número de linhas contendo Java e não JavaScript

🎉 PARABÉNS ! 🎉

[<< Dia 18](./18_regular_expressions_pt.md) | [Dia 20 >>](./20_python_package_manager_pt.md)

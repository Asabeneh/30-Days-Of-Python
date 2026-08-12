<div align="center">
  <h1> 30 Dias de Python: Dia 15 - Tipos de Erros em Python </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>Autor:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> Segunda edição: Julho, 2021</small>
  </sub>

</div>

[<< Dia 14](./14_higher_order_functions_pt.md) | [Dia 16 >>](./16_python_datetime_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Dia 15](#-dia-15)
  - [Tipos de Erros em Python](#tipos-de-erros-em-python)
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexerror)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)
  - [💻 Exercícios: Dia 15](#-exercícios-dia-15)

# 📘 Dia 15

## Tipos de Erros em Python

Quando escrevemos código, é comum cometermos um erro de digitação ou algum outro erro comum. Se nosso código falhar ao executar, o interpretador Python exibirá uma mensagem, contendo feedback com informações sobre onde o problema ocorre e o tipo de erro. Às vezes ele também nos dá sugestões de uma possível correção. Entender os diferentes tipos de erros nas linguagens de programação vai nos ajudar a depurar nosso código rapidamente e também vai nos tornar melhores no que fazemos.

Vamos ver os tipos de erro mais comuns, um por um. Primeiro, vamos abrir nosso shell interativo do Python. Vá até o terminal do seu computador e escreva 'python'. O shell interativo do Python será aberto.

### SyntaxError

**Exemplo 1: SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

Como você pode ver, cometemos um erro de sintaxe porque esquecemos de colocar a string entre parênteses e o Python já sugere a solução. Vamos corrigi-lo.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

O erro foi um _SyntaxError_. Depois da correção, nosso código foi executado sem problemas. Vamos ver mais tipos de erro.

### NameError

**Exemplo 1: NameError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

Como você pode ver na mensagem acima, o nome age não está definido. Sim, é verdade que não definimos uma variável age, mas estávamos tentando imprimi-la como se já a tivéssemos declarado. Agora, vamos corrigir isso declarando-a e atribuindo um valor.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

O tipo de erro foi um _NameError_. Nós depuramos o erro definindo o nome da variável.

### IndexError

**Exemplo 1: IndexError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

No exemplo acima, o Python levantou um _IndexError_, porque a lista só tem índices de 0 a 4, então estava fora do intervalo.

### ModuleNotFoundError

**Exemplo 1: ModuleNotFoundError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

No exemplo acima, adicionei um s extra a math de propósito e o _ModuleNotFoundError_ foi levantado. Vamos corrigi-lo removendo o s extra de math.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

Corrigimos, então vamos usar algumas das funções do módulo math.

### AttributeError

**Exemplo 1: AttributeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

Como você pode ver, cometi um erro de novo! Em vez de pi, tentei chamar uma constante PI do módulo maths. Isso levantou um erro de atributo, ou seja, o atributo não existe no módulo. Vamos corrigi-lo mudando de PI para pi.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

Agora, quando chamamos pi do módulo math, obtivemos o resultado.

### KeyError

**Exemplo 1: KeyError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

Como você pode ver, houve um erro de digitação na chave usada para obter o valor do dicionário. Então, isso é um erro de chave e a correção é bem direta. Vamos fazer isso!

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

Depuramos o erro, nosso código foi executado e obtivemos o valor.

### TypeError

**Exemplo 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

No exemplo acima, um TypeError é levantado porque não podemos somar um número a uma string. A primeira solução seria converter a string em int ou float. Outra solução seria converter o número em uma string (o resultado então seria '43'). Vamos seguir a primeira correção.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

Erro removido e obtivemos o resultado que esperávamos.

### ImportError

**Exemplo 1: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

Não existe uma função chamada power no módulo math, ela tem um nome diferente: _pow_. Vamos corrigir:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### ValueError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

Neste caso não podemos converter a string fornecida em um número, por causa da letra 'a' presente nela.

### ZeroDivisionError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

Não podemos dividir um número por zero.

Cobrimos alguns dos tipos de erro do Python; se você quiser saber mais sobre isso, consulte a documentação do Python sobre tipos de erro em Python.
Se você for bom em ler os tipos de erro, então conseguirá corrigir seus bugs rapidamente e também se tornará um programador melhor.

🌕 Você está se destacando. Você chegou à metade do caminho para a grandeza. Agora faça alguns exercícios para o cérebro e para os músculos.

## 💻 Exercícios: Dia 15

1. Abra seu shell interativo do Python e tente todos os exemplos abordados nesta seção.

🎉 PARABÉNS ! 🎉

[<< Dia 14](./14_higher_order_functions_pt.md) | [Dia 16 >>](./16_python_datetime_pt.md)

<div align="center">
  <h1> 30 Dias de Python: Dia 14 - Funções de Ordem Superior</h1>
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

[<< Dia 13](./13_list_comprehension_pt.md) | [Dia 15 >>](./15_python_type_errors_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 Dia 14](#-dia-14)
  - [Funções de Ordem Superior](#funções-de-ordem-superior)
    - [Função como Parâmetro](#função-como-parâmetro)
    - [Função como Valor de Retorno](#função-como-valor-de-retorno)
  - [Closures em Python](#closures-em-python)
  - [Decoradores em Python](#decoradores-em-python)
    - [Criando Decoradores](#criando-decoradores)
    - [Aplicando Múltiplos Decoradores a uma Única Função](#aplicando-múltiplos-decoradores-a-uma-única-função)
    - [Aceitando Parâmetros em Funções Decoradoras](#aceitando-parâmetros-em-funções-decoradoras)
  - [Funções de Ordem Superior Integradas](#funções-de-ordem-superior-integradas)
    - [Python - Função Map](#python---função-map)
    - [Python - Função Filter](#python---função-filter)
    - [Python - Função Reduce](#python---função-reduce)
  - [💻 Exercícios: Dia 14](#-exercícios-dia-14)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 14

## Funções de Ordem Superior

Em Python, as funções são tratadas como cidadãs de primeira classe, o que permite realizar as seguintes operações com funções:

- Uma função pode receber uma ou mais funções como parâmetros
- Uma função pode ser retornada como resultado de outra função
- Uma função pode ser modificada
- Uma função pode ser atribuída a uma variável

Nesta seção, vamos abordar:

1. Lidar com funções como parâmetros
2. Retornar funções como valor de retorno de outras funções
3. Usar closures e decoradores em Python

### Função como Parâmetro

```py
def sum_numbers(nums):  # função normal
    return sum(nums)    # uma função triste abusando da função integrada sum :<

def higher_order_function(f, lst):  # função como parâmetro
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### Função como Valor de Retorno

```py
def square(x):          # uma função de quadrado
    return x ** 2

def cube(x):            # uma função de cubo
    return x ** 3

def absolute(x):        # uma função de valor absoluto
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # uma função de ordem superior retornando uma função
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

Você pode ver a partir do exemplo acima que a função de ordem superior está retornando funções diferentes dependendo do parâmetro passado

## Closures em Python

Python permite que uma função aninhada acesse o escopo externo da função que a envolve. Isso é conhecido como Closure. Vamos dar uma olhada em como as closures funcionam em Python. Em Python, uma closure é criada aninhando uma função dentro de outra função encapsuladora e depois retornando a função interna. Veja o exemplo abaixo.

**Exemplo:**

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Decoradores em Python

Um decorador é um padrão de projeto em Python que permite a um usuário adicionar nova funcionalidade a um objeto existente sem modificar sua estrutura. Os decoradores geralmente são chamados antes da definição de uma função que você deseja decorar.

### Criando Decoradores

Para criar uma função decoradora, precisamos de uma função externa com uma função wrapper interna.

**Exemplo:**

```py
# Função normal
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Vamos implementar o exemplo acima com um decorador

'''Esta função decoradora é uma função de ordem superior
que recebe uma função como parâmetro'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

```

### Aplicando Múltiplos Decoradores a uma Única Função

```py

'''Estas funções decoradoras são funções de ordem superior
que recebem funções como parâmetros'''

# Primeiro decorador
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Segundo decorador
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

# Os decoradores serão executados de baixo para cima
@split_string_decorator
@uppercase_decorator     # a ordem dos decoradores é importante neste caso - a função .upper() não funciona com listas
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### Aceitando Parâmetros em Funções Decoradoras

Na maioria das vezes precisamos que nossas funções recebam parâmetros, então podemos precisar definir um decorador que aceite parâmetros.

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## Funções de Ordem Superior Integradas

Algumas das funções de ordem superior integradas que abordamos nesta parte são _map()_, _filter_ e _reduce_.
Uma função lambda pode ser passada como parâmetro e o melhor caso de uso de funções lambda é em funções como map, filter e reduce.

### Python - Função Map

A função map() é uma função integrada que recebe uma função e um iterável como parâmetros.

```py
    # sintaxe
    map(function, iterable)
```

**Exemplo:1**

```py
numbers = [1, 2, 3, 4, 5] # iterável
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Vamos aplicar com uma função lambda
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**Exemplo:2**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterável
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**Exemplo:3**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterável

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Vamos aplicar com uma função lambda
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

O que a map realmente faz é iterar sobre uma lista. Por exemplo, ela transforma os nomes em maiúsculas e retorna uma nova lista.

### Python - Função Filter

A função filter() chama a função especificada, que retorna um booleano para cada item do iterável (lista) especificado. Ela filtra os itens que satisfazem o critério de filtragem.

```py
    # sintaxe
    filter(function, iterable)
```

**Exemplo:1**

```py
# Vamos filtrar apenas números pares
numbers = [1, 2, 3, 4, 5]  # iterável

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**Exemplo:2**

```py
numbers = [1, 2, 3, 4, 5]  # iterável

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# Filtrar nomes longos
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterável
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### Python - Função Reduce

A função _reduce()_ é definida no módulo functools e devemos importá-la desse módulo. Assim como map e filter, ela recebe dois parâmetros, uma função e um iterável. No entanto, ela não retorna outro iterável, e sim um único valor.
**Exemplo:1**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterável
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Exercícios: Dia 14

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Exercícios: Nível 1

1. Explique a diferença entre map, filter e reduce.
2. Explique a diferença entre função de ordem superior, closure e decorador
3. Defina uma função de chamada antes de map, filter ou reduce, veja os exemplos.
4. Use for para imprimir cada país na lista countries.
5. Use for para imprimir cada nome na lista names.
6. Use for para imprimir cada número na lista numbers.

### Exercícios: Nível 2

1. Use map para criar uma nova lista transformando cada país em maiúsculas na lista countries
1. Use map para criar uma nova lista transformando cada número em seu quadrado na lista numbers
1. Use map para transformar cada nome em maiúsculas na lista names
1. Use filter para filtrar países que contenham 'land'.
1. Use filter para filtrar países que tenham exatamente seis caracteres.
1. Use filter para filtrar países que contenham seis letras ou mais na lista de países.
1. Use filter para filtrar países que comecem com 'E'
1. Encadeie dois ou mais iteradores de lista (ex.: arr.map(callback).filter(callback).reduce(callback))
1. Declare uma função chamada get_string_lists que recebe uma lista como parâmetro e retorna uma lista contendo apenas os itens do tipo string.
1. Use reduce para somar todos os números na lista numbers.
1. Use reduce para concatenar todos os países e produzir esta frase: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
1. Declare uma função chamada categorize_countries que retorna uma lista de países com algum padrão em comum (você pode encontrar a [lista de países](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) neste repositório como countries.js (ex: 'land', 'ia', 'island', 'stan')).
1. Crie uma função que retorne um dicionário, onde as chaves representam as letras iniciais dos países e os valores são o número de nomes de países que começam com aquela letra.
2. Declare uma função get_first_ten_countries - ela retorna uma lista dos primeiros dez países da lista countries.js na pasta data.
1. Declare uma função get_last_ten_countries que retorna os últimos dez países na lista countries.

### Exercícios: Nível 3

1. Use o arquivo countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) e siga as tarefas abaixo:
   - Ordene os países por nome, por capital, por população
   - Filtre as dez línguas mais faladas por localização.
   - Filtre os dez países mais populosos.

🎉 PARABÉNS ! 🎉

[<< Dia 13](./13_list_comprehension_pt.md) | [Dia 15 >>](./15_python_type_errors_pt.md)

<div align="center">
  <h1> 30 Dias de Python: Dia 11 - Funções</h1>
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

[<< Dia 10](./10_loops_pt.md) | [Dia 12 >>](./12_modules_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 11](#-dia-11)
  - [Funções](#funções)
    - [Definindo uma Função](#definindo-uma-função)
    - [Declarando e Chamando uma Função](#declarando-e-chamando-uma-função)
    - [Função sem Parâmetros](#função-sem-parâmetros)
    - [Função Retornando um Valor - Parte 1](#função-retornando-um-valor---parte-1)
    - [Função com Parâmetros](#função-com-parâmetros)
    - [Passando Argumentos com Chave e Valor](#passando-argumentos-com-chave-e-valor)
    - [Função Retornando um Valor - Parte 2](#função-retornando-um-valor---parte-2)
    - [Função com Parâmetros Padrão](#função-com-parâmetros-padrão)
    - [Número Arbitrário de Argumentos](#número-arbitrário-de-argumentos)
    - [Número Padrão e Arbitrário de Parâmetros em Funções](#número-padrão-e-arbitrário-de-parâmetros-em-funções)
    - [Desempacotamento de Dicionário](#desempacotamento-de-dicionário)
    - [Número Arbitrário de Argumentos Nomeados](#número-arbitrário-de-argumentos-nomeados)
    - [Função como Parâmetro de Outra Função](#função-como-parâmetro-de-outra-função)
  - [Depoimento](#depoimento)
  - [💻 Exercícios: Dia 11](#-exercícios-dia-11)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 11

## Funções

Até agora vimos muitas funções integradas do Python. Nesta seção, vamos focar nas funções personalizadas. O que é uma função? Antes de começarmos a criar funções, vamos aprender o que é uma função e por que precisamos delas?

### Definindo uma Função

Uma função é um bloco de código reutilizável ou um conjunto de instruções de programação projetado para realizar uma determinada tarefa. Para definir ou declarar uma função, o Python fornece a palavra-chave _def_. A seguir está a sintaxe para definir uma função. O bloco de código da função só é executado se a função for chamada ou invocada.

### Declarando e Chamando uma Função

Quando criamos uma função, chamamos isso de declarar uma função. Quando começamos a usá-la, chamamos isso de _chamar_ ou _invocar_ uma função. As funções podem ser declaradas com ou sem parâmetros.

```py
# sintaxe
# Declarando uma função
def nome_da_funcao():
    codigos
    codigos
# Chamando uma função
nome_da_funcao()
```

### Função sem Parâmetros

Uma função pode ser declarada sem parâmetros.

**Exemplo:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # chamando a função

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Função Retornando um Valor - Parte 1

Funções retornam valores usando a instrução _return_. Se uma função não tiver uma instrução return, ela retorna None. Vamos reescrever as funções acima usando return. A partir de agora, obtemos um valor de uma função quando a chamamos e o imprimimos.

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Função com Parâmetros

Em uma função podemos passar diferentes tipos de dados (número, string, booleano, lista, tupla, dicionário ou conjunto) como parâmetros.

- Parâmetro único: Se nossa função recebe um parâmetro, devemos chamar nossa função com um argumento

```py
  # sintaxe
  # Declarando uma função
  def nome_da_funcao(parametro):
    codigos
    codigos
  # Chamando a função
  print(nome_da_funcao(argumento))
```

**Exemplo:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Dois parâmetros: Uma função pode ter ou não ter um ou mais parâmetros. Uma função também pode ter dois ou mais parâmetros. Se nossa função recebe parâmetros, devemos chamá-la com argumentos. Vamos verificar uma função com dois parâmetros:

```py
  # sintaxe
  # Declarando uma função
  def nome_da_funcao(para1, para2):
    codigos
    codigos
  # Chamando a função
  print(nome_da_funcao(arg1, arg2))
```

**Exemplo:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # o valor precisa ser convertido para string primeiro
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Passando Argumentos com Chave e Valor

Se passarmos os argumentos com chave e valor, a ordem dos argumentos não importa.

```py
# sintaxe
# Declarando uma função
def nome_da_funcao(para1, para2):
    codigos
    codigos
# Chamando a função
print(nome_da_funcao(para1 = 'John', para2 = 'Doe')) # a ordem dos argumentos não importa aqui
```

**Exemplo:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # A ordem não importa
```

### Função Retornando um Valor - Parte 2

Se não retornarmos um valor com uma função, então nossa função retorna _None_ por padrão. Para retornar um valor com uma função, usamos a palavra-chave _return_ seguida da variável que estamos retornando. Podemos retornar qualquer tipo de dado de uma função.

- Retornando uma string:
**Exemplo:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- Retornando um número:

**Exemplo:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))
```

- Retornando um booleano:
  **Exemplo:**

```py
def is_even (n):
    if n % 2 == 0:
        return True    # return interrompe a execução da função, semelhante ao break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Retornando uma lista:
  **Exemplo:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Função com Parâmetros Padrão

Às vezes passamos valores padrão para os parâmetros, quando invocamos a função. Se não passarmos argumentos ao chamar a função, seus valores padrão serão usados.

```py
# sintaxe
# Declarando uma função
def nome_da_funcao(param = valor):
    codigos
    codigos
# Chamando a função
nome_da_funcao()
nome_da_funcao(arg)
```

**Exemplo:**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age 
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # o valor precisa ser convertido para string primeiro
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - gravidade média na superfície da Terra
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravidade na superfície da Lua
```

### Número Arbitrário de Argumentos

Se não sabemos o número de argumentos que vamos passar para nossa função, podemos criar uma função que pode receber um número arbitrário de argumentos, adicionando \* antes do nome do parâmetro.

```py
# sintaxe
# Declarando uma função
def nome_da_funcao(*args):
    codigos
    codigos
# Chamando a função
nome_da_funcao(param1, param2, param3,..)
```

**Exemplo:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # o mesmo que total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### Número Padrão e Arbitrário de Parâmetros em Funções

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i) 
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

### Desempacotamento de Dicionário

Você pode chamar uma função que tem argumentos nomeados usando um dicionário com nomes de chave correspondentes. Você faz isso usando ``**``.

```py
# Define uma função que recebe dois argumentos: 'name' e 'location'
def greet(name, location):
    # Imprime uma mensagem de saudação usando os argumentos fornecidos
    print("Hi there", name, "how is the weather in", location)

# Chama a função usando argumentos nomeados
greet(name="Alice", location="New York")  
# Saída: Hi there Alice how is the weather in New York

# Cria um dicionário com chaves correspondentes aos nomes dos parâmetros da função
my_dict = {"name": "Alice", "location": "New York"}

# Chama a função usando desempacotamento de dicionário
greet(**my_dict)  
# O operador ** desempacota o dicionário, passando seus pares chave-valor
# como argumentos nomeados para a função.
# Saída: Hi there Alice how is the weather in New York
```

### Número Arbitrário de Argumentos Nomeados

Você também pode definir uma função para aceitar um número arbitrário de argumentos nomeados.

```py
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
```

Em geral, evite isso a menos que seja necessário, pois torna mais difícil entender o que a função aceita e faz.

### Função como Parâmetro de Outra Função

```py
# Você pode passar funções como parâmetros
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 Você conquistou muito até agora. Continue! Você acabou de completar os desafios do dia 11 e está onze passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## Depoimento

Agora é hora de expressar seus pensamentos sobre o Autor e o 30DaysOfPython. Você pode deixar seu depoimento neste [link](https://testimonial-s3sw.onrender.com/)

## 💻 Exercícios: Dia 11

### Exercícios: Nível 1

1. Declare uma função _add_two_numbers_. Ela recebe dois parâmetros e retorna uma soma.
2. A área de um círculo é calculada da seguinte forma: area = π x r x r. Escreva uma função que calcule _area_of_circle_.
3. Escreva uma função chamada add_all_nums que recebe um número arbitrário de argumentos e soma todos os argumentos. Verifique se todos os itens da lista são do tipo número. Caso contrário, dê um retorno razoável.
4. A temperatura em °C pode ser convertida para °F usando esta fórmula: °F = (°C x 9/5) + 32. Escreva uma função que converta °C para °F, _convert_celsius_to-fahrenheit_.
5. Escreva uma função chamada check-season, que recebe um parâmetro de mês e retorna a estação: Outono, Inverno, Primavera ou Verão.
6. Escreva uma função chamada calculate_slope que retorna a inclinação de uma equação linear
7. A equação quadrática é calculada da seguinte forma: ax² + bx + c = 0. Escreva uma função que calcule o conjunto solução de uma equação quadrática, _solve_quadratic_eqn_.
8. Declare uma função chamada print_list. Ela recebe uma lista como parâmetro e imprime cada elemento da lista.
9. Declare uma função chamada reverse_list. Ela recebe um array como parâmetro e retorna o array invertido (use loops).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) 
# ["C", "B", "A"]
```

10. Declare uma função chamada capitalize_list_items. Ela recebe uma lista como parâmetro e retorna uma lista de itens capitalizados
11. Declare uma função chamada add_item. Ela recebe uma lista e um parâmetro item. Ela retorna uma lista com o item adicionado ao final.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

12. Declare uma função chamada remove_item. Ela recebe uma lista e um parâmetro item. Ela retorna uma lista com o item removido.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

13. Declare uma função chamada sum_of_numbers. Ela recebe um parâmetro número e soma todos os números naquele intervalo.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

14. Declare uma função chamada sum_of_odds. Ela recebe um parâmetro número e soma todos os números ímpares naquele intervalo.
15. Declare uma função chamada sum_of_even. Ela recebe um parâmetro número e soma todos os números pares naquele intervalo.

### Exercícios: Nível 2

1. Declare uma função chamada evens_and_odds. Ela recebe um número inteiro positivo como parâmetro e conta o número de números pares e ímpares no número.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

1. Chame sua função factorial, ela recebe um número inteiro como parâmetro e retorna o fatorial do número
1. Chame sua função _is_empty_, ela recebe um parâmetro e verifica se ele está vazio ou não
1. Escreva diferentes funções que recebem listas. Elas devem calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (desvio padrão).
1. Escreva uma função chamada _greet_ que recebe um argumento padrão, _name_. Se nenhum argumento for fornecido, ela deve imprimir "Hello, Guest!", caso contrário deve saudar a pessoa pelo nome.

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```
1. Crie uma função chamada _show_args_ para receber um número arbitrário de argumentos nomeados e imprimir seus nomes e valores.
   ```py
   show_args(name="Alice", age=30, city="New York")
   # Received: name: Alice, age: 30, city: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # Received: name: Bob, pet: Fluffy, the bunny
   ```


### Exercícios: Nível 3

1. Escreva uma função chamada is_prime, que verifica se um número é primo.
1. Escreva uma função que verifica se todos os itens são únicos na lista.
1. Escreva uma função que verifica se todos os itens da lista são do mesmo tipo de dado.
1. Escreva uma função que verifica se a variável fornecida é uma variável Python válida
1. Vá até a pasta data e acesse o arquivo countries-data.py.

- Crie uma função chamada most_spoken_languages no mundo. Ela deve retornar as 10 ou 20 línguas mais faladas no mundo em ordem decrescente
- Crie uma função chamada most_populated_countries. Ela deve retornar os 10 ou 20 países mais populosos em ordem decrescente.

🎉 PARABÉNS ! 🎉

[<< Dia 10](./10_loops_pt.md) | [Dia 12 >>](./12_modules_pt.md)

<div align="center">
  <h1> 30 Dias de Python: Dia 13 - List Comprehension</h1>
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

[<< Dia 12](./12_modules_pt.md) | [Dia 14 >>](./14_higher_order_functions_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 13](#-dia-13)
  - [List Comprehension](#list-comprehension)
  - [Função Lambda](#função-lambda)
    - [Criando uma Função Lambda](#criando-uma-função-lambda)
    - [Função Lambda Dentro de Outra Função](#função-lambda-dentro-de-outra-função)
  - [💻 Exercícios: Dia 13](#-exercícios-dia-13)

# 📘 Dia 13

## List Comprehension

List comprehension em Python é uma forma compacta de criar uma lista a partir de uma sequência. É uma forma curta de criar uma nova lista. List comprehension é consideravelmente mais rápida do que processar uma lista usando o loop _for_.

```py
# sintaxe
[expressão for i in iterável if condição]
```

**Exemplo:1**

Por exemplo, se você quiser transformar uma string em uma lista de caracteres. Você pode usar alguns métodos. Vamos ver alguns deles:

```py
# Uma forma
language = 'Python'
lst = list(language) # transformando a string em lista
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Segunda forma: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

```

**Exemplo:2**

Por exemplo, se você quiser gerar uma lista de números

```py
# Gerando números
numbers = [i for i in range(11)]  # para gerar números de 0 a 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# É possível fazer operações matemáticas durante a iteração
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Também é possível fazer uma lista de tuplas
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

```

**Exemplo:2**

List comprehension pode ser combinada com a expressão if

```py
# Gerando números pares
even_numbers = [i for i in range(21) if i % 2 == 0]  # para gerar uma lista de números pares no intervalo de 0 a 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Gerando números ímpares
odd_numbers = [i for i in range(21) if i % 2 != 0]  # para gerar números ímpares no intervalo de 0 a 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filtrar números: vamos filtrar apenas os números pares positivos da lista abaixo
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Achatando um array bidimensional
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Função Lambda

Função lambda é uma pequena função anônima sem nome. Ela pode receber qualquer número de argumentos, mas só pode ter uma expressão. A função lambda é semelhante às funções anônimas em JavaScript. Precisamos dela quando queremos escrever uma função anônima dentro de outra função.

### Criando uma Função Lambda

Para criar uma função lambda usamos a palavra-chave _lambda_ seguida de um ou mais parâmetros, seguida de uma expressão. Veja a sintaxe e o exemplo abaixo. A função lambda não usa return, mas retorna explicitamente a expressão.

```py
# sintaxe
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

**Exemplo:**

```py
# Função nomeada
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Vamos transformar a função acima em uma função lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Função lambda autoinvocada
(lambda a, b: a + b)(2,3) # 5 - precisa encapsular em print() para ver o resultado no console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Múltiplas variáveis
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### Função Lambda Dentro de Outra Função

Usando uma função lambda dentro de outra função.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # a função power agora precisa de 2 argumentos para funcionar, em parênteses separados
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

🌕 Continue com o bom trabalho. Mantenha o ritmo, o céu é o limite! Você acabou de completar os desafios do dia 13 e está treze passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 13

1. Filtre apenas os números negativos e zero na lista usando list comprehension
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
2. Achate a seguinte lista de listas de listas em uma lista unidimensional:

   ```py
   list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   saída
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

3. Usando list comprehension, crie a seguinte lista de tuplas:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
4. Achate a seguinte lista em uma nova lista:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   saída:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
5. Transforme a seguinte lista em uma lista de dicionários:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   saída:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
6. Transforme a seguinte lista de listas em uma lista de strings concatenadas:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   saída
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
7. Escreva uma função lambda que possa resolver a inclinação ou o intercepto y de funções lineares.

🎉 PARABÉNS ! 🎉

[<< Dia 12](./12_modules_pt.md) | [Dia 14 >>](./14_higher_order_functions_pt.md)

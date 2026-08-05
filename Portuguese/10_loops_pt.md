<div align="center">
  <h1> 30 Dias de Python: Dia 10 - Loops</h1>
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

[<< Dia 9](./09_conditionals_pt.md) | [Dia 11 >>](./11_functions_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 10](#-dia-10)
  - [Loops](#loops)
    - [Loop While](#loop-while)
    - [Break e Continue - Parte 1](#break-e-continue---parte-1)
    - [Loop For](#loop-for)
    - [Break e Continue - Parte 2](#break-e-continue---parte-2)
    - [A Função Range](#a-função-range)
    - [Loop For Aninhado](#loop-for-aninhado)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [💻 Exercícios: Dia 10](#-exercícios-dia-10)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 10

## Loops

A vida é repleta de rotinas. Na programação também fazemos muitas tarefas repetitivas. Para lidar com tarefas repetitivas, as linguagens de programação usam loops. A linguagem de programação Python também oferece os seguintes dois tipos de loop:

1. loop while
2. loop for

### Loop While

Usamos a palavra reservada _while_ para criar um loop while. Ele é usado para executar um bloco de instruções repetidamente até que uma determinada condição seja satisfeita. Quando a condição se torna falsa, as linhas de código após o loop continuarão a ser executadas.

```py
  # sintaxe
while condition:
    code goes here
```

**Exemplo:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#imprime de 0 a 4
```

No loop while acima, a condição se torna falsa quando count é 5. É nesse momento que o loop para.
Se estivermos interessados em executar um bloco de código uma vez que a condição não seja mais verdadeira, podemos usar _else_.

```py
  # sintaxe
while condition:
    code goes here
else:
    code goes here
```

**Exemplo:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

A condição do loop acima será falsa quando count for 5 e o loop parar, e a execução começará a instrução else. Como resultado, 5 será impresso.

### Break e Continue - Parte 1

- Break: Usamos break quando queremos sair ou parar o loop.

```py
# sintaxe
while condition:
    code goes here
    if another_condition:
        break
```

**Exemplo:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

O loop while acima imprime apenas 0, 1, 2, mas quando chega a 3, ele para.

- Continue: Com a instrução continue podemos pular a iteração atual e continuar com a próxima:

```py
  # sintaxe
while condition:
    code goes here
    if another_condition:
        continue
```

**Exemplo:**

```py
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1
```

O loop while acima imprime apenas 0, 1, 2 e 4 (pula o 3).

### Loop For

A palavra-chave _for_ é usada para criar um loop for, de forma semelhante a outras linguagens de programação, mas com algumas diferenças de sintaxe. O loop é usado para iterar sobre uma sequência (que pode ser uma lista, uma tupla, um dicionário, um conjunto ou uma string).

-Usando o loop For em uma lista

```py
# sintaxe
for iterator in lst:
    code goes here
```

**Exemplo:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number é um nome temporário que se refere aos itens da lista, válido apenas dentro deste loop
    print(number)       # os números serão impressos linha por linha, de 0 a 5
```

-Usando o loop For em uma string

```py
# sintaxe
for iterator in string:
    code goes here
```

**Exemplo:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

-Usando o loop For em uma tupla

```py
# sintaxe
for iterator in tpl:
    code goes here
```

**Exemplo:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- Loop for com dicionário
  Percorrer um dicionário com um loop te dá a chave do dicionário.

```py
  # sintaxe
for iterator in dct:
    code goes here
```

**Exemplo:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # desta forma obtemos tanto as chaves quanto os valores impressos
```

-Usando o loop For em um conjunto

```py
# sintaxe
for iterator in st:
    code goes here
```

**Exemplo:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break e Continue - Parte 2

Breve recapitulação:
_Break_: Usamos break quando queremos parar o loop antes que ele seja concluído.

```py
# sintaxe
for iterator in sequence:
    code goes here
    if condition:
        break
```

**Exemplo:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

No exemplo acima, o loop para quando chega a 3.

Continue: Usamos continue quando queremos pular algumas das etapas na iteração do loop.

```py
  # sintaxe
for iterator in sequence:
    code goes here
    if condition:
        continue
```

**Exemplo:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # para condições em forma reduzida, é necessário tanto o if quanto o else
print('outside the loop')
```

No exemplo acima, se o número for igual a 3, a etapa _após_ a condição (mas dentro do loop) é pulada e a execução do loop continua se ainda houver iterações restantes.

### A Função Range

A função _range()_ é usada para retornar uma lista de números. O _range(start, end, step)_ recebe três parâmetros: início, fim e incremento. Por padrão, começa em 0 e o incremento é 1. A sequência range precisa de pelo menos 1 argumento (fim).
Criando sequências usando range

```py
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 argumentos indicam o início e o fim da sequência, o passo é definido como padrão 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# para ir de trás para frente, do início ao fim
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

```py
# sintaxe
for iterator in range(start, end, step):
```

**Exemplo:**

```py
for number in range(11):
    print(number)   # imprime de 0 a 10, sem incluir o 11
```

### Loop For Aninhado

Podemos escrever loops dentro de um loop.

```py
# sintaxe
for x in y:
    for t in x:
        print(t)
```

**Exemplo:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

Se quisermos exibir alguma mensagem quando o loop terminar, usamos else.

```py
# sintaxe
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**Exemplo:**

```py
for number in range(11):
    print(number)   # imprime de 0 a 10, sem incluir o 11
else:
    print('The loop stops at', number)
```

### Pass

Em Python, quando uma instrução é obrigatória (após os dois pontos), mas não queremos executar nenhum código nesse ponto, podemos escrever a palavra _pass_ para evitar erros. Também podemos usá-la como um placeholder, para instruções futuras.

**Exemplo:**

```py
for number in range(6):
    pass
```

🌕 Você estabeleceu um grande marco, você é imparável. Continue assim! Você acabou de completar os desafios do dia 10 e está dez passos à frente no seu caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 10

### Exercícios: Nível 1

1. Percorra de 0 a 10 usando um loop for, faça o mesmo usando um loop while.
2. Percorra de 10 a 0 usando um loop for, faça o mesmo usando um loop while.
3. Escreva um loop que faça sete chamadas a print(), para que obtenhamos na saída o seguinte triângulo:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

4. Use loops aninhados para criar o seguinte:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

5. Imprima o seguinte padrão:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

6. Percorra a lista, ['Python', 'Numpy','Pandas','Django', 'Flask'] usando um loop for e imprima os itens.
7. Use um loop for para percorrer de 0 a 100 e imprima apenas os números pares
8. Use um loop for para percorrer de 0 a 100 e imprima apenas os números ímpares

### Exercícios: Nível 2

1.  Use um loop for para percorrer de 0 a 100 e imprima a soma de todos os números.

```sh
The sum of all numbers is 5050.
```

2. Use um loop for para percorrer de 0 a 100 e imprima a soma de todos os pares e a soma de todos os ímpares.

   ```sh
   The sum of all evens is 2550. And the sum of all odds is 2500.
   ```

### Exercícios: Nível 3

1. Vá até a pasta data e use o arquivo [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py). Percorra os países e extraia todos os países que contêm a palavra _land_.
1. Esta é uma lista de frutas, ['banana', 'orange', 'mango', 'lemon'] inverta a ordem usando um loop.
1. Vá até a pasta data e use o arquivo [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py).
   1. Qual é o número total de idiomas nos dados
   2. Encontre os dez idiomas mais falados nos dados
   3. Encontre os 10 países mais populosos do mundo

🎉 PARABÉNS ! 🎉

[<< Dia 9](./09_conditionals_pt.md) | [Dia 11 >>](./11_functions_pt.md)

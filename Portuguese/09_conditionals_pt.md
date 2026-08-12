<div align="center">
  <h1> 30 Dias de Python: Dia 9 - Condicionais</h1>
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

[<< Dia 8](./08_dictionaries_pt.md) | [Dia 10 >>](./10_loops_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 9](#-dia-9)
  - [Condicionais](#condicionais)
    - [Condição If](#condição-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Forma Reduzida](#forma-reduzida)
    - [Condições Aninhadas](#condições-aninhadas)
    - [Condição If e Operadores Lógicos](#condição-if-e-operadores-lógicos)
    - [Operadores Lógicos And e Or](#operadores-lógicos-and-e-or)
  - [💻 Exercícios: Dia 9](#-exercícios-dia-9)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 9

## Condicionais

Por padrão, as instruções em um script Python são executadas sequencialmente de cima para baixo. Se a lógica de processamento exigir, o fluxo sequencial de execução pode ser alterado de duas maneiras:

- Execução condicional: um bloco de uma ou mais instruções será executado se uma determinada expressão for verdadeira
- Execução repetitiva: um bloco de uma ou mais instruções será executado repetidamente enquanto uma determinada expressão for verdadeira. Nesta seção, vamos abordar as instruções _if_, _else_ e _elif_. Os operadores de comparação e lógicos que aprendemos nas seções anteriores serão úteis aqui.

### Condição If

Em Python e em outras linguagens de programação, a palavra-chave _if_ é usada para verificar se uma condição é verdadeira e executar o bloco de código. Lembre-se da identação após os dois pontos.

```py
# sintaxe
if condition:
    esta parte do código é executada para condições verdadeiras
```

**Exemplo: 1**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

Como você pode ver no exemplo acima, 3 é maior que 0. A condição foi verdadeira e o bloco de código foi executado. No entanto, se a condição for falsa, não veremos o resultado. Para ver o resultado da condição falsa, devemos ter outro bloco, que será o _else_.

### If Else

Se a condição for verdadeira, o primeiro bloco será executado; se não, a condição else será executada.

```py
# sintaxe
if condition:
    esta parte do código é executada para condições verdadeiras
else:
     esta parte do código é executada para condições falsas
```

**Exemplo:**

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

A condição acima é falsa, portanto o bloco else foi executado. E se tivermos mais de duas condições? Podemos usar _elif_.

### If Elif Else

Na nossa vida diária, tomamos decisões todos os dias. Tomamos decisões não verificando apenas uma ou duas condições, mas várias condições. Assim como na vida, a programação também está repleta de condições. Usamos _elif_ quando temos várias condições.

```py
# sintaxe
if condition:
    code
elif condition:
    code
else:
    code

```

**Exemplo:**

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### Forma Reduzida

```py
# sintaxe
code if condition else code
```

**Exemplo:**

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # primeira condição atendida, 'A is positive' será impresso
```

### Condições Aninhadas

Condições podem ser aninhadas

```py
# sintaxe
if condition:
    code
    if condition:
    code
```

**Exemplo:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

```

Podemos evitar escrever condições aninhadas usando o operador lógico _and_.

### Condição If e Operadores Lógicos

```py
# sintaxe
if condition and condition:
    code
```

**Exemplo:**

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

### Operadores Lógicos And e Or

```py
# sintaxe
if condition or condition:
    code
```

**Exemplo:**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

🌕 Você está indo muito bem. Nunca desista, porque grandes coisas levam tempo. Você acabou de completar os desafios do dia 9 e está nove passos à frente no seu caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 9

### Exercícios: Nível 1

1. Obtenha a entrada do usuário usando input("Enter your age: "). Se o usuário tiver 18 anos ou mais, dê o retorno: You are old enough to drive. Se for menor de 18, dê o retorno de quanto tempo falta. Saída:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. Compare os valores de my_age e your_age usando if … else. Quem é mais velho (eu ou você)? Use input("Enter your age: ") para obter a idade como entrada. Você pode usar uma condição aninhada para imprimir 'year' para uma diferença de 1 ano, 'years' para diferenças maiores, e um texto personalizado se my_age = your_age. Saída:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

3. Obtenha dois números do usuário usando o prompt input. Se a for maior que b retorne a is greater than b, se a for menor que b retorne a is smaller than b, senão a is equal to b. Saída:

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

### Exercícios: Nível 2

   1. Escreva um código que dê a nota aos estudantes de acordo com suas notas:

    ```sh
    90-100, A
    80-89, B
    70-79, C
    60-69, D
    0-59, F
    ```

   2. Obtenha o mês da entrada do usuário e depois verifique se a estação é Outono, Inverno, Primavera ou Verão. Se a entrada do usuário for:
    Setembro, Outubro ou Novembro, a estação é Outono.
    Dezembro, Janeiro ou Fevereiro, a estação é Inverno.
    Março, Abril ou Maio, a estação é Primavera
    Junho, Julho ou Agosto, a estação é Verão
   3. A seguinte lista contém algumas frutas:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    Se uma fruta não existir na lista, adicione a fruta à lista e imprima a lista modificada. Se a fruta existir, imprima print('That fruit already exist in the list')

### Exercícios: Nível 3

   1. Aqui temos um dicionário person. Sinta-se livre para modificá-lo!

```py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

     * Verifique se o dicionário person tem a chave skills; se sim, imprima a habilidade do meio na lista skills.
     * Verifique se o dicionário person tem a chave skills; se sim, verifique se a pessoa tem a habilidade 'Python' e imprima o resultado.
     * Se as habilidades da pessoa forem apenas JavaScript e React, imprima print('He is a front end developer'); se as habilidades da pessoa incluírem Node, Python, MongoDB, imprima print('He is a backend developer'); se as habilidades da pessoa incluírem React, Node e MongoDB, imprima print('He is a fullstack developer'); senão imprima print('unknown title') - para resultados mais precisos, mais condições podem ser aninhadas!
     * Se a pessoa for casada e morar na Finlândia, imprima a informação no seguinte formato:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 PARABÉNS ! 🎉

[<< Dia 8](./08_dictionaries_pt.md) | [Dia 10 >>](./10_loops_pt.md)

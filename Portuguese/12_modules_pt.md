<div align="center">
  <h1> 30 Dias de Python: Dia 12 - Módulos </h1>
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

[<< Dia 11](./11_functions_pt.md) | [Dia 13 >>](./13_list_comprehension_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 12](#-dia-12)
  - [Módulos](#módulos)
    - [O que é um Módulo](#o-que-é-um-módulo)
    - [Criando um Módulo](#criando-um-módulo)
    - [Importando um Módulo](#importando-um-módulo)
    - [Importar Funções de um Módulo](#importar-funções-de-um-módulo)
    - [Importar Funções de um Módulo e Renomear](#importar-funções-de-um-módulo-e-renomear)
  - [Importar Módulos Integrados](#importar-módulos-integrados)
    - [Módulo OS](#módulo-os)
    - [Módulo Sys](#módulo-sys)
    - [Módulo Statistics](#módulo-statistics)
    - [Módulo Math](#módulo-math)
    - [Módulo String](#módulo-string)
    - [Módulo Random](#módulo-random)
  - [💻 Exercícios: Dia 12](#-exercícios-dia-12)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 12

## Módulos

### O que é um Módulo

Um módulo é um arquivo contendo um conjunto de códigos ou um conjunto de funções que podem ser incluídos em uma aplicação. Um módulo pode ser um arquivo contendo uma única variável, uma função ou uma grande base de código.

### Criando um Módulo

Para criar um módulo escrevemos nosso código em um script Python e o salvamos como um arquivo .py. Crie um arquivo chamado mymodule.py dentro da sua pasta de projeto. Vamos escrever algum código neste arquivo.

```py
# arquivo mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

Crie o arquivo main.py no diretório do seu projeto e importe o arquivo mymodule.py.

### Importando um Módulo

Para importar o arquivo usamos a palavra-chave _import_ e apenas o nome do arquivo.

```py
# arquivo main.py
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### Importar Funções de um Módulo

Podemos ter muitas funções em um arquivo e podemos importar todas as funções de formas diferentes.

```py
# arquivo main.py
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Importar Funções de um Módulo e Renomear

Durante a importação podemos renomear o nome do módulo.

```py
# arquivo main.py
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Importar Módulos Integrados

Assim como em outras linguagens de programação, também podemos importar módulos importando o arquivo/função usando a palavra-chave _import_. Vamos importar o módulo comum que usaremos com mais frequência. Alguns dos módulos integrados comuns: _math_, _datetime_, _os_,_sys_, _random_, _statistics_, _collections_, _json_,_re_

### Módulo OS

Usando o módulo _os_ do Python, é possível realizar automaticamente muitas tarefas do sistema operacional. O módulo OS no Python fornece funções para criar, alterar o diretório de trabalho atual e remover um diretório (pasta), buscar seu conteúdo, alterar e identificar o diretório atual.

```py
# importando o módulo
import os
# Criando um diretório
os.mkdir('directory_name')
# Alterando o diretório atual
os.chdir('path')
# Obtendo o diretório de trabalho atual
os.getcwd()
# Removendo diretório
os.rmdir()
```

### Módulo Sys

O módulo sys fornece funções e variáveis usadas para manipular diferentes partes do ambiente de execução do Python. A função sys.argv retorna uma lista de argumentos de linha de comando passados para um script Python. O item no índice 0 nesta lista é sempre o nome do script, no índice 1 está o argumento passado a partir da linha de comando.

Exemplo de um arquivo script.py:

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # esta linha imprimiria: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

Agora, para verificar como esse script funciona, eu escrevi na linha de comando:

```sh
python script.py Asabeneh 30DaysOfPython
```

O resultado:

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge! 
```

Alguns comandos sys úteis:

```py
# para sair do sys
sys.exit()
# Para saber o maior valor inteiro que ele aceita
sys.maxsize
# Para saber o caminho do ambiente
sys.path
# Para saber a versão do Python que você está usando
sys.version
```

### Módulo Statistics

O módulo statistics fornece funções para estatística matemática de dados numéricos. As funções estatísticas populares definidas neste módulo: _mean_, _median_, _mode_, _stdev_ etc.

```py
from statistics import * # importando todos os módulos statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Módulo Math

Módulo contendo muitas operações e constantes matemáticas.

```py
import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, raiz quadrada
print(math.pow(2, 3))    # 8.0, função exponencial
print(math.floor(9.81))  # 9, arredondando para baixo
print(math.ceil(9.81))   # 10, arredondando para cima
print(math.log10(100))   # 2, logaritmo com base 10
```

Agora, importamos o módulo *math*, que contém muitas funções que podem nos ajudar a realizar cálculos matemáticos. Para verificar quais funções o módulo possui, podemos usar _help(math)_ ou _dir(math)_. Isso exibirá as funções disponíveis no módulo. Se quisermos importar apenas uma função específica do módulo, importamos da seguinte forma:

```py
from math import pi
print(pi)
```

Também é possível importar múltiplas funções ao mesmo tempo

```py

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2

```

Mas se quisermos importar todas as funções do módulo math, podemos usar \* .

```py
from math import *
print(pi)                  # 3.141592653589793, constante pi
print(sqrt(2))             # 1.4142135623730951, raiz quadrada
print(pow(2, 3))           # 8.0, exponencial
print(floor(9.81))         # 9, arredondando para baixo
print(ceil(9.81))          # 10, arredondando para cima
print(math.log10(100))     # 2
```

Quando importamos, também podemos renomear o nome da função.

```py
from math import pi as  PI
print(PI) # 3.141592653589793
```

### Módulo String

Um módulo string é um módulo útil para muitos propósitos. O exemplo abaixo mostra alguns usos do módulo string.

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Módulo Random

Agora você já está familiarizado com a importação de módulos. Vamos fazer mais uma importação para nos familiarizarmos ainda mais com isso. Vamos importar o módulo _random_, que nos dá um número aleatório entre 0 e 0.9999.... O módulo _random_ tem muitas funções, mas nesta seção usaremos apenas _random_ e _randint_.

```py
from random import random, randint
print(random())   # não recebe nenhum argumento; retorna um valor entre 0 e 0.9999
print(randint(5, 20)) # retorna um número inteiro aleatório entre [5, 20] inclusive
```

🌕 Você está indo longe. Continue! Você acabou de completar os desafios do dia 12 e está doze passos à frente no caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 12

### Exercícios: Nível 1

1. Escreva uma função que gere um random_user_id de seis dígitos/caracteres. 
   ```py
     print(random_user_id()) 
     '1ee33d'
   ```
2. Modifique a tarefa anterior. Declare uma função chamada user_id_gen_by_user. Ela não recebe nenhum parâmetro, mas recebe duas entradas usando input(). Uma das entradas é o número de caracteres e a segunda entrada é o número de IDs que devem ser gerados.
   
```py
print(user_id_gen_by_user()) # entrada do usuário: 5 5
#saída:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. Escreva uma função chamada rgb_color_gen. Ela vai gerar cores rgb (3 valores variando de 0 a 255 cada).
   
```py
print(rgb_color_gen())
# rgb(125,244,255) - a saída deve estar nesse formato
```

### Exercícios: Nível 2

1. Escreva uma função list_of_hexa_colors que retorna qualquer número de cores hexadecimais em um array (seis números hexadecimais escritos após #. O sistema numeral hexadecimal é composto de 16 símbolos, 0-9 e as primeiras 6 letras do alfabeto, a-f. Verifique a tarefa 6 para exemplos de saída).
1. Escreva uma função list_of_rgb_colors que retorna qualquer número de cores RGB em um array.
1. Escreva uma função generate_colors que possa gerar qualquer número de cores hexa ou rgb.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

### Exercícios: Nível 3

1. Chame sua função shuffle_list, ela recebe uma lista como parâmetro e retorna uma lista embaralhada
1. Escreva uma função que retorne um array com sete números aleatórios em um intervalo de 0-9. Todos os números devem ser únicos.

🎉 PARABÉNS ! 🎉

[<< Dia 11](./11_functions_pt.md) | [Dia 13 >>](./13_list_comprehension_pt.md)

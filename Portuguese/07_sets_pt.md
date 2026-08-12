<div align="center">
  <h1> 30 Dias de Python: Dia 7 - Conjuntos</h1>
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

[<< Dia 6](./06_tuples_pt.md) | [Dia 8 >>](./08_dictionaries_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 7](#-dia-7)
  - [Conjuntos](#conjuntos)
    - [Criando um Conjunto](#criando-um-conjunto)
    - [Obtendo o Comprimento de um Conjunto](#obtendo-o-comprimento-de-um-conjunto)
    - [Acessando Itens em um Conjunto](#acessando-itens-em-um-conjunto)
    - [Verificando um Item](#verificando-um-item)
    - [Adicionando Itens a um Conjunto](#adicionando-itens-a-um-conjunto)
    - [Removendo Itens de um Conjunto](#removendo-itens-de-um-conjunto)
    - [Limpando Itens de um Conjunto](#limpando-itens-de-um-conjunto)
    - [Excluindo um Conjunto](#excluindo-um-conjunto)
    - [Convertendo Lista em Conjunto](#convertendo-lista-em-conjunto)
    - [Unindo Conjuntos](#unindo-conjuntos)
    - [Encontrando Itens de Interseção](#encontrando-itens-de-interseção)
    - [Verificando Subconjunto e Superconjunto](#verificando-subconjunto-e-superconjunto)
    - [Verificando a Diferença Entre Dois Conjuntos](#verificando-a-diferença-entre-dois-conjuntos)
    - [Encontrando a Diferença Simétrica Entre Dois Conjuntos](#encontrando-a-diferença-simétrica-entre-dois-conjuntos)
    - [Unindo Conjuntos](#unindo-conjuntos-1)
  - [💻 Exercícios: Dia 7](#-exercícios-dia-7)
    - [Exercícios: Nível 1](#exercícios-nível-1)
    - [Exercícios: Nível 2](#exercícios-nível-2)
    - [Exercícios: Nível 3](#exercícios-nível-3)

# 📘 Dia 7

## Conjuntos

Conjunto (Set) é uma coleção de itens. Deixe-me te levar de volta à sua aula de Matemática do ensino fundamental ou médio. A definição matemática de conjunto também pode ser aplicada em Python. Um conjunto é uma coleção de elementos distintos, não ordenados e sem índice. Em Python, o conjunto é usado para armazenar itens únicos, e é possível encontrar a _união_, _interseção_, _diferença_, _diferença simétrica_, _subconjunto_, _superconjunto_ e _conjunto disjunto_ entre conjuntos.

### Criando um Conjunto

Para criar um conjunto vazio, usamos a função set(). Chaves vazias {} criarão um dicionário. 

- Criando um conjunto vazio

```py
# sintaxe
st = set()
```

- Criando um conjunto com itens iniciais

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
```

**Exemplo:**

```py
# sintaxe
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### Obtendo o Comprimento de um Conjunto

Usamos o método **len()** para encontrar o comprimento de um conjunto.

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

### Acessando Itens em um Conjunto

Usamos loops para acessar itens. Veremos isso na seção de loops

### Verificando um Item

Para verificar se um item existe em uma lista usamos o operador de pertencimento _in_.

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### Adicionando Itens a um Conjunto

Uma vez que um conjunto é criado não podemos alterar nenhum item, mas podemos adicionar itens adicionais.

- Adicione um item usando _add()_

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

- Adicione vários itens usando _update()_
  O _update()_ permite adicionar vários itens a um conjunto. O _update()_ recebe uma lista como argumento.

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### Removendo Itens de um Conjunto

Podemos remover um item de um conjunto usando o método _remove()_. Se o item não for encontrado, o método _remove()_ vai gerar um erro, então é bom verificar se o item existe no conjunto dado. Já o método _discard()_ não gera nenhum erro.

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

O método pop() remove um item aleatório de uma lista e retorna o item removido.

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # remove um item aleatório do conjunto

```

Se estivermos interessados no item removido.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
```

### Limpando Itens de um Conjunto

Se quisermos limpar ou esvaziar o conjunto usamos o método _clear_.

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### Excluindo um Conjunto

Se quisermos excluir o próprio conjunto usamos o operador _del_.

```py
# sintaxe
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### Convertendo Lista em Conjunto

Podemos converter lista em conjunto e conjunto em lista. Converter lista em conjunto remove os duplicados e apenas os itens únicos serão preservados.

```py
# sintaxe
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - a ordem é aleatória, pois conjuntos em geral não são ordenados
```

**Exemplo:**

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### Unindo Conjuntos

Podemos unir dois conjuntos usando o método _union()_ ou _update()_ ou o símbolo _|_.

- Union (União)
  Este método retorna um novo conjunto

```py
# sintaxe
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# ou usando isto: print(fruits | vegetables)
```

- Update (Atualização)
  Este método insere um conjunto em um determinado conjunto

```py
# sintaxe
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # o conteúdo de st2 é adicionado a st1
```

**Exemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

### Encontrando Itens de Interseção

A interseção retorna um conjunto de itens que estão em ambos os conjuntos, ou usando o símbolo _&_. Veja o exemplo

```py
# sintaxe
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# ou usando isto: st1 & st2
```

**Exemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon
```

### Verificando Subconjunto e Superconjunto

Um conjunto pode ser um subconjunto ou superconjunto de outros conjuntos:

- Subconjunto: _issubset()_
- Superconjunto: _issuperset_

```py
# sintaxe
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**Exemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, porque é um superconjunto
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### Verificando a Diferença Entre Dois Conjuntos

Retorna a diferença entre dois conjuntos, ou usando o símbolo _-_.

```py
# sintaxe
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2  : st2 - st1
```

**Exemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - o resultado não é ordenado (característica dos conjuntos)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python
```

### Encontrando a Diferença Simétrica Entre Dois Conjuntos

Retorna a diferença simétrica entre dois conjuntos. Isso significa que retorna um conjunto que contém todos os itens de ambos os conjuntos, exceto os itens presentes em ambos, matematicamente: (A\B) ∪ (B\A)

```py
# sintaxe
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# significa (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
```

**Exemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon
```

### Unindo Conjuntos

Se dois conjuntos não têm nenhum item em comum, nós os chamamos de conjuntos disjuntos. Podemos verificar se dois conjuntos são unidos ou disjuntos usando o método _isdisjoint()_.

```py
# sintaxe
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

**Exemplo:**

```py
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, porque não há item em comum

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, existem itens em comum {'o', 'n'}
```

🌕 Você é uma estrela em ascensão. Você acabou de completar os desafios do dia 7 e está sete passos à frente no seu caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 7

```py
# conjuntos
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Exercícios: Nível 1

1. Encontre o comprimento do conjunto it_companies
2. Adicione 'Twitter' a it_companies
3. Insira várias empresas de TI de uma vez no conjunto it_companies
4. Remova uma das empresas do conjunto it_companies
5. Qual é a diferença entre remove e discard

### Exercícios: Nível 2

1. Una A e B
2. Encontre a interseção de A com B
3. A é subconjunto de B?
4. A e B são conjuntos disjuntos?
5. Una A com B e B com A
6. Qual é a diferença simétrica entre A e B
7. Exclua os conjuntos completamente

### Exercícios: Nível 3

1. Converta as idades (age) em um conjunto e compare o comprimento da lista e do conjunto; qual é maior?
2. Explique a diferença entre os seguintes tipos de dados: string, lista, tupla e conjunto
3. _I am a teacher and I love to inspire and teach people._ Quantas palavras únicas foram usadas na frase? Use os métodos split e set para obter as palavras únicas.

🎉 PARABÉNS ! 🎉

[<< Dia 6](./06_tuples_pt.md) | [Dia 8 >>](./08_dictionaries_pt.md)

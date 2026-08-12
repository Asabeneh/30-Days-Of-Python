<div align="center">
  <h1> 30 Dias de Python: Dia 8 - Dicionários</h1>
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

[<< Dia 7](./07_sets_pt.md) | [Dia 9 >>](./09_conditionals_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 8](#-dia-8)
  - [Dicionários](#dicionários)
    - [Criando um Dicionário](#criando-um-dicionário)
    - [Comprimento do Dicionário](#comprimento-do-dicionário)
    - [Acessando Itens do Dicionário](#acessando-itens-do-dicionário)
    - [Adicionando Itens a um Dicionário](#adicionando-itens-a-um-dicionário)
    - [Modificando Itens em um Dicionário](#modificando-itens-em-um-dicionário)
    - [Verificando Chaves em um Dicionário](#verificando-chaves-em-um-dicionário)
    - [Removendo Pares de Chave e Valor de um Dicionário](#removendo-pares-de-chave-e-valor-de-um-dicionário)
    - [Convertendo Dicionário em Lista de Itens](#convertendo-dicionário-em-lista-de-itens)
    - [Limpando um Dicionário](#limpando-um-dicionário)
    - [Excluindo um Dicionário](#excluindo-um-dicionário)
    - [Copiando um Dicionário](#copiando-um-dicionário)
    - [Obtendo as Chaves do Dicionário como Lista](#obtendo-as-chaves-do-dicionário-como-lista)
    - [Obtendo os Valores do Dicionário como Lista](#obtendo-os-valores-do-dicionário-como-lista)
  - [💻 Exercícios: Dia 8](#-exercícios-dia-8)

# 📘 Dia 8

## Dicionários

Um dicionário é uma coleção de dados não ordenada, alterável (mutável), organizada em pares (chave: valor).

### Criando um Dicionário

Para criar um dicionário usamos chaves, {} ou a função integrada *dict()*.

```py
# sintaxe
empty_dict = {}
# Dicionário com valores
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
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
```

O dicionário acima mostra que um valor pode ser de qualquer tipo de dado: string, booleano, lista, tupla, conjunto ou até um dicionário.

### Comprimento do Dicionário

Verifica o número de pares 'chave: valor' no dicionário.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**Exemplo:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

```

### Acessando Itens do Dicionário

Podemos acessar itens do dicionário nos referindo ao nome da sua chave.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Erro
```

Acessar um item pelo nome da chave gera um erro se a chave não existir. Para evitar esse erro, primeiro devemos verificar se uma chave existe, ou podemos usar o método _get_. O método get retorna None, que é um objeto do tipo NoneType, se a chave não existir.
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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### Adicionando Itens a um Dicionário

Podemos adicionar novos pares de chave e valor a um dicionário

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

### Modificando Itens em um Dicionário

Podemos modificar itens em um dicionário

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### Verificando Chaves em um Dicionário

Usamos o operador _in_ para verificar se uma chave existe em um dicionário

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### Removendo Pares de Chave e Valor de um Dicionário

- _pop(key)_: remove o item com o nome de chave especificado:
- _popitem()_: remove o último item
- _del_: remove um item com o nome de chave especificado

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # remove o item key1
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # remove o último item
del dct['key2'] # remove o item key2
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
person.pop('first_name')        # Remove o item firstname
person.popitem()                # Remove o item address
del person['is_married']        # Remove o item is_married
```

### Convertendo Dicionário em Lista de Itens

O método _items()_ converte o dicionário em uma lista de tuplas.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### Limpando um Dicionário

Se não quisermos os itens em um dicionário, podemos limpá-los usando o método _clear()_

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### Excluindo um Dicionário

Se não usarmos mais o dicionário, podemos excluí-lo completamente

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### Copiando um Dicionário

Podemos copiar um dicionário usando o método _copy()_. Usando copy podemos evitar a mutação do dicionário original.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### Obtendo as Chaves do Dicionário como Lista

O método _keys()_ nos dá todas as chaves de um dicionário como uma lista.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### Obtendo os Valores do Dicionário como Lista

O método _values_ nos dá todos os valores de um dicionário como uma lista.

```py
# sintaxe
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 Você é surpreendente. Agora você está superequipado com o poder dos dicionários. Você acabou de completar os desafios do dia 8 e está oito passos à frente no seu caminho para a grandeza. Agora faça alguns exercícios para o cérebro e os músculos.

## 💻 Exercícios: Dia 8

1. Crie um dicionário vazio chamado dog
2. Adicione name, color, breed, legs, age ao dicionário dog
3. Crie um dicionário student e adicione first_name, last_name, gender, age, marital status, skills, country, city e address como chaves do dicionário
4. Obtenha o comprimento do dicionário student
5. Obtenha o valor de skills e verifique o tipo de dado; deve ser uma lista
6. Modifique os valores de skills adicionando uma ou duas habilidades
7. Obtenha as chaves do dicionário como uma lista
8. Obtenha os valores do dicionário como uma lista
9. Converta o dicionário em uma lista de tuplas usando o método _items()_
10. Exclua um dos itens do dicionário
11. Exclua um dos dicionários

🎉 PARABÉNS ! 🎉

[<< Dia 7](./07_sets_pt.md) | [Dia 9 >>](./09_conditionals_pt.md)

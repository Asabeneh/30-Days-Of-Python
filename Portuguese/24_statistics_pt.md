<div align="center">
  <h1> 30 Dias de Python: Dia 24 - Estatística</h1>
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

[<< Dia 23](./23_virtual_environment_pt.md) | [Dia 25 >>](./25_pandas_pt.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Dia 24](#-dia-24)
  - [Python para Análise Estatística](#python-para-análise-estatística)
  - [Estatística](#estatística)
  - [Dados](#dados)
  - [Módulo Statistics](#módulo-statistics)
- [NumPy](#numpy)

# 📘 Dia 24

## Python para Análise Estatística

## Estatística

Estatística é a disciplina que estuda a _coleta_, _organização_, _exibição_, _análise_, _interpretação_ e _apresentação_ de dados.
Estatística é um ramo da Matemática recomendado como pré-requisito para ciência de dados e machine learning. Estatística é um campo muito amplo, mas nesta seção vamos focar apenas na parte mais relevante.
Depois de concluir este desafio, você pode seguir para os caminhos de desenvolvimento web, análise de dados, machine learning e ciência de dados. Qualquer que seja o caminho que você siga, em algum momento da sua carreira você receberá dados nos quais poderá trabalhar. Ter algum conhecimento estatístico vai ajudá-lo a tomar decisões baseadas em dados, _os dados falam por si, como se costuma dizer_.

## Dados

O que é um dado? Um dado é qualquer conjunto de caracteres reunido e traduzido para algum propósito, geralmente análise. Pode ser qualquer caractere, incluindo texto e números, imagens, som ou vídeo. Se um dado não for colocado em um contexto, ele não faz nenhum sentido para um humano ou computador. Para dar sentido aos dados, precisamos trabalhar sobre eles usando diferentes ferramentas.

O fluxo de trabalho da análise de dados, ciência de dados ou machine learning começa a partir dos dados. Os dados podem ser fornecidos por alguma fonte de dados ou podem ser criados. Existem dados estruturados e não estruturados.

Os dados podem ser encontrados em formato pequeno ou grande. A maioria dos tipos de dados que vamos encontrar já foram abordados na seção de manipulação de arquivos.

## Módulo Statistics

O módulo Python _statistics_ fornece funções para calcular estatísticas matemáticas de dados numéricos. O módulo não pretende ser um concorrente de bibliotecas de terceiros como NumPy, SciPy, ou pacotes estatísticos completos e proprietários voltados para estatísticos profissionais, como Minitab, SAS e Matlab. Ele visa o nível de calculadoras gráficas e científicas.

# NumPy

Na primeira seção, definimos Python como uma excelente linguagem de programação de uso geral por si só, mas com a ajuda de outras bibliotecas populares (numpy, scipy, matplotlib, pandas etc.), ela se torna um ambiente poderoso para computação científica.

NumPy é a biblioteca principal para computação científica em Python. Ela fornece um objeto de array multidimensional de alto desempenho e ferramentas para trabalhar com arrays.

Até agora, temos usado o vscode, mas a partir de agora eu recomendaria usar o Jupyter Notebook. Para acessar o jupyter notebook vamos instalar o [anaconda](https://www.anaconda.com/). Se você estiver usando o anaconda, a maioria dos pacotes comuns já está incluída e você não precisa instalar pacotes se instalou o anaconda.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy
```

## Importando o NumPy

O Jupyter notebook está disponível se você preferir o [jupyter notebook](https://github.com/Asabeneh/data-science-for-everyone/blob/master/numpy/numpy.ipynb)

```py
    # Como importar o numpy
    import numpy as np
    # Como verificar a versão do pacote numpy
    print('numpy:', np.__version__)
    # Verificando os métodos disponíveis
    print(dir(np))
```

## Criando um array numpy usando

### Criando arrays numpy de inteiros

```py
    # Criando uma lista Python
    python_list = [1,2,3,4,5]

    # Verificando os tipos de dados
    print('Type:', type (python_list)) # <class 'list'>
    #
    print(python_list) # [1, 2, 3, 4, 5]

    two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

    print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Criando um array Numpy (Numerical Python) a partir de uma lista Python

    numpy_array_from_list = np.array(python_list)
    print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
    print(numpy_array_from_list) # array([1, 2, 3, 4, 5])
```

### Criando arrays numpy de float

Criando um array numpy de float a partir de uma lista com o parâmetro de tipo de dado float

```py
    # Lista Python
    python_list = [1,2,3,4,5]

    numy_array_from_list2 = np.array(python_list, dtype=float)
    print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])
```

### Criando arrays numpy booleanos

Criando um array numpy booleano a partir de uma lista

```py
    numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
    print(numpy_bool_array) # array([False,  True,  True, False, False])
```

### Criando um array multidimensional usando numpy

Um array numpy pode ter uma ou várias linhas e colunas

```py
    two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
    numpy_two_dimensional_list = np.array(two_dimensional_list)
    print(type (numpy_two_dimensional_list))
    print(numpy_two_dimensional_list)
```

```sh
    <class 'numpy.ndarray'>
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
```

### Convertendo um array numpy em lista

```python
# Sempre podemos converter um array de volta para uma lista Python usando tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('array unidimensional:', np_to_list)
print('array bidimensional: ', numpy_two_dimensional_list.tolist())
```

```sh
    <class 'list'>
    array unidimensional: [1, 2, 3, 4, 5]
    array bidimensional:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

### Criando um array numpy a partir de uma tupla

```py
# Array numpy a partir de uma tupla
# Criando uma tupla em Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]
```

### Forma (shape) de um array numpy

O método shape fornece a forma do array como uma tupla. O primeiro elemento é a linha e o segundo é a coluna. Se o array for unidimensional, ele retorna o tamanho do array.

```py
    nums = np.array([1, 2, 3, 4, 5])
    print(nums)
    print('forma de nums: ', nums.shape)
    numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
    print(numpy_two_dimensional_list)
    print('forma de numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
    three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10,11]])
    print(three_by_four_array)
    print('forma de three_by_four_array: ', three_by_four_array.shape)

```

```sh
    [1 2 3 4 5]
    forma de nums:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    forma de numpy_two_dimensional_list:  (3, 3)
    (3, 4)
```

### Tipo de dado de um array numpy

Tipos de dados: str, int, float, complex, bool, list, None

```py
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
```

```sh
    [-3 -2 -1  0  1  2  3]
    int64
    [-3. -2. -1.  0.  1.  2.  3.]
    float64
```

### Tamanho de um array numpy

No numpy, para saber o número de itens em um array, usamos size

```py
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('O tamanho:', numpy_array_from_list.size) # 5
print('O tamanho:', two_dimensional_list.size)  # 3

```

```sh
    O tamanho: 5
    O tamanho: 9
```

## Operações matemáticas usando numpy

Um array NumPy não é exatamente como uma lista Python. Para fazer operações matemáticas em uma lista Python, temos que percorrer os itens com um loop, mas o numpy permite fazer qualquer operação matemática sem loops.
Operações matemáticas:

- Adição (+)
- Subtração (-)
- Multiplicação (\*)
- Divisão (/)
- Módulo (%)
- Divisão inteira (//)
- Exponenciação (\*\*)

### Adição

```py
# Operação matemática
# Adição
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('array original: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)

```

```sh
    array original:  [1 2 3 4 5]
    [11 12 13 14 15]
```

### Subtração

```python
# Subtração
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('array original: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)
```

```sh
    array original:  [1 2 3 4 5]
    [-9 -8 -7 -6 -5]
```

### Multiplicação

```python
# Multiplicação
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('array original: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
```

```sh
    array original:  [1 2 3 4 5]
    [10 20 30 40 50]
```

### Divisão

```python
# Divisão
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('array original: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
```

```sh
    array original:  [1 2 3 4 5]
    [0.1 0.2 0.3 0.4 0.5]
```

### Módulo

```python
# Módulo; encontrando o resto
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('array original: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
```

```sh
    array original:  [1 2 3 4 5]
    [1 2 0 1 2]
```

### Divisão inteira

```py
# Divisão inteira: o resultado da divisão sem o resto
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('array original: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
```

### Exponenciação

```py
# Exponenciação é elevar um número à potência de outro:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('array original: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)
```

```sh
    array original:  [1 2 3 4 5]
    [ 1  4  9 16 25]
```

## Verificando tipos de dados

```py
# Números Int e Float
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
```

```sh
    int64
    float64
    bool
```

### Convertendo tipos

Podemos converter os tipos de dados de um array numpy

1. Int para Float

```py
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr
```

    array([1., 2., 3., 4.])

2. Float para Int

```py
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr
```

```sh
    array([1, 2, 3, 4])
```

3. Int para booleano

```py
np.array([-3, -2, 0, 1,2,3], dtype='bool')

```

```sh
    array([ True,  True, False,  True,  True,  True])
```

4. Int para str

```py
numpy_float_list.astype('int').astype('str')
```

```sh
    array(['1', '2', '3'], dtype='<U21')
```

## Arrays multidimensionais

```py
# Array de 2 dimensões
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Forma: ', two_dimension_array.shape)
print('Tamanho:', two_dimension_array.size)
print('Tipo de dado:', two_dimension_array.dtype)
```

```sh
    <class 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Forma:  (3, 3)
    Tamanho: 9
    Tipo de dado: int64
```

### Obtendo itens de um array numpy

```py
# Array de 2 dimensões
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('Primeira linha:', first_row)
print('Segunda linha:', second_row)
print('Terceira linha: ', third_row)
```

```sh
    Primeira linha: [1 2 3]
    Segunda linha: [4 5 6]
    Terceira linha:  [7 8 9]
```

```py
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('Primeira coluna:', first_column)
print('Segunda coluna:', second_column)
print('Terceira coluna: ', third_column)
print(two_dimension_array)

```

```sh
    Primeira coluna: [1 4 7]
    Segunda coluna: [2 5 8]
    Terceira coluna:  [3 6 9]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
```

## Fatiando um array numpy

Fatiar (slicing) em numpy é similar a fatiar em uma lista Python

```py
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
```

```sh
    [[1 2]
     [4 5]]
```

### Como inverter as linhas e o array inteiro?

```py
two_dimension_array[::]
```

```sh
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
```

### Inverter as posições das linhas e colunas

```py
    two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
    two_dimension_array[::-1,::-1]
```

```sh
    array([[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]])
```

## Como representar valores ausentes?

```python
    print(two_dimension_array)
    two_dimension_array[1,1] = 55
    two_dimension_array[1,2] =44
    print(two_dimension_array)
```

```sh
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
```

```py
    # Numpy Zeros
    # numpy.zeros(shape, dtype=float, order='C')
    numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
    numpy_zeroes
```

```sh
    array([[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]])
```

```py
# Numpy Zeros
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
```

```sh
    [[1 1 1]
     [1 1 1]
     [1 1 1]]
```

```py
twoes = numpy_ones * 2
```

```py
# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

```

```sh
    [[1 2 3]
     [4 5 6]]
    [[1 2]
     [3 4]
     [5 6]]
```

```py
flattened = reshaped.flatten()
flattened
```

```sh
    array([1, 2, 3, 4, 5, 6])
```

```py
    ## Empilhamento horizontal
    np_list_one = np.array([1,2,3])
    np_list_two = np.array([4,5,6])

    print(np_list_one + np_list_two)

    print('Concatenação horizontal:', np.hstack((np_list_one, np_list_two)))
```

```sh
    [5 7 9]
    Concatenação horizontal: [1 2 3 4 5 6]
```

```py
    ## Empilhamento vertical
    print('Concatenação vertical:', np.vstack((np_list_one, np_list_two)))
```

```sh
    Concatenação vertical: [[1 2 3]
     [4 5 6]]
```

#### Gerando números aleatórios

```py
    # Gerar um número float aleatório
    random_float = np.random.random()
    random_float
```

```sh
    0.018929887384753874
```

```py
    # Gerar números float aleatórios
    random_floats = np.random.random(5)
    random_floats
```

```sh
    array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])
```

```py
    # Gerando um número inteiro aleatório entre 0 e 10

    random_int = np.random.randint(0, 11)
    random_int
```

```sh
    4
```

```py
    # Gerando inteiros aleatórios entre 2 e 11, e criando um array de uma linha
    random_int = np.random.randint(2,10, size=4)
    random_int
```

```sh
    array([8, 8, 8, 2])
```

```py
    # Gerando inteiros aleatórios entre 0 e 10
    random_int = np.random.randint(2,10, size=(3,3))
    random_int
```

```sh
    array([[3, 5, 3],
           [7, 3, 6],
           [2, 3, 3]])
```

### Gerando números aleatórios

```py
    # np.random.normal(mu, sigma, size)
    normal_array = np.random.normal(79, 15, 80)
    normal_array

```

```sh
    array([ 89.49990595,  82.06056961, 107.21445842,  38.69307086,
            47.85259157,  93.07381061,  76.40724259,  78.55675184,
            72.17358173,  47.9888899 ,  65.10370622,  76.29696568,
            95.58234254,  68.14897213,  38.75862686, 122.5587927 ,
            67.0762565 ,  95.73990864,  81.97454563,  92.54264805,
            59.37035153,  77.76828101,  52.30752166,  64.43109931,
            62.63695351,  90.04616138,  75.70009094,  49.87586877,
            80.22002414,  68.56708848,  76.27791052,  67.24343975,
            81.86363935,  78.22703433, 102.85737041,  65.15700341,
            84.87033426,  76.7569997 ,  64.61321853,  67.37244562,
            74.4068773 ,  58.65119655,  71.66488727,  53.42458179,
            70.26872028,  60.96588544,  83.56129414,  72.14255326,
            81.00787609,  71.81264853,  72.64168853,  86.56608717,
            94.94667321,  82.32676973,  70.5165446 ,  85.43061003,
            72.45526212,  87.34681775,  87.69911217, 103.02831489,
            75.28598596,  67.17806893,  92.41274447, 101.06662611,
            87.70013935,  70.73980645,  46.40368207,  50.17947092,
            61.75618542,  90.26191397,  78.63968639,  70.84550744,
            88.91826581, 103.91474733,  66.3064638 ,  79.49726264,
            70.81087439,  83.90130623,  87.58555972,  59.95462521])
```

## Numpy e Estatística

```py
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
```

```sh
    (array([2., 0., 0., 0., 1., 2., 2., 0., 2., 0., 0., 1., 2., 2., 1., 4., 3.,
            4., 2., 7., 2., 2., 5., 4., 2., 4., 3., 2., 1., 5., 3., 0., 3., 2.,
            1., 0., 0., 1., 3., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1.]),
     array([ 38.69307086,  40.37038529,  42.04769973,  43.72501417,
             45.4023286 ,  47.07964304,  48.75695748,  50.43427191,
             52.11158635,  53.78890079,  55.46621523,  57.14352966,
             58.8208441 ,  60.49815854,  62.17547297,  63.85278741,
             65.53010185,  67.20741628,  68.88473072,  70.56204516,
             72.23935959,  73.91667403,  75.59398847,  77.27130291,
             78.94861734,  80.62593178,  82.30324622,  83.98056065,
             85.65787509,  87.33518953,  89.01250396,  90.6898184 ,
             92.36713284,  94.04444727,  95.72176171,  97.39907615,
             99.07639058, 100.75370502, 102.43101946, 104.1083339 ,
            105.78564833, 107.46296277, 109.14027721, 110.81759164,
            112.49490608, 114.17222052, 115.84953495, 117.52684939,
            119.20416383, 120.88147826, 122.5587927 ]),
     <a list of 50 Patch objects>)
```

### Matriz com numpy

```py

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
```

```py
four_by_four_matrix
```

```sh
matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]])
```

```py
np.asarray(four_by_four_matrix)[2] = 2
four_by_four_matrix
```

```sh

matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [2., 2., 2., 2.],
            [1., 1., 1., 1.]])
```

### Numpy numpy.arange()

#### O que é o Arange?

Às vezes você quer criar valores igualmente espaçados dentro de um intervalo definido. Por exemplo, você quer criar valores de 1 a 10; você pode usar a função numpy.arange()

```py
# criando uma lista usando range(início, fim, passo)
lst = range(0, 11, 2)
lst
```

```python
range(0, 11, 2)
```

```python
for l in lst:
    print(l)
```

```sh 0
    2
    4
    6
    8
    10
```

```py
# Similar ao range, o arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
whole_numbers
```

```sh
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])
```

```py
natural_numbers = np.arange(1, 20, 1)
natural_numbers
```

```py
odd_numbers = np.arange(1, 20, 2)
odd_numbers
```

```sh
    array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])
```

```py
even_numbers = np.arange(2, 20, 2)
even_numbers
```

```sh
    array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])
```

### Criando uma sequência de números usando linspace

```py
# numpy.linspace()
# numpy.logspace() em Python com exemplo
# Por exemplo, pode ser usado para criar 10 valores de 1 a 5 igualmente espaçados.
np.linspace(1.0, 5.0, num=10)
```

```sh
    array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
           3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

```py
# para não incluir o último valor do intervalo
np.linspace(1.0, 5.0, num=5, endpoint=False)
```

```
array([1. , 1.8, 2.6, 3.4, 4.2])
```

```py
# LogSpace
# LogSpace retorna números igualmente espaçados em uma escala logarítmica. Logspace tem os mesmos parâmetros que np.linspace.

# Sintaxe:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)
```

```sh

array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])
```

```py
# para verificar o tamanho de um array
x = np.array([1,2,3], dtype=np.complex128)
```

```py
x
```

```sh
    array([1.+0.j, 2.+0.j, 3.+0.j])
```

```py
x.itemsize
```

```sh
16
```

```py
# indexação e fatiamento de arrays NumPy em Python
np_list = np.array([(1,2,3), (4,5,6)])
np_list

```

```sh
    array([[1, 2, 3],
           [4, 5, 6]])
```

```py
print('Primeira linha: ', np_list[0])
print('Segunda linha: ', np_list[1])

```

```sh

    Primeira linha:  [1 2 3]
    Segunda linha:  [4 5 6]
```

```p
print('Primeira coluna: ', np_list[:,0])
print('Segunda coluna: ', np_list[:,1])
print('Terceira coluna: ', np_list[:,2])

```

```sh
    Primeira coluna:  [1 4]
    Segunda coluna:  [2 5]
    Terceira coluna:  [3 6]
```

### Funções estatísticas do NumPy com exemplos

O NumPy possui funções estatísticas bastante úteis para encontrar mínimo, máximo, média, mediana, percentil, desvio padrão e variância, etc., a partir dos elementos dados no array.
As funções são explicadas a seguir −
Função estatística
O Numpy é equipado com funções estatísticas robustas, listadas abaixo

- Funções Numpy
  - Mínimo np.min()
  - Máximo np.max()
  - Média np.mean()
  - Mediana np.median()
  - Variância
  - Percentil
  - Desvio padrão np.std()

```python
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())
```

    min:  1
    max:  55
    mean:  14.777777777777779
    sd:  18.913709183069525

```python
min:  1
max:  55
mean:  14.777777777777779
sd:  18.913709183069525
```

```python
print(two_dimension_array)
print('Coluna com mínimo: ', np.amin(two_dimension_array,axis=0))
print('Coluna com máximo: ', np.amax(two_dimension_array,axis=0))
print('=== Linha ==')
print('Linha com mínimo: ', np.amin(two_dimension_array,axis=1))
print('Linha com máximo: ', np.amax(two_dimension_array,axis=1))
```

    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
    Coluna com mínimo:  [1 2 3]
    Coluna com máximo:  [ 7 55 44]
    === Linha ==
    Linha com mínimo:  [1 4 7]
    Linha com máximo:  [ 3 55  9]

### Como criar sequências repetitivas?

```python
a = [1,2,3]

# Repete todo o 'a' duas vezes
print('Tile:   ', np.tile(a, 2))

# Repete cada elemento de 'a' duas vezes
print('Repeat: ', np.repeat(a, 2))

```

    Tile:    [1 2 3 1 2 3]
    Repeat:  [1 1 2 2 3 3]

### Como gerar números aleatórios?

```python
# Um número aleatório entre [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
```

    0.6149403282678213

```python
0.4763968133790438
```

    0.4763968133790438

```python
# Números aleatórios entre [0,1) de forma 2,3
r = np.random.random(size=[2,3])
print(r)
```

    [[0.13031737 0.4429537  0.1129527 ]
     [0.76811539 0.88256594 0.6754075 ]]

```python
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
```

    ['u' 'o' 'o' 'i' 'e' 'e' 'u' 'o' 'u' 'a']

```python
['i' 'u' 'e' 'o' 'a' 'i' 'e' 'u' 'o' 'i']
```

    ['iueoaieuoi']

```python
## Números aleatórios entre [0, 1] de forma 2, 2
rand = np.random.rand(2,2)
rand
```

    array([[0.97992598, 0.79642484],
           [0.65263629, 0.55763145]])

```python
rand2 = np.random.randn(2,2)
rand2

```

    array([[ 1.65593322, -0.52326621],
           [ 0.39071179, -2.03649407]])

```python
# Inteiros aleatórios entre [0, 10) de forma 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
rand_int
```

    array([[0, 7, 5],
           [4, 1, 4],
           [3, 5, 3],
           [4, 3, 8],
           [4, 6, 7]])

```py
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # média, desvio padrão, número de amostras
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
```

```sh

    min:  3.557811005458804
    max:  6.876317743643499
    mean:  5.035832048106663
    median:  5.020161980441937
    mode:  ModeResult(mode=array([3.55781101]), count=array([1]))
    sd:  0.489682424165213

```

```python
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
```

![png](../test_files/test_121_0.png)

```python
# numpy.dot(): Produto escalar em Python usando Numpy
# Produto escalar
# Numpy é uma biblioteca poderosa para computação de matrizes. Por exemplo, você pode calcular o produto escalar com np.dot

# Sintaxe

# numpy.dot(x, y, out=None)
```

### Álgebra Linear

1. Produto escalar

```python
## Álgebra linear
### Produto escalar: produto de dois arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23
```

### Multiplicação de matrizes NumPy com np.matmul()

```python
### Matmul: produto matricial de dois arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)
```

```sh
    array([[19, 22],
           [43, 50]])

```

```py
## Determinante de uma matriz 2*2
### 5*8-7*6np.linalg.det(i)
```

```python
np.linalg.det(i)
```

    -1.999999999999999

```python
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
```

```python
Z
```

    array([[0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.],
           [0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.],
           [0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.],
           [0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.]])

```python
new_list = [ x + 2 for x in range(0, 11)]
```

```python
new_list
```

    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

```python
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

```python
np_arr = np.array(range(0, 11))
np_arr + 2
```

array([ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

Usamos equações lineares para grandezas que têm uma relação linear entre si. Veja o exemplo abaixo:

```python
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
pressure
```

array([ 7, 9, 11, 13, 15])

```python
plt.plot(temp,pressure)
plt.xlabel('Temperatura em oC')
plt.ylabel('Pressão em atm')
plt.title('Temperatura vs Pressão')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
```

![png](../test_files/test_141_0.png)

Para traçar a distribuição normal gaussiana usando numpy. Como você pode ver abaixo, o numpy pode gerar números aleatórios. Para criar uma amostra aleatória, precisamos da média (mu), do sigma (desvio padrão) e do número de pontos de dados.

```python
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
```

![png](../test_files/test_143_0.png)

# Resumo

Resumindo, as principais diferenças com as listas Python são:

1. Arrays suportam operações vetorizadas, enquanto as listas não.
1. Uma vez que um array é criado, você não pode mudar seu tamanho. Você terá que criar um novo array ou sobrescrever o existente.
1. Todo array tem um e apenas um dtype. Todos os itens nele devem ser desse dtype.
1. Um array numpy equivalente ocupa muito menos espaço do que uma lista Python de listas.
1. Arrays numpy suportam indexação booleana.

## 💻 Exercícios: Dia 24

1. Repita todos os exemplos

🎉 PARABÉNS ! 🎉

[<< Dia 23](./23_virtual_environment_pt.md) | [Dia 25 >>](./25_pandas_pt.md)

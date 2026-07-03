<div align="center">
  <h1> 30 Days Of Python: Day 24 - 통계(Statistics)</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Second Edition: July, 2021</small>
</sub>
</div>

[<< Day 23](../23_Day_Virtual_environment/23_virtual_environment.md) | [Day 25 >>](../25_Day_Pandas/25_pandas.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 24](#-day-24)
  - [통계 분석을 위한 Python](#통계-분석을-위한-python)
  - [통계](#통계)
  - [데이터](#데이터)
  - [statistics 모듈](#statistics-모듈)
- [NumPy](#numpy)

# 📘 Day 24

## 통계 분석을 위한 Python

## 통계

통계는 데이터의 _수집_, _정리_, _표시_, _분석_, _해석_ 및 _발표_를 연구하는 학문입니다.
통계는 데이터 사이언스와 머신러닝의 선수과목으로 권장되는 수학의 한 분야입니다. 통계는 매우 광범위한 분야이지만 이 섹션에서는 가장 관련성이 높은 부분에만 집중하겠습니다.
이 챌린지를 완료한 후에는 웹 개발, 데이터 분석, 머신러닝 및 데이터 사이언스 경로로 나아갈 수 있습니다. 어떤 경로를 선택하든, 경력의 어느 시점에서 작업해야 할 데이터를 접하게 될 것입니다. 통계적 지식이 있으면 데이터를 기반으로 의사결정을 내리는 데 도움이 됩니다. _데이터가 말해주는 대로_라고 합니다.

## 데이터

데이터란 무엇일까요? 데이터는 보통 분석을 목적으로 수집되고 변환된 모든 문자의 집합입니다. 텍스트와 숫자, 그림, 소리 또는 비디오를 포함한 모든 문자가 될 수 있습니다. 데이터가 맥락에 놓이지 않으면 사람이나 컴퓨터에게 아무런 의미가 없습니다. 데이터로부터 의미를 만들어내기 위해서는 다양한 도구를 사용하여 데이터를 처리해야 합니다.

데이터 분석, 데이터 사이언스 또는 머신러닝의 워크플로우는 데이터에서 시작됩니다. 데이터는 어떤 데이터 소스에서 제공될 수도 있고 직접 생성할 수도 있습니다. 구조화된 데이터와 비구조화된 데이터가 있습니다.

데이터는 작은 형식이나 큰 형식으로 존재할 수 있습니다. 우리가 접하게 될 대부분의 데이터 타입은 파일 처리 섹션에서 다루었습니다.

## statistics 모듈

Python _statistics_ 모듈은 수치 데이터의 수학적 통계를 계산하는 함수를 제공합니다. 이 모듈은 NumPy, SciPy와 같은 서드파티 라이브러리나 Minitab, SAS, Matlab과 같은 전문 통계학자를 위한 완전한 기능을 갖춘 통계 패키지의 경쟁자가 되려는 것이 아닙니다. 이 모듈은 그래프 계산기 및 공학용 계산기 수준을 목표로 합니다.

# NumPy

첫 번째 섹션에서 Python 자체가 훌륭한 범용 프로그래밍 언어라고 정의했지만, 다른 인기 있는 라이브러리(numpy, scipy, matplotlib, pandas 등)의 도움을 받으면 과학 컴퓨팅을 위한 강력한 환경이 됩니다.

NumPy는 Python에서 과학 컴퓨팅을 위한 핵심 라이브러리입니다. 고성능 다차원 배열 객체와 배열 작업을 위한 도구를 제공합니다.

지금까지 vscode를 사용해왔지만, 이제부터는 Jupyter Notebook 사용을 권장합니다. Jupyter notebook에 접근하려면 [anaconda](https://www.anaconda.com/)를 설치하세요. anaconda를 사용하면 대부분의 일반적인 패키지가 포함되어 있어 anaconda를 설치했다면 별도로 패키지를 설치할 필요가 없습니다.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy
```

## NumPy 가져오기

[jupyter notebook](https://github.com/Asabeneh/data-science-for-everyone/blob/master/numpy/numpy.ipynb)을 선호하신다면 Jupyter notebook을 사용하실 수 있습니다.

```py
    # numpy를 가져오는 방법
    import numpy as np
    # numpy 패키지의 버전 확인하기
    print('numpy:', np.__version__)
    # 사용 가능한 메서드 확인하기
    print(dir(np))
```

## numpy 배열 생성하기

### 정수형 numpy 배열 만들기

```py
    # Python 리스트 생성
    python_list = [1,2,3,4,5]

    # 데이터 타입 확인
    print('Type:', type (python_list)) # <class 'list'>
    #
    print(python_list) # [1, 2, 3, 4, 5]

    two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

    print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Python 리스트에서 Numpy(Numerical Python) 배열 생성

    numpy_array_from_list = np.array(python_list)
    print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
    print(numpy_array_from_list) # array([1, 2, 3, 4, 5])
```

### 실수형 numpy 배열 만들기

float 데이터 타입 매개변수를 사용하여 리스트에서 실수형 numpy 배열을 생성합니다.

```py
    # Python 리스트
    python_list = [1,2,3,4,5]

    numy_array_from_list2 = np.array(python_list, dtype=float)
    print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])
```

### 불리언 numpy 배열 만들기

리스트에서 불리언 numpy 배열을 생성합니다.

```py
    numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
    print(numpy_bool_array) # array([False,  True,  True, False, False])
```

### numpy를 사용한 다차원 배열 만들기

numpy 배열은 하나 또는 여러 개의 행과 열을 가질 수 있습니다.

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

### numpy 배열을 리스트로 변환하기

```python
# tolist()를 사용하여 항상 배열을 Python 리스트로 다시 변환할 수 있습니다.
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())
```

```sh
    <class 'list'>
    one dimensional array: [1, 2, 3, 4, 5]
    two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

### 튜플에서 numpy 배열 만들기

```py
# 튜플에서 Numpy 배열 생성
# Python에서 튜플 생성
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]
```

### numpy 배열의 형태(shape)

shape 메서드는 배열의 형태를 튜플로 제공합니다. 첫 번째는 행이고 두 번째는 열입니다. 배열이 1차원이면 배열의 크기를 반환합니다.

```py
    nums = np.array([1, 2, 3, 4, 5])
    print(nums)
    print('shape of nums: ', nums.shape)
    numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
    print(numpy_two_dimensional_list)
    print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
    three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10,11]]
    print(three_by_four_array)
    print('shape of three_by_four_array: ', three_by_four_array.shape)

```

```sh
    [1 2 3 4 5]
    shape of nums:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    shape of numpy_two_dimensional_list:  (3, 3)
    (3, 4)
```

### numpy 배열의 데이터 타입

데이터 타입의 종류: str, int, float, complex, bool, list, None

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

### numpy 배열의 크기

numpy에서 numpy 배열 리스트의 항목 수를 알기 위해 size를 사용합니다.

```py
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

```

```sh
    The size: 5
    The size: 9
```

## numpy를 사용한 수학 연산

NumPy 배열은 Python 리스트와 정확히 같지 않습니다. Python 리스트에서 수학 연산을 하려면 항목을 반복해야 하지만, numpy는 반복 없이 모든 수학 연산을 수행할 수 있습니다.
수학 연산:

- 덧셈 (+)
- 뺄셈 (-)
- 곱셈 (\*)
- 나눗셈 (/)
- 나머지 (%)
- 바닥 나눗셈(//)
- 거듭제곱(\*\*)

### 덧셈

```py
# 수학 연산
# 덧셈
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)

```

```sh
    original array:  [1 2 3 4 5]
    [11 12 13 14 15]
```

### 뺄셈

```python
# 뺄셈
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)
```

```sh
    original array:  [1 2 3 4 5]
    [-9 -8 -7 -6 -5]
```

### 곱셈

```python
# 곱셈
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [10 20 30 40 50]
```

### 나눗셈

```python
# 나눗셈
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [0.1 0.2 0.3 0.4 0.5]
```

### 나머지

```python
# 나머지; 나눈 후 나머지 찾기
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [1 2 0 1 2]
```

### 바닥 나눗셈

```py
# 바닥 나눗셈: 나머지를 제외한 나눗셈 결과
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
```

### 거듭제곱

```py
# 거듭제곱은 어떤 수의 다른 수에 대한 제곱을 구하는 것입니다:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [ 1  4  9 16 25]
```

## 데이터 타입 확인하기

```py
# 정수, 실수
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

### 타입 변환하기

numpy 배열의 데이터 타입을 변환할 수 있습니다.

1. Int에서 Float으로

```py
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr
```

    array([1., 2., 3., 4.])

2. Float에서 Int로

```py
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr
```

```sh
    array([1, 2, 3, 4])
```

3. Int에서 boolean으로

```py
np.array([-3, -2, 0, 1,2,3], dtype='bool')

```

```sh
    array([ True,  True, False,  True,  True,  True])
```

4. Int에서 str로

```py
numpy_float_list.astype('int').astype('str')
```

```sh
    array(['1', '2', '3'], dtype='<U21')
```

## 다차원 배열

```py
# 2차원 배열
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
```

```sh
    <class 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Shape:  (3, 3)
    Size: 9
    Data type: int64
```

### numpy 배열에서 항목 가져오기

```py
# 2차원 배열
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
```

```sh
    First row: [1 2 3]
    Second row: [4 5 6]
    Third row:  [7 8 9]
```

```py
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

```

```sh
    First column: [1 4 7]
    Second column: [2 5 8]
    Third column:  [3 6 9]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
```

## Numpy 배열 슬라이싱

numpy에서의 슬라이싱은 Python 리스트에서의 슬라이싱과 유사합니다.

```py
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
```

```sh
    [[1 2]
     [4 5]]
```

### 행과 전체 배열을 뒤집는 방법

```py
two_dimension_array[::]
```

```sh
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
```

### 행과 열 위치 반전하기

```py
    two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
    two_dimension_array[::-1,::-1]
```

```sh
    array([[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]])
```

## 결측값을 표현하는 방법

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
    # Numpy 영행렬
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
# Numpy 1로 채워진 배열
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
# Reshape (형태 변환)
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
    ## 수평 스택
    np_list_one = np.array([1,2,3])
    np_list_two = np.array([4,5,6])

    print(np_list_one + np_list_two)

    print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
```

```sh
    [5 7 9]
    Horizontal Append: [1 2 3 4 5 6]
```

```py
    ## 수직 스택
    print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
```

```sh
    Vertical Append: [[1 2 3]
     [4 5 6]]
```

#### 난수 생성하기

```py
    # 랜덤 실수 생성
    random_float = np.random.random()
    random_float
```

```sh
    0.018929887384753874
```

```py
    # 랜덤 실수 생성
    random_floats = np.random.random(5)
    random_floats
```

```sh
    array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])
```

```py
    # 0에서 10 사이의 랜덤 정수 생성

    random_int = np.random.randint(0, 11)
    random_int
```

```sh
    4
```

```py
    # 2에서 11 사이의 랜덤 정수를 생성하고, 1행 배열 만들기
    random_int = np.random.randint(2,10, size=4)
    random_int
```

```sh
    array([8, 8, 8, 2])
```

```py
    # 0에서 10 사이의 랜덤 정수 생성
    random_int = np.random.randint(2,10, size=(3,3))
    random_int
```

```sh
    array([[3, 5, 3],
           [7, 3, 6],
           [2, 3, 3]])
```

### 난수 생성하기

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

## Numpy와 통계

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

### numpy의 행렬

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

#### arange란 무엇인가요?

때때로 정의된 구간 내에서 균등하게 배치된 값을 만들고 싶을 때가 있습니다. 예를 들어, 1에서 10까지의 값을 만들고 싶다면 numpy.arange() 함수를 사용할 수 있습니다.

```py
# range(시작, 종료, 간격)를 사용하여 리스트 생성
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
# range와 유사한 numpy.arange(시작, 종료, 간격)
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

### linspace를 사용한 숫자 시퀀스 생성

```py
# numpy.linspace()
# Python에서의 numpy.logspace() 예제
# 예를 들어, 1에서 5까지 균등하게 배치된 10개의 값을 만드는 데 사용할 수 있습니다.
np.linspace(1.0, 5.0, num=10)
```

```sh
    array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
           3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

```py
# 구간의 마지막 값을 포함하지 않음
np.linspace(1.0, 5.0, num=5, endpoint=False)
```

```
array([1. , 1.8, 2.6, 3.4, 4.2])
```

```py
# LogSpace
# LogSpace는 로그 스케일에서 균등하게 배치된 숫자를 반환합니다. Logspace는 np.linspace와 같은 매개변수를 가집니다.

# 구문:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)
```

```sh

array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])
```

```py
# 배열의 크기를 확인하려면
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
# Python에서 NumPy 배열의 인덱싱과 슬라이싱
np_list = np.array([(1,2,3), (4,5,6)])
np_list

```

```sh
    array([[1, 2, 3],
           [4, 5, 6]])
```

```py
print('First row: ', np_list[0])
print('Second row: ', np_list[1])

```

```sh

    First row:  [1 2 3]
    Second row:  [4 5 6]
```

```p
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

```

```sh
    First column:  [1 4]
    Second column:  [2 5]
    Third column:  [3 6]
```

### NumPy 통계 함수 예제

NumPy는 주어진 배열 요소에서 최솟값, 최댓값, 평균, 중앙값, 백분위수, 표준편차 및 분산 등을 구하기 위한 매우 유용한 통계 함수를 가지고 있습니다.
함수들은 다음과 같이 설명됩니다 −
통계 함수
Numpy는 아래에 나열된 강력한 통계 함수를 갖추고 있습니다.

- Numpy 함수
  - Min np.min()
  - Max np.max()
  - Mean np.mean()
  - Median np.median()
  - Variance
  - Percentile
  - Standard deviation np.std()

```python
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## 최솟값, 최댓값, 평균, 중앙값, 표준편차
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
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))
```

    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
    Column with minimum:  [1 2 3]
    Column with maximum:  [ 7 55 44]
    === Row ==
    Row with minimum:  [1 4 7]
    Row with maximum:  [ 3 55  9]

### 반복 시퀀스를 만드는 방법

```python
a = [1,2,3]

# 'a' 전체를 두 번 반복
print('Tile:   ', np.tile(a, 2))

# 'a'의 각 요소를 두 번 반복
print('Repeat: ', np.repeat(a, 2))

```

    Tile:    [1 2 3 1 2 3]
    Repeat:  [1 1 2 2 3 3]

### 난수를 생성하는 방법

```python
# [0,1) 사이의 하나의 랜덤 숫자
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
# [0,1) 사이의 (2,3) 형태의 랜덤 숫자
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
## [0, 1] 사이의 (2, 2) 형태의 랜덤 숫자
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
# [0, 10) 사이의 (5,3) 형태의 랜덤 정수
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
np_normal_dis = np.random.normal(5, 0.5, 1000) # 평균, 표준편차, 샘플 수
np_normal_dis
## 최솟값, 최댓값, 평균, 중앙값, 표준편차
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

![png](../../test_files/test_121_0.png)

```python
# numpy.dot(): Python에서 Numpy를 사용한 내적
# 내적
# Numpy는 행렬 계산을 위한 강력한 라이브러리입니다. 예를 들어, np.dot으로 내적을 계산할 수 있습니다.

# 구문

# numpy.dot(x, y, out=None)
```

### 선형 대수

1. 내적

```python
## 선형 대수
### 내적: 두 배열의 곱
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23
```

### np.matmul()을 사용한 NumPy 행렬 곱셈

```python
### Matmul: 두 배열의 행렬 곱
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
## 2*2 행렬의 행렬식
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

선형 관계가 있는 양에 대해 선형 방정식을 사용합니다. 아래 예제를 살펴보겠습니다:

```python
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
pressure
```

array([ 7, 9, 11, 13, 15])

```python
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
```

![png](../../test_files/test_141_0.png)

numpy를 사용하여 가우시안 정규분포를 그려보겠습니다. 아래에서 볼 수 있듯이, numpy는 난수를 생성할 수 있습니다. 랜덤 샘플을 만들려면 평균(mu), 시그마(표준편차), 데이터 포인트 수가 필요합니다.

```python
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
```

![png](../../test_files/test_143_0.png)

# 요약

요약하면, Python 리스트와의 주요 차이점은 다음과 같습니다:

1. 배열은 벡터화된 연산을 지원하지만 리스트는 그렇지 않습니다.
1. 배열이 생성되면 크기를 변경할 수 없습니다. 새 배열을 만들거나 기존 배열을 덮어써야 합니다.
1. 모든 배열은 하나의 dtype만 가집니다. 모든 항목은 해당 dtype이어야 합니다.
1. 동등한 numpy 배열은 Python 리스트의 리스트보다 훨씬 적은 공간을 차지합니다.
1. numpy 배열은 불리언 인덱싱을 지원합니다.

## 💻 연습문제: Day 24

1. 모든 예제를 반복해 보세요.

🎉 축하합니다 ! 🎉

[<< Day 23](../23_Day_Virtual_environment/23_virtual_environment.md) | [Day 25 >>](../25_Day_Pandas/25_pandas.md)

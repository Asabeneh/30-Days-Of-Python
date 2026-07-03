<div align="center">
  <h1> 30 Days Of Python: Day 25 - Pandas </h1>
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

[<< Day 24](../24_Day_Statistics/24_statistics.md) | [Day 26 >>](../26_Day_Python_web/26_python_web.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 25](#-day-25)
  - [Pandas](#pandas)
    - [Pandas 설치하기](#pandas-설치하기)
    - [Pandas 가져오기](#pandas-가져오기)
    - [기본 인덱스로 Pandas Series 만들기](#기본-인덱스로-pandas-series-만들기)
    - [사용자 정의 인덱스로 Pandas Series 만들기](#사용자-정의-인덱스로-pandas-series-만들기)
    - [딕셔너리에서 Pandas Series 만들기](#딕셔너리에서-pandas-series-만들기)
    - [상수 Pandas Series 만들기](#상수-pandas-series-만들기)
    - [Linspace를 사용하여 Pandas Series 만들기](#linspace를-사용하여-pandas-series-만들기)
  - [DataFrames](#dataframes)
    - [리스트의 리스트에서 DataFrame 만들기](#리스트의-리스트에서-dataframe-만들기)
    - [딕셔너리를 사용하여 DataFrame 만들기](#딕셔너리를-사용하여-dataframe-만들기)
    - [딕셔너리 리스트에서 DataFrame 만들기](#딕셔너리-리스트에서-dataframe-만들기)
  - [Pandas를 사용하여 CSV 파일 읽기](#pandas를-사용하여-csv-파일-읽기)
    - [데이터 탐색](#데이터-탐색)
  - [DataFrame 수정하기](#dataframe-수정하기)
    - [DataFrame 만들기](#dataframe-만들기)
    - [새 열 추가하기](#새-열-추가하기)
    - [열 값 수정하기](#열-값-수정하기)
    - [DataFrame 열 서식 지정하기](#dataframe-열-서식-지정하기)
  - [열 값의 데이터 타입 확인하기](#열-값의-데이터-타입-확인하기)
    - [불리언 인덱싱](#불리언-인덱싱)
  - [연습문제: Day 25](#연습문제-day-25)

# 📘 Day 25

## Pandas

Pandas는 Python 프로그래밍 언어를 위한 오픈 소스, 고성능, 사용하기 쉬운 데이터 구조 및 데이터 분석 도구입니다.
Pandas는 *Series*와 *Data Frames*와 같은 테이블 형태의 데이터를 다루기 위해 설계된 데이터 구조와 도구를 제공합니다.
Pandas는 다음과 같은 데이터 조작 도구를 제공합니다:

- 재구조화(reshaping)
- 병합(merging)
- 정렬(sorting)
- 슬라이싱(slicing)
- 집계(aggregation)
- 결측값 대체(imputation)
anaconda를 사용하고 있다면, pandas를 별도로 설치할 필요가 없습니다.

### Pandas 설치하기

Mac의 경우:
```py
pip install conda
conda install pandas
```

Windows의 경우:
```py
pip install conda
pip install pandas
```

Pandas 데이터 구조는 *Series*와 *DataFrames*를 기반으로 합니다.

*Series*는 *열(column)*이고, DataFrame은 *Series*의 모음으로 구성된 *다차원 테이블*입니다. Pandas Series를 만들기 위해서는 numpy를 사용하여 1차원 배열을 만들거나 Python 리스트를 사용해야 합니다.
Series의 예제를 살펴보겠습니다:

이름 Pandas Series

![pandas series](../../images/pandas-series-1.png)

국가 Series

![pandas series](../../images/pandas-series-2.png)

도시 Series

![pandas series](../../images/pandas-series-3.png)

보시다시피, Pandas Series는 하나의 데이터 열에 불과합니다. 여러 열을 원한다면 Data Frame을 사용합니다. 아래 예제는 Pandas DataFrames를 보여줍니다.

Pandas Data Frame의 예제를 살펴보겠습니다:

![Pandas data frame](../../images/pandas-dataframe-1.png)

Data Frame은 행과 열의 모음입니다. 아래 표를 보세요; 위의 예제보다 훨씬 더 많은 열이 있습니다:

![Pandas data frame](../../images/pandas-dataframe-2.png)

다음으로, pandas를 가져오는 방법과 pandas를 사용하여 Series 및 DataFrames를 만드는 방법을 알아보겠습니다.

### Pandas 가져오기

```python
import pandas as pd # pandas를 pd로 가져오기
import numpy  as np # numpy를 np로 가져오기
```

### 기본 인덱스로 Pandas Series 만들기

```python
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)
```

```sh
    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64
```

### 사용자 정의 인덱스로 Pandas Series 만들기

```python
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums, index=[1, 2, 3, 4, 5])
print(s)
```

```sh
    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64
```

```python
fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)
```

```sh
    1    Orange
    2    Banana
    3    Mango
    dtype: object
```

### 딕셔너리에서 Pandas Series 만들기

```python
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
```

```python
s = pd.Series(dct)
print(s)
```

```sh
    name       Asabeneh
    country     Finland
    city       Helsinki
    dtype: object
```

### 상수 Pandas Series 만들기

```python
s = pd.Series(10, index = [1, 2, 3])
print(s)
```

```sh
    1    10
    2    10
    3    10
    dtype: int64
```

### Linspace를 사용하여 Pandas Series 만들기

```python
s = pd.Series(np.linspace(5, 20, 10)) # linspace(시작, 끝, 항목수)
print(s)
```

```sh
    0     5.000000
    1     6.666667
    2     8.333333
    3    10.000000
    4    11.666667
    5    13.333333
    6    15.000000
    7    16.666667
    8    18.333333
    9    20.000000
    dtype: float64
```

## DataFrames

Pandas Data Frame은 다양한 방법으로 만들 수 있습니다.

### 리스트의 리스트에서 DataFrame 만들기

```python
data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsink</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

### 딕셔너리를 사용하여 DataFrame 만들기

```python
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsiki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

### 딕셔너리 리스트에서 DataFrame 만들기

```python
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

## Pandas를 사용하여 CSV 파일 읽기

이 예제에서 필요한 CSV 파일을 다운로드하려면, 콘솔/명령줄만 있으면 충분합니다:

```sh
curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
```

다운로드한 파일을 작업 디렉토리에 넣으세요.

```python
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
```

### 데이터 탐색

head()를 사용하여 처음 5개의 행만 읽어보겠습니다.

```python
print(df.head()) # 5개의 행을 제공합니다. head() 메서드에 인자를 전달하여 행 수를 늘릴 수 있습니다
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Male</td>
      <td>73.847017</td>
      <td>241.893563</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Male</td>
      <td>68.781904</td>
      <td>162.310473</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Male</td>
      <td>74.110105</td>
      <td>212.740856</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Male</td>
      <td>71.730978</td>
      <td>220.042470</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Male</td>
      <td>69.881796</td>
      <td>206.349801</td>
    </tr>
  </tbody>
</table>

tail() 메서드를 사용하여 데이터프레임의 마지막 레코드도 탐색해 보겠습니다.

```python
print(df.tail()) # tail은 마지막 5개의 행을 제공합니다. tail 메서드에 인자를 전달하여 행 수를 늘릴 수 있습니다
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>9995</td>
      <td>Female</td>
      <td>66.172652</td>
      <td>136.777454</td>
    </tr>
    <tr>
      <td>9996</td>
      <td>Female</td>
      <td>67.067155</td>
      <td>170.867906</td>
    </tr>
    <tr>
      <td>9997</td>
      <td>Female</td>
      <td>63.867992</td>
      <td>128.475319</td>
    </tr>
    <tr>
      <td>9998</td>
      <td>Female</td>
      <td>69.034243</td>
      <td>163.852461</td>
    </tr>
    <tr>
      <td>9999</td>
      <td>Female</td>
      <td>61.944246</td>
      <td>113.649103</td>
    </tr>
  </tbody>
</table>

보시다시피, CSV 파일에는 Gender, Height, Weight 세 개의 행이 있습니다. DataFrame의 행이 많다면, 모든 열을 파악하기 어려울 것입니다. 따라서, 열을 알기 위한 메서드를 사용해야 합니다. 행의 수도 알 수 없습니다. shape 메서드를 사용해 보겠습니다.

```python
print(df.shape) # 보시다시피 10000개의 행과 3개의 열이 있습니다
```

    (10000, 3)

columns를 사용하여 모든 열을 가져와 보겠습니다.

```python
print(df.columns)
```

    Index(['Gender', 'Height', 'Weight'], dtype='object')

이제, 열 키를 사용하여 특정 열을 가져와 보겠습니다.

```python
heights = df['Height'] # 이것은 이제 Series입니다
```

```python
print(heights)
```

```sh
    0       73.847017
    1       68.781904
    2       74.110105
    3       71.730978
    4       69.881796
              ...
    9995    66.172652
    9996    67.067155
    9997    63.867992
    9998    69.034243
    9999    61.944246
    Name: Height, Length: 10000, dtype: float64
```

```python
weights = df['Weight'] # 이것은 이제 Series입니다
```

```python
print(weights)
```

```sh
    0       241.893563
    1       162.310473
    2       212.740856
    3       220.042470
    4       206.349801
               ...
    9995    136.777454
    9996    170.867906
    9997    128.475319
    9998    163.852461
    9999    113.649103
    Name: Weight, Length: 10000, dtype: float64
```

```python
print(len(heights) == len(weights))
```

    True

describe() 메서드는 데이터셋의 기술 통계 값을 제공합니다.

```python
print(heights.describe()) # 키 데이터에 대한 통계 정보를 제공합니다
```

```sh
    count    10000.000000
    mean        66.367560
    std          3.847528
    min         54.263133
    25%         63.505620
    50%         66.318070
    75%         69.174262
    max         78.998742
    Name: Height, dtype: float64
```

```python
print(weights.describe())
```

```sh
    count    10000.000000
    mean       161.440357
    std         32.108439
    min         64.700127
    25%        135.818051
    50%        161.212928
    75%        187.169525
    max        269.989699
    Name: Weight, dtype: float64
```

```python
print(df.describe())  # describe는 DataFrame에서도 통계 정보를 제공할 수 있습니다
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>66.367560</td>
      <td>161.440357</td>
    </tr>
    <tr>
      <td>std</td>
      <td>3.847528</td>
      <td>32.108439</td>
    </tr>
    <tr>
      <td>min</td>
      <td>54.263133</td>
      <td>64.700127</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>63.505620</td>
      <td>135.818051</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>66.318070</td>
      <td>161.212928</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>69.174262</td>
      <td>187.169525</td>
    </tr>
    <tr>
      <td>max</td>
      <td>78.998742</td>
      <td>269.989699</td>
    </tr>
  </tbody>
</table>

describe()와 마찬가지로, info() 메서드도 데이터셋에 대한 정보를 제공합니다.

## DataFrame 수정하기

DataFrame 수정하기:
    * 새로운 DataFrame을 만들 수 있습니다.
    * DataFrame에 새 열을 만들어 추가할 수 있습니다.
    * DataFrame에서 기존 열을 제거할 수 있습니다.
    * DataFrame의 기존 열을 수정할 수 있습니다.
    * DataFrame의 열 값의 데이터 타입을 변경할 수 있습니다.

### DataFrame 만들기

항상 그렇듯이, 먼저 필요한 패키지를 가져옵니다. 이제 pandas와 numpy, 이 둘도 없는 최고의 친구를 가져오겠습니다.

```python
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

DataFrame에 열을 추가하는 것은 딕셔너리에 키를 추가하는 것과 같습니다.

먼저 이전 예제를 사용하여 DataFrame을 만들겠습니다. DataFrame을 만든 후, 열과 열 값을 수정하기 시작하겠습니다.

### 새 열 추가하기

DataFrame에 체중(weight) 열을 추가해 보겠습니다.

```python
weights = [74, 78, 69]
df['Weight'] = weights
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
    </tr>
  </tbody>
</table>

DataFrame에 키(height) 열도 추가해 보겠습니다.

```python
heights = [173, 175, 169]
df['Height'] = heights
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>173</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>175</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>169</td>
    </tr>
  </tbody>
</table>

위의 DataFrame에서 보시다시피, Weight와 Height라는 새 열을 추가했습니다. 체중과 키를 사용하여 BMI(체질량지수)를 계산하는 열을 하나 더 추가해 보겠습니다. BMI는 체중을 키의 제곱(미터 단위)으로 나눈 값입니다 - Weight/Height * Height.

보시다시피, 키가 센티미터 단위이므로, 미터로 변환해야 합니다. 키 행을 수정해 보겠습니다.

### 열 값 수정하기

```python
df['Height'] = df['Height'] * 0.01
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
    </tr>
  </tbody>
</table>

```python
# 함수를 사용하면 코드가 깔끔해지지만, 함수 없이도 BMI를 계산할 수 있습니다
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = calculate_bmi()

```


```python
df['BMI'] = bmi
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.725183</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.469388</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.158818</td>
    </tr>
  </tbody>
</table>

### DataFrame 열 서식 지정하기

DataFrame의 BMI 열 값은 소수점 이하 유효 숫자가 많은 부동 소수점입니다. 소수점 이하 한 자리로 변경해 보겠습니다.

```python
df['BMI'] = round(df['BMI'], 1)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
    </tr>
  </tbody>
</table>

DataFrame의 정보가 아직 완전하지 않은 것 같습니다. 출생 연도와 현재 연도 열을 추가해 보겠습니다.

```python
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
      <td>1769</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
      <td>1985</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
      <td>1990</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>

## 열 값의 데이터 타입 확인하기

```python
print(df.Weight.dtype)
```

```sh
    dtype('int64')
```

```python
df['Birth Year'].dtype # 문자열 객체를 반환합니다. 이것을 숫자로 변경해야 합니다

```

```python
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # 이제 데이터 타입을 확인해 보겠습니다
```

```sh
    dtype('int32')
```

현재 연도도 마찬가지입니다:

```python
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype
```

```sh
    dtype('int32')
```

이제, 출생 연도와 현재 연도의 열 값이 정수입니다. 나이를 계산할 수 있습니다.

```python
ages = df['Current Year'] - df['Birth Year']
ages
```

    0    251
    1     35
    2     30
    dtype: int32

```python
df['Ages'] = ages
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
      <td>1769</td>
      <td>2019</td>
      <td>250</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
      <td>1985</td>
      <td>2019</td>
      <td>34</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
      <td>1990</td>
      <td>2019</td>
      <td>29</td>
    </tr>
  </tbody>
</table>

첫 번째 행의 사람은 지금까지 251년을 살았습니다. 누군가가 그렇게 오래 사는 것은 있을 수 없는 일입니다. 오타이거나 데이터가 조작된 것입니다. 따라서 이상치를 제외하고 열의 평균값으로 해당 데이터를 채워 보겠습니다.

mean = (35 + 30)/ 2

```python
mean = (35 + 30)/ 2
print('Mean: ',mean)	#출력에 설명을 추가하면 무엇이 무엇인지 알 수 있어 좋습니다
```

```sh
   Mean:  32.5
```

### 불리언 인덱싱

```python
print(df[df['Ages'] > 120])
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
      <td>1769</td>
      <td>2020</td>
      <td>251</td>
    </tr>
  </tbody>
</table>


```python
print(df[df['Ages'] < 120])
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
      <td>1985</td>
      <td>2020</td>
      <td>35</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
      <td>1990</td>
      <td>2020</td>
      <td>30</td>
    </tr>
  </tbody>
</table>

## 연습문제: Day 25

1. data 디렉토리에서 hacker_news.csv 파일을 읽으세요
1. 처음 5개의 행을 가져오세요
1. 마지막 5개의 행을 가져오세요
1. title 열을 pandas series로 가져오세요
1. 행과 열의 수를 세어 보세요
    - python이 포함된 제목을 필터링하세요
    - JavaScript가 포함된 제목을 필터링하세요
    - 데이터를 탐색하고 의미를 파악하세요

🎉 축하합니다! 🎉

[<< Day 24](../24_Day_Statistics/24_statistics.md) | [Day 26 >>](../26_Day_Python_web/26_python_web.md)

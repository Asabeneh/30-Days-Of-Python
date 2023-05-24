<div align="center">
  <h1> 30 дней Python: День 25 - Библиотека Pandas </h1>
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

[<< День 24](../24_Day_Statistics/24_statistics.md) | [День 26 >>](../26_Day_Python_web/26_python_web.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 День 25](#день-25)
  - [Библиотека Pandas](#библиотека-pandas)
    - [Установка библиотеки Pandas](#установка-библиотеки-pandas)
    - [Импорт библиотеки Pandas](#импорт-библиотеки-pandas)
    - [Создание Pandas Series с индексом по умолчанию](#создание-pandas-series-с-индексом-по-умолчанию)
    - [Создание Pandas Series с пользовательским индексом](#создание-pandas-series-с-пользовательским-индексом)
    - [Создание Pandas Series из словаря](#создание-pandas-series-из-словаря)
    - [Создание постоянной Pandas Series](#создание-постоянной-pandas-series)
    - [Создание Pandas Series с использованием linspace](#создание-pandas-series-с-использованием-linspace)
  - [DataFrames](#dataframes)
    - [Создание DataFrame из списка списков](#создание-dataframe-из-списка-списков)
    - [Создание DataFrame с использованием словаря](#создание-dataframe-с-использованием-словаря)
    - [Создание DataFrame из списка словарей](#создание-dataframe-из-списка-словарей)
  - [Чтение CSV-файла с помощью Pandas](#чтение-csv-файла-с-помощью-pandas)
    - [Исследование данных](#исследование-данных)
  - [Изменение DataFrame](#изменение-dataframe)
    - [Создание DataFrame](#создание-dataframe)
    - [Добавление нового столбца](#добавление-нового-столбца)
    - [Изменение значений столбцов](#изменение-значений-столбцов)
    - [Форматирование столбцов DataFrame](#форматирование-столбцов-dataframe)
  - [Проверка типов данных значений столбцов](#проверка-типов-данных-значений-столбцов)
    - [Логическое (Boolean) индексирование](#логическое-(boolean)-индексирование)
  - [Упражнения: День 25](#упражнения-день-25)
  
# 📘 День 25

## Библиотека Pandas

Pandas - это библиотека с открытым исходным кодом, обеспечивающая высокую производительность и простоту использования для работы с данными и анализа данных в языке программирования Python.
Pandas добавляет структуры данных и инструменты, специально разработанные для работы с табличными данными, такими как *Series* и *DataFrames*.
Pandas предоставляет инструменты для манипуляции данными, включая: 

- изменение формы данных (reshaping)
- объединение данных (merging)
- сортировку данных (sorting)
- выборку данных (slicing)
- агрегацию данных (aggregation)
- заполнение пропущенных значений (imputation).
Если вы используете Anaconda, вам не нужно устанавливать pandas, так как она включена в состав Anaconda по умолчанию.

### Установка библиотеки Pandas

Для Mac:
```py
pip install conda
conda install pandas
```

Для Windows:
```py
pip install conda
pip install pandas
```

Структура данных в Pandas основана на *Series* и *DataFrames*. 

*Series* представляет собой *столбец*, а *DataFrame* представляет собой *многомерную таблицу*, состоящую из коллекции *Series*. Чтобы создать *Series* в Pandas, мы можем использовать библиотеку NumPy для создания одномерных массивов или использовать обычный список в Python.
Давайте рассмотрим пример:

Names Series

![pandas series](../images/pandas-series-1.png) 

Countries Series

![pandas series](../images/pandas-series-2.png) 

Cities Series

![pandas series](../images/pandas-series-3.png)

Как видно, серия в Pandas представляет собой всего лишь один столбец данных. Если мы хотим иметь несколько столбцов, мы используем DataFrames. Приведенный ниже пример демонстрирует использование DataFrame в Pandas.

Давайте рассмотрим пример использования Pandas DataFrame:

![Pandas data frame](../images/pandas-dataframe-1.png)

DataFrame представляет собой коллекцию строк и столбцов. Посмотрите на таблицу ниже; она имеет гораздо больше столбцов, чем пример выше:

![Pandas data frame](../images/pandas-dataframe-2.png)

Далее мы рассмотрим, как импортировать библиотеку Pandas и как создавать серии (Series) и таблицы данных (DataFrames) с использованием Pandas.

### Импорт библиотеки Pandas

```python
import pandas as pd # импорт библиотеки pandas под псевдонимом pd
import numpy  as np # импорт библиотеки numpy под псевдонимом np
```

### Создание Pandas Series с индексом по умолчанию

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

### Создание Pandas Series с пользовательским индексом

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

### Создание Pandas Series из словаря

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

### Создание постоянной Pandas Series

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

### Создание Pandas Series с использованием linspace

```python
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
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

DataFrames в Pandas можно создавать различными способами.

### Создание DataFrame из списка списков

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

### Создание DataFrame с использованием словаря

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

### Создание DataFrame из списка словарей

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

## Чтение CSV-файла с помощью Pandas

Чтобы скачать файл CSV, который используется в данном примере, достаточно использовать консоль или командную строку:

```sh
curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
```

Положите загруженный CSV-файл в вашу рабочую директорию.

```python
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
```

### Исследование данных

Давайте прочитаем только первые 5 строк, используя метод head():

```python
print(df.head()) # выведем первые пять строк; мы можем увеличить количество строк, передав аргумент в метод head()
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

Давайте также рассмотрим последние записи в DataFrame с помощью метода tail():

```python
print(df.tail()) # выведем последние пять строк; мы можем увеличить количество строк, передав аргумент в метод tail()
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

Как видно из CSV-файла, у нас есть три строки: Gender (Пол), Height (Рост) и Weight (Вес). Если DataFrame имеет большее количество строк, то может быть сложно держать на виду весь столбец сразу. Поэтому мы должны использовать метод для определения размера столбцов.Давайте воспользуемся методом shape().

```python
print(df.shape) # как вы можете видеть, dataframe имеет 10000 строк и три столбца
```

    (10000, 3)

Давайте получим все столбцы с помощью атрибута columns:

```python
print(df.columns)
```

    Index(['Gender', 'Height', 'Weight'], dtype='object')

Теперь давайте получим определенный столбец, используя его название (ключ):

```python
heights = df['Height'] # это теперь объект серии (series)
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
weights = df['Weight'] # это теперь объект серии (series)
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

Метод describe() предоставляет описательные статистические значения набора данных.

```python
print(heights.describe()) # статистическая информация столбец (height)
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
print(df.describe())  # метод describe() также может предоставлять статистическую информацию о dataframe в целом
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

Аналогично методу describe(), метод info() также предоставляет информацию о наборе данных:

## Изменение DataFrame

Изменение DataFrame:
    * Мы можем создать новый DataFrame,
    * Мы можем создать новый столбец и добавить его в DataFrame,
    * Мы можем удалить существующий столбец из DataFrame, 
    * Мы можем изменить существующий столбец в DataFrame, 
    * Мы можем изменить тип данных значений столбца в DataFrame.

### Создание DataFrame

Как всегда, первым делом мы импортируем необходимые пакеты. Давайте импортируем двух неразлучных друзей - pandas и numpy.

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

Добавление столбца в DataFrame аналогично добавлению ключа в словарь.

Давайте сначала используем предыдущий пример, чтобы создать DataFrame. После создания DataFrame мы начнем изменять столбцы и значения в них.

### Добавление нового столбца

Давайте добавим столбец "Weight" в DataFrame:

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

Давайте также добавим столбец "Height":

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

Как видно из приведенного выше DataFrame, мы добавили новые столбцы "Weight" и "Height". Давайте также добавим дополнительный столбец с именем "BMI" (Индекс массы тела), вычислив его значение на основе массы и роста. Индекс массы тела (ИМТ) рассчитывается как отношение массы квадрата роста (в метрах) - Вес/Рост * Рост.

Как видно, рост указан в сантиметрах, поэтому мы должны перевести его в метры. Давайте изменим столбец с ростом "Height".

### Изменение значений столбцов

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
# Использование функций делает наш код более читабельным, но вы также можете вычислить индекс массы тела без использования функции
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

### Форматирование столбцов DataFrame

Значения столбца "BMI" в DataFrame являются числами с плавающей точкой с большим количеством значащих цифр после запятой. Давайте изменим их, чтобы они имели одну значащую цифру после запятой.

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

Информация в DataFrame, кажется неполной, давайте добавим столбцы "Birth Year" (год рождения) и "Current Year" (текущий год).

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

## Проверка типов данных значений столбцов

```python
print(df.Weight.dtype)
```

```sh
    dtype('int64')
```

```python
df['Birth Year'].dtype # возвращает объект типа "строка", нам следует преобразовать его в число

```

```python
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # давайте проверим тип данных
```

```sh
    dtype('int32')
```

Теперь то же самое для текущего года (current year):

```python
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype
```

```sh
    dtype('int32')
```

Теперь значения столбцов "год рождения" и "текущий год" являются целыми числами. Мы можем вычислить возраст.

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

Человек в первой строке жил 251 год. Вряд ли кто-то может прожить так долго. Возможно, это ошибка или данные искажены. Поэтому давайте заполним эти данные средним значением столбцов, исключив выбросы.

Среднее значение будет равно (35 + 30) / 2:

```python
mean = (35 + 30)/ 2
print('Mean: ',mean)	#считается правилом хорошего тона добавлять некоторое описание вывода, чтобы мы знали, что это такое.
```

```sh
   Mean:  32.5
```

### Логическое (Boolean) индексирование

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

## Упражнения: День 25

1. Прочитать файл hacker_news.csv из директории "data"
2. Получить первые пять строк
3. Получить последние пять строк
4. Получить столбец "title" в виде серии (pandas series)
5. Посчитать количество строк и столбцов
    - Отфильтровать заголовки, содержащие "python"
    - Отфильтровать заголовки, содержащие "JavaScript"
    - Исследовать данные и понять их смысл

🎉 МОИ ПОЗДРАВЛЕНИЯ ! 🎉

[<< День 24](../24_Day_Statistics/24_statistics.md) | [День 26 >>](../26_Day_Python_web/26_python_web.md)

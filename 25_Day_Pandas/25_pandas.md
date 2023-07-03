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

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 25](#-day-25)
  - [Pandas](#pandas)
    - [ការដំឡើង Pandas](#installing-pandas)
    - [ការនាំចូល Pandas](#importing-pandas)
    - [ការបង្កើតស៊េរី "Pandas" ជាមួយសន្ទស្សន៍លំនាំដើម](#creating-pandas-series-with-default-index)
    - [ការបង្កើតស៊េរី "Pandas" ជាមួយនឹងសន្ទស្សន៍ផ្ទាល់ខ្លួន](#creating--pandas-series-with-custom-index)
    - [ការបង្កើតស៊េរី "Pandas" ពីវចនានុក្រម](#creating-pandas-series-from-a-dictionary)
    - [ការបង្កើតស៊េរី "Pandas" ថេរ](#creating-a-constant-pandas-series)
    - [ការបង្កើតស៊េរី "Pandas" ដោយប្រើ Linspace](#creating-a--pandas-series-using-linspace)
  - [DataFrames](#dataframes)
    - [ការបង្កើត "DataFrames" ពីបញ្ជីបញ្ជី](#creating-dataframes-from-list-of-lists)
    - [ការបង្កើត "DataFrames" ដោយប្រើវចនានុក្រម](#creating-dataframe-using-dictionary)
    - [ការបង្កើត DataFrames ពីបញ្ជីវចនានុក្រម](#creating-dataframes-from-a-list-of-dictionaries)
  - [ការអានឯកសារ CSV ដោយប្រើ Pandas](#reading-csv-file-using-pandas)
    - [ការរុករកទិន្នន័យ](#data-exploration)
  - [ការកែប្រែ DataFrame](#modifying-a-dataframe)
    - [ការបង្កើត DataFrame](#creating-a-dataframe)
    - [ការបន្ថែមជួរឈរថ្មី។](#adding-a-new-column)
    - [ការកែប្រែតម្លៃជួរឈរ](#modifying-column-values)
    - [ការធ្វើទ្រង់ទ្រាយជួរឈរ DataFrame](#formating-dataframe-columns)
  - [ពិនិត្យមើលប្រភេទទិន្នន័យនៃតម្លៃជួរឈរ](#checking-data-types-of-column-values)
    - [សន្ទស្សន៍ប៊ូលីន](#boolean-indexing)
  - [Exercises: Day 25](#exercises-day-25)
  
# 📘 Day 25

## Pandas

Pandas គឺជាប្រភពបើកចំហ ដំណើរការខ្ពស់ ងាយស្រួលប្រើ រចនាសម្ព័ន្ធទិន្នន័យ និងឧបករណ៍វិភាគទិន្នន័យសម្រាប់ភាសាសរសេរកម្មវិធី Python ។
Pandas បន្ថែមរចនាសម្ព័ន្ធទិន្នន័យ និងឧបករណ៍ដែលត្រូវបានរចនាឡើងដើម្បីធ្វើការជាមួយទិន្នន័យដូចតារាងដែលជា *ស៊េរី* និង *ស៊ុមទិន្នន័យ*។
Pandas ផ្តល់ឧបករណ៍សម្រាប់រៀបចំទិន្នន័យ៖

- កែទម្រង់
- ការរួមបញ្ចូលគ្នា
- តម្រៀប
- ចំណិត
- ការប្រមូលផ្តុំ
- ការកាត់ទោស។

ប្រសិនបើអ្នកកំពុងប្រើ anaconda អ្នកមិនមានដំឡើង pandas ទេ។

### ការដំឡើង Pandas

សម្រាប់ Mac:
```py
pip install conda
conda install pandas
```

សម្រាប់ Windows:
```py
pip install conda
pip install pandas
```

រចនាសម្ព័ន្ធទិន្នន័យ Pandas គឺផ្អែកលើ *ស៊េរី* និង *DataFrames*។

A *series* គឺជា *column* ហើយ DataFrame គឺជា *តារាងពហុវិមាត្រ* ដែលបង្កើតឡើងដោយបណ្តុំនៃ *series*។ ដើម្បីបង្កើតស៊េរីផេនដា យើងគួរប្រើ numpy ដើម្បីបង្កើតអារេវិមាត្រមួយ ឬបញ្ជី python ។
តោះមើលឧទាហរណ៍នៃស៊េរី៖

Names Pandas Series

![pandas series](../images/pandas-series-1.png) 

Countries Series

![pandas series](../images/pandas-series-2.png) 

Cities Series

![pandas series](../images/pandas-series-3.png)

ដូចដែលអ្នកអាចឃើញស៊េរីផេនដាគឺគ្រាន់តែជាជួរឈរមួយនៃទិន្នន័យប៉ុណ្ណោះ។ ប្រសិនបើយើងចង់មានជួរឈរច្រើន យើងប្រើស៊ុមទិន្នន័យ។ ឧទាហរណ៍ខាងក្រោមបង្ហាញពីផេនដា DataFrames ។

តោះមើលឧទាហរណ៍នៃស៊ុមទិន្នន័យខ្លាឃ្មុំផេនដា៖

![Pandas data frame](../images/pandas-dataframe-1.png)

ស៊ុមទិន្នន័យគឺជាបណ្តុំនៃជួរដេក និងជួរឈរ។ សូមមើលតារាងខាងក្រោម; វាមានជួរឈរច្រើនលើសពីឧទាហរណ៍ខាងលើ៖

![Pandas data frame](../images/pandas-dataframe-2.png)

បន្ទាប់ យើងនឹងឃើញពីរបៀបនាំចូលផេនដា និងរបៀបបង្កើត Series និង DataFrames ដោយប្រើផេនដា

### ការនាំចូល Pandas

```python
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np
```

### ការបង្កើតស៊េរី Pandas ជាមួយសន្ទស្សន៍លំនាំដើម

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

### ការបង្កើតស៊េរី Pandas ជាមួយនឹងសន្ទស្សន៍ផ្ទាល់ខ្លួន

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

### ការបង្កើតស៊េរី Pandas ពីវចនានុក្រម

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

### ការបង្កើតស៊េរី Pandas ថេរ

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

### ការបង្កើតស៊េរី Pandas ដោយប្រើ Linspace

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

ស៊ុមទិន្នន័យ Pandas អាចត្រូវបានបង្កើតតាមវិធីផ្សេងៗគ្នា។

### ការបង្កើត DataFrames ពីបញ្ជីរាយនាម

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

### ការបង្កើត DataFrame ដោយប្រើវចនានុក្រម

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

### ការបង្កើត DataFrames ពីបញ្ជីវចនានុក្រម

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

## ការអានឯកសារ CSV ដោយប្រើ Pandas

ដើម្បីទាញយកឯកសារ CSV អ្វីដែលត្រូវការក្នុងឧទាហរណ៍នេះ កុងសូល/បន្ទាត់ពាក្យបញ្ជាគឺគ្រប់គ្រាន់ហើយ៖

```sh
curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
```

ដាក់ឯកសារដែលបានទាញយកនៅក្នុងថតការងាររបស់អ្នក។

```python
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
```

### Data Exploration

អនុញ្ញាតឱ្យយើងអានតែ 5 ជួរដំបូងដោយប្រើ head()

```python
print(df.head()) # give five rows we can increase the number of rows by passing argument to the head() method
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

អនុញ្ញាតឱ្យយើងរុករកផងដែរនូវការកត់ត្រាចុងក្រោយនៃស៊ុមទិន្នន័យដោយប្រើវិធី tail() ។

```python
print(df.tail()) # tails ផ្តល់ឱ្យប្រាំជួរចុងក្រោយ យើងអាចបង្កើនជួរដេកដោយឆ្លងកាត់អាគុយម៉ង់ទៅវិធីសាស្ត្រ "tail"
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

ដូចដែលអ្នកអាចឃើញឯកសារ csv មានបីជួរ៖ ភេទ កម្ពស់ និងទម្ងន់។ ប្រសិនបើ DataFrame នឹងមានជួរវែង វានឹងពិបាកក្នុងការដឹងពីជួរឈរទាំងអស់។ ដូច្នេះ​ហើយ យើង​គួរ​ប្រើ​វិធី​ដើម្បី​ស្គាល់​កូឡុំ។ យើងមិនដឹងចំនួនជួរដេកទេ។ តោះប្រើសាច់ក្រករាង។

```python
print(df.shape) # ដូចដែលអ្នកអាចមើលឃើញ 10000 ជួរនិងជួរឈរបី
```

    (10000, 3)

អនុញ្ញាតឱ្យយើងទទួលបានជួរឈរទាំងអស់ដោយប្រើជួរឈរ។

```python
print(df.columns)
```

    Index(['Gender', 'Height', 'Weight'], dtype='object')

ឥឡូវនេះ អនុញ្ញាតឱ្យយើងទទួលបានជួរឈរជាក់លាក់មួយដោយប្រើគ្រាប់ចុចជួរឈរ

```python
heights = df['Height'] # ឥឡូវនេះនេះគឺជាស៊េរី
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
weights = df['Weight'] # ឥឡូវនេះនេះគឺជាស៊េរី
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

វិធីសាស្ត្រ describe() ផ្តល់នូវតម្លៃស្ថិតិពិពណ៌នានៃសំណុំទិន្នន័យ។

```python
print(heights.describe()) # ផ្តល់ព័ត៌មានស្ថិតិអំពីទិន្នន័យកម្ពស់

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
print(df.describe())  # ពិពណ៌នាក៏អាចផ្តល់ព័ត៌មានស្ថិតិពី dataFrame ផងដែរ។
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

ស្រដៀងនឹង describe() វិធីសាស្ត្រ info() ក៏ផ្តល់ព័ត៌មានអំពីសំណុំទិន្នន័យផងដែរ។

## Modifying a DataFrame

ការកែប្រែ DataFrame៖
     * យើងអាចបង្កើត DataFrame ថ្មី។
     * យើងអាចបង្កើតជួរឈរថ្មី ហើយបន្ថែមវាទៅ DataFrame,
     * យើងអាចដកជួរឈរដែលមានស្រាប់ចេញពី DataFrame,
     * យើងអាចកែប្រែជួរឈរដែលមានស្រាប់នៅក្នុង DataFrame,
     * យើងអាចផ្លាស់ប្តូរប្រភេទទិន្នន័យនៃតម្លៃជួរឈរក្នុង DataFrame

### Creating a DataFrame

ដូចរាល់ដង ជាដំបូងយើងនាំចូលកញ្ចប់ចាំបាច់។ ឥលូវនេះសូមនាំផេនដា និង នឹមភី ដែលជាមិត្តភ័ក្តិល្អពីរនាក់ដែលធ្លាប់មាន។

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

ការបន្ថែមជួរឈរទៅ DataFrame គឺដូចជាការបន្ថែមកូនសោទៅវចនានុក្រម។

ជាដំបូង ចូរយើងប្រើឧទាហរណ៍មុនដើម្បីបង្កើត DataFrame ។ បន្ទាប់ពីយើងបង្កើត DataFrame យើងនឹងចាប់ផ្តើមកែប្រែតម្លៃជួរឈរ និងតម្លៃជួរឈរ។

### Adding a New Column

ចូរយើងបន្ថែមជួរឈរទម្ងន់នៅក្នុង DataFrame

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

ចូរបន្ថែមជួរឈរកម្ពស់ទៅក្នុង DataFrame ផងដែរ។

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

ដូចដែលអ្នកអាចឃើញនៅក្នុង DataFrame ខាងលើ យើងបានបន្ថែមជួរឈរថ្មី ទម្ងន់ និងកម្ពស់។ ចូរបន្ថែមជួរឈរមួយបន្ថែមទៀតដែលហៅថា BMI (សន្ទស្សន៍ម៉ាសរាងកាយ) ដោយគណនា BMI របស់ពួកគេដោយប្រើម៉ាស់ និងកម្ពស់។ BMI ត្រូវបានបែងចែកដោយកម្ពស់ការ៉េ (គិតជាម៉ែត្រ) - ទំងន់ / កម្ពស់ * កម្ពស់។

ដូចដែលអ្នកអាចឃើញកម្ពស់គិតជាសង់ទីម៉ែត្រដូច្នេះយើងគួរតែប្តូរវាទៅជាម៉ែត្រ។ តោះកែប្រែជួរកម្ពស់។

### ការកែប្រែតម្លៃជួរឈរ

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
# ការប្រើប្រាស់មុខងារធ្វើឱ្យកូដរបស់យើងស្អាត ប៉ុន្តែអ្នកអាចគណនា bmi ដោយគ្មានលេខ
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

### ការធ្វើទ្រង់ទ្រាយជួរឈរ DataFrame

តម្លៃជួរឈរ BMI នៃ DataFrame គឺអណ្តែតដោយមានខ្ទង់សំខាន់ៗជាច្រើនបន្ទាប់ពីទសភាគ។ ចូរប្តូរវាទៅជាខ្ទង់សំខាន់មួយបន្ទាប់ពីចំនុច។

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

ព័ត៌មាននៅក្នុង DataFrame ហាក់ដូចជាមិនទាន់ពេញលេញនៅឡើយ សូមបន្ថែមឆ្នាំកំណើត និងជួរឈរឆ្នាំបច្ចុប្បន្ន។

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

## កំពុងពិនិត្យមើលប្រភេទទិន្នន័យនៃតម្លៃជួរឈរ

```python
print(df.Weight.dtype)
```

```sh
    dtype('int64')
```

```python
df['Birth Year'].dtype # វាផ្តល់ឱ្យ string object យើងគួរតែប្តូរវាទៅជាលេខ
```

```python
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # សូមពិនិត្យមើលប្រភេទទិន្នន័យឥឡូវនេះ
```

```sh
    dtype('int32')
```

ឥឡូវនេះដូចគ្នាសម្រាប់ឆ្នាំបច្ចុប្បន្ន៖

```python
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype
```

```sh
    dtype('int32')
```

ឥឡូវនេះ តម្លៃជួរឈរនៃឆ្នាំកំណើត និងឆ្នាំបច្ចុប្បន្នគឺជាចំនួនគត់។ យើងអាចគណនាអាយុបាន។

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

អ្នក​នៅ​ជួរ​ទី​មួយ​បាន​រស់​នៅ​រហូត​មក​ដល់​ពេល​នេះ​អស់​រយៈ​ពេល ២៥១ ឆ្នាំ។ វាមិនទំនងសម្រាប់នរណាម្នាក់រស់នៅបានយូរនោះទេ។ ទាំងវាជាកំហុស ឬទិន្នន័យត្រូវបានចម្អិន។ ដូច្នេះអនុញ្ញាតឱ្យបំពេញទិន្នន័យនោះជាមួយនឹងមធ្យមនៃជួរឈរដោយមិនរាប់បញ្ចូលខាងក្រៅ។

mean = (35 + 30)/ 2

```python
mean = (35 + 30)/ 2
print('Mean: ',mean)	#វាជាការល្អក្នុងការបន្ថែមការពិពណ៌នាខ្លះទៅលទ្ធផល ដូច្នេះយើងដឹងថាអ្វីជាអ្វី
```

```sh
   Mean:  32.5
```

### Boolean Indexing

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

## Exercises: Day 25

1. អានឯកសារ hacker_news.csv ពីថតទិន្នន័យ
1. ទទួលបានប្រាំជួរដំបូង
1. ទទួលបានប្រាំជួរចុងក្រោយ
1. ទទួលបានជួរឈរចំណងជើងជាស៊េរីផេនដា
1. រាប់ចំនួនជួរដេកនិងជួរឈរ
     - ត្រងចំណងជើងដែលមាន python
     - ត្រងចំណងជើងដែលមាន JavaScript
     - រុករកទិន្នន័យ និងធ្វើឱ្យយល់អំពីវា។

🎉 CONGRATULATIONS ! 🎉

[<< Day 24](../24_Day_Statistics/24_statistics.md) | [Day 26 >>](../26_Day_Python_web/26_python_web.md)

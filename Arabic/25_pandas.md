<div align="center">
  <h1> 30 يومًا من بايثون: اليوم 25 - Pandas </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>المؤلف:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>الطبعة الثانية: يوليو، 2021</small>
  </sub>

</div>

[<< اليوم 24](./24_statistics.md) | [اليوم 26 >>](./26_python_web.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 اليوم 25](#-day-25)
  - [Pandas](#pandas)
    - [تثبيت Pandas](#installing-pandas)
    - [استيراد Pandas](#importing-pandas)
    - [إنشاء سلاسل Pandas مع فهرس افتراضي](#creating-pandas-series-with-default-index)
    - [إنشاء سلاسل Pandas مع فهرس مخصص](#creating--pandas-series-with-custom-index)
    - [إنشاء سلاسل Pandas من قاموس](#creating-pandas-series-from-a-dictionary)
    - [إنشاء سلسلة Pandas ثابتة](#creating-a-constant-pandas-series)
    - [إنشاء سلسلة Pandas باستخدام Linspace](#creating-a--pandas-series-using-linspace)
  - [>DataFrames](#dataframes)
    - [إنشاء DataFrames من قائمة القوائم](#creating-dataframes-from-list-of-lists)
    - [إنشاء DataFrame باستخدام القاموس](#creating-dataframe-using-dictionary)
    - [إنشاء DataFrames من قائمة القواميس](#creating-dataframes-from-a-list-of-dictionaries)
  - [قراءة ملف CSV باستخدام Pandas](#reading-csv-file-using-pandas)
    - [استكشاف البيانات](#data-exploration)
  - [تعديل DataFrame](#modifying-a-dataframe)
    - [إنشاء DataFrame](#creating-a-dataframe)
    - [إضافة عمود جديد](#adding-a-new-column)
    - [تعديل قيم الأعمدة](#modifying-column-values)
    - [تنسيق أعمدة DataFrame](#formatting-dataframe-columns)
  - [فحص أنواع بيانات قيم الأعمدة](#checking-data-types-of-column-values)
    - [الفهرسة المنطقية](#boolean-indexing)
  - [تمارين: اليوم 25](#exercises-day-25)

# 📘 اليوم 25

## Pandas

'Pandas' هو مكتبة مفتوحة المصدر عالية الأداء وسهلة الاستخدام لهياكل البيانات وأدوات تحليل البيانات بلغة البرمجة 'Python'.
تضيف 'Pandas' هياكل بيانات وأدوات مصممة للعمل مع البيانات الشبيهة بالجداول وهي *Series* و*Data Frames*.
توفر 'Pandas' أدوات لمعالجة البيانات:

- إعادة تشكيل
- دمج
- ترتيب
- تقسيم
- تجميع
- ملء النقص
إذا كنت تستخدم 'anaconda'، فلا حاجة لتثبيت 'pandas'.

### تثبيت Pandas

لـ Mac:
```py
pip install conda
conda install pandas
```

لـ Windows:
```py
pip install conda
pip install pandas
```

هيكل بيانات 'Pandas' مبني على *Series* و*DataFrames*.

'السلسلة' هي *عمود* و'الإطار البياناتي' هو *جدول متعدد الأبعاد* مكون من مجموعة من *السلسلات*. لإنشاء سلسلة 'pandas' يجب استخدام 'numpy' لإنشاء مصفوفات أحادية البعد أو قائمة 'python'.
دعنا نرى مثالاً على السلسلة:

سلسلة أسماء Pandas

![pandas series](../images/pandas-series-1.png)

سلسلة البلدان

![pandas series](../images/pandas-series-2.png)

سلسلة المدن

![pandas series](../images/pandas-series-3.png)

كما ترى، سلسلة 'pandas' هي مجرد عمود واحد من البيانات. إذا أردنا الحصول على أعمدة متعددة نستخدم 'DataFrames'. يوضح المثال التالي 'DataFrames' الخاصة بـ 'pandas'.

دعنا نرى مثالاً على إطار بيانات 'pandas':

![Pandas data frame](../images/pandas-dataframe-1.png)

'الإطار البياناتي' هو مجموعة من الصفوف والأعمدة. انظر إلى الجدول أدناه؛ يحتوي على أعمدة أكثر بكثير من المثال أعلاه:

![Pandas data frame](../images/pandas-dataframe-2.png)

بعد ذلك، سنرى كيفية استيراد 'pandas' وكيفية إنشاء 'Series' و'DataFrames' باستخدام 'pandas'

### استيراد Pandas

```python
import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np
```

### إنشاء سلاسل Pandas مع فهرس افتراضي

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

### إنشاء سلاسل Pandas مع فهرس مخصص

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

### إنشاء سلاسل Pandas من قاموس

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

### إنشاء سلسلة Pandas ثابتة

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

### إنشاء سلسلة Pandas باستخدام Linspace

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

يمكن إنشاء أطر البيانات الخاصة بـ 'pandas' بطرق مختلفة.

### إنشاء DataFrames من قائمة القوائم

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

### إنشاء DataFrame باستخدام القاموس

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

### إنشاء DataFrames من قائمة القواميس

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

### قراءة ملف CSV باستخدام Pandas

لتنزيل ملف 'CSV' المطلوب في هذا المثال، يكفي استخدام وحدة التحكم/سطر الأوامر:

```sh
curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
```

ضع الملف المحمل في دليل العمل الخاص بك.

```python
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
```

### استكشاف البيانات

دعنا نقرأ فقط أول 5 صفوف باستخدام 'head()'

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

دعنا أيضًا نستكشف آخر السجلات في الإطار البياناتي باستخدام طريقة 'tail()'

```python
print(df.tail()) # tails give the last five rows, we can increase the rows by passing argument to tail method
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

كما ترى، يحتوي ملف 'csv' على ثلاثة أعمدة: 'Gender' و'Height' و'Weight'. إذا كان 'DataFrame' يحتوي على عدد كبير من الصفوف، فمن الصعب معرفة جميع الأعمدة. لذلك يجب استخدام طريقة لمعرفة الأعمدة. لا نعرف عدد الصفوف. دعنا نستخدم طريقة 'shape'.

```python
print(df.shape) # as you can see 10000 rows and three columns
```

    (10000, 3)

دعنا نحصل على جميع الأعمدة باستخدام 'columns'.

```python
print(df.columns)
```

    Index(['Gender', 'Height', 'Weight'], dtype='object')

الآن، دعنا نحصل على عمود محدد باستخدام مفتاح العمود

```python
heights = df['Height'] # this is now a series
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
weights = df['Weight'] # this is now a series
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

توفر طريقة 'describe()' قيمًا إحصائية وصفية لمجموعة البيانات.

```python
print(heights.describe()) # give statistical information about height data
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
print(df.describe())  # describe can also give statistical information from a dataFrame
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

على غرار 'describe()'، توفر طريقة 'info()' أيضًا معلومات حول مجموعة البيانات.

### تعديل DataFrame

تعديل 'DataFrame':
    * يمكننا إنشاء 'DataFrame' جديد
    * يمكننا إنشاء عمود جديد وإضافته إلى 'DataFrame'
    * يمكننا إزالة عمود موجود من 'DataFrame'
    * يمكننا تعديل عمود موجود في 'DataFrame'
    * يمكننا تغيير نوع بيانات قيم الأعمدة في 'DataFrame'

#### إنشاء DataFrame

كما هو معتاد، نستورد الحزم اللازمة أولاً. الآن، دعنا نستورد 'pandas' و'numpy'، أفضل صديقين على الإطلاق.

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

إضافة عمود إلى 'DataFrame' تشبه إضافة مفتاح إلى قاموس.

أولاً دعنا نستخدم المثال السابق لإنشاء 'DataFrame'. بعد إنشاء 'DataFrame'، سنبدأ بتعديل الأعمدة وقيم الأعمدة.

##### إضافة عمود جديد

دعنا نضيف عمود الوزن في 'DataFrame'

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

دعنا نضيف عمود الارتفاع إلى 'DataFrame' أيضًا

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

كما ترى في 'DataFrame' أعلاه، أضفنا أعمدة جديدة، 'Weight' و'Height'. دعنا نضيف عمودًا إضافيًا يسمى 'BMI' (مؤشر كتلة الجسم) عن طريق حساب 'BMI' الخاص بهم باستخدام كتلتهم وارتفاعهم. 'BMI' هو الكتلة مقسومة على الارتفاع مربعاً (بالمتر) - Weight/Height * Height.

كما ترى، الارتفاع بالسنتيمتر، لذا يجب تغييره إلى أمتار. دعنا نعدّل صف الارتفاع.

##### تعديل قيم الأعمدة

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
# Using functions makes our code clean, but you can calculate the bmi without one
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

##### تنسيق أعمدة DataFrame

قيم عمود 'BMI' في 'DataFrame' هي أرقام عشرية مع العديد من الأرقام المعنوية بعد الفاصلة. دعنا نغيرها إلى رقم معنوي واحد بعد النقطة.

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

تبدو معلومات 'DataFrame' غير مكتملة بعد، دعنا نضيف عمودي 'Birth Year' و'Current Year'.

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

### فحص أنواع بيانات قيم الأعمدة

```python
print(df.Weight.dtype)
```

```sh
    dtype('int64')
```

```python
df['Birth Year'].dtype # it gives string object , we should change this to number

```

```python
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # let's check the data type now
```

```sh
    dtype('int32')
```

الآن نفس الشيء للسنة الحالية:

```python
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype
```

```sh
    dtype('int32')
```

الآن، قيم العمود لسنة الميلاد والسنة الحالية أعداد صحيحة. يمكننا حساب العمر.

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

الشخص في الصف الأول عاش حتى الآن 251 عاماً. من غير المرجح أن يعيش شخص طويلاً هكذا. إما أنه خطأ مطبعي أو البيانات مفبركة. لذا دعنا نملأ تلك البيانات بالمتوسط العمومي للأعمدة مع استبعاد القيم الشاذة.

mean = (35 + 30)/ 2

```python
mean = (35 + 30)/ 2
print('Mean: ',mean)	#it is good to add some description to the output, so we know what is what
```

```sh
   Mean:  32.5
```

##### الفهرسة المنطقية

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

### تمارين: اليوم 25

1. اقرأ ملف 'hacker_news.csv' من دليل 'data'
1. احصل على أول خمسة صفوف
1. احصل على آخر خمسة صفوف
1. احصل على عمود 'title' كسلسلة 'pandas'
1. احسب عدد الصفوف والأعمدة
    - تصف العناوين التي تحتوي على 'python'
    - تصف العناوين التي تحتوي على 'JavaScript'
    - استكشف البيانات واستخرج المعنى منها

🎉 مبروك ! 🎉

[<< اليوم 24](./24_statistics.md) | [اليوم 26 >>](./26_python_web.md)
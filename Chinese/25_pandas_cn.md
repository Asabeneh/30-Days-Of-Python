# 30天Python编程挑战：第25天 - Pandas

- [第25天](#-第25天)
  - [Pandas](#pandas)
    - [安装Pandas](#安装pandas)
    - [导入Pandas](#导入pandas)
    - [使用默认索引创建Pandas系列](#使用默认索引创建pandas系列)
    - [使用自定义索引创建Pandas系列](#使用自定义索引创建pandas系列)
    - [从字典创建Pandas系列](#从字典创建pandas系列)
    - [创建常量Pandas系列](#创建常量pandas系列)
    - [使用Linspace创建Pandas系列](#使用linspace创建pandas系列)
  - [数据框（DataFrames）](#数据框dataframes)
    - [从列表的列表创建数据框](#从列表的列表创建数据框)
    - [使用字典创建数据框](#使用字典创建数据框)
    - [从字典列表创建数据框](#从字典列表创建数据框)
  - [使用Pandas读取CSV文件](#使用pandas读取csv文件)
    - [数据探索](#数据探索)
  - [修改数据框](#修改数据框)
    - [创建数据框](#创建数据框)
    - [添加新列](#添加新列)
    - [修改列值](#修改列值)
    - [格式化数据框列](#格式化数据框列)
  - [检查列值的数据类型](#检查列值的数据类型)
    - [布尔索引](#布尔索引)
  - [练习：第25天](#练习第25天)
  
# 📘 第25天

## Pandas

Pandas是一个开源的、高性能的、易于使用的Python编程语言数据结构和数据分析工具。
Pandas添加了设计用于处理表格数据的数据结构和工具，这些数据结构是*系列（Series）*和*数据框（Data Frames）*。
Pandas提供了用于数据操作的工具：

- 重塑
- 合并
- 排序
- 切片
- 聚合
- 插补
如果你使用的是anaconda，则不必安装pandas。

### 安装Pandas

对于Mac：
```py
pip install conda
conda install pandas
```

对于Windows：
```py
pip install conda
pip install pandas
```

Pandas数据结构基于*系列（Series）*和*数据框（DataFrames）*。

*系列*是一个*列*，而数据框是由*系列*集合组成的*多维表*。为了创建pandas系列，我们应该使用numpy创建一维数组或Python列表。
让我们看一个系列的例子：

名称Pandas系列

![pandas series](../images/pandas-series-1.png) 

国家系列

![pandas series](../images/pandas-series-2.png) 

城市系列

![pandas series](../images/pandas-series-3.png)

如你所见，pandas系列只是一列数据。如果我们想要有多列，我们使用数据框。下面的例子显示了pandas数据框。

让我们看一个pandas数据框的例子：

![Pandas data frame](../images/pandas-dataframe-1.png)

数据框是行和列的集合。看看下面的表格；它比上面的例子有更多的列：

![Pandas data frame](../images/pandas-dataframe-2.png)

接下来，我们将看到如何导入pandas以及如何使用pandas创建系列和数据框

### 导入Pandas

```python
import pandas as pd # 将pandas导入为pd
import numpy  as np # 将numpy导入为np
```

### 使用默认索引创建Pandas系列

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

### 使用自定义索引创建Pandas系列

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

### 从字典创建Pandas系列

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

### 创建常量Pandas系列

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

### 使用Linspace创建Pandas系列

```python
s = pd.Series(np.linspace(5, 20, 10)) # linspace(起始点, 终点, 项目数)
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

## 数据框（DataFrames）

Pandas数据框可以以不同的方式创建：

- 从列表的列表创建
- 从字典创建
- 从字典的列表创建
- 从CSV文件创建

### 从列表的列表创建数据框

```python
data = [
    ['Asabeneh', 'Finland', 'Helsinki'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Name', 'Country', 'City'])
print(df)
```

```sh
        Name Country      City
0   Asabeneh Finland  Helsinki
1      David      UK    London
2       John  Sweden Stockholm
```

### 使用字典创建数据框

```python
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsinki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)
```

```sh
        Name Country      City
0   Asabeneh Finland  Helsinki
1      David      UK    London
2       John  Sweden Stockholm
```

### 从字典列表创建数据框

```python
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
```

```sh
        Name Country      City
0   Asabeneh Finland  Helsinki
1      David      UK    London
2       John  Sweden Stockholm
```

## 使用Pandas读取CSV文件

让我们在数据目录中读取文件，将通过将文件路径作为参数传递给pd.read_csv()函数来读取weight-height.csv文件。让我们使用head()方法查看前五行。

```python
import pandas as pd

df = pd.read_csv('./data/weight-height.csv')
print(df.head()) # 默认为前五行
```

```sh
   Gender     Height      Weight
0    Male  73.847017  241.893563
1    Male  68.781904  162.310473
2    Male  74.110105  212.740856
3    Male  71.730978  220.042470
4    Male  69.881796  206.349801
```

让我们使用tail()方法查看最后五行：

```python
print(df.tail()) # 最后五行
```

```sh
      Gender     Height      Weight
9995  Female  66.172652  136.777454
9996  Female  67.067155  170.867906
9997  Female  63.867992  128.475319
9998  Female  69.034243  163.852461
9999  Female  61.944246  113.649103
```

### 数据探索

让我们使用shape属性获取行和列的数量：
```python
print(df.shape) # 行和列的数量
```

```sh
(10000, 3)
```

如你所见，该数据集有10000行和3列。让我们获取有关数据的更多信息：

```python
print(df.columns) # 列名
print(df.head(10)) # 前10行
print(df.tail(10)) # 最后10行
print(df['Gender'].value_counts()) # 计算每个值有多少个
print(df.describe()) # 数据统计概要
```

```sh
Index(['Gender', 'Height', 'Weight'], dtype='object')
   Gender     Height      Weight
0    Male  73.847017  241.893563
1    Male  68.781904  162.310473
2    Male  74.110105  212.740856
3    Male  71.730978  220.042470
4    Male  69.881796  206.349801
5    Male  68.767792  152.212156
6    Male  67.961960  183.927889
7    Male  68.563817  175.929316
8    Male  71.267570  196.028855
9    Male  72.040119  205.801386
      Gender     Height      Weight
9990  Female  64.744846  139.725595
9991  Female  62.109532  132.451630
9992  Female  62.593008  130.727432
9993  Female  62.100222  131.220717
9994  Female  63.421888  133.330246
9995  Female  66.172652  136.777454
9996  Female  67.067155  170.867906
9997  Female  63.867992  128.475319
9998  Female  69.034243  163.852461
9999  Female  61.944246  113.649103
Gender
Male      5000
Female    5000
Name: count, dtype: int64
            Height        Weight
count  10000.000000  10000.000000
mean      66.367560    161.440357
std        3.847528     32.108439
min       54.263133     64.700127
25%       63.505620    135.818051
50%       66.318070    161.212928
75%       69.174262    187.169525
max       78.998742    269.989699
```

## 修改数据框

### 创建数据框

首先，让我们使用前面学到的内容创建一个数据框：

```python
# 导入pandas包
import pandas as pd
# 导入numpy包
import numpy as np
# 数据
data = [
    {"Name": "张三", "Country":"中国", "City":"上海"},
    {"Name": "李四", "Country":"中国", "City":"北京"},
    {"Name": "王五", "Country":"中国", "City":"广州"}]
# 创建一个数据框
df = pd.DataFrame(data)
print(df)
```

```sh
    Name Country City
0   张三    中国   上海
1   李四    中国   北京
2   王五    中国   广州
```

### 添加新列

让我们向DataFrame添加权重列：

```python
weights = [74, 78, 69]
df['Weight'] = weights
df
```

```sh
    Name Country City  Weight
0   张三    中国   上海      74
1   李四    中国   北京      78
2   王五    中国   广州      69
```

让我们添加一个高度列：

```python
heights = [173, 175, 169]
df['Height'] = heights
df
```

```sh
    Name Country City  Weight  Height
0   张三    中国   上海      74     173
1   李四    中国   北京      78     175
2   王五    中国   广州      69     169
```

### 修改列值

我们可以通过三种方式修改列：

1. 直接在列名中写入新数据：

```python
df['Name'] = ['赵六', '钱七', '孙八']
df
```

```sh
    Name Country City  Weight  Height
0   赵六    中国   上海      74     173
1   钱七    中国   北京      78     175
2   孙八    中国   广州      69     169
```

2. 通过索引进行修改：

```python
df.loc[1, 'Name'] = '小七'
df
```

```sh
    Name Country City  Weight  Height
0   赵六    中国   上海      74     173
1   小七    中国   北京      78     175
2   孙八    中国   广州      69     169
```

通过iloc索引：

```python
print('原始数据：\n', df)
df.iloc[1, 0] = '阿七'
print('修改后的数据：\n', df)
```

```sh
原始数据：
     Name Country City  Weight  Height
0   赵六    中国   上海      74     173
1   小七    中国   北京      78     175
2   孙八    中国   广州      69     169
修改后的数据：
     Name Country City  Weight  Height
0   赵六    中国   上海      74     173
1   阿七    中国   北京      78     175
2   孙八    中国   广州      69     169
```

### 格式化数据框列

让我们使用格式进行修改。强大公式是BMI：体重（kg）/ 身高²（m）。让我们添加一个BMI列：

```python
# 添加身高、体重和BMI列
df['BMI'] = np.round(df['Weight'] / ((df['Height'] * 0.01) ** 2), 2) # 保留两位小数

print(df)
```

```sh
   Name Country City  Weight  Height   BMI
0  赵六    中国   上海      74     173  24.73
1  阿七    中国   北京      78     175  25.47
2  孙八    中国   广州      69     169  24.16
```

## 检查列值的数据类型

我们可以使用dtypes属性检查DataFrame中列的数据类型：

```python
print(df.dtypes)
```

```sh
Name        object
Country     object
City        object
Weight       int64
Height       int64
BMI        float64
dtype: object
```

### 布尔索引

布尔索引或布尔掩码允许您使用条件选择DataFrame中的特定行：

```python
# 创建一个数据框
df = pd.DataFrame({
    'name': ['张三', '李四', '王五', '赵六'],
    'country': ['中国', '美国', '英国', '西班牙'],
    'age': [25, 15, 22, 28],
    '在职': [True, False, True, False]
})

print(df)
```

```sh
  name country  age    在职
0  张三     中国   25   True
1  李四     美国   15  False
2  王五     英国   22   True
3  赵六   西班牙   28  False
```

让我们筛选出年龄大于20岁且在职的人员：

```python
print(df[(df['age'] > 20) & (df['在职'] == True)])
```

```sh
  name country  age   在职
0  张三     中国   25  True
2  王五     英国   22  True
```

## 练习：第25天

1. 阅读[hacker_news.csv](../data/hacker_news.csv)文件并获取前五行
2. 获取标题列
3. 获取行数、列数
4. 获取前十行和最后十行
5. 获取第二行和第四行从第二列到第四列的数据
6. 获取主题为Python的行
7. 获取Python主题行的数量
8. 获取投票数超过200的所有行
9. 按投票数排序数据框
10. 按投票数进行降序排序
11. 过滤掉Python主题并按票数排序

🎉 恭喜！🎉

[<< 第 24 天](./24_statistics_cn.md) | [第 26 天 >>](./26_python_web_cn.md) 
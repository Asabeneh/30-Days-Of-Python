# 30天Python编程挑战：第24天 - 统计

- [第24天](#-第24天)
  - [Python进行统计分析](#python进行统计分析)
  - [统计学](#统计学)
  - [数据](#数据)
  - [统计模块](#统计模块)
- [NumPy](#numpy)
  - [导入NumPy](#导入numpy)
  - [使用NumPy创建数组](#使用numpy创建数组)
    - [创建整型NumPy数组](#创建整型numpy数组)
    - [创建浮点型NumPy数组](#创建浮点型numpy数组)
    - [创建布尔型NumPy数组](#创建布尔型numpy数组)
    - [使用NumPy创建多维数组](#使用numpy创建多维数组)
    - [将NumPy数组转换为列表](#将numpy数组转换为列表)
    - [从元组创建NumPy数组](#从元组创建numpy数组)
    - [NumPy数组的形状](#numpy数组的形状)
    - [NumPy数组的数据类型](#numpy数组的数据类型)
    - [NumPy数组的大小](#numpy数组的大小)
  - [使用NumPy进行数学运算](#使用numpy进行数学运算)
    - [加法](#加法)

# 📘 第24天

## Python进行统计分析

## 统计学

统计学是研究数据的_收集_、_组织_、_显示_、_分析_、_解释_和_呈现_的学科。
统计学是数学的一个分支，建议作为数据科学和机器学习的先决条件。统计学是一个非常广泛的领域，但在本节中，我们将只关注最相关的部分。
完成这个挑战后，你可以进入Web开发、数据分析、机器学习和数据科学的道路。无论你选择哪条路，在你的职业生涯中的某个时刻，你都会得到可能需要处理的数据。拥有一些统计知识将帮助你基于数据做出决策，正如他们所说的_数据会告诉我们_。

## 数据

什么是数据？数据是为某种目的收集和翻译的任何字符集，通常用于分析。它可以是任何字符，包括文本和数字、图片、声音或视频。如果数据没有放在上下文中，对人类或计算机来说都没有任何意义。为了从数据中获取意义，我们需要使用不同的工具来处理数据。

数据分析、数据科学或机器学习的工作流程都是从数据开始的。数据可以由某些数据源提供，也可以创建。有结构化和非结构化数据。

数据可以以小型或大型格式存在。我们将获得的大多数数据类型已在文件处理部分中介绍。

## 统计模块

Python的_statistics_模块提供了用于计算数值数据的数学统计的函数。该模块并不打算与第三方库如NumPy、SciPy或面向专业统计学家的专有全功能统计软件包（如Minitab、SAS和Matlab）竞争。它的目标是达到图形和科学计算器的水平。

# NumPy

在第一部分中，我们将Python定义为一种优秀的通用编程语言，但在其他流行库（如numpy、scipy、matplotlib、pandas等）的帮助下，它成为了一个强大的科学计算环境。

NumPy是Python中科学计算的核心库。它提供了高性能的多维数组对象和用于处理这些数组的工具。

到目前为止，我们一直在使用vscode，但从现在开始，我建议使用Jupyter Notebook。要访问jupyter notebook，让我们安装[anaconda](https://www.anaconda.com/)。如果你使用anaconda，大多数常用的包都已包含在内，如果你已安装anaconda，就不需要再安装这些包。

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy
```

## 导入NumPy

如果你喜欢[jupyter notebook](https://github.com/Asabeneh/data-science-for-everyone/blob/master/numpy/numpy.ipynb)，可以使用它

```py
# 如何导入numpy
import numpy as np
# 如何检查numpy包的版本
print('numpy:', np.__version__)
# 检查可用的方法
print(dir(np))
```

## 使用NumPy创建数组

### 创建整型NumPy数组

```py
# 创建Python列表
python_list = [1,2,3,4,5]

# 检查数据类型
print('Type:', type (python_list)) # <class 'list'>
#
print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 从Python列表创建NumPy(数值Python)数组

numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])
```

### 创建浮点型NumPy数组

使用浮点数据类型参数从列表创建浮点NumPy数组

```py
# Python列表
python_list = [1,2,3,4,5]

numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2) # array([1., 2., 3., 4., 5.])
```

### 创建布尔型NumPy数组

从列表创建布尔NumPy数组

```py
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])
```

### 使用NumPy创建多维数组

一个NumPy数组可能有一个或多个行和列

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

### 将NumPy数组转换为列表

```python
# 我们总是可以使用tolist()将数组转换回Python列表。
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('一维数组:', np_to_list)
print('二维数组: ', numpy_two_dimensional_list.tolist())
```

```sh
<class 'list'>
一维数组: [1, 2, 3, 4, 5]
二维数组:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

### 从元组创建NumPy数组

```py
# 从元组创建NumPy数组
# 在Python中创建元组
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]
```

### NumPy数组的形状

shape方法以元组形式提供数组的形状。第一个是行，第二个是列。如果数组只是一维的，它返回数组的大小。

```py
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('nums的形状: ', nums.shape)
print(numpy_two_dimensional_list)
print('numpy_two_dimensional_list的形状: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10, 11]])
print(three_by_four_array.shape)
```

```sh
[1 2 3 4 5]
nums的形状:  (5,)
[[0 1 2]
 [3 4 5]
 [6 7 8]]
numpy_two_dimensional_list的形状:  (3, 3)
(3, 4)
```

### NumPy数组的数据类型

数据类型的类型：str, int, float, complex, bool, list, None

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

### NumPy数组的大小

在NumPy中，要知道NumPy数组列表中的项目数，我们使用size

```py
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('大小:', numpy_array_from_list.size) # 5
print('大小:', two_dimensional_list.size)  # 9
```

```sh
大小: 5
大小: 9
```

## 使用NumPy进行数学运算

NumPy数组与Python列表不完全相同。要对Python列表进行数学运算，我们必须遍历项目，但NumPy可以不通过循环就进行任何数学运算。
数学运算：

- 加法 (+)
- 减法 (-)
- 乘法 (*)
- 除法 (/)
- 模数 (%)
- 整除 (//)
- 指数 (**)

### 加法

```py
# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('加法: ', numpy_array_from_list + 2)
print('加法: ', np.add(numpy_array_from_list, 2))
```

```sh
原始数组:  [1 2 3 4 5]
加法:  [3 4 5 6 7]
加法:  [3 4 5 6 7]
```

### 减法

```py
# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('减法: ', numpy_array_from_list - 2)
print('减法: ', np.subtract(numpy_array_from_list, 2))
```

```sh
原始数组:  [1 2 3 4 5]
减法:  [-1  0  1  2  3]
减法:  [-1  0  1  2  3]
```

### 乘法

```py
# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('乘法: ', numpy_array_from_list * 2)
print('乘法: ', np.multiply(numpy_array_from_list, 2))
```

```sh
原始数组:  [1 2 3 4 5]
乘法:  [ 2  4  6  8 10]
乘法:  [ 2  4  6  8 10]
```

### 除法

```py
# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('除法: ', numpy_array_from_list / 2)
print('除法: ', np.divide(numpy_array_from_list, 2))
```

```sh
原始数组:  [1 2 3 4 5]
除法:  [0.5 1.  1.5 2.  2.5]
除法:  [0.5 1.  1.5 2.  2.5]
```

### 模数

```py
# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('模数: ', numpy_array_from_list % 2)
print('模数: ', np.mod(numpy_array_from_list, 2))
```

```sh
原始数组:  [1 2 3 4 5]
模数:  [1 0 1 0 1]
模数:  [1 0 1 0 1]
```

### 整除

```py
# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('整除: ', numpy_array_from_list // 2)
print('整除: ', np.floor_divide(numpy_array_from_list, 2))
```

```sh
原始数组:  [1 2 3 4 5]
整除:  [0 1 1 2 2]
整除:  [0 1 1 2 2]
```

### 指数

```py
# 声明
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('原始数组: ', numpy_array_from_list)
print('指数: ', numpy_array_from_list ** 2)
print('指数: ', np.power(numpy_array_from_list, 2))
```

```sh
原始数组:  [1 2 3 4 5]
指数:  [ 1  4  9 16 25]
指数:  [ 1  4  9 16 25]
```

## 检查数据类型

```py
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
```

```sh
int64
float64
bool
```

## 转换类型

我们可以使用astype将数据类型从一种类型转换为另一种类型。让我们将int类型转换为浮点数，浮点数转换为整数，整数转换为布尔型。

```py
numpy_int_arr = np.array([1, 2, 3, 4], dtype='float')
numpy_int_arr.astype('int').dtype
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_float_arr.astype('int').dtype
numpy_int_arr = np.array([-3, -2, 0, 1, 2, 3])
numpy_int_arr.astype('bool').dtype
```

```sh
int64
int64
bool
```

## 多维数组

NumPy的主要优点之一是处理多维数组。我们先构建多维数组。

```py
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('形状: ', two_dimension_array.shape)
print('大小: ', two_dimension_array.size)
print('数据类型: ', two_dimension_array.dtype)
```

```sh
<class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]
 [7 8 9]]
形状:  (3, 3)
大小:  9
数据类型:  int64
```

### 从NumPy中获取项目

```py
# 二维数组
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('第一行:', first_row)
print('第二行:', second_row)
print('第三行: ', third_row)
```

```sh
第一行: [1 2 3]
第二行: [4 5 6]
第三行:  [7 8 9]
```

现在让我们获取每一行的第一项：

```py
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('第一列:', first_column)
print('第二列:', second_column)
print('第三列: ', third_column)
```

```sh
第一列: [1 4 7]
第二列: [2 5 8]
第三列:  [3 6 9]
```

## NumPy数组切片

切片NumPy数组与切片Python列表相似，只是它适用于两个维度（行和列）。让我们先看看如何从NumPy数组中切片项目。

```py
numpy_array_from_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('原始数组：', numpy_array_from_list)

# 第一个参数代表：起始位置
# 第二个参数代表：停止位置
# 第三个参数代表：步长
print('第一个参数代表：起始位置')
print('第二个参数代表：停止位置')
print('第三个参数代表：步长')
# 使用正index
ten_first_items = numpy_array_from_list[0:10]
print('前10项：', ten_first_items)
first_five_items = numpy_array_from_list[:5]
print('前5项：', first_five_items)
last_five_items = numpy_array_from_list[5:]
print('后5项：', last_five_items)
# 使用负index
last_five_items = numpy_array_from_list[-5:]
print('后5项：', last_five_items)
```

```sh
原始数组： [ 1  2  3  4  5  6  7  8  9 10]
第一个参数代表：起始位置
第二个参数代表：停止位置
第三个参数代表：步长
前10项： [ 1  2  3  4  5  6  7  8  9 10]
前5项： [1 2 3 4 5]
后5项： [ 6  7  8  9 10]
后5项： [ 6  7  8  9 10]
```

现在，让我们通过设置步长来访问每个2个项目：

```py
every_two_item = numpy_array_from_list[::2]
print('每隔一项：', every_two_item)
```

```sh
每隔一项： [1 3 5 7 9]
```

让我们反转数组：

```py
reversed_array = numpy_array_from_list[::-1]
print('反转数组：', reversed_array)
```

```sh
反转数组： [10  9  8  7  6  5  4  3  2  1]
```

我们可以在NumPy二维数组上使用切片：

```py
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
print(two_dimension_array)
print(two_dimension_array[1, 1])
print(two_dimension_array[1, 1:3])
print(two_dimension_array[1:3, 1:3])
```

```sh
[[1 2 3]
 [4 5 6]
 [7 8 9]]
5
[5 6]
[[5 6]
 [8 9]]
```

## NumPy连接数组

NumPy提供了连接数组的方法。

```py
first_array = np.array([1, 2, 3])
second_array = np.array([4, 5, 6])
third_array = np.array([7, 8, 9])
print('第一个数组：', first_array)
print('第二个数组：', second_array)
print('第三个数组：', third_array)
```

```sh
第一个数组： [1 2 3]
第二个数组： [4 5 6]
第三个数组： [7 8 9]
```

### 水平连接

```py
horizontal_concat = np.hstack((first_array, second_array, third_array))
print('水平连接：', horizontal_concat)
```

```sh
水平连接： [1 2 3 4 5 6 7 8 9]
```

### 垂直连接

```py
vertical_concat = np.vstack((first_array, second_array, third_array))
print('垂直连接：', vertical_concat)
```

```sh
垂直连接：
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

## 常见NumPy函数

我们看看最常见的NumPy函数：

### 最小值、最大值、平均值、中位数和百分位数

```py
numpy_array_from_list = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('最小值：', numpy_array_from_list.min())
print('最大值：', numpy_array_from_list.max())
print('平均值：', numpy_array_from_list.mean())
```

🎉 恭喜！🎉

[<< 第 23 天](./23_virtual_environment_cn.md) | [第 25 天 >>](./25_pandas_cn.md) 
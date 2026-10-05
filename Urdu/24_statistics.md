<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 24 — شماریات اور NumPy</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../24_Day_Statistics/24_statistics.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 23](./23_virtual_environment.md) | [فہرست](./readme.md) | [اگلا دن: 25](./25_pandas.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 24](#day-24-section-1)
  - [شماریاتی تجزیے کے لیے پائتھن](#day-24-section-2)
  - [شماریات](#day-24-section-3)
  - [ڈیٹا](#day-24-section-4)
  - [statistics ماڈیول](#day-24-section-5)
- [NumPy](#day-24-section-6)
  - [NumPy امپورٹ کرنا](#day-24-section-7)
  - [NumPy array بنانا](#day-24-section-8)
    - [صحیح اعداد کا array](#day-24-section-9)
    - [اعشاری اعداد کا array](#day-24-section-10)
    - [بولین array](#day-24-section-11)
    - [کئی جہتوں والا array](#day-24-section-12)
    - [array کو لسٹ میں بدلنا](#day-24-section-13)
    - [ٹپل سے array بنانا](#day-24-section-14)
    - [array کی شکل](#day-24-section-15)
    - [array کی ڈیٹا قسم](#day-24-section-16)
    - [array کا سائز](#day-24-section-17)
  - [NumPy سے حسابی عمل](#day-24-section-18)
    - [جمع](#day-24-section-19)
    - [تفریق](#day-24-section-20)
    - [ضرب](#day-24-section-21)
    - [تقسیم](#day-24-section-22)
    - [باقی](#day-24-section-23)
    - [فلور ڈویژن](#day-24-section-24)
    - [قوت](#day-24-section-25)
  - [ڈیٹا کی اقسام جانچنا](#day-24-section-26)
    - [قسم تبدیل کرنا](#day-24-section-27)
  - [کئی جہتوں والے arrays](#day-24-section-28)
    - [array کے عناصر حاصل کرنا](#day-24-section-29)
  - [NumPy array کی سلائسنگ](#day-24-section-30)
    - [قطاروں اور پورے array کو الٹنا](#day-24-section-31)
    - [قطار اور کالم کی جگہ بدلنا](#day-24-section-32)
  - [غائب قدریں کیسے ظاہر کریں؟](#day-24-section-33)
      - [اتفاقی اعداد پیدا کرنا](#day-24-section-34)
    - [اتفاقی اعداد کی مزید مثالیں](#day-24-section-35)
  - [NumPy اور شماریات](#day-24-section-36)
    - [NumPy میں میٹرکس](#day-24-section-37)
    - [numpy.arange](#day-24-section-38)
      - [arange کیا ہے؟](#day-24-section-39)
    - [linspace سے اعداد کا سلسلہ بنانا](#day-24-section-40)
    - [NumPy کے شماریاتی فنکشنز](#day-24-section-41)
    - [دہرائے جانے والے سلسلے بنانا](#day-24-section-42)
    - [اتفاقی اعداد کیسے بنائیں؟](#day-24-section-43)
    - [خطی الجبرا](#day-24-section-44)
    - [np.matmul سے میٹرکس کی ضرب](#day-24-section-45)
- [خلاصہ](#day-24-section-46)
  - [💻 مشقیں — دن 24](#day-24-section-47)

<a id="day-24-section-1"></a>

# 📘 دن 24

<a id="day-24-section-2"></a>

## شماریاتی تجزیے کے لیے پائتھن

<a id="day-24-section-3"></a>

## شماریات

شماریات ڈیٹا جمع کرنے، ترتیب دینے، دکھانے، تجزیہ کرنے، معنی سمجھنے اور پیش کرنے کا علم ہے۔ یہ ریاضی کی شاخ ہے اور ڈیٹا سائنس اور مشین لرننگ کے لیے مفید بنیاد فراہم کرتی ہے۔ یہ وسیع شعبہ ہے؛ یہاں صرف متعلقہ بنیادی باتیں دیکھیں گے۔

چیلنج کے بعد آپ ویب ڈیولپمنٹ، ڈیٹا تجزیے، ڈیٹا سائنس یا مشین لرننگ کی طرف جا سکتے ہیں۔ کسی بھی راستے میں ڈیٹا پر کام کرنا پڑ سکتا ہے۔ شماریاتی سمجھ ڈیٹا کی بنیاد پر فیصلے کرنے میں مدد دیتی ہے۔

<a id="day-24-section-4"></a>

## ڈیٹا

ڈیٹا کسی مقصد، عموماً تجزیے، کے لیے جمع کی گئی معلومات ہے۔ یہ متن، اعداد، تصاویر، آواز یا ویڈیو ہو سکتی ہے۔ سیاق کے بغیر اسے سمجھنا مشکل ہے؛ معنی اخذ کرنے کے لیے مناسب اوزار استعمال کرتے ہیں۔

ڈیٹا تجزیے، ڈیٹا سائنس اور مشین لرننگ کا آغاز ڈیٹا سے ہوتا ہے۔ یہ کسی ذریعے سے مل سکتا ہے یا پیدا کیا جا سکتا ہے۔ یہ ساخت یافتہ (*structured*) یا غیر ساخت یافتہ (*unstructured*) ہو سکتا ہے۔

ڈیٹا کم یا زیادہ مقدار میں ہو سکتا ہے۔ اس کے اکثر فائل فارمیٹس فائل ہینڈلنگ میں دیکھ چکے ہیں۔

<a id="day-24-section-5"></a>

## statistics ماڈیول

پائتھن کا `statistics` عددی ڈیٹا کے شماریاتی حساب دیتا ہے۔ اس کا مقصد NumPy، SciPy یا Minitab، SAS اور Matlab جیسے مکمل پیشہ ور پیکیجز کا بدل بننا نہیں؛ یہ بنیادی سائنسی اور شماریاتی حساب کے لیے ہے۔

<a id="day-24-section-6"></a>

# NumPy

پائتھن بذاتِ خود عام مقاصد کی زبان ہے۔ NumPy، SciPy، Matplotlib اور Pandas کے ساتھ یہ سائنسی حساب کا مؤثر ماحول بن جاتی ہے۔

NumPy سائنسی حساب کی بنیادی لائبریری ہے۔ یہ تیز، کئی جہتوں والا array اور اس پر کام کرنے کے اوزار دیتی ہے۔

اب تک Visual Studio Code استعمال ہوا۔ ان مثالوں کے لیے مصنف Jupyter Notebook تجویز کرتا ہے۔ [Anaconda](https://www.anaconda.com/) کے ذریعے اسے حاصل کیا جا سکتا ہے؛ اس کی مکمل تقسیم میں بہت سے عام پیکیج شامل ہوتے ہیں۔

<div dir="ltr">

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy
```

</div>

<a id="day-24-section-7"></a>

## NumPy امپورٹ کرنا

اگر نوٹ بک پسند ہو تو [Jupyter Notebook کی مثال](https://github.com/Asabeneh/data-science-for-everyone/blob/master/numpy/numpy.ipynb) دستیاب ہے۔

<div dir="ltr">

```py
    # How to import numpy
    import numpy as np
    # How to check the version of the numpy package
    print('numpy:', np.__version__)
    # Checking the available methods
    print(dir(np))
```

</div>

<a id="day-24-section-8"></a>

## NumPy array بنانا

<a id="day-24-section-9"></a>

### صحیح اعداد کا array

<div dir="ltr">

```py
    # Creating python List
    python_list = [1,2,3,4,5]

    # Checking data types
    print('Type:', type (python_list)) # <class 'list'>
    #
    print(python_list) # [1, 2, 3, 4, 5]

    two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

    print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # Creating Numpy(Numerical Python) array from python list

    numpy_array_from_list = np.array(python_list)
    print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
    print(numpy_array_from_list) # array([1, 2, 3, 4, 5])
```

</div>

<a id="day-24-section-10"></a>

### اعشاری اعداد کا array

لسٹ دیتے وقت اعشاری قسم مقرر کریں۔

<div dir="ltr">

```py
    # Python list
    python_list = [1,2,3,4,5]

    numy_array_from_list2 = np.array(python_list, dtype=float)
    print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])
```

</div>

<a id="day-24-section-11"></a>

### بولین array

لسٹ سے بولین array بنائیں۔

<div dir="ltr">

```py
    numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
    print(numpy_bool_array) # array([False,  True,  True, False, False])
```

</div>

<a id="day-24-section-12"></a>

### کئی جہتوں والا array

NumPy array میں ایک یا کئی قطاریں اور کالم ہو سکتے ہیں۔

<div dir="ltr">

```py
    two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
    numpy_two_dimensional_list = np.array(two_dimensional_list)
    print(type (numpy_two_dimensional_list))
    print(numpy_two_dimensional_list)
```

</div>

<div dir="ltr">

```sh
    <class 'numpy.ndarray'>
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
```

</div>

<a id="day-24-section-13"></a>

### array کو لسٹ میں بدلنا

<div dir="ltr">

```python
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())
```

</div>

<div dir="ltr">

```sh
    <class 'list'>
    one dimensional array: [1, 2, 3, 4, 5]
    two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

</div>

<a id="day-24-section-14"></a>

### ٹپل سے array بنانا

<div dir="ltr">

```py
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]
```

</div>

<a id="day-24-section-15"></a>

### array کی شکل

`shape` ہر جہت کا سائز ٹپل میں دیتا ہے۔ دو جہتوں میں پہلے قطاروں اور پھر کالموں کی تعداد ہوتی ہے۔ ایک جہت میں ایک عنصر والا ٹپل ملتا ہے۔

<div dir="ltr">

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

</div>

<div dir="ltr">

```sh
    [1 2 3 4 5]
    shape of nums:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    shape of numpy_two_dimensional_list:  (3, 3)
    (3, 4)
```

</div>

<a id="day-24-section-16"></a>

### array کی ڈیٹا قسم

پائتھن میں `str`، `int`، `float`، `complex`، `bool`، لسٹس اور `None` جیسی قدریں ملتی ہیں۔ NumPy array کی مخصوص `dtype` جانچیں۔

<div dir="ltr">

```py
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
```

</div>

<div dir="ltr">

```sh
    [-3 -2 -1  0  1  2  3]
    int64
    [-3. -2. -1.  0.  1.  2.  3.]
    float64
```

</div>

<a id="day-24-section-17"></a>

### array کا سائز

`size` عناصر کی کل تعداد دیتا ہے۔

<div dir="ltr">

```py
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3

```

</div>

<div dir="ltr">

```sh
    The size: 5
    The size: 9
```

</div>

<a id="day-24-section-18"></a>

## NumPy سے حسابی عمل

عام لسٹ کے ہر عنصر پر حساب کے لیے عموماً لوپ لکھنا پڑتا ہے۔ NumPy میں عناصر پر یکجا، یعنی vectorized، عمل کر سکتے ہیں۔

- جمع: `+`
- تفریق: `-`
- ضرب: `*`
- تقسیم: `/`
- باقی: `%`
- فلور ڈویژن: `//`
- قوت: `**`

<a id="day-24-section-19"></a>

### جمع

<div dir="ltr">

```py
# Mathematical Operation
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)

```

</div>

<div dir="ltr">

```sh
    original array:  [1 2 3 4 5]
    [11 12 13 14 15]
```

</div>

<a id="day-24-section-20"></a>

### تفریق

<div dir="ltr">

```python
# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)
```

</div>

<div dir="ltr">

```sh
    original array:  [1 2 3 4 5]
    [-9 -8 -7 -6 -5]
```

</div>

<a id="day-24-section-21"></a>

### ضرب

<div dir="ltr">

```python
# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
```

</div>

<div dir="ltr">

```sh
    original array:  [1 2 3 4 5]
    [10 20 30 40 50]
```

</div>

<a id="day-24-section-22"></a>

### تقسیم

<div dir="ltr">

```python
# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
```

</div>

<div dir="ltr">

```sh
    original array:  [1 2 3 4 5]
    [0.1 0.2 0.3 0.4 0.5]
```

</div>

<a id="day-24-section-23"></a>

### باقی

<div dir="ltr">

```python
# Modulus; Finding the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
```

</div>

<div dir="ltr">

```sh
    original array:  [1 2 3 4 5]
    [1 2 0 1 2]
```

</div>

<a id="day-24-section-24"></a>

### فلور ڈویژن

<div dir="ltr">

```py
# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
```

</div>

<a id="day-24-section-25"></a>

### قوت

<div dir="ltr">

```py
# Exponential is finding some number the power of another:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)
```

</div>

<div dir="ltr">

```sh
    original array:  [1 2 3 4 5]
    [ 1  4  9 16 25]
```

</div>

<a id="day-24-section-26"></a>

## ڈیٹا کی اقسام جانچنا

<div dir="ltr">

```py
#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
```

</div>

<div dir="ltr">

```sh
    int64
    float64
    bool
```

</div>

<a id="day-24-section-27"></a>

### قسم تبدیل کرنا

NumPy array کی قسم بدلی جا سکتی ہے۔

1. صحیح عدد سے اعشاری عدد:

<div dir="ltr">

```py
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr
```

</div>

<div dir="ltr">

```text
array([1., 2., 3., 4.])
```

</div>

2. اعشاری عدد سے صحیح عدد:

<div dir="ltr">

```py
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr
```

</div>

<div dir="ltr">

```sh
    array([1, 2, 3, 4])
```

</div>

3. صحیح عدد سے بولین:

<div dir="ltr">

```py
np.array([-3, -2, 0, 1,2,3], dtype='bool')

```

</div>

<div dir="ltr">

```sh
    array([ True,  True, False,  True,  True,  True])
```

</div>

4. صحیح عدد سے سٹرنگ:

<div dir="ltr">

```py
numpy_float_list.astype('int').astype('str')
```

</div>

<div dir="ltr">

```sh
    array(['1', '2', '3'], dtype='<U21')
```

</div>

<a id="day-24-section-28"></a>

## کئی جہتوں والے arrays

<div dir="ltr">

```py
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
```

</div>

<div dir="ltr">

```sh
    <class 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Shape:  (3, 3)
    Size: 9
    Data type: int64
```

</div>

<a id="day-24-section-29"></a>

### array کے عناصر حاصل کرنا

<div dir="ltr">

```py
# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
```

</div>

<div dir="ltr">

```sh
    First row: [1 2 3]
    Second row: [4 5 6]
    Third row:  [7 8 9]
```

</div>

<div dir="ltr">

```py
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)

```

</div>

<div dir="ltr">

```sh
    First column: [1 4 7]
    Second column: [2 5 8]
    Third column:  [3 6 9]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
```

</div>

<a id="day-24-section-30"></a>

## NumPy array کی سلائسنگ

یہ پائتھن لسٹ کی سلائسنگ سے ملتی جلتی ہے۔

<div dir="ltr">

```py
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
```

</div>

<div dir="ltr">

```sh
    [[1 2]
     [4 5]]
```

</div>

<a id="day-24-section-31"></a>

### قطاروں اور پورے array کو الٹنا

<div dir="ltr">

```py
two_dimension_array[::]
```

</div>

<div dir="ltr">

```sh
    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])
```

</div>

<a id="day-24-section-32"></a>

### قطار اور کالم کی جگہ بدلنا

<div dir="ltr">

```py
    two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
    two_dimension_array[::-1,::-1]
```

</div>

<div dir="ltr">

```sh
    array([[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]])
```

</div>

<a id="day-24-section-33"></a>

## غائب قدریں کیسے ظاہر کریں؟

<div dir="ltr">

```python
    print(two_dimension_array)
    two_dimension_array[1,1] = 55
    two_dimension_array[1,2] =44
    print(two_dimension_array)
```

</div>

<div dir="ltr">

```sh
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
```

</div>

<div dir="ltr">

```py
    # Numpy Zeroes
    # numpy.zeros(shape, dtype=float, order='C')
    numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
    numpy_zeroes
```

</div>

<div dir="ltr">

```sh
    array([[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]])
```

</div>

<div dir="ltr">

```py
# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
```

</div>

<div dir="ltr">

```sh
    [[1 1 1]
     [1 1 1]
     [1 1 1]]
```

</div>

<div dir="ltr">

```py
twoes = numpy_ones * 2
```

</div>

<div dir="ltr">

```py
# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

```

</div>

<div dir="ltr">

```sh
    [[1 2 3]
     [4 5 6]]
    [[1 2]
     [3 4]
     [5 6]]
```

</div>

<div dir="ltr">

```py
flattened = reshaped.flatten()
flattened
```

</div>

<div dir="ltr">

```sh
    array([1, 2, 3, 4, 5, 6])
```

</div>

<div dir="ltr">

```py
    ## Horitzontal Stack
    np_list_one = np.array([1,2,3])
    np_list_two = np.array([4,5,6])

    print(np_list_one + np_list_two)

    print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
```

</div>

<div dir="ltr">

```sh
    [5 7 9]
    Horizontal Append: [1 2 3 4 5 6]
```

</div>

<div dir="ltr">

```py
    ## Vertical Stack
    print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
```

</div>

<div dir="ltr">

```sh
    Vertical Append: [[1 2 3]
     [4 5 6]]
```

</div>

<a id="day-24-section-34"></a>

#### اتفاقی اعداد پیدا کرنا

<div dir="ltr">

```py
    # Generate a random float  number
    random_float = np.random.random()
    random_float
```

</div>

<div dir="ltr">

```sh
    0.018929887384753874
```

</div>

<div dir="ltr">

```py
    # Generate a random float  number
    random_floats = np.random.random(5)
    random_floats
```

</div>

<div dir="ltr">

```sh
    array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])
```

</div>

<div dir="ltr">

```py
    # Generating a random integers between 0 and 10

    random_int = np.random.randint(0, 11)
    random_int
```

</div>

<div dir="ltr">

```sh
    4
```

</div>

<div dir="ltr">

```py
    # Generating a random integers between 2 and 11, and creating a one row array
    random_int = np.random.randint(2,10, size=4)
    random_int
```

</div>

<div dir="ltr">

```sh
    array([8, 8, 8, 2])
```

</div>

<div dir="ltr">

```py
    # Generating a random integers between 0 and 10
    random_int = np.random.randint(2,10, size=(3,3))
    random_int
```

</div>

<div dir="ltr">

```sh
    array([[3, 5, 3],
           [7, 3, 6],
           [2, 3, 3]])
```

</div>

<a id="day-24-section-35"></a>

### اتفاقی اعداد کی مزید مثالیں

<div dir="ltr">

```py
    # np.random.normal(mu, sigma, size)
    normal_array = np.random.normal(79, 15, 80)
    normal_array

```

</div>

<div dir="ltr">

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

</div>

<a id="day-24-section-36"></a>

## NumPy اور شماریات

<div dir="ltr">

```py
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
```

</div>

<div dir="ltr">

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

</div>

<a id="day-24-section-37"></a>

### NumPy میں میٹرکس

<div dir="ltr">

```py

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
```

</div>

<div dir="ltr">

```py
four_by_four_matrix
```

</div>

<div dir="ltr">

```sh
matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]])
```

</div>

<div dir="ltr">

```py
np.asarray(four_by_four_matrix)[2] = 2
four_by_four_matrix
```

</div>

<div dir="ltr">

```sh

matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [2., 2., 2., 2.],
            [1., 1., 1., 1.]])
```

</div>

<a id="day-24-section-38"></a>

### numpy.arange

<a id="day-24-section-39"></a>

#### arange کیا ہے؟

ایک حد میں برابر وقفوں کی قدریں بنانے کے لیے `numpy.arange()` استعمال ہوتا ہے، مثلاً 1 سے 10 تک کا سلسلہ۔ اختتامی حد شامل نہیں ہوتی۔

<div dir="ltr">

```py
# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
lst
```

</div>

<div dir="ltr">

```python
range(0, 11, 2)
```

</div>

<div dir="ltr">

```python
for l in lst:
    print(l)
```

</div>

<div dir="ltr">

```sh 0
    2
    4
    6
    8
    10
```

</div>

<div dir="ltr">

```py
# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
whole_numbers
```

</div>

<div dir="ltr">

```sh
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])
```

</div>

<div dir="ltr">

```py
natural_numbers = np.arange(1, 20, 1)
natural_numbers
```

</div>

<div dir="ltr">

```py
odd_numbers = np.arange(1, 20, 2)
odd_numbers
```

</div>

<div dir="ltr">

```sh
    array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])
```

</div>

<div dir="ltr">

```py
even_numbers = np.arange(2, 20, 2)
even_numbers
```

</div>

<div dir="ltr">

```sh
    array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])
```

</div>

<a id="day-24-section-40"></a>

### linspace سے اعداد کا سلسلہ بنانا

<div dir="ltr">

```py
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
np.linspace(1.0, 5.0, num=10)
```

</div>

<div dir="ltr">

```sh
    array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
           3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

</div>

<div dir="ltr">

```py
# not to include the last value in the interval
np.linspace(1.0, 5.0, num=5, endpoint=False)
```

</div>

<div dir="ltr">

```
array([1. , 1.8, 2.6, 3.4, 4.2])
```

</div>

<div dir="ltr">

```py
# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)
```

</div>

<div dir="ltr">

```sh

array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])
```

</div>

<div dir="ltr">

```py
# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
```

</div>

<div dir="ltr">

```py
x
```

</div>

<div dir="ltr">

```sh
    array([1.+0.j, 2.+0.j, 3.+0.j])
```

</div>

<div dir="ltr">

```py
x.itemsize
```

</div>

<div dir="ltr">

```sh
16
```

</div>

<div dir="ltr">

```py
# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
np_list

```

</div>

<div dir="ltr">

```sh
    array([[1, 2, 3],
           [4, 5, 6]])
```

</div>

<div dir="ltr">

```py
print('First row: ', np_list[0])
print('Second row: ', np_list[1])

```

</div>

<div dir="ltr">

```sh

    First row:  [1 2 3]
    Second row:  [4 5 6]
```

</div>

<div dir="ltr">

```p
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

```

</div>

<div dir="ltr">

```sh
    First column:  [1 4]
    Second column:  [2 5]
    Third column:  [3 6]
```

</div>

<a id="day-24-section-41"></a>

### NumPy کے شماریاتی فنکشنز

NumPy سے کم سے کم، زیادہ سے زیادہ، اوسط، میڈین، percentile، معیاری انحراف اور ویرینس نکال سکتے ہیں۔ اہم فنکشنز:

- کم سے کم: `np.min()`
- زیادہ سے زیادہ: `np.max()`
- اوسط: `np.mean()`
- میڈین: `np.median()`
- ویرینس: `np.var()`
- percentile: `np.percentile()`
- معیاری انحراف: `np.std()`

<div dir="ltr">

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

</div>

<div dir="ltr">

```text
min:  1
max:  55
mean:  14.777777777777779
sd:  18.913709183069525
```

</div>

<div dir="ltr">

```python
min:  1
max:  55
mean:  14.777777777777779
sd:  18.913709183069525
```

</div>

<div dir="ltr">

```python
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))
```

</div>

<div dir="ltr">

```text
[[ 1  2  3]
 [ 4 55 44]
 [ 7  8  9]]
Column with minimum:  [1 2 3]
Column with maximum:  [ 7 55 44]
=== Row ==
Row with minimum:  [1 4 7]
Row with maximum:  [ 3 55  9]
```

</div>

<a id="day-24-section-42"></a>

### دہرائے جانے والے سلسلے بنانا

<div dir="ltr">

```python
a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

```

</div>

<div dir="ltr">

```text
Tile:    [1 2 3 1 2 3]
Repeat:  [1 1 2 2 3 3]
```

</div>

<a id="day-24-section-43"></a>

### اتفاقی اعداد کیسے بنائیں؟

<div dir="ltr">

```python
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
```

</div>

<div dir="ltr">

```text
0.6149403282678213
```

</div>

<div dir="ltr">

```python
0.4763968133790438
```

</div>

<div dir="ltr">

```text
0.4763968133790438
```

</div>

<div dir="ltr">

```python
# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)
```

</div>

<div dir="ltr">

```text
[[0.13031737 0.4429537  0.1129527 ]
 [0.76811539 0.88256594 0.6754075 ]]
```

</div>

<div dir="ltr">

```python
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
```

</div>

<div dir="ltr">

```text
['u' 'o' 'o' 'i' 'e' 'e' 'u' 'o' 'u' 'a']
```

</div>

<div dir="ltr">

```python
['i' 'u' 'e' 'o' 'a' 'i' 'e' 'u' 'o' 'i']
```

</div>

<div dir="ltr">

```text
['iueoaieuoi']
```

</div>

<div dir="ltr">

```python
## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
rand
```

</div>

<div dir="ltr">

```text
array([[0.97992598, 0.79642484],
       [0.65263629, 0.55763145]])
```

</div>

<div dir="ltr">

```python
rand2 = np.random.randn(2,2)
rand2

```

</div>

<div dir="ltr">

```text
array([[ 1.65593322, -0.52326621],
       [ 0.39071179, -2.03649407]])
```

</div>

<div dir="ltr">

```python
# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
rand_int
```

</div>

<div dir="ltr">

```text
array([[0, 7, 5],
       [4, 1, 4],
       [3, 5, 3],
       [4, 3, 8],
       [4, 6, 7]])
```

</div>

<div dir="ltr">

```py
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
```

</div>

<div dir="ltr">

```sh

    min:  3.557811005458804
    max:  6.876317743643499
    mean:  5.035832048106663
    median:  5.020161980441937
    mode:  ModeResult(mode=array([3.55781101]), count=array([1]))
    sd:  0.489682424165213

```

</div>

<div dir="ltr">

```python
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
```

</div>

![اتفاقی ڈیٹا کا گراف](../test_files/test_121_0.png)

<div dir="ltr">

```python
# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)
```

</div>

<a id="day-24-section-44"></a>

### خطی الجبرا

1. ڈاٹ پراڈکٹ:

<div dir="ltr">

```python
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23
```

</div>

<a id="day-24-section-45"></a>

### np.matmul سے میٹرکس کی ضرب

<div dir="ltr">

```python
### Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
np.matmul(h, i)
```

</div>

<div dir="ltr">

```sh
    array([[19, 22],
           [43, 50]])

```

</div>

<div dir="ltr">

```py
## Determinant 2*2 matrix
### 5*8-7*6np.linalg.det(i)
```

</div>

<div dir="ltr">

```python
np.linalg.det(i)
```

</div>

<div dir="ltr">

```text
-1.999999999999999
```

</div>

<div dir="ltr">

```python
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
```

</div>

<div dir="ltr">

```python
Z
```

</div>

<div dir="ltr">

```text
array([[0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.]])
```

</div>

<div dir="ltr">

```python
new_list = [ x + 2 for x in range(0, 11)]
```

</div>

<div dir="ltr">

```python
new_list
```

</div>

<div dir="ltr">

```text
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

</div>

<div dir="ltr">

```python
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

</div>

<div dir="ltr">

```text
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

</div>

<div dir="ltr">

```python
np_arr = np.array(range(0, 11))
np_arr + 2
```

</div>

<div dir="ltr">

```text
array([ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
```

</div>

خطی تعلق رکھنے والی مقداروں کے لیے خطی مساوات استعمال ہوتی ہے۔ مثال:

<div dir="ltr">

```python
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
pressure
```

</div>

<div dir="ltr">

```text
array([ 7, 9, 11, 13, 15])
```

</div>

<div dir="ltr">

```python
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
```

</div>

![خطی مساوات کا گراف](../test_files/test_141_0.png)

NumPy سے گاؤسی یا نارمل تقسیم کا نمونہ بنا سکتے ہیں۔ اس کے لیے اوسط `mu`، معیاری انحراف `sigma` اور ڈیٹا نقاط کی تعداد درکار ہے۔

<div dir="ltr">

```python
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
```

</div>

![نارمل تقسیم](../test_files/test_143_0.png)

<a id="day-24-section-46"></a>

# خلاصہ

عام پائتھن لسٹس اور NumPy arrays میں بنیادی فرق:

1. arrays عناصر پر یکجا حسابی عمل کرتے ہیں؛ لسٹس براہِ راست ایسا نہیں کرتیں۔
2. عام طور پر array کا سائز مقرر ہوتا ہے؛ سائز بدلنے کے عمل اکثر نیا array بناتے ہیں۔
3. ہر array کی ایک `dtype` ہوتی ہے اور عناصر اسی کے مطابق محفوظ ہوتے ہیں۔
4. یکساں عددی ڈیٹا کا NumPy array عموماً لسٹوں کی لسٹ سے کم جگہ لیتا ہے۔
5. arrays بولین انڈیکسنگ کی حمایت کرتے ہیں۔

<a id="day-24-section-47"></a>

## 💻 مشقیں — دن 24

1. تمام مثالیں دوبارہ آزمائیں۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 23](./23_virtual_environment.md) | [فہرست](./readme.md) | [اگلا دن: 25](./25_pandas.md)

</div>

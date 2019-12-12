###### Author: Asabeneh Yetayeh

# Numpy(Numberic Python)

In this note book you will cover all what you need to know about Numpy. Inditon to numpy we will see how to use matplot lib python library which will help us to draw graphs and visualize data.

So far, we have been using vscode but from now on I would recommend using Jupter Notebook. To access jupter notebook let's install [anaconda](https://www.anaconda.com/)


```python
# Installation anconda numpy
```

## How to import numpy (Numeric Python)


```python
# A numpy array must have all items to be of the same data type, unlike lists.
# This is another significant difference.
```


```python
# How to import numpy
import numpy as np

```

## How to check package version in python


```python
# How to check the version of the numpy package
print('numpy:', np.__version__)

```

    numpy: 1.17.2



```python
# Checking the available methods
print(dir(np))
```

    ['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '_UFUNC_API', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__mkl_version__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_add_newdoc_ufunc', '_distributor_init', '_globals', '_mat', '_pytesttester', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex256', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'dual', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float128', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_float_positional', 'format_float_scientific', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'gcd', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogram_bin_edges', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'lcm', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mkl', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanquantile', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'os', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'printoptions', 'prod', 'product', 'promote_types', 'ptp', 'put', 'put_along_axis', 'putmask', 'pv', 'quantile', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'take_along_axis', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']



```python
print(np.log10(2))
print(np.not_equal(10, 10))
```

    0.3010299956639812
    False


## Creating a list in python


```python
# Creating python List

python_list = [1,2,3,4,5]
# Checking data types
print(type (python_list))
print(python_list)
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print(two_dimensional_list)
```

    <class 'list'>
    [1, 2, 3, 4, 5]
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


## Creating numpy array using numpy


```python
# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))
print(numpy_array_from_list)

```

    <class 'numpy.ndarray'>
    [1 2 3 4 5]



```python
numy_array_from_list2 = np.array(python_list)
numy_array_from_list2
```




    array([1, 2, 3, 4, 5])




```python
numy_array_from_list2 = np.array(python_list, dtype=float)
numy_array_from_list2
```




    array([1., 2., 3., 4., 5.])




```python
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
numpy_bool_array
```




    array([False,  True,  True, False, False])




```python

numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)
```

    <class 'numpy.ndarray'>
    [[0 1 2]
     [3 4 5]
     [6 7 8]]



```python
numpy_array_from_list
```




    array([1, 2, 3, 4, 5])




```python
numpy_two_dimensional_list
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])



### Converting numpy array to list


```python
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())
```

    <class 'list'>
    one dimensional array: [1, 2, 3, 4, 5]
    two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]



```python
numpy_two_dimensional_list
```




    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])



## Creating numpy array from tuple


```python
# Numpy array from tuple

# Creating tuple in Python

python_tuple = (1,2,3,4,5)
print(type (python_tuple))
print('python_tuple: ', python_tuple)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple))
print('numpy_array_from_tuple: ', numpy_array_from_tuple)
```

    <class 'tuple'>
    python_tuple:  (1, 2, 3, 4, 5)
    <class 'numpy.ndarray'>
    numpy_array_from_tuple:  [1 2 3 4 5]



```python
numpy_array_from_tuple
```




    array([1, 2, 3, 4, 5])



## Shape of numpy array
The shape method provide the shape of the array as a tuple. The first is the row and the second is the column


```python
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
       [4,5,6,7],
       [8,9,10, 11]])
print(three_by_four_array.shape)
```

    [1 2 3 4 5]
    shape of nums:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    shape of numpy_two_dimensional_list:  (3, 3)
    (3, 4)


## Data type of numpy array

Type of data types: str, int, float, complex, bool, list, None


```python
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

```

    [-3 -2 -1  0  1  2  3]
    int64
    [-3. -2. -1.  0.  1.  2.  3.]
    float64


## Size of a numpy array
Instead of len size is used to get the length of items in a numpy array


```python
numpy_array_from_list.size
```




    5




```python
numpy_two_dimensional_list.size
```




    9



### Mathematical Operation




```python
# Mathematical Operation

# Addition
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)
# Multiplication
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
```

    original array:  [1 2 3 4 5]
    [11 12 13 14 15]
    [-9 -8 -7 -6 -5]
    [10 20 30 40 50]



```python
# Float numbers

numpy_int_list = np.array([1,2,3,4])
numpy_float_list = np.array([1.1, 2.0,3.2])
numpy_float_list2 = np.array([1.1,2.0,3.2])

print(numpy_int_list.dtype)
print(numpy_float_list2.dtype)
print(numpy_float_list.dtype)
```

    int64
    float64
    float64


## Converting type from float to int


```python
# Converting type from float to int
numpy_float_list.astype('int')

```




    array([1, 2, 3])




```python
# Converting type from int to str
numpy_float_list.astype('int').astype('str')
```




    array(['1', '2', '3'], dtype='<U21')



## Dimensional Arrays


```python
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

```

    <class 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Shape:  (3, 3)
    Size: 9
    Data type: int64



```python
two_dimension_array
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])



## How to extract specific items from an array?


```python
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)

```

    First row: [1 2 3]
    Second row: [4 5 6]
    Third row:  [7 8 9]



```python
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
```

    First column: [1 4 7]
    Second column: [2 5 8]
    Third column:  [3 6 9]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]


Slicing in numpy is similar to list


```python
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
first_two_rows_and_columns
```




    array([[1, 2],
           [4, 5]])



## How to reverse the rows and the whole array?


```python
two_dimension_array[::]
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])



### Reverse only the row positions


```python
two_dimension_array[::-1,]
```




    array([[7, 8, 9],
           [4, 5, 6],
           [1, 2, 3]])



### Reverse the row and column positions


```python
two_dimension_array[::-1,::-1]
```




    array([[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]])



## How to represent missing values and infinite?


```python
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)
```

    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]



```python
# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
numpy_zeroes
```




    array([[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]])




```python
# Numpy Zeroes
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
```

    [[1 1 1]
     [1 1 1]
     [1 1 1]]



```python
twoes = numpy_ones * 2
```


```python
# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)

```

    [[1 2 3]
     [4 5 6]]
    [[1 2]
     [3 4]
     [5 6]]



```python
flattened = reshaped.flatten()
flattened
```




    array([1, 2, 3, 4, 5, 6])




```python
## Horitzontal Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np_list_one + np_list_two)

print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
```

    [5 7 9]
    Horizontal Append: [1 2 3 4 5 6]



```python
## Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
```

    Vertical Append: [[1 2 3]
     [4 5 6]]


#### Generating Random Numbers


```python
# Generate a random float  number
random_float = np.random.random()
random_float
```




    0.6661632875670657




```python
# Generate a random float  number
random_floats = np.random.random(5)
random_floats
```




    array([0.12945387, 0.1859908 , 0.47805876, 0.51996342, 0.52458233])




```python
# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
random_int
```




    7




```python
# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
random_int
```




    array([5, 8, 8, 9])




```python
# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
random_int
```




    array([[8, 9, 5],
           [9, 8, 3],
           [2, 3, 8]])




```python
# Generate random numbers
# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 1000)
normal_array


```




    array([ 76.67233671,  87.8686846 ,  64.80771996,  79.44136527,
            68.83066184, 102.85967631,  74.40838573,  58.56053793,
            93.76814784,  82.16082568,  86.80548555,  77.95291907,
            97.71514434,  95.94083876,  82.53018033,  73.74619803,
            67.07970869, 102.20984782,  81.67766599,  73.82096132,
            90.17632538, 102.87342877,  84.19855251,  81.11888938,
            63.42782472,  75.3734846 ,  79.04423914,  56.52607352,
            58.30505483,  54.69555571,  63.25792739,  88.75239018,
            85.44533248,  59.76883843,  39.72683784,  78.1029094 ,
            54.19952262,  82.383277  ,  87.01010766,  73.09642208,
            81.99276776,  82.58990091,  72.71303439, 101.73499367,
            73.65596295,  81.89611334,  96.14703307,  74.9629613 ,
            84.79491744,  90.77830881,  70.69085365,  69.27799996,
            74.07836137,  56.79410721,  76.08072393,  83.28246182,
            83.66382654,  80.79644627,  83.39674788,  73.68044176,
            59.74405724,  47.50763054,  50.99870066,  85.53776901,
            80.61131428,  62.66726385,  69.8289171 ,  58.2394869 ,
            86.5158869 ,  86.92976422,  65.12965299, 101.9918336 ,
            73.3855881 ,  99.29788439,  82.48238578,  83.14592314,
           109.13987986,  87.18461073,  73.18647475,  76.04712709,
            67.2936962 ,  56.39363409,  81.35106332,  84.5083442 ,
            64.45556043,  91.48890982,  82.97061603,  88.02694597,
            79.98966974,  87.1672428 ,  98.96048765,  79.90801913,
            66.33509656,  84.04023607,  88.09079879,  77.35006201,
           103.55727658,  64.13437043,  68.05358071,  90.89443625,
            82.79038989,  62.89514185,  74.97098809,  66.19397795,
            92.70537742,  71.0629109 ,  96.37710058, 111.0582448 ,
            82.49413524,  86.81684626,  51.59797622,  82.4090514 ,
            67.44794517,  81.27167783,  56.5523663 ,  70.31869978,
            73.27622806,  70.45432913,  69.65909073,  65.26697689,
            92.09133852,  77.6409777 ,  75.12755482,  86.92392364,
            52.345763  ,  61.21302273,  76.91865347, 101.50717646,
            65.45696696,  79.72489732,  76.1272494 ,  95.31233116,
           115.96549733,  75.92209483,  79.08231261,  97.77244182,
            74.18461463,  66.86589353,  70.58006434,  37.59185572,
           103.64455596,  48.23404954,  47.68141346,  69.76670989,
           105.52887085,  67.35640534,  59.53778107,  79.01221476,
            63.25760905,  53.41243319,  67.56688095,  89.44295326,
            73.0249909 , 110.62094367,  75.30776079,  83.06746009,
            72.00044242,  95.55925297,  87.41229729,  75.83119383,
            81.76799949,  66.66909113, 111.87301683,  55.64386831,
            88.2057447 ,  86.98310199,  90.64320901,  51.16660292,
            86.44260395, 101.81543578,  54.33572759,  86.59505355,
            74.96338672,  88.58073882,  99.97520135, 115.62885994,
            48.33081456,  87.46330109,  92.57228694, 105.5973409 ,
            74.69521182,  85.18418419,  71.00401484,  94.4873179 ,
            89.58091544,  78.19894226,  78.62597505,  97.70529476,
            48.9448779 ,  54.77461514,  80.84647783,  56.72044906,
            53.17830126,  69.47376476,  62.70835212,  73.50984826,
            79.95708327,  60.30922811,  68.71736216,  92.40372794,
            86.23245168,  71.58967187,  58.57427101,  91.13298606,
            54.02876851,  91.61300175,  73.85802225,  74.1262673 ,
           113.37398924,  83.62799161,  69.67276347,  90.92422022,
            93.80366456,  75.49340444,  69.68268106,  65.21188249,
            73.08843699,  76.9702737 ,  86.63909332,  63.38692368,
            59.0107169 ,  64.58012401,  67.77071814,  82.81680919,
            47.00115734,  77.89249231,  94.57639045,  82.62969276,
            89.2754606 ,  75.03679732, 105.40459045,  82.31470981,
            91.73027956,  82.57265691,  73.93925755,  79.39961404,
            78.42971467,  81.85491373,  98.50921957,  89.41696616,
            64.5228743 ,  86.34810062,  85.53403969,  65.44710598,
            97.61823581,  73.36500749,  78.7969976 ,  82.64530182,
           102.5212311 ,  60.24103391,  88.97487767,  67.74463234,
            87.06975383,  90.35731726, 113.93417792,  94.43622715,
            75.68177623,  79.23496178,  63.19462299,  67.36853029,
            39.35791739,  74.51434441,  72.60509108,  80.38587487,
            68.68165911,  67.91476795,  73.7642702 ,  97.97756047,
            99.15996313,  89.43595584,  53.27369357,  75.35961475,
            93.21230424,  75.6875106 ,  75.20803627,  86.68011244,
            73.46234329,  46.2650612 ,  85.99510379,  89.78716287,
            86.54377973,  89.4421289 ,  66.35904948,  73.69434082,
            72.16037244, 100.7404422 ,  76.81167206,  92.47498529,
            51.99811087,  68.1875055 ,  97.21350945,  73.98272047,
            79.9433559 ,  91.32704877,  70.36341543,  91.53287551,
            64.0916329 ,  82.05669765,  59.91901105,  67.06455073,
            90.82458082,  69.24155283,  86.00691215,  97.78612486,
            57.53429118,  55.13961827,  65.92071751,  69.12679024,
            80.24386507,  70.76561644,  52.38657486,  74.03314561,
            55.08560907,  78.93565259,  72.12457096,  88.1878194 ,
            69.26543786,  94.26645154,  57.22213699,  85.08262645,
            75.15236761, 112.25159803,  60.69175095, 107.55714907,
            97.40508175, 100.34600206,  71.64266763,  69.56735445,
           105.37943464, 106.66581679,  69.88994757,  55.50599503,
            96.85984215,  82.27633384,  71.99542571,  87.3033245 ,
            53.9629657 ,  86.75436111,  93.71079875,  78.1735369 ,
            59.12435725, 106.91289813,  90.55510253,  80.63892904,
            49.52196748,  69.92138936,  82.59370828,  64.36717287,
            83.46872542,  80.66546831,  73.272708  ,  85.55761189,
            70.29998731,  85.27149783,  61.22698174, 112.1539227 ,
            85.06829561, 105.62724187,  83.21087039,  91.47630885,
            52.61117972,  96.39363125,  98.7615724 ,  82.3406285 ,
            78.21209665,  81.68186011,  65.53179422,  81.636421  ,
            48.28426725,  84.22834582,  72.65396863,  89.78723124,
            62.69033062,  67.42236676,  61.70774152,  91.00289665,
            65.8869877 ,  98.85053178,  90.95893416,  80.71673232,
            69.1443606 ,  83.24469518,  53.61281569,  98.41838607,
            95.89214815,  76.08288325, 105.95876474,  87.8123779 ,
            98.83277115,  75.70467395,  64.52606003,  46.55761117,
            61.35279897,  79.03475418,  70.26356208,  83.15010813,
            71.35489747,  85.12422364,  79.6318843 ,  64.65930113,
            50.39553485,  59.74637731,  97.17317934, 101.28981635,
            55.51070593,  65.5724488 ,  56.9783323 ,  76.69243571,
            80.22507493,  93.93824876,  74.27245434,  62.22895849,
            61.71693803,  91.50874511, 102.93624517,  66.51614867,
            73.66758854, 101.95706886,  80.17324289,  89.77788816,
            79.41557833,  83.12691023,  78.39868201,  82.1245395 ,
            75.39745528,  64.15220095,  66.19591545,  78.52233881,
            69.45532022,  80.07279819,  92.05981037,  57.88406497,
            78.39408713, 103.98322005,  71.85190829,  85.69820843,
            78.01623836,  42.12347928,  82.10875153,  59.7121601 ,
            75.6374047 ,  68.03654408,  75.31781043,  57.31129216,
            82.6326405 ,  83.43080808,  81.52065719,  61.07178023,
            65.89585315,  98.07305443,  57.04010365,  99.11343007,
            82.03829385,  94.96220101,  63.10779942,  43.75533224,
            60.96190311,  60.38889234,  86.01180327,  72.03287838,
            88.56135551,  83.20459124,  85.33961473,  65.09373303,
            72.95666996,  70.31639299,  82.84800507,  65.21994284,
            83.71082556,  59.30552118,  57.24161946,  91.59640687,
            81.07946716,  81.72062826, 104.82245391, 102.22642442,
            85.5935274 ,  80.65595414,  85.21561212,  89.32052529,
            70.80532767,  81.2402353 ,  73.3429679 ,  83.96484983,
           102.14285344,  66.28045024,  69.08414849,  83.96027461,
            99.882723  ,  92.56429669,  71.38334333,  91.29460474,
            74.73563361,  82.61344943, 101.38451941,  96.22447959,
            92.46992093,  73.64548057,  95.67625789,  97.30840065,
            86.18687145,  39.79818989,  67.44627234,  78.81800827,
            99.88127457,  97.08040669,  80.20672721,  61.6621477 ,
            89.45069827,  69.2126993 , 105.30121908,  92.73651782,
           104.02718862,  82.63560985, 117.14218447,  70.78186465,
            69.38217047,  68.6752697 , 118.88261052,  94.16663109,
            58.85480966,  84.43706331,  93.91832945,  59.99542403,
            69.73006365,  87.14948387,  86.17056873,  72.04322939,
            74.60316737,  65.4121187 ,  75.88172757,  73.0725911 ,
            68.47916028,  88.94688011,  79.68974545,  66.22710966,
            75.65901653,  65.17336078,  82.7854841 ,  68.54114688,
            63.5422467 ,  85.27593096,  77.11949083,  85.1792345 ,
            85.91031198,  94.40889745,  81.53460066,  78.13741406,
            48.50311626,  74.00832439,  62.64749899,  26.42484343,
            90.37956952,  47.85275007,  90.21932564,  71.54854049,
            66.33008326,  61.45646105,  83.24146521,  77.85092006,
            79.41867441,  82.35535991,  95.10042516, 104.55030347,
            68.41918381,  62.24245143,  52.68448442,  61.93464607,
            86.38263287,  81.40589031, 106.80202022,  76.64983598,
            67.98843927,  81.30232608,  90.07378784,  66.33965558,
            59.26391705,  90.22932022,  78.57688898,  60.99512356,
            53.16782133,  76.80554089,  73.18463521,  75.74775613,
            72.42763706,  84.15981253,  79.86702314, 107.59287088,
            42.72244939,  94.10074796,  65.11731346,  92.44057941,
            88.45199421,  49.7210141 ,  70.92988608,  84.87914436,
           111.27471207,  71.10212581,  85.88122011,  85.39018312,
            64.75059945,  80.19182056,  52.28697701,  63.63607001,
            70.81836933,  92.12627834, 117.01393871,  84.55599041,
            74.38388382,  72.05047965,  80.96294247,  76.95375672,
            53.52743329,  68.26820071,  84.62245233,  83.76592911,
            71.66491816,  62.84764731, 101.77473998,  83.7109928 ,
            88.14356241,  70.56990958,  63.4114506 ,  97.03530829,
            75.29544449,  86.46570106,  90.71226994,  59.58744577,
            66.28889053,  81.81896037, 106.19049949,  76.79027375,
           103.79328945,  68.83879663,  86.96337876, 109.07240618,
            89.57507226,  71.02647491,  66.01655389,  63.71481491,
            84.96881056,  81.47094049,  41.08479295, 102.81032149,
            57.10553083,  74.69771968,  85.08750235,  77.86982387,
            66.24827223,  77.61800937,  87.85279737,  97.44114529,
            73.62465256,  84.87370213,  59.82819789,  83.51332999,
            76.1564969 ,  92.80216207,  84.45078494,  98.12615727,
            92.82159165,  77.68306951,  56.70024893,  96.13691428,
            58.6947481 ,  62.43855793,  89.44203656,  88.39339383,
            64.83174886,  80.20517572,  62.43358506,  90.35687599,
            56.89696185, 101.4910522 ,  63.87426467,  64.76978812,
            86.19666835,  64.7236682 ,  94.34248975,  75.09728512,
            91.30899086,  96.6812488 ,  91.14172719,  82.51490688,
            89.22153835,  82.87563357,  84.59497932,  41.99164693,
            98.11955977,  79.61268968,  72.40763417,  73.97813269,
            58.1632078 ,  62.83530224,  82.15621201,  71.28072756,
           114.50107295,  98.83008872,  64.0437643 ,  99.65822453,
            75.48720903,  63.32837291,  76.20823217,  86.84282223,
            62.43082268,  73.15705444, 101.1511228 ,  76.82948915,
            81.40991749,  69.48832828,  93.78545288,  84.11019295,
            74.84590881,  80.41138779, 119.75165158,  94.30283763,
            62.60960855,  80.05025988, 104.81265311,  83.38125656,
            38.78328615,  62.41916009,  70.16735618,  51.44288365,
            92.80525403,  84.92470846,  66.26844763,  74.71143692,
            63.24518316, 101.03067104,  87.61812768,  81.78062237,
            79.26854548,  82.45239206,  62.84682868,  75.85374972,
            81.50671709,  91.61193178,  84.80540264,  76.83093669,
            85.07574758,  78.12229555,  66.29072864,  95.26350438,
            56.05352073,  75.24843365,  94.25579772,  80.29484646,
            54.79358077,  80.00636677,  98.09007754,  65.05236219,
            92.21169732,  93.78045193, 100.08258446,  50.34210852,
            78.48684671,  92.46745685,  84.84801383,  80.80624528,
           105.39277867,  95.79633397,  84.89636306, 113.4129892 ,
            94.37919945,  33.04894125,  57.62445042,  74.70068129,
            84.36545129,  58.65159412,  59.80499077,  72.37282525,
            63.67362837,  60.15747326,  92.27103467,  67.58559178,
            71.78018188,  78.50521982,  57.14143778,  87.75269721,
            70.3938368 ,  85.84713936,  75.96861357,  77.60591163,
            73.37361875,  94.88377692,  66.33736786,  67.73206898,
            98.54323406,  97.7942897 ,  32.15593272,  92.2224777 ,
            86.09657291,  79.07206812,  59.96670651,  67.31216781,
            53.64584436,  55.49172965,  87.88340258,  93.21390739,
            74.83629979,  74.97550995, 104.20264824,  85.90602294,
            98.25959023,  82.32831776,  91.19296573,  68.66385157,
            72.47319467,  66.32588349,  69.46771085,  84.80546774,
            92.2537018 ,  91.61146021,  87.97125321,  77.40162354,
            56.81359943, 100.63347184,  46.06026334,  64.3072636 ,
            73.16833499,  66.58449357,  77.1759305 ,  80.95588782,
            98.53819261,  93.8004291 ,  71.79955175,  71.8092341 ,
            67.48364477,  76.92938082,  80.90556577,  76.3361884 ,
            56.08189834,  69.72013329,  83.23890509,  87.63876162,
            91.6671542 ,  65.9815465 ,  72.61972745,  98.36138944,
            79.27809954,  83.22987584,  87.65365004,  89.72387738,
            77.28925164,  96.80686114,  66.27593891,  58.22356418,
            69.00110634,  98.69032179,  83.51534823,  54.84798906,
            65.53428591,  64.14493646,  73.09656991,  80.90855247,
            68.49764325,  66.70828679,  88.94583478,  68.08884137,
           114.20054981,  48.43412772,  65.62243783,  76.5361132 ,
            92.80262402,  73.745952  ,  77.88874597, 103.32373442,
            82.78186246,  87.31269531,  82.7184332 ,  93.00860143,
            86.81186734,  81.88725671,  85.57497866,  83.06657941,
            73.92135462,  64.67840907,  54.1324434 ,  44.56198425,
           103.74716492,  73.00720986,  79.70037455, 117.226086  ,
            90.95959027,  82.93746876,  68.01202978,  51.38653362,
            49.21376817,  82.98155396,  63.73945045,  71.87810968,
            67.47155016,  50.17812178,  68.00005018,  74.54213222,
            86.46204427,  81.88129502, 102.2539116 , 109.56599738,
           101.67600164,  59.82763125,  66.7090957 ,  48.75955951,
            84.40734607,  86.4125707 ,  31.21236081,  76.260938  ,
            94.59278233, 112.3969095 ,  82.55898885,  66.22114921,
            80.83856717,  85.08680709,  68.69636286,  69.71161312,
            76.3196622 ,  78.68149223,  88.42004846,  78.94426232,
            54.8348913 ,  82.21921133,  71.59374818,  82.0954091 ,
            62.69406376,  79.16889409,  67.81528319,  95.83872873,
            74.96783523,  81.70211669,  97.29360667,  51.07465606,
            70.03123751,  94.59751783,  68.4839708 ,  51.8779431 ,
            43.06271614,  53.56724106,  38.99403909,  92.53214605,
           100.08867662,  74.91608135,  76.43190909,  77.23653514,
           101.68713224,  74.48287587,  80.29475109,  86.49937422,
            74.18560655,  90.32342146,  67.54203627,  61.65836826,
            65.90214024,  90.18667155,  84.24811988,  87.31264766,
            65.51077902,  73.6819876 ,  85.97917178,  84.60220551,
            83.61993451,  81.97165845,  77.12380967,  85.92629768,
            68.07735309,  97.04263534, 107.17028674,  56.66687639,
            63.0328498 ,  95.71169257,  66.41415792,  73.01941362,
            77.43739944,  80.91838286,  76.94361736,  92.45966561,
            64.28909701,  90.86504202,  64.31354427,  68.00874105,
            74.90902052,  46.84873109,  96.71448387,  92.88217861,
            58.61271069,  74.34878286,  76.81571832, 100.83234903,
            87.04080477,  76.17316306,  76.60724189,  57.03191229,
           102.49683378,  84.94708014,  97.89869778,  51.74458192,
            71.56589366,  71.92667719,  66.78215404,  90.44885288])




```python

```

## Numpy and Statistics


```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
```




    (array([ 1.,  0.,  1.,  2.,  0.,  1.,  3.,  3.,  4.,  2.,  4., 10.,  7.,
            12., 15., 13., 20., 26., 16., 32., 36., 42., 38., 37., 35., 54.,
            50., 40., 40., 55., 56., 49., 45., 29., 37., 26., 26., 23., 28.,
            12., 22., 10., 11.,  5.,  3.,  6.,  4.,  4.,  3.,  2.]),
     array([ 26.42484343,  28.2913796 ,  30.15791576,  32.02445192,
             33.89098809,  35.75752425,  37.62406041,  39.49059657,
             41.35713274,  43.2236689 ,  45.09020506,  46.95674123,
             48.82327739,  50.68981355,  52.55634972,  54.42288588,
             56.28942204,  58.1559582 ,  60.02249437,  61.88903053,
             63.75556669,  65.62210286,  67.48863902,  69.35517518,
             71.22171134,  73.08824751,  74.95478367,  76.82131983,
             78.687856  ,  80.55439216,  82.42092832,  84.28746449,
             86.15400065,  88.02053681,  89.88707297,  91.75360914,
             93.6201453 ,  95.48668146,  97.35321763,  99.21975379,
            101.08628995, 102.95282611, 104.81936228, 106.68589844,
            108.5524346 , 110.41897077, 112.28550693, 114.15204309,
            116.01857926, 117.88511542, 119.75165158]),
     <a list of 50 Patch objects>)




```python

```


```python
# numpy.asarray()
# Asarray
# The asarray()function is used when you want to convert an input to an array. 
# The input could be a lists, tuple, ndarray, etc.
```


```python
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
```


```python
four_by_four_matrix
```




    matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]])




```python
np.asarray(four_by_four_matrix)[2] = 2
four_by_four_matrix
```




    matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [2., 2., 2., 2.],
            [1., 1., 1., 1.]])




```python
# numpy.arange() in Python with Example
# Whay is Arrange?
# Sometimes, you want to create values that are evenly spaced within a defined interval. 
# For instance, you want to create values from 1 to 10; you can use numpy.arange() function

```


```python
# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
lst
```




    range(0, 11, 2)




```python
for l in lst:
    print(l)
```

    0
    2
    4
    6
    8
    10



```python
# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
whole_numbers
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])




```python
natural_numbers = np.arange(1, 20, 1)
natural_numbers
```




    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
           18, 19])




```python
odd_numbers = np.arange(1, 20, 2)
odd_numbers
```




    array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])




```python
even_numbers = np.arange(2, 20, 2)
even_numbers
```




    array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])




```python
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
np.linspace(1.0, 5.0, num=10)
```




    array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
           3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])




```python
# not to include the last value in the interval
np.linspace(1.0, 5.0, num=5, endpoint=False)
```




    array([1. , 1.8, 2.6, 3.4, 4.2])




```python
# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)
```


```python
np.logspace(2, 4.0, num=4)
```




    array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])




```python
# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
```


```python
x
```




    array([1.+0.j, 2.+0.j, 3.+0.j])




```python
x.itemsize
```




    16




```python
# indexing and Slicing NumPy Arrays in Python 

np_list = np.array([(1,2,3), (4,5,6)])
np_list

```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
print('First row: ', np_list[0])
print('Second row: ', np_list[1])

```

    First row:  [1 2 3]
    Second row:  [4 5 6]



```python
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])

```

    First column:  [1 4]
    Second column:  [2 5]
    Third column:  [3 6]



## NumPy Statistical Functions with Example
NumPy has quite a few useful statistical functions for finding minimum, maximum, percentile standard deviation and variance, etc from the given elements in the array.
The functions are explained as follows −
Statistical function
Numpy is equipped with the robust statistical function as listed below

- Numpy Functions
    - Min	np.min()
    - Max	np.max()
    - Mean	np.mean()
    - Median	np.median()
    - Standard deviation	np.std()


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


## How to create repeating sequences?



```python
a = [1,2,3] 

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2))

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2))

```

    Tile:    [1 2 3 1 2 3]
    Repeat:  [1 1 2 2 3 3]


## How to generate random numbers?


```python
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
```

    0.4763968133790438



```python
# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)
```

    [[0.67018871 0.71699922 0.36490538]
     [0.78086531 0.5779336  0.81444353]]



```python
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))  
```

    ['i' 'u' 'e' 'o' 'a' 'i' 'e' 'u' 'o' 'i']



```python

```


```python
## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
rand
```




    array([[0.66811333, 0.1139411 ],
           [0.90955775, 0.14954203]])




```python
rand2 = np.random.randn(2,2)
rand2

```




    array([[-0.84819546, -0.39626819],
           [ 0.9172979 ,  0.03661474]])




```python
# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
rand_int
```




    array([[2, 7, 0],
           [0, 2, 7],
           [5, 9, 4],
           [6, 0, 8],
           [4, 6, 2]])




```python

```


```python
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000)
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
```

    min:  3.566493784430423
    max:  6.823091905048957
    mean:  5.034308251615374
    median:  5.0317142506545505
    mode:  ModeResult(mode=array([3.56649378]), count=array([1]))
    sd:  0.5050902240094916



```python
plt.hist(np_normal_dis, color="grey", bins=21)
```




    (array([  3.,   7.,  11.,  22.,  41.,  64.,  72., 109., 117., 122., 117.,
             93.,  94.,  47.,  36.,  20.,  15.,   5.,   3.,   0.,   2.]),
     array([3.56649378, 3.72156989, 3.87664599, 4.03172209, 4.18679819,
            4.34187429, 4.49695039, 4.65202649, 4.80710259, 4.96217869,
            5.11725479, 5.2723309 , 5.427407  , 5.5824831 , 5.7375592 ,
            5.8926353 , 6.0477114 , 6.2027875 , 6.3578636 , 6.5129397 ,
            6.6680158 , 6.82309191]),
     <a list of 21 Patch objects>)




![png](numpy_files/numpy_108_1.png)



```python
# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)
```


```python
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2])
g = np.array([4,5])
### 1*4+2*5
np.dot(f, g)
```




    14




```python
## Linear algebra
### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)
```




    23




```python
# NumPy Matrix Multiplication with np.matmul() 
```


```python
### Matmul: matruc product of two arrays
h = [[1,2],[3,4]] 
i = [[5,6],[7,8]] 
### 1*5+2*7 = 19
np.matmul(h, i)
```




    array([[19, 22],
           [43, 50]])




```python
## Determinant 2*2 matrix
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
np_arr = np.array(range(0, 11))
np_arr + 2
```




    array([ 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])




```python
x = np.array([1,2,3,4,5])
y = x * 2 + 5
y
```




    array([ 7,  9, 11, 13, 15])




```python
plt.plot(x,y)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
```


![png](numpy_files/numpy_122_0.png)



```python
x = np.random.normal(size=1000)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')

```




    [Text(0, 0.5, 'y'), Text(0.5, 0, 'x')]




![png](numpy_files/numpy_123_1.png)


# Summery

To summarise, the main differences with python lists are:

1. Arrays support vectorised operations, while lists don’t.
1. Once an array is created, you cannot change its size. You will have to create a new array or overwrite the existing one.
1. Every array has one and only one dtype. All items in it should be of that dtype.
1. An equivalent numpy array occupies much less space than a python list of lists.
1. numpy arrays support boolean indexing.

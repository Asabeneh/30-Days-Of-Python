<div dir="rtl" lang="ur">

<div align="center">
  <h1>پائتھن کے 30 دن: دن 11 — فنکشنز</h1>
  <a href="https://www.linkedin.com/in/asabeneh/">
    <img alt="LinkedIn" src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&amp;logo=linkedin&amp;style=social">
  </a>
  <a href="https://twitter.com/Asabeneh">
    <img alt="Twitter پر مصنف" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>
  <p>مصنف: <a href="https://www.linkedin.com/in/asabeneh/">Asabeneh Yetayeh</a><br>دوسرا ایڈیشن: جولائی 2021</p>
</div>

[اصل انگریزی سبق](../11_Day_Functions/11_functions.md) | [تمام زبانیں](../readme.md)

[پچھلا دن: 10](./10_loops.md) | [فہرست](./readme.md) | [اگلا دن: 12](./12_modules.md)

![پائتھن کے 30 دن](../images/30DaysOfPython_banner3@2x.png)

**اس سبق کی فہرست**

- [📘 دن 11](#day-11-section-1)
  - [فنکشنز](#day-11-section-2)
    - [فنکشن کی تعریف](#day-11-section-3)
    - [فنکشن بنانا اور بلانا](#day-11-section-4)
    - [پیرامیٹر کے بغیر فنکشن](#day-11-section-5)
    - [قدر واپس کرنے والا فنکشن — حصہ 1](#day-11-section-6)
    - [پیرامیٹرز والا فنکشن](#day-11-section-7)
    - [نام اور قدر کے ساتھ آرگیومنٹ دینا](#day-11-section-8)
    - [قدر واپس کرنے والا فنکشن — حصہ 2](#day-11-section-9)
    - [طے شدہ قدروں والے پیرامیٹرز](#day-11-section-10)
    - [غیر متعین تعداد کے آرگیومنٹس](#day-11-section-11)
    - [طے شدہ قدر اور غیر متعین تعداد ایک ساتھ](#day-11-section-12)
    - [ڈکشنری کھول کر آرگیومنٹ دینا](#day-11-section-13)
    - [غیر متعین تعداد کے نام زد آرگیومنٹس](#day-11-section-14)
    - [ایک فنکشن کو دوسرے فنکشن میں دینا](#day-11-section-15)
  - [اپنی رائے دیں](#day-11-section-16)
  - [💻 مشقیں — دن 11](#day-11-section-17)
    - [مشقیں: درجہ 1](#day-11-section-18)
    - [مشقیں: درجہ 2](#day-11-section-19)
    - [مشقیں: درجہ 3](#day-11-section-20)

<a id="day-11-section-1"></a>

# 📘 دن 11

<a id="day-11-section-2"></a>

## فنکشنز

اب تک کئی بلٹ اِن فنکشنز دیکھ چکے ہیں۔ اب اپنے فنکشنز بنائیں گے۔ پہلے سمجھیں کہ فنکشن کیا ہے اور اس کی ضرورت کیوں پڑتی ہے۔

<a id="day-11-section-3"></a>

### فنکشن کی تعریف

فنکشن دوبارہ استعمال ہونے والا کوڈ کا بلاک ہے جو ایک خاص کام کرتا ہے۔ اسے بنانے کے لیے `def` استعمال ہوتا ہے۔ فنکشن کا بلاک صرف اسے بلانے، یعنی *call* کرنے، پر چلتا ہے۔

<a id="day-11-section-4"></a>

### فنکشن بنانا اور بلانا

فنکشن کی تعریف لکھنا اسے بنانا ہے، اور اسے استعمال کرنا *calling* یا *invoking* کہلاتا ہے۔ فنکشن پیرامیٹرز کے ساتھ یا بغیر بن سکتا ہے۔

<div dir="ltr">

```py
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
```

</div>

<a id="day-11-section-5"></a>

### پیرامیٹر کے بغیر فنکشن

فنکشن بغیر پیرامیٹر کے بھی بنایا جا سکتا ہے۔

**مثال:**

<div dir="ltr">

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

</div>

<a id="day-11-section-6"></a>

### قدر واپس کرنے والا فنکشن — حصہ 1

`return` سے فنکشن قدر واپس دیتا ہے۔ `return` نہ ہو تو نتیجہ `None` ہوتا ہے۔ اوپر کی مثالوں کو `return` کے ساتھ لکھیں، پھر واپس آنے والی قدر دکھائیں۔

<div dir="ltr">

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

</div>

<a id="day-11-section-7"></a>

### پیرامیٹرز والا فنکشن

فنکشن کو اعداد، سٹرنگز، بولین، لسٹس، ٹپلز، ڈکشنریز یا سیٹس جیسی مختلف قدریں دی جا سکتی ہیں۔

- ایک پیرامیٹر: فنکشن بلاتے وقت اس کے لیے آرگیومنٹ دیں۔

<div dir="ltr">

```py
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
```

</div>

**مثال:**

<div dir="ltr">

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

</div>

- دو پیرامیٹرز: فنکشن کے صفر، ایک، دو یا زیادہ پیرامیٹر ہو سکتے ہیں۔ ضروری پیرامیٹرز کے لیے آرگیومنٹ دینا ہوتے ہیں۔ دو پیرامیٹرز کی مثال:

<div dir="ltr">

```py
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
```

</div>

**مثال:**

<div dir="ltr">

```py
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

</div>

<a id="day-11-section-8"></a>

### نام اور قدر کے ساتھ آرگیومنٹ دینا

آرگیومنٹ نام کے ساتھ دیں تو انہیں پیرامیٹرز کی ترتیب میں دینا ضروری نہیں۔

<div dir="ltr">

```py
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
```

</div>

**مثال:**

<div dir="ltr">

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
```

</div>

<a id="day-11-section-9"></a>

### قدر واپس کرنے والا فنکشن — حصہ 2

قدر واپس نہ کی جائے تو `None` ملتا ہے۔ `return` کے بعد مطلوبہ متغیر یا عبارت لکھ کر کسی بھی قسم کی قدر واپس کر سکتے ہیں۔

- سٹرنگ واپس کرنا:

**مثال:**

<div dir="ltr">

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

</div>

- عدد واپس کرنا:

**مثال:**

<div dir="ltr">

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))
```

</div>

- بولین واپس کرنا:

**مثال:**

<div dir="ltr">

```py
def is_even (n):
    if n % 2 == 0:
        return True    # return stops further execution of the function, similar to break
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

</div>

- لسٹ واپس کرنا:

**مثال:**

<div dir="ltr">

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

</div>

<a id="day-11-section-10"></a>

### طے شدہ قدروں والے پیرامیٹرز

فنکشن کی تعریف میں پیرامیٹر کو طے شدہ قدر دے سکتے ہیں۔ بلاتے وقت اس کا آرگیومنٹ نہ دیں تو یہی قدر استعمال ہو گی۔

<div dir="ltr">

```py
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

</div>

**مثال:**

<div dir="ltr">

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
```

</div>

<a id="day-11-section-11"></a>

### غیر متعین تعداد کے آرگیومنٹس

آرگیومنٹس کی تعداد پہلے معلوم نہ ہو تو پیرامیٹر کے نام سے پہلے `*` لگائیں۔ اس طرح فنکشن کئی positional آرگیومنٹ قبول کر سکتا ہے۔

<div dir="ltr">

```py
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

</div>

**مثال:**

<div dir="ltr">

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

</div>

<a id="day-11-section-12"></a>

### طے شدہ قدر اور غیر متعین تعداد ایک ساتھ

<div dir="ltr">

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

</div>

<a id="day-11-section-13"></a>

### ڈکشنری کھول کر آرگیومنٹ دینا

فنکشن کے نام زد پیرامیٹرز سے ملتی کلیدوں والی ڈکشنری کو `**` سے کھول کر آرگیومنٹ دے سکتے ہیں۔

<div dir="ltr">

```py
# Define a function that takes two arguments: 'name' and 'location'
def greet(name, location):
    # Print a greeting message using the provided arguments
    print("Hi there", name, "how is the weather in", location)

# Call the function using keyword arguments
greet(name="Alice", location="New York")
# Output: Hi there Alice how is the weather in New York

# Create a dictionary with keys matching the function's parameter names
my_dict = {"name": "Alice", "location": "New York"}

# Call the function using dictionary unpacking
greet(**my_dict)
# The ** operator unpacks the dictionary, passing its key-value pairs
# as keyword arguments to the function.
# Output: Hi there Alice how is the weather in New York
```

</div>

<a id="day-11-section-14"></a>

### غیر متعین تعداد کے نام زد آرگیومنٹس

فنکشن کو کئی نام زد آرگیومنٹ قبول کرنے کے قابل بھی بنا سکتے ہیں۔

<div dir="ltr">

```py
def arbitrary_named_args(**args):
    print("I received an arbitrary number of arguments, totaling", len(args))
    print("They are provided as a dictionary in my function:", type(args))
    print("Let's print them:")
    for k, v in args.items():
        print(" * key:", k, "value:", v)
```

</div>

بلا ضرورت یہ انداز استعمال نہ کریں، کیونکہ اس سے فنکشن کے مطلوبہ ان پٹ اور کام کو سمجھنا مشکل ہو سکتا ہے۔

<a id="day-11-section-15"></a>

### ایک فنکشن کو دوسرے فنکشن میں دینا

<div dir="ltr">

```py
#You can pass functions around as parameters
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

</div>

🌕 آپ نے گیارہویں دن کا چیلنج مکمل کر لیا! مشق جاری رکھیں۔

<a id="day-11-section-16"></a>

## اپنی رائے دیں

مصنف اور 30DaysOfPython کے بارے میں اپنے خیالات اس [رابطے](https://testimonial-s3sw.onrender.com/) پر لکھ سکتے ہیں۔

<a id="day-11-section-17"></a>

## 💻 مشقیں — دن 11

<a id="day-11-section-18"></a>

### مشقیں: درجہ 1

1. `add_two_numbers` بنائیں جو دو پیرامیٹر لے اور مجموعہ واپس کرے۔
2. `area_of_circle` بنائیں جو `π * r * r` سے دائرے کا رقبہ نکالے۔
3. `add_all_nums` بنائیں جو غیر متعین تعداد کے آرگیومنٹ جمع کرے۔ سب کی عددی قسم جانچیں؛ کوئی غیر عدد ہو تو مناسب پیغام دیں۔
4. `convert_celsius_to_fahrenheit` بنائیں جو `°F = (°C * 9/5) + 32` سے درجۂ حرارت بدلے۔ اصل سوال کے نام میں ہائفن ہے؛ درست پائتھن نام کے لیے انڈر اسکور استعمال کریں۔
5. `check_season` بنائیں جو مہینہ لے اور خزاں، سردی، بہار یا گرمی واپس کرے۔
6. `calculate_slope` بنائیں جو خطی مساوات کی ڈھلوان دے۔
7. `solve_quadratic_eqn` بنائیں جو `ax² + bx + c = 0` کے حل دے۔
8. `print_list` بنائیں جو لسٹ کے ہر عنصر کو دکھائے۔
9. `reverse_list` بنائیں جو لسٹ لے اور لوپ کے ذریعے الٹی ترتیب واپس کرے۔

<div dir="ltr">

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
```

</div>

10. `capitalize_list_items` بنائیں جو لسٹ کی سٹرنگز کے ابتدائی حروف بڑے کر کے واپس کرے۔
11. `add_item` بنائیں جو لسٹ اور عنصر لے، آخر میں عنصر شامل کرے اور لسٹ واپس دے۔

<div dir="ltr">

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

```

</div>

12. `remove_item` بنائیں جو لسٹ اور ایک عنصر لے، اس عنصر کو ہٹائے اور تبدیل شدہ لسٹ واپس کرے۔

<div dir="ltr">

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

</div>

13. `sum_of_numbers` بنائیں جو عدد لے اور اس حد تک اعداد جمع کرے۔

<div dir="ltr">

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

</div>

14. `sum_of_odds` بنائیں جو اس حد تک طاق اعداد کا مجموعہ دے۔
15. `sum_of_even` بنائیں جو اس حد تک جفت اعداد کا مجموعہ دے۔

<a id="day-11-section-19"></a>

### مشقیں: درجہ 2

1. `evens_and_odds` بنائیں جو مثبت صحیح عدد لے اور صفر سے اس عدد تک جفت اور طاق اعداد کی تعداد دے۔

<div dir="ltr">

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

</div>

2. `factorial` بنائیں جو غیر منفی صحیح عدد کا فیکٹوریل دے۔
3. `is_empty` بنائیں جو دی گئی قدر کے خالی ہونے کی جانچ کرے۔
4. لسٹس کے لیے `calculate_mean`، `calculate_median`، `calculate_mode`، `calculate_range`، `calculate_variance` اور `calculate_std` بنائیں۔
5. `greet` میں `name` کی طے شدہ قدر رکھیں۔ نام نہ ملے تو `Hello, Guest!`، ورنہ نام کے ساتھ سلام دکھائیں۔

<div dir="ltr">

```py
    greet()
    # "Hello, Guest!
    greet("Alice")
    # "Hello, Alice!"
```

</div>

6. `show_args` بنائیں جو غیر متعین تعداد کے نام زد آرگیومنٹس کے نام اور قدریں دکھائے۔

<div dir="ltr">

```py
show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny
```

</div>

<a id="day-11-section-20"></a>

### مشقیں: درجہ 3

1. `is_prime` بنائیں جو عدد کے اوّل ہونے کی جانچ کرے۔
2. فنکشن بنائیں جو لسٹ کے تمام عناصر کے منفرد ہونے کی جانچ کرے۔
3. فنکشن بنائیں جو تمام عناصر کی قسم یکساں ہونے کی جانچ کرے۔
4. فنکشن بنائیں جو دیے گئے نام کے درست پائتھن متغیر ہونے کی جانچ کرے۔
5. ڈیٹا فولڈر کی [countries-data.py](../data/countries-data.py) استعمال کریں:
   - `most_spoken_languages` دس یا بیس سب سے زیادہ بولی جانے والی زبانیں گھٹتی ترتیب میں واپس کرے۔
   - `most_populated_countries` دس یا بیس سب سے زیادہ آبادی والے ممالک گھٹتی ترتیب میں واپس کرے۔

🎉 مبارک ہو! 🎉

---

[پچھلا دن: 10](./10_loops.md) | [فہرست](./readme.md) | [اگلا دن: 12](./12_modules.md)

</div>

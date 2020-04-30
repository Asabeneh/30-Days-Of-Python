<div align="center">
  <h1> 30 Days Of Python: Day 11 - Functions</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> First Edition: Nov 22 - Dec 22, 2019</small>
</sub>

</div>
</div>

[<< Day 10](../10_Day/10_loop.md) | [Day 12 >>](../12_Day/12_module.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 11](#%f0%9f%93%98-day-11)
  - [Functions](#functions)
    - [Defining a Function](#defining-a-function)
    - [Declaring and calling a function](#declaring-and-calling-a-function)
    - [Function without parameters](#function-without-parameters)
    - [Function returning value](#function-returning-value)
    - [Function with parameters](#function-with-parameters)
    - [Passing arguments with key and value](#passing-arguments-with-key-and-value)
    - [Returning a value from a function](#returning-a-value-from-a-function)
    - [Function with default parameters](#function-with-default-parameters)
    - [Arbitrary number of arguments](#arbitrary-number-of-arguments)
    - [Default and arbitrary number of parameters in function](#default-and-arbitrary-number-of-parameters-in-function)
    - [Function as parameter of other function](#function-as-parameter-of-other-function)
  - [💻 Exercises: Day 11](#%f0%9f%92%bb-exercises-day-11)

# 📘 Day 11

## Functions

So far we have seen many builtin python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, lets understand what function is and why we need function?

### Defining a Function

A function is a reusable block of code or programming statements designed to perform a certain task. To define a function, Python provides the _def_ keyword. The following is the syntax of defining a function. The function block of code only executed only if we call the function.

### Declaring and calling a function

When we make a function we call it declaring a function. When we start using the function we call it calling or invoking a function. Function can be declared with or without a parameter.

```py
  # syntax
  # Declaring a function
  def function_name():
    codes
    codes
  # Calling function
  function_name()
```

### Function without parameters

Function can be declared without a parameter.
**Example:**

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

### Function returning value

Function can also return values, if a function does not return values the value of the function is None. Lets rewrite the above functions using return. From now on, we return value to a function instead of printing it.

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

### Function with parameters

In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter

- Single Parameter: If our function takes a parameter we should call our function with an argument

```py
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  function_name(parameter)
```

**Example:**

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
    print(total)
sum_of_numbers(10) # 55
sum_of_numbers(100) # 5050
```

- Two Parameter: A function may or may not have a parameter or parameters. A function may have two or more parameters. If our function takes parameters we should call our function with arguments. Let's see function with two parameters:

```py
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  function_name(arg1, arg2)
```

**Example:**

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
      return age;

  print('Age: ', calculate_age(2019, 1819))

  def weight_of_object (mass, gravity):
      weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
      return weight
  print('Weight of an object in Newton: ', weight_of_object(100, 9.81))
```

### Passing arguments with key and value

If we pass the arguments with key and value, the order of the arguments does not matter.

```py
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  function_name(para1='John', para2='Doe') # the order of argument now does not matter
```

**Example:**

```py
  def print_fullname(firstname, lastname):
        space = ' '
        full_name = firstname  + space + lastname
        print(full_name)
  print_fullname(firstname='Asabeneh', lastname='Yetayeh')

  def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
  add_two_numbers(num2=3, num1=2) # Order does not matter
```

### Returning a value from a function

If we do not return a value from a function, then our function is returning _None_ by default. To return a value from a function we use the key word _return_ followed by the data type we are returning. We can return any kind of data types from a function.

- Returning string:
  **Example:**

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

- Returning Number:

**Example:**

```py
  def add_two_numbers (num1, num2):
          total = num1 + num2
          return total
  print(add_two_numbers(2, 3))

  def calculate_age (current_year, birth_year):
      age = current_year - birth_year
      return age;
  print('Age: ', calculate_age(2019, 1819))
```

- Returning Boolean:
  **Example:**

```py
  def is_even (n):
      if n % 2 == 0:
          print('even')
          return True
      return False
  print(is_even(10)) # True
  print(is_even(7)) # False
```

- Returning List:
  **Example:**

```py
  def find_even_numbers(n):
      evens = []
      for i in range(n+1):
          if i % 2 == 0:
              evens.append(i)
      return evens
  print(find_even_numbers(10))
```

### Function with default parameters

Sometimes we pass default values to parameters, when we invoke the function if we do not pass an argument the default value will be used.

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

**Example:**

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

  def calculate_age (birth_year,current_year = 2019):
      age = current_year - birth_year
      return age;
  print('Age: ', calculate_age(1819))

  def weight_of_object (mass, gravity = 9.81):
      weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
      return weight
  print('Weight of an object in Newton: ', weight_of_object(100)) # 9.81 gravity at the surface of Earth
  print('Weight of an object in Newton: ', weight_of_object(100, 1.62)) # gravity at surface of Moon
```

### Arbitrary number of arguments

If we do not know the number of arguments we pass to our function we can create a function which can take arbitrary number of arguments by add \* before the parameter name.

```py
  # syntax
  # Declaring a function
  def function_name(*args):
    codes
    codes
  # Calling function
  function_name(param1, param2, param3,..)
```

**Example:**

```py
  def sum_all_nums(*nums):
      total = 0
      for num in nums:
          total += num
      return total
  print(sum_all_nums(2, 3, 5))
```

### Default and arbitrary number of parameters in function

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

### Function as parameter of other function

```py
  #You can pass functions around as parameters
  def square_number (n):
      return n * n
  def do_something(f, x):
      return f(x)
  print(do_something(square_number, 3))
```

## 💻 Exercises: Day 11

1. Declare a function _add_two_numbers_ and it takes two two parameters and it returns sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function which calculates _area_of_circle_.
3. Write a function called add_all_nums which take arbitrary number of arguments and sum all the arguments. Check if all the list items are number types. If not give return reasonable feedback.
4. Temperature in oC can be converted to oF using this formula: oF = (oC x 9/5) + 32. Write a function which converts oC to oF, _convert_celcius_to-fahrenheit_.
5. Write a function called check-season, it takes a month parameter and returns the season:Autumn, Winter, Spring or Summer.
6. Write a function called calculate_slope which return the slop of a linear equation
7. Quadratic equation is calculated as follows: ax2 + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
8. Declare a function name print_list. It takes list as a parameter and it prints out each element of the list.
9. Declare a function name reverse_list. It takes array as a parameter and it returns the reverse of the array (dont’ use method).

```py
    print(reverse_list([1, 2, 3, 4, 5]))
    # [5, 4, 3, 2, 1]
    print(reverse_list1.(["A", "B", "C"]))
    # ["C", "B", "A"]
```

10. Declare a function name capitalize_list_items. It takes list as a parameter and it returns the capitalized list of the items
11.

- Declare a function name add_item. It takes a list and an item parameter and it returns a list after adding the item

```py
  food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
  print(  add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
  numbers = [2, 3,7,9];
  print(add_item(numbers, 5))      [2, 3,7,9,5]
```

- Declare a function name remove_item. It takes a list and an item parameter and it returns a list after removing an item.

```py
  food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
  print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
  numbers = [2, 3,7, 9];
  print(remove_item(numbers, 3))  # [2, 7, 9]
```

1.  Declare a function name sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

```py
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050


```

2.  Declare a function name sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
3.  Declare a function name sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
    Declare a function name evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

```py
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.
```

15. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
    Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
16. Write different functions which take lists and it calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std.
17. Write a function called is_prime, which checks if a number is prime number.
18. Write a functions which checks if all items are unique in the list.
19. Write a function which checks if all the items of the list are the same data type.
20. Write a function which check if variable if valid python variable
21. Go the data folder and access the countries-data.py file.

- Create a function called the most_spoken_languages the world and it returns the 10 or 20 most spoken countries in the world in descending order
- Create a function called the most_populated_countries and it return 10 or 20 most populated countries in descending order.

🎉 CONGRATULATIONS ! 🎉

[<< Day 10](../10_Day/10_loop.md) | [Day 12 >>](../12_Day/12_module.md)

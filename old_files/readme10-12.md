![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

🧳 [Part 1: Day 1 - 3](https://github.com/Asabeneh/30-Days-Of-Python)  
🧳 [Part 2: Day 4 - 6](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)  
🧳 [Part 3: Day 7 - 9](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)  
🧳 [Part 4: Day 10 - 12](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)  
🧳 [Part 5: Day 13 - 15](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)  
🧳 [Part 6: Day 16 - 18](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme16-18.md)  
🧳 [Part 7: Day 19 - 21](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme19-21.md)  
🧳 [Part 8: Day 22 - 24](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme22-24.md)  
🧳 [Part 9: Day 25 - 27](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme25-27.md)  
🧳 [Part 10: Day 28 - 30](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme28-30.md) 

---
- [📘 Day 10](#%f0%9f%93%98-day-10)
  - [Loops](#loops)
    - [While Loop](#while-loop)
    - [Break and continue](#break-and-continue)
    - [For Loop](#for-loop)
    - [Break and Continue](#break-and-continue)
    - [The range function](#the-range-function)
    - [Nested for loop](#nested-for-loop)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [💻 Exercises: Day 10](#%f0%9f%92%bb-exercises-day-10)
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
- [📘 Day 12](#%f0%9f%93%98-day-12)
  - [Module](#module)
    - [What is a module](#what-is-a-module)
    - [Creating a module](#creating-a-module)
    - [Importing a module](#importing-a-module)
    - [Import functions from a module](#import-functions-from-a-module)
    - [Import functions from a module and renaming](#import-functions-from-a-module-and-renaming)
  - [Import Builtin Modules](#import-builtin-modules)
    - [OS Module](#os-module)
    - [Sys Module](#sys-module)
    - [Statistics Module](#statistics-module)
    - [Math Module](#math-module)
    - [Random Module](#random-module)
  - [💻 Exercises: Day 12](#%f0%9f%92%bb-exercises-day-12)

GIVE FEEDBACK: http://thirtydayofpython-api.herokuapp.com/feedback
# 📘 Day 10
## Loops
Life is full of routines. In programming also we do lots of repetitive tasks. In order to handle repetitive task programming languages provide loops. Python programming language also provides the following types of two loops to handle looping. 
1. while loop
2. for loop
### While Loop
We use the reserved word *while* to make a while loop. While loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop will be executed.
```py
  # syntax
  while condition:
      code goes here
```
**Example:**
```py
  count = 0
  while count < 5:
      print(count)
      count = count + 1
```
In the above while loop, the condition become false when count is 5, then the loop stops.
If we are interested to run block of code once the condition is no longer true, we can use *else*.
```py
  # syntax
  while condition:
      code goes here
  else:
      code goes here
```
**Example:**
```py
  count = 0
  while count < 5:
        print(count)
        count = count + 1
  else:
      print(count)
```
The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement and 5 prints in the else statement.
### Break and continue
* Break: We use break when we like to get out or stop the loop.
```py
  # syntax
  while condition:
      code goes here
      if another_condition:
          break 
```
**Example:**
```py
  count = 0
  while count < 5:
      print(count)
      count = count + 1
      if count == 3:
          break
```
The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.
* Continue: With the continue statement we can stop the current iteration, and continue with the next:
```py
  # syntax
  while condition:
      code goes here
      if another_condition:
          continue
```
**Example:**
```py
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
```
The above while loop only prints 0, 1, 2,4 but skips 3.
### For Loop 
A *for* key word used to make a for loop like in other programming language but with some syntax difference.  Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
* For loop with list 
```py
  # syntax
  for iterator in lst:
    code goes here
```
  **Example:**

```py
  numbers = [0, 1, 2, 3, 4, 5]
  for number in numbers:
      print(number)
```
* For loop with string
```py
  # syntax
  for iterator in string:
    code goes here
```
  **Example:**

```py
  language = 'Python'
  for letter in language:
    print(letter)
```
* For loop with tuple
```py
  # syntax
  for iterator in tpl:
    code goes here
```
  **Example:**
```py
  numbers = (0, 1,2,3,4,5)
  for number in numbers:
    print(number)
```
* For loop with dictionary
  Looping through a dictionary gives you the key of the dictionary.
```py
  # syntax
  for iterator in dct:
    code goes here
```
  **Example:**
```py
  person = {
      'first_name':'Asabeneh',
      'last_name':'Yetayeh',
      'age':250,
      'country':'Finland',
      'is_marred':True,
      'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
      'address':{
          'street':'Space street',
          'zipcode':'02210'
      }
      }
  for key in person:
    print(key)

  for key, value in person.items():
    print(key, value) # 
```
* Loops in set
```py
  # syntax
  for iterator in st:
    code goes here
```
  **Example:**
```py
  it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
  for company in it_companies:
    print(company)
```
### Break and Continue
*Break*: We use break when we like to stop our loop before the loop is completed.
```py
  # syntax
  for iterator in sequence:
    code goes here
    if condition:
      break
```
  **Example:**

```py
  numbers = (0, 1,2,3,4,5)
  for number in numbers:
    print(number)
    if number == 3:
      break
```
  In the above example, the loop stops when it reaches 3.
  Continue: We use continue when we like to skip some of the step in the iteration of the loop.

```py
  # syntax
  for iterator in sequence:
    code goes here
    if condition:
      continue
```
    **Example:**
    
```py
  numbers = (0, 1,2,3,4,5)
  for number in numbers:
    print(number)
    if number == 3:
      continue
```
 In the above example, if number is 3 the skip step and continues to the next.
### The range function
The range() function uses to loop through a set of code a certain number of times. The *range(start,end, step)* takes three parameters:starting, ending and increment.By default it starts from 0 and the increment is 1. The range sequence doesn't include the end.
Creating sequence using range

```py
  lst = list(rang(11)) 
  print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  st = set(range(11))
  print(st) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

  lst = list(rang(0,11,2)) 
  print(lst) # [0, 2, 4, 6, 8, 10]
  st = set(range(0,11,2))
  print(st) #  {0, 2, 4, 6, 8, 10}
```
```py
  # syntax
  for iterator in range(start, end, increment):
```
  **Example:**
  
```py
  for number in range(11):
    print(number)   # prints 0 to 10, not including 11
  fruits = ['banana', 'orange', 'mango', 'lemon']
  for fruit in fruits:
    print(fruit)
```
###  Nested for loop
We can write loop inside another loop.
```py
  # syntax
  for x in y:
    for t in s:
      print(t)
```
  **Example:**
```py
  person = {
      'first_name': 'Asabeneh',
      'last_name': 'Yetayeh',
      'age': 250,
      'country': 'Finland',
      'is_marred': True,
      'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
      'address': {
          'street': 'Space street',
          'zipcode': '02210'
      }
  }
  for key in person:
      if key == 'skills':
        for skill in person['skills']:
          print(skill)
  
```
### For Else
If we want to execute some message when the loop ends, we use else.
```py
  # syntax
  for iterator in range(start, end, increment):
    do something
  else:
    print('The loop is ended')
```
  **Example:**
```py
  for number in range(11):
    print(number)   # prints 0 to 10, not including 11
  else:
    print('The loop stops at', number)
```
### Pass
In python after semicolon, it requires some code to run but we don't like to execute any code after if or for loop we can write the word *pass* to avoid error.

## 💻 Exercises: Day 10
1. Iterate 0 to 10 using for loop, do the same using while and do while loop.
2. Iterate 10 to 0 using for loop, do the same using while and do while loop.
3. Write a loop that makes seven calls to print() output the following triangle:
    ```py
      #
      ##
      ###
      ####
      #####
      ######
      #######
    ```
4. Use nested loops to create the following:
    ```sh
    # # # # # # # # 
    # # # # # # # # 
    # # # # # # # # 
    # # # # # # # # 
    # # # # # # # # 
    # # # # # # # # 
    # # # # # # # # 
    # # # # # # # #
    ```
5. Print the following pattern:
    ```sh
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100
    ```
6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
7. Use for loop to iterate from 0 to 100 and print only even numbers
8. Use for loop to iterate from 0 to 100 and print only odd numbers
9. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    ```sh
    The sum of all numbers is 5050.
    ```
10. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    ```sh
      The sum of all evens is 2550. And the sum of all odds is 2500.
    ```
11. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word *land*.
12. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

# 📘 Day 11
## Functions
So far we have seen many builtin python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, lets understand what function is and why we need function?
### Defining a Function
A function is a reusable block of code or programming statements designed to perform a certain task. To define a function, Python provides the *def* keyword. The following is the syntax of defining a function. The function block of code only executed only if we call the function.
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
* Single Parameter: If our function takes a parameter we should call our function with an argument
```py
  # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  function_name(parameter)
````
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
* Two Parameter: A function may or may not have a parameter or parameters. A function may have two or more parameters. If our function takes parameters we should call our function with arguments. Let's see function with two parameters:
```py
  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  function_name(arg1, arg2)
````
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
````
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
If we do not return a value from a function, then our function is returning *None* by default. To return a value from a function we use the key word *return* followed by the data type we are returning. We can return any kind of data types from a function.
* Returning string:
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
* Returning Number:

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
* Returning Boolean:
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
* Returning List:
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
Sometimes we pass default values to parameters, when we invoke the function if we do not  pass an argument the default value will be used.
```py
  # syntax
  # Declaring a function
  def function_name(param = value):
    codes
    codes
  # Calling function
  function_name()
  function_name(arg)
````
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
If we do not know the number of arguments we pass to our function we can create a function which can take arbitrary number of arguments by add * before the parameter name.
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
1. Declare a function *add_two_numbers* and it takes two two parameters and it returns sum.
2. Area of a circle is calculated as follows: area = π x r x r. Write a function which calculates *area_of_circle*.
3. Write a function called add_all_nums which take arbitrary number of arguments and sum all the arguments.  Check if all the list items are number types. If not give return reasonable feedback.
4. Temperature in oC can be converted to oF using this formula: oF = (oC x 9/5) + 32. Write a function which converts oC to oF, *convert_celcius_to-fahrenheit*.
5. Write a function called check-season, it takes a month parameter and returns the season:Autumn, Winter, Spring or Summer.
6. Write a function called calculate_slope which return the slop of a linear equation
7. Quadratic equation is calculated as follows: ax2 + bx + c = 0. Write a function which calculates solution set of a quadratic equation, *solve_quadratic_eqn*.
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
* Declare a function name add_item. It takes a list and an item parameter and it returns a list after adding the item
  
```py
  food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
  print(  add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
  numbers = [2, 3,7,9];
  print(add_item(numbers, 5))      [2, 3,7,9,5]
```
* Declare a function name remove_item. It takes a list and an item parameter and it returns a list after removing an item.
  
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
Call your function *is_empty*, it takes a parameter and it checks if it is empty or not
16. Write different functions which take lists and it calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std. 
17. Write a function called is_prime, which checks if a number is prime number.
18. Write a functions which checks if all items are unique in the list.
19. Write a function which checks if all the items of the list are the same data type.
20. Write a function which check if variable if valid python variable 
21. Go the data folder and access the countries-data.py file. 
* Create a function called the most_spoken_languages the world and it returns the 10 or 20 most spoken countries in the world in descending order
* Create a function called the most_populated_countries and it return 10 or 20 most populated countries in descending order.

# 📘 Day 12
## Module
### What is a module
A module is a file containing set of codes or a set of function which can be included to an application. A module could be a file containing a single variable, or function, a big code base.  
### Creating  a module
To create a module we write our codes in a python script and we save it as .py file. Create a file named mymodule.py inside your project folder. Let write code on this file.
```py
# mymodule.py file
def generate_full_name(firstname, lastname):
      space = ' '
      fullname = firstname + space + lastname
      return fullname
```
Create main.py file in your project directory and import the mymodule.py file.
### Importing a module
To import the file we use the *import* keyword and the name of the file only.
```py
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))
```
### Import functions from a module
We can have many functions in a file and we can import all the functions differently.
```py
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetay'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
```
### Import functions from a module and renaming
During importing we can rename the name of the module.
```py
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1,9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```
## Import Builtin Modules
Like other programming languages we can also import modules  by importing the file/function using the key word *import*. Lets import the common module we will use most of the time. Some of the common builtin modules *math*, *datetime*, *os*,*sys*, *random*, *statistics*, *collections*, *json*,*re*
### OS Module
Using python *os* module it is possible to automatically perform many operating system tasks.The OS module in Python provides functions for creating, changing current working directory,  and removing a directory (folder), fetching its contents, changing and identifying the current directory.
```py
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```
### Sys Module
The sys module provides functions and variables used to manipulate different parts of the Python runtime environment. sys.argv returns a list of command line arguments passed to a Python script. The item at index 0 in this list is always the name of the script, at index 1 is argument passed from the command line.
```py
import sys
print(sys.argv[0], argv[1],sys.argv[2])
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
output
Welcome Asabeneh. Enjoy  30DayOfPython challenge!

# to exist syst
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
syst.path
# To know the version of python you are using
sys.version
```
### Statistics Module
The statistics module provides functions to mathematical statistics of numeric data. The  popular statistical functions which are defined in this module *mean*, *median*, *mode*, *stdev* etc.
```py
from statistics import * # importing all the statistics module
print(mean(ages))       # 22.4
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # 2.3
```
### Math Module
  ```py
  import math
  print(math.pi)           # 3.141592653589793, pi constant
  print(math.sqrt(2))      # 1.4142135623730951, square root
  print(math.pow(2, 3))    # 8.0, exponential
  print(math.floor(9.81))  # 9, rounding to the lowest
  print(math.ceil(9.81))   # 10, rounding to the highest
  print(math.log10(100))   # 2 
  ```
Now, we have imported the math module which contains lots of function which can help us to perform mathematical calculations.To check what functions the module has, you can use *help(math)*, or dir(math) and this will display the available functions in the module. If we want to import only a specific function from a module we import as follow:
  ```py
  from math import pi
  print(pi)
  ```
It is also possible to import multiple functions at once
  ```py

  from math import pi, sqrt, pow, floor, ceil,log10
  print(pi)                 # 3.141592653589793
  print(sqrt(2))            # 1.4142135623730951
  print(pow(2, 3))          # 8.0
  print(floor(9.81))        # 9
  print(ceil(9.81))         # 10
  print(math.log10(100))    # 2 

  ```
But if we want to import all the function in math module we can use * . 
  ```py
  from math import *
  print(pi)                  # 3.141592653589793, pi constant
  print(sqrt(2))             # 1.4142135623730951, square root
  print(pow(2, 3))           # 8.0, exponential
  print(floor(9.81))         # 9, rounding to the lowest
  print(ceil(9.81))          # 10, rounding to the highest
  print(math.log10(100))     # 2 
  ```
When we import we can also rename the name of the function. 
  ```py
  from math import pi as  PI
  print(PI) # 3.141592653589793
  ```
### Random Module
By now you are familiar with importing modules. Lets do another more import to be very familiar with importing. Let's import *random* module which can gives random number between 0 and 0.9999.... The *random* module has lots of functions but in this section we will only see *random* and *randint*.
  ```py
  from random import random, randint
  print(random())   # it doesn't take argument and return 0 to 0.9999
  print(randint(5, 20)) # it returns a random number between 5 and 20
  ```
## 💻 Exercises: Day 12
1. Writ a function which generates a six digit random_user_id.
    ```py
      print(random_user_id());
      '1ee33d'
    ```
2. Modify question number above . Declare a function name user_id_gen_by_user. It doesn’t take any parameter but it takes two inputs using input(). One of the input is the number of characters and the second input is the number of ids which are supposed to be generated.
    ```py
    user_id_gen_by_user()
    "kcsy2
    SMFYb
    bWmeq
    ZXOYh
    2Rgxf
    "
    user_id_gen_by_user()
    "1GCSgPLMaBAVQZ26
    YD7eFwNQKNs7qXaT
    ycArC5yrRupyG00S
    UbGxOFI7UXSWAyKN
    dIV0SSUTgAdKwStr
    "
    ```
3. Write a function name rgb_color_gen and it generates rgb colors.
    ```py
          print(rgb_color_gen())
        # rgb(125,244,255)
    ```
4. Write a function list_of_hexa_colors which return any number of hexadecimal colors in an array.
5. Write a function list_of_rgb_colors which return any number of RGB colors in an array.
Write a function generate_colors which can generate any number of hexa or rgb colors.
    ```py
          generate_colors('hexa', 3)
          # ['#a3e12f','#03ed55','#eb3d2b']
          generate_colors('hexa', 1)
          # '#b334ef'
          generate_colors('rgb', 3)
          # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
          generate_colors('rgb', 1)
          # 'rgb(33,79, 176)'
    ```
1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
1. Write a function which returns array of seven random numbers in a range of 0-9. All the numbers must be unique.

[<< Part 3 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md) | [Part 5 >>](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme13-15.md)
***

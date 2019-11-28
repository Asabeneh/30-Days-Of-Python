[Part 1](https://github.com/Asabeneh/30-Days-Of-Python) | [Part 2](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme4-6.md)| [Part 3](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md)| [Part 4](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme10-12.md)| [Part 5](#)

![30DaysOfPython](./images/30DaysOfPython_banner3@2x.png)

- [Day 10](#day-10)
  - [Loops](#loops)
    - [While Loop](#while-loop)
    - [Break and continue](#break-and-continue)
    - [For Loop](#for-loop)
    - [Break and Continue](#break-and-continue)
    - [The range function](#the-range-function)
    - [Nested for loop](#nested-for-loop)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [Exercises: Day 10](#exercises-day-10)
# Day 10
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
    if another_conditon:
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
    if another_conditon:
        continue
 
```
**Example:**
 
```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        continue
```
The above while loop only prints 0, 1, 2,4 but skips 3.
### For Loop 
A *for* key word used to make a for loop like in other programming language but with some syntax difference.  Loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

* For loop with list
  ```py
  # syntax
  for iterator in sequecne:
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
  for iterator in sequecne:
    code goes here
  
  ```
  **Example:**
  
  ```py
  language = 'Python'
  for letter in language:
    prin(letter)
  ```
* For loop with tuple
  ```py
  # syntax
  for iterator in sequecne:
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
    for iterator in sequecne:
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
  ```
  * Loops in set

    ```py
    # syntax
    for iterator in sequecne:
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
      for iterator in sequecne:
        code goes here
        if conditon:
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
      for iterator in sequecne:
        code goes here
        if conditon:
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
    pirnt('The loop stops at', number)
  
  ```
### Pass
In python after semicolon, it requires some code to run but we don't like to execute any code after if or for loop we can write the word *pass* to avoid error.

## Exercises: Day 10
1. Iterate 0 to 10 using for loop, do the same using while and do while loop.
1. Iterate 10 to 0 using for loop, do the same using while and do while loop.

1. Write a loop that makes seven calls to print() output the following triangle:
    ```py
      #
      ##
      ###
      ####
      #####
      ######
      #######
    ```
1. Use nested loops to create the following:
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
1. Print the following pattern:
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
1. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
1. Use for loop to iterate from 0 to 100 and print only even numbers
1. Use for loop to iterate from 0 to 100 and print only odd numbers
1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
    ```sh
    The sum of all numbers is 5050.
    ```
1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
    ```sh
      The sum of all evens is 2550. And the sum of all odds is 2500.
    ```
1. Go to the data folder and use the countries.py file. Loop throught the countries and extract all the contries containing the word *land*.
1. This is the fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

[<< Part 3 ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/readme7-9.md) | [Part 5 >>](#)
***


<div align="center">
  <h1> 30 Days Of Python: Day 7 - Conditionals</h1>
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

[<< Day 8](../08_Day/08_dictionary.md) | [Day 10 >>](../10_Day/10_loop.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Day 9](#%f0%9f%93%98-day-9)
  - [Conditionals](#conditionals)
    - [If condition](#if-condition)
    - [If Else](#if-else)
    - [If elif else](#if-elif-else)
    - [Short Hand](#short-hand)
    - [Nested condition](#nested-condition)
    - [If condition and and logical operator](#if-condition-and-and-logical-operator)
    - [If and or logical operator](#if-and-or-logical-operator)
  - [💻 Exercises: Day 9](#%f0%9f%92%bb-exercises-day-9)

# 📘 Day 9

## Conditionals

By default, statements in python script executed sequentially from top to bottom. If the processing logic require so, the sequential flow of execution can be altered in two way:
* Conditional execution: a block of one or more statements will be executed if a certain expression is true
* Repetitive execution: a block of one or more statements will be repetitively executed as long as a certain expression is true. In this section, we will cover * if*, *else*, *elif* statements. The comparison and logical operator we learned in the previous sections will be useful here.

### If condition

In python and other programming languages the key word * if* use to check if a condition is true and to execute the block code. Remember the indentation after the colon.
```py
# syntax
if condition:
    this part of code run for truthy condition
```
**Example: **
```py
a = 3
if a > 0:
    print('A is a positive number')
# a is a positive number
```
As you can see in the above condition, 3 is greater than 0 and it is a positive number. The condition was true and the block code was executed. However, if the condition is false, we do not see a result. In order to see the result of the falsy condition, we should have another block, which is going to be * else*.

### If Else

If condition is true the first block will be executed, if not the else condition will run.
```py
# syntax
if condition:
    this part of code run for truthy condition
else:
     this part of code run for false condition
```
**Example: **
```py
a = 3
if a < 0:
    print('A is a positive number')
else:
    print('A is a negative number')
```
The above condition is false, therefore the else block was executed. How about if our condition is more than two, we will use * elif*.

### If elif else

On our daily life, we make decision on daily basis. We make decision not by checking  one or two conditions instead multiple conditions. As similar to life, programming is also full conditions. We use * elif* when we have multiple conditions.
```py
# syntax
if condition:
    code
elif condition:
    code
else:
    code

```
**Example: **
```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### Short Hand

```py
# syntax
code if condition else code
```
**Example: **
```py
a = 3
print('A is positive') if a > 0 else print('A is negative')
```

### Nested condition

Condition can be nested
```py
# syntax
if condition:
    code
    if condition:
    code
```
**Example: **
```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is positive even integer')
    else:
        print('A positive number')
elif a == 0:
    print('Zero')
else:
    print('A negative number')

```
We can avoid writing nested condition by using logical operator, *and*.

### If condition and and logical operator

```py
# syntax
if condition and condition:
    code
```
**Example: **
```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is even positive integer')
elif a > 0 and a % 2 != = 0:
     print('A is positive integer')
elif a == 0:
    print('Zero')
else:
    print('A negative number')
```
### If and or logical operator
```py
# syntax
if condition or condition:
    code
```
**Example: **
```py
a = 0
if a > 0 or % 2 == 0:
        print('A is positive integer')
elif a == 0:
    print('Zero')
else:
    print('A negative number')
```

## 💻 Exercises: Day 9

1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive but if not 18 give feedback to wait for the years he supposed to wait for. Output:
    ```sh
    Enter your age: 30
    You are old enough to drive.
    Output:
    Enter your age: 15
    You are left with 3 years to drive.
    ```
1. Compare the values of my_age and your_age using if … else. Based on the comparison print who is older(me or you). Use input(“Enter your age: ”) to get the age as input. Output:
    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```
1. Get two numbers from user using, input prompt. If a is greater than b return a is greater than b, if a is less b return a lesson b, else a is equal to b. Output:
    ```sh
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
    ```
1. Write a code which give grade to students according to theirs scores:
    ```sh
    80-100, A
    70-89, B
    60-69, C
    50-59, D
    0 - 49, F
    ```
1. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
September, October or November, the season is Autumn.
December, January or February, the season is Winter.
March, April or May, the season is Spring
June, July or August, the season is Summer
1. The following list contains some fruits:
    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```
    If a fruit doesn't exist in the list add the fruit in the list and print the modified list but if the fruit exists print('A fruit already exist in the list')
        1. Here we have a person dictionary.
    ```py
        person={
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
    ```
        * Check if the person dictionary has skills, if it has skills key check print out the middle skill in the skills list.
        * Check if the person dictionary has skills, if it has skills key check if the person has 'Python' skill and print the skill.
        * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
        * If the person is married and if he lives in Finland, print the following:
    ```py
        Asabeneh Yetayeh lives in Finland. He is married.
    ```

🎉 CONGRATULATIONS ! 🎉

[<< Day 8](../08_Day/08_dictionary.md) | [Day 10 >>](../10_Day/10_loop.md)

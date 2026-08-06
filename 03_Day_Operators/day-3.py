# Arithmetic Operations in Python
# Integers

print(f'Addition: {1 + 2}')
print(f'Subtraction: {2 - 1}')
print(f'Multiplication: {2 * 3}')
# Division in python gives floating number
print(f'Division: {4 / 2}')
print(f'Division: {6 / 2}')
print(f'Division: {7 / 2}')
# gives without the floating number or without the remaining
print(f'Division without the remainder: {7 // 2}')
print(f'Modulus: {3 % 2}')                           # Gives the remainder
print(f'Division without the remainder: {7 // 3}')
print(f'Exponential: {3 ** 2}')                     # it means 3 * 3

# Floating numbers
print(f'Floating Number, PI: {3.14}')
print(f'Floating Number, gravity: {9.81}')

# Complex numbers
print(f'Complex number: {1+1j}')
print(f'Multiplying complex number: {(1+1j) * (1-1j)}')

# Declaring the variable at the top first

a = 3  # a is a variable name and 3 is an integer data type
b = 2  # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total)  # if you don't label your print with some string, you never know from where is  the result is coming
print(f'a + b = {total}')
print(f'a - b = {diff}')
print(f'a * b = {product}')
print(f'a / b = {division}')
print(f'a % b = {remainder}')
print(f'a // b = {floor_division}')
print(f'a ** b = {exponential}')

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print(f'total: {total}')
print(f'difference: {diff}')
print(f'product: {product}')
print(f'division: {div}')
print(f'remainder: {remainder}')


# Calculating area of a circle
radius = 10                                 # radius of a circle
# two * sign means exponent or power
area_of_circle = 3.14 * radius ** 2
print(f'Area of a circle: {area_of_circle}')

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print(f'Area of rectangle: {area_of_rectangle}')

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print(f'True == True: {True == True}')
print(f'True == False: {True == False}')
print(f'False == False: {False == False}')
print(f'True and True: {True and True}')
print(f'True or False: {True or False}')

# Another way comparison
# 'is' checks for object identity, while '==' checks for value equality.
# For comparing values (like numbers), it is safer to use '=='.
# True - because the data values are the same
print(f'1 is 1: {1 is 1}')
print(f'1 is not 2: {1 is not 2}')           # True - because 1 is not 2
print(f"'A' in 'Asabeneh': {'A' in 'Asabeneh'}")  # True - A found in the string
print(f"'B' in 'Asabeneh': {'B' in 'Asabeneh'}")  # False -there is no uppercase B
# True - because coding for all has the word coding
print(f"'coding' in 'coding for all': {'coding' in 'coding for all'}")
print(f"'a' in 'an': {'a' in 'an'}")      # True
print(f'4 is 2 ** 2: {4 is 2 ** 2}')   # True, but using '==' is recommended for value comparison

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False

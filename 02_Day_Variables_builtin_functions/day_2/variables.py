# Exercises: Level 1
#'Day 2: 30 Days of python programming'
# 1º Declare a first name variable and assign a value to it
from math import pi


first_name = 'Noe'
# 2º Declare a last name variable and assign a value to it
last_name = 'Sola'
# 3º Declare a full name variable and assign a value to it
full_name = 'Noe Sola'
# 4º Declare a country variable and assign a value to it
country = 'Spain'
# 5º Declare a city variable and assign a value to it
city = 'Córdoba'
# 6º Declare an age variable and assign a value to it
age = 34
# 7º Declare a year variable and assign a value to it
year = 2022
# 8º Declare a variable is_married and assign a value to it
is_married = False
# 9º Declare a variable is_true and assign a value to it
is_true = True
# 10º Declare a variable is_light_on and assign a value to it
is_light_on = False
# 11º Declare multiple variable on one line
first_name, last_name, full_name, country, city, is_married = 'Noe','Sola','Noe Sola','Spain','Córdoba',False

# Exercises: Level 2
# 1º Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(age))
print(type(year))
print(type(is_married))

# 2º Using the len() built-in function, find the length of your first name
print(len('Noe'))
# 3º Compare the length of your first name and your last name
print(len('Noe'))
print(len('Sola'))
# 4º Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
    # Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
    #  Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
    # Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
    # Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
    #  Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
resto = num_two % num_one   
    #  Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two   
    # Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two    
# 5º The radius of a circle is 30 meters.
    #  Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = pow(30,2)
    #  Take radius as user input and calculate the area.
radius = input('radius of a circle is..')
result =pow(radius,2)
# 6ºUse the built-in input function to get first name, last name, country and age from a user and store the value to  their corresponding variable names
first_name = input('What is your name: ')
last_name = input('What is your last name: ')
country = input('what is your country')
age = input('How old are you? ')
# 7º Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords


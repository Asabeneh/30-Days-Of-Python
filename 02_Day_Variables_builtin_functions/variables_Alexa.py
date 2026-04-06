#Day 2: 30 days of python programming 

import math
import keyword


first_name = 'Alexa'
last_name = 'Garcia'
full_name = first_name + " " + last_name

country = 'United States'
city = 'Salt Lake City'
age = 37
year = 2025
is_married = False
is_true = True
is_light_on = True
demographics = {
    'full_name': full_name,
    'country': country,
    'city': city
}


print(first_name)
print(len(first_name))

print(last_name)
print(len(last_name))

print(full_name)
print(len(full_name))

print(country)
print(len(country))

print(city)
print(len(city))

print(age) #int has no len

print(year) #int has no len

print(is_married) #bool has no len

print(is_true) #bool has no len

print(is_light_on) #bool has no len

print(demographics)
print(len(demographics))

#assigning int values to find sum
num_one = 5
num_two = 4
total_sum = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
result = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

#Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = math.pi * (radius ** 2)
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius

##Take radius as user input and calculate the area
# Get radius as user input
radius = float(input("Enter the radius of the circle:" + " "))
# Calculate the area
area = math.pi * (radius ** 2)
# Display the result
print(f"The area of the circle with radius {radius} is: {area}")

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_first_name = input("First Name:" + " ")
user_last_name = input("Last Name:" + " ")
user_country = input("Country:" + " ")
user_age = int(input("Age:" + " "))

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
#'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
#'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
#'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

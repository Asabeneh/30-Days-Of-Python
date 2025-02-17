# Exercise 1
import math
first_name = 'Carlos'
last_name = 'Ayala'
full_name = first_name + ' ' + last_name
country = 'Peru'
city = 'Arequipa'
age = 44
year = 2022
is_married = True
is_true = True
is_light_on = False
multiple, variables, to, see = True, False, 10, 'Keys'

# Exercise 2
print("type(first_name):", type(first_name))
print("type(last_name):", type(last_name))
print("type(full_name):", type(full_name))
print("type(country):", type(country))
print("type(city):", type(city))
print("type(age):", type(age))
print("type(year):", type(year))
print("type(is_married):", type(is_married))
print("type(is_true):", type(is_true))
print("type(is_light_on):", type(is_light_on))
print("type(multiple):", type(multiple))
print("type(variables):", type(variables))
print("type(to):", type(to))
print("type(see):", type(see))

print('len(first_name):', len(first_name))
print('len(first_name) == len(last_name)', len(first_name) == len(last_name))
num_one, num_two = 5, 4
print("num_one:", num_one, "num_two:", num_two)
total = num_one + num_two
print('total:', total)
diff = num_one - num_two
print('diff:', diff)
product = num_two * num_one
print('product:', product)
division = num_one / num_two
print('division:', division)
reminder = num_two % num_one
print('reminder:', reminder)
exp = num_one ** num_two
print('exp:', exp)
floor_division = num_one // num_two
print('floor_division:', floor_division)
radius = 30
print('radius:', radius)
area_of_circle = math.pi * (radius ** 2)
print('area_of_circle:', area_of_circle)
circum_of_circle = math.pi * 2 * radius
print('circum_of_circle:', circum_of_circle)
user_radius = input('Enter circle radius: ')
print("Area:", math.pi * (float(user_radius) ** 2))

user_first_name = input('Enter user first name: ')
user_last_name = input('Enter user last name: ')
user_country = input('Enter user country: ')
user_age = input('Enter user age: ')
print(help('keywords'))

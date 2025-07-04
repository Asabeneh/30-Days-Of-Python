# Day 2: 30 Days of python programming
#declare variables 
first_name, last_name = "pac", "man"
full_name = first_name + " " + last_name
city, country = "cle", "usa"
age = 42
year = 1983
is_married = False
is_true = False
is_light_on = False

# Exercises: Level 2
# question 1
print("question 1")
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(city))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Exercises: Level 2
# question 2
print("question 2")
print(len(first_name))
print(len(last_name))

# Exercises: Level 2
# question 3
print("question 3")
print('The hash for First Name is ' + str(hash(first_name)))
print('The hash for First Name is ' + str(hash(last_name)))
print(hash(first_name)==hash(last_name))
print(len(first_name)==len(last_name))


# Exercises: Level 2
# question 4
print("question 4")
num_one = 5
num_two = 4
print(num_one)
print(num_two)

# Exercises: Level 2
# question 5
print("question 5")
add_one_two =  num_one + num_two

# Exercises: Level 2
# question 6
print("question 6")
sub_one_two =  num_two - num_one

# Exercises: Level 2
# question 7
print("question 7")
mult_one_two = num_one * num_two

# Exercises: Level 2
# question 8
print("question 8")
div_one_two = num_one / num_two

# Exercises: Level 2
# question 9
print("question 9")
mod_rem_one_two = num_one % num_two

# Exercises: Level 2
# question 10
print("question 10")
exp_one_two = ((num_one) ** (num_two))

# Exercises: Level 2
# question 11
print("question 11")
flr_div_one_two = ((num_one) // (num_two))

# Exercises: Level 2
# question 12
print("question 12")
#12.1
import math
radius = 30
area_of_circle = (math.pi)*((radius)**2)
print(area_of_circle)

#12.2
circum_of_circle = 2*(math.pi)*radius
print(circum_of_circle)

# 12.3
user_radius = float(input('what is the radius? '))
user_area_of_circle = (math.pi)*((user_radius)**2)
print(user_area_of_circle)


#question 13
print("question 13")
user_fname = str(input('First name? '))
user_lname = str(input('Last name? '))
user_age = str(input('How old? '))
user_origin = str(input('Where from? '))

print(user_fname, user_lname, user_age, user_origin)

# question 14
print("question 14")
user_help_topic = input('What python topic do you want help for?')
print('very good... here you are')
help(user_help_topic)

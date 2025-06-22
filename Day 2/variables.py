# Day 2: 30 Days of python programming
# ! Level 1
first_name = "Ahmad"
last_name = "Al-Sanosi"
full_name = first_name + " " + last_name
country = "Sudan"
city = "Khartoum"
age = 21
year = 2003
is_married = False
is_true = True
is_light_on = False
street_num, building_num, room_num = 4, 21, 623

# ! Level 2
print(f"The data type of {first_name} is {type(first_name)}")
print(f"The data type of {last_name} is {type(last_name)}")
print(f"The data type of {full_name} is {type(full_name)}")
print(f"The data type of {country} is {type(country)}")
print(f"The data type of {city} is {type(city)}")
print(f"The data type of {age} is {type(age)}")
print(f"The data type of {year} is {type(year)}")
print(f"The data type of {is_married} is {type(is_married)}")
print(f"The data type of {is_light_on} is {type(is_light_on)}")
print(f"The data type of {street_num} is {type(street_num)}")
print(f"The data type of {building_num} is {type(building_num)}")
print(f"The data type of {room_num} is {type(room_num)}")

print(f"The length of {first_name} is {len(first_name)} while the length of the {last_name} is {len(last_name)}")

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two
print(f"we have two numbers {num_one} and {num_two}")
print(f"The sum of {num_one} plus {num_two} equals {total}")
print(f"The difference of {num_one} minus {num_two} equals {diff}")
print(f"The product of {num_one} times {num_two} equals {product}")
print(f"The quotient of {num_one} over {num_two} equals {division}")
print(f"The remainder when dividing {num_two} by {num_one} is {remainder}")
print(f"The product of raising {num_one} to the power of {num_two} equals {exp}")
print(f"The floor division of {num_one} by {num_two} equals {floor_division}")

radius_string = input('Enter a radius of a circle: ')
radius = int(radius_string)
area_of_circle = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius
print(f"""The area of a circle of radius {radius} meters is equal to {area_of_circle}
and the circumference of that circle equals {circum_of_circle}""")

first_name = input('Enter your first name :')
last_name = input('Enter your last name :')
country = input('Enter your country :')
age = input('Enter your age :')




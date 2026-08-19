# 'Day 2: 30 Days of python programming'

firstname = 'sehyun'
lastname = 'chin'
fullname = 'chinsehyun'
country = 'korea'
city = 'seoul'
age = 23
year = 2004
is_married = 'no'
is_true = 'yes'

print(type(firstname))
print(type(lastname))
print(type(fullname))
print(type(age))

print(len(firstname))
print(len(lastname))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
rimainder = num_one % num_two
exp = num_one **num_two

print(total, diff, product, division, rimainder, exp)

import math
circle = int(input("원의 반지름을 지정하세요: "))

area_of_circle = math.pi*circle **2 
circum_of_circle = 2* math.pi * circle

print(area_of_circle)
print(circum_of_circle)


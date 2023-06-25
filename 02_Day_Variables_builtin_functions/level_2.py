#Day 2 : 30 Days of python programming
import math
firstName = "Dito"
lastName  = "Laksana"
fullName = "Emmanuel Krishnandito Laksana"
country  = "Wakanda"
city = "YK"
age = 19
year = 2023
is_married = False
is_true  = True
is_light_on  =False


print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))


f = len(firstName)
l = len(lastName)

if(f > l ):
    print("My first name is greater than last name")

else:
    print("My first  name is smaller than last name  ")


num_one = 5
num_two = 4



total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = math.pow(num_one , num_two)
floor_division = num_two // num_one




radius  =(int(input('radius : ? ')))

area_of_circle = math.pi * math.pow(radius , 2 )
circum_of_circle = 2 * math.pi * radius
print(area_of_circle)
print(circum_of_circle)
# Declare your age as integer variable
age=30
# Declare your height as a float variable
height=5.10
# Declare a variable that store a complex number
complex=1+4j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

# base=float(input("Enter the base value:"))
# height=float(input("Enter the height value:"))
# area=0.5*base*height
# print("The area of the triangle is:", area)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

# a=float(input("Enter the value of a:"))
# b=float(input("Enter the value of b:"))
# c=float(input("Enter the value of c:"))
# perimeter=a+b+c
# print("The perimeter of the triangle is:", perimeter)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

# l=float(input("Enter the value of length:"))
# w=float(input("Enter the value of width:"))
# area=l*w
# perimeter=2*(l+w)
# print("The area of the rectangle is", area)
# print("The perimeter of the rectangle is", perimeter)
# print("The length of the rectangle is:", l)
# print("The width of rectangle is:", w)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
# r=float(input("Enter the radius of the circle:"))
# pi=3.14
# area=pi*r**2
# print("The area of the circle is", area)
# circumference=2*pi*r
# print("The circumference of the circle is", circumference)
# print("The radius of the circle is:", r)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Slope formula is y=mx+b

# slope=int(input("Enter the slope value for task1"))

# x_intercept=2/slope
# y_intercept=-2
# print("the slope value for task1 is",slope)
# print("The value of x_intercept is",x_intercept)
# print("The value of y_intercept is",y_intercept)

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

# import math
# x1, y1=2, 2
# x2, y2=6, 10
# m=y2-y1/x2-x1
# print("The slope value for task2 is:",m)
# # d=sqrt((x2-x1)^2+(y2-y1)^2)
# d=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print("The distance between the two points is:",d)

#Compare the slopes in the above two tasks
# if slope==m:
#     print("Task 1 and Task 2 slopes are equal")
# else:
#     print("Task 1 and Task 2 slopes are not equal")
# if slope>m:
#     print("Task 1 is greater than Task 2")
# else:
#     print("Task 2 is greater than Task 1")
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# import math

# # Define the coefficients of the quadratic equation
# a = 1  # Coefficient of x^2
# b = 6  # Coefficient of x
# c = 9  # Constant term

# # Calculate the discriminant
# discriminant = b**2 - 4*a*c

# # Check if the discriminant is non-negative
# if discriminant >= 0:
#     # Calculate the two possible solutions for x
#     x1 = (-b - math.sqrt(discriminant)) / (2*a)
#     x2 = (-b + math.sqrt(discriminant)) / (2*a)
    
#     # Print the solutions
#     print("The solutions for x are:", x1, "and", x2)
# else:
#     print("No real solutions for x")

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# a="python"
# b="dragon"
# print("The length of python is:", len(a))
# print("The length of dragon is:", len(b))
# if len(a)==len(b):
#     print("python and dragon are of same length")
# if a==b:
#     print("Python and dragon are same")
# else:
#     print("Python is a language and dragon is a creature")
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
# a='python'
# b='dragon' 
# if 'on' in a and 'on' in b:
#     print("'on' is in both python and dragon")
# else:
#     print("'on' is not on both the words")
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
# a="I hope this course is not full of jargon"
# if 'jargon' in a:
#     print("jargon is in the above sentence")
# else:
#     print("jargon is not in the above sentence")
# There is no 'on' in both dragon and python
# import re
# a='python'
# b='on' 
# matcha=re.search(r'\bon\b', a) 
# matchb=re.search(r'\bon\b', b)
# if matcha:
#     print("Match found on a:", matcha.group())
#     print(matcha.group())
# else:
#     print("No match found on a")
# if matchb:
#     print("Match found on b:", matchb.group())
#     print(matchb.group())
# else:
#     print("No match found on b")
#Find the length of the text python and convert the value to float and convert it to string
# a="python"
# print(len(a))
# b=float(len(a))
# print(b)
# c=str(b)
# print(type(c))
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
a=int(input("Enter a number:"))
if a%2==0:
    print(f"The number {a} is an even number")
else:
    print(f"{a} is not an even number")
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# a=7
# b=3
# c=a//b
# print("The floor division value of 7//3 is:",c)
# print(int(c))
# Check if type of '10' is equal to type of 10
# a='10'
# b=10
# c=type(a)
# d=type(b)
# print(c)
# print(d)
# if c==d:
#     print("They are equal classes")
# else:
#     print("they are different class")
# Check if int('9.8') is equal to 10
 
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# a=float(input("Enter the number of hours worked today:"))
# b=10
# c=b*a
# d=int(c)
# print(f"your total billable amount per day is {d}$")
# e=d*7
# print(f"you weekly income is {e}$")

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# a=int(input("Enter your age:"))
# min=60
# hour=min*60
# day=hour*24
# year=365*day
# life=year*100
# total_age_in_sec=a*year
# print("The total seconds you lived are:", total_age_in_sec)
# total_left_time_sec=life - total_age_in_sec
# print(f"You have {total_left_time_sec} seconds left in your life, Good luck")

#Write a Python script that displays the following table

# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

# print
# print("1 1 1 1 1")
# print("2 1 2 4 8")
# print("3 1 3 9 27")
# print("4 1 4 16 64")
# print("5 1 5 25 125")

#with loops
# for i in range(0,6):
#     print(i, i**0, i**1, i**2, i**3)
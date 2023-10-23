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
#d=sqrt((x2-x1)^2+(y2-y1)^2)
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
import math

# Define the coefficients of the quadratic equation
a = 1  # Coefficient of x^2
b = 6  # Coefficient of x
c = 9  # Constant term

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is non-negative
if discriminant >= 0:
    # Calculate the two possible solutions for x
    x1 = (-b - math.sqrt(discriminant)) / (2*a)
    x2 = (-b + math.sqrt(discriminant)) / (2*a)
    
    # Print the solutions
    print("The solutions for x are:", x1, "and", x2)
else:
    print("No real solutions for x")

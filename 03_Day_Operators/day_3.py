#################################################
#-------------- Exercises - Day 3 --------------#
#################################################

# 1. Declare your age as integer variable
age = int(30)

# 2. Declare your height as a float variable
height = float(178.33)

# 3. Declare a variable that store a complex number
c_num = 3j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
b = float(input("Enter base: "))
h = float(input("Enter height: "))
area = 0.5 * b * h
print("The area of the triangle is ", area)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
per = side_a + side_b + side_c
print("The perimeter of the triangle is ", per)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Length: "))
width = float(input("Width: "))
area = length * width  
perimeter = 2 * (length + width)
print("Area: ", area)
print("Perimeter: ", perimeter)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = float(input("Radius: "))
pi = 3.14
area = pi * r ** 2  
c = 2 * pi * r

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = input("x-intercept: ")
y = 2*x - 2

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1 = 2
y1 = 2
x2 = 6
y2 = 10

m = (y2 - y1)/(x2 - x1)

# 10. Compare the slopes in tasks 8 and 9.
euclidean_a = (2 ** 2 + 2 ** 2) ** 0.5
euclidean_b = (6 ** 2 + 10 ** 2) ** 0.5

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = -3
y = x**2 + 6*x + 9

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length1 = len("python")
length2 = len("dragon")
compare = length1 != length2

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on in python:", "on" in "python")
print("on in dragon:", "on" in "dragon")

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
print("jargon in sentence:", "jargon" in sentence)

# 15. There is no 'on' in both dragon and python
print("on in python:", "on" not in "python")
print("on in dragon:", "on" not in "dragon")

# 16. Find the length of the text python and convert the value to float and convert it to string
print(str(float(len("python"))))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter number: ")) 
is_even = number % 2 == 0
print(is_even)

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(float(2.7)))

# 19. Check if type of '10' is equal to type of 10
print(int(10) == 10)

# 20. Check if int('9.8') is equal to 10
print(int(float('9.8')) == 10)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input("Enter hours:") 
rate = input("Enter rate per hour:") 
print("Your weekly earning is", hours * rate)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = ("Enter number of years you have lived: ")
secs = years * 365 * 24 * 60 * 60
print("You have lived for", secs ,"seconds.")

# 23. Write a Python script that displays the following table
print( "\n", 1,  1**0,  1**1,  1**2,  1**3, "\n", 2,  2**0,  2**1,  2**2,  2**3, "\n", 3,  3**0,  3**1,  3**2,  3**3, "\n", 4,  4**0,  4**1,  4**2,  4**3, "\n", 5,  5**0,  5**1,  5**2,  5**3 )

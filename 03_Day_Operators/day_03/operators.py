# Exercises - Day 3
# 1º Declare your age as integer variable
age = 34
# 2º Declare your height as a float variable
my_height = 1.65
# 3º Declare a variable that store a complex number
complex_number = 1+4j
# 4º Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input('Enter base size of triangle')
height = input ('Enter height of triangle')
area_of_triangle = 0.5*base*height
print('The area of triangle is:',area_of_triangle)
# 5º Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input('Enter side a of triangle')
side_b =  input('Enter side b of triangl')
side_c =  input('Enter side c of triangl')
perimeter_of_triangle = side_a + side_b + side_c
print('The perimeter os triangle is:',perimeter_of_triangle)
# 6º Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input('Enter lenght of rectangle')
width = input('Enter width of rectangle')
area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is',area,'The perimeter of the rectangle is',perimeter)
# 7º Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14. // 
radius = input ('Enter radius circle')
area_of_circle = 3.14*radius*radius
circumference = 2 * 3.14 * radius
print('The area of the circle is',area_of_circle,'The circumference of the circle is',circumference)
# 8º Calculate the slope, x-intercept and y-intercept of y = 2x -2
x_intercept = 2 / 2
y_intercept = -2
slope_1 = ((0 - y_intercept) / (x_intercept - 0))
print('Calculate slope: %s; x-intercept(y = 0): %s; y-intercept(x = 0): %s' %
(slope_1, x_intercept, y_intercept))
# 9º Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_2 = ((y2 - y1) / (x2 - x1))
euclidian_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("(x1, y1) = (%s, %s); (x2, y2) = (%s, %s); slope = %s; euclidian distance = %s" %
(x1, y1, x2, y2, slope_2, euclidian_distance))
# 10º Compare the slopes in tasks 8 and 9.
print('slope_1 == slope_2:', slope_1 == slope_2)
print('slope_1 != slope_2:', slope_1 != slope_2)
print('slope_1 <= slope_2:', slope_1 <= slope_2)
print('slope_1 >= slope_2:', slope_1 >= slope_2)
# 11º Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
print('Calculate the value of y (y = x ^ 2 + 6x + 9)')
n = -5
while n < 5:
    y = n ** 2 + 6 * n + 9
    if y == 0:
        print("x = ", n)
        break
    n += 1

# 12º Find the length of 'python' and 'dragon' and make a falsy comparison statement.
python_length = len('python')
dragon_length = len('dragon')
print("python_length = len('python'):", python_length)
print("dragon_length = len('dragon'):", dragon_length)
print("python_length < dragon_length and python_length > dragon_length",
    python_length < dragon_length and python_length > dragon_length)
print("python_length < dragon_length or python_length > dragon_length",
    python_length < dragon_length or python_length > dragon_length)
print("not (python_length < dragon_length):",
    not (python_length < dragon_length))
print("not (python_length > dragon_length):",
    not (python_length > dragon_length))
# 13º Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("('on' in 'dragon' and 'on' in 'python'):",
    ('on' in 'dragon' and 'on' in 'python')) #True

# 14º I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
string_to_inspect = 'I hope this course is not full of jargon'
print(string_to_inspect,
    ("has" if 'jargon' in string_to_inspect else "has not"), " 'jargon'.")

# 15º There is no 'on' in both dragon and python
print("not ('on' in 'dragon' and 'on' in 'python'):",
    not ('on' in 'dragon' and 'on' in 'python'))

# 16º Find the length of the text python and convert the value to float and convert it to string
print("str(float(len('python')))", str(float(len('python'))))
# 17º Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
n = 0
while n <= 6:
    print(n, "is even" if n % 2 == 0 else "is not even")
    n += 1
# 18º Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print( 7 // 3 == int(2.7))
# 19º Check if type of '10' is equal to type of 10
print(type(10)== type('10')) #False
# 20º Check if int('9.8') is equal to 10
print(type(9.8)== type(10)) #False
# 21º Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input ('Enter hours')
rate_per_hour = input ('Enter rate per hour')
total_pay = hours * rate_per_hour
print("Total pay is:", total_pay)
# 22º Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = input('Enter your years')
total_years_live = years *365*24*60*60
print('Your total years in seconds is:',total_years_live)
# 23º Write a Python script that displays the following table
n = 1
while n <= 5:
    print(n, n ** 0, n ** 1, n ** 2, n ** 3)
    n += 1
import math

# Exercise 1
# q1
age = 44
# q2
height = 1.79
# q3
complex_number = 1 - 1j
print("age:", age, "height:", height, "complex_number:", complex_number)
# q4
base = input('Enter base size of triangle: ')
height = input('Enter height of triangle: ')
print('The area od the triangle is:', 0.5 * float(base) * float(height))
# q5
side_a = input('Enter side A of triangle: ')
side_b = input('Enter side B of triangle: ')
side_c = input('Enter side C of triangle: ')
print('The perimeter of the triangle is', float(
    side_a) + float(side_b) + float(side_c))
# q6
length = input('Enter length of rectangle: ')
width = input('Enter width of rectangle: ')
print('The area of the rectangle is', float(length) * float(width),
      'the perimeter of the rectangle is', 2 * (float(length) + float(width)))
# q7
radius = input('Enter radius of circle: ')
print('The area of the circle is', math.pi * (float(radius) ** 2))
print('The perimeter of the circle is', 2 * math.pi * float(radius))
# q8
x_intercept = 2 / 2
y_intercept = -2
slope_q8 = ((0 - y_intercept) / (x_intercept - 0))
print('Calculate slope_q8: %s; x-intercept(y = 0): %s; y-intercept(x = 0): %s' %
      (slope_q8, x_intercept, y_intercept))
# q9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_q9 = ((y2 - y1) / (x2 - x1))
euclidian_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("(x1, y1) = (%s, %s); (x2, y2) = (%s, %s); slope_q9 = %s; euclidian distance = %s" %
      (x1, y1, x2, y2, slope_q9, euclidian_distance))
# q10
print('slope_q8 == slope_q9:', slope_q8 == slope_q9)
print('slope_q8 != slope_q9:', slope_q8 != slope_q9)
print('slope_q8 <= slope_q9:', slope_q8 <= slope_q9)
print('slope_q8 >= slope_q9:', slope_q8 >= slope_q9)
# q11
print('Calculate the value of y (y = x ^ 2 + 6x + 9)')
n = -5
while n < 5:
    y = n ** 2 + 6 * n + 9
    if y == 0:
        print("x = ", n)
        break
    n += 1

# q12
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

# q13
print("('on' in 'dragon' and 'on' in 'python'):",
      ('on' in 'dragon' and 'on' in 'python'))

# q14
string_to_inspect = 'I hope this course is not full of jargon'
print(string_to_inspect,
      ("has" if 'jargon' in string_to_inspect else "has not"), " 'jargon'.")

# q15
print("not ('on' in 'dragon' and 'on' in 'python'):",
      not ('on' in 'dragon' and 'on' in 'python'))

# q16
print("str(float(len('python')))", str(float(len('python'))))

# q17
n = 0
while n <= 6:
    print(n, "is even" if n % 2 == 0 else "is not even")
    n += 1

# q18
print("7 // 3 = int(2.7): ", 7 // 3 == int(2.7))

# q19
print("type('10') == type(10)", type('10') == type(10))

# q20
print("int('9.8') == 10", int(float('9.8')) == 10)

# q21
hours = input('Enter hours: ')
rate = input('Enter rate per hour: ')
print('Your weekly earning is', int(hours) * float(rate))

# q22
years = input('Enter number of years you have lived: ')
print('You have lived for', int(years) * 365 * 24 * 60 * 60, 'seconds.')

# q23
n = 1
while n <= 5:
    print(n, n ** 0, n ** 1, n ** 2, n ** 3)
    n += 1

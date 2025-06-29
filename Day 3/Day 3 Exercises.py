your_age = 28
your_height = 191.5
imaginary = 32 + 4j 
print(f"type of your_age is {type(your_age)}")
print('type of your_height is', type(your_height))

##################################################

script_base = input('Enter the base of a triangle: ')
base = float(script_base)
script_height = input('Enter the height of that triangle: ')
height = float(script_height)
print(f"The area of the triangle equals {round(0.5 * base * height, 2)}")

side_a = input('Enter side a of a triangle: ')
a = float(side_a)
side_b = input('Enter side b of a triangle: ')
b = float(side_b)
side_c = input('Enter side c of a triangle: ')
c = float(side_c)
print('The perimeter of the triangle is ', a + b + c)

script_length = input('Enter the length of a rectangle: '); length = float(script_length)
script_width = input('Enter the width of that rectangle: '); width = float(script_width)
print(f"The area of the rectangle equals {round(length * width, 2)}, and the perimeter of that rectangle equals {round(2*(length + width), 2)}")

script_radius = input('Enter the radius of a circle: ')
radius = float(script_radius)
print('The area of the circle equals ', round(3.14 * radius**2, 2), ', and the circumference of that circle equals ', round(2*3.14*radius, 2))

#####################################################

script_slope = input('Enter the value of the slope of a line:' ); slope = int(script_slope)
script_b = input('Enter the value of the free term of the line (If none, enter 0): '); b = int(script_b)
print(f"The equation of the line you entered is y = {slope}x + ({b})")
print(f"The slope of the equation equals {slope}. The x-intercept equals {-(b)/slope} and the y-intercept equals {b}")

#####################################################

print("Let's point out two points on the x-y plane!")
script_x1 = input('Enter the x-coordinate of the first point: '); x1 = int(script_x1)
script_y1 = input('Enter the y-coordinate of the first point: '); y1 = int(script_y1)
script_x2 = input('Enter the x-coordinate of the second point: '); x2 = int(script_x2)
script_y2 = input('Enter the y-coordinate of the second point: '); y2 = int(script_y2)
slope2 = round((y2-y1)/(x2-x1),2)
print(f"You've just entered the line equation: ({slope2})x + ({round((y1 - slope2*x1),2)})")
print(f"The euclidean distance between the points ({x1},{y1}) and ({x2},{y2}) equals {round(((y2-y1)**2+(x2-x1)**2)**0.5,2)}")

########################################################

print('I challenge you to solve this problem.\n Find the x value that makes this equation equals 0 (You have only one trial)')
print('y = x^2 + 6x + 9')
script_user_answer = input('Enter your value for x in integers only: '); user_answer = int(script_user_answer)
if user_answer == -3 : print('Congratulations! Your answer is correct.') 
else : print('Sorry. That was incorrect :/')

#########################################################

print('python is longer than dragon is a ', len('python') > len('dragon'), 'statement.')
print(f"The 'on' word exists on both python and dragon is a {'on' in 'python' and 'on' in 'dragon'} statement.")
print(f"there's jargon in 'I hope this course is not full of jargon' is a {'jargon' in 'I hope this course is not full of jargon'} statement.")
print(f"There's no 'on' in both dragon and python is a {'on' not in 'dragon' and 'on' not in 'python'} statement.")
print(f"The length of the word 'python' equals {len('python')}: {float(len('python'))}: {str(len('python'))}")

##########################################################

string_number = input("Enter an integer and I'll tell it's even or odd: "); number = int(string_number)
if number % 2 == 0 : print('Number is even')
else : print('Number is odd')

##########################################################

print(f"'The floor division of 7 by 3 is equal to the int converted value of 2.7' is a {7 // 3 == int(2.7)} statement.")
print(f"The type of '10' is equal to type of 10 is a {'10' is 10} statement.")
print(f"int('9.8') is equal to 10 is a {int(9.8) == 10} statement.")

##########################################################

string_hours = input('Enter the number of hours: '); hours = int(string_hours)
string_rph = input('Enter the rate per hour: '); rph = int(string_rph)
print(f"Your weekly earning is about {hours * rph}")

##########################################################

age = int(input('Enter your age: '))
print('You have lived for ', age * 365 * 24 * 60 * 60, 'seconds.')

##########################################################

print('1 1 1 1 1 \n2 1 2 4 8 \n3 1 3 9 27 \n4 1 4 16 64 \n5 1 5 25 125 ')





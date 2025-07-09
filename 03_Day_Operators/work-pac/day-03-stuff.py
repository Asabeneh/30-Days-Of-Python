# day 3 Exercises 
import time

# 1. Declare your age as integer variable:
user_age = int(input("How many levels do you have? "))
print(str(user_age) + " is a " + (type(user_age).__name__) + " type.")

# 2. Declare your height as a float variable
user_height = float(input("How many bald eagles tall? "))
print(str(user_height) + " is a " + (type(user_height).__name__) + " type.")

# 3. Declare a variable that store a complex number
complex_number = (1+1j)
print(str(complex_number) + " is a " + (type(complex_number).__name__) + " type.")

# 4. Write a script that prompts the user to enter base and height of the triangle and 
#    calculate an area of this triangle (area = 0.5 x b x h)
print('Want the Area of a tringle? ')
user_base = int(input('What is the base? '))
user_height = int(input('And the height? '))
print('rad... calculating')
triangle_area = 0.5 * user_base * user_height
time.sleep(1)
print('Easy Day, base = ' + (str(user_base)) + ", and height = " + (str(user_height)) + ". \nSo the area = " + (str(triangle_area)))

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#    Calculate the perimeter of the triangle (perimeter = a + b + c).
print('Want the perimeter of a tringle? ')
side_a = int(input('Side a? '))
side_b = int(input('side b?? '))
side_c = int(input('And the c side? '))
print('rad... calculating')
triange_perimeter = side_a * side_b * side_c
# time.sleep(1)
print('Easy Day, the perimeter = ' + (str(triange_perimeter)))

# 6. Get length and width of a rectangle using prompt. 
#    Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
print('Rectangle time...')
rect_length = int(input('Length: '))
rect_width = int(input('Width: '))
rect_area = rect_length * rect_width
rect_perimeter = ((rect_length + rect_width) * 2)
print('The rectangle area is ' + str(rect_area) + ".\n with a perimeter of " + str(rect_perimeter)+ ".")

# 7. Get radius of a circle using prompt. 
#    Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14 
print("Circle time! ")
radius = float(input("What is the radius? "))
circle_circum = 2 * pi * radius
cirlce_area = (radius **2) * pi
print("Circumferance = " + str(circle_circum) +"\n Area = " + str(cirlce_area) )


# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
#       slope = y = mx + b
#       x-intercept = (-b)/m
#       y-intercept = 
slope_m = 2
slope_b = -2
slope_y = 0
x_intercept = (slope_b*-1)/slope_m
print(x_intercept)
y_intercept = (2*0) + slope_b
print(y_intercept)


#   9. Find the slope = (m = y2-y1/x2-x1). 
#      Find Euclidean distance = squarroot( ((x2-x1)**2) + ((y2-y1)**2)) )
#      between point (2, 2) and point (6,10) 
x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope = (y2-y1)/ (x2-x1)
print(slope)
edist = ( ((x2-x1)**2) + ((y2-y1)**2)) ** 0.5
print(edist)

#  10. Compare the slopes in tasks 8 and 9.
compareq8_q9 = (slope_m==slope)
print(f"comparing slope q8 '{slope_m}' and Q9 '{slope}' = '{compareq8_q9}'") 

#   11. Calculate the value of y (y = x^2 + 6x + 9). 
#       Try to use different x values and figure out at what x value y is going to be 0.
user_x = float(input("What is your x guess : "))
user_y = (user_x**2) + (6*user_x) + (9)
print(f"The y value is : {user_y} is this 0 : {user_y == 0}" )

#   12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word1 = 'dragon'
word2 =  'python'

print(f"The Length of {word1} = {len(word1)}") 
print(f"The Length of {word2} = {len(word2)}") 
print(f"Is the length the same = {len(word1) == len(word2)}")
print(f"The Hash of {word1} = {hash(word1)}") 
print(f"The Hash of {word2} = {hash(word2)}") 
print(f"Is the Hash the same = {hash(word1) == hash(word2)}")


#   13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'
words_q13 = ['python', 'dragon']
search_term = 'on'
print(f"looking for the search term '{search_term}' in {words_q13[0]} and {words_q13[1]} returns : ")
print((search_term in words_q13[0]) and (search_term in words_q13[1]))

#   14. I hope this course is not full of jargon. 
#   Use 'in' operator to check if 'jargon' is in the sentence.
sentance14 = "I hope this course is not full of jargon"
search_term14 = "jargon"
print(f"Looking at the sentance : '{sentance14}' \nchecking for '{search_term14}' is : {search_term14 in sentance14}")


#   15. There is no 'on' in both dragon and python
q15_words = ['dragon','python']
q15_search = 'on'
print(f"There is no 'on' in {q15_words[0]} and {q15_words[1]} : {q15_search not in q15_words[0] and q15_search not in q15_words[1]}")

#   16. Find the length of the text _python_ and convert the value to float and convert it to string
word16 = 'python'
word16_len = len(word16)
print(f"{word16} has a length of : {word16_len}")
print(f"{word16} as a float : {float(word16_len)}")
print(f"{word16} as a string : {str(word16_len)}")


#   17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
q17_number = float(input("Pick a number : "))
#q17_number = (input("Pick a number : "))
print(f"{q17_number} is even : {0 == (q17_number % 2)}") 
      

#   18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
#q18_nums = [7, 3, 2.7]
#print(({q18_nums[0]} // {q18_nums[1]}) == int({q18_nums[2]}))
#print(type(q18_nums[0]))
#q18 = 
print((7 // 3) == (int(2.7)))

#   19. Check if type of '10' is equal to type of 10
q19_1 = '10'
q19_2 = 10
print(type(q19_1) == type(q19_2))


#   20. Check if int('9.8') is equal to 10
q20_1 = int(9.8)
q20_2 = 10
print(q20_1 == q20_2)


#   21. Write a script that prompts the user to enter hours and rate per hour. 
#       Calculate pay of the person?
user_hours = float(input("Hours per week : "))
user_payrate = float(input("Hourly wage : "))
weekly_rate = user_hours * user_payrate
print(f"Your weekly earning is : ${weekly_rate:.2f}\n Buy more Bitcoin")



#   22. Write a script that prompts the user to enter number of years. 
#       Calculate the number of seconds a person can live. Assume a person can live hundred years

user_age22 = int(input("How many levels : "))
user_age_week = (user_age22 * 52)
user_age_days = (user_age_week * 7)
user_age_hours = (user_age_days * 24)
user_age_mins = user_age_hours * 60
user_age_sec = user_age_mins * 60

print(f"you have lived for {user_age_week} weeks! wow!")
print(f"you have lived for {user_age_days} days! wow!")
print(f"you have lived for {user_age_hours} hours! wow!")
print(f"you have lived for {user_age_mins} mins! wow!")
print(f"you have lived for {user_age_sec} seconds! wow!")



#23. Write a Python script that displays the following table
#```py
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125
#```

# Function to display the table
def display_table():
    print("This script will display a table with specific calculations per row.")
    print("-" * 30) # A separator for better readability

    # Loop from 1 to 5 to generate each row
    for i in range(1, 6): # range(1, 6) will go from 1 up to (but not including) 6
        # Calculate the values for each column based on 'i'
        col1 = i
        col2 = 1
        col3 = i
        col4 = i ** 2  # i squared
        col5 = i ** 3  # i cubed

        # Print the values, formatted to align nicely.
        # :<3 means left-align in a field of 3 characters width
        print(f"{col1:<3} {col2:<3} {col3:<3} {col4:<3} {col5:<3}")

    print("-" * 30)

# Call the function to execute the script
display_table()


# ─────────────────────────────────────────────
## 💻 Exercises: Day 9
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 1
# ─────────────────────────────────────────────
# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#     ```sh
#     Enter your age: 30
#     You are old enough to learn to drive.
#     Output:
#     Enter your age: 15
#     You need 3 more years to learn to drive.
#     ```
a = int(input("Enter your age: "))
if a >= 18:
 	print("You are old enough to learn to drive.")
else:
 	print(f"You need {18 - a} more years to learn to drive.")
	
# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#     ```sh
#     Enter your age: 30
#     You are 5 years older than me.
#     ```
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
      
age_diff = abs(my_age - your_age)

if my_age > your_age:
    if age_diff > 1:
        print(f"You are {age_diff} years younger than me.")
    else:
        print(f"You are {age_diff} year younger than me.")
elif my_age < your_age:
    if age_diff > 1:
        print(f"You are {age_diff} years older than me.")
    else:
        print(f"You are {age_diff} year older than me.")
else:
    print("Yay! We're the same age.")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#   ```sh
#   Enter number one: 4
#   Enter number two: 3
#   4 is greater than 3
#   ```
numb_a = int(input("Enter number one: "))
numb_b = int(input("Enter number two: "))

if numb_a > numb_b:
    print(f"{numb_a} is greater than {numb_b}")
elif numb_a < numb_b:
    print(f"{numb_a} is smaller than {numb_b}")
else:
    print(f"{numb_a} is equal {numb_b}")

# ─────────────────────────────────────────────
### Exercises: Level 2
# ─────────────────────────────────────────────
# 1.  Write a code which gives grade to students according to theirs scores:
#     ```sh
#     90-100, A
#     80-89, B
#     70-79, C
#     60-69, D
#     0-59, F
#     ```
grade = int(input("Enter your grade: "))
if grade >= 0 and grade < 60:
    print("You got an F")
elif grade >= 60 and grade < 70:
    print("You got a D")
elif grade >= 70 and grade < 80:
    print("You got a C")
elif grade >= 80 and grade < 90:
    print("You got a B")
elif grade >= 90 and grade <= 100:
    print("You got an A")
else:
    print("Invalid number, Valid Grade is between 0 and 100")

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is:
#     September, October or November, the season is Autumn.
#     December, January or February, the season is Winter.
#     March, April or May, the season is Spring
#     June, July or August, the season is Summer
month = input("Enter month: ").title()

autum = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

if month in autum:
	print("The season is Autumn.")
elif month in winter:
	print("The season is Winter.")
elif month in spring:
	print("The season is Spring.")
elif month in summer: 
	print("The season is Summer.")
else: 
	print("Please enter a Month of the Year")

# 3. The following list contains some fruits:
#     ```sh
#     fruits = ['banana', 'orange', 'mango', 'lemon']
#     ```
#     If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
check_fruit = input('Enter fruit: ').lower()

fruits = ['banana', 'orange', 'mango', 'lemon']

if check_fruit in fruits:
	print('That fruit already exist in the list')
else: 
	fruits.append(check_fruit)
	print(fruits)

# ─────────────────────────────────────────────
### Exercises: Level 3
# ─────────────────────────────────────────────
# 1. Here we have a person dictionary. Feel free to modify it!
person={
     'first_name': 'Asabeneh',
     'last_name': 'Yetayeh',
     'age': 250,
     'country': 'Finland',
     'is_married': True,
     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
     'address': {
         'street': 'Space street',
         'zipcode': '02210'
     }
    }

#   * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
	print(person['skills'][2:-2])
else:
	print('Skills is not in person')
    
#   * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
	if 'Python' in person['skills']:
		print(True)		
else:
	print('Skills is not in person')
      
#   * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
front_end = ['JavaScript', 'React']
backend = ['Node', 'Python', 'MongoDB']
fullstack = ['React', 'Node', 'MongoDB']

person['skills'].sort()
front_end.sort()
backend.sort()
fullstack.sort()


if 'skills' in person:
	if front_end == person['skills']:
		print('He is a front end developer')
	elif backend == person['skills']:
		print('He is a backend developer')
	elif fullstack == person['skills']:
		print('He is a fullstack developer')
	else:
		print('Unknown Title')
else:
	print('Skills not in person')
	
#   * If the person is married and if he lives in Finland, print the information in the following format:
#   ```py
#     Asabeneh Yetayeh lives in Finland. He is married.
#   ```
if person['is_married'] == True:
	print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.')
else:
	print(f'{person['first_name']} {person['last_name']} not married.')

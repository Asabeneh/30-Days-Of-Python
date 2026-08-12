# =====================================================
# 30 Days Of Python - Day 9: Conditionals (Full Code)
# =====================================================

print("===== DAY 9: CONDITIONALS =====\n")

# -----------------------------------------------------
# 1. IF CONDITION
# -----------------------------------------------------

a = 3
if a > 0:
    print("A is a positive number")
print()

# -----------------------------------------------------
# 2. IF ELSE
# -----------------------------------------------------

a = -2
if a < 0:
    print("A is a negative number")
else:
    print("A is a positive number")
print()

# -----------------------------------------------------
# 3. IF ELIF ELSE
# -----------------------------------------------------

a = 0
if a > 0:
    print("A is a positive number")
elif a < 0:
    print("A is a negative number")
else:
    print("A is zero")
print()

# -----------------------------------------------------
# 4. SHORT HAND (TERNARY)
# -----------------------------------------------------

a = 3
print("A is positive") if a > 0 else print("A is negative")
print()

# -----------------------------------------------------
# 5. NESTED CONDITIONS
# -----------------------------------------------------

a = 4
if a > 0:
    if a % 2 == 0:
        print("A is a positive and even number")
    else:
        print("A is a positive and odd number")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")
print()

# -----------------------------------------------------
# 6. IF WITH AND LOGICAL OPERATOR
# -----------------------------------------------------

a = -3
if a > 0 and a % 2 == 0:
    print("A is an even and positive integer")
elif a > 0 and a % 2 != 0:
    print("A is a positive integer")
elif a == 0:
    print("A is zero")
else:
    print("A is a negative number")
print()

# -----------------------------------------------------
# 7. IF WITH OR LOGICAL OPERATOR
# -----------------------------------------------------

user = 'James'
access_level = 3

if user == 'admin' or access_level >= 4:
    print("Access granted!")
else:
    print("Access denied!")
print()

# =====================================================
# EXERCISES: LEVEL 1
# =====================================================

print("===== EXERCISES: LEVEL 1 =====\n")

# 1. Driving age check
age = int(input("Enter your age: "))

if age >= 18:
    print("You are old enough to learn to drive.")
else:
    years_left = 18 - age
    print(f"You need {years_left} more year(s) to learn to drive.")
print()

# 2. Compare ages
my_age = 25
your_age = int(input("Enter your age: "))

difference = abs(my_age - your_age)

if your_age > my_age:
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {difference} years older than me.")
elif your_age < my_age:
    if difference == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {difference} years younger than me.")
else:
    print("We are the same age.")
print()

# 3. Compare two numbers
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")
print()

# =====================================================
# EXERCISES: LEVEL 2
# =====================================================

print("===== EXERCISES: LEVEL 2 =====\n")

# 1. Grade system
score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score <= 59:
    print("Grade: F")
else:
    print("Invalid score")
print()

# 2. Season checker
month = input("Enter a month: ").capitalize()

if month in ['September', 'October', 'November']:
    print("Season: Autumn")
elif month in ['December', 'January', 'February']:
    print("Season: Winter")
elif month in ['March', 'April', 'May']:
    print("Season: Spring")
elif month in ['June', 'July', 'August']:
    print("Season: Summer")
else:
    print("Invalid month")
print()

# 3. Fruit checker
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print("Updated fruits list:", fruits)
print()

# =====================================================
# EXERCISES: LEVEL 3
# =====================================================

print("===== EXERCISES: LEVEL 3 =====\n")

person = {
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

# 1. Middle skill
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])
print()

# 2. Check Python skill
if 'skills' in person:
    print("Has Python skill?", 'Python' in person['skills'])
print()

# 3. Developer role check
skills = set(person['skills'])

if {'JavaScript', 'React'}.issubset(skills) and len(skills) == 2:
    print("He is a front end developer")
elif {'Node', 'Python', 'MongoDB'}.issubset(skills) and 'React' not in skills:
    print("He is a backend developer")
elif {'React', 'Node', 'MongoDB'}.issubset(skills):
    print("He is a fullstack developer")
else:
    print("Unknown title")
print()

# 4. Marital & country info
if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")

print("\n===== END OF DAY 9 =====")
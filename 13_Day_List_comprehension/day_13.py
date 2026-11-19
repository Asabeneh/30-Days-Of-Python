# =====================================================
# 30 Days Of Python - Day 13: List Comprehension
# =====================================================

print("===== DAY 13: LIST COMPREHENSION =====\n")

# -----------------------------------------------------
# 1. List Comprehension Basics
# -----------------------------------------------------

language = 'Python'

# Converting string to list (normal way)
lst = list(language)
print("List using list():", lst)

# Using list comprehension
lst = [i for i in language]
print("List using list comprehension:", lst)
print()

# -----------------------------------------------------
# 2. Generating Numbers with List Comprehension
# -----------------------------------------------------

numbers = [i for i in range(11)]
print("Numbers from 0 to 10:", numbers)

# Squares
squares = [i * i for i in range(11)]
print("Squares:", squares)

# List of tuples (number, square)
number_tuples = [(i, i * i) for i in range(11)]
print("Tuples (number, square):", number_tuples)
print()

# -----------------------------------------------------
# 3. List Comprehension with Condition
# -----------------------------------------------------

# Even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print("Even numbers:", even_numbers)

# Odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]
print("Odd numbers:", odd_numbers)

# Filtering positive even numbers
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print("Positive even numbers:", positive_even_numbers)
print()

# -----------------------------------------------------
# 4. Flattening a 2D List
# -----------------------------------------------------

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print("Flattened list:", flattened_list)
print()

# =====================================================
# LAMBDA FUNCTIONS
# =====================================================

print("===== LAMBDA FUNCTIONS =====\n")

# Named function
def add_two_nums(a, b):
    return a + b

print("Named function:", add_two_nums(2, 3))

# Lambda version
add_two_nums = lambda a, b: a + b
print("Lambda function:", add_two_nums(2, 3))

# Self-invoking lambda
print("Self-invoking lambda:", (lambda a, b: a + b)(2, 3))

# Square and cube
square = lambda x: x ** 2
cube = lambda x: x ** 3

print("Square of 3:", square(3))
print("Cube of 3:", cube(3))

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print("Multiple variable lambda:", multiple_variable(5, 5, 3))
print()

# -----------------------------------------------------
# Lambda Inside Another Function
# -----------------------------------------------------

def power(x):
    return lambda n: x ** n

cube = power(2)(3)
print("2 power of 3:", cube)

two_power_of_five = power(2)(5)
print("2 power of 5:", two_power_of_five)
print()

# =====================================================
# EXERCISES - DAY 13
# =====================================================

print("===== EXERCISES: DAY 13 =====\n")

# 1. Filter only negative and zero
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [i for i in numbers if i <= 0]
print("1. Negative and zero:", negative_and_zero)

# 2. Flatten list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in list_of_lists for num in row]
print("\n2. Flattened list:", flattened)

# 3. Create list of tuples
tuple_list = [
    (i, 1, i, i**2, i**3, i**4, i**5)
    for i in range(11)
]
print("\n3. List of tuples:")
for item in tuple_list:
    print(item)

# 4. Flatten countries list and format
countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]

formatted_countries = [
    [country.upper(), country[:3].upper(), city.upper()]
    for row in countries
    for country, city in row
]

print("\n4. Formatted countries:", formatted_countries)

# 5. Convert to list of dictionaries
countries_dict = [
    {'country': country.upper(), 'city': city.upper()}
    for row in countries
    for country, city in row
]

print("\n5. Countries as dictionaries:", countries_dict)

# 6. Concatenate names
names = [[('Asabeneh', 'Yetayeh')],
         [('David', 'Smith')],
         [('Donald', 'Trump')],
         [('Bill', 'Gates')]]

full_names = [
    f"{first} {last}"
    for row in names
    for first, last in row
]

print("\n6. Full names:", full_names)

# 7. Lambda for slope and y-intercept
# y = mx + b
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda m, x, y: y - m * x

print("\n7. Slope:", slope(1, 2, 3, 6))
print("   Y-intercept:", y_intercept(2, 1, 4))

print("\n===== END OF DAY 13 =====")
# =====================================================
# 30 Days Of Python - Day 14: Higher Order Functions
# =====================================================

from functools import reduce

print("===== DAY 14: HIGHER ORDER FUNCTIONS =====\n")

# -----------------------------------------------------
# FUNCTION AS A PARAMETER
# -----------------------------------------------------

def sum_numbers(nums):
    return sum(nums)

def higher_order_function(func, lst):
    return func(lst)

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print("Sum using function as parameter:", result)
print()

# -----------------------------------------------------
# FUNCTION AS A RETURN VALUE
# -----------------------------------------------------

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    return x if x >= 0 else -x

def higher_order_function_returner(func_type):
    if func_type == 'square':
        return square
    elif func_type == 'cube':
        return cube
    elif func_type == 'absolute':
        return absolute

print("Square:", higher_order_function_returner('square')(3))
print("Cube:", higher_order_function_returner('cube')(3))
print("Absolute:", higher_order_function_returner('absolute')(-3))
print()

# -----------------------------------------------------
# PYTHON CLOSURES
# -----------------------------------------------------

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_func = add_ten()
print("Closure result 5:", closure_func(5))
print("Closure result 10:", closure_func(10))
print()

# -----------------------------------------------------
# PYTHON DECORATORS
# -----------------------------------------------------

def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print("Decorator result:", greeting())
print()

# -----------------------------------------------------
# MULTIPLE DECORATORS
# -----------------------------------------------------

def split_string_decorator(function):
    def wrapper():
        return function().split()
    return wrapper

@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print("Multiple decorators:", greeting())
print()

# -----------------------------------------------------
# DECORATOR WITH PARAMETERS
# -----------------------------------------------------

def decorator_with_parameters(function):
    def wrapper(first_name, last_name, country):
        function(first_name, last_name, country)
        print(f"I live in {country}")
    return wrapper

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print(f"I am {first_name} {last_name}. I love to teach.")

print_full_name("Asabeneh", "Yetayeh", "Finland")
print()

# =====================================================
# BUILT-IN HIGHER ORDER FUNCTIONS
# =====================================================

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = list(range(1, 11))

# -----------------------------------------------------
# MAP
# -----------------------------------------------------

countries_upper = list(map(str.upper, countries))
print("Map uppercase countries:", countries_upper)

numbers_squared = list(map(lambda x: x ** 2, numbers))
print("Map square numbers:", numbers_squared)

names_upper = list(map(str.upper, names))
print("Map uppercase names:", names_upper)
print()

# -----------------------------------------------------
# FILTER
# -----------------------------------------------------

countries_with_land = list(filter(lambda c: 'land' in c.lower(), countries))
print("Countries with 'land':", countries_with_land)

six_char_countries = list(filter(lambda c: len(c) == 6, countries))
print("Countries with 6 letters:", six_char_countries)

six_or_more = list(filter(lambda c: len(c) >= 6, countries))
print("Countries with >= 6 letters:", six_or_more)

countries_starting_E = list(filter(lambda c: c.startswith('E'), countries))
print("Countries starting with E:", countries_starting_E)
print()

# -----------------------------------------------------
# REDUCE
# -----------------------------------------------------

sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", sum_numbers)

sentence = reduce(
    lambda x, y: f"{x}, {y}",
    countries[:-1]
) + f", and {countries[-1]} are north European countries"

print(sentence)
print()

# -----------------------------------------------------
# CHAINING MAP + FILTER + REDUCE
# -----------------------------------------------------

chained = reduce(
    lambda x, y: x + y,
    map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
)
print("Chained result:", chained)
print()

# -----------------------------------------------------
# FUNCTIONS FOR EXERCISES
# -----------------------------------------------------

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

print("String only list:", get_string_lists([1, 'hello', 3, 'world']))
print()

def categorize_countries(pattern):
    return list(filter(lambda c: pattern.lower() in c.lower(), countries))

print("Countries with 'land':", categorize_countries('land'))
print()

def count_countries_by_letter(country_list):
    result = {}
    for country in country_list:
        first_letter = country[0]
        result[first_letter] = result.get(first_letter, 0) + 1
    return result

print("Country count by letter:", count_countries_by_letter(countries))
print()

def get_first_ten_countries(country_list):
    return country_list[:10]

def get_last_ten_countries(country_list):
    return country_list[-10:]

print("First ten countries:", get_first_ten_countries(countries))
print("Last ten countries:", get_last_ten_countries(countries))

print("\n===== END OF DAY 14 =====")
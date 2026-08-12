# =====================================================
# 30 Days Of Python - Day 11: Functions (FULL SOLUTION)
# =====================================================

import math
import keyword

print("===== DAY 11: FUNCTIONS =====\n")

# =====================================================
# BASIC FUNCTION DECLARATIONS
# =====================================================

def add_two_numbers(a, b):
    return a + b

print("Add two numbers:", add_two_numbers(3, 7))


def area_of_circle(r):
    return math.pi * r * r

print("Area of circle:", area_of_circle(10))


def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return "All arguments must be numbers"
        total += num
    return total

print("Sum all numbers:", add_all_nums(1, 2, 3, 4))


def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("C to F:", convert_celsius_to_fahrenheit(25))


def check_season(month):
    month = month.capitalize()
    if month in ['September', 'October', 'November']:
        return 'Autumn'
    elif month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer'
    else:
        return 'Invalid month'

print("Season:", check_season("October"))


def calculate_slope(x1=0, y1=0, x2=1, y2=1):
    if x2 - x1 == 0:
        return "Undefined slope"
    return (y2 - y1) / (x2 - x1)

print("Slope:", calculate_slope())


def solve_quadratic_eqn(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No real roots"
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    return x1, x2

print("Quadratic:", solve_quadratic_eqn(1, -3, 2))


def print_list(lst):
    for item in lst:
        print(item)

print_list([1, 2, 3])


def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr)-1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


def capitalize_list_items(lst):
    return [item.upper() for item in lst]

print(capitalize_list_items(['python', 'java']))


def add_item(lst, item):
    lst.append(item)
    return lst

print(add_item(['Potato', 'Tomato'], 'Meat'))


def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

print(remove_item(['Potato', 'Tomato', 'Mango'], 'Mango'))


def sum_of_numbers(n):
    return sum(range(n+1))

print(sum_of_numbers(100))


def sum_of_odds(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

print("Sum odds:", sum_of_odds(10))


def sum_of_even(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

print("Sum evens:", sum_of_even(10))


# =====================================================
# LEVEL 2
# =====================================================

def evens_and_odds(n):
    evens = sum(1 for i in range(n+1) if i % 2 == 0)
    odds = sum(1 for i in range(n+1) if i % 2 != 0)
    return f"The number of odds are {odds}. The number of evens are {evens}."

print(evens_and_odds(100))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

print("Factorial:", factorial(5))


def is_empty(value):
    return not bool(value)

print("Is empty:", is_empty(""))


def calculate_mean(lst):
    return sum(lst) / len(lst)


def calculate_median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (lst[mid] if n % 2 != 0 else (lst[mid-1] + lst[mid]) / 2)


def calculate_mode(lst):
    return max(set(lst), key=lst.count)


def calculate_range(lst):
    return max(lst) - min(lst)


def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)


def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))


numbers = [1, 2, 2, 3, 4, 5]
print("Mean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Std Dev:", calculate_std(numbers))


def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
print(greet("Alice"))


def show_args(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

show_args(name="Alice", age=30)


# =====================================================
# LEVEL 3
# =====================================================

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("Is prime:", is_prime(29))


def all_unique(lst):
    return len(lst) == len(set(lst))

print("All unique:", all_unique([1, 2, 3]))


def same_data_type(lst):
    return all(type(item) == type(lst[0]) for item in lst)

print("Same type:", same_data_type([1, 2, 3]))


def is_valid_variable(var):
    return var.isidentifier() and not keyword.iskeyword(var)

print("Valid variable:", is_valid_variable("my_var"))


def most_spoken_languages(data, n=10):
    languages = {}
    for country in data:
        for lang in country['languages']:
            languages[lang] = languages.get(lang, 0) + 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:n]


def most_populated_countries(data, n=10):
    return sorted(data, key=lambda x: x['population'], reverse=True)[:n]


print("\n===== END OF DAY 11 =====")
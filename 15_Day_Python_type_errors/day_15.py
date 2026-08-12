# =====================================================
# 30 Days Of Python - Day 15: Python Type Errors
# =====================================================

print("===== DAY 15: PYTHON TYPE ERRORS =====\n")

# -----------------------------------------------------
# SYNTAX ERROR (cannot be caught at runtime)
# -----------------------------------------------------
print("SyntaxError example (shown as comment):")
print("print 'hello world'  # Missing parentheses\n")

# -----------------------------------------------------
# NAME ERROR
# -----------------------------------------------------
try:
    print(age)
except NameError as e:
    print("NameError:", e)
    age = 25
    print("Fixed -> age =", age)
print()

# -----------------------------------------------------
# INDEX ERROR
# -----------------------------------------------------
numbers = [1, 2, 3, 4, 5]
try:
    print(numbers[5])
except IndexError as e:
    print("IndexError:", e)
    print("Valid indexes are 0 to", len(numbers) - 1)
print()

# -----------------------------------------------------
# MODULE NOT FOUND ERROR
# -----------------------------------------------------
try:
    import maths
except ModuleNotFoundError as e:
    print("ModuleNotFoundError:", e)
    import math
    print("Fixed -> math module imported")
print()

# -----------------------------------------------------
# ATTRIBUTE ERROR
# -----------------------------------------------------
import math
try:
    print(math.PI)
except AttributeError as e:
    print("AttributeError:", e)
    print("Fixed -> math.pi =", math.pi)
print()

# -----------------------------------------------------
# KEY ERROR
# -----------------------------------------------------
user = {'name': 'Asab', 'age': 250, 'country': 'Finland'}
try:
    print(user['county'])
except KeyError as e:
    print("KeyError:", e)
    print("Fixed -> country =", user['country'])
print()

# -----------------------------------------------------
# TYPE ERROR
# -----------------------------------------------------
try:
    print(4 + '3')
except TypeError as e:
    print("TypeError:", e)
    print("Fixed -> 4 + int('3') =", 4 + int('3'))
    print("Alternative -> '4' + '3' =", str(4) + '3')
print()

# -----------------------------------------------------
# IMPORT ERROR
# -----------------------------------------------------
try:
    from math import power
except ImportError as e:
    print("ImportError:", e)
    from math import pow
    print("Fixed -> pow(2, 3) =", pow(2, 3))
print()

# -----------------------------------------------------
# VALUE ERROR
# -----------------------------------------------------
try:
    print(int('12a'))
except ValueError as e:
    print("ValueError:", e)
    print("Fixed -> int('12') =", int('12'))
print()

# -----------------------------------------------------
# ZERO DIVISION ERROR
# -----------------------------------------------------
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
    print("Fix -> check denominator before division")
print()

print("===== END OF DAY 15 =====")
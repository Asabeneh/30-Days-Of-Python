# Basic arithmetic operations
print('Addition:', 5 + 3)       # Outputs: Addition: 8
print('Subtraction:', 10 - 7)   # Outputs: Subtraction: 3
print('Multiplication:', 4 * 6) # Outputs: Multiplication: 24

# Division
print('Division:', 15 / 4)      # Outputs: Division: 3.75

# Integer Division
print('Integer Division:', 15 // 4)  # Outputs: Integer Division: 3

# Modulus (Remainder)
print('Modulus:', 15 % 4)       # Outputs: Modulus: 3

# Exponentiation
print('Exponential:', 2 ** 5)   # Outputs: Exponential: 32
# Floating point arithmetic
print('Floating Point Division:', 17.5 / 2.5)  # Outputs: Floating Point Division: 7.0

# Mixed operations
result = 2.5 * 3 + 7 / 2 - 1
print('Mixed Operations:', result)  # Outputs: Mixed Operations: 9.5
# Variable assignments and reassignments
x = 5
y = 3
z = x + y
print('Value of z:', z)  # Outputs: Value of z: 8

# Increment and decrement
counter = 0
counter += 1  # Increment
print('Counter:', counter)  # Outputs: Counter: 1

counter -= 1  # Decrement
print('Counter:', counter)  # Outputs: Counter: 0
# Calculating area of a triangle
base = 6
height = 4
area_of_triangle = 0.5 * base * height
print('Area of triangle:', area_of_triangle)  # Outputs: Area of triangle: 12.0

# Calculating volume of a cube
side_length = 10
volume_of_cube = side_length ** 3
print('Volume of cube:', volume_of_cube)  # Outputs: Volume of cube: 1000
# Boolean expressions
print('True and False:', True and False)   # Outputs: True and False: False
print('True or False:', True or False)     # Outputs: True or False: True
print('Not True:', not True)               # Outputs: Not True: False

# Comparison operators
print('Greater than:', 5 > 3)              # Outputs: Greater than: True
print('Less than or equal to:', 7 <= 7)    # Outputs: Less than or equal to: True
print('Not equal to:', 10 != 12)           # Outputs: Not equal to: True
# Membership operators
print('Substring in string:', 'python' in 'python programming')  # Outputs: Substring in string: True
print('Character not in string:', 'a' not in 'hello')            # Outputs: Character not in string: True

# Identity operators
a = 5
b = a
print('Identity:', a is b)         # Outputs: Identity: True

c = 10
print('Identity:', a is not c)     # Outputs: Identity: True

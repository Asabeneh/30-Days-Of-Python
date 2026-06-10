# Exercise: Level 1
# 1. Check the python version you are using
import sys 
print(sys.version)

# 2. Open the  python interactive shell and do the following operations. The operands are 3 and 4.
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

# 3. Write strings on the python interactive shell. The strings are the following
print('Tomas')
print('Oriol')
print('Spain')
print('I am enjoying 30 days of python')

# 4. Check the data types of the following data:
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Tomas'))
print(type('Oriol'))
print(type('Spain'))

# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
type(10) # Int
type(9.8) # Float
type(4-4j) # Complex
type('Tomas') # String
type(True) # Boolean
type(['Asabeneh', 'Python', 'Finland']) # List
type((2, 3, 4, 5)) # Tuple
type({9.8, 3.14, 2.7}) # Set
type({'name': 'Tomas'}) # Dictionary

# Find an Euclidean distance between (2, 3) and (10, 8)
i1 = 2
i2 = 3
i3 = 10
i4 = 8

print(f"The Euclidean distance between ({i1}, {i2}) and ({i3}, {i4}) is:")
print(((i1-i3)**2 + (i2-i4)**2)**0.5)
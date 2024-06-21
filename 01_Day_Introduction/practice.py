
import math

# 1. check the python version
import sys

version = sys.version_info
print(f'Python version: {version.major}.{version.minor}.{version.micro}')

# 2. use 3 and 4 to do operations
print(3 + 4)  # addition
print(3 - 4)  # subtraction
print(3 * 4)  # multiplication
print(3 % 4)  # modulus
print(3 / 4)  # division
print(3 // 4)  # floor division operator
print(3 ** 4)  # exponential

# 3. make some strings
name = 'Yunxin'
family_name = 'Wen'
country = 'China'
slogan = 'I am enjoying 30 days of Python'

# 4. chect data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type(name))
print(type(family_name))
print(type(country))

# 5. different Python data types
print(1)
print(1.0)
print(1 + 1j)
print('data')
print(['Python', 'JavaScript'])
print((2,))
print({'language': 'Python'})
print({1, 3, 5, 7, 9})

# 6. find an Euclidian distance between (2,3) and (10,8)
def euclidian_distance(point1, point2):
    line_square = (point2[0]-point1[0])**2 + (point2[1]-point1[1])**2
    return math.sqrt(line_square)

print(euclidian_distance((2,3),(10,8)))
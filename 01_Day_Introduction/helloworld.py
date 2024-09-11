from ctypes import pointer
import math
# Introduction
# Day 1 - 30DaysOfPython Challenge

print(2 + 3)   # addition(+)
print(3 - 1)   # subtraction(-)
print(2 * 3)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)   # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple


#Level 2
print(3+4)  #   7 
print(3-4)  #   -1
print(3*4)  #   12
print(3%4)  #   3
print(3/4)  #   0.75
print(3**4) #   81
print(3//4) #   0

print('James')
print('Smith')
print('UK')
print('''I am enjoying 30 days of Python''')

print(type(10))                                 #   int
print(type(9.8))                                #   float
print(type(3.14))                               #   float
print(type(4-4j))                               #   complex
print(type(['John', 'Python', 'France']))       #   list
print(type('John'))                             #   str
print(type('Smith'))                            #   str
print(type('Portugal'))                         #   str

#Level 3
print(type(True))                                                               #   boolean
print(type(('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn')))         #   tuple
print(type({'Mario', 'Luigi', 'Toad', 'Peach', 'Daisy', 'Bowser'}))             #   set
print(type(
    {
        'first_name': 'Harry',
        'last_name': 'Potter',
        'age': 30,
        'country': 'UK',
        'is_married': True,
        'skills': ['Quidditch', 'Defense Against the Dark Arts', 'Herbs', 'Potions']
    }
))                                                                              # dictionary

#function for euclidean distance
def euclidean_distance(p, q):
    squared_diff = [(q_i - p_i) ** 2 for p_i, q_i in zip(p,q)]
    sum_squared_diff = sum(squared_diff)
    return math.sqrt(sum_squared_diff)

point1 = (1,3)
point2 = (4,6)
print(euclidean_distance(point1, point2))

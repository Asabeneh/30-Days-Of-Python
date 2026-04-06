a = type(10)
print(a)

b = type(9.8)
print(b)

c = type(3.14)
print(c)

d = type(4 - 4j)
print(d)

e = type(['Asabeneh', 'Python', 'Finland'])
print(e)

f = type('Your name')
print(f)

g = type('Your family name')
print(g)

h = type('Your country')
print(h)

#Integer
i = 30
print(i)

#Float
j = 5.5
print(j)

#Complex
k = (5 - 5j)
print(k)

#String
l = "What a wounderful world"
print(l)

#Boolean
m = 5 < 4
print(m)

#List
n = ['Alexa', 'Giraffe', 300]
print(n)

#Tuple
o = ('banana', 'kiwi', 'strawberry')
print(o)

#Set
p = {'jason', 23, 5 == 5}
print(p)
    
#Dictionary data type
q_dict = {"k": (5 - 5j), "l": "What a wonderful world"}
print(q_dict)

#Find an Euclidian distance between (2, 3) and (10, 8)

import math

# Define the two points (p and q) as lists of coordinates
p = [2, 3]    # Represents the point (2, 3)
q = [10, 8]   # Represents the point (10, 8)

# Calculate the Euclidean distance
distance = math.dist(p, q)

# Print the result
print(distance)

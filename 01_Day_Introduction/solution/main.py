import numpy as np

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 % 4)
print(3 / 4)
print(3 ** 4)
print(3 // 4)

print("Haise")
print("Sasaki")
print("Philippines")
print("I am Enjoying 30 days of python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Haise"))
print(type("Sasaki"))
print(type("Philippines"))

# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
num1 = 16
num2 = 3.14
num3 = 14j

string1 = "Haise"
isPogi = True
myList = ["haise", "sasaki", "kaneki"]
myTuple = ("banana", "coconut", "orange")
mySet = {"banana", "orange", "coconut"}
myDictionary = [
    "Brand:" "Toyota",
    "name:" "GTR",
    "age:" "12"
]

# Find an Euclidian distance between (2, 3) and (10, 8)

p1 = np.array((2, 3))
p2 = np.array((10, 8))

dist = np.linalg.norm(p1 - p2)

print(dist)


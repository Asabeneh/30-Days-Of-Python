import math
from ensurepip import version

# Day 1 - 30DaysOfPython Challenge
print("Exercise: Level 1 and 2")
print("Check the pip version you are using: ", version())
print("- Open the python interactive shell and do the following operations. The operands are 3 and 4.")
print("\taddition: 3 + 4 =", 3 + 4)
print("\tsubtraction: 3 - 4 =", 3 - 4)
print("\tmultiplication: 3 * 4 =", 3 * 4)
print("\tdivision: 3 / 4 =", 3 / 4)
print("\texponential: 3 ** 4 =", 3 ** 4)
print("\tfloor division operator: 3 // 4 =", 3 // 4)
print("- Write strings on the python interactive shell. The strings are the following:")
print("\tIván")
print("\tGonzález")
print("\tSpain")
print("\tI am enjoying 30 days of python")
print("- Check the data types of the following data:")
print("\t10: ", type(10))
print("\t9.8: ", type(9.8))
print("\t3.14: ", type(3.14))
print("\t4 - 4j: ", type(4 - 4j))
print("\t['Asabeneh', 'Python', 'Finland']: ",
      type(['Asabeneh', 'Python', 'Finland']))
print("\tIván: ", type("Iván"))
print("\tGonzález: ", type("tGonzález"))
print("\tSpain: ", type("tSpain"))

print("Exercise: Level 3")
print("- Find an Euclidian distance between (2, 3) and (10, 8):")
print(math.sqrt(pow(2+10, 2)+pow(3+8, 2)))

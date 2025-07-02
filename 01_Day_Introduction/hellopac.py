# Introduction to Python
# Day 1 of a 30 day Python challenge
# Exercise #2

# question 1
import sys
print(("You are using Python version ") + (str(sys.version_info.major)) + "." +(str(sys.version_info.minor)))   # first question
print()

# start 2nd question
print("3 + 4 = " + str((3 + 4)))        
print("3 - 4 = " + str((3 - 4)))
print("3 * 4 = " + str((3 * 4))) 
print("3 % 4 = " + str((3 % 4))) 
print("3 / 4 = " + str((3 / 4))) 
print("3 ** 4 = " + str((3 ** 4)))
print("3 // 4 = " + str((3 // 4))) 
print()

# Question 3 
print("Hello there 👋" + "\nI'm " + "Pacman\n")
print("I'm the owner of " + "Pac's Arcade")
print("I'm crushing the 30 day Python Challenge!")
print()

# Question 4
print("10 is a " + str(type(10)) + " type.")
print("9.8 is a " + str(type(9.8)) + " type.")
print("3.14 is a " + str(type(3.14)) + " type.")
print("4 - 4j is a " + str(type(4 - 4j)) + " type.")
print("['Asabeneh', 'Python', 'Finland'] is a " + str(type(['Asabeneh', 'Python', 'Finland'])) + " type.")
print("Pacman is a " + str(type("Pacman")) + " type.")
print("Pac's Arcade is a " + str(type("Pac's Arcade")) + " type.")
print()
print("Great Job Pac! You Finished Excercise #2!\n")


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

#Program to reverse 2 numbers
a=50
b=60
print("Value of a is:\t"+ str(a))
print("Value of b is:\t"+ str(b))
c =a+b
b=c-b
print("***************************************************")
a=c-a
print("Value of a is:\t"+str(a))
print("Value of b is:\t"+ str(b))
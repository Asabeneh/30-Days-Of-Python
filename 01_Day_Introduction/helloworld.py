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
a=int(input("Enter value of a:\t"))
b=int(input("Enter Value of b:\t"))
print("Value of a is:\t"+ str(a))
print("Value of b is:\t"+ str(b))
c =a+b
b=c-b
print("***************************************************")
a=c-a
print("Value of a is:\t"+str(a))
print("Value of b is:\t"+ str(b))

# Program to print table of any number

number= int(input("Below is the table of :"))
for i in range(1,11,1):
    n = number * i
    print(n)

print("**********Factorial of a number:\t" + str(number))
#Factorial of a numner
for i in range (number-1,0,-1):
    number=number*i
print(number)

# prime number.
num = int(input("Enter the number for Prime check:\t"))
z = 0
for i in range(2, num):
    if (num % i == 0):
        print("Its not a Prime number")
        z = 1
        break
print("This is Prime number")


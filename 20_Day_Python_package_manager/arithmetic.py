def add_numbers(*args):
    total = 0
    for num in args:
        print(num)
        total += num
        
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
args=12345
print(add_numbers(args))
num1=10
num2=20
print(subtract(num1,num2))
print(multiple(num1,num2))
print(division(num1,num2))
print(remainder(num1,num2))
print(power(num1,num2))
# 首先声明变量

a = 3 # a 是一个变量名，3 是一个整型值
b = 2 # b 是一个变量名，2 是一个整型值

# 进行算术运算，并将结果赋值给变量
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# 应该使用 sum 而不是 total，但 sum 是一个内置函数 - 尽量避免覆盖内置函数
print(total) # 如果不打印标签字符串，就不知道值是怎么计算出来的
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
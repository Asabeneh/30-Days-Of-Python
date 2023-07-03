n = 10
for i in range(n):
    print('#')
    for j in range(i + 1 , n-1 , 1):
        print(' # ' , end=" ")

i = 0
x = 1
for x in range(10):
    i +=1
    print(i  , " x "  , x , "  =  "  , i * x )
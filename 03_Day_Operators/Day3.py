import math
age = 19
height = 170.0

print('1 is 1 ', 1 is not  1 )
print('B in Asabeneh ' , 'A' in 'Asabeneh')


complex  = age + 1j
print(complex)

base = (int(input('Enter base : ')))
height  = (int(input('Enter height : ')))
area =  0.5 * base * height
print('The area of the triangle is ' , '{0:.3g}'.format(area))


sa = (int(input('Enter side a : ')))
sb = (int(input('Enter side b  : ')))
sc = (int(input('Enter side c : ')))

perimeter = sa + sb + sc
print('The perimeter of the triangle is ','{0:.3g}'.format(perimeter))


length = (int(input('Enter length : ')))
width = (int(input('Enter width : ')))
perimeter2 = 2 *(length + width)

print('The perimeter of the Rectangle is ','{0:.3g}'.format(perimeter2))

radius = int(input('Enter the radius : '))
circleArea = math.pi * math.pow(radius , 2)
print('The radius of the circle is','{0:.3g}'.format(circleArea))

x = int(input('Enter x  : '))
ySlope = (2 * x) - 2
print('The slope is',ySlope)

x1 = int(input('Enter x1 : '))
y1 = int(input('Enter y1 '))
x2 = int(input('Enter x2 : '))
y2 = int(input('Enter y2 : '))

m  = (y2 - y1 )/(x2 - x1)
print('slope is ',m)


m  = True

slopeComparison = "gua  lebih besar dari elu" if m > ySlope else "lu lebih kecil"
print(slopeComparison)

yValue  = (math.pow(x,2) + (6 * x)) + 9
print(yValue)

print(len('python') == len('dragon'))

print('on' in  'python:' & 'dragon')

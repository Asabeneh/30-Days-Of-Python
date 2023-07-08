import math
print('on' in  'python:' and  'on' in 'dragon')
print('a in an:', 'a' in 'an')

print('jargon' in 'I hope this course is not full of jargon.')

print('on'is not'python'  and  'on' is not 'dragon' )

pyt  = len('python')
print(pyt)
fpyt = float(pyt)
strfpyt = str(fpyt)
print(type(strfpyt))

types = type(10)
typeZ = type('10')

isRun   = "Equal" if types == typeZ else "Not equal"
print(isRun)

str = '9.8'
Fstr = float(str)
Istr = int(Fstr)
isCheck = "Equals" if Istr == 10 else "not equals"
print(isCheck)


hour = int(input('Enter hours : '))
rph = int(input('Enter rate per hour : '))

weekly = (60 / (24 * 7)) +(hour * rph)
weeklys = int(weekly)
print('Your weekly earnings ' , weeklys)

years = (60 * 60 * 24 *(365   * 100))
print(years)

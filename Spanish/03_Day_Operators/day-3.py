# Operaciones aritméticas en Python
# Integers

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # La división en python da un número flotante
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # da sin el número flotante o sin el resto
print('Modulus: ', 3 % 2)                           # Da el resto
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # significa 3 * 3

# Números Floating 
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Números Complex
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declarar la variable en la parte superior primero

a = 3 # a es un nombre de variable y 3 es un tipo de dato entero
b = 2 # b es un nombre de variable y 3 es un tipo de dato entero

# Operaciones aritméticas y asignación del resultado a una variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# Debería haber usado sum en lugar de total, pero sum es una función integrada. Trate de evitar anular las funciones integradas.
print(total) # si no etiqueta su impresión con alguna cadena, nunca sabrá de dónde viene el resultado
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declarar valores y organizarlos juntos
num_one = 3
num_two = 4

# Operaciones aritmeticas
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Imprimiendo valores con etiqueta
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Cálculo del área de un círculo
radius = 10                                 # radio de un circulo
area_of_circle = 3.14 * radius ** 2         # dos * signo significa exponente o potencia
print('Area of a circle:', area_of_circle)

# Calcular el área de un rectángulo
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calcular el peso de un objeto
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, porque 3 es mayor que 2
print(3 >= 2)    # True, porque 3 es mayor que 2
print(3 < 2)     # False,  porque 3 es mayor que 2
print(2 < 3)     # True, porque 2 es menor que 3
print(2 <= 3)    # True, porque 2 es menor que 3
print(3 == 2)    # False, porque 3 no es igual a 2
print(3 != 2)    # True, porque 3 no es igual a 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Comparación booleana
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Comparación de otra forma
print('1 is 1', 1 is 1)                   # True - porque los valores de los datos son los mismos
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A encontrado en la cadena
print('B in Asabeneh', 'B' in 'Asabeneh') # False - no hay b mayúscula
print('coding' in 'coding for all') # True - porque codificar para todos tiene la palabra codificar
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - porque ambas afirmaciones son verdaderas
print(3 > 2 and 4 < 3) # False - porque la segunda afirmación es falsa
print(3 < 2 and 4 < 3) # False - porque ambas afirmaciones son falsas
print(3 > 2 or 4 > 3)  # True - porque ambas afirmaciones son verdaderas
print(3 > 2 or 4 < 3)  # True - porque uno de los enunciados es verdadero
print(3 < 2 or 4 < 3)  # False - porque ambas afirmaciones son falsas
print(not 3 > 2)     # False - porque 3 > 2 es verdadero, entonces not verdadero da falso
print(not True)      # False - Negación, el operador not devuelve verdadero a falso
print(not False)     # True
print(not not True)  # True
print(not not False) # False
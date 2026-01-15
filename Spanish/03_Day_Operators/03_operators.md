<div align="center">
  <h1> 30 días de Python: Día 3 - Operadores</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Author:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Second Edition: July, 2021</small>
</sub>
</div>

[<< Dia 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Dia 4 >>](../04_Day_Strings/04_strings.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 3](#📘-día-3)
   - [Booleano](#booleano)
   - [Operadores](#operadores)
     - [Operadores de asignación](#operadores-de-asignación)
     - [Operadores aritméticos:](#operadores-aritméticos)
     - [Operadores de comparación](#operadores-de-comparación)
     - [Operadores lógicos](#operadores-lógicos)
   - [💻 Ejercicios - Día 3](#💻-ejercicios---día-3)

# 📘 Día 3

## Booleano

Un tipo de datos booleano representa uno de los dos valores: _Verdadero_ o _Falso_. El uso de estos tipos de datos quedará claro una vez que comencemos a usar el operador de comparación. La primera letra **T** para Verdadero y **F** para Falso debe ser en mayúscula a diferencia de JavaScript.
**Ejemplo: valores booleanos**

```py
print(True)
print(False)
```

## Operadores

Python language supports several types of operators. In this section, we will focus on few of them.

### Operadores de asignación

Los operadores de asignación se utilizan para asignar valores a las variables. Tomemos = como ejemplo. El signo igual en matemáticas muestra que dos valores son iguales, sin embargo, en Python significa que estamos almacenando un valor en una determinada variable y lo llamamos asignación o asignación de valor a una variable. La siguiente tabla muestra los diferentes tipos de operadores de asignación de Python, tomados de [w3school](https://www.w3schools.com/python/python_operators.asp).

![Operadores de Asignación](../../images/assignment_operators.png)

### Operadores aritméticos:

- Suma (+): a + b
- Resta(-): a - b
- Multiplicación(*): a * b
- División(/): a/b
- Módulo(%): a % b
- División de piso(//): a // b
- Exponenciación(**): a ** b

![Arithmetic Operators](../../images/arithmetic_operators.png)

**Ejemplo: Enteros**

```py
# Operaciones aritméticas en Python
# enteros

print('Addition: ', 1 + 2)        # 3
print('Subtraction: ', 2 - 1)     # 1
print('Multiplication: ', 2 * 3)  # 6
print ('Division: ', 4 / 2)       # 2.0  La división en Python da un número flotante
print('Division: ', 6 / 2)        # 3.0         
print('Division: ', 7 / 2)        # 3.5
print('Division without the remainder: ', 7 // 2)   # 3,  da sin el número flotante o sin el resto
print ('Division without the remainder: ',7 // 3)   # 2
print('Modulus: ', 3 % 2)         # 1, da el resto
print('Exponentiation: ', 2 ** 3) # 9 significa 2 * 2 * 2
```

**Ejemplo: Floats**

```py
# Números flotantes
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)
```

**Ejemplo: Números complex**

```py
# Números complejos
print('Complex number: ', 1 + 1j)
print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
```

Declaremos una variable y asignemos un tipo de dato numérico. Voy a usar una variable de un solo carácter, pero recuerde que no desarrolle el hábito de declarar este tipo de variables. Los nombres de las variables deben ser siempre mnemotécnicos.

**Ejemplo:**

```python
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

# Debería haber usado sum en lugar de total, pero sum es una función integrada; trate de evitar anular las funciones integradas
print(total) # si no etiqueta su impresión con alguna cadena, nunca sabrá de dónde viene el resultado
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponentiation)
```

**Ejemplo:**

```py
print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# Declarar valores y organizarlos juntos
num_one = 3
num_two = 4

# Operaciones aritmeticas
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Imprimiendo valores con etiqueta
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)
```

Empecemos a conectar los puntos y empecemos a hacer uso de lo que ya sabemos para calcular (área, volumen, densidad, peso, perímetro, distancia, fuerza).

**Ejemplo:**
```py
# Cálculo del área de un círculo
radius = 10                                 # radio de un circulo
area_of_circle = 3.14 * radius ** 2         # dos signo * significa exponente o potencia
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
print(weight, 'N')                         # Agregando unidad al peso

# Calcular la densidad de un líquido
mass = 75 # en kg
volume = 0.075 # en metros cúbicos
density = mass / volume # 1000 Kg/m^3

```

### Operadores de comparación

En programación comparamos valores, usamos operadores de comparación para comparar dos valores. Comprobamos si un valor es mayor o menor o igual a otro valor. La siguiente tabla muestra los operadores de comparación de Python que se tomaron de [w3shool](https://www.w3schools.com/python/python_operators.asp).

![Operadores de comparación](../../images/comparison_operators.png)
**Ejemplo: Operadores de comparación**

```py
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


# Comparar algo da un True o False

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
```

Además del operador de comparación anterior, Python usa:

- _is_: Devuelve True si ambas variables son el mismo objeto (x es y)
- _is not_: Devuelve True si ambas variables no son el mismo objeto (x no es y)
- _in_: Devuelve True si la lista consultada contiene un elemento determinado (x en y)
- _not in_: Devuelve True si la lista consultada no tiene un elemento determinado (x en y)

```py
print('1 is 1', 1 is 1)                   # True - porque los valores de los datos son los mismos
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A encontrado en la cadena
print('B in Asabeneh', 'B' in 'Asabeneh') # False - no hay b mayúscula
print('coding' in 'coding for all') # True - porque 'coding for all' tiene la palabra 'coding'
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True
```

### Operadores lógicos

A diferencia de otros lenguajes de programación, Python utiliza las palabras clave _and_, _or_ y _not_ para los operadores lógicos. Los operadores lógicos se utilizan para combinar sentencias condicionales:

![Operadores lógicos](../../images/logical_operators.png)

```py
print(3 > 2 and 4 > 3) # True - porque ambas afirmaciones son verdaderas
print(3 > 2 and 4 < 3) # False - porque la segunda afirmación es falsa
print(3 < 2 and 4 < 3) # False - porque ambas afirmaciones son falsas
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - porque ambas afirmaciones son verdaderas
print(3 > 2 or 4 < 3)  # True - porque una de las afirmaciones es verdadera
print(3 < 2 or 4 < 3)  # False - porque ambas afirmaciones son falsas
print('True or False:', True or False)
print(not 3 > 2)     # False - porque 3 > 2 es verdadero, entonces no verdadero da falso
print(not True)      # False - Negación, el operador not devuelve verdadero a falso
print(not False)     # True
print(not not True)  # True
print(not not False) # False

```

🌕 Tienes una energía ilimitada. Acaba de completar los desafíos del día 3 y está tres pasos por delante en su camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios - Día 3

1. Declara tu edad como variable entera
2. Declara tu altura como una variable flotante
3. Declarar una variable que almacene un número complejo
4. Escriba un script que solicite al usuario que ingrese la base y la altura del triángulo y calcule el área de este triángulo (área = 0,5 x b x h).

```py
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
```

5. Escriba un script que solicite al usuario que ingrese el lado a, el lado b y el lado c del triángulo. Calcula el perímetro del triángulo (perímetro = a + b + c).

```py
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
```

6. Obtenga la longitud y el ancho de un rectángulo usando el indicador. Calcula su área (área = largo x ancho) y perímetro (perímetro = 2 x (largo + ancho))
7. Obtenga el radio de un círculo usando el aviso. Calcula el área (área = pi x r x r) y la circunferencia (c = 2 x pi x r) donde pi = 3,14.
8. Calcular la pendiente, la intersección x y la intersección y de y = 2x -2
9. La pendiente es (m = y2-y1/x2-x1). Encuentre la pendiente y la [distancia euclidiana](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) entre el punto (2, 2) y el punto (6,10)
10. Compara las pendientes en las tareas 8 y 9.
11. Calcula el valor de y (y = x^2 + 6x + 9). Trate de usar diferentes valores de x y descubra en qué valor de x y será 0.
12. Encuentra la longitud de 'python' y 'dragon' y haz una declaración de comparación falsa.
13. Use el operador _and_ para verificar si 'on' se encuentra tanto en 'python' como en 'dragon'
14. _Espero que este curso no esté lleno de jerga_. Use el operador _in_ para verificar si _jerga_ está en la oración.
15. No hay 'on' ni en dragón ni en pitón
16. Encuentre la longitud del texto _python_ y convierta el valor en flotante y conviértalo en cadena
17. Los números pares son divisibles por 2 y el resto es cero. ¿Cómo verifica si un número es par o no usando python?
18. Verifique si la división de piso de 7 por 3 es igual al valor int convertido de 2.7.
19. Comprueba si el tipo de '10' es igual al tipo de 10
20. Comprueba si int('9.8') es igual a 10
21. Escriba un script que solicite al usuario que ingrese las horas y la tarifa por hora. ¿Calcular el salario de la persona?

```py
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
```

22. Escriba un script que le solicite al usuario que ingrese el número de años. Calcula el número de segundos que una persona puede vivir. Suponga que una persona puede vivir cien años.

```py
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
```

23. Escriba un script de Python que muestre la siguiente tabla

```py
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```

🎉 ¡FELICITACIONES! 🎉

[<< Day 2](../02_Day_Variables_builtin_functions/02_variables_builtin_functions.md) | [Day 4 >>](../04_Day_Strings/04_strings.md)

<div align="center">
  <h1> 30 días de Python: Día 2 - Variables y funciones integradas</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Segunda edición: julio de 2021</small>
</sub>

</div>

[<< Día 1](../readme.md) | [Día 3 >>](../03_Day_Operators/03_operators.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

_Lectura aproximada: 12 min_

- [📘 Día 2](#-día-2)
  - [Funciones integradas](#funciones-integradas)
  - [Variables](#variables)
    - [Declarar varias variables en una línea](#declarar-varias-variables-en-una-línea)
  - [Tipos de datos](#tipos-de-datos)
  - [Conversión de tipos de datos](#conversión-de-tipos-de-datos)
  - [Números](#números)
  - [💻 Ejercicios - Día 2](#-ejercicios---día-2)
    - [Ejercicio: Nivel 1](#ejercicio-nivel-1)
    - [Ejercicio: Nivel 2](#ejercicio-nivel-2)

# 📘 Día 2

## Funciones integradas

Python proporciona muchas funciones integradas. Las funciones integradas están disponibles a nivel global, lo que significa que puede usarlas sin importar o configurar nada. A continuación se muestran algunas de las funciones integradas más comunes de Python: _print()_, _len()_, _type()_, _int()_, _float()_, _str()_, _input()_, _list()_, _dict()_, _min()_, _max()_, _sum()_, _sorted()_, _open()_, _file()_, _help()_, _dir()_. En la tabla siguiente verá la lista completa de funciones integradas obtenida de la [documentación de Python](https://docs.python.org/3.9/library/functions.html).

![Built-in Functions](../../images/builtin-functions.png)

Abramos el intérprete interactivo de Python y comencemos a usar algunas de las funciones integradas más comunes.

![Built-in functions](../../images/builtin-functions_practice.png)

Practique más usando diferentes funciones integradas

![Help and Dir Built in Functions](../../images/help_and_dir_builtin.png)

Como se muestra arriba, Python tiene palabras reservadas. No podemos usar palabras reservadas para declarar variables o funciones. Presentaremos las variables en la sección siguiente.

Confío en que ahora esté familiarizado con las funciones integradas. Practiquemos más con ellas antes de continuar a la siguiente sección.

![Min Max Sum](../../images/builtin-functional-final.png)

## Variables

Las variables almacenan datos en la memoria del ordenador. En muchos lenguajes de programación se recomienda usar nombres de variables mnemotécnicos. Un nombre mnemotécnico es un nombre de variable fácil de recordar y asociar. Una variable hace referencia a la dirección de memoria donde se almacena un dato.

Al nombrar variables, no se permite empezar con un número, usar caracteres especiales ni guiones. Una variable puede tener un nombre corto (por ejemplo x, y, z), pero se recomienda encarecidamente usar nombres más descriptivos (nombre, apellido, edad, país).

Reglas para nombres de variables en Python

- El nombre de la variable debe comenzar con una letra o un guion bajo
- El nombre de la variable no puede comenzar con un número
- El nombre de la variable sólo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _)
- Los nombres de variables distinguen mayúsculas de minúsculas (firstname, Firstname, FirstName y FIRSTNAME son variables diferentes)

A continuación algunos ejemplos de nombres válidos:

```shell
firstname
lastname
age
country
city
first_name
last_name
capital_city
	_if # si queremos usar una palabra reservada como variable
year_2021
year2021
current_year_2021
birth_year
num1
num2
```

Nombres de variables inválidos

```shell
first-name
first@name
first$name
num-1
1num
```
Usaremos la convención de nombres estándar adoptada por muchos desarrolladores de Python. Los desarrolladores de Python usan la convención snake_case. Para variables que contienen varias palabras usamos guiones bajos entre las palabras (por ejemplo first_name, last_name, engine_rotation_speed). El siguiente ejemplo muestra la convención estándar: cuando el nombre de la variable contiene más de una palabra, se deben usar guiones bajos.

Cuando asignamos un valor a una variable, esto se llama declarar una variable. Por ejemplo, en el siguiente ejemplo mi nombre se asigna a la variable first_name. El signo igual es el operador de asignación. Asignar significa almacenar un dato en una variable. El signo igual en Python no es el mismo que en matemáticas.

_Ejemplo:_

```py
# Variables en Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
```

Usemos las funciones integradas _print()_ y _len()_. La función print puede aceptar un número ilimitado de argumentos. Un argumento es un valor que podemos pasar dentro de los paréntesis de la función; vea el ejemplo a continuación.

**Ejemplo:**

```py
print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',', 'World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument
```

Imprimamos y calculemos la longitud de las variables declaradas arriba：


**Ejemplo:**

```py
# Imprimir valores de las variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)
```

### Declarar varias variables en una línea

También se pueden declarar múltiples variables en la misma línea：

**Ejemplo:**

```py
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
```

Use la función integrada _input()_ para obtener entrada del usuario. Asignemos los datos ingresados por el usuario a las variables first_name y age.
.
**Ejemplo:**

```py
first_name = input('What is your name: ') 
age = input('How old are you? ')

print(first_name)
print(age)
```

## Tipos de datos

Hay varios tipos de datos en Python. Para identificar el tipo de un dato usamos la función integrada _type_.  Le recomiendo dominar los distintos tipos de datos: en programación todo está relacionado con los tipos de datos. Ya introduje los tipos de datos al principio y los vuelvo a mencionar porque cada tema está relacionado con los tipos de datos. Estudiaremos cada tipo con más detalle en capítulos posteriores.

## Conversión de tipos de datos

- Comprobar el tipo de dato: Para comprobar el tipo de un dato/variable usamos la función _type_

  **Ejemplo:**

```py
# Diferentes tipos de datos en Python
# Declaramos algunas variables con distintos tipos de datos

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, no se preocupe, esta no es mi edad real :) 

# Printing out types
print(type('Asabeneh'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set
```

- Conversión de tipos: convertir un tipo de dato a otro. Usamos _int()_, _float()_, _str()_, _list_, _set_.
Cuando realizamos operaciones aritméticas, las cadenas que contienen números deben convertirse primero a int o float, de lo contrario se producirá un error. Si concatenamos un número y una cadena, hay que convertir primero el número a cadena. Veremos la concatenación en la sección de cadenas.


  **Ejemplo:**

```py
# De entero a float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# De float a entero
gravity = 9.81
print(int(gravity))             # 9

# De entero a cadena
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# De cadena a entero o float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# De cadena a lista
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

## Números

Diferentes tipos numéricos en Python

- Integer: números enteros (negativos, 0 y positivos)
    Ejemplo:
    ... -3, -2, -1, 0, 1, 2, 3 ...
- Float: números de punto flotante
    Ejemplo
    ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complex: números complejos
    Ejemplo
    1 + j, 2 + 4j, 1 - 1j

🌕 ¡Excelente! Acabas de completar el desafío del Día 2, estás un paso más cerca del éxito. Ahora realiza algunos ejercicios para ejercitar tu mente y tus habilidades.


## 💻 Ejercicios - Día 2

### Ejercicio: Nivel 1

1. Crea una carpeta `day_2` dentro de la carpeta `30DaysOfPython`. Dentro de esa carpeta crea un archivo `variables.py`
2. Añade un comentario: 'Día 2: 30 Days of Python programming'
3. Declara una variable `first_name` y asígnale un valor
4. Declara una variable `last_name` y asígnale un valor
5. Declara una variable `full_name` y asígnale un valor
6. Declara una variable `country` y asígnale un valor
7. Declara una variable `city` y asígnale un valor
8. Declara una variable `age` y asígnale un valor
9. Declara una variable `year` y asígnale un valor
10. Declara una variable `is_married` y asígnale un valor
11. Declara una variable `is_true` y asígnale un valor
12. Declara una variable `is_light_on` y asígnale un valor
13. Declara múltiples variables en una sola línea

### Ejercicio: Nivel 2

1. Usa la función integrada _type()_ para comprobar el tipo de las variables que declaraste
1. Usa la función _len()_ para calcular la longitud de la variable `first_name`
1. Compara la longitud de las variables `first_name` y `last_name`
1. Declara las variables `num_one = 5` y `num_two = 4`
    1. Suma `num_one` y `num_two` y asigna el resultado a la variable `total`
    2. Resta `num_two` de `num_one` y asigna el resultado a la variable `diff`
    3. Multiplica `num_one` y `num_two` y asigna el resultado a la variable `product`
    4. Divide `num_one` entre `num_two` y asigna el resultado a la variable `division`
    5. Usa la operación módulo para obtener el resto de `num_two` dividido por `num_one` y asígnalo a `remainder`
    6. Calcula `num_one` elevado a `num_two` y asigna el valor a `exp`
    7. Calcula la división entera de `num_one` entre `num_two` (operación de floor division) y asigna el resultado a `floor_division`
1. El círculo tiene un radio de 30 metros.
    1. Calcula el área del círculo y asígnala a la variable `_area_of_circle_`
    2. Calcula la circunferencia del círculo y asígnala a la variable `_circum_of_circle_`
    3. Pide el radio al usuario y calcula el área.
1. Usa la función integrada `input()` para obtener nombre, apellido, país y edad del usuario y almacena los valores en las variables correspondientes
1. Ejecuta `help('keywords')` en el intérprete de Python o en un archivo para comprobar las palabras reservadas (keywords) de Python



🎉 ¡Felicidades! 🎉

[<< Día 1](../readme.md) | [Día 3 >>](../03_Day_Operators/03_operators.md)
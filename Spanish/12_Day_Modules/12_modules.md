<div align="center">
  <h1> 30 días de Python: Día 12 - Módulos </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>Segunda edición: julio de 2021</small>
</sub>

</div>

[<< Día 11](../11_Day_Functions/11_functions.md) | [Día 13 >>](../13_Day_List_comprehension/13_list_comprehension.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 12](#-día-12)
  - [Módulos](#módulos)
    - [¿Qué es un módulo?](#¿qué-es-un-módulo?)
    - [Crear módulos](#crear-módulos)
    - [Importar módulos](#importar-módulos)
    - [Importar funciones desde un módulo](#importar-funciones-desde-un-módulo)
    - [Importar funciones y renombrarlas](#importar-funciones-y-renombrarlas)
  - [Importar módulos incorporados](#importar-módulos-incorporados)
    - [Módulo OS](#módulo-os)
    - [Módulo sys](#módulo-sys)
    - [Módulo statistics](#módulo-statistics)
    - [Módulo math](#módulo-math)
    - [Módulo string](#módulo-string)
    - [Módulo random](#módulo-random)
  - [💻 Ejercicios: Día 12](#-ejercicios-día-12)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)
    - [Ejercicios: Nivel 3](#ejercicios-nivel-3)

# 📘 Día 12

## Módulos

### ¿Qué es un módulo?

Un módulo es un archivo que contiene un conjunto de código o funciones que se pueden incluir en una aplicación. Un módulo puede ser un archivo con una sola variable, una función o una biblioteca de gran escala.

### Crear módulos

Para crear un módulo, escribimos código en un script de Python y lo guardamos con extensión .py. En la carpeta del proyecto crea un archivo llamado mymodule.py. Escribamos algo de código en ese archivo.

```py
# archivo mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

En el directorio del proyecto crea un archivo main.py e importa mymodule.py.

### Importar módulos

Para importar archivos usamos la palabra clave import y el nombre del archivo.

```py
# archivo main.py
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### Importar funciones desde un módulo

Podemos tener muchas funciones en un archivo y podemos importar cada una por separado.

```py
# archivo main.py
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Importar funciones y renombrarlas

Durante la importación también podemos renombrar nombres.

```py
# archivo main.py
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Importar módulos incorporados

Al igual que otros lenguajes, podemos importar módulos usando la palabra clave import. A continuación importamos algunos módulos incorporados que usamos con frecuencia. Algunos módulos comunes son: math, datetime, os, sys, random, statistics, collections, json, re

### Módulo OS

El módulo os de Python permite automatizar muchas tareas del sistema operativo. El módulo OS ofrece funciones para crear, cambiar directorio de trabajo, eliminar directorios (carpetas), obtener su contenido y reconocer/cambiar el directorio actual.

```py
# importar módulo
import os
# crear directorio
os.mkdir('directory_name')
# cambiar el directorio actual
os.chdir('path')
# obtener el directorio actual
os.getcwd()
# eliminar directorio
os.rmdir()
```

### Módulo sys

El módulo sys provee funciones y variables para interactuar con diferentes partes del entorno de ejecución de Python. La función sys.argv devuelve la lista de argumentos de la línea de comandos pasados al script de Python. El elemento en el índice 0 de esa lista es siempre el nombre del script, el índice 1 es el primer argumento pasado desde la línea de comandos.

Ejemplo archivo script.py:

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # esta línea imprimirá: nombre_archivo argumento1 argumento2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

Para ver cómo funciona el script, en la línea de comandos escribe:

```sh
python script.py Asabeneh 30DaysOfPython
```

Resultado:

```sh
Welcome Asabeneh. Enjoy  30DayOfPython challenge!
```

Algunos comandos útiles de sys:

```py
# salir del script
sys.exit()
# conocer el tamaño máximo de un entero
sys.maxsize
# conocer la ruta de módulos
sys.path
# conocer la versión de Python en uso
sys.version
```

### Módulo statistics

El módulo statistics proporciona funciones de estadísticas para datos numéricos. Algunas funciones comunes definidas en este módulo: mean, median, mode, stdev, etc.

```py
from statistics import * # importar todo del módulo statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Módulo math

Contiene muchas operaciones matemáticas y constantes.

```py
import math
print(math.pi)           # 3.141592653589793, constante pi
print(math.sqrt(2))      # 1.4142135623730951, raíz cuadrada
print(math.pow(2, 3))    # 8.0, potencia
print(math.floor(9.81))  # 9, redondeo hacia abajo
print(math.ceil(9.81))   # 10, redondeo hacia arriba
print(math.log10(100))   # 2, logaritmo base 10
```

Ahora que hemos importado el módulo math con muchas funciones útiles, podemos ver qué funciones contiene usando help(math) o dir(math). Si sólo queremos importar funciones específicas podemos hacerlo así:

```py
from math import pi
print(pi)
```

También podemos importar múltiples funciones:

```py
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
```

Si queremos importar todas las funciones del módulo matemático podemos usar *.

```py
from math import *
print(pi)                  # 3.141592653589793, constante pi
print(sqrt(2))             # 1.4142135623730951, raíz cuadrada
print(pow(2, 3))           # 8.0, potencia
print(floor(9.81))         # 9, redondeo hacia abajo
print(ceil(9.81))          # 10, redondeo hacia arriba
print(math.log10(100))     # 2
```

También podemos renombrar funciones al importarlas.

```py
from math import pi as PI
print(PI) # 3.141592653589793
```

### Módulo string

El módulo string es muy útil. Los siguientes ejemplos muestran algunos usos.

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Módulo random

Ahora que sabes importar módulos, familiaricémonos con random. El módulo random nos da números aleatorios entre 0 y 0.9999. El módulo tiene muchas funciones; aquí usamos random y randint.

```py
from random import random, randint
print(random())   # no necesita parámetros; devuelve un valor entre 0 y 0.9999
print(randint(5, 20)) # devuelve un entero aleatorio en [5, 20] (inclusive)
```

🌕 ¡Has llegado muy lejos. Sigue así! Acabas de completar el desafío del Día 12 y has dado 12 pasos hacia algo grandioso. Ahora ejercita tu mente y tus músculos.

## 💻 Ejercicios: Día 12

### Ejercicios: Nivel 1

1. Escribe una función que genere un random_user_id de seis caracteres/dígitos.
   ```py
     print(random_user_id());
     '1ee33d'
   ```
2. Modifica la tarea anterior. Declara una función llamada user_id_gen_by_user. No acepta argumentos, pero pide dos entradas: una es la cantidad de caracteres por ID y la otra es cuántos IDs generar.

```py
print(user_id_gen_by_user()) # entrada del usuario: 5 5
#salida:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3. Escribe una función llamada rgb_color_gen. Debe generar un color RGB (cada valor en el rango 0-255).

```py
print(rgb_color_gen())
# rgb(125,244,255) - la salida debe estar en este formato
```

### Ejercicios: Nivel 2

1. Escribe una función list_of_hexa_colors que devuelva una lista con cualquier cantidad de colores hexadecimales (seis dígitos hexadecimales después de #; el sistema hex usa 0-9 y a-f).
2. Escribe una función list_of_rgb_colors que devuelva una lista con cualquier cantidad de colores RGB.
3. Escribe una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o RGB.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
```

### Ejercicios: Nivel 3

1. Llama a tu función shuffle_list, que recibe una lista y devuelve la lista mezclada.
2. Escribe una función que devuelva una lista de siete números aleatorios únicos en el rango 0-9.

🎉 ¡Felicidades! 🎉

[<< Día 11](../11_Day_Functions/11_functions.md) | [Día 13 >>](../13_Day_List_comprehension/13_list_comprehension.md)

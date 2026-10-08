<div align="center">
  <h1> 30 días de Python: Día 15 - Errores de tipo </h1>
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

[<< Día 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Día 16 >>](../16_Day_Python_date_time/16_python_datetime.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 15](#día-15)
  - [Tipos de error en Python](#tipos-de-error-en-python)
    - [SyntaxError (Error de sintaxis)](#syntaxerror-error-de-sintaxis)
    - [NameError (Error de nombre)](#nameerror-error-de-nombre)
    - [IndexError (Error de índice)](#indexerror-error-de-índice)
    - [ModuleNotFoundError (Módulo no encontrado)](#modulenotfounderror-módulo-no-encontrado)
    - [AttributeError (Error de atributo)](#attributeerror-error-de-atributo)
    - [KeyError (Error de clave)](#keyerror-error-de-clave)
    - [TypeError (Error de tipo)](#typeerror-error-de-tipo)
    - [ImportError (Error de importación)](#importerror-error-de-importación)
    - [ValueError (Error de valor)](#valueerror-error-de-valor)
    - [ZeroDivisionError (Error de división por cero)](#zerodivisionerror-error-de-división-por-cero)
  - [💻 Ejercicios - Día 15](#-ejercicios---día-15)

# 📘 Día 15

## Tipos de error en Python

Al escribir código, con frecuencia cometemos errores tipográficos u otros errores comunes. Si nuestro código falla, el intérprete de Python muestra un mensaje que nos da retroalimentación sobre dónde ocurrió el problema y cuál es el tipo de error. A veces incluso sugiere posibles soluciones. Conocer los distintos tipos de errores en el lenguaje nos ayudará a depurar más rápido y a mejorar nuestras habilidades de programación.

Revisemos los tipos de error más comunes uno por uno. Primero, abre el intérprete interactivo de Python. Ve a la terminal de tu equipo e ingresa 'python'. Se abrirá el intérprete interactivo de Python.

### SyntaxError (Error de sintaxis)

**Ejemplo 1: SyntaxError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

Como ves, cometimos un error de sintaxis porque olvidamos encerrar la cadena entre paréntesis; Python incluso sugiere la corrección. Arreglémoslo.

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

Ese fue un SyntaxError. Tras corregirlo, el código se ejecuta correctamente. Veamos otros tipos de errores.

### NameError (Error de nombre)

**Ejemplo 1: NameError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

El mensaje indica que el nombre age no está definido. En efecto, no hemos declarado age pero intentamos imprimirlo. Solucionémoslo declarando la variable y asignándole un valor.

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

Ese fue un NameError. Lo depuramos definiendo la variable.

### IndexError (Error de índice)

**Ejemplo 1: IndexError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

En este ejemplo Python lanzó un IndexError porque los índices válidos de la lista son 0 a 4; el índice 5 está fuera de rango.

### ModuleNotFoundError (Módulo no encontrado)

**Ejemplo 1: ModuleNotFoundError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

Aquí añadí intencionadamente una 's' extra a math, lo que produjo un ModuleNotFoundError. Corrijámoslo quitando la 's'.

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

Lo hemos corregido y ahora podemos usar el módulo math.

### AttributeError (Error de atributo)

**Ejemplo 1: AttributeError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

Aquí intenté acceder a math.PI en lugar de math.pi, lo que produjo un AttributeError porque ese atributo no existe. Corrijámoslo usando el nombre correcto:

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

Ahora la llamada devuelve el valor esperado.

### KeyError (Error de clave)

**Ejemplo 1: KeyError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

Aquí hay un error de ortografía en la clave usada para obtener un valor del diccionario. Es un KeyError; la solución es usar la clave correcta.

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

Error depurado; el código devuelve el resultado esperado.

### TypeError (Error de tipo)

**Ejemplo 1: TypeError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

En este caso aparece un TypeError porque no podemos sumar un entero y una cadena. Una solución es convertir la cadena a int o float; otra es convertir el entero a cadena para concatenarlos. Probemos la primera solución:

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

El error desaparece y obtenemos el resultado esperado.

### ImportError (Error de importación)

**Ejemplo 1: ImportError**

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

El módulo math no tiene una función llamada power; la función correcta es pow. Corrijámoslo:

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### ValueError (Error de valor)

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

No podemos convertir la cadena dada a número porque contiene la letra 'a'.

### ZeroDivisionError (Error de división por cero)

```python
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

No podemos dividir un número por cero.

Hemos revisado varios tipos de errores en Python; para más información, consulta la documentación oficial sobre excepciones en Python. Si te acostumbras a leer los mensajes de error, podrás corregir tus bugs rápidamente y convertirte en un mejor programador.

🌕 Vas progresando. Has completado la mitad del camino hacia algo genial. Ahora haz algunos ejercicios para entrenar tu cerebro y tus manos.

## 💻 Ejercicios - Día 15

1. Abre tu intérprete interactivo de Python y prueba todos los ejemplos mostrados en esta sección.

🎉 ¡Felicidades! 🎉

[<< Día 14](../14_Day_Higher_order_functions/14_higher_order_functions.md) | [Día 16 >>](../16_Day_Python_date_time/16_python_datetime.md)
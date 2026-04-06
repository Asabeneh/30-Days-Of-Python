<div align="center">
  <h1> 30 días de Python: Día 17 - Manejo de excepciones </h1>
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

[<< Día 16](../16_Day_Python_date_time/16_python_datetime.md) | [Día 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 17](#-día-17)
  - [Manejo de excepciones](#manejo-de-excepciones)
  - [Empacar y desempacar parámetros en Python](#empacar-y-desempacar-parámetros-en-python)
    - [Desempaquetado](#desempaquetado)
      - [Desempaquetar listas](#desempaquetar-listas)
      - [Desempaquetar diccionarios](#desempaquetar-diccionarios)
    - [Empaquetado](#empaquetado)
    - [Empaquetar listas](#empaquetar-listas)
      - [Empaquetar diccionarios](#empaquetar-diccionarios)
  - [Expandir en Python](#expandir-en-python)
  - [Enumerar (enumerate)](#enumerar-enumerate)
  - [Zip](#zip)
  - [Ejercicios: Día 17](#ejercicios-día-17)

# 📘 Día 17

## Manejo de excepciones

Python utiliza _try_ y _except_ para manejar errores de forma elegante. Salir de forma controlada (o manejar errores con elegancia) es una buena práctica: el programa detecta una condición de error y la maneja adecuadamente, normalmente mostrando un mensaje descriptivo en la terminal o en un registro. Las excepciones suelen deberse a factores externos al programa (entrada errónea, nombre de archivo incorrecto, archivo no encontrado, fallos de I/O, etc.). El manejo adecuado de excepciones evita que las aplicaciones se bloqueen.

En la sección anterior hemos cubierto los distintos tipos de errores en Python. Si usamos _try_ y _except_ correctamente, podemos impedir que esos errores hagan que el programa falle.

![Try and Except](../../images/try_except.png)

```py
try:
    # si todo va bien, se ejecuta el código en este bloque
except:
    # si ocurre un error, se ejecuta el código en este bloque
```

**Ejemplo:**

```py
try:
    print(10 + '5')
except:
    print('Ocurrió un error')
```

En el ejemplo anterior, el segundo operando es una cadena. Podemos convertirlo a int o float para sumarlo a un número; si no lo hacemos, se ejecutará el bloque _except_.

**Ejemplo:**

```py
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - year_born
    print(f'Eres {name}. Tu edad es {age}.')
except:
    print('Ocurrió un error')
```

```sh
Ocurrió un error
```

En el ejemplo anterior, se ejecuta el bloque de excepción, pero no sabemos exactamente qué pasó. Para identificar el problema podemos capturar tipos de excepción concretos.

En el siguiente ejemplo capturamos y mostramos el tipo de error:

```py
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - year_born
    print(f'Eres {name}. Tu edad es {age}.')
except TypeError:
    print('Se produjo un error de tipo (TypeError)')
except ValueError:
    print('Se produjo un ValueError')
except ZeroDivisionError:
    print('Se produjo una división por cero (ZeroDivisionError)')
```

```sh
Introduce tu nombre:Asabeneh
¿En qué año naciste?:1920
Se produjo un error de tipo (TypeError)
```

En el ejemplo anterior la salida será _TypeError_. Ahora añadamos bloques adicionales:

```py
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - int(year_born)
    print(f'Eres {name}. Tu edad es {age}.')
except TypeError:
    print('Se produjo un error de tipo (TypeError)')
except ValueError:
    print('Se produjo un ValueError')
except ZeroDivisionError:
    print('Se produjo una división por cero (ZeroDivisionError)')
else:
    print('Este bloque se ejecuta normalmente después de try')
finally:
    print('Este bloque siempre se ejecuta.')
```

```sh
Introduce tu nombre:Asabeneh
¿En qué año naciste?:1920
Eres Asabeneh. Tu edad es 99.
Este bloque se ejecuta normalmente después de try
Este bloque siempre se ejecuta.
```

También podemos simplificar el manejo de excepción así:

```py
try:
    name = input('Introduce tu nombre:')
    year_born = input('¿En qué año naciste?:')
    age = 2019 - int(year_born)
    print(f'Eres {name}. Tu edad es {age}.')
except Exception as e:
    print(e)
```

## Empacar y desempacar parámetros en Python

Usamos dos operadores:

- * para tuplas/listas
- ** para diccionarios

Veamos un ejemplo. Supongamos que una función acepta parámetros separados, pero nosotros tenemos una lista. Podemos desempaquetarla y convertirla en argumentos.

### Desempaquetado

#### Desempaquetar listas

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

Al ejecutar lo anterior ocurre un error porque la función espera números separados, no una lista. Desempaquetemos la lista:

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

También podemos usar desempaquetado con range(), que acepta inicio y fin:

```py
numbers = range(2, 7)  # llamada normal con parámetros separados
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # llamada usando los parámetros desempaquetados desde la lista
print(list(numbers))      # [2, 3, 4, 5, 6]
```

También podemos usar desempaquetado en asignaciones:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```

#### Desempaquetar diccionarios

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} vive en {city}, {country}. Tiene {age} años.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh vive en Helsinki, Finland. Tiene 250 años.
```

### Empaquetado

A veces no sabemos cuántos argumentos nos pasarán a una función. Podemos usar empaquetado para aceptar un número variable de argumentos.

### Empaquetar listas

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### Empaquetar diccionarios

```py
def packing_person_info(**kwargs):
    # comprobar el tipo de kwargs: es un dict
    # print(type(kwargs))
    # imprimir los pares clave-valor
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

## Expandir en Python

Al igual que en JavaScript, Python permite expandir listas usando el operador *. Veámoslo:

```py
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
```

## Enumerar (enumerate)

Si necesitamos los índices de una lista, usamos la función integrada enumerate.

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```py
for index, i in enumerate(countries):
    print('hola')
    if i == 'Finland':
        print(f'El país {i} está en el índice {index}')
```

```sh
0 20
1 30
2 40
```

## Zip

A veces necesitamos combinar listas. Observa el ejemplo:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

## Ejercicios: Día 17

1. Crea en _countries.py_ funciones que usen los datos de _countries_data.py_:
   - una función para encontrar los 10 idiomas más usados
   - una función para encontrar los 10 países más poblados

🎉 ¡Felicidades! 🎉

[<< Día 16](../16_Day_Python_date_time/16_python_datetime.md) | [Día 18 >>](../18_Day_Regular_expressions/18_regular_expressions.md)
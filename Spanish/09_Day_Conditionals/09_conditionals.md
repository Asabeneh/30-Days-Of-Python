<div align="center">
  <h1> 30 días de Python: Día 9 - Sentencias condicionales</h1>
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

[<< Día 8](../08_Day_Dictionaries/08_dictionaries.md) | [Día 10 >>](../10_Day_Loops/10_loops.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 9](#-día-9)
  - [Sentencias condicionales](#sentencias-condicionales)
    - [Condición If](#condición-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Abreviación](#abreviación)
    - [Condicionales anidados](#condicionales-anidados)
    - [If y operadores lógicos](#if-y-operadores-lógicos)
    - [If y operador lógico Or](#if-y-operador-lógico-or)
  - [💻 Ejercicios - Día 9](#-ejercicios---día-9)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)

# 📘 Día 9

## Sentencias condicionales

Por defecto, las sentencias en un script de Python se ejecutan secuencialmente de arriba hacia abajo. Si la lógica lo requiere, podemos cambiar el orden de dos maneras:

- Ejecución condicional: si una expresión es verdadera, se ejecutan uno o más bloques de código
- Ejecución repetitiva: mientras una expresión sea verdadera, se repiten uno o más bloques de código. En esta sección discutiremos las sentencias *if*, *else* y *elif*. Los operadores de comparación y lógicos vistos antes serán útiles aquí.

### Condición If

En Python y otros lenguajes, la palabra clave *if* se usa para comprobar si una condición es verdadera y ejecutar un bloque de código. Recuerda la indentación después de los dos puntos.

```py
# Sintaxis
if condition:
    # Si la condición es verdadera, ejecutar este bloque de código
```

**Ejemplo 1**

```py
a = 3
if a > 0:
    print('A es un número positivo')
# A es un número positivo
```

Como se muestra arriba, 3 es mayor que 0. La condición es verdadera y se ejecuta el bloque de código. Si la condición fuera falsa, no veríamos resultado; para manejar condiciones falsas usamos el bloque *else*.

### If Else

Si la condición es verdadera se ejecuta el primer bloque, de lo contrario se ejecuta el bloque *else*.

```py
# Sintaxis
if condition:
    # Si la condición es verdadera, ejecutar este bloque
else:
    # Si la condición es falsa, ejecutar este bloque
```

**Ejemplo:**

```py
a = 3
if a < 0:
    print('A es un número negativo')
else:
    print('A es un número positivo')
```

La condición anterior es falsa, por eso se ejecuta el bloque *else*. ¿Y si tenemos más de dos condiciones? Podemos usar *elif*.

### If Elif Else

En la vida tomamos decisiones cada día que implican más de una condición. En programación, cuando tenemos múltiples condiciones, usamos *elif*.

```py
# Sintaxis
if condition:
    # código
elif condition:
    # código
else:
    # código
```

**Ejemplo:**

```py
a = 0
if a > 0:
    print('A es un número positivo')
elif a < 0:
    print('A es un número negativo')
else:
    print('A es cero')
```

### Abreviación

```py
# Sintaxis
<expr> if condición else <expr>
```

**Ejemplo:**

```py
a = 3
print('A es positivo') if a > 0 else print('A es negativo') # Se cumple la primera condición, imprimirá 'A es positivo'
```

### Condicionales anidados

Los condicionales pueden anidarse.

```py
# Sintaxis
if condición:
    # código
    if condición:
        # código
```

**Ejemplo:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A es un número positivo y par')
    else:
        print('A es un número positivo')
elif a == 0:
    print('A es cero')
else:
    print('A es un número negativo')
```

Podemos usar el operador lógico *and* para evitar escribir condicionales anidados.

### If y operadores lógicos

```py
# Sintaxis
if condición and condición:
    # código
```

**Ejemplo:**

```py
a = 0
if a > 0 and a % 2 == 0:
    print('A es un número positivo y par')
elif a > 0 and a % 2 != 0:
    print('A es un número positivo')
elif a == 0:
    print('A es cero')
else:
    print('A es un número negativo')
```

### If y operador lógico Or

```py
# Sintaxis
if condición or condición:
    # código
```

**Ejemplo:**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Acceso concedido!')
else:
    print('Acceso denegado!')
```

🌕 Lo estás haciendo muy bien. Nunca te rindas; las cosas grandiosas requieren tiempo. Acabas de completar el desafío del Día 9; estás a 9 pasos en tu camino hacia lo grande. Haz ahora algunos ejercicios para entrenar tu mente y tu cuerpo.

## 💻 Ejercicios - Día 9

### Ejercicios: Nivel 1

1. Usa input para obtener la edad del usuario (por ejemplo: "Introduce tu edad:"). Si el usuario tiene 18 años o más, muestra: 'Ya tienes la edad suficiente para aprender a conducir.' Si es menor, muestra cuántos años le faltan. Ejemplo de salida:

   ```sh
   Introduce tu edad: 30
   Ya tienes la edad suficiente para aprender a conducir.
   Salida:
   Introduce tu edad: 15
   Aún necesitas esperar 3 años para aprender a conducir.
   ```

2. Usa if…else para comparar my_age y your_age. ¿Quién es mayor (yo o tú)? Usa input("Introduce tu edad:") para obtener la edad. Puedes usar condicionales anidados para imprimir 'año' cuando la diferencia sea 1, 'años' para diferencias mayores, y un mensaje personalizado si my_age = your_age. Salida de ejemplo:

   ```sh
   Introduce tu edad: 30
   Tienes 5 años más que yo.
   ```

3. Pide al usuario dos números con input. Si a > b, imprime 'a es mayor que b'; si a < b, imprime 'a es menor que b'; si son iguales, imprime 'a es igual a b'.

```sh
Introduce el primer número: 4
Introduce el segundo número: 3
4 es mayor que 3
```

### Ejercicios: Nivel 2

1. Escribe un código que asigne una calificación según la nota del estudiante:

   ```sh
   80-100, A
   70-79, B
   60-69, C
   50-59, D
   0-49, F
   ```

2. Comprueba si es otoño, invierno, primavera o verano. Si el usuario introduce:
   Septiembre, Octubre o Noviembre → otoño.
   Diciembre, Enero o Febrero → invierno.
   Marzo, Abril o Mayo → primavera.
   Junio, Julio u Agosto → verano.
3. La siguiente lista contiene algunas frutas:

   ```py
   fruits = ['banana', 'orange', 'mango', 'lemon']
   ```

   Si una fruta no está en la lista, añádela e imprime la lista modificada. Si ya existe, imprime 'La fruta ya está en la lista'.

### Ejercicios: Nivel 3

1. Aquí hay un diccionario persona. ¡Siéntete libre de modificarlo!

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finlandia',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Calle Espacial',
        'zipcode': '02210'
    }
}
```

- Comprueba si existe la clave skills en el diccionario; si existe, imprime la habilidad central de la lista skills.
- Comprueba si existe la clave skills; si existe, verifica si la persona tiene la habilidad 'Python' e imprime el resultado.
- Si las habilidades son sólo JavaScript y React, imprime 'Es desarrollador frontend'; si incluyen Node, Python y MongoDB, imprime 'Es desarrollador backend'; si incluyen React, Node y MongoDB, imprime 'Es desarrollador full-stack'; en caso contrario, imprime 'Título desconocido' — puedes anidar más condiciones para mayor precisión.
- Si la persona está casada y vive en Finlandia, imprime la siguiente línea:

```py
print('Asabeneh Yetayeh vive en Finlandia. Está casado.')
```

🎉 ¡Felicidades! 🎉

[<< Día 8](../08_Day_Dictionaries/08_dictionaries.md) | [Día 10 >>](../10_Day_Loops/10_loops.md)

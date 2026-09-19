<div align="center">
  <h1> 30 días de Python: Día 6 - Tuplas</h1>
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

[<< Día 5](../05_Day_Lists/05_lists.md) | [Día 7 >>](../07_Day_Sets/07_sets.md)

![30DaysOfPython](../../images/30DaysOfPython_banner3@2x.png)

- [Día 6](#día-6)
  - [Tuplas](#tuplas)
    - [Cómo crear tuplas](#cómo-crear-tuplas)
    - [Longitud de la tupla](#longitud-de-la-tupla)
    - [Obtener elementos de la tupla](#obtener-elementos-de-la-tupla)
    - [Slicing de tuplas](#slicing-de-tuplas)
    - [Convertir tupla a lista](#convertir-tupla-a-lista)
    - [Comprobar si un elemento está en la tupla](#comprobar-si-un-elemento-está-en-la-tupla)
    - [Unir tuplas](#unir-tuplas)
    - [Eliminar tupla](#eliminar-tupla)
  - [💻 Ejercicios - Día 6](#-ejercicios---día-6)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)

# Día 6

## Tuplas

Una tupla es una colección ordenada e inmutable que puede contener distintos tipos de datos. Una vez creada una tupla, no podemos cambiar sus valores. No podemos usar métodos como add, insert o remove en una tupla porque no es modificable (es inmutable). A diferencia de las listas, las tuplas tienen menos métodos. Los métodos asociados a tuplas son:

- tuple(): crea una tupla vacía
- count(): cuenta cuántas veces aparece un elemento en la tupla
- index(): busca el índice de un elemento en la tupla
- Operador +: concatena dos o más tuplas creando una nueva tupla

### Cómo crear tuplas

- Crear una tupla vacía

  ```py
  # Sintaxis
  empty_tuple = ()
  # o usando el constructor de tuplas
  empty_tuple = tuple()
  ```

- Crear una tupla con valores iniciales

  ```py
  # Sintaxis
  tpl = ('item1', 'item2','item3')
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  ```


### Longitud de la tupla

Usamos la función _len()_ para obtener la longitud de una tupla.

```py
# Sintaxis
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### Obtener elementos de la tupla

- Índices positivos
  Al igual que con las listas, usamos índices positivos o negativos para acceder a los elementos de una tupla.
  ![Accessing tuple items](../../images/tuples_index.png)

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3')
  first_item = tpl[0]
  second_item = tpl[1]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[0]
  second_fruit = fruits[1]
  last_index =len(fruits) - 1
  last_fruit = fruits[las_index]
  ```

- Índices negativos
  Los índices negativos cuentan desde el final: -1 es el último elemento, -2 el penúltimo, y así sucesivamente.
  ![Tuple Negative indexing](../../images/tuple_negative_indexing.png)

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3','item4')
  first_item = tpl[-4]
  second_item = tpl[-3]
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  first_fruit = fruits[-4]
  second_fruit = fruits[-3]
  last_fruit = fruits[-1]
  ```

### Slicing de tuplas

Podemos extraer subtuplas especificando un rango de índices de inicio y fin; el resultado es una nueva tupla con los elementos seleccionados.

- Rango de índices positivos

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # todos los elementos
  all_items = tpl[0:]         # todos los elementos
  middle_two_items = tpl[1:3]  # no incluye el índice 3
  ```

  ```py
  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # todos los elementos
  all_fruits= fruits[0:]      # todos los elementos
  orange_mango = fruits[1:3]  # no incluye el índice 3
  orange_to_the_rest = fruits[1:]
  ```

- Rango de índices negativos

  ```py
  # Sintaxis
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # todos los elementos
  middle_two_items = tpl[-3:-1]  # no incluye el índice 3
  ```

  ```py

  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # todos los elementos
  orange_mango = fruits[-3:-1]  # no incluye el índice 3
  orange_to_the_rest = fruits[-3:]
  ```

### Convertir tupla a lista

Podemos convertir una tupla en una lista y viceversa. Si queremos modificar una tupla, conviene convertirla primero en lista.

```py
# Sintaxis
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### Comprobar si un elemento está en la tupla

Podemos usar el operador _in_ para comprobar si un elemento pertenece a la tupla; devuelve un valor booleano.

```py
# Sintaxis
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```



### Unir tuplas

Podemos concatenar dos o más tuplas usando el operador +.

```py
# Sintaxis
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

### Eliminar tupla

No se pueden eliminar elementos individuales de una tupla, pero sí se puede eliminar la tupla completa con la palabra clave _del_.

```py
# Sintaxis
tpl1 = ('item1', 'item2', 'item3')
del tpl1

```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```


🌕 Muy bien, lo conseguiste. Acabas de completar el desafío del día 6. Ahora realiza algunos ejercicios para practicar.

## 💻 Ejercicios - Día 6

### Ejercicios: Nivel 1

1. Crea una tupla vacía
2. Crea una tupla con los nombres de tus hermanos y hermanas (pueden ser ficticios)
3. Concatena las tuplas de hermanos y asígnalas a `siblings`
4. ¿Cuántos hermanos tienes?
5. Modifica la tupla de `siblings` y añade los nombres de tus padres; asígnala a `family_members`

### Ejercicios: Nivel 2

1. Extrae los hermanos y los padres desde `family_members`
2. Crea las tuplas `fruits`, `vegetables` y `animal_products`. Concatena las tres tuplas y asígnalas a la variable `food_stuff_tp`
3. Convierte la tupla `food_stuff_tp` en la lista `food_stuff_lt`
4. Extrae los elementos del medio desde la tupla `food_stuff_tp` o la lista `food_stuff_lt`
5. Extrae las primeras tres y las últimas tres entradas de la lista `food_stuff_lt`
6. Elimina completamente la tupla `food_stuff_tp`
7. Comprueba si existen los elementos:
- Verifica si 'Estonia' está en la tupla `nordic_countries`
- Verifica si 'Iceland' está en la tupla `nordic_countries`

  ```py
  nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
  ```


[<< Día 5](../05_Day_Lists/05_lists.md) | [Día 7 >>](../07_Day_Sets/07_sets.md)

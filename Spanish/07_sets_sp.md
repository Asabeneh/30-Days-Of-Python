<div align="center">
  <h1> 30 días de Python: Día 7 - Conjuntos</h1>
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

[<< Día 6](./06_tuples_sp.md) | [Día 8 >>](./08_dictionaries_sp.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Día 7](#-día-7)
  - [Conjuntos](#conjuntos)
    - [Crear conjuntos](#crear-conjuntos)
    - [Obtener la longitud del conjunto](#obtener-la-longitud-del-conjunto)
    - [Acceder a elementos del conjunto](#acceder-a-elementos-del-conjunto)
    - [Comprobar elementos](#comprobar-elementos)
    - [Añadir elementos al conjunto](#añadir-elementos-al-conjunto)
    - [Eliminar elementos del conjunto](#eliminar-elementos-del-conjunto)
    - [Vaciar el conjunto](#vaciar-el-conjunto)
    - [Eliminar conjunto](#eliminar-conjunto)
    - [Convertir lista a conjunto](#convertir-lista-a-conjunto)
    - [Unir conjuntos](#unir-conjuntos)
    - [Encontrar intersección](#encontrar-intersección)
    - [Comprobar subconjuntos y superconjuntos](#comprobar-subconjuntos-y-superconjuntos)
    - [Comprobar la diferencia entre conjuntos](#comprobar-la-diferencia-entre-conjuntos)
    - [Encontrar diferencia simétrica](#encontrar-diferencia-simétrica)
    - [Comprobar conjuntos disjuntos](#comprobar-conjuntos-disjuntos)
  - [💻 Ejercicios - Día 7](#-ejercicios---día-7)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)
    - [Ejercicios: Nivel 3](#ejercicios-nivel-3)

# 📘 Día 7

## Conjuntos

Un conjunto es una colección de elementos. Volvamos a las clases de matemáticas de primaria o secundaria: la definición matemática de conjuntos aplica también en Python. Un conjunto es una colección desordenada y no indexada de elementos distintos. En Python, los conjuntos almacenan elementos únicos y se pueden encontrar la _unión_, la _intersección_, la _diferencia_, la _diferencia simétrica_, los _subconjuntos_, los _superconjuntos_ y los _conjuntos disjuntos_ entre conjuntos.

### Crear conjuntos

Usamos la función incorporada _set()_.

- Crear un conjunto vacío

```py
# Sintaxis
st = set()
```

- Crear un conjunto con elementos iniciales

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
```

**Ejemplo:**

```py
# Sintaxis
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### Obtener la longitud del conjunto

Usamos la función **len()** para obtener la longitud de un conjunto.

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)

```

### Acceder a elementos del conjunto

Usamos bucles para recorrer los elementos. Veremos esto con más detalle en la sección de bucles.

### Comprobar elementos

Para comprobar si un elemento existe en un conjunto usamos el operador de pertenencia _in_.

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**Ejemplo:**

```py

fruits = {'plátano', 'naranja', 'mango', 'limón'}

print('mango' in fruits ) # True

```

### Añadir elementos al conjunto

Una vez creado el conjunto no podemos cambiar elementos existentes, pero sí podemos añadir nuevos.

- Usar el método _add()_ para agregar un solo elemento

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

- Usar el método _update()_ para agregar varios elementos
  El método _update()_ permite añadir múltiples elementos; recibe un iterable como argumento.

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### Eliminar elementos del conjunto

Podemos usar el método _remove()_ para eliminar un elemento de un conjunto. Si el elemento no existe, _remove()_ lanzará un error; por eso es útil comprobar antes si existe. El método _discard()_ no lanzará error si el elemento no existe.

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

El método _pop()_ elimina y devuelve un elemento aleatorio del conjunto.

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # Elimina un elemento aleatorio del conjunto
```

Si nos interesa el elemento eliminado.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
```

### Vaciar el conjunto

Si queremos vaciar todas las entradas de un conjunto, podemos usar el método _clear()_.

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### Eliminar conjunto

Si queremos eliminar el conjunto por completo, podemos usar el operador _del_.

```py
# Sintaxis
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### Convertir lista a conjunto

Podemos convertir una lista en un conjunto y viceversa. Convertir una lista a conjunto elimina duplicados y conserva solo elementos únicos.

```py
# Sintaxis
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - El orden es aleatorio, ya que los conjuntos son generalmente no ordenados
```

**Ejemplo:**

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### Unir conjuntos

Podemos usar los métodos _union()_ o _update()_ para combinar dos conjuntos.

- Union
  Este método devuelve un nuevo conjunto

```py
# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

- Update
  Este método inserta los elementos de un conjunto en el conjunto dado

```py
# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # Los elementos de st2 se añaden a st1
```

**Ejemplo:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

### Encontrar intersección

La intersección devuelve un conjunto con los elementos que están presentes en ambos conjuntos. Véase el ejemplo.

```py
# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```

**Ejemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.intersection(dragon)     # {'o', 'n'}
```

### Comprobar subconjuntos y superconjuntos

Un conjunto puede ser subconjunto o superconjunto de otro:

- Subconjunto: _issubset()_
- Superconjunto: _issuperset()_

```py
# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**Ejemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # Falso, porque es un superconjunto
whole_numbers.issuperset(even_numbers) # Verdadero

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.issubset(dragon)     # Falso
```

### Comprobar la diferencia entre conjuntos

Devuelve la diferencia entre dos conjuntos.

```py
# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

**Ejemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.difference(dragon)     # {'p', 'y', 't'}  - El resultado es desordenado (propiedad de los conjuntos)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

### Encontrar diferencia simétrica

Devuelve la diferencia simétrica entre dos conjuntos. Es decir, devuelve los elementos que pertenecen a uno de los conjuntos pero no a ambos; matemáticamente: (A\B) ∪ (B\A).

```py
# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# Significa (A\B) ∪ (B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```

**Ejemplo:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

### Comprobar conjuntos disjuntos

Si dos conjuntos no comparten elementos se dicen disjuntos. Podemos usar el método _isdisjoint()_ para comprobar si dos conjuntos son disjuntos.

```py
# Sintaxis
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # Falso
```

**Ejemplo:**

```py
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # Verdadero, porque no comparten elementos

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python.isdisjoint(dragon)  # Falso, comparten {'o', 'n'}
```

🌕 Eres una estrella en ascenso. Acabas de completar el desafío del día 7. Ahora realiza algunos ejercicios para practicar.

## 💻 Ejercicios - Día 7

```py
# Conjuntos
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Ejercicios: Nivel 1

1. Encuentra la longitud del conjunto `it_companies`
2. Agrega 'Twitter' a `it_companies`
3. Inserta varias empresas IT a `it_companies` de una sola vez
4. Elimina una empresa de `it_companies`
5. ¿Cuál es la diferencia entre `remove()` y `discard()`?

### Ejercicios: Nivel 2

1. Concatena A y B
2. Encuentra la intersección entre A y B
3. ¿Es A un subconjunto de B?
4. ¿Son A y B conjuntos disjuntos?
5. Combina A con B y viceversa
6. ¿Cuál es la diferencia simétrica entre A y B?
7. Elimina un conjunto por completo

### Ejercicios: Nivel 3

1. Convierte la lista de edades a un conjunto y compara la longitud de la lista y la del conjunto: ¿cuál es mayor?
2. Explica la diferencia entre estos tipos de datos: cadena, lista, tupla y conjunto
3. Para la frase _"Soy profesor, me gusta motivar y enseñar a las personas."_ ¿cuántas palabras únicas tiene? Usa `split()` y conjuntos para obtener las palabras únicas.

🎉 ¡Felicidades! 🎉

[<< Día 6](./06_tuples_sp.md) | [Día 8 >>](./08_dictionaries_sp.md)

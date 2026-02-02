# 30 Días de Python: Día 21 - Clases y Objetos

- [Día 21](#-día-21)
  - [Clases y objetos](#clases-y-objetos)
    - [Crear una clase](#crear-una-clase)
    - [Crear un objeto](#crear-un-objeto)
    - [Constructor de clase](#constructor-de-clase)
    - [Métodos de instancia](#métodos-de-instancia)
    - [Valores por defecto de los objetos](#valores-por-defecto-de-los-objetos)
    - [Modificar valores por defecto de la clase](#modificar-valores-por-defecto-de-la-clase)
    - [Herencia](#herencia)
    - [Sobrescribir métodos de la clase padre](#sobrescribir-métodos-de-la-clase-padre)
  - [💻 Ejercicios: Día 21](#-ejercicios-día-21)
    - [Ejercicios: Nivel 1](#ejercicios-nivel-1)
    - [Ejercicios: Nivel 2](#ejercicios-nivel-2)
    - [Ejercicios: Nivel 3](#ejercicios-nivel-3)

# 📘 Día 21

## Clases y objetos

Python es un lenguaje orientado a objetos. En Python todo es un objeto con atributos y métodos. Los números, cadenas, listas, diccionarios, tuplas, conjuntos, etc. que usamos en programas son instancias de las clases incorporadas correspondientes. Creamos clases para definir objetos. Una clase es como un constructor de objetos o un "molde" para crear objetos. Instanciamos una clase para crear un objeto. La clase define las propiedades y el comportamiento, mientras que el objeto representa la instancia.

Desde el inicio de este reto hemos estado usando clases y objetos sin darnos cuenta. Cada elemento en un programa Python es un objeto perteneciente a alguna clase. Veamos que todo en Python pertenece a una clase:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### Crear una clase

Para crear una clase usamos la palabra clave class seguida del nombre de la clase y dos puntos. El nombre de la clase debe usar CamelCase.

```sh
# sintaxis
class NombreClase:
    # código aquí
```

**Ejemplo:**

```py
class Person:
    pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### Crear un objeto

Creamos un objeto llamando a la clase:

```py
p = Person()
print(p)
```

### Constructor de clase

En el ejemplo anterior creamos un objeto de la clase Person. Sin embargo, una clase sin constructor no es muy útil en la práctica. Usamos el método especial __init__ como constructor en Python. __init__ recibe self, que es la referencia a la instancia actual.

**Ejemplo:**

```py
class Person:
    def __init__(self, name):
        # self permite ligar parámetros a la instancia
        self.name = name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# salida
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

Añadamos más parámetros al constructor:

```py
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# salida
Asabeneh
Yetayeh
250
Finland
Helsinki
```

### Métodos de instancia

Un objeto puede tener métodos, que son funciones pertenecientes a esa instancia.

**Ejemplo:**

```py
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} años. Vive en {self.city}, {self.country}.'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# salida
Asabeneh Yetayeh tiene 250 años. Vive en Helsinki, Finland.
```

### Valores por defecto de los objetos

A veces queremos proporcionar valores por defecto a los parámetros del constructor para evitar errores cuando la clase se instancia sin argumentos.

**Ejemplo:**

```py
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} años. Vive en {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# salida
Asabeneh Yetayeh tiene 250 años. Vive en Helsinki, Finland.
John Doe tiene 30 años. Vive en Noman city, Nomanland.
```

### Modificar valores por defecto de la clase

En el siguiente ejemplo todos los parámetros del constructor tienen valores por defecto y añadimos un atributo skills y un método add_skill para añadir habilidades.

```py
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} años. Vive en {self.city}, {self.country}.'
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# salida
Asabeneh Yetayeh tiene 250 años. Vive en Helsinki, Finland.
John Doe tiene 30 años. Vive en Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### Herencia

La herencia nos permite definir una clase que hereda el comportamiento de otra, facilitando la reutilización del código.

```py
# sintaxis
class NombreSubclase(NombreSuperclase):
    # código aquí
```

Ejemplo:

```py
class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
# salida
Eyob Yetayeh tiene 30 años. Vive en Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam tiene 28 años. Vive en Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

No hemos definido nuevos métodos en Student, pero puede usar los métodos del padre Person. Student hereda el constructor __init__ y el método person_info de Person. Si queremos añadir comportamiento específico en la subclase, definimos nuevos métodos o redefinimos los existentes.

```py
class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'él' if self.gender == 'male' else 'ella'
        return f'{self.firstname} {self.lastname} tiene {self.age} años. {gender.capitalize()} vive en {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
```

```sh
# salida
Eyob Yetayeh tiene 30 años. Él vive en Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam tiene 28 años. Ella vive en Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

Podemos usar super() o el nombre de la clase padre para invocar el comportamiento del padre. En el ejemplo anterior sobrescribimos el método person_info en la subclase con una implementación distinta.

### Sobrescribir métodos de la clase padre

Como se mostró, podemos sobrescribir un método del padre definiendo en la subclase un método con el mismo nombre.

## 💻 Ejercicios: Día 21

### Ejercicios: Nivel 1

1. Python tiene un módulo llamado _statistics_ que podemos usar para calcular estadísticas. Ahora intentemos desarrollar una clase que calcule count, sum, min, max, range, mean, median, mode, standard deviation, variance, frequency distribution y describe.

```py
class Statistics:
    def __init__(self, data=[]):
        self.data = data

    def count(self):
        # tu propia implementación
        pass

    def sum(self):
        # tu propia implementación
        pass

    def min(self):
        # tu propia implementación
        pass

    def max(self):
        # tu propia implementación
        pass

    def range(self):
        # tu propia implementación
        pass

    def mean(self):
        # tu propia implementación
        pass

    def median(self):
        # tu propia implementación
        pass

    def mode(self):
        # tu propia implementación
        pass

    def standard_deviation(self):
        # tu propia implementación
        pass

    def variance(self):
        # tu propia implementación
        pass

    def frequency_distribution(self):
        # tu propia implementación
        pass

    def describe(self):
        # tu propia implementación
        pass
```

```py
# código de prueba
data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
statistics = Statistics(data)
print('Count:', statistics.count()) # 25
print('Sum: ', statistics.sum()) # 730
print('Min: ', statistics.min()) # 24
print('Max: ', statistics.max()) # 38
print('Range: ', statistics.range()) # 14
print('Mean: ', statistics.mean()) # 29.2
print('Median: ', statistics.median()) # 27
print('Mode: ', statistics.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', statistics.standard_deviation()) # 4.2
print('Variance: ', statistics.variance()) # 17.5
print('Frequency Distribution: ', statistics.frequency_distribution()) # [(24, 2), (25, 1), (26, 5), (27, 4), (29, 1), (31, 2), (32, 3), (33, 2), (34, 2), (37, 2), (38, 1)]
```

### Ejercicios: Nivel 2

1. Crea una clase llamada PersonAccount. Debe tener firstname, lastname, incomes, expenses como atributos y métodos para añadir ingresos, añadir gastos y calcular el balance.

### Ejercicios: Nivel 3

1. El siguiente código es una función; conviértelo en una clase con comportamiento equivalente.

```python
def print_products(*args, **kwargs):
    for product in args:
        print(product)
    print(kwargs)
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

print_products("apple", "banana", "orange", vegetable="tomato", juice="orange")
```

```sh
apple
banana
orange
{'vegetable': 'tomato', 'juice': 'orange'}
vegetable: tomato
juice: orange
```

2. En la clase PersonAccount diseña atributos firstname, lastname, incomes y expenses y añade métodos para calcular el ingreso neto de la persona.

🎉 ¡Felicidades! 🎉

[<< Día 20](./20_python_package_manager_sp.md) | [Día 22 >>](./22_web_scraping_sp.md)
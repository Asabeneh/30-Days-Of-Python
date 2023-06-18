empty_list = list() # пустой список, в котором нет элементов
print(len(empty_list)) # 0

fruits = ['banana', 'orange', 'mango', 'lemon']                     # сисок фруктов
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # список овощей
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # список продуктов животного происхождения
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # список веб-технологий
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Выводит список и его длину
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Number of countries:', len(countries))

# Элементы списка по индексу

fruits = ['banana', 'orange', 'mango', 'lemon'] 
first_fruit = fruits[0] # получаем доступ к первому элементу, используя его индексу
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# последний индекс
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Доступ к элементам по отрицательному индексу
fruits = ['banana', 'orange', 'mango', 'lemon'] 
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Срезы элементов
fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[0:4] # вернет список всех фруктов
all_fruits = fruits[0:] # если не указать аргумент stop, то по умолчанию stop=lent(list)
orange_and_mango = fruits[1:3] # не вкулючает последний индекс
orange_mango_lemon = fruits[1:]

fruits = ['banana', 'orange', 'mango', 'lemon'] 
all_fruits = fruits[-4:] # вернет сисок всех фруктов
orange_and_mango = fruits[-3:-1] # вернет список без последнего элемента
orange_mango_lemon = fruits[-3:] # вернет список без первого элемента


fruits = ['banana', 'orange', 'mango', 'lemon'] 
fruits[0] = 'Avocado' 
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']

# Проверка на вхождение
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Добавление
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime]
print(fruits)

# Вставка
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # вставляет apple между orange и  mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'mango', 'lime','lemon',]
print(fruits)

# Удаление
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango']

# pop
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()     
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)     
print(fruits)       # ['orange', 'mango'] 

# del 
fruits = ['banana', 'orange', 'mango', 'lemon']
del fruits[0]     
print(fruits)       # ['orange', 'mango', 'lemon']

del fruits[1]     
print(fruits)       # ['orange', 'lemon']
del fruits
print(fruits)       # Выдаст ошибку: NameError: name 'fruits' is not defined

# Очистка
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()     
print(fruits)       # []

# Копирование списка

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()     
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# Соединение оператором (+)
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )

# Соединение методом extend
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'] 
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )

# Нахождение кол-ва вхождений
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# Нахождение индекса
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) 
# Разоворот списка
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) 

# Сортировка списка
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) 
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) 
ages.sort(reverse=True)
print(ages) 

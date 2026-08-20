empty_list = list()    # bo'sh ro'yxat, ichida hech narsa yo'q
print(len(empty_list))  # 0

# mevalar ro'yxati
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage',
              'Onion', 'Carrot']      # sabzavotlar ro'yxati
animal_products = ['milk', 'meat', 'butter',
                    'yoghurt']             # hayvon mahsulotlari ro'yxati
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB']  # veb-texnologiyalar ro'yxati
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Ro'yxatlarni va ularning uzunligini chiqarish
print('Mevalar:', fruits)
print('Mevalar soni:', len(fruits))
print('Sabzavotlar:', vegetables)
print('Sabzavotlar soni:', len(vegetables))
print('Hayvon mahsulotlari:', animal_products)
print('Hayvon mahsulotlari soni:', len(animal_products))
print('Veb-texnologiyalar:', web_techs)
print('Veb-texnologiyalar soni:', len(web_techs))
print('Davlatlar soni:', len(countries))

# Ro'yxat elementlariga indeks orqali murojaat

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]  # birinchi elementga indeks orqali murojaat
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit)  # lemon
# Oxirgi indeks
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)  # lemon

# Manfiy indeks orqali murojaat
fruits = ['banana', 'orange', 'mango', 'lemon']
last_fruit = fruits[-1]
second_last = fruits[-2]
print(last_fruit)       # lemon
print(second_last)      # mango

# Slicing (bo'lakka kesish)
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4]  # barcha mevalarni qaytaradi
# bu ham yuqoridagi bilan bir xil natija beradi
all_fruits = fruits[0:]  # tugash nuqtasini ko'rsatmasak, qolganini oladi
orange_and_mango = fruits[1:3]  # oxirgi indeks kirmaydi
orange_mango_lemon = fruits[1:]
print(orange_and_mango)
print(orange_mango_lemon)

fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:]  # barcha mevalarni qaytaradi
orange_and_mango = fruits[-3:-1]  # oxirgi indeks kirmaydi
orange_mango_lemon = fruits[-3:]
print(orange_and_mango)
print(orange_mango_lemon)

# Ro'yxatni o'zgartirish
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)  # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)  # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)  # ['avocado', 'apple', 'mango', 'lime']

# Elementni tekshirish
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

# Append — oxiriga element qo'shish
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']

# Insert — ma'lum indeksga element qo'shish
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple')  # 'orange' va 'mango' orasiga 'apple' qo'shiladi
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')
print(fruits)           # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']

# Remove — qiymati bo'yicha o'chirish
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')  # faqat birinchi uchragan 'banana' o'chadi
print(fruits)  # ['orange', 'mango', 'lemon', 'banana']
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']

# Pop — indeks bo'yicha o'chirish (yoki indekssiz, oxirgisini)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']

# Del — indeks bo'yicha yoki butun ro'yxatni o'chirish
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # ko'rsatilgan indekslar oralig'idagilarni o'chiradi
print(fruits)       # ['orange', 'lime']

# Clear — barcha elementlarni o'chirish
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

# Ro'yxatdan nusxa olish
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']

# Birlashtirish — + operatori orqali
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# Birlashtirish — extend() metodi orqali
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print('Sonlar:', num1)
negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Butun sonlar:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Mevalar va sabzavotlar:', fruits)

# Count — necha marta uchraganini sanash
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3

# Index — elementning indeksini topish
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, birinchi marta uchragan joyi

# Reverse — tartibni teskari aylantirish
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)  # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages)  # [24, 25, 24, 26, 25, 24, 19, 22]

# Sort — saralash
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)              # alfavit tartibida saralanadi
fruits.sort(reverse=True)
print(fruits)               # kamayish tartibida
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

# ប្រតិបត្តិការនព្វន្ធ ក្នុង Python
# ចំនួនគត់

print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # ការចែកក្នុង Python នឹងទទួលបានចំនួនទសភាគ
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # ការចែក ទទួលបានចំនួនគត់
print('Modulus: ', 3 % 2)                           # ការរកសំណល់
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # មានន័យថា 3 * 3

# ចំនួនទសភាគ
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# ចំនួនកំផ្លិច
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# បង្កើតអថេរនៅខាងលើមុន

a = 3 # a ជាឈ្មោះអថេរ និង 3 ជាចំនួនគត់
b = 2 # b ជាឈ្មោះអថេរ និង 2 ជាចំនួនគត់

# ប្រតិបត្តិការនព្វន្ធ និង ការដាក់ចម្លើយនៅក្នុងអថេរ
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# បង្កើតអថេរនិងតម្លៃ 2 ហើយរៀបវាជាមួយគ្នា
num_one = 3
num_two = 4

# ប្រតិបត្តិការនព្វន្ធ
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# បង្ហាញចម្លើយជាមួយឈ្មោះរបស់វា
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# ការគណនាផ្ទៃក្រឡារង្វង់
radius = 10                                 # កាំនៃរង្វង់
area_of_circle = 3.14 * radius ** 2         # ** មានន័យថាស្វាយគុណ
print('Area of a circle:', area_of_circle)

# ការគណនាផ្ទៃក្រឡានៃចតុកោណកែង
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# ការគណនាទម្ងន់នៃវត្ថុមួយ។
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

# True = ពិត , False = មិនពិត
print(3 > 2)     # True, ដោយសារតែ 3 គឺធំជាង 2
print(3 >= 2)    # True, ដោយសារតែ 3 គឺធំជាង 2
print(3 < 2)     # False,  ដោយសារតែ 3 គឺធំជាង 2
print(2 < 3)     # True, ដោយសារតែ 2 គឺតិចជាង 3
print(2 <= 3)    # True, ដោយសារតែ 2 iគឺតិចជាង 3
print(3 == 2)    # False, ដោយសារតែ 3 មិនស្មើនឹង 2
print(3 != 2)    # True, ដោយសារតែ 3 មិនស្មើនឹង 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# ការប្រៀបធៀបជាមួយសញ្ញា​ប្រមាណ
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# វិធីមួយទៀត
print('1 is 1', 1 is 1)                   # True - ដោយសារតែ តម្លៃដូចគ្នា
print('1 is not 2', 1 is not 2)           # True - ដោយសារតែ 1 មិនមែន 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A មាននៅក្នុងក្រុមអក្សរ
print('B in Asabeneh', 'B' in 'Asabeneh') # False - គ្មានអក្សរ B
print('coding' in 'coding for all') # True - ដោយសារតែ "coding for all" មានពាក្យ "coding"
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - ដោយសារតែ សេចក្តីទាំងពីរគឺពិត
print(3 > 2 and 4 < 3) # False - ដោយសារតែ សេចក្តីទី 2 មិនពិត
print(3 < 2 and 4 < 3) # False - ដោយសារតែ សេចក្តីទាំងពីរគឺមិនពិត
print(3 > 2 or 4 > 3)  # True - ដោយសារតែ សេចក្តីទាំងពីរគឺពិត
print(3 > 2 or 4 < 3)  # True - ដោយសារតែ សេចក្តីមួយគឺពិត
print(3 < 2 or 4 < 3)  # False - ដោយសារតែ សេចក្តីទាំងពីរគឺមិនពិត
print(not 3 > 2)     # False - ដោយសារតែ 3 > 2 គឺពិត, ហើយ not True បាន False
print(not True)      # False - ការបដិសេធ, ប្រតិបត្តិ not ទទួលបាន true ទៅ false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
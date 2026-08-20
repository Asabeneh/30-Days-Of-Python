# Python'da arifmetik amallar
# Butun sonlar

print('Qo\'shish: ', 1 + 2)
print('Ayirish: ', 2 - 1)
print('Ko\'paytirish: ', 2 * 3)
# Python'da bo'lish doim float (kasr son) qaytaradi
print('Bo\'lish: ', 4 / 2)
print('Bo\'lish: ', 6 / 2)
print('Bo\'lish: ', 7 / 2)
# qoldiqsiz, faqat butun qismini beradi
print('Qoldiqsiz bo\'lish: ', 7 // 2)
print('Modul: ', 3 % 2)                           # qoldiqni qaytaradi
print('Qoldiqsiz bo\'lish: ', 7 // 3)
print('Daraja: ', 3 ** 2)                          # bu 3 * 3 degani

# Kasr sonlar
print('Kasr son, PI', 3.14)
print('Kasr son, tortilish kuchi', 9.81)

# Kompleks sonlar
print('Kompleks son: ', 1+1j)
print('Kompleks sonlarni ko\'paytirish: ', (1+1j) * (1-1j))

# Avval o'zgaruvchini e'lon qilamiz

a = 3  # a — o'zgaruvchi nomi, 3 — integer qiymat
b = 2  # b — o'zgaruvchi nomi, 2 — integer qiymat

# Arifmetik amallar va natijani o'zgaruvchiga yozish
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# total deb nomlash kerak edi, chunki sum() — ichki funksiya, uni qayta yozib bo'lmaydi
print(total)  # qatorga izoh qo'ymasangiz, natija qayerdan kelganini bilmay qolasiz
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Qiymatlarni e'lon qilib, birga guruhlaymiz
num_one = 3
num_two = 4

# Arifmetik amallar
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Natijalarni izoh bilan chiqarish
print('jami: ', total)
print('ayirma: ', diff)
print('ko\'paytma: ', product)
print('bo\'linma: ', div)
print('qoldiq: ', remainder)


# Doira yuzini hisoblash
radius = 10                                 # doira radiusi
# ikkita * belgisi daraja (kvadratga oshirish) degani
area_of_circle = 3.14 * radius ** 2
print('Doira yuzi:', area_of_circle)

# To'rtburchak yuzini hisoblash
length = 10
width = 20
area_of_rectangle = length * width
print('To\'rtburchak yuzi:', area_of_rectangle)

# Jismning og'irligini hisoblash
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, chunki 3 dan 2 katta
print(3 >= 2)    # True
print(3 < 2)     # False
print(2 < 3)     # True
print(2 <= 3)    # True
print(3 == 2)    # False, chunki 3 va 2 teng emas
print(3 != 2)    # True, chunki 3 va 2 teng emas
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean taqqoslash
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Taqqoslashning yana bir usuli
# True - chunki ikkisining qiymati bir xil
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)           # True - chunki 1, 2 emas
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - 'A' satr ichida bor
print('B in Asabeneh', 'B' in 'Asabeneh')  # False - katta B yo'q
# True - chunki "coding for all" ichida "coding" so'zi bor
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3)  # True - ikkisi ham rost
print(3 > 2 and 4 < 3)  # False - ikkinchisi yolg'on
print(3 < 2 and 4 < 3)  # False - ikkisi ham yolg'on
print(3 > 2 or 4 > 3)  # True - ikkisi ham rost
print(3 > 2 or 4 < 3)  # True - bittasi rost bo'lsa kifoya
print(3 < 2 or 4 < 3)  # False - ikkisi ham yolg'on
print(not 3 > 2)     # False - 3 > 2 rost, not uni False qiladi
print(not True)      # False - inkor, not true'ni false'ga aylantiradi
print(not False)     # True
print(not not True)  # True
print(not not False)  # False

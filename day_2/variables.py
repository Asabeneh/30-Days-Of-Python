# Day 2 30 days of python programming

# Level 1

last_name = "Bérenger"
first_name = "Hto"
full_name = "Bérenger Hto"
country = "Bénin"
city = "Cotonou"
age = 19
year = 2026
is_married = False
is_true = True
is_light_on = False

# Level 2

print(type(last_name))
print(type(first_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print("Longueur de mon prénom : ", len(last_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print('5 + 4 = ', total)
print('5 - 4 = ', diff)
print('5 * 4 = ', product)
print('5 / 4 = ', division)
print('5 % 4 = ', remainder)
print('5 ^ 4 = ', exp)
print('5 // 4 = ', floor_division)

r = 30
area_of_circle = 3.14 * r ** 2
circum_of_circle = r * 2 * 3.14

print('Rayon du cercle = ', r, 'm')
print('Aire = ', area_of_circle, 'm2')
print("Périmètre = ", circum_of_circle, 'm')

last_name = input("Votre prénom : ")
first_name = input("Votre nom : ")
country = input("Votre pays : ")
age = input("Votre age : ")

print("Infos de l'utilisateur")
print("Nom", first_name)
print("Prénom", last_name)
print("Pays", country)
print("Age", age, 'ans')



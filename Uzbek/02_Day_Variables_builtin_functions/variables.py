
# Python'dagi o'zgaruvchilar
# (JS'da: let firstName = 'Asabeneh'; Python'da kalit so'zsiz, snake_case bilan)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']   # JS'dagi array kabi
person_info = {
    'firstname': 'Asabeneh',
    'lastname': 'Yetayeh',
    'country': 'Finland',
    'city': 'Helsinki'
}    # JS'dagi object kabi

# O'zgaruvchilarda saqlangan qiymatlarni chiqarish

print('Ism:', first_name)
print('Ism uzunligi:', len(first_name))      # len() -> JS'dagi .length xususiyati o'rnida
print('Familiya: ', last_name)
print('Familiya uzunligi: ', len(last_name))
print('Davlat: ', country)
print('Shahar: ', city)
print('Yosh: ', age)
print('Turmush qurgan: ', is_married)
print('Ko\'nikmalar: ', skills)
print('Shaxs haqida ma\'lumot: ', person_info)

# Bir qatorda bir necha o'zgaruvchi e'lon qilish

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsinki', 250, True

print(first_name, last_name, country, age, is_married)
print('Ism:', first_name)
print('Familiya: ', last_name)
print('Davlat: ', country)
print('Yosh: ', age)
print('Turmush qurgan: ', is_married)

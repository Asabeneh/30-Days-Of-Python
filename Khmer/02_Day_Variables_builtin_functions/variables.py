# Variable = អថេរ ឬ អថេរកូដ
# អថេរ នៅក្នុង Python

first_name = 'Hanni'
last_name = 'Pham'
country = 'Vietnam'
city = 'Hanoi'
age = 19
is_married = False
skills = ['Dancing', 'Singing', 'Variety Show', 'Modelling', 'Being a cutie']
person_info = {
    'firstname':'Hanni', 
    'lastname':'Pham', 
    'country':'Vietnam',
    'city':'Hanoi'
    }

# បង្ហាញតម្លៃ ដែកដាក់ក្នុងអថេរ ដែលយើងបានបង្កើតនៅខាងលើ

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# បង្កើតអថេរថ្មីច្រើននៅជួរតែមួយ

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
# Day 2: 30 Days of python programming

# Variables in Python

first_name = 'Tung'
last_name = 'Dao'
country = 'Vietnam'
city = 'Hanoi'
age = 25
is_married = False
skills = ['HTML', 'CSS', 'JS', 'C#', 'Python']
person_info = {
    'firstname':'Tung', 
    'lastname':'Dao', 
    'country':'VietNam',
    'city':'Hanoi'
    }

# Printing the values stored in the variables

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

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
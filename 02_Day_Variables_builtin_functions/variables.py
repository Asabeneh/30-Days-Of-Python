
# Variables in Python
# There is no need to state the data type, 
# variables can be declared with name and data in them can be stored directly.
# Pyrhon automatically recognises the data type.

# String literals in python are surrounded by either single quotation marks or double quotation marks.
first_name = 'Asabeneh'
last_name = 'Yetayeh'
acountry = "Finland"         
city = "Helsinki"

age = 250
is_married = True

# A list can be used to store multiple values
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']

# A dictionary can be used to store key-value pairs.
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
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


# Variables in Python

first_name = 'MAX'            #string
last_name = 'VERSTAPPEN'      #string 
continent = 'Europe'          #string
country = 'Netherlands'       #string
city = 'Amsterdam'            #string

age = 69                      #integer

is_married = True             #bool

skills = ['HTML', 'CSS', 'JS', 'React', 'Python','Rust']    #list of string

person_info = {
    'firstname': 'MAX',
    'lastname': 'VERSTAPPEN',
    'country': 'Netherlands',
    'city': 'Amsterdam'
}                             #dictionary

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Continent: ', cotinent)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'MAX', 'VERSTAPPEN', 'Netherlands', 69, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

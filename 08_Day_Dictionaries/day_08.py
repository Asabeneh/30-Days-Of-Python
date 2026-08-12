# =====================================================
# 30 Days Of Python - Day 8: Dictionaries (Full Code)
# =====================================================

print("===== DAY 8: DICTIONARIES =====\n")

# -----------------------------------------------------
# 1. Creating Dictionaries
# -----------------------------------------------------

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Dictionary with data
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

print("Person dictionary:", person)
print()

# -----------------------------------------------------
# 2. Dictionary Length
# -----------------------------------------------------

print("Length of person dictionary:", len(person))
print()

# -----------------------------------------------------
# 3. Accessing Dictionary Items
# -----------------------------------------------------

print("Accessing items:")
print("First name:", person['first_name'])
print("Country:", person['country'])
print("Skills:", person['skills'])
print("First skill:", person['skills'][0])
print("Street:", person['address']['street'])
print()

# Using get() method
print("Using get():")
print("City:", person.get('city'))  # None (no error)
print()

# -----------------------------------------------------
# 4. Adding Items to a Dictionary
# -----------------------------------------------------

person['job_title'] = 'Instructor'
person['skills'].append('HTML')

print("After adding job_title and skill:", person)
print()

# -----------------------------------------------------
# 5. Modifying Items in a Dictionary
# -----------------------------------------------------

person['first_name'] = 'Eyob'
person['age'] = 252

print("After modifying name and age:", person)
print()

# -----------------------------------------------------
# 6. Checking Keys in a Dictionary
# -----------------------------------------------------

print("Checking keys:")
print("'first_name' in person?", 'first_name' in person)
print("'salary' in person?", 'salary' in person)
print()

# -----------------------------------------------------
# 7. Removing Items from a Dictionary
# -----------------------------------------------------

# pop(key)
person.pop('job_title')
print("After pop('job_title'):", person)

# popitem() - removes last item
person.popitem()
print("After popitem():", person)

# del keyword
del person['is_married']
print("After deleting is_married:", person)
print()

# -----------------------------------------------------
# 8. Changing Dictionary to List of Items
# -----------------------------------------------------

items_list = person.items()
print("Dictionary items:", items_list)
print()

# -----------------------------------------------------
# 9. Clearing a Dictionary
# -----------------------------------------------------

temp_dict = {'a': 1, 'b': 2}
temp_dict.clear()
print("Cleared dictionary:", temp_dict)
print()

# -----------------------------------------------------
# 10. Copying a Dictionary
# -----------------------------------------------------

person_copy = person.copy()
print("Copied dictionary:", person_copy)
print()

# -----------------------------------------------------
# 11. Getting Keys and Values
# -----------------------------------------------------

print("Keys:", person.keys())
print("Values:", person.values())
print()

# =====================================================
# EXERCISES - DAY 8
# =====================================================

print("===== EXERCISES: DAY 8 =====\n")

# 1. Create an empty dictionary called dog
dog = {}
print("1. Dog dictionary:", dog)

# 2. Add name, color, breed, legs, age
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5
print("2. Dog after adding properties:", dog)

# 3. Create student dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'Finland',
    'city': 'Helsinki',
    'address': {
        'street': 'Main street',
        'zipcode': '00100'
    }
}
print("\n3. Student dictionary:", student)

# 4. Length of student dictionary
print("\n4. Length of student dictionary:", len(student))

# 5. Get skills value and check data type
skills = student['skills']
print("\n5. Skills:", skills)
print("   Data type of skills:", type(skills))

# 6. Modify skills
student['skills'].append('React')
student['skills'].append('Django')
print("\n6. Modified skills:", student['skills'])

# 7. Get dictionary keys as a list
keys_list = list(student.keys())
print("\n7. Keys list:", keys_list)

# 8. Get dictionary values as a list
values_list = list(student.values())
print("\n8. Values list:", values_list)

# 9. Change dictionary to list of tuples
items_tuples = list(student.items())
print("\n9. Dictionary as list of tuples:", items_tuples)

# 10. Delete one item
del student['marital_status']
print("\n10. After deleting marital_status:", student)

# 11. Delete one dictionary
del dog
print("\n11. Dog dictionary deleted")

print("\n===== END OF DAY 8 =====")
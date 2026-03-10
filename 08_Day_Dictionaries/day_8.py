# ─────────────────────────────────────────────
## 💻 Exercises: Day 8
# ─────────────────────────────────────────────

# 1. Create  an empty dictionary called dog
dog = dict()
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {'name': '', 'color': '', 'breed': '', 'legs': '', 'age': ''}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
	'first_name': '', 
    'last_name': '', 
    'gender': '', 
    'age': '', 
    'marital status': '', 
    'skills': ['AWS'], 
    'country': '', 
    'city': '', 
    'address': ''
}

# 4. Get the length of the student dictionary
len_student = len(student)

# 5. Get the value of skills and check the data type, it should be a list
skills_value = student['skills']
data_type = type(student['skills'])

# 6. Modify the skills values by adding one or two skills
# 7. Get the dictionary keys as a list
# 8. Get the dictionary values as a list
# 9. Change the dictionary to a list of tuples using _items()_ method
# 10. Delete one of the items in the dictionary
# 11. Delete one of the dictionaries
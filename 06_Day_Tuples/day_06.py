# =====================================================
# 30 Days Of Python - Day 6: Tuples (Full Practice Code)
# =====================================================

print("===== DAY 6: TUPLES =====\n")

# -----------------------------------------------------
# 1. Creating Tuples
# -----------------------------------------------------

# Empty tuple
empty_tuple_1 = ()
empty_tuple_2 = tuple()

print("Empty tuples:")
print(empty_tuple_1)
print(empty_tuple_2)
print()

# Tuple with initial values
fruits = ('banana', 'orange', 'mango', 'lemon')
print("Fruits tuple:", fruits)
print()

# -----------------------------------------------------
# 2. Tuple Length
# -----------------------------------------------------

print("Length of fruits tuple:", len(fruits))
print()

# -----------------------------------------------------
# 3. Accessing Tuple Items
# -----------------------------------------------------

# Positive indexing
first_fruit = fruits[0]
second_fruit = fruits[1]
last_fruit = fruits[len(fruits) - 1]

print("Positive indexing:")
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Last fruit:", last_fruit)
print()

# Negative indexing
print("Negative indexing:")
print("First fruit:", fruits[-4])
print("Second fruit:", fruits[-3])
print("Last fruit:", fruits[-1])
print()

# -----------------------------------------------------
# 4. Slicing Tuples
# -----------------------------------------------------

# Positive slicing
print("Positive slicing:")
print("All fruits:", fruits[0:])
print("Middle fruits:", fruits[1:3])
print("From index 1 to end:", fruits[1:])
print()

# Negative slicing
print("Negative slicing:")
print("All fruits:", fruits[-4:])
print("Middle fruits:", fruits[-3:-1])
print("From -3 to end:", fruits[-3:])
print()

# -----------------------------------------------------
# 5. Changing Tuples to Lists
# -----------------------------------------------------

print("Changing tuple to list to modify it:")

fruits_list = list(fruits)
fruits_list[0] = 'apple'
print("Modified list:", fruits_list)

fruits = tuple(fruits_list)
print("Converted back to tuple:", fruits)
print()

# -----------------------------------------------------
# 6. Checking an Item in a Tuple
# -----------------------------------------------------

print("Checking items in tuple:")
print("'orange' in fruits:", 'orange' in fruits)
print("'banana' in fruits:", 'banana' in fruits)
print("'grape' in fruits:", 'grape' in fruits)
print()

# -----------------------------------------------------
# 7. Joining Tuples
# -----------------------------------------------------

vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables

print("Joined tuples:")
print(fruits_and_vegetables)
print()

# -----------------------------------------------------
# 8. Deleting Tuples
# -----------------------------------------------------

temp_tuple = ('item1', 'item2', 'item3')
del temp_tuple
print("Tuple deleted successfully\n")

# =====================================================
# EXERCISES - LEVEL 1
# =====================================================

print("===== EXERCISES: LEVEL 1 =====\n")

# 1. Create an empty tuple
empty_tuple = ()
print("1. Empty tuple:", empty_tuple)

# 2. Create sisters and brothers tuples
sisters = ('Anna', 'Beth')
brothers = ('John', 'Mike')

print("2. Sisters:", sisters)
print("   Brothers:", brothers)

# 3. Join siblings
siblings = sisters + brothers
print("3. Siblings:", siblings)

# 4. Number of siblings
print("4. Number of siblings:", len(siblings))

# 5. Add parents to family_members
family_members = siblings + ('Father', 'Mother')
print("5. Family members:", family_members)
print()

# =====================================================
# EXERCISES - LEVEL 2
# =====================================================

print("===== EXERCISES: LEVEL 2 =====\n")

# 1. Unpack siblings and parents
*siblings_only, father, mother = family_members

print("1. Unpacked:")
print("   Siblings:", siblings_only)
print("   Father:", father)
print("   Mother:", mother)
print()

# 2. Create food tuples
fruits_tp = ('banana', 'orange', 'mango')
vegetables_tp = ('carrot', 'potato', 'onion')
animal_products_tp = ('milk', 'meat', 'butter')

food_stuff_tp = fruits_tp + vegetables_tp + animal_products_tp
print("2. Food stuff tuple:", food_stuff_tp)
print()

# 3. Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print("3. Food stuff list:", food_stuff_lt)
print()

# 4. Slice middle item(s)
middle_index = len(food_stuff_lt) // 2

if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1: middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index]

print("4. Middle item(s):", middle_items)
print()

# 5. Slice first three and last three items
print("5. First three items:", food_stuff_lt[:3])
print("   Last three items:", food_stuff_lt[-3:])
print()

# 6. Delete food_stuff_tp
del food_stuff_tp
print("6. food_stuff_tp tuple deleted")
print()

# 7. Check nordic countries
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("7. Nordic country checks:")
print("   Is 'Estonia' a nordic country?", 'Estonia' in nordic_countries)
print("   Is 'Iceland' a nordic country?", 'Iceland' in nordic_countries)

print("\n===== END OF DAY 6 =====")
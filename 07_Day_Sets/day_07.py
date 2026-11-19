# =====================================================
# 30 Days Of Python - Day 7: Sets (Full Practice Code)
# =====================================================

print("===== DAY 7: SETS =====\n")

# -----------------------------------------------------
# 1. Creating Sets
# -----------------------------------------------------

# Empty set
empty_set = set()
print("Empty set:", empty_set)

# Set with initial values
fruits = {'banana', 'orange', 'mango', 'lemon'}
print("Fruits set:", fruits)
print()

# -----------------------------------------------------
# 2. Getting Set Length
# -----------------------------------------------------

print("Length of fruits set:", len(fruits))
print()

# -----------------------------------------------------
# 3. Checking Items in a Set
# -----------------------------------------------------

print("Checking items:")
print("Is 'mango' in fruits?", 'mango' in fruits)
print("Is 'apple' in fruits?", 'apple' in fruits)
print()

# -----------------------------------------------------
# 4. Adding Items to a Set
# -----------------------------------------------------

# Add one item
fruits.add('lime')
print("After adding lime:", fruits)

# Add multiple items
vegetables = ('tomato', 'potato', 'cabbage', 'onion', 'carrot')
fruits.update(vegetables)
print("After updating with vegetables:", fruits)
print()

# -----------------------------------------------------
# 5. Removing Items from a Set
# -----------------------------------------------------

# Remove an item
fruits.remove('banana')
print("After removing banana:", fruits)

# Discard (no error if item doesn't exist)
fruits.discard('grape')
print("After discarding grape (no error):", fruits)

# Pop random item
removed_item = fruits.pop()
print("Randomly removed item:", removed_item)
print("Set after pop:", fruits)
print()

# -----------------------------------------------------
# 6. Clearing and Deleting Sets
# -----------------------------------------------------

temp_set = {'a', 'b', 'c'}
temp_set.clear()
print("Cleared set:", temp_set)

temp_set2 = {'x', 'y', 'z'}
del temp_set2
print("temp_set2 deleted\n")

# -----------------------------------------------------
# 7. Converting List to Set
# -----------------------------------------------------

fruit_list = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruit_set = set(fruit_list)
print("List:", fruit_list)
print("Converted to set (unique items):", fruit_set)
print()

# -----------------------------------------------------
# 8. Joining Sets (Union & Update)
# -----------------------------------------------------

set_a = {1, 2, 3}
set_b = {4, 5, 6}

union_set = set_a.union(set_b)
print("Union using union():", union_set)
print("Union using | :", set_a | set_b)

set_a.update(set_b)
print("After update:", set_a)
print()

# -----------------------------------------------------
# 9. Intersection
# -----------------------------------------------------

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print("Intersection:", whole_numbers.intersection(even_numbers))
print("Intersection using &:", whole_numbers & even_numbers)
print()

# -----------------------------------------------------
# 10. Subset and Superset
# -----------------------------------------------------

print("Is even_numbers subset of whole_numbers?",
      even_numbers.issubset(whole_numbers))

print("Is whole_numbers superset of even_numbers?",
      whole_numbers.issuperset(even_numbers))
print()

# -----------------------------------------------------
# 11. Difference
# -----------------------------------------------------

print("Difference (whole - even):",
      whole_numbers.difference(even_numbers))

python = {'p', 'y', 't', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

print("Python - Dragon:", python - dragon)
print("Dragon - Python:", dragon - python)
print()

# -----------------------------------------------------
# 12. Symmetric Difference
# -----------------------------------------------------

print("Symmetric difference:",
      python.symmetric_difference(dragon))
print("Using ^ :", python ^ dragon)
print()

# -----------------------------------------------------
# 13. Disjoint Sets
# -----------------------------------------------------

even = {0, 2, 4, 6, 8}
odd = {1, 3, 5, 7, 9}

print("Are even and odd disjoint?", even.isdisjoint(odd))
print("Are python and dragon disjoint?", python.isdisjoint(dragon))
print()

# =====================================================
# EXERCISES - LEVEL 1
# =====================================================

print("===== EXERCISES: LEVEL 1 =====\n")

it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1. Length
print("1. Number of IT companies:", len(it_companies))

# 2. Add Twitter
it_companies.add('Twitter')
print("2. After adding Twitter:", it_companies)

# 3. Add multiple companies
it_companies.update(['Tesla', 'Intel', 'Netflix'])
print("3. After adding multiple companies:", it_companies)

# 4. Remove one company
it_companies.remove('IBM')
print("4. After removing IBM:", it_companies)

# 5. Difference between remove and discard
print("\n5. Difference between remove and discard:")
print("- remove(): raises error if item not found")
print("- discard(): does NOT raise error\n")

# =====================================================
# EXERCISES - LEVEL 2
# =====================================================

print("===== EXERCISES: LEVEL 2 =====\n")

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B
print("1. A union B:", A.union(B))

# 2. Intersection
print("2. A intersection B:", A.intersection(B))

# 3. Subset
print("3. Is A subset of B?", A.issubset(B))

# 4. Disjoint
print("4. Are A and B disjoint?", A.isdisjoint(B))

# 5. Join A with B and B with A
print("5. A | B:", A | B)
print("   B | A:", B | A)

# 6. Symmetric difference
print("6. Symmetric difference:", A.symmetric_difference(B))

# 7. Delete sets
del A
del B
print("7. Sets A and B deleted\n")

# =====================================================
# EXERCISES - LEVEL 3
# =====================================================

print("===== EXERCISES: LEVEL 3 =====\n")

age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set = set(age)

# 1. Compare list and set length
print("1. Age list length:", len(age))
print("   Age set length:", len(age_set))
print("   List is bigger because it contains duplicates\n")

# 2. Data type explanation
print("2. Data types explanation:")
print("- String: ordered, immutable, text data")
print("- List: ordered, mutable, allows duplicates")
print("- Tuple: ordered, immutable, allows duplicates")
print("- Set: unordered, mutable, unique items only\n")

# 3. Unique words in sentence
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)

print("3. Sentence:", sentence)
print("   Unique words:", unique_words)
print("   Number of unique words:", len(unique_words))

print("\n===== END OF DAY 7 =====")
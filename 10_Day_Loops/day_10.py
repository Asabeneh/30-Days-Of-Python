# =====================================================
# 30 Days Of Python - Day 10: Loops (FULL SOLUTION)
# =====================================================

print("===== DAY 10: LOOPS =====\n")

# =====================================================
# WHILE LOOP
# =====================================================

print("While loop: 0 to 4")
count = 0
while count < 5:
    print(count)
    count += 1
print()

# While loop with else
print("While loop with else:")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop finished at:", count)
print()

# =====================================================
# BREAK AND CONTINUE (WHILE)
# =====================================================

print("Break example (stop at 3):")
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break
print()

print("Continue example (skip 3):")
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1
print()

# =====================================================
# FOR LOOP EXAMPLES
# =====================================================

print("For loop with list:")
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
print()

print("For loop with string:")
language = "Python"
for letter in language:
    print(letter)
print()

print("For loop with tuple:")
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
print()

print("For loop with dictionary:")
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland'
}

for key, value in person.items():
    print(key, ":", value)
print()

print("For loop with set:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple'}
for company in it_companies:
    print(company)
print()

# =====================================================
# BREAK AND CONTINUE (FOR)
# =====================================================

print("Break in for loop:")
for number in range(6):
    print(number)
    if number == 3:
        break
print()

print("Continue in for loop:")
for number in range(6):
    if number == 3:
        continue
    print(number)
print()

# =====================================================
# RANGE FUNCTION
# =====================================================

print("Range examples:")
print(list(range(11)))
print(list(range(0, 11, 2)))
print(list(range(10, -1, -1)))
print()

# =====================================================
# NESTED FOR LOOP
# =====================================================

print("Nested loop (skills):")
person = {
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
}

for skill in person['skills']:
    print(skill)
print()

# =====================================================
# FOR ELSE
# =====================================================

print("For-else example:")
for number in range(5):
    print(number)
else:
    print("Loop ended successfully")
print()

# =====================================================
# PASS
# =====================================================

print("Pass example:")
for _ in range(3):
    pass
print("Pass executed without errors\n")

# =====================================================
# EXERCISES: LEVEL 1
# =====================================================

print("===== EXERCISES: LEVEL 1 =====\n")

# 1. 0 to 10 (for & while)
print("0 to 10 using for loop:")
for i in range(11):
    print(i)

print("\n0 to 10 using while loop:")
i = 0
while i <= 10:
    print(i)
    i += 1
print()

# 2. 10 to 0 (for & while)
print("10 to 0 using for loop:")
for i in range(10, -1, -1):
    print(i)

print("\n10 to 0 using while loop:")
i = 10
while i >= 0:
    print(i)
    i -= 1
print()

# 3. Triangle pattern
print("Triangle pattern:")
for i in range(1, 8):
    print("#" * i)
print()

# 4. 8x8 grid
print("8x8 grid:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()
print()

# 5. Multiplication pattern
print("Square numbers:")
for i in range(11):
    print(f"{i} x {i} = {i*i}")
print()

# 6. Iterate list
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for lang in languages:
    print(lang)
print()

# 7. Even numbers 0–100
print("Even numbers:")
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
print()

# 8. Odd numbers 0–100
print("Odd numbers:")
for i in range(0, 101):
    if i % 2 != 0:
        print(i)
print()

# =====================================================
# EXERCISES: LEVEL 2
# =====================================================

print("===== EXERCISES: LEVEL 2 =====\n")

# 1. Sum of all numbers
total = 0
for i in range(101):
    total += i
print("The sum of all numbers is", total)
print()

# 2. Sum of evens and odds
even_sum = 0
odd_sum = 0

for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")
print()

# =====================================================
# EXERCISES: LEVEL 3
# =====================================================

print("===== EXERCISES: LEVEL 3 =====\n")

# 1. Countries containing 'land'
countries = [
    'Finland', 'Iceland', 'Thailand', 'Poland',
    'Switzerland', 'Canada', 'Ireland'
]

print("Countries containing 'land':")
for country in countries:
    if 'land' in country.lower():
        print(country)
print()

# 2. Reverse fruits using loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Reversed fruits:", reversed_fruits)
print()

# 3. Countries data (simplified version)
countries_data = [
    {'name': 'China', 'population': 1444216107, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1393409038, 'languages': ['Hindi', 'English']},
    {'name': 'USA', 'population': 331893745, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 276361783, 'languages': ['Indonesian']},
    {'name': 'Pakistan', 'population': 225199937, 'languages': ['Urdu', 'English']}
]

# Total number of languages
languages = set()
for country in countries_data:
    for lang in country['languages']:
        languages.add(lang)

print("Total number of languages:", len(languages))

# 10 most populated countries (here limited sample)
countries_data.sort(key=lambda x: x['population'], reverse=True)

print("\nMost populated countries:")
for country in countries_data[:10]:
    print(country['name'], "-", country['population'])

print("\n===== END OF DAY 10 =====")
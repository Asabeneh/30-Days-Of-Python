## 💻 Exercises: Day 7

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# ---------------------
### Exercises: Level 1
# ---------------------
# 1. Find the length of the set it_companies
length = len(it_companies)

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Twitter', 'Instagram'])

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Instagram')

# 5. What is the difference between remove and discard
it_companies.remove('HP')
#--- If the item to remove does not exist, remove() will raise an error.
it_companies.discard('HP')
#--- If the item to remove does not exist, discard() will NOT raise an error.

# ---------------------
### Exercises: Level 2
# ---------------------
# 1. Join A and B
# 2. Find A intersection B
# 3. Is A subset of B
# 4. Are A and B disjoint sets
# 5. Join A with B and B with A
# 6. What is the symmetric difference between A and B
# 7. Delete the sets completely

# ---------------------
### Exercises: Level 3
# ---------------------
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# 2. Explain the difference between the following data types: string, list, tuple and set
# 3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
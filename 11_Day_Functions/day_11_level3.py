# ─────────────────────────────────────────────
## 💻 Exercises: Day 11
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 3
# ─────────────────────────────────────────────

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    if type(number) == int:
        if number > 1:
            if number == 2:
                return f"{number} is a Prime"
            elif (number % 2) and (number % 3) and (number % 5 ) > 0:
                return f"{number} is a Prime"
            else:
                return f"{number} is not a Prime"
        else:
            return f"Only positive numbers can be Prime"
    else:
        return f"{type(number)} is not a Prime"
#print(is_prime(104728))      

# 2. Write a functions which checks if all items are unique in the list.
def unique(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for value in count.values():
        if value > 1:
            return f'Not Unique'
    return f'All items are unique'

# 3. Write a function which checks if all the items of the list are of the same data type.
def all_unique_types(nums):
    seen = type(nums[0])
    for item in nums:
        if type(item) != seen:
            return False
    return True
#print(all_unique_types([2, 4, 6, 8, 10]))

# 4. Write a function which check if provided variable is a valid python variable
def is_variable(name):
    result = f'{False} - \"{name}\" is not a valid variable name.'
    keywords = [
    "False", "None", "True", "and", "as", 
    "assert", "async", "await", "break",
    "class", "continue", "def", "del",
    "elif", "else", "except", "finally", 
    "for", "from", "global", "if", "import", 
    "in", "is", "lambda", "nonlocal", "not",
    "or", "pass", "raise", "return",
    "try", "while", "with", "yield" ]
                 
    if type(name) != str:
        return result
    elif name[0].isdigit():
        return result
    elif name in keywords:
        return result
    elif not name.replace('_', '').isalnum():
        return result
    return f'{True} - \"{name}\" is a valid variable name.'

#print(is_variable("While"))

# 5. Go to the data folder and access the countries-data.py file.
# Used AI to access the countries-data.y
import json
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "countries-data.py"
)

with open(file_path, "r", encoding="utf-8") as f:
    countries = json.load(f)

# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
def top_ten(countries):
    language_count = {}
    for country in countries:
        for lang in country["languages"]:
            if lang in language_count:
                 language_count[lang] += 1
            else:
                 language_count[lang] = 1
            
    sorted_languages = sorted(language_count.items(), key=lambda item: item[1], reverse=True)
    spoken_languages = sorted_languages[:10]
    new_list = []								# List of countries without the count
    for lang, count in spoken_languages:
        new_list.append(lang)
    return f'10 most spoken languages in the world are: {new_list}'  
# 10 most spoken languages in the world are: ['English', 'French', 'Arabic', 'Spanish', 'Portuguese', 'Russian', 'Dutch', 'German', 'Chinese', 'Serbian']

# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

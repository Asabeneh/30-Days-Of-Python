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
print(is_prime(104728))      

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
# 4. Write a function which check if provided variable is a valid python variable
# 5. Go to the data folder and access the countries-data.py file.
# - Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# - Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

## 💻 Exercises: Day 6

# ---------------------
### Exercises: Level 1
# ---------------------

# 1. Create an empty tuple
empty = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Summer",)
brothers = ("Ben", "Morty")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
num_siblings = len(siblings)   # 3

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("Rick", "Beth")

# ---------------------
# ### Exercises: Level 2
# ---------------------

# 1. Unpack siblings and parents from family_members
family_members = family_members[:3], family_members[-2:]
siblings, parents = family_members

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "peach", "tomato")
vegetables = ("carrot", "bell pepper", "potato")
animal_products = ("cheese", "beef mince", "honey")

food_stuff_tp = fruits + vegetables + animal_products

# 3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = food_stuff_tp[:4] + food_stuff_tp[-4:]

# 5. Slice out the first three items and the last three items from food_stuff_lt list
food_stuff_lt = food_stuff_lt[3:-3]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in  tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# - Check if 'Estonia' is a nordic country
estonia_check = "Estonia" in nordic_countries

# - Check if 'Iceland' is a nordic country
iceland_check = "Iceland" in nordic_countries
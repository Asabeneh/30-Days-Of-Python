# ─────────────────────────────────────────────
## 💻 Exercises: Day 11
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 1
# ─────────────────────────────────────────────
# 1. Declare a function _add_two_numbers_. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
	return num1 + num2
add_two_numbers(5, 3)

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates _area_of_circle_.
def area_of_circle(radius):
	return 3.14 * radius ** 2
area_of_circle(5)

# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
	total = 0
	for num in nums:
		if type(num) != int and type(num) != float:
			return  f"Error: '{num}' is not a number."       
		total += num
	return total
add_all_nums(4, 12, 35)

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, _convert_celsius_to-fahrenheit_.
def convert_celsius_to_fahrenheit(cel):
	f = (cel * 9/5) + 32
	return f
convert_celsius_to_fahrenheit(26)

# 5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
	autum = ["March", "April", "May"]
	winter = ["June", "July", "August"] 
	spring = ["September", "October", "November"]
	summer = ["December", "January", "February"]

	if month in autum:
		return "Autumn"
	elif month in winter:
		return "Winter"
	elif month in spring:
		return "Spring"
	elif month in summer: 
		return "Summer"
	else: 
		return "Please enter a Month of the Year"
check_season("May")

# 6. Write a function called calculate_slope which return the slope of a linear equation
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, _solve_quadratic_eqn_.
# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

# ```py
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]
# ```

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# 11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

# ```py
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

# ```

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

# ```py
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# ```

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

# ```py
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# ```

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
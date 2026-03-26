# ─────────────────────────────────────────────
## 💻 Exercises: Day 10
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 1
# ─────────────────────────────────────────────
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
count = range(11)
for i in count:
    print(i)

count = 0
while count < 11:
	print(count)
	count = count + 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
count = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in count:
	print(i)
	
count = 10
while count > -1:
	print(count)
	count = count - 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#    ```py
#      #
#      ##
#      ###
#      ####
#      #####
#      ######
#      #######
#    ```
pyramid = '#'
while len(pyramid) < 8:
	print(pyramid)
	pyramid = pyramid + '#'

# 4. Use nested loops to create the following:
#    ```sh
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    # # # # # # # #
#    ```
num = 0
hashes = '# # # # # # # #'
while True:
	print(hashes)
	num = num + 1
	if num == 9:
		break

# 5. Print the following pattern:
#    ```sh
#    0 x 0 = 0
#    1 x 1 = 1
#    2 x 2 = 4
#    3 x 3 = 9
#    4 x 4 = 16
#    5 x 5 = 25
#    6 x 6 = 36
#    7 x 7 = 49
#    8 x 8 = 64
#    9 x 9 = 81
#    10 x 10 = 100
#    ```
count = range(11)
for i in count:
    print(f'{i} x {i} = {i*i}')

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
languages = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lang in languages:
    print(lang)
	
# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
	remain = i % 2
	if remain == 0:
		print(i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
	remain = i % 2
	if remain == 1:
		print(i)
		
# ─────────────────────────────────────────────
### Exercises: Level 2
# ─────────────────────────────────────────────
# 1.  Use for loop to iterate from 0 to 100 and print the sum of all numbers.
#    ```sh
#    The sum of all numbers is 5050.
#    ```
num_sum = 0
for i in range(101):
	num_sum = num_sum + i

print(f'The sum of all numbers is {num_sum}.')

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
#     ```sh
#     The sum of all evens is 2550. And the sum of all odds is 2500.
#     ```
even_sum = 0
odd_sum = 0

for i in range(101):
	remain = i % 2
	if remain == 0:
		even_sum = even_sum + i
	elif remain == 1:
		odd_sum = odd_sum + i

print(f'The sum of all Even Numbers is: {even_sum}.')
print(f'The sum of all Odd Numbers is: {odd_sum}.')

# ─────────────────────────────────────────────
### Exercises: Level 3
# ─────────────────────────────────────────────
# 1. Go to the data folder and use the [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) file. Loop through the countries and extract all the countries containing the word _land_.
from data.countries import countries

for country in countries:
	if country.endswith('land'):
		print(country)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_list = ['banana', 'orange', 'mango', 'lemon']
reverse_list = []
start = len(fruit_list) - 1
    
for fruit in fruit_list:
	reverse_list.append(fruit_list[start])
	start = start - 1
    
print(reverse_list)

# 3. Go to the data folder and use the [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file. 
#    1. What are the total number of languages in the data
#    2. Find the ten most spoken languages from the data
#    3. Find the 10 most populated countries in the world
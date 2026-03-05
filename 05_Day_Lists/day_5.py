## 💻 Exercises: Day 5

### Exercises: Level 1

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
new_list = ["car", "bike", "horse", "space", "girl"]

# 3. Find the length of your list
print(len(new_list))

# 4. Get the first item, the middle item and the last item of the list
print(new_list[0:2:-1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_list = ["Shaun", 30, 1.78, "single", "Joburg"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using _print()_
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0:3:-1])

# 10. Print the list after modifying one of the companies
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# 11. Add an IT company to it_companies
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.insert(3, "Synthesis")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[3] = "APPLE"

# 14. Join the it_companies with a string '#;  '
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies = "#;  ".join(it_companies)

# 15. Check if a certain company exists in the it_companies list.
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
exists = "IBM" in it_companies

# 16. Sort the list using sort() method
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[3:]

# 19. Slice out the last 3 companies from the list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies[:-3]

# 20. Slice out the middle IT company or companies from the list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
new_list = it_companies[:3] + it_companies[-3:]

# 21. Remove the first IT company from the list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove("The Facebook")

# 22. Remove the middle IT company or companies from the list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove("Apple")

# 23. Remove the last IT company from the list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop()

# 24. Remove all IT companies from the list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()

# 25. Destroy the IT companies list
it_companies = ["The Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')

### Exercises: Level 2

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# - Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)

# - Add the min age and the max age again to the list
add_age = [min(ages)] + [max(ages)]
ages.extend(add_age)

# - Find the median age (one middle item or two middle items divided by two)
ages.sort()
mean = (ages[4] + ages[5]) / 2

# - Find the average age (sum of all items divided by their number )
ave = sum(ages) / len(ages)

# - Find the range of the ages (max minus min)
ages_range = max(ages) - min(ages)

# - Compare the value of (min - average) and (max - average), use abs() method
ave = sum(ages) / len(ages)
ave_min = abs(min(ages) - ave)
ave_max = abs(max(ages) - ave)

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
countries = "https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py"
a = len(countries)/2
middle_countries = [countries[int(a)], countries[int(a+1)]]

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = len(countries[:98])
second_half = len(countries[-97:])

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first, second, third, *scandic_countries = countries
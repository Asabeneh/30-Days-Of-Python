# ─────────────────────────────────────────────
## 💻 Exercises: Day 11
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 2
# ─────────────────────────────────────────────

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     The number of odds are 50.
#     The number of evens are 51.
def evens_and_odds(num):
    even = []
    odd = []
    for i in range(num+1):
        remain = i % 2
        if remain == 0:   
            even.append(i)
        elif remain == 1:
            odd.append(i)
    return f'The number of odds are: {len(odd)} \nThe number of evens are: {len(even)}'
print(evens_and_odds(100))

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    result = 1
    if n >= 0:
        for i in range(1, n+1):
            result *= i
    else:
        return f'Enter positive number'
    return result
print(factorial(6))

# 3. Call your function _is_empty_, it takes a parameter and it checks if it is empty or not
def is_empty(check):
    empty = len(check)
    if empty > 0:
        return f'Not empty'
    else:
        return f'Empty'

result = [1]

print(is_empty(result))
print(is_empty([]))
print(is_empty([1,2,3,4]))
print(is_empty(()))

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(nums):                   # Average
    mean = sum(nums)/len(nums)
    return mean

def calculate_median(nums):                 # Middle number
    mid = len(nums) % 2
    if mid == 0:
        num1 = int((len(nums)/2) - 1)
        num2 = int((len(nums)/2))
        return (nums[num1] + nums[num2])/2
    else:
        median = int(len(nums)/2)
        return nums[median]
print(calculate_median([5,1,1,2,4,3,7]))

def calculate_mode(nums):                   # Number that appears the most
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    sorted_by_key = dict(sorted(count.items()))
    nums_sorted_list = list(sorted_by_key.keys())
    return nums_sorted_list[0]
print(calculate_mode([5,1,1,2,4,3,7]))

def calculate_range(nums):
    sorted_list = sorted(nums)
    return sorted_list[-1] - sorted_list[0]
print(calculate_range([5,1,1,2,4,3,7]))

def calculate_variance(nums):
    mean = sum(nums)/len(nums)
    squared_diff = 0
    for i in nums:
         squared_diff += (i - mean) ** 2
    return squared_diff/(len(nums) - 1)

def calculate_std(nums):
    mean = sum(nums)/len(nums)
    squared_diff = 0
    for i in nums:
         squared_diff += (i - mean) ** 2
    return (squared_diff/(len(nums) - 1)) ** 0.5

# 5. Write a function called _greet_ which takes a default argument, _name_. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
#    greet()
#    "Hello, Guest!
#    greet("Alice")
#    "Hello, Alice!"
def greet(guest = "Guest"):
    print(f"Hello, {guest}")

# 6. Create a function called _show_args_ to take an arbitrary number of named arguments and print their names and values.
#    show_args(name="Alice", age=30, city="New York")
#    Received: name: Alice, age: 30, city: New York
#    show_args(name="Bob", pet="Fluffy, the bunny")
#    Received: name: Bob, pet: Fluffy, the bunny
def show_args(**args):
    print("Received:", end=" ")
    for k, v in args.items():
        print(f"{k}: {v}", end=" ")
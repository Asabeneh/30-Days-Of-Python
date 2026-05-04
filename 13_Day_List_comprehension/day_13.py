# ─────────────────────────────────────────────
## 💻 Exercises: Day 13
# ─────────────────────────────────────────────

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
below_zero =  [i for i in numbers if i <= 0]
print(below_zero)

# 2. Flatten the following list of lists of lists to a one dimensional list :

#    ```py
#    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

#    output
#    [1, 2, 3, 4, 5, 6, 7, 8, 9]
#    ```

# 3. Using list comprehension create the following list of tuples:
#    ```py
#    [(0, 1, 0, 0, 0, 0, 0),
#    (1, 1, 1, 1, 1, 1, 1),
#    (2, 1, 2, 4, 8, 16, 32),
#    (3, 1, 3, 9, 27, 81, 243),
#    (4, 1, 4, 16, 64, 256, 1024),
#    (5, 1, 5, 25, 125, 625, 3125),
#    (6, 1, 6, 36, 216, 1296, 7776),
#    (7, 1, 7, 49, 343, 2401, 16807),
#    (8, 1, 8, 64, 512, 4096, 32768),
#    (9, 1, 9, 81, 729, 6561, 59049),
#    (10, 1, 10, 100, 1000, 10000, 100000)]
#    ```
# 4. Flatten the following list to a new list:
#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
#    ```
# 5. Change the following list to a list of dictionaries:
#    ```py
#    countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#    output:
#    [{'country': 'FINLAND', 'city': 'HELSINKI'},
#    {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
#    {'country': 'NORWAY', 'city': 'OSLO'}]
#    ```
# 6. Change the following list of lists to a list of concatenated strings:
#    ```py
#    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#    output
#    ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
#    ```
# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
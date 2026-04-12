values = [10, 3.14, 1 + 3j, 'Reddy', [1, 2, 3], {'name': 'Reddy', 'age': 30}, (1, 2, 3)]

for i, val in enumerate(values, start=1):
    print(f'{i}. {type(val)}')

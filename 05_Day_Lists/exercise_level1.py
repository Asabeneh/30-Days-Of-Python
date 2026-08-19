item = ['phone', 'wallet', 'clock', 'mouse', 'keyboard']

print(len(item))
print(item[0], item[2], item[4])

mixed_data_types = ['sehyun', 23, 183, 'not marry', 'seoul']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(mixed_data_types)
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])

it_companies[1] = "samsung"
print(it_companies)
it_companies.append("hyundai")
print(it_companies)
it_companies.insert(3, "LG")
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print('LG' in it_companies)

it_companies.sort()
print(it_companies)
it_companies.sort(reverse = True)
print(it_companies)

print(it_companies[3:])
print(it_companies[:-3])

middle = len(it_companies) // 2
print(it_companies[middle])
it_companies.remove('LG')
print(it_companies)

del it_companies[0]
print(it_companies)

del it_companies[-1]
print(it_companies)

print(it_companies.clear())

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full = front_end + back_end
print(full)

full_stack = full.copy()

full_stack.extend(["Python", "SQL", "Redux"])
print(full_stack)
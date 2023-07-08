listt = []
game = ['Pubg', 'Ml','Ff','Fortnite','Gta']

print(len(game))

first_game = game[0:1]
print(" ".join(first_game))

middle_game = game[2:3]
print("Middle of the game is " , " ".join(middle_game))

last_game = game[4:5]
print("Last of the game is  " , " ".join(last_game))

mixed_data_type = ['Dito',19 , 169 , 'None' ,'Sragen']
it_companies = ['Facebook' , 'Google','Microsoft','IBM','Oracle','Amazon']
print(it_companies)

print(it_companies.count('Facebook'))

print(it_companies[0:1])
print(it_companies[2:3])
print(it_companies[5:6])

it_companies[2] = 'Netflix'
print(it_companies)

it  = 'BBM'
it_companies.append(it)
print(it_companies)

it_companies.insert(3 , it)
print(it_companies)

print(" # ".join(it_companies))


google_exists = 'Google' in it_companies
print(google_exists)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[0:3])
print(it_companies[5:8])

print(it_companies[4:5])

del it_companies[0]
print(it_companies)

del it_companies[4]
print(it_companies)

del it_companies[5]
print(it_companies)


#must be slicing 
it_companies.clear()
print(it_companies)


it_companies = ['Facebook' , 'Google','Microsoft','IBM','Oracle','Amazon']
google , fb, *other = it_companies
fb = it_companies[0]
google = it_companies[1]

print(google)
print(other)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

back_end.extend(front_end)

print(back_end)

full_stack = back_end.copy()
py = "Python"
sq = "SQL"
full_stack.append(py)
full_stack.append(sq)
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(min(ages))
print(max(ages))

med = len(ages)//2
print(ages[med])


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
total  = 0
for i in ages:
    total += i
print(total)    
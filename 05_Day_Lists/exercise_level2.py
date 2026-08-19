ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(max(ages), min(ages))
total = 0

for i in ages:
    total += i
print(total / len(ages))

avg = sum(ages) / len(ages)
print(avg)

print(round(abs(max(ages) - avg),1), round(abs(min(ages)- avg),3))
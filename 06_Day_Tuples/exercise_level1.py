family = tuple()

girl = ('은서', '혜영')
boy = ('세현', '석현')

siblings = girl + boy
print(len(siblings))

family_members = list(siblings)
family_members.extend(["아버지", "어머니"])
family_members = tuple(family_members)

print(family_members)
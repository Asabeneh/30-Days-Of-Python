empty_tuple = ()
    # or using the tuple constructor
empty_tuple = tuple()

    # syntax
tpl = ('item1', 'item2','item3')


fruits = ('banana', 'orange', 'mango', 'lemon')

kosongan = ()
brothers = ("Joko" , "Joki" , "Jono")
sisters  = ("Sika" , "Sike" , "Siki")
siblings = ("Bucciarati" ,"Bojinov")
siblings = brothers + sisters + siblings
family_members = siblings
print(family_members)

daddy,mother,broth,sist, *other  = family_members
daddy = family_members[7]
mother = family_members[6]
broth = family_members[:2]
sist = family_members[3:5]

print(sist)
print(daddy)
print(mother)
print(broth)

fruits = ("apple" , "melon")
vegetables = ("parrot" , "tomato")
animal = ("lion" , "cat")

food_stuff_tp = fruits + vegetables + animal
print(type(food_stuff_tp))

food_stuff_lt =  list(food_stuff_tp)
print(type(food_stuff_lt))

print((food_stuff_tp))


print(food_stuff_tp[3])
print(food_stuff_lt[0:3])
print(food_stuff_lt[3:7])

del food_stuff_lt

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
estcheck = 'Estonia' in nordic_countries
icecheck = 'Iceland' in nordic_countries
print(estcheck ,icecheck)
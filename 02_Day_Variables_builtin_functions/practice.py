# print (my_set)
# print ('Your first day is done, Go to sleep')
# print(type('$!$!'))
# print(type({'name':'Sai'}))
my_set = {1, 2, 3, 3, 4, 5}
my_list = list(my_set)  # Convert the set to a list
ar=my_list.reverse()  # Reverse the list in-place
a=set(ar)
print(a)

name='sai_kumar'
country='india'
print(name)
print(country)

customer_data={
    'customer_type':'Dunnapothu',
    'account':'gaddi',
    'ifsccode':'gaadam',
    'security_answer':'kudithi'
}

print(customer_data)
print("This is customer data length:",len(customer_data))
world=['love', 'despair', 'length']
print(world)
print(len(world))

print('Name:', name)
print(len)

c=18
t=150000
print('gstcalc: ', ((c/100)*t))

def add_num(x,y):
    return x+y
total=add_num(2,3)
print(total)

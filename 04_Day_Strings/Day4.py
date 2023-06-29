a = 'Dito'
b  = 'Days'
c = "Thirsty"

concate = a + b + c
print(concate)

d = 'Coding'
e = 'For'
f = 'All'
concate = d + " " + e + " " + f
print(concate)

company = "Coding For All"
print(company)

print(len(company))
print(company.upper())

print(company.lower())
print(company.capitalize() + " " + company.title() + " " + company.swapcase())

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto

cmp  = company[0:1]
print(cmp)

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty

if company.__contains__('Coding'):
    print(company)

else:
    print("not found")

print(company.replace('Coding' ,'python')) 

companies = "Python for Everyone"
print(companies.replace("Everyone","All"))

print(company.split(" "))

elite = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(elite.split(" , "))

firstConcate = concate[0:1]
print(firstConcate)

lastConcate = concate[-1]
print("Last index of the string is " , lastConcate)

ldi = len(company) -1 
lastC = company[ldi]
print(lastC)


ten = company[10]
print(ten)

companies = "Python For Everyone"
abreCompanies =  companies[::7]
print(abreCompanies)

subA = 'C'
print(company.index(subA))

subB = 'F'
print(company.index(subB))

print(company.rindex(subA))

print(company.rindex(subB))

subI = 'l'
print(company.rindex(subI))

sentences = 'You cannon end a sentence with because because because is a conjunction'
print(len(sentences))
find = 'because'
print(sentences.rindex(find))

becauseSlice = sentences[31:54:1]
print(becauseSlice)

find = 'because'
print(sentences.index(find))

print(company.startswith('Coding'))
print(company.endswith('coding'))

com ='\tCoding for all'
print(com)

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

pyLib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
results = " ".join(pyLib)
print(results)

print("I am enjoying this challenge ","\n I just wonder what is next.")
print("Name","\t Age" , "\tCountry","\tCity")
print("Dito",'\t' ,250 ," \tFinland","\tHelsinki")

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius " , radius , "is",area , " meters square")


print("8 + 6 = 14",
"8 - 6 = 2",
"\n8 * 6 = 48",
"\n8 / 6 = 1.33",
"\n8 % 6 = 2",
"\n8 // 6 = 1",
"\n8 ** 6 = 262144")


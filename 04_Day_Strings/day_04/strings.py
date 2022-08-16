# Exercises - Day 4
# 1º Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
word_1 = 'Thirty'
word_2 = 'Days'
word_3 = 'Of'
word_4 = 'Python'
print(f'{word_1} { word_2} {word_3} {word_4}')
# 2º Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word_a = 'Coding'
word_b = 'For'
word_c = 'All'
print(f'{word_a} { word_b} {word_c}.')
# 3º Declare a variable named company and assign it to an initial value "Coding For All".
named_company = "Coding For All"
# 4º Print the variable company using print().
print(named_company)
# 5º Print the length of the company string using len() method and print().
print(len(named_company))
# 6º Change all the characters to uppercase letters using upper() method.
print(named_company.upper())
# 7º Change all the characters to lowercase letters using lower() method.
print(named_company.lower())
# 8º Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(named_company.capitalize())
print(named_company.title())
print(named_company.swapcase())
# 9º Cut(slice) out the first word of Coding For All string.
named_company = "Coding For All"
print(len(named_company))
name = slice(6,14)
print(name)
# 10º Check if Coding For All string contains a word Coding using the method index, find or other methods.
named_company = "Coding For All"
print(named_company.find('Coding'))
print(named_company.index('Coding'))
# 11º Replace the word coding in the string 'Coding For All' to Python.
print(named_company.replace('Coding','Python'))
# 12º Change Python for Everyone to Python for All using the replace method or other methods.
print(named_company.replace('All','Everyone'))

# 13º Split the string 'Coding For All' using space as the separator (split()) .
# 14º "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# 15º What is the character at index 0 in the string Coding For All.
# 16º What is the last index of the string Coding For All.
# 17º What character is at index 10 in "Coding For All" string.
# 18º Create an acronym or an abbreviation for the name 'Python For Everyone'.
# 18º Create an acronym or an abbreviation for the name 'Coding For All'.
# 20º Use index to determine the position of the first occurrence of C in Coding For All.
# 21º Use index to determine the position of the first occurrence of F in Coding For All.
# 22º Use rfind to determine the position of the last occurrence of l in Coding For All People.
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# Does ''Coding For All' start with a substring Coding?
# Does 'Coding For All' end with a substring coding?
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

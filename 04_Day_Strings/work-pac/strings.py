## Day 04 Pac's work...

## 💻 Exercises - Day 4


#   1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
q1_words = ['Thirty','Days','Of','Python']
print(f"{q1_words[0]} {q1_words[1]} {q1_words[2]} {q1_words[3]}")



#   2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
q2_words = 'Coding', 'For', 'All'
q2_results = ' '.join(q2_words)
print(q2_results)


#   3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#   4. Print the variable company using _print()_.
print(company)

#   5. Print the length of the company string using _len()_ method and _print()_.
print(len(company))

#   6. Change all the characters to uppercase letters using _upper()_ method.
print(company.upper())

#   7. Change all the characters to lowercase letters using _lower()_ method.
print(company.lower())

#   8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
q8_string = 'Coding For All'
print(q8_string.capitalize())
print(q8_string.title())
print(q8_string.swapcase())

#   9. Cut(slice) out the first word of _Coding For All_ string.
q9_string = 'Coding For  All'
print(q9_string[7:])

#   10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
q10_string = 'Coding For All'
print(q10_string.find('Coding'))

#   11. Replace the word coding in the string 'Coding For All' to Python.
q11_string = 'Coding For All'
print(q11_string.replace('Coding','Python'))

#   12. Change Python for Everyone to Python for All using the replace method or other methods.
q12_string = 'Python for Everyone'
print(q12_string.replace('Everyone','All'))


#   13. Split the string 'Coding For All' using space as the separator (split()) .
q13_string = 'Coding For All'
print(q13_string.split(' '))
print(q13_string.split())


#   14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
q14_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(q14_string.split(', '))


#   15. What is the character at index 0 in the string _Coding For All_.
q15_string = 'Coding For All'
print(q15_string[0])

#   16. What is the last index of the string _Coding For All_.
q16_string = 'Coding For All'
print(q16_string[-1])

#   17. What character is at index 10 in "Coding For All" string.
q17_string = 'Coding For All'
print(q17_string[10])




#   18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
q18_string = 'Python For Everyone'
print(q18_string[0])
print(q18_string[7])
print(q18_string[11])


#   19. Create an acronym or an abbreviation for the name 'Coding For All'.
q19_string = 'Coding For All'
print(q19_string[0])
print(q19_string[7])
print(q19_string[11])

#   20. Use index to determine the position of the first occurrence of C in Coding For All.
q20_string =  "Coding For All"
print(q20_string.index('C'))

#   21. Use index to determine the position of the first occurrence of F in Coding For All.
q21_string =  "Coding For All"
print(q21_string.index('F'))


#   22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
q22_string = 'Coding For All People'
print(q22_string.rfind('l'))    


#   23. Use index or find to find the position of the first occurrence of the word 'because' in the 
#       following sentence: 'You cannot end a sentence with because because because is a conjunction'
q23_string = 'You cannot end a sentence with because because because is a conjunction'
print(q23_string.find('because'))
print(q23_string.index('because'))





#   24. Use rindex to find the position of the last occurrence of the word because in the 
#       following sentence: 'You cannot end a sentence with because because because is a conjunction'
q24_string = 'You cannot end a sentence with because because because is a conjunction'
print(q24_string.rfind('because'))


#   25. Slice out the phrase 'because because because' in the 
#   following sentence: 'You cannot end a sentence with because because because is a conjunction'
q25_string = 'You cannot end a sentence with because because because is a conjunction'

print(q25_string.replace('because',''))



#   26. Find the position of the first occurrence of the word 'because' in the 
#       following sentence: 'You cannot end a sentence with because because because is a conjunction'
q26_string = 'You cannot end a sentence with because because because is a conjunction'
print(q26_string.index('because'))


#   27. Slice out the phrase 'because because because' in the 
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
q27_string = 'You cannot end a sentence with because because because is a conjunction'

print(q27_string.replace('because because because',''))



#   28. Does 'Coding For All' start with a substring _Coding_?
q28_string = 'Coding For All'
print(q28_string.startswith('Coding'))



#   29. Does 'Coding For All' end with a substring _coding_?
q29_string = 'Coding For All'
print(q29_string.endswith('coding'))


#   30. ' Coding For All    ', remove the left and right trailing spaces in the given string.
q30_string = ' Coding For All    '
print(q30_string[1:])



#   31. Which one of the following variables return True 
#       when we use the method isidentifier():
#   - 30DaysOfPython
#   - thirty_days_of_python
q31_a = '30DaysOfPython'
q31_b = 'thirty_days_of_python'
print(q31_a.isidentifier())
print(q31_b.isidentifier())

#   32. The following list contains the names of some of python libraries: 
#       ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
#       Join the list with a hash with space string.
q32_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
q32_join = '# '.join(q32_list)
print(q32_join)


#   33. Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge. \nI just wonder what is next.")


#   34. Use a tab escape sequence to write the following lines.
q34_list=['Name', 'Age','Country', 'City', '\nAsabeneh','250','Finland','Helsinki']        
print('\t'.join(q34_list))




#   35. Use the string formatting method to display the following:

q35a = 'radius = 10'
q35b = 'area = 3.14 * radius ** 2'
q35c = 'The area of a circle with radius 10 is 314 meters square.'
print(f"{q35a} \n{q35b}\n{q35c}")




#   36. Make the following using string formatting methods:

q36_a = 8
q36_b = 6

print(f"{q36_a} + {q36_b} = {q36_a+q36_b}") 
print(f"{q36_a} * {q36_b} = {q36_a * q36_b}")
print(f"{q36_a} / {q36_b} = {q36_a / q36_b:.2f}")
print(f"{q36_a} % {q36_b} = {q36_a % q36_b}")
print(f"{q36_a} // {q36_b} = {q36_a // q36_b}")
print(f"{q36_a} ** {q36_b} = {q36_a ** q36_b}")
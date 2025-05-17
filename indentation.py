"""
Whitespace at the beginning of the line is called 'indentation'. These whitespaces or the indentation are very important in python. In a Python program,
the leading whitespace including spaces and tabs at the beginning of the logical line determines the indentation level of that logic.

* In most programming languages, indentation has no effect on progamming logic. It is used to align statements to make the code more readable.
However, in python, indentation is used to associate and group statements.

All statements within the same block must have the same indentation level. Typically, one tab or 4 spaces are used per level.

All statements inside a block should be at the same indentation level..


Below is the correct syntax for nested conditions with proper indentation:

if <condition>:
    -Statements-
    if <contion>:
        -statements-

"""
# example:
user  = int(input ("enter any digit.. "))
if user <=10:
    if user>=5: 
        print("entered number is less than 10 and greater than 5")
    else:
        print("entered number is less than 5")
else:
    print("entered number is greater than 10")
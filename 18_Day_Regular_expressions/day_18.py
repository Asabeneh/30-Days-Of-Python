import re
from collections import Counter

print("===== DAY 18: REGULAR EXPRESSIONS =====\n")

# --------------------------------------------------
# EXERCISES: LEVEL 1
# --------------------------------------------------

# 1. Most frequent word in a paragraph
paragraph = '''I love teaching. If you do not love teaching what else can you love.
I love Python if you do not love something which can give you all the capabilities
to develop an application what else can you love.'''

# extract words (ignore punctuation, case-insensitive)
words = re.findall(r'\b[a-zA-Z]+\b', paragraph)
word_counts = Counter(words)

most_common_words = word_counts.most_common()
print("LEVEL 1 - Exercise 1:")
print(most_common_words)
print()

# --------------------------------------------------

# 2. Extract numbers and find distance
text = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

numbers = re.findall(r'-?\d+', text)
numbers = list(map(int, numbers))

distance = max(numbers) - min(numbers)

print("LEVEL 1 - Exercise 2:")
print("Extracted numbers:", numbers)
print("Distance between furthest particles:", distance)
print()

# --------------------------------------------------
# EXERCISES: LEVEL 2
# --------------------------------------------------

# Valid Python variable checker
def is_valid_variable(name):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(pattern, name))

print("LEVEL 2:")
print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True
print()

# --------------------------------------------------
# EXERCISES: LEVEL 3
# --------------------------------------------------

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;
There $is nothing; &as& mo@re rewarding as educa@ting &and&
@emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting
tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Clean text
def clean_text(text):
    return re.sub(r'[^a-zA-Z\s]', '', text)

cleaned_text = clean_text(sentence)
print("LEVEL 3 - Cleaned Text:")
print(cleaned_text)
print()

# Find most frequent words
def most_frequent_words(text, n=3):
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    counts = Counter(words)
    return counts.most_common(n)

print("LEVEL 3 - Most Frequent Words:")
print(most_frequent_words(cleaned_text))

print("\n===== END OF DAY 18 =====")
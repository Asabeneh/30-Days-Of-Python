# ─────────────────────────────────────────────
## 💻 Exercises: Day 12
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 2
# ─────────────────────────────────────────────
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import string
import random

def random_user_id():
    alpha_numeric = "abcdef" + string.digits
    new = "#"
    for i in random.choices(alpha_numeric, k=6):
        new += i
    return new

print(random_user_id())
# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
# ```py
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
# ```
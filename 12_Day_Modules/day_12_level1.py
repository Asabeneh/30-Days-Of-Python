# ─────────────────────────────────────────────
## 💻 Exercises: Day 11
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 1
# ─────────────────────────────────────────────
# 1. Write a function which generates a six digit/character random_user_id. 
#    ```py
#      print(random_user_id()) 
#      '1ee33d'
#    ```
import string
from random import *
import random

def random_user_id():
    alpha_numeric = string.ascii_letters + string.digits
    new = ""
    for i in random.choices(alpha_numeric, k=6):
        new += i
    return f"\'{new}\'"

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# ```py
# print(user_id_gen_by_user()) # user input: 5 5
# output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
   
# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr
# ```
def user_id_gen_by_user():
    alpha_numeric = string.ascii_letters + string.digits
    id_chars = int(input("Enter user ID length: "))
    user_ids = int(input("Enter number of IDs: "))
    numb_of_id = []
    while user_ids > 0:
        user_ids -= 1
        new = "#"
        for i in random.choices(alpha_numeric, k=id_chars):
            new += i
        numb_of_id.append(new)
    return "\n".join(numb_of_id)

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# ```py
# print(rgb_color_gen())
#  rgb(125,244,255) - the output should be in this form
# ```
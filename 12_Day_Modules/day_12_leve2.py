# ─────────────────────────────────────────────
## 💻 Exercises: Day 12
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 2
# ─────────────────────────────────────────────
# 1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import string
import random

def list_of_hexa_colors():
    number = int(input("Number of hexa colours: "))
    hexa_colours = []
    while number > 0:
        number -= 1
        alpha_numeric = "abcdef" + string.digits
        new = "#"
        for i in random.choices(alpha_numeric, k=6):
            new += i
        hexa_colours.append(new)
    return hexa_colours

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors():
    numb = int(input("Number of RGB colours: "))
    rgb_colours = []
    while numb > 0:
        numb -= 1
        rgb = f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
        rgb_colours.append(rgb)
    return rgb_colours

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
# ```py
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
# ```
def generate_colors(kind,number: int):
    if kind == "hexa":
        hexa_colours = []
        while number > 0:
            number -= 1
            alpha_numeric = "abcdef" + string.digits
            new = "#"
            for i in random.choices(alpha_numeric, k=6):
                new += i
            hexa_colours.append(new)
        return hexa_colours
    elif kind == "rgb":
        rgb_colours = []
        while number > 0:
            number -= 1
            rgb = f"rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"
            rgb_colours.append(rgb)
        return rgb_colours
    else:
        return f"{kind} is not a valid colour type."
    
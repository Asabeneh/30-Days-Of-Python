# ─────────────────────────────────────────────
## 💻 Exercises: Day 12
# ─────────────────────────────────────────────

# ─────────────────────────────────────────────
### Exercises: Level 3
# ─────────────────────────────────────────────
# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random

def shuffle_list(lst: list) -> list:
    shuffled_list = []
    for item in lst:
        shuffled_list.append(random.choice(lst))
    return shuffled_list

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def array_of_seven() -> set[int]:
    array = set()
    while len(array) < 7:
        array.add(random.randint(0,9))
    return array

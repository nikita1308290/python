from random import random
from random import randint, choice, shuffle, choices

value = random()
print(value)
for i in range(10):
    value = randint(1,10)
    print(value, end='')

nums = []
for i in range(10):
    nums.append(randint(1, 1000))
print("\n", nums)

animals = ['🐶','🐼', '🐻', '🐘', '🐁','🐿️', '🦖','🐃', '🐑']

sel_ani = choice(animals)
print(f'selected animal: {sel_ani}')

sel_3_anim = choices(animals)
print(f'selected 3 animals: {" ".join(sel_3_anim)}')

shuffle(animals)
print(f'shuffled animals:{"".join(animals)}')
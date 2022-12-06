import copy
import re
from pprint import pprint
f = open("2022/day_5/input.txt", "r")
text = f.read()
split_text = text.split("\n\n")

# Grid
columns = split_text[0].split("\n")[0:-1]
columns_split = [[line[i:i+1] for i in range(1, len(line), 4)] for line in columns]
rotated = list(zip(*columns_split[::-1]))
rotated_clean = [[el for el in line if el != ' '] for line in rotated]
pprint(rotated_clean)


# Moves
moves = split_text[1].split("\n")[0:-1]
moves_int = []
for move_text in moves:
    move = re.findall(r'\d+', move_text)
    move = [int(a) for a in move]
    move[1] -= 1
    move[2] -= 1
    moves_int.append(move)
print(moves_int)

# Logic
def move_crate_9000(quantity, origin, destination, piles):
    for _ in range(quantity):
        popped = piles[origin].pop()
        piles[destination].append(popped)
    return piles

def move_crate_9001(quantity, origin, destination, piles):
    popped = piles[origin][-quantity:]
    piles[origin] = piles[origin][:-quantity]
    piles[destination] += popped
    return piles

def crate_mover(model, grid, moves):
    piles = copy.deepcopy(grid)
    for el in moves:
        globals()['move_crate_'+model](*el, piles)
    for pile in piles:
        print(pile[-1])

crate_mover('9000', rotated_clean, moves_int)
crate_mover('9001', rotated_clean, moves_int)
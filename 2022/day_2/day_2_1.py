f = open("day_2/input.txt", "r")
text = f.read().strip()

score_dict = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

split_text = text.split("\n")
moves = []
score = 0
for el in split_text:
    move_couple = el.split(" ")
    moves.append(move_couple)

    score += score_dict[move_couple[1]]

    if move_couple in [['A', 'Y'], ['B', 'Z'], ['C', 'X']]:
        score += 6
    if score_dict[move_couple[0]] == score_dict[move_couple[1]]:
        score += 3
print(score)

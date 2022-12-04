f = open("day_2/input.txt", "r")
text = f.read().strip()

score_dict = {
    'A': 1,
    'B': 2,
    'C': 3
}

split_text = text.split("\n")
moves = []
score = 0
for el in split_text:
    move_couple = el.split(" ")
    moves.append(move_couple)

    if move_couple[1] == 'Z':
        score += 6
        score += (score_dict[move_couple[0]] +
                  1) if score_dict[move_couple[0]] != 3 else 1
    if move_couple[1] == 'Y':
        score += 3
        score += score_dict[move_couple[0]]
    if move_couple[1] == 'X':
        score += (score_dict[move_couple[0]] -
                  1) if score_dict[move_couple[0]] != 1 else 3
print(score)

f = open("day_1/input.txt", "r")
text = f.read().strip()

split_text = text.split("\n\n")
elves_sum = []
for el in split_text:
    int_weights_list = [int(weight) for weight in el.split("\n")]
    elves_sum.append(sum(int_weights_list))
print(sorted(elves_sum)[-1])
print(sum(sorted(elves_sum)[-3:]))
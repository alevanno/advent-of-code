f = open("day_4/input.txt", "r")
text = f.read().strip()

split_text = text.split("\n")
complete_overlap_count = 0
partial_overlap_count = 0

def range_inclusive(start, end):
    return range(start, end+1)

for elf_couple in split_text:
    elf_1, elf_2 = elf_couple.split(",")
    range_1 = range_inclusive(*[int(i) for i in elf_1.split("-")])
    range_2 = range_inclusive(*[int(i) for i in elf_2.split("-")])
    contained = all(elem in range_1 for elem in range_2) | all(elem in range_2 for elem in range_1)
    if (all(elem in range_1 for elem in range_2) | all(elem in range_2 for elem in range_1)):
        complete_overlap_count += 1
    if (any(elem in range_1 for elem in range_2) | any(elem in range_2 for elem in range_1)):
        partial_overlap_count += 1

print(complete_overlap_count)
print(partial_overlap_count)

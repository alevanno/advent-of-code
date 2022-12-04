f = open("day_3/input.txt", "r")
text = f.read().strip()

import string
alphabet_list = list(string.ascii_lowercase + string.ascii_uppercase)

split_text = text.split("\n")
elf_groups = [split_text[i:i+3] for i in range(0, len(split_text), 3)]
priorities = 0

for group in elf_groups:
    (common_char,) = list(set(group[0]) & set(group[1]) & set(group[2]))
    priorities += alphabet_list.index(common_char)+1
    
print(priorities)

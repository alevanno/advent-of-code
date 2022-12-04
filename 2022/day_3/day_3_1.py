f = open("day_3/input.txt", "r")
text = f.read().strip()

import string
alphabet_list = list(string.ascii_lowercase + string.ascii_uppercase)

split_text = text.split("\n")
priorities = 0

for rucksack in split_text:
    firsthalf, secondhalf = rucksack[:len(
        rucksack)//2], rucksack[len(rucksack)//2:]
    (common_char,) = list(set(firsthalf) & set(secondhalf))
    priorities += alphabet_list.index(common_char)+1
    
print(priorities)

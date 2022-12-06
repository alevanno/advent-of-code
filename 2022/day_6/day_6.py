from collections import deque
f = open("2022/day_6/input.txt", "r")
text = f.read()

# Adjust size of the sliding window
size = 14

q = deque(maxlen=size)

for i, char in enumerate(text):
    # Check if all the elements in the sliding window are unique
    if len(set(q)) == size:
        print(i)
        break
    q.append(char)

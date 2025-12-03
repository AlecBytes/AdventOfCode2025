import re

# with open('./day1/puzzle_example.txt')  as f:
with open('./day1/puzzle.txt')  as f:
    rotations = [line.strip() for line in f]

dial = 50
zero_count = 0

for rotation in rotations:
    m = re.match(r"^(R|L)(\d+)$", rotation)
    dir, val = m.groups()

    if dir == 'L':
        dial = (dial - int(val)) % 100

    elif dir == 'R':
        dial = (dial + int(val)) % 100

    if dial == 0:
        zero_count += 1
    

print('final: ' + str(zero_count))
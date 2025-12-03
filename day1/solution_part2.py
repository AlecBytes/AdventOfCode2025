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
        sum = dial - int(val)
        if sum <= 0 and sum >= -99:
            zero_count += 1
        elif sum <= -100:
            zero_count += (abs(sum) // 100) + 1

        if dial == 0:
            zero_count -= 1
        dial = (dial - int(val)) % 100

    elif dir == 'R':
        sum = dial + int(val)
        if sum >= 100:
            zero_count += (sum // 100)

        dial = (dial + int(val)) % 100


    

print('final: ' + str(zero_count))
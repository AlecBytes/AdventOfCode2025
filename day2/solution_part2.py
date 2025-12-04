import re

with open('./day2/puzzle.txt') as f:
    ranges_str = f.read().strip().split(",")

ranges = []
for r in ranges_str:
    match = re.match(r"(\d+)-(\d+)", r)
    min, max = match.groups()
    ranges.append((int(min), int(max)))

def find_invalid_IDs(min, max):
    invalid_IDs = []
    for id in range(min, max + 1):
        if not is_ID_valid(id):
            invalid_IDs.append(id)
    return invalid_IDs

def is_ID_valid(id):
    id_str  = str(id)
    i, j = 0, 1
    while True:
        if len(id_str) % len(id_str[i:j]) == 0:
            times = len(id_str) // len(id_str[i:j])
            if times > 1 and id_str[i:j] * times == id_str:
                return False
        j += 1
        if id_str[i:j+1] == id_str:
            break
    return True

invalidIDs = []
for min, max in ranges:
    invalidIDs.extend(find_invalid_IDs(min, max))

print(sum(invalidIDs))

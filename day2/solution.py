import re

with open('./day2/puzzle.txt') as f:
    ranges_str = f.read().strip().split(",")

ranges = []
for r in ranges_str:
    match = re.match(r"(\d+)-(\d+)", r)
    min, max = match.groups()
    ranges.append((int(min), int(max)))

def is_ID_invalid(id):
    id_str = str(id)
    id_len = len(id_str)
    if id_len % 2 == 0:
        mid = id_len // 2
        left_half = id_str[:mid]
        right_half = id_str[mid:]
        if left_half == right_half:
            return True
        else:
            False
    else:
        return False

def find_invalid_IDs(min, max):
    invalid_IDs = []
    for id in range(min, max + 1):
        if is_ID_invalid(id):
            invalid_IDs.append(id)
    return invalid_IDs

invalidIDs = []
for min, max in ranges:
    invalidIDs.extend(find_invalid_IDs(min, max))

print(sum(invalidIDs))
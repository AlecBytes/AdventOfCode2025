import re

def load_input(file):
    with open(file) as f:
        ranges, ids = f.read().split("\n\n")
    id_ranges = []
    for r in ranges.splitlines():
        match = re.match(r"(\d+)-(\d+)", r)
        min, max = match.groups()
        id_ranges.append((int(min), int(max)))
    avail_ids = [int(id) for id in ids.splitlines()]
    return id_ranges, avail_ids

def is_fresh(id, ranges):
    for range in ranges:
        min, max = range
        if id >= min and id <= max:
            return True
    return False

def count_fresh_ids(ids, ranges):
    fresh_ids = []
    for id in ids:
        if is_fresh(id, ranges):
            fresh_ids.append(id)
    return len(fresh_ids)

def count_possible_fresh_ids(ranges):
    count = 0
    for r in ranges:
        min, max = r
        count += max - min + 1
    return count

def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    merged = []
    merged.append(sorted_ranges[0])
    for r in range(1, len(sorted_ranges)):
        r_min, r_max = sorted_ranges[r]
        m_min, m_max = merged[-1]
        if m_max >= r_min:
            merged[-1] = (m_min, max(m_max, r_max)) # extend last merged range
        else:
            merged.append(sorted_ranges[r])
    return merged

def solve_1(ranges, ids):
    fresh_id_count = count_fresh_ids(ids, ranges)
    print(f'solution 1\n Fresh Id count: {fresh_id_count}')

def solve_2(ranges):
    merged_ranges = merge_ranges(ranges)
    possible_fresh_count = count_possible_fresh_ids(merged_ranges)
    print(f'Solution 2\n possible fresh count: {possible_fresh_count}')


def main():
    id_ranges, avail_ids = load_input('./day5/input.txt')
    solution_1 = solve_1(id_ranges, avail_ids)
    solution_2 = solve_2(id_ranges)

if __name__ == "__main__":
    main()
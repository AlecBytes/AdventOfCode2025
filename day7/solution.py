

def load_input(file):
    with open(file) as f:
        return [list(line.strip()) for line in f.readlines()]
    
def print_grid(grid):
    print('Printing Grid:\n')
    for line in grid:
        print("".join(line))

def find_next_row_tacs(cur_row, next_row):
    split_count = 0
    cur_row_tacs = [i for i, c in enumerate(cur_row) if c == '|' or c == 'S']
    for tac_pos in cur_row_tacs:
        if next_row[tac_pos] == '.':
            next_row[tac_pos] = '|'
        elif next_row[tac_pos] == '^':
            split_count += 1
            if tac_pos >= 0:
                next_row[tac_pos - 1] = '|'
            if tac_pos < len(next_row):
                next_row[tac_pos + 1] = '|'
    return next_row, split_count

def solve_p1(grid):
    total_splits = 0
    for i in range(len(grid) - 1):
        grid[i+1], split_count = find_next_row_tacs(grid[i], grid[i+1])
        total_splits += split_count
        # print(f'Step {i}, Splits {total_splits}')
        # print_grid(grid)
    return total_splits

def solve_p2(input_path):
    empty_space = '.'
    splitter = '^'
    grid = load_input(input_path)
    rows = len(grid)
    cols = len(grid[0])

    # init dp grid
    ways_to_reach_pos = [[0] * cols for _ in range(rows)]

    start_col = grid[0].index('S')
    ways_to_reach_pos[0][start_col] = 1

    # calculate dp grid
    for r in range(rows - 1):
        for c in range(cols):
            ways = ways_to_reach_pos[r][c]
            if not ways: #pos was not reached by prev row, can skip
                continue

            down = grid[r + 1][c]
            if down == empty_space:
                ways_to_reach_pos[r + 1][c] += ways
            elif down == splitter:
                if c > 0:
                    ways_to_reach_pos[r + 1][c - 1] += ways
                if c < cols - 1:
                    ways_to_reach_pos[r + 1][c + 1] += ways
    # ways to reach each leaf = # of paths from S to any leaf
    total_timelines = sum(ways_to_reach_pos[-1]) 
    print(f"# of timelines: {total_timelines}")
    return total_timelines


def main():
    grid_example = load_input('./day7/input_example.txt')
    solution_p1_example = solve_p1(grid_example)
    print(f'\nSolution: Part 1: Example: Split Count = {solution_p1_example}')
    
    grid = load_input('./day7/input.txt')
    solution_p1 = solve_p1(grid)
    print(f'Solution: Part 1: Split Count = {solution_p1}')

    print('\nSolution: Part 2: Example:')    
    solve_p2('./day7/input_example.txt')
    print('\nSolution: Part 2:')    
    solve_p2('./day7/input.txt')


if __name__ == "__main__":
    main()
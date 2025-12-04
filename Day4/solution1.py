
def load_input(file):
    with open(file) as f:
        return [list(row.strip()) for row in f.readlines()]
    
def print_grid(grid):
    for row in grid:
        print("".join(row))
    
def is_pos_inbounds(pos, grid):
   i, j = pos
   return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

def count_adjacent_paper(pos, grid):
    i, j = pos
    count = 0
    pos_NW = (i - 1, j - 1)
    pos_N = (i - 1, j)
    pos_NE = (i - 1, j + 1)
    pos_W = (i, j - 1)
    pos_E = (i, j + 1)
    pos_SW = (i + 1, j - 1)
    pos_S = (i + 1, j)
    pos_SE = (i + 1, j + 1)
    adjacent_positions = [pos_NW, pos_N, pos_NE, pos_W, pos_E, pos_SW, pos_S, pos_SE]

    for neighbor in adjacent_positions:
        if is_pos_inbounds(neighbor, grid):
            if grid[neighbor[0]][neighbor[1]] == '@':
                count += 1

    return count

def find_accessible_paper(grid):
    count = 0
    for i, row in enumerate(grid):
        for j, pos in enumerate(row):
            if pos == '@':
                if count_adjacent_paper((i, j), grid) < 4:
                    # grid[i][j] = 'X'
                    count += 1
    return count

def main():
    print('running...')
    grid = load_input("./day4/input.txt")
    print_grid(grid)
    accessible_paper_count = find_accessible_paper(grid)
    print(accessible_paper_count)

    print(f'solution: {accessible_paper_count}')


if __name__ == "__main__":
    main()
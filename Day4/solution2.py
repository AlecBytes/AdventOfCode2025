
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
    paper_pos_to_remove = []
    for i, row in enumerate(grid):
        for j, pos in enumerate(row):
            if pos == '@':
                if count_adjacent_paper((i, j), grid) < 4:
                    count += 1
                    paper_pos_to_remove.append((i, j))
    return count, paper_pos_to_remove

def remove_paper_in_phases(grid):
    count_total = 0
    count, paper_pos_to_remove = find_accessible_paper(grid)
    while count > 0:
        count_total += count
        for pos in paper_pos_to_remove:
            grid[pos[0]][pos[1]] = 'X'
        count, paper_pos_to_remove = find_accessible_paper(grid)
    return count_total
  
def main():
    grid = load_input("./day4/input.txt")
    print_grid(grid)
    total_removed_paper =  remove_paper_in_phases(grid)
    print(f'solution: {total_removed_paper}')

if __name__ == "__main__":
    main()
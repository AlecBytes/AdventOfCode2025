def load_input(file):
    with open(file) as f:
        input = [line.split() for line in f.readlines()]
    return  input[:-1], input[-1]

def do_math(nums, ops):
    total = 0
    for column_index, op in enumerate(ops):
        sub_total = 0 if op == '+' else 1
        for row_index in range(len(nums)):
            num = int(nums[row_index][column_index])
            if op == '*':
                sub_total *= num
            elif op == '+':
                sub_total += num
            else:
                raise Exception("Operation invalid")
        print(f'col_{column_index} {sub_total} + {total} = {sub_total + total}')
        total += sub_total
    return total

def get_col_widths(op_str):
    col_widths = []
    width = 0
    for i, c in enumerate(op_str):
        if (c == '*' or c == '+'):
            if width != 0:
                col_widths.append(width)
            width = 1
        elif c == ' ':
            if i+1 < len(op_str) and op_str[i+1] == ' ' :
                width += 1
            elif i+1 == len(op_str):
                width +=1
                col_widths.append(width)
    print(col_widths)
    return col_widths

def get_op_indexes(op_str):
    return [i for i, c in enumerate(op_str) if c == '*' or c == '+']


def solve_p2(input):
    with open(input) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]
    num_lines = lines[:-1]
    op_line = lines[-1]
    col_widths = get_col_widths(op_line)
    op_indexes = get_op_indexes(op_line)
    print(op_indexes)

    chunks = []
    chunk = []
    for i, op_index in enumerate(op_indexes):
        start = op_index
        end = start + col_widths[i]
        for line in num_lines:
            chunk.append(line[start:end])
        chunks.append(chunk)
        chunk = []
    print(chunks)

    total = 0
    for i, op_index in enumerate(op_indexes):
        nums = convert_chunk_to_nums(chunks[i])
        subtotal = 0 if op_line[op_index] == '+' else 1
        for num in nums:
            if op_line[op_index] == '+':
                subtotal += num
            if op_line[op_index] == '*':
                subtotal *= num
        total += subtotal
    print(f'total: {total}')


def convert_chunk_to_nums(chunk):
    nums = []
    width = len(chunk[0])
    for i in range(width):
        num_str = ''
        for sub_chunk in chunk:
            num_str += sub_chunk[(i + 1) * -1]
        nums.append(int(num_str))
    return nums
            
def main():
    print('Solving day 6...')
    nums, ops = load_input('./day6/input.txt')
    print(f'nums: {nums}')
    print(f'ops: {ops}')

    print(f'nums len: {len(nums)}')
    print(f'ops len: {len(ops)}')

    grand_total = do_math(nums, ops)
    print(f'Part 1\nSolution: Grand Total = {grand_total}')

    print(f'Part 2 Example:')
    solve_p2('./day6/input_example.txt')

    print(f'Part 2:')
    solve_p2('./day6/input.txt')

if __name__ == "__main__":
    main()
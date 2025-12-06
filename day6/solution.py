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
            
def main():
    print('Solving day 6...')
    nums, ops = load_input('./day6/input.txt')
    print(f'nums: {nums}')
    print(f'ops: {ops}')

    print(f'nums len: {len(nums)}')
    print(f'ops len: {len(ops)}')

    grand_total = do_math(nums, ops)
    print(f'Part 1\nSolution: Grand Total = {grand_total}')

if __name__ == "__main__":
    main()
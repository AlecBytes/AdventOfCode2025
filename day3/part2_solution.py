
def load_input(file):
    with open(file) as f:
        return  [list(bank.strip()) for bank in f.readlines()]

def find_max_joltage(bank):
    first_digit = max(bank[:-1])
    first_digit_pos = bank.index(first_digit)
    second_digit = max(bank[first_digit_pos + 1:])
    return (int(str(first_digit) + str(second_digit)))

def find_max_joltage12(bank):
    digits = []
    start_index = 0 
    for i in range(12):
        end_index = -11 + i
        search_str = bank[start_index:end_index] if end_index != 0 else bank[start_index:]
        digit = max(search_str)
        start_index += search_str.index(digit) + 1
        digits.append(digit)
    return int("".join(d for d in digits))

def find_each_bank_max(banks):
    banks_joltage_maxes = []
    for bank in banks:
        banks_joltage_maxes.append(find_max_joltage12(bank))
    return banks_joltage_maxes

def main():
    banks = load_input('./day3/input.txt')
    max_joltages = find_each_bank_max(banks)
    solution = sum(max_joltages)
    print(solution)

if __name__ == "__main__":
    main()
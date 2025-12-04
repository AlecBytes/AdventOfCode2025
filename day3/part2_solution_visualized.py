import sys
import time
from colorama import Fore, Style, ansi, init

init(autoreset=True)

def load_input(file):
    with open(file) as f:
        return [list(bank.strip()) for bank in f.readlines()]

def find_max_joltage(bank):
    first_digit = max(bank[:-1])
    first_digit_pos = bank.index(first_digit)
    second_digit = max(bank[first_digit_pos + 1:])
    return int(str(first_digit) + str(second_digit))

BLUE, RED, GREEN, RESET = Fore.BLUE, Fore.RED, Fore.GREEN, Style.RESET_ALL
CLEAR = ansi.clear_screen() + ansi.Cursor.POS(1, 1)


def find_max_joltage12(bank, visualize=False, delay=1):
    digits = []
    start_index = 0
    bank_str = "".join(bank)
    for i in range(12):
        end_index = -11 + i
        search_str = bank[start_index:end_index] if end_index != 0 else bank[start_index:]
        digit = max(search_str)
        pos = start_index + search_str.index(digit)
        digits.append(digit)

        if visualize:
            left = bank_str[:start_index]
            window_before = bank_str[start_index:pos]
            chosen = bank_str[pos]
            window_after = bank_str[pos + 1 : end_index if end_index != 0 else len(bank)]
            tail = bank_str[end_index if end_index != 0 else len(bank) :]

            line = (
                left
                + BLUE
                + window_before
                + GREEN
                + chosen
                + BLUE
                + window_after
                + RESET
                + RED
                + tail
                + RESET
            )
            sys.stdout.write(CLEAR)
            sys.stdout.write(
                f"step {i+1} selected={digit} idx={pos} built={''.join(digits)}\n"
            )
            sys.stdout.write(line + "\n")
            sys.stdout.flush()
            time.sleep(delay)

        start_index += search_str.index(digit) + 1
    return int("".join(d for d in digits))


def find_each_bank_max(banks, visualize=False, delay=1):
    banks_joltage_maxes = []
    for bank in banks:
        banks_joltage_maxes.append(
            find_max_joltage12(bank, visualize=visualize, delay=delay)
        )
    return banks_joltage_maxes


def main():
    banks = load_input("./day3/input.txt")
    max_joltages = find_each_bank_max(banks, visualize=True, delay = .5)
    solution = sum(max_joltages)
    print("final sum:", solution)


if __name__ == "__main__":
    main()

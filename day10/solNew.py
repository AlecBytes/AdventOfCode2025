import re
from itertools import combinations
from dataclasses import dataclass

@dataclass
class Light:
    diagram: int
    buttons: list[int]
    jolt_req: int

    def print_light(self):
        print(f'Diagram: {bin(self.diagram)}')
        for b in self.buttons:
            print(f'{bin(b)}')

def diag_str_to_bit(diag):
    diagram = 0
    for i, c in enumerate(diag):
        if c == '.':
            continue
        elif c == '#':
            mask = 1 << i
            diagram |= mask
    return diagram

def button_nums_to_bit(buttons):
    button_bins = []
    for i, b in enumerate(buttons):
        mask = 0
        for l in b:
            mask |= 1 << l
        button_bins.append(mask)
        print(f'Button {i} converted from {b} to {bin(mask)}')
    return button_bins

def load_input(file) -> Light:
    lights = []
    with open(file) as f:
        for line in f.readlines():
            match = re.match(r'^(\[[.#]+\]) ((?:\([\d,]+\) *)+) ({[\d,]+})$', line) 
            diagram_str = match.group(1).strip('[]')
            diagram = diag_str_to_bit(diagram_str)

            button_part = match.group(2)
            buttons_split = button_part.strip('()').split(') (')
            buttons_nums = [
                [int(i) for i in b.split(',')]
                for b in buttons_split
                ]
            buttons = button_nums_to_bit(buttons_nums)

            jolts = match.group(3)

            lights.append(Light(diagram, buttons, jolts))
    return lights


def find_min_button_press(light: Light) -> int:
    for button_count in range(1, len(light.buttons) + 1):
        button_combos = combinations(light.buttons, button_count)
        potential = 0
        for combo in button_combos:
            for button in combo:
                potential ^= button
            if potential == light.diagram:
                return button_count
            potential = 0
    return None

def solve_part1(puzzle_input):
    lights = load_input(puzzle_input)
    button_press_per_Light = []
    for l in lights:
        Light.print_light(l)
        min_press = find_min_button_press(l)
        if min_press is not None:
            button_press_per_Light.append(min_press)
    sum_of_min_presses = sum(button_press_per_Light)
    return(sum_of_min_presses)


def main():
    print('Advent Day 10\n')
    # solution = solve_part1('./day10/input_example.txt')
    solution = solve_part1('./day10/input.txt')
    print(f'Part 1 Solution: Fewest presses to configure all lights: {solution}')


if __name__ == "__main__":
    main()
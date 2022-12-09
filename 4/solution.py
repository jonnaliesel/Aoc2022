import re


def get_puzzle_input(file: str) -> list[str]:
    return [line.strip() for line in open(f"{file}.txt", "r").readlines()]


def create_list(r1: int, r2: int) -> list:
    return list(range(r1, r2 + 1))


def parse_input(sections: list) -> list:
    ranges = []
    for section in sections:
        input = re.split(",|-", section)
        elf_1 = create_list(int(input[0]), int(input[1]))
        elf_2 = create_list(int(input[2]), int(input[3]))
        ranges.append([elf_1, elf_2])
    return ranges


def sort_sections(elves: list) -> list:
    sorted_sections = []
    for elf in elves:
        pass
        if len(elf[0]) >= len(elf[1]):
            outer, inner = elf[0], elf[1]
        else:
            outer, inner = elf[1], elf[0]
        sorted_sections.append([outer, inner])
    return sorted_sections


def solution(sections: list) -> int:
    dubble_work = 0
    overlapping = 0
    for outer, inner in sections:
        all_in = []
        for section in inner:
            if section in outer:
                all_in.append(True)
            else:
                all_in.append(False)

        if all(all_in):
            dubble_work += 1
        if any(all_in):
            overlapping += 1
    return dubble_work, overlapping


sections = get_puzzle_input("input")
ranges = parse_input(sections)
sorted_sections = sort_sections(ranges)
solutions = solution(sorted_sections)
print(solutions)

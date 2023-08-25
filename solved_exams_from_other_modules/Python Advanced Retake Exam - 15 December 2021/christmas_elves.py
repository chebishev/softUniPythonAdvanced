from collections import deque

elf_energy = deque(int(x) for x in input().split())
boxes_of_materials = [int(x) for x in input().split()]

total_energy = 0
elves_counter = 0
toys_counter = 0
no_more_elves = False

while elf_energy and boxes_of_materials:
    current_elf = elf_energy.popleft()
    while current_elf < 5:
        if elf_energy:
            current_elf = elf_energy.popleft()
        else:
            no_more_elves = True
            break
    if no_more_elves:
        break
    elves_counter += 1
    current_box = boxes_of_materials.pop()
    current_toys = 0
    current_energy = 0

    if elves_counter % 3 == 0:
        if current_elf >= current_box * 2:
            current_energy = current_box * 2
            current_elf -= current_energy
            if elves_counter % 5 == 0:
                current_toys = 0
            else:
                current_toys = 2
                current_elf += 1
        else:
            current_elf *= 2
            boxes_of_materials.append(current_box)

        elf_energy.append(current_elf)

    else:
        if current_elf >= current_box:
            current_energy += current_box
            current_elf -= current_box
            if elves_counter % 5 == 0:
                current_toys = 0
            else:
                current_elf += 1
                current_toys = 1
        else:
            current_elf *= 2
            boxes_of_materials.append(current_box)

        elf_energy.append(current_elf)

    toys_counter += current_toys
    total_energy += current_energy

print(f"Toys: {toys_counter}")
print(f'Energy: {total_energy}')
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if boxes_of_materials:
    print(f"Boxes left: {', '.join(str(x) for x in boxes_of_materials)}")

# test inputs:

# 10 16 13 25
# 12 11 8

# 10 14 22 4 5
# 11 16 17 11 1 8

# 5 6 7
# 2 1 5 7 5 3

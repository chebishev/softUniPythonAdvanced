def boarding_passengers(capacity, *passengers):
    passengers_dictionary = {}
    partial = False
    full = False
    for group in passengers:
        count, program = group
        if capacity == 0:
            full = True
            break
        if capacity - count < 0:
            partial = True
            continue
        if program not in passengers_dictionary:
            passengers_dictionary[program] = 0
        passengers_dictionary[program] += count
        capacity -= count

    sorted_dictionary = sorted(passengers_dictionary.items(), key=lambda x: (-x[1], x[0]))
    output = "Boarding details by benefit plan:\n"
    for key, value in sorted_dictionary:
        output += f"## {key}: {value} guests\n"

    if not full and not partial:
        message = "All passengers are successfully boarded!"
    elif full:
        message = "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        message = f"Partial boarding completed. Available capacity: {capacity}."
    output += message
    return output


# test inputs:

# print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))

# print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15,
# 'Diamond'), (10, 'Gold')))

# print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31,
# 'Platinum'), (20, 'Diamond')))

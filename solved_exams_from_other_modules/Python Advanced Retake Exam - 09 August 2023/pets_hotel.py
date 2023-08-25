def accommodate_new_pets(capacity, weight_limit, *pets):
    pets_dict = {}
    hotel_capacity = capacity
    maximum_weight = weight_limit

    for pet, weight in pets:
        if hotel_capacity:
            if weight <= maximum_weight:
                if pet not in pets_dict.keys():
                    pets_dict[pet] = 0
                pets_dict[pet] += 1
                hotel_capacity -= 1

        else:
            output = ['You did not manage to accommodate all pets!']
            break
    else:
        output = [f"All pets are accommodated! Available capacity: {hotel_capacity}."]

    output.append("Accommodated pets:")
    for pet, count in sorted(pets_dict.items()):
        output.append(f"{pet}: {count}")
    return '\n'.join(output)


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))

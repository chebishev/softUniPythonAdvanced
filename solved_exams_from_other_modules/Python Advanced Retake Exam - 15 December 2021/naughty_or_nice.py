def naughty_or_nice_list(kids_names, *args, **kwargs):
    output = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for action in args:
        current_action = action.split("-")
        number = int(current_action[0])
        name = current_action[1]
        kids_by_number = []
        for item in kids_names:
            if item[0] == number:
                kids_by_number.append(item)
        if len(kids_by_number) == 1:
            output[name].append(kids_by_number[0][1])
            kids_names.remove(kids_by_number[0])

    for k, v in kwargs.items():
        kids_by_key = []
        for item in kids_names:
            if item[1] == k:
                kids_by_key.append(item)
        if len(kids_by_key) == 1:
            output[v].append(k)
            kids_names.remove(kids_by_key[0])

    if kids_names:
        for name in kids_names:
            output["Not found"].append(name[1])

    output_list = []
    for k, v in output.items():
        if len(v) > 0:
            output_list.append(f"{k}: {', '.join(v)}")

    return '\n'.join(output_list)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

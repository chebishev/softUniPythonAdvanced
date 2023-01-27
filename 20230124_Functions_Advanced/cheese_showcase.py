def sorting_cheeses(**kwargs):
    sorted_cheeses = dict(kwargs)
    output_list = []
    new_line = "\n"
    for k, v in sorted(sorted_cheeses.items(), key=lambda x: (-len(x[1]), x[0])):
        output_list.append(k)
        output_list.extend(sorted(v, reverse=True))

    return f"{new_line.join(str(x) for x in output_list)}"


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125]
    )
)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

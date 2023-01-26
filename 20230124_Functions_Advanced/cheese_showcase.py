def sorting_cheeses(**kwargs):
    cheeses = kwargs
    sorted_cheeses = sorted(cheeses.values(), key=len, reverse=True)
    index = 0
    for k in sorted(cheeses.items(), key=lambda x: (len(x[1]), x[0]), reverse=True):
        print(k)
        print(cheeses[k])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

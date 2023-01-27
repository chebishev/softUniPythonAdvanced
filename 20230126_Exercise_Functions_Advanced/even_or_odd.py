def even_odd(*args):
    command = args[-1]
    numbers = {
        "even": lambda x: [x for x in args[:-1] if x % 2 == 0],
        "odd": lambda x: [x for x in args[:-1] if x % 2 != 0]
    }

    return numbers[command](args)


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

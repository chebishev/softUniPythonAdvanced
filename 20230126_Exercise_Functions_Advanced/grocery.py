def grocery_store(**kwargs):
    sorted_receipt = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    output_list = []
    new_line = "\n"
    for k, v in sorted_receipt.items():
        output_list.append(f"{k}: {v}")
    return f"{new_line.join(output_list)}"


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
def start_spring(**kwargs):

    # reversing the items from the initial dictionary:
    output_dict = {}
    for k, v in kwargs.items():
        if v not in output_dict:
            output_dict[v] = []
        output_dict[v].append(k)

    sorted_dict = dict(sorted(output_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    output_list = []
    for k, v in sorted_dict.items():
        output_list.append(f"{k}:")
        for value in sorted(v):
            output_list.append(f"-{value}")

    return "\n".join(output_list)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower"}
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird"}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

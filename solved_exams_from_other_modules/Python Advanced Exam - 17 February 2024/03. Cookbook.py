def cookbook(*recipes):
    recipes_dictionary = {}

    for recipe in recipes:
        name, cuisine, ingredients = recipe
        if cuisine not in recipes_dictionary:
            recipes_dictionary[cuisine] = {}
        recipes_dictionary[cuisine].update({name: ingredients})

    output = ""
    sorted_recipes = sorted(recipes_dictionary.items(), key=lambda x: (-len(x[1]), x[0]))
    for recipe in sorted_recipes:
        cuisine = recipe[0]
        dictionary = recipe[1]
        output += f"{cuisine} cuisine contains {len(dictionary)} recipes:\n"
        for dish, ingredients in sorted(dictionary.items()):
            output += f"  * {dish} -> Ingredients: {', '.join(ingredients)}\n"

    return output


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
# ))
#
print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))

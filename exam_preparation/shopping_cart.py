def shopping_cart(*products):
    max_ingredients = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    meal_products = {
        "Soup": set(),
        "Pizza": set(),
        "Dessert": set()
    }
    for product in products:
        if product == "Stop":
            break
        meal = product[0]
        ingredient = product[1]

        if len(meal_products[meal]) == max_ingredients[meal]:
            continue
        else:
            meal_products[meal].add(ingredient)

    for key in meal_products:
        if len(meal_products[key]):
            break
    else:
        return "No products in the cart!"

    sorted_meals = dict(sorted(meal_products.items(), key=lambda x: (-len(x[1]), x[0])))
    output_list = []
    for k, v in sorted_meals.items():
        output_list.append(f"{k}:")
        if v:
            for value in sorted(v):
                output_list.append(f" - {value}")

    return "\n".join(output_list)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
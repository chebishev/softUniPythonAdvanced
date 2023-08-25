def shopping_list(budget, **products):
    if budget < 100:
        return "You do not have enough budget."

    bought_items = {}
    enough_money = True
    basket_is_full = False
    while enough_money and not basket_is_full:

        for k, v in products.items():
            if len(bought_items) < 5:
                product = k
                price, quantity = v
                result = price * quantity
                if result <= budget:
                    if product not in bought_items:
                        bought_items[product] = 0
                    bought_items[product] += result
                    budget -= result

                else:
                    continue
            else:
                basket_is_full = True
                break
        else:
            enough_money = False

    output = []
    for k, v in bought_items.items():
        output.append(f"You bought {k} for {v:.2f} leva.")

    return "\n".join(output)


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
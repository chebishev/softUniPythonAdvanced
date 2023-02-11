def stock_availability(flavours, command, *args):
    if command == "delivery":
        for element in args:
            flavours.append(element)
    elif command == "sell":
        if len(args) == 0:
            if flavours:
                flavours.pop(0)
        elif isinstance(args[0], int):
            elements_to_remove = args[0]
            for element in range(elements_to_remove):
                if flavours:
                    flavours.pop(0)
                else:
                    break
        else:
            for element in args:
                while element in flavours:
                    flavours.remove(element)

    return flavours


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

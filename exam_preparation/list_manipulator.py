def list_manipulator(initial_list, command, position, *args):
    if command == "add":
        if position == "end":
            for element in args:
                initial_list.append(element)
        else:
            for index in range(len(args) - 1, -1, -1):
                initial_list.insert(0, args[index])
    elif command == "remove":
        if position == "end":
            if args:
                for _ in range(args[0]):
                    initial_list.pop()
            else:
                initial_list.pop() if initial_list else None
        else:
            if args:
                for _ in range(args[0]):
                    initial_list.pop(0) if initial_list else None
            else:
                initial_list.pop(0) if initial_list else None

    return initial_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))

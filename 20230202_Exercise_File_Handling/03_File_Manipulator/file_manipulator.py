import os


def create_file(*args):
    file_name = args[0][0]
    new_file = open(file_name, "w")
    new_file.close()


def add_line(*args):
    file_name, new_line = args[0]
    with open(file_name, "a") as file:
        file.write(new_line + "\n")


def replace_line(*args):
    file_name, old_string, new_string = args[0]

    if not os.path.isfile(file_name):
        print("Non existing file")
    else:
        replaced_info = []

        with open(file_name, "r") as file:
            current_info = file.readlines()
            for element in current_info:
                if old_string in element:
                    element = element.replace(old_string, new_string)

                replaced_info.append(element)

        with open(file_name, "w") as output_file:
            output_file.write("".join(replaced_info))


def delete_file(*args):
    file_name = args[0][0]
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("Non existing file")


command_dictionary = {
    "Create": create_file,
    "Add": add_line,
    "Replace": replace_line,
    "Delete": delete_file
}

while True:

    command = input()

    if command == "End":
        break

    action, *options = command.split("-")

    command_dictionary[action](options)

# test input:

# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End


# A chance to check the content of the file:

# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# End

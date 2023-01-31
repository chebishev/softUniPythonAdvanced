numbers_dictionary = {}

line = input()

while line != "Search":

    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:   # added exception to handle lines that aren't integers
        print("The variable number must be an integer")
    # reading the line again in order to prevent infinite loop
    line = input()

line = input()

while line != "Remove":

    searched = line
    print(numbers_dictionary[searched])
    # added line in the loop in order to prevent infinite one
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:  # added exception in order to handle invalid keys
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)

# test inputs:

# one
# 1
# two
# 2
# Search
# one
# Remove
# two
# End

# one
# two
# Search
# Remove
# End

# one
# 1
# Search
# one
# Remove
# two
# End

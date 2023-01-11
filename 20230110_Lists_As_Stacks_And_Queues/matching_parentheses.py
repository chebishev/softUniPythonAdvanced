class MatchingParentheses:
    def __init__(self):
        self.initial_string = input()
        self.opening_parentheses = []

    def print_match(self, start, end):
        return self.initial_string[start:end + 1]


string = MatchingParentheses()
for index in range(len(string.initial_string)):
    if string.initial_string[index] == "(":
        string.opening_parentheses.append(index)
    elif string.initial_string[index] == ")":
        start_index = string.opening_parentheses.pop()
        end_index = index
        print(string.print_match(start_index, end_index))

# test inputs:

# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5

# (2 + 3) - (2 + 3)

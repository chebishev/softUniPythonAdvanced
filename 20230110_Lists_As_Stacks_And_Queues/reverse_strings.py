class ReverseStrings:
    def __init__(self):
        self.output = ""
        self.initial_list = [x for x in input()]

    def reverse(self):
        while self.initial_list:
            self.output += self.initial_list.pop()
        return self.output


test_stack = ReverseStrings()
print(test_stack.reverse())

# input_list = [x for x in input()]
# while input_list:
#     print(input_list.pop(), end="")

# test inputs:

# I Love Python

# Stacks and Queues

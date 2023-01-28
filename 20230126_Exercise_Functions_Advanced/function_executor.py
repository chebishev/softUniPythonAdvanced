def func_executor(*args):
    final_string = []
    new_line = "\n"
    for element in args:
        func_name = element[0]
        values = element[1]
        final_string.append(f"{func_name.__name__} - {func_name(*values)}")
    return f"{new_line.join(final_string)}"

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)), 
    (multiply_numbers, (2, 4))
))
###############################################
def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
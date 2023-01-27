def positives():
    return sum(number for number in list_of_numbers if number > 0)


def negatives():
    return sum(number for number in list_of_numbers if number < 0)


def conclusion():
    if abs(negatives()) > positives():
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


list_of_numbers = list(map(int, input().split()))
print(negatives())
print(positives())
print(conclusion())

# test inputs:

# 1 2 -3 -4 65 -98 12 57 -84

# 1 2 3

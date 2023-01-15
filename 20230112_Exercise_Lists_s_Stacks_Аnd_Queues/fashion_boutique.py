clothes = [int(x) for x in input().split()]
max_rack = int(input())
temp = 0
rack = 1

for number in clothes:
    if number + temp <= max_rack:
        temp += number
    else:
        rack += 1
        temp = number
print(rack)

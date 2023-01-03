clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 1
temp = 0
while clothes:
    if temp + clothes[-1] == rack_capacity:
        clothes.pop()
        if clothes:
            temp = clothes.pop()
            racks += 1
    elif temp + clothes[-1] > rack_capacity:
        temp = 0
        racks += 1
    else:
        temp += clothes.pop()

print(racks)

# test inputs:

# 5 4 8 6 3 8 7 7 9
# 16

# 1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20

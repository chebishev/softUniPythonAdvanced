from collections import deque

customers = deque(int(x) for x in input().split(", "))
taxis = [int(x) for x in input().split(", ")]
total_time = 0

while customers:
    current_customer = customers.popleft()
    if taxis:
        current_taxi = taxis.pop()
    else:
        customers.appendleft(current_customer)
        print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str, customers))}")
        break

    if current_taxi >= current_customer:
        total_time += current_customer
    else:
        customers.appendleft(current_customer)

else:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")

# test inputs:

# 4, 6, 8, 5, 1
# 1, 9, 15, 10, 6

# 10, 5, 8, 9
# 2, 4, 5, 8

# 2, 8, 4, 3, 11, 7
# 10, 15, 4, 6, 3, 10, 2, 1

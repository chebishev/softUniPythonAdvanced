from collections import deque

pizza_orders = deque(int(x) for x in input().split(", "))
pizzas_per_employee = [int(x) for x in input().split(", ")]
total_pizzas_made = 0
no_more_orders = False
while pizza_orders and pizzas_per_employee:
    current_order = pizza_orders.popleft()
    while current_order > 10 or current_order <= 0:
        if pizza_orders:
            current_order = pizza_orders.popleft()
        else:
            no_more_orders = True
            break
    if no_more_orders:
        break
    current_employee = pizzas_per_employee.pop()
    if current_order <= current_employee:
        total_pizzas_made += current_order
    elif current_order > current_employee:
        current_order -= current_employee
        total_pizzas_made += current_employee
        pizza_orders.appendleft(current_order)

if pizza_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in pizzas_per_employee)}")

# test inputs:

# 11, 6, 8, 1
# 3, 1, 9, 10, 5, 9, 1

# 10, 9, 8, 7, 5
# 5, 10, 9, 8, 7

# 12, -3, 14, 3, 2, 0
# 10, 15, 4, 6, 3, 1, 22, 1

from collections import deque

money = [int(x) for x in input().split()]  # stack
prices = deque([int(x) for x in input().split()])  # queue
food_eaten = 0
while money and prices:
    current_money = money.pop()
    current_price = prices.popleft()

    if current_money < current_price:
        continue

    else:
        food_eaten += 1
        if current_money > current_price:
            current_money -= current_price
            if money:
                money[-1] += current_money

if food_eaten == 0:
    print("Henry remained hungry. He will try next weekend again.")

elif food_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {food_eaten} foods.")
else:
    print(f"Henry ate: {food_eaten} food{'s' if food_eaten > 1 else ''}.")

# test inputs:

# 9 5 8 18
# 18 12 10 5

# 18 10 8 9
# 5 10 12 18

# 1 1 4 5 9 9 9
# 9 15 18 13 10

# 1 1 4 5 6 2 3 2
# 17 8 18 19 20

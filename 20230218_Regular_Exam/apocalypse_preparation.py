from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

items_table = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}

created_items = {

}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    elements_sum = current_medicament + current_textile
    for item in items_table:
        if elements_sum == item:
            if items_table[item] not in created_items:
                created_items[items_table[item]] = 0
            created_items[items_table[item]] += 1
            break
    else:
        if elements_sum > 100:
            if medicaments:
                current_medicament = medicaments.pop()
                current_medicament += elements_sum - 100
            if "MedKit" not in created_items:
                created_items["MedKit"] = 0
            created_items["MedKit"] += 1
        else:
            current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")
for k, v in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    print(f"{k} - {v}")
if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments[::-1])}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")

# test inputs:

# 20 10 40 70 20
# 10 50 10 30 20 80

# 30 30 10 80 60
# 40 20 30 10 70

# 30 30 10 80 60 20
# 40 20 30 10 70

# 60 15 20 30 20
# 20 15 40

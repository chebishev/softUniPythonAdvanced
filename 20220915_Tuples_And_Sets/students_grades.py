number_of_students = int(input())
students = {}
for student in range(number_of_students):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    print(f"{student} -> ", end="")
    for grade in grades:
        print(f"{grade:.2f}", end=" ")
    print(f"(avg: {(sum(grades)/len(grades)):.2f})")

# test inputs:

# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00

# 4
# Scott 4.50
# Ted 3.00
# Scott 5.00
# Ted 3.66

# 5
# Lee 6.00
# Lee 5.50
# Lee 6.00
# Peter 4.40
# Kenny 3.30

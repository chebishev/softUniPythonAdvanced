# Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even. Use
# nested comprehension for that problem. On the first line, you will receive the rows of the matrix. On the next
# rows, you will get elements for each column separated with a comma and a space ", ".

print([[int(x) for x in input().split(", ") if int(x) % 2 == 0] for _ in range(int(input()))])

# variant 2:
# matrix = []
# for row in range(int(input())):
#     matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
# print(matrix)

# test inputs:
# 2
# 1, 2, 3
# 4, 5, 6

# 4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67

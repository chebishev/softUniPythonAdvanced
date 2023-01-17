string = input()
output_dict = {ch: string.count(ch) for ch in string}
for k, v in sorted(output_dict.items()):
    print(f"{k}: {v} time/s")

# variant 2:
# text = input()
# counter = {}
# for character in text:
#     if character not in counter:
#         counter[character] = 0
#     counter[character] += 1
#
# for key in sorted(counter):
#     print(f"{key}: {counter[key]} time/s")

# test inputs:

# SoftUni rocks

# Why do you like Python?

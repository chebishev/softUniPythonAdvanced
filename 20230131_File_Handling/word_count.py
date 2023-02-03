import os
import re

words = input().split()
count_dictionary = {}
pattern = r"\b[A-z]+\b"
for word in words:
    if word not in count_dictionary:
        count_dictionary[word] = 0

with open("input.txt", "r") as file:
    data = file.read()
    lines = data.split()
    for word in lines:
        result = re.findall(pattern, word)
        current_word = result[0].lower() if result else None
        if current_word in count_dictionary:
            count_dictionary[current_word] += 1

sorted_dictionary = dict(sorted(count_dictionary.items(), key=lambda x: -x[1]))
file = open("output.txt", "w")
for k, v in sorted_dictionary.items():
    file.write(f"{k} - {v}\n")
file.close()

# test input:

# quick is fault

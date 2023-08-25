from collections import deque


def check_letter(letter):

    for key in words:
        if letter in words[key]:
            words[key] = words[key].replace(letter, "")


vowels = deque(x for x in input().split())
consonants = [x for x in input().split()]

words = {
    "rose": "rose",
    "tulip": 'tulip',
    "lotus": "lotus",
    "daffodil": "daffodil"}

word_found = False
while vowels and consonants:

    current_vowel = vowels.popleft()
    check_letter(current_vowel)
    curent_consonant = consonants.pop()
    check_letter(curent_consonant)

    for key in words:
        if not words[key]:
            word_found = True
            print(f"Word found: {key}")
            break
    if word_found:
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

# test inputs:

# o e a o e a i
# p r s x r

# a a a
# x r l t p p

# u a o i u y o e
# p m t l

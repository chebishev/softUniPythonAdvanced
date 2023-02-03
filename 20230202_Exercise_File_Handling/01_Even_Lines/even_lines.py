symbols_for_converting = {"-", ",", ".", "!", "?"}

with open("../02_Line_Numbers/text.txt", "r") as file:
    input_text = file.readlines()

    for line in input_text:

        if input_text.index(line) % 2 == 0:

            for ch in line:
                if ch in symbols_for_converting:
                    line = line.replace(ch, "@")

            print(*line.split()[::-1])

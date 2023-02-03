output_list = []

with open("text.txt") as file:
    input_text = file.readlines()

    for index in range(1, len(input_text) + 1):
        current_line = input_text[index - 1]
        char_counter = 0
        punctuation_counter = 0

        for ch in current_line:
            if ch != " " and ch != "\n":
                if ch.isalpha():
                    char_counter += 1
                else:
                    punctuation_counter += 1

        output_list.append(f"Line {index}: {current_line[:-1]} ({char_counter})({punctuation_counter})\n")

with open("output.txt", "w") as output_file:
    output_file.write("".join(output_list))

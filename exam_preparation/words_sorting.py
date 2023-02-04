def words_sorting(*words):
    words_dictionary = {}
    for word in words:
        if word not in words_dictionary:
            words_dictionary[word] = 0
        words_dictionary[word] = sum([ord(x) for x in word])
    sum_values = 0
    sorted_dictionary = None
    for k in words_dictionary:
        sum_values += words_dictionary[k]

    if sum_values % 2 == 0:
        sorted_dictionary = sorted(words_dictionary.items(), key=lambda x: x[0])
    else:
        sorted_dictionary = sorted(words_dictionary.items(), key=lambda x: -x[1])

    output_list = []
    for k, v in sorted_dictionary:
        output_list.append(f"{k} - {v}")

    return "\n".join(output_list)


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',         
        'accolade'
  ))


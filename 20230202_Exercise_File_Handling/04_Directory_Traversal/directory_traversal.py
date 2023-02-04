import os
extensions_dictionary = {}
original_directory = os.curdir
file_list = os.listdir(".")
folder_found = None
folder_count = 0
directory_found = ""
while True:

    for file in file_list:
        current_file = file.split(".")
        if len(current_file) == 1:
            directory_found = current_file[0]
            folder_found = True
            folder_count += 1
        else:
            extension = current_file[1]
            if extension not in extensions_dictionary:
                extensions_dictionary[extension] = []
            extensions_dictionary[extension].append(file)

    if not folder_found:
        break

    if folder_count > 2:
        break
    # updating the current path in order to get item for the first subdirectory
    file_list = os.listdir(os.chdir("./" + directory_found))
    folder_found = False


# going to the original directory
[os.chdir("../") for _ in range(2)]

# writing the info from the dictionary into the "report.txt" file
with open("report.txt", "w") as output_file:
    for k in sorted(extensions_dictionary):
        output_file.write(f".{k}\n")
        for v in sorted(extensions_dictionary[k]):
            output_file.write(f"- - - {v}\n")


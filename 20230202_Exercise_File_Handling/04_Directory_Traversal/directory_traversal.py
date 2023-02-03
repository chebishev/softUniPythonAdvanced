import os
extensions_dictionary = {}
file_list = os.listdir("RESOURCES")
folder_found = None
directory_found = ""
while True:

    for file in file_list:
        current_file = file.split(".")
        if len(current_file) == 1:
            directory_found = current_file[0]
            folder_found = True
        else:
            extension = current_file[1]
            if extension not in extensions_dictionary:
                extensions_dictionary[extension] = []
            extensions_dictionary[extension].append(current_file)

    if not folder_found:
        break

    file_list = os.listdir(os.chdir(directory_found))
    folder_found = False

    print(extensions_dictionary)
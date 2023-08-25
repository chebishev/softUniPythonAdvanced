def get_magic_triangle(number_of_rows):
    triangle = []
    for index in range(1, number_of_rows + 1):
        current_row = [1] * index
        for column in range(len(current_row)):
            if column == 0 or column == len(current_row) - 1:
                current_row[column] = 1
            else:
                current_row[column] = triangle[index - 2][column - 1] + triangle[index - 2][column]
        triangle.append(current_row)

    return triangle


get_magic_triangle(5)

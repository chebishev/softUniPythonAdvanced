def softuni_students(*students_info, **courses):
    students = {}
    invalid_students = []
    for student in students_info:
        id = student[0]
        username = student[1]
        if id not in students:
            students[username] = []
        students[username] = [id, ""]

    for id, name in courses.items():
        for student in students:
            if id == students[student][0]:
                students[student] = [id, name]

    for student, id in students.items():
        if id[1] == "":
            invalid_students.append(student)

    output = ""
    for student, id in sorted(students.items(), key=lambda x: x[0]):
        if student not in invalid_students:
            output += f"*** A student with the username {student} has successfully finished the course {id[1]}!\n"
    if invalid_students:
        output += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
    return output


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))

print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))

print(softuni_students(('id_7', 'Silvester1'),
                       ('id_7', 'The programmer'),
                       ('id_32', 'Katq21'), id_76='Spring Fundamentals',
                       id_7='Spring Advanced',
                       ))

print(softuni_students(('id_1', 'John'),
                       ('id_3', 'Bob'),
                       ('id_4', 'Eve'),
                       ('id_2', 'Alice'),
                       ('id_43', 'Chris'),
                       ('id_12', 'Mariya'),
                       id_1='Course 1',
                       id_3='Course 2',
                       id_12='Course 3', ))

def students_credits(*args):
    student_credits = {}
    max_credits = 0
    
    for row in args:
        discipline, credits, max_test_points, diyans_points = row.split("-")
        current_credits = int(credits) * (int(diyans_points) / int(max_test_points))
        student_credits[discipline] = current_credits
        max_credits += current_credits
    
    sorted_dict = sorted(student_credits.items(), key=lambda x: -x[1])
    final_list = []
    new_line = "\n"
    
    for item in sorted_dict:
        final_list.append(f"{item[0]} - {item[1]:.1f}")
    
    if max_credits < 240:
        return f"Diyan needs {(240  - max_credits):.1f} credits more for a diploma.\n{new_line.join(final_list)}"
    else:
        return f"Diyan gets a diploma with {max_credits:.1f} credits.\n{new_line.join(final_list)}"
    
print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
from collections import deque


def gather_credits(*args):
    input_list = deque(args)
    credits_needed = input_list.popleft()
    credits_gained = 0
    enrolled_courses = []
    while credits_needed > credits_gained:
        if input_list:
            course_name, course_credits = input_list.popleft()
            if course_name not in enrolled_courses:
                enrolled_courses.append(course_name)
                credits_gained += course_credits
        else:
            return "You need to enroll in more courses! " \
                   f"You have to gather {credits_needed - credits_gained} credits more."

    else:
        output = sorted(enrolled_courses)
        return f"Enrollment finished! Maximum credits: {credits_gained}.\n" \
               f"Courses: {', '.join(output)}"


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

from collections import deque

def fill_the_box(*args):
    box_queue = deque(x for x in args)
    height = int(box_queue.popleft())
    length = int(box_queue.popleft())
    width = int(box_queue.popleft())
    box_volume = height * length * width

    def cubes_rest(queue, start_element):
        while queue:
            current_element = queue.popleft()
            if current_element == "Finish":
                break
            start_element += int(current_element)
        return start_element


    while True:
        next_line = box_queue.popleft()
        if next_line == "Finish":
            return f"There is free space in the box. You could put {box_volume} more cubes."
        else:
            next_line = int(next_line)
            if box_volume - next_line < 0:
                last_element = abs(box_volume - next_line)
                return f"No more free space! You have {cubes_rest(box_queue, last_element)} more cubes."
            elif box_volume - next_line == 0:
                return f"No more free space! You have {cubes_rest(box_queue, 0)} more cubes."
            else:
                box_volume -= next_line

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
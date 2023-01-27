def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * (length + width)

    if not type(length) == int or not type(width) == int:
        return "Enter valid values!"

    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"


print(rectangle(2, 10))
print(rectangle('2', 10))

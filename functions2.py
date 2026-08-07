def calculate_area(radius):
    c = 3.14 * (radius * radius)
    print(f"area of the circle: {c}")
def calculate_circumference(radius):
    d = (2 * 3.14) * radius
    print(f"circumference of the circle: {d}")

def main():
    calculate_area(9)
    calculate_circumference(9)
main()
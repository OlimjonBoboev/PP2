import math

# Convert degrees to radians
def deg_to_rad(deg):
    return round(math.radians(deg), 6)

deg = 15
print("Output radian:", deg_to_rad(deg))

# Calculate area of a trapezoid
def trapezoid_area(h, b1, b2):
    return 0.5 * (b1 + b2) * h

h, b1, b2 = 5, 5, 6
print("Trapezoid area:", trapezoid_area(h, b1, b2))

# Calculate area of a regular polygon
def polygon_area(sides, length):
    return round((sides * (length ** 2)) / (4 * math.tan(math.pi / sides)), 2)

sides, length = 4, 25
print("Polygon area:", polygon_area(sides, length))

# Calculate area of a parallelogram
def parallelogram_area(base, height):
    return base * height

base, height = 5, 6
print("Parallelogram area:", parallelogram_area(base, height))

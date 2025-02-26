import math

# Function to calculate area of different shapes
def calculate_area(shape, dimension1, dimension2=0):
    if shape == "circle":
        return math.pi * dimension1 ** 2
    elif shape == "rectangle":
        return dimension1 * dimension2
    elif shape == "triangle":
        return 0.5 * dimension1 * dimension2
    else:
        return "Invalid shape"

# Testing the function with different shapes
print("Circle area:", calculate_area("circle", 5))
print("Rectangle area:", calculate_area("rectangle", 4, 6))
print("Triangle area:", calculate_area("triangle", 8, 10))

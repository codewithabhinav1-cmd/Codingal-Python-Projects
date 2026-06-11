import turtle  # importing library

# Set up screen
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300, 400)

# Create turtle object
polygon = turtle.Turtle()

# Variables
num_sides = 6
side_length = 70
angle = 360.0 / num_sides

# Draw polygon
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

# Keep window open
turtle.done()
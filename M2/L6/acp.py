import turtle

# Create turtle object
square = turtle.Turtle()

# Draw square
for i in range(4):
    square.forward(100)  # Draw side
    square.right(90)     # Turn 90 degrees

# Keep window open
turtle.done()
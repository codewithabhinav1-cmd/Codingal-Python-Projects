import turtle

# Set background color
turtle.Screen().bgcolor("Aqua")

# Create turtle object
board = turtle.Turtle()

# First triangle for the star
board.forward(100)  # Draw base

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

# Move to position for second triangle
board.penup()
board.right(150)
board.forward(50)

# Second triangle for the star
board.pendown()

board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

# Keep window open
turtle.done()
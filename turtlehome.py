import turtle

# --- Setup ---
screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.title("Simple Fun with Shapes")
pen = turtle.Turtle()
pen.speed(1) # Set speed for drawing

# --- Function to draw regular polygons ---
def draw_regular_polygon(sides, length, color_outline, color_fill, start_x, start_y):
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color(color_outline)
    pen.fillcolor(color_fill)
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(length)
        pen.right(360 / sides)
        pen.end_fill()

# --- Draw Shapes ---

# Equilateral Triangle
draw_regular_polygon(3, 100, "blue", "cyan", -200, 50)

# Hexagon
draw_regular_polygon(6, 60, "purple", "magenta", 150, 50)

# Rectangle (requires specific dimensions)
pen.penup()
pen.goto(-50, 50)
pen.pendown()
pen.color("red")
pen.fillcolor("pink")
pen.begin_fill()
pen.forward(150)
pen.right(90)
pen.forward(75)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(75)
pen.right(90)
pen.end_fill()

# --- Keep window open ---
turtle.done()

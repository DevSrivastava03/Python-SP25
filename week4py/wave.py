import turtle
import random

turtle.setup(1000, 800)
turtle.bgcolor("#1a1a1a") 

t = turtle.Turtle()
t.speed(0)
t.width(2)

base_colors = ["#1f78b4", "#33a02c", "#e31a1c", "#ff7f00", "#6a3d9a", "#b15928"]
glow_colors = ["#3a9ad9", "#5cb85c", "#f04e30", "#ffa533", "#7d50b2", "#d77944"]

def draw_hexagon(x, y, size, color, glow_color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Create a glow effect by layering a slightly larger shape
    t.color(glow_color)
    t.width(4)
    t.begin_fill()
    for _ in range(6):
        t.forward(size * 1.05)
        t.right(60)
    t.end_fill()

    # Main hexagon
    t.color(color)
    t.width(2)
    t.begin_fill()
    for _ in range(6):
        t.forward(size)
        t.right(60)
    t.end_fill()

# Dynamic pattern
def draw_pattern(rows, cols, size):
    for row in range(rows):
        for col in range(cols):
            x = col * (size * 1.5) - 400  
            y = row * (size * 1.3) - (col % 2) * (size * 0.75) - 300  
            
            # Gradient sets
            color_index = (row + col) % len(base_colors)
            color = base_colors[color_index]
            glow_color = glow_colors[color_index]

            draw_hexagon(x, y, size, color, glow_color)
            
draw_pattern(8, 12, 40)  

t.hideturtle()
turtle.done()

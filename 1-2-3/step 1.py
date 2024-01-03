# Imports
import turtle as trtl
import random as rand

# Setup Turtles
maze_painter = trtl.Turtle()
wn = trtl.Screen()

# Configuration Values
wall_length = 10
wall_increment = 10
wall_color = "black"
door_width = 15

# Configure Turtles
maze_painter.speed(0)
maze_painter.pencolor(wall_color)
'''
Psuedocode for drawing the basic spiral
x = starting distance
y = incremental distance

In a loop:
    1. go forward x
    2. turn left 90 degrees
    3. go forward x + y
    2. turn left 90 degrees
'''
width = 10
def draw_spiral():
    global wall_length, wall_increment
    maze_painter.penup()
    maze_painter.goto(0,0)
    maze_painter.pendown()
    for wall in range (25):
        if wall > 3:
            randomNum = rand.randint(0,1)
            maze_painter.left(90)
            if randomNum == 1:
                draw_barrier()
                draw_door()

            else:
                draw_barrier()
                draw_door()
        maze_painter.forward(wall_length + wall_increment - 30)
        wall_increment += 10

    maze_painter.hideturtle()

# Draw door method
def draw_door():
    maze_painter.forward(10)
    maze_painter.penup()
    maze_painter.forward(width * 2)
    maze_painter.pendown()

# Draw barrier method
def draw_barrier():
    maze_painter.forward(40)
    maze_painter.left(90)
    maze_painter.forward(width * 2)
    maze_painter.back(width * 2)
    maze_painter.right(90)




# randomize location of doors and barriers in wall





draw_spiral()




wn.mainloop()

import turtle as trtl



drawer = trtl
'''


x = starting distance
y = incremental distance

In a loop
    1. go forward x
    2. turn left 90 degrees
    3.go forward x + y
    2. turn left 90 degrees






    
'''


def drawSpiral():
    x = 10
    y = 10

    drawer.penup()
    drawer.goto(0, 0)
    drawer.pendown()
    for wall in range(25):
        drawer.left(90)
        drawer.forward(x +                                                                                                                                                                                          y)
        y += 10



drawSpiral()
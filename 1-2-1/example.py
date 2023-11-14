import turtle as trtl
test = trtl.Turtle()

def drawTriangle():
    test.pendown()
    test.fd(100)
    test.right(120)
    test.fd(100)
    test.right(120)
    test.fd(100)

def drawTriangle(long, x, y):
    test.penup()
    test.goto(x, y)
    test.pendown()
    test.fd(long)
    test.right(120)
    test.fd(long)
    test.right(120)
    test.fd(long)

x = 100
y = 100
for tri in range(100):
    drawTriangle(100, 30, 40)


wn = trtl.Screen()
wn.mainloop()
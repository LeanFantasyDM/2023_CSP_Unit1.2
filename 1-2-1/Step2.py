# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand


#-----game configuration----
Star = trtl.Turtle()
Star.shape("circle")
Star.shapesize(5)
Star.fillcolor("pink")
Score = 0


#-----initialize turtle-----


#-----game functions--------
def Star_clicked(x, y):
    update_Score()
    change_position()

def change_position():
    global Star
    new_xpos = rand.randint(0, 300)
    new_ypos = rand.randint(0, 300)
    print(new_xpos)
    print(new_ypos)
    Star.penup()
    Star.goto(new_xpos, new_ypos)

def update_Score():
    global Score
    Score + 1
    print("Score")


#-----events----------------
Star.onclick(Star_clicked)



wn = trtl.Screen()
wn.mainloop()






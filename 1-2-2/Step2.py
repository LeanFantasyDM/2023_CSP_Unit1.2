# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
leaderboard_file_name = "a122_leaderboard.txt"
player_name = input ("Please enter your name:")
Star = trtl.Turtle()
Star.shape("circle")
Star.shapesize(5)
Star.fillcolor("pink")
Score = 0
ScoreWriter = trtl.Turtle()
ScoreWriter.hideturtle()
ScoreWriter.penup()
ScoreWriter.goto(300, -300)
font_setup = ("Arial", 20, "normal")
counter = trtl.Turtle()
counter.penup()
counter.goto(-350, -350)
counter.pendown()
counter.hideturtle()
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----


#-----game functions--------
def Star_clicked(x, y):
    global timer_up
    if timer_up == False:
        change_position()
        update_Score()
    else:
        counter.hideturtle()



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
    Score += 1
    ScoreWriter.clear()
    ScoreWriter.write(Score,font_setup)


def manage_leaderboard():
    pass


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


#-----events----------------
Star.onclick(Star_clicked)



wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()






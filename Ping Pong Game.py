# imported module turtle
import turtle

        # window setup
wind = turtle.Screen() # intialize the screen
wind.title("ping bong game by OUSHA") # set the title of the screen
wind.bgcolor("black") # set the background color
wind.setup(width=800, height=600) # set he width and height of the window
wind.tracer(0) # stops the window from updates automatically

              ########################################

# madrab1

madrab1 = turtle.Turtle()  # intialize turtle object(shape)
madrab1.speed(0)         # set the speed of the animation
madrab1.shape("square")  # set the shape of the object
madrab1.color("red")     # set the color of object
madrab1.shapesize(stretch_wid=5, stretch_len=1)   # set the width and height of the object
madrab1.penup()     # stops the object from drawn lines
madrab1.goto(-350, 0)  # the position of object

# madrab2

madrab2 = turtle.Turtle() # intialize turtle object(shape)
madrab2.speed(0)  # set the speed of the animation
madrab2.shape("square") # set the shape of the object
madrab2.color("blue")   # set the color of object
madrab2.shapesize(stretch_wid=5, stretch_len=1)  # set the width and height of the object
madrab2.penup() # stops the object from drawn lines
madrab2.goto(350, 0)   # the position of object

# ball

ball = turtle.Turtle() # intialize turtle object(shape)
ball.speed(0)  # set the speed of the animation
ball.shape("circle")  # set the shape of the object
ball.color("white")  # set the color of object
ball.shapesize(stretch_wid=1.1, stretch_len=1.1)  # set the width and height of the object
ball.penup()  # stops the object from drawn lines
ball.goto(0, 0)   # the position of object
ball.dx = 0.5
ball.dy = 0.5

# score

score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1 : 0   player 2 : 0" , align="center" , font=("courier",24,"normal"))

        #########################

#FUNCTIONS for (madrab1)
def madrab1_up():
     y = madrab1.ycor() # get the y coordinates of the madrab
     y  += 30  # set the y to increas by 20
     madrab1.sety(y)  #set the new y to y coordinates

def madrab1_low():
    y = madrab1.ycor()   # get the y coordinates of the madrab
    y -= 30  # set the y to decreas by 20
    madrab1.sety(y)    #set the new y to y coordinates

                   ############################################
# FUNCTIONS for (madrab2)
def madrab2_up():
    y = madrab2.ycor() # get the y coordinates of the madrab
    y += 20  # set the y to increas by 20
    madrab2.sety(y)  #set the new y to y coordinates


def madrab2_low():
    y = madrab2.ycor() # get the y coordinates of the madrab
    y -= 20   # set the y to decreas by 20
    madrab2.sety(y) #set the new y to y coordinates

                   ############################################
#keyboard bindings
wind.listen() # tell the window to expect the keyboard input
wind.onkeypress(madrab1_up,"w") # set the key  for up function of madrab1
wind.onkeypress(madrab1_low,"s") # set the key  for down function of madrab1
wind.onkeypress(madrab2_up,"Up") #set the key  for up function of madrab2
wind.onkeypress(madrab2_low,"Down") ## set the key  for down function of madrab2


#main game loop

while True:

    wind.update() # update the window everytime the loop runs

# the moving of the ball
    ball.setx(ball.xcor() + ball.dx) # ball starts with 0 and everytime loop run-------> +0.5 x-axis
    ball.sety(ball.ycor() + ball.dy) # ball starts with 0 and everytime loop run-------> +0.5 y-axis

# border check , top border 300px , bottom border 300px , ball 22px
    if ball.ycor() >290: # if the at top border
      ball.sety(290) # set y coordinate +290
      ball.dy *= -1 # reverse the direction , making +0.5---->-0.5

    if ball.ycor() <-290: # if the at bottom border
      ball.sety(-290) # set y coordinate -290
      ball.dy *= -1 # reverse the direction , making +0.5---->-0.5


    if ball.xcor() >390: # if the at right border
      ball.goto(0,0) # set the ball at the center
      ball.dx *= -1 # reverse the direction , making +0.5---->-0.5
      score1 += 1
      score.clear()
      score.write("player 1 : {}   player 2 : {}".format(score1, score2), align="center", font=("courier", 24, "normal"))
      

    if ball.xcor() <-390: # if the at left border
      ball.goto(0,0) # set the ball at the center
      ball.dx *= -1 # reverse the direction , making +0.5---->-0.5
      score2 += 1
      score.clear()
      score.write("player 1 : {}   player 2 : {}".format(score1, score2), align="center", font=("courier", 24, "normal"))

    #collision of the ball
    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1






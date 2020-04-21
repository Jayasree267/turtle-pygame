
import turtle
import time
wn=turtle.Screen()
wn.bgcolor('black')
wn.title("pong game")
wn.setup(width=800,height=600)
wn.tracer()

score_a = 0
score_b = 0

#paddle 1
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.penup()
paddle1.shape("square")
paddle1.shapesize(stretch_wid=6,stretch_len=1)
paddle1.color("red")
paddle1.goto(-350,0)

#paddle 2
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.penup()
paddle2.shape("square")
paddle2.shapesize(stretch_wid=6,stretch_len=1)
paddle2.color("blue")
paddle2.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx=2   
ball.dy=2

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black") 
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0 || player B: 0", align ="center", font=("courier",24,"normal"))
    
def paddle1_up():
    y=paddle1.ycor()
    y=y+20
    paddle1.sety(y)

def paddle1_down():
    y=paddle1.ycor()
    y=y-20
    paddle1.sety(y)

def paddle2_up():
    y=paddle2.ycor()
    y=y+20
    paddle2.sety(y)


def paddle2_down():
    y=paddle2.ycor()
    y=y-20
    paddle2.sety(y)

wn.listen()
wn.onkeypress(paddle1_up,'w')
wn.onkeypress(paddle1_down,'s')
wn.onkeypress(paddle2_up,'a')
wn.onkeypress(paddle2_down,'b')

 
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    
   #Border checking
    if ball.ycor()>290:
       ball.sety(290)
       ball.dy=ball.dy*-1
       
    if ball.ycor()<-290: 
       ball.sety(-290)
       ball.dy=ball.dy*-1

    if ball.xcor()>390:
       ball.goto(0,0)
       pen.clear()
       score_a = score_a + 1
       pen.write("player A: {} || player B: {}".format(score_a,score_b), align ="center", font=("courier",24,"normal")) 
       ball.dx = ball.dx * -1

    if ball.xcor()<-390:
       ball.goto(0,0)
       pen.clear()
       score_b = score_b + 1
       pen.write("player A: {} || player B: {}".format(score_a,score_b), align ="center", font=("courier",24,"normal")) 
       ball.dx=ball.dx*-1

    if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()< paddle2.ycor()+ 50 and ball.ycor()>paddle2.ycor()-50):
      ball.setx(340)
      ball.dx=ball.dx*-1                                         

    if(ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle1.ycor()+ 50 and ball.ycor()>paddle1.ycor()-50):
      ball.setx(-340)
      ball.dx=ball.dx*-1

    if paddle1.ycor()>250:
       paddle1.sety(250)


    if paddle1.ycor()<-250:
        paddle1.sety(-250)

    if paddle2.ycor()>250:
        paddle2.sety(250)

    if paddle2.ycor()<-250:
        paddle2.sety(-250) 

        
       
   
    

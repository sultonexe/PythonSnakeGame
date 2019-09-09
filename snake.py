#SNAKE GAME with Python3 Programming
#Coded By @sulton.exe
#TOLONG JANGAN RECODE YA :) HARGAI SI PEMBUAT TERIMA KASIH :D

import turtle
import time
import random

delay = 0.1

#Score
score = 0
hscore = 0

#Set Up The Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Snake Game Using Python By SultonExe")
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake Head
shead = turtle.Turtle()
shead.speed(0)
shead.shape("square")
shead.color("white")
shead.penup()
shead.goto(0, 0)
shead.direction = "stop"

#Make a Snake Food
sfood = turtle.Turtle()
sfood.speed(0)
sfood.shape("circle")
sfood.color("yellow")
sfood.penup()
sfood.goto(0, 100)

#Snake Body
segments = []

#Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align="center", font=("courier", 24, "normal"))

#Function

def go_up():
    if shead.direction != "down":
        shead.direction = "up"

def go_down():
    if shead.direction != "up":
        shead.direction = "down"

def go_left():
    if shead.direction != "right":
        shead.direction = "left"

def go_right():
    if shead.direction != "left":
        shead.direction = "right"

def move():

    if shead.direction == "up":
        y = shead.ycor()
        shead.sety(y + 20)

    if shead.direction == "down":
        y = shead.ycor()
        shead.sety(y - 20)

    if shead.direction == "left":
        x = shead.xcor()
        shead.setx(x - 20)

    if shead.direction == "right":
        x = shead.xcor()
        shead.setx(x + 20)        

#Keyboard Controls
wn.listen()
wn.onkeypress(go_up, "i")
wn.onkeypress(go_down, "k")
wn.onkeypress(go_left, "j")
wn.onkeypress(go_right, "l")

#Main Game Loop
while True:
    wn.update()

    #Check for a collision with the border
    if shead.xcor() > 290 or shead.xcor() < -290 or shead.ycor() > 290 or shead.ycor() < -290:
        time.sleep(1)
        shead.goto(0, 0)
        shead.direction = "stop"
    
        #hide the segment
        for segment in segments:
            segment.goto(1000, 1000)

        #clear the segments list
        segments.clear()

        #reset the score
        score = 0

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, hscore), align="center", font=("courier", 24, "normal"))

    if shead.distance(sfood) < 20:
        #Move the food
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        sfood.goto(x, y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)

        #increase the score
        score += 5

        if score > hscore:
            hscore = score

        pen.clear()
        pen.write("Score: {}   High Score: {}".format(score, hscore), align="center", font=("courier", 24, "normal"))

    #Move The End Segment
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    #Move Segment 0 to where the head
    if len(segments) > 0:
        x = shead.xcor()
        y = shead.ycor()
        segments[0].goto(x, y)


    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(shead) < 20:
            time.sleep(1)
            shead.goto(0, 0)
            shead.direction = "stop"

            #hide the segment
            for segment in segments:
                segment.goto(1000, 1000)

            #clear the segments list
            segments.clear()

            #reset the score
            score = 0

            pen.clear()
            pen.write("Score: {}   High Score: {}".format(score, hscore), align="center", font=("courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
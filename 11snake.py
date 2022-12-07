# import required modules
import turtle
import time
import random

#init game variables
delay = 0.1
score = 0
high_score = 0
this_colors = ['red', 'blue', 'green','purple', 'pink', 'violet', 'brown1', "yellow"]
shapes = random.choice(['square', 'circle'])
sizes = [i/2 for i in range(1,5)]

#init modes
background_rave = False #colour changing
varied_speed = False #varied speed
earthworm = False #skin
monochrome = False #monochrome
bomb_mode = False #bomb
TATWD = False #turtles all the way down
varied_size = False #random segment size + food
segment_colours = False #change each segment colours
invisible = False #invisible mode with blink
wide = False #wide screen mode
agario = False #snake evolves into block

#choosing game mode in terminal
mode = -1
modestring = ["background_rave", "varied_speed", "earthworm", "monochrome", "bomb_mode", "TATWD", "varied_size", "segment_colours", "invisible" ,"wide", "agario"]
# index = [i for i in range(11)]
print("0 - normal mode")
for i in range(len(modestring)):
    print(f"{i+1} - {modestring[i]}")
while mode not in [str(i) for i in range(12)]:
    mode = input("Choose your game mode: ")
if mode == '1':
    background_rave = True
elif mode == '2':
    varied_speed = True
elif mode == '3':
    earthworm = True
elif mode == '4':
    monochrome = True
elif mode == '5':
    bomb_mode = True
elif mode == '6':
    TATWD = True
elif mode == '7':
    varied_size = True
elif mode == '8':
    segment_colours = True
elif mode == '9':
    invisible = True
elif mode == '10':
    wide = True
elif mode == '11':
    agario = True

# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)

if wide:
    wn.setup(width=1000, height=700)
    wn.tracer(0)


# bomb (turtle object)
if bomb_mode:
    bomb = turtle.Turtle()
    bomb.speed(0)
    bomb.shape("turtle")
    bomb.color("black")
    bomb.penup()
    bomb.goto(100, 0)

# head of the snake (turtle object)
head = turtle.Turtle()
head.shape("square")
if TATWD:
    head.shape("turtle")
if invisible:
    head.shape("circle")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game (turtle object)
food = turtle.Turtle()
colors = random.choice(['yellow'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
if TATWD:
    food.shape("turtle")
food.color(colors)
food.penup()
food.goto(0, 100)


#init score (turtle object)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
if invisible:
    pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
print('init')
pen.write("Score : 0  High Score : 0", align="center", font=("candara", 24, "bold"))

# rotate snake head
def goup():
    if head.direction != "down":
        head.direction = "up"
    if TATWD:
        head.left(270)
        if segments != []:
            for segment in segments:
                segment.left(270)

def godown():
    if head.direction != "up":
        head.direction = "down"
    if TATWD:
        head.left(90)
        if segments != []:
            for segment in segments:
                segment.left(90)

def goleft():
    if head.direction != "right":
        head.direction = "left"
    if TATWD:
        head.left(180)
        if segments != []:
            for segment in segments:
                segment.left(180)

def goright():
    if head.direction != "left":
        head.direction = "right"
        if TATWD:
            if segments != []:
                for segment in segments:
                    segment.left(270)

#move head
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#key bind         
wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")


segments = []
prevTime = 0
currentTime = 0

# Main Gameplay
while True:
    wn.update()

    # blink background
    if invisible:
        wn.bgcolor("white")#default before blink
        currentTime = time.time()
        if (currentTime - prevTime > 3): #every sec
            print("change color")
            for i in range(2):
                for i in range(100):
                    wn.bgcolor("blue")
                for i in range(100):
                    wn.bgcolor("white")
            prevTime = time.time()
            # print(currentTime, prevTime)

    # border collision
    if wide:
        x, y = 490, 340
    else: 
        x= y = 290
    if head.xcor() > x or head.xcor() < -x or head.ycor() > y or head.ycor() < -y:
        if invisible:
            wn.bgcolor('black')
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    
    if bomb_mode:
        if head.distance(bomb) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delaly = 0.1
            time.sleep(0.5)

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        if agario: 
            size = 1
            for segment in segments:
                size += 2
                segment.turtlesize(stretch_wid = size)

        if varied_size:
            size = random.choice(sizes)
            food.turtlesize(stretch_wid=size)

        if bomb_mode:
            i = random.randint(-270, 270)
            j = random.randint(-270, 270)
            if i != x and j != y:
                bomb.goto(i, j)
            else:
                i = random.randint(-270, 270)
                j = random.randint(-270, 270) 
        
        if background_rave:
            col = random.choice(['purple', 'pink', 'violet', 'brown1'])
            #"red", "green", "yellow",
            wn.bgcolor(col)

        elif varied_speed:
            wn.bgcolor('CornflowerBlue')
            speeds = random.choice([1, 5, 10])
            head.speed(speeds)
            for segment in segments:
                segment.speed(speeds)

        elif monochrome:
            col = random.choice(['gray90','gray80', 'gray70', 'gray60', 'gray50', 'gray40', 'gray30'])
            wn.bgcolor(col)
        
        elif earthworm:
            wn.bgcolor('brown')
            
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("orange")  # tail colour
        
        if TATWD:
            new_segment.shape("turtle")
        if monochrome:
            new_segment.color("black")
        elif segment_colours:
            print(this_colors)
            col = random.choice(this_colors)
            print(col)
            new_segment.color(col)
        elif invisible:
            new_segment.color("white")

        if varied_size:
            if segments != []:
                segment.turtlesize(stretch_wid=size)

        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
        
    move()
    # print(head.xcor(), head.ycor())

    # Checking for head collisions with body segments
    for segment in segments:
        if segment.distance(head) < 10:
            # print("crash self")
            if invisible:
                wn.bgcolor('black')
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            print('cleared')

            score = 0
            delay = 0.1
            pen.clear()
            print(281)
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

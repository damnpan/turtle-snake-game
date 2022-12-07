# CTD 1D Documentation
## Required Libraries
### Turtle
Turtle is a Graphical User Interface that allows us to run the snake game on another window using keybinds through the use of `turtle.onkey()`. Turtle objects can be moved on the turtle window, which 

### Random
Random library helps us to generate psedudo-random random to vary the occurences of game instances, such as random window colours and random speeds of the snake.

### Time
The time library allows us to add delays in the game for our game mechanics through `time.sleep` and `time.time`.

## Game Setup
### Main
The user is prompted with a menu of game modes. The user makes a choice, after which, the snake game is played in the turtle window. 

### Game Objects
Turtle objects are used to create the components of the game, namely the snake head, snake body, food, score and bomb. 

```python 
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

# Adding segment
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
```

### Mechanics
Rotation of snake head decides the direction of snake movement. This also prevents snake from changing direction 180 degrees (eg from up to down). Move moves the snake by changing the coordinates of the snake turtle objects. This is tied to the keyboard controls WASD and arrow keys. 
```python
# rotate snake head
def goup():
    if head.direction != "down":
        head.direction = "up"

def godown():
    if head.direction != "up":
        head.direction = "down"

def goleft():
    if head.direction != "right":
        head.direction = "left"

def goright():
    if head.direction != "left":
        head.direction = "right"

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
```

### Spawning The Food
After being eaten by the snake, the food is spawned at random coordinates. 
```python
if head.distance(food) < 20:
    x = random.randint(-270, 270)
    y = random.randint(-270, 270)
    food.goto(x, y)
```
### Scoreboard
Scoreboard is updated to give the current score and the highscore.
```python
if score > high_score:
    high_score = score
pen.clear()
print(250)
pen.write("Score : {} High Score : {} ".format(
    score, high_score), align="center", font=("candara", 24, "bold"))
```

### Movement of Snake Body
```python
#move segments of snake, starting with last segment
for index in range(len(segments)-1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)
#move first segment of body
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

#move head    
move()
```
### Collision Checking
If snake bumps into wall or its own body, game terminates.
```python
# Checking for head collisions with body segments
for segment in segments:
    if segment.distance(head) < 10:
        if invisible:
            wn.bgcolor('black')
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        print('cleared')
```

## Game Modes 
Games modes are controlled through Boolean variables. 
``` python
background_rave = False #colour changing
varied_speed = False #varied speed
earthworm = False #earthworm skin
monochrome = False #monochrome
bomb_mode = False #bomb
TATWD = False #turtles all the way down
varied_size = False #random segment size + food
segment_colours = False #change each segment colours
invisible = False #invisible mode with blink
wide = False #wide screen mode
agario = False #snake evolves into block
```

### "Invisible" Game Mode
This game mode makes the snake white, as such it is "invisible" to the player. Making use of the time library, the background occasionally changes colour to indicate to the player the position of the snake. In addition, the snake reappears upon death (by changing background colour to black). 
```python
# main game mechanic showcased: blinking background
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
```

### "Bomb Mode" Game Mode
The snake game is played with both a food object and a bomb object spawning on the board. If the snake eats the bomb, the game terminates. 
```python
# main game mechanic showcased: collision sequence
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
```
```python
# main game mechanic showcased: bomb respawn
#respawn bomb in random location when food is respawned
if bomb_mode:
    i = random.randint(-270, 270)
    j = random.randint(-270, 270)
    if i != x and j != y:
        bomb.goto(i, j)
    else:
        i = random.randint(-270, 270)
        j = random.randint(-270, 270)
```
### "Wide" Game Mode
Large window version of the default game

### "Agario" Game Mode
Inspired by popular webgame 'Agario',  we use `turtle.turtlesize(stretch_wid)`, we create the visual effect of the snake evolving into a singular block that grows bigger when the food is eaten. 
```python
# main game mechanic showcased: agario formation/evolution
# if agario: 
    size = 1
    for segment in segments:
        size += 2
        segment.turtlesize(stretch_wid = size)
```
### "Varied Size" Game Mode
The food takes on a random sizes, which in turn causes the snake's body segments to vary in size when it is eaten.
```python
# main game mechanic showcased: varying food size
if varied_size:
    size = random.choice(sizes)
    food.turtlesize(stretch_wid=size)

# main game mechanic showcased: varying snake segment size
if varied_size:
    if segments != []:
        segment.turtlesize(stretch_wid=size)
```
### "Background Rave" Game Mode
Window background changes colours when snake eats food. The colours are chosen from a pre-determined array called `col`.
```python        
# main game mechanic showcased: background colour changes
if background_rave:
    col = random.choice(['purple', 'pink', 'violet', 'brown1'])
    #"red", "green", "yellow",
    wn.bgcolor(col)
```
### "Varied Speed" Game Mode
Each time food is eaten, snake's speed is set to a random value. 
```python
# main game mechanic showcased: varied speed
elif varied_speed:
    wn.bgcolor('CornflowerBlue')
    speeds = random.choice([1, 5, 10])
    head.speed(speeds)
    for segment in segments:
        segment.speed(speeds)
```
### "Monochrome" Game Mode
The background colours change when the food is eaten, varying between shades of gray. In addition the snake body is now black. In essence, it is in monochrome.
```python
# main game mechanic showcased: window colour change
elif monochrome:
    col = random.choice(['gray90','gray80', 'gray70', 'gray60', 'gray50', 'gray40', 'gray30'])
    wn.bgcolor(col)
```
### "TATWD" Game Mode aka "Turtles All The Way Down" Game Mode
What if the snake was made out of turtles? A homage to the turtle library, this game mode makes all objects turtle shaped, including the snake, snake body and the food. 

In addition, the snake head rotates to face the direction of the motion, using `turtle.Turtle().left()`. 
```python
# main game mechanic showcased: game mechanics
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

```
### 'Segment Colours' Game Mode
This game mode randomises the colours of the segments of the snake's body to give a colourful snake.
```python
# main game mechanic showcased: window colour change
elif segment_colours:
    print(this_colors)
    col = random.choice(this_colors)
    print(col)
    new_segment.color(col)
```
### 'Earthworm' Game Mode
Snake on brown background.
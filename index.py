import turtle
import random
import time

jimmy = turtle.Turtle()
jimmy.shape("circle")
jimmy.speed("fastest")

screen = turtle.Screen()
screenTk = screen.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)

##########  Variables ##########
### Colors List ##
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

### Planets
planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
planetsVel = [3.7, 8.87, 9.807, 3.721, 24.79, 10.44, 8.87, 11.15]

### Timer Variable ##
timer = 0

### FPS Count ##
fps = 0
fps_count = 0
start_time = time.time()


########## Functions ##########
def box(size):
    
    ### Declare Turtle ##
    boxTurtle = turtle.Turtle()
    boxTurtle.speed("fastest")

    ### Draw Box ##
    boxTurtle.penup()
    boxTurtle.goto(size, size)
    boxTurtle.pendown()
    boxTurtle.goto(size, -size)
    boxTurtle.goto(-size, -size)
    boxTurtle.goto(-size, size)
    boxTurtle.goto(size, size)

    ### Hide Turtle ##
    boxTurtle.hideturtle()

#Takes in velocity in m/s, converts to pixels/frame
#moves it that much in 1 frame
def move(xVelocity, yVelocity):
    
    pixelsToMoveX = xVelocity / 6 #Converts X Velocity from meters per second
                                  #to pixels per frame

    currentXCoord = jimmy.xcor()  #Gets x coordinate of our turtle
    
    newXCoord = currentXCoord + pixelsToMoveX #Adds x pixels per frame to
                                                #turtle's x coordinate

    pixelsToMoveY = yVelocity / 6 #Converts Y Velocity from meters per second
                                  #to pixels per frame

    currentYCoord = jimmy.ycor()  #Gets y coordinate of our turtle

    newYCoord = currentYCoord + pixelsToMoveY  #Adds y pixels per frame to
                                                #turtle's Y coordinate
    
    jimmy.setposition(newXCoord, newYCoord) #Updates turtle's position to
                                            #new x coord and new y coord


########## While Loop ##########
box(400)

#While loop runs per frame, like unity's update function!

xVelocity = float(planetsVel[5]) #X velocity in m/s
yVelocity = float(planetsVel[5]) #Y velocity in m/s

randomAccel = float(planetsVel[5])

ntimer = 0

while ntimer < 25:
    print(ntimer)
    
    if jimmy.xcor() > 400:
        xVelocity = -xVelocity
        
        jimmy.color(colors[timer])

        
        timer +=1

        ntimer +=1
        
        
        ##randomAccel = random.randrange(-20, 1)

    if jimmy.xcor() < -400:
        xVelocity = -xVelocity
        
        jimmy.color(colors[timer])
        
        timer +=1

        ntimer +=1


        ##randomAccel = random.randrange(-20, 1)

        
    if jimmy.ycor() > 400:
        yVelocity = -yVelocity
        
        jimmy.color(colors[timer])
        
        timer +=1
        
        ##randomAccel = random.randrange(-20, 1)

    if jimmy.ycor() < -400:
        yVelocity = -yVelocity
        
        jimmy.color(colors[timer])
    
        timer +=1

        ntimer +=1

        ##randomAccel = random.randrange(-20, 1)
        
    ### Resets Timer Length
    if timer >= len(colors):
        timer = 0

    ### Get Frame Rate
    if (time.time()-start_time) > 1:
        fps = fps_count
        fps_count = 1
        start_time = time.time()
    else:
        fps_count += 1

    # FPS = 0
    if fps == 0:
        fps = 1000

    if ntimer == 24:
        print(ntimer)
        jimmy.hideturtle()

    
    #This is our move function:
    move(xVelocity, yVelocity) #The first input is our x velocity
                                #The second is our y velocity
        
    xVelocity = xVelocity + 0       #X acceleration
    yVelocity = yVelocity + randomAccel / -fps #Y acceleration

    

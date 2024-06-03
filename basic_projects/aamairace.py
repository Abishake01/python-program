# Aamai race...
import turtle
import time
import random

HEIGHT,WIDTH=500,500
COLORS=['red','blue','black','yellow','purple','pink','cyan','brown','orange','grey']
def get_numberof_racers():
    racer=0
    while True:
        racer=input('Enter a Number of Players to Play (2 - 10 ): ')
        if racer.isdigit():
            racer=int(racer)
        else:
            print('Please Enter a Number...Try Again')
            continue
        if 2<= racer <=10:
            return racer
        else:
            print('The number Must be between the range (2-10)...Try again')
def race(colors):
    turtles=create_turtles(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,10)
            racer.forward(distance)
            
            x,y=racer.pos()
            if y>= HEIGHT //2 -10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*spacingx,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_race():
    screen=turtle.Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title('Aamai Race')
            
racers=get_numberof_racers()
init_race()
random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)
print("The Winner is ",winner)
time.sleep(5)

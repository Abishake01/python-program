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
            print('Must be between the range (2-10)...Try again')
            
def init_race():
    screen=turtle.Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title('Aamai Race')
            
racers=get_numberof_racers()
print(racers)
init_race()
random.shuffle(COLORS)
colors=COLORS[:racers]
print(colors)

'''
#basic turtle function
racer=turtle.Turtle()

racer.speed(1)#It is a speed of the turtle
racer.penup()#It is used to remove a line turtle move...
racer.shape('turtle')# It is a turtle shape shows...
racer.color('yellow')#It is used for a color difference
racer.forward(100)#forward and backward is a distance move
racer.pendown()#it shows a line
racer.left(90)#left right is a 90degree,45degree
racer.forward(100)
racer.right(90)
racer.backward(100)
racer.right(90)
racer.forward(100)
 
racer2=turtle.Turtle()

racer2.speed(5)#It is a speed of the turtle
racer2.penup()#It is used to remove a line turtle move...
racer2.shape('turtle')# It is a turtle shape shows...
racer2.color('brown')#It is used for a color difference
racer2.forward(150)#forward and backward is a distance move
racer2.pendown()#it shows a line
racer2.left(90)#left right is a 90degree,45degree
racer2.forward(100)
racer2.right(90)
racer2.backward(150)
racer2.right(90)
racer2.forward(150)
'''
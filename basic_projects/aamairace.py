# Aamai race...
import turtle
import time
HEIGHT,WIDTH=500,500

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
            
racer=get_numberof_racers()
print(racer)
init_race()
racer=turtle.Turtle()
racer.forward(100)#forward and backward is a distance move
racer.left(90)#left right is a 90degree,45degree
racer.forward(100)
racer.right(90)
racer.backward(100)
racer.right(90)
racer.forward(100)
time.sleep(20)
 
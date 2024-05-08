#Rock, Paper ,Scissors
import random
u_point=0
c_point=0
draw=0
print('Welcome To Rock Paper Scissor Game...')
while True:
    user= input('Type Rock/paper/scissor or q to quit:\n').lower()
    if user == 'q':
        break
    if user not in ['rock','paper','scissor']:
        continue
    computer = random.choice(['rock','paper','scissor'])
    print('Computer Pick: ',computer)
    
    if user =='rock' and computer=='scissor':
        print('You Won!')
        u_point+=1
    elif user =='scissor' and computer=='paper':
        print('You Won!')
        u_point+=1
    elif user =='paper' and computer=='rock':
        print('You Won!')
        u_point+=1   
    elif user == computer:
        print('Draw...')
        draw+=1
    else:
        print('You Lost!')
        c_point+=1
        
print('You Won ',u_point,'Times...')
print('Computer Won ',c_point,'Times...')
print('Draws ',draw,'Times...')
print('Thanks For Playing...')
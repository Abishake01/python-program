import random
def play():
    player=input("Rock->r,Papper->p,scissors->s: ").lower()
    choose=['r','s','p']
    computer=random.choice(choose)
    if (player==computer):
        print("Match is draw")
    elif((player=='r' and computer=='s')or(player=='r' and computer=='p')or(player=='s' and computer=='r')or(player=='s' and computer=='p')or(player=='p' and computer=='s')or(player=='p' and computer=='r')):
        print("You Won the Match")
    else:
        print("You loose the Game!")
play()
    
    
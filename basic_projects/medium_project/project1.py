import random
def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll
 
while True:
    players=input('Enter the players (2-4): ')
    if players.isdigit():
        players=int(players)
        if 2<=players<=4:
            break
        else:
            print('Enter a number (2-4)')
    else:
        print('Invalide... Please Enter a Numbers(2-4)')
max_score=25
players_score=[0 for _ in range(players)]
print(players_score)
while max(players_score)< max_score:
    for player_ind in range(players):
        print('\nPlayer Number', player_ind+1,"Turn has just started")
        print('Your Total Score is:',players_score[player_ind],'\n')
        current_score=0
        while True:
            re_roll=input('Whould You like to roll (y): ')
            if re_roll.lower()!='y':
                break
            value=roll()
            if value==1:
                print('You rolled a 1! Turn Done!')
                current_score=0
                break
            else:
                current_score+=value
                print('You Rolled a:',value)
                
            print('Your Score is: ',current_score)
            
        players_score[player_ind]+=current_score
        print('Your Total Score is:',players_score[player_ind])
        
max_score=max(players_score)
winnig_ind=players_score.index(max_score)
print('Player Number',winnig_ind+1,'is the Winner with the score of:',max_score)
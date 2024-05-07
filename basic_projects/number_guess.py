import random
range=input('Type a Number: ')
if range.isdigit():
    range=int(range)
    if range <=0:
        print('Please Type a Number larger than 0..')
        quit()
else:
    print('Please Enter a Number...')
    quit()
random_num=random.randint(0,range) 
 
guesses=0
while True:
    guesses+=1
    user_guess=input('Make a Guess: ')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Please Enter a Number...')
        continue
    if user_guess==random_num:
        print('You Got It!')
        break
    else:
        print('You Got Wrong!')

print('You Got It in ',guesses,' guesses')
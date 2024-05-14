import random
options=["rock","paper","scissors"]
user_choice=input("Enter your choice(rock,paper,or scissors):")
computer_choice=random.choice("options")
print("computer choose:")
print(computer_choice)
if(computer_choice==user_choice):
	print("It's a tie!"or "It's a draw")
elif( user_choice=='rock' and computer_choice=='scissors' )or(user_choice=='rock' and computer_choice=='paper')or( user_choice=='paper' and computer_choice=='Rock'):
	print("you win the game")
elif("user_choice==scissor"and"computer_choice==rock")or("user_choice==paper"and"computer_science==rock")or("user_choice==scissors"and"computer_choice==paper"):
	print("Game is over please try again")
else:
	print("Computer is win the game!")
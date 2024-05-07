print('Welcome to the Quiz Game....')
question= input('Do you want to play? \nSay(yes/no) ')
print(question)
if question.lower() !='yes':
    quit()
print('Lets play..' )
point=0
answer=input('Full Form of RAM?\n')
if answer.lower()=='random access memory':
    print('Correct')
    point+=1
else:
    print('Incorrect')
answer=input('Full Form of ROM?\n')
if answer.lower()=='read only memory':
    print('Correct')
    point+=1
else:
    print('Incorrect')
answer=input('Full Form of CPU?\n')
if answer.lower()=='central process unit':
    print('Correct')
    point+=1
else:
    print('Incorrect')
answer=input('Full Form of CM?\n')
if answer.lower()=='chief minister':
    print('Correct')
    point+=1
else:
    print('Incorrect')
    
print('You Got a ',point,'Points in the Quiz')
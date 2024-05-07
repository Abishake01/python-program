import answer
print('Welcome to the Quiz Game....')
question= input('Do you want to play? \nSay(yes/no) ')
print(question)
if question.lower() !='yes':
    quit()
print('Lets play..' )
Points=0
q1=input('Full Form of RAM?\n')
p1=answer.qu1(q1,Points) 
q2=input('Full Form of ROM?\n')
p2=answer.qu2(q2,Points)
q3=input('Full Form of CPU?\n')
p3=answer.qu3(q3,Points)
q4=input('Full Form of CM?\n')
p4=answer.qu4(q4,Points)
Point=p1+p2+p3+p4

print('You Got a ',(Point/4)*100,'Points in the Quiz')
    

#Timed Math challenge
import random
import time
 
OPERATORS=['+','-','*']
MAX_OPE=12
MIN_OPE=3
TOTAL_PROBLEMS=10

def problem_gen():
    left=random.randint(MIN_OPE,MAX_OPE) 
    right=random.randint(MIN_OPE,MAX_OPE)
    operator=random.choice(OPERATORS)
    exp=str(left)+' '+operator+' '+str(right)
    answer=eval(exp)
    return exp,answer
 
 
wrong=0
print('Lets start the Math Problems!')
print('---------------------------------')
start_time=time.time()
for i in range(TOTAL_PROBLEMS):
    exp,answer=problem_gen()
    while True:
        guess=input('Problem #'+str(i+1)+': '+exp+'=')
        if guess==str(answer):
            break
        wrong+=1
end_time=time.time()
Total_time=round(end_time-start_time)
print('---------------------------------')
print('Nice Work You Finished ',Total_time,'seconds')
print('Wrong Answers ',wrong)
'''
# The basic of if statement...
if True:
    print('It is True...')
elif False:
    print('It is False...')
else:
    print('Not True and Not False')
    
    a==True
    a>=b or a<=b or a!=b
'''    

#If execute only if true statement...
#elif execute may be true or false it check and run ...
a=int(input('Enter a Number: '))
b=int(input('Enter b Number: '))
c=int(input('Enter c Number: '))
if (a<b and a<c):# and check both the condition are true meand if statement is execute...or means any one of the condition true it execute
    #if(a<c): it is nested if statement
        print('A is lesser')
elif (b<c):
    print('B is lesser')
else:
    print('C is lesser')
#-------------------------------------------------------------------------------------------------------------------------------------------------
d=2
 
if d==True:
    print('It is True...')
elif d== False:
    print('It is False...')
else:
    print('Not True and Not False')
#-------------------------------------------------------------------------------------------------------------------------------------------------
#type check
val= tuple(input('Enter a value:'))  
if type(val)==str:
    print('It is a String')
elif type(val)==int:
    print('It is integer')
elif type(val)==list:
    print('It is List')
elif type(val)==tuple:
    print('It is tuple')
else:
    print('None of these')
#-------------------------------------------------------------------------------------------------------------------------------------------------
#Eligible to Vote check...
age=int(input('Enter your age: '))
if age>18:
    print('You can vote...')
elif age==18:
    print('You will apply for voting')
else:
    print("You are not eligible to vote...")
#-------------------------------------------------------------------------------------------------------------------------------------------------
#Too check odd number or even number
a=int(input('Enter a Number: '))
if a%2==0:
    print('It is Even Number ',a)
else:
    print('It is odd number ',a)
#-------------------------------------------------------------------------------------------------------------------------------------------------


 
#While loop check the condition if the condition is true means it executed
 
i=1

while i<3:#it check the ccondition it is true means it will execute
    print(i)
    i+=1# increament 1 again check the condition untile the condition false

while i<6 and i==1:
    print(i)
    i=i+1
# it is a basic concept of while loop 
#-------------------------------------------------------------------------------------------------------------------------------------------------
#For Loop have a (start,end,increment)
for word in 'Solluu..':# it is basic concept of for loop...for word in 'something':  word is a var we asigin the the value of something
    print(word)
name=['abi','bala','kp']
for list in name:# we do this method also it will print one by one 
    print(list)#  it execute and check if condition
    if list=='bala':
        break#it stop the loop
    print(list)# it check and stop to eecute
    
for i in range(6,12,1):#n-1 are applied
    print(i)
else:
 print('for loop is End')
 
#-------------------------------------------------------------------------------------------------------------------------------------------------
print ('Odd numbers...')
for i in range(1,100,2):
    print(i) 
'''
try:
    x=int(input('Enter a Number: '))
    print(x)
except:
    print('Not an integer')
else:
    print('Nothing will happend...')
'''
    
try:
    x=2/0
    print(x)
except:#it shows what type of error occuerd
    print('zero is not divide')
finally:#Even try and except block are execute or not finall statement run successfully
    print('Try block executed...succesfully')
 
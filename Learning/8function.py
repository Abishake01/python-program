# Function in Python we use def()
def v(name):# def variable(arguments):    Error->TypeError: v() missing 1 required positional argument: 'name'
    print('Function Works ...'+name)
v('abi')# it is call function 
def add(a,b):
    c=a+b
    print(c)
add(5,6)
'''
def v(name): 
    print('Function Works ...'+name)
v()
def add(a,b):
    c=a+b
    return(c)
d=add(5,6)
print(d)
'''
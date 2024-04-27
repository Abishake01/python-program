# Function in Python we use def()
def v(name):# def variable(arguments):   
    print('Function Works ...'+str(name))
v(23)# it is call function.  Error-->TypeError: can only concatenate str (not "int") to str

def add(a,b):
    c=a+b
    print(c)
add(5,6)
'''
def v(name):  Error->TypeError: v() missing 1 required positional argument: 'name'
    print('Function Works ...'+name)
v()
def add(a,b):
    c=a+b
    return(c)
d=add(5,6)
print(d)
'''
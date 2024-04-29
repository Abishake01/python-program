# Function in Python we use def()
def v(name):# def variable(arguments):   
    print('Function Works ...'+str(name))
v(23)# it is call function.  Error-->TypeError: can only concatenate str (not "int") to str

def add(a,b):
    c=a+b
    print(c)
add(5,6)#add(a=5,b=6) we also use like this same answer 
'''
We get the input of value and call the function also
def v(name):  Error->TypeError: v() missing 1 required positional argument: 'name'
    print('Function Works ...'+name)
v()

'''
def name(*val):# name(*val) * the star denotes all value of the ()like tuple
    print(val[1])
name('abi','baral','lucy')

def sub(a,b):
    c=a-b
    return c# return type in python function
d=sub(5,6)
print(d)
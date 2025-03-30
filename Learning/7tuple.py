# Tuple is immutable --> Unchangeable  we use ()brackets When we separate , is identify it is tuple
name='a',1,True
area=str(('adf'))
print(name)#('a', 1)
print(type(name))#<class 'tuple'>
print(len(name))
#name[0]='abi'
print(name)#TypeError: 'tuple' object does not support item assignment
print(type(name[0]))#<class 'str'>
print(type(name[1]))#<class 'int'>
print(type(name[2]))#<class 'bool'>
print(type(area))#<class 'tuple'>


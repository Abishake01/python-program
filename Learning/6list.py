#Lis tis a Mutable--> It means Changeable 
state=['Tamil Nadu','Kerla','Andra Pradesh','Goa']
#If Want to change an element in the list usethis method [0] o
state[3]='karnataka'
print(state)
print(len(state))
#print(state[0]) To Access Index Value
print(state[0][4]) #to find an element using index value
print(state[1:])
print(state[:2])
print(state[0:3])#n-1 [start:end]end-1 will display
print(state[-1:])
print(state[-3:-1])
print(type(state))
#-------------------------------------------------------------------------------------------------------------------------------------------------
#mixed elements are used in list
dis=['Chennai',600028,True,'Avadi']
print(type(dis))#<class 'list'>
print(type(dis[0]))#<class 'str'>
print(type(dis[1]))#<class 'int'>
print(type(dis[2]))#<class 'bool'>
#-------------------------------------------------------------------------------------------------------------------------------------------------
#It is also list
name=list(('Abi','Arun',44,True))
print(name)#['Abi', 'Arun', 44, True]
#-------------------------------------------------------------------------------------------------------------------------------------------------
#List Methods....
l1=[21,34,56,42,78,25]
l2=['black','White','Yellow','Green']
l3=l2.copy()
l1.sort()#It sort the element in the ascending order
l2.reverse()#reverwse the all element in the list 
l3.pop()# It remove the last value of the list nothing will give in the pop()
l3.pop(1)#it remove the index element in the list
del l3[0] # delete the element are in the index of the list
# After the process it show an error NameError: name 'l3' is not defined. Did you mean: 'l1'?
print(l1)
print(l2)
print(l3)
# Methods Start
l1.append(l2)# Append is add a bunch of list or element in a new list---> it separate a list
l1.append(56)#Append add a element int he last of the list
l1.extend(l2)# Extend is add a element in the list
l2.insert(1,'blue')#Insert a element in between the list
#l2.remove('green')#ValueError: list.remove(x): x not in list
l2.remove('Green')
l3.clear()
print(l2.count('black'))
print(l2.index('black'))#shows an index value
#print(l1.append(l2)) None
print(l1)
print(l2)
print(l3)





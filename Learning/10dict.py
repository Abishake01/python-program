dict={
    'name':'Abi',
    'nationality':'Indian',
    'Age':19,  
    'course':'Django',
    'friends':['bala','kp']
    
}#{key:value} to access value using keys
a=dict['Age']
print('age',a)
print(dict)
print(type(dict))
#print(dict('name'))#TypeError: 'dict' object is not callable
print(type(dict['friends']))#<class 'list'>
print(dict['course'])# it consider recently used only


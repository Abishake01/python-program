str='Harry POtter'#string
#\n is used for next line
print('The Movie name is\n',str)
#str  shows a value stored in the variable
print(str)
#it can display third letter of str...string always start with 0
print(str[3])
#str[30] Error     print(str[30]) IndexError: string index out of range
#String functions
print(str.upper())
print(str.capitalize())
print(str.count('r'))
print(str.title())
print(str.split())
print(str.lower())
print(str.isalnum())
print(str.isalpha())
print(str.islower())
print(str.isupper())
print(len(str))
print(str.index('a'))#print(str.index('A')) ValueError: substring not found
print(str.replace('r','p'))
#We use this method also
print(str.upper().isupper())
file =open('C:/Users/abish/OneDrive/Desktop/Python/Learning/create.py','r')#open('path','mode')

print(file.readable())#boolean True
#print(file.readline())# Read 1st line
print(file.readlines()[0])# Read all lines
for files in file.readlines():
    print(files)
file.close()
 
#Write a file
#file.write('print(\'This is new line\')')
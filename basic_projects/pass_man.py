from cryptography.fernet import Fernet
main_pwd=input('What is Your Master Password: ')
def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            data_list = data.split("|")
    
    # If there are more than two elements, take only the first two
            user, pwd = data_list[:2]
            print('User: ',user,', Password: ',pwd)
 
def add():
    name=input('Account Name: ')
    password=input("Password: ")
    
    with open('password.txt','a') as f:
        f.write(name + '|' + password + '\n')

while True:
    mode =input('whould you like to add a New Password(add) or view existing one(view),press q for quit?\n').lower()
    if mode=='q':
        break
    if mode =='view':
        view()
    elif mode=='add':
        add()
    else:
        print('Invalid Please check the input...')
        continue
from cryptography.fernet import Fernet
def load_key():
    file=open('key.key','rb') 
    key=file.read()
    file.close()
    return key
 

key=load_key()
fer=Fernet(key)

'''
def write_key():
    key=Fernet.generate_key()
    with open ('key.key','wb') as key_file:
        key_file.write(key)
        '''

def view():
    with open('password.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            data_list = data.split("|")
    
    # If there are more than two elements, take only the first two
            user, pwd = data_list[:2]
            print('User: ',user,', Password: ',fer.decrypt(pwd.encode()).decode())
 
def add():
    name=input('Account Name: ')
    password=input("Password: ")
    
    with open('password.txt','a') as f:
        f.write(name + '|' + fer.encrypt(password.encode()).decode() + '\n')

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
# Password Generator
import random
import string

def pass_gen(min_length,numbers=True,special_character=True):
    letter=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    
    character=letter
    if numbers:
        character+=digits
    if special_character:
        character+=special
        
        
    pwd=''
    meets_criteria=False
    has_number=False
    has_special=False
    
    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(character)
        pwd+=new_char
        
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
            
        meets_criteria=True
        
        if numbers:
            meets_critera=has_number
        if special_character:
            meets_criteria=meets_critera and has_special
            
    return pwd
            
            
min_length=int(input('Enter minimum length: '))
has_number=input('Do You want to numbers in password (y/n): ').lower()=='y'
has_special=input('Do You want to special character in password (y/n): ').lower()=='y'
gen_pass=pass_gen(min_length,has_number,has_special)
print('The Generated password is : ',gen_pass)
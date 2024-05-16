#Slot Machine
import random
MAX_LINES=3
MIN_BET=1
MAX_BET=100

ROWS=3
COLS=3
symbol_count={
    'A':2,
    'B':4,
    'C':6,
    'D':8  
}
def get_slot_machine_spin(rows,cols,symbols):
    all_symbole=[]
    for symbol,symbol_count in symbols.item():
        for _ in range(symbol_count):
            all_symbole.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbole[:]
        for row in range(rows):
            value= random.coice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],'|')
            else:
                print(column[row])
                
def deposit():
    while True:
        amount=input('What Whould You like to Deposite$ ')
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0')
        else:
            print('Enter a Number only...')
    return amount

def get_no_of_lines():
    while True:
        lines=input('Enter the Number of Lines To bet on (1-'+str(MAX_LINES)+'):')
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print('Enter a Valid number of Lines')
        else:
            print('Enter a Number only...')
    return lines

def get_bet():
    while True:
        amount=input('What Whould You like to Bet on each Line?$ ')
        if amount.isdigit():
            amount=int(amount)
            if 1<=amount<=MAX_BET:
                break
            else:
                print(f'Amount must be ${MIN_BET}-${MAX_BET} ')
        else: 
            print('Enter a Number only...')
    return amount
    
def main():
    balance=deposit()
    lines=get_no_of_lines()
    bet=get_bet()
    
main()    
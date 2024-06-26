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
symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2  
}
def check_winnings(columns,lines,bet,values):
    winning=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
            else:
                winning+=values[symbol]*bet
                winning_line.append(line+1)
    return winning,winning_line

def get_slot_machine_spin(rows,cols,symbols):
    all_symbole=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbole.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbol=all_symbole[:]
        for row in range(rows):
            value= random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=' | ')
            else:
                print(column[row],end='')
        print()
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

def spin(balance):
    lines=get_no_of_lines()
    while True:
        bet = get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f'You do not have enough to bet that amount, your current balance{balance}')
        else:
            break
    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to:${total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winning,winning_line=check_winnings(slots,lines,bet,symbol_value)
    print(f"you Won ${winning}.")
    print(f"You won on lines:",*winning_line)
    return winning-total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer=input('Press enter to paly (q to quit).')
        if answer =='q':
            break
        balance+=spin(balance)
    
    print(f"You left with ${balance}")
    
main()   
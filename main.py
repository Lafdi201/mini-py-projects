import random 
#Slot machine parameters
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS=3
COLS=3
#Symbols and symbol counts
sym_count = {
    "A" :3,
    "B" :5,
    "C" :8,
    "D" : 10
}

def machine_spins(rows,col,symbols):
    all_symbols = []
    for symbol, sym_count in symbols.items():
        for _ in range(sym_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(col):
        column = []
        current_sym=all_symbols[:]
        for _ in range(rows):
            value= random.choice(current_sym)
            current_sym.remove(value)
            column.append(value)
        columns.append(column) 
    return columns

def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
                print("please enter a number")
    return amount

def get_Number_Of_Lines():
    while True:
        lines= input("Please enter number of lines to bet on (1-"+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and 3")
        else:
            print("please enter a valid number")
    return lines

def get_bet():
    while True:
        bet=input("How much do you want to bet? ")
        if bet.isdigit():
            bet=int(bet)

            if MIN_BET<= bet <= MAX_BET :
                break
            else:
                    print("The bet must be between "+str(MIN_BET)+" and "+str(MAX_BET)+" ")    
        else:     
             print("please enter a number")
    return bet
def play (balance):
    lines= get_Number_Of_Lines()
    while True:
        bet= get_bet()
        total_bet=lines*bet
        if total_bet>balance :
            print(f"You don't have enough funds. Your balance is ${balance} ")
        else :
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}.")
    slots= machine_spins(ROWS,COLS,sym_count)
    print_slot_machine(slots)
    winningss, winning_lines= winnings(slots, lines, bet, multipliers)
    print(f"Lucky lines: $",*winning_lines,"$.")
    print(f"You won ${winningss} .")
    return winningss - total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin= input("press enter to play again, q to quit.")
        if spin == 'q':
            break
        balance +=play(balance)
    print(f"You left with ${balance}")

main()
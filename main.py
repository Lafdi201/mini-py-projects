MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
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
        bet=input("How much do you want to bet")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<= bet <= MAX_BET
                break
            else:
                print("The bet must be between "+str(MIN_BET)+" and "+str(MAX_BET)+" ")
        else: 
            print("please enter a number")
    return bet

def main():
    balance=deposit()
    lines= get_Number_Of_Lines()
    bet= get_bet()
    print("Balance: "+str(balance) + "  N. Lines: "+str(lines)+"")


main()
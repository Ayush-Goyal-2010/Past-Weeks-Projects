##### Gambling Game 

### Ayush Goyal
### 8/11/22
### Gambling Game For Practice

# importing random library
import random

# To Define The Values For UX
MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

# Defining The Number Of Rows And Columns In The Slot Machine
ROWS = 3
COLS = 3

# Defining A Dictionary With The Value And Its Number For To Gamble On
symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

# Defining A Dictionary For The Multpilier Of Bet For Each Symbol
symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

# Defining A Function check_winnings To Calculate The Winnings Or Loss Of The User
def check_winnings(columns ,lines ,values ,bet):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings
# Will Continue For Each Of The Three Columns/Rows

# Defining A Function get_slot_machine spin with rows,cols and symbols as three parameter. This Is Used To Get Values For The Columns And Rows
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
# This Is A One Time Function

# To Print The Slot Machine Valus On Kernel
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

# This Is A One Time Fumction

# Defining a function deposit to get the money the user wants to give 
def deposit():
    while True:
        amount = input("How Much Money Would You Like To Deposit in $ ? " + "\n$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please Enter A Number Greater Than Zero")
        else:
            print("Please Enter A Valid Number")
    return amount
# Due To While Loop, The Function Will Be Repeated Until The Statement Is True

# Defining a function get_number_of_lines to get the line the user wants to bet on out of MAX_LINES
def get_number_of_lines():
    while True:
        lines = input("How Many Lines Would You Like To Bet At (1-" + str(MAX_LINES) + ")?" "\n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("Please Enter A Valid Number Of Lines")
        else:
            print("Please Enter A Valid Number")
    return lines
# Due To While Loop, The Function Will Be Repeated Until The Statement Is True

# Defining a function get_bet to get the amount of money he wants to bet in between the MIN_BET and MAX_BET
def get_bet():
    while True:
        bet = input("How Much Money Would You Like To Bet On Each Line In $(" + str(MIN_BET) +"-" + str(MAX_BET) + ")" + "\n$")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount Must Be Greater That ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please Enter A Valid Number")
    return bet
# Due To While Loop, The Function Will Be Repeated Until The Statement Is True

# Defining Function Main To Store The Information
def main():
    balance = deposit()
    while True:
        print(f"Your Current Balance Is {balance}.")
        answer = input("Press Enter To Play (or Q to quit).")
        if answer == "Q":
            break
        balance += spin(balance)
    print(f"You Left With ${balance}")       
# To Know The Values On The Kernel

# Making A Seperate Function spin to get the values and instances of the user
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"Please Enter Money According To Your Balance. Your Current Balance Is ${balance}")
        else:
            break
    print(f"You Are Betting ${bet} on {lines}. You Total Bet Is ${total_bet} ")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = check_winnings(slots, lines, symbol_value, bet)
    winning_lines = check_winnings(slots, lines, symbol_value, bet)
    print(f"You Won ${winnings} and on lines: ", *str(winning_lines) )
    return winnings - total_bet
# Will Perform and find the entirety of the game a by the spin

main()
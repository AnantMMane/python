MAX_LINES = 3
MIN_BET=1
MAX_BET=100

def deposit():
    amount = 0
    while True:
        user_input = input("Please enter your deposit amount: $")
        if user_input.isdigit():
            amount = int(user_input)
            if amount < 0:
                print("Please enter a positive number")
            else:
                break
        else:
            print("Please enter a valid amount")
            continue
    print("Your deposit amount is: ", amount)
    return amount

def withdraw():
    amount = 0
    while True:
        user_input = input("Please enter your withdraw amount: $")
        if user_input.isdigit():
            amount = int(user_input)
            if amount < 0:
                print("Please enter a positive number")
                continue
            else:
                break
        else:
            print("Please enter a valid amount")
            continue
    print("Your withdraw amount is: ", amount)
    return amount

def get_no_of_lines():
    lines = 0
    while True:
        user_input = input(f"Please enter number of lines (1-{MAX_LINES}): ")
        if user_input.isdigit():
            lines = int(user_input)
            if lines < 1 or lines > MAX_LINES:
                print("Please enter a valid number of lines")
                continue
            else:
                break
        else:
            print("Please enter a valid number of lines")
            continue
    print("Number of lines is: ", lines)
    return lines

def get_bet():
    bet = 0
    while True:
        user_input = input("Please enter your bet amount on each line: ")
        if user_input.isdigit():
            bet = int(user_input)
            if bet < MIN_BET or bet > MAX_BET:
                print(f"Please enter a valid Bet amount. ({MIN_BET}-{MAX_BET})")
                continue
            else:
                break
        else:
            print("Please enter a valid amount")
            continue
    print("Your bet amount is: ", bet)
    return bet


if __name__ == '__main__':
    deposited = deposit()
    no_of_lines = get_no_of_lines()
    print(f"You have balance of ${deposited} and you have put bet on {no_of_lines} lines")


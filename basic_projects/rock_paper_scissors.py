import random

r,p,s = 'r', 'p', 's'
valid_choices = ('r', 'p', 's')
while True:
    user_input = input('Rock, paper, or scissors?(R/P/S): ').lower()
    if user_input not in valid_choices:
        print('Invalid input. Please try again.')
        continue

    computer_choice = random.choice([r,p,s])

    if user_input == computer_choice:
        print('It tie. Please try again.')
        continue
    elif user_input == r :
       if computer_choice == p:
           print('Computer wins!. Computer selected Paper.')
       if computer_choice == s:
           print('You wins!. Computer selected Scissors.')
    elif user_input == p:
        if computer_choice == r:
            print('You wins!. Computer selected Rock.')
        if computer_choice == s:
            print('Computer wins!. Computer selected Scissors.')
    elif user_input == s:
        if computer_choice == r:
            print('Computer wins!. Computer selected Rock.')
        if computer_choice == p:
            print('You wins!. Computer selected Paper.')


    user_want_to_play = input('Do you want to play again?(y/n): ').lower()
    if user_want_to_play == 'n':
        break





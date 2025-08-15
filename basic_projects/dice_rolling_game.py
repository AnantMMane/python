import random

while True:
    user_input = input('Do you want to roll again? (y/n): ').lower()
    if user_input == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'You rolled {dice1} and {dice2}')
    elif user_input == 'n':
        break
    else:
        print('Invalid input. Please try again.')
        continue
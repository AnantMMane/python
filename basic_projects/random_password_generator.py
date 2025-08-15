import random
import string

POSSIBLE_INPUTS = ('y', 'n')

def get_password(pass_length, has_special_characters, has_capital_characters, has_lowercase_characters, has_numeric_characters):
    pass


if __name__ == '__main__':
    length = 0
    special_characters = False
    capital_characters = False
    lowercase_characters = False
    numeric_characters = False

    while True:
        try:

            print("*" * 143)
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to the Password Generator!")
            print("*" * 143)

            special_characters = input('Does your password has special characters: (y/n): ').strip().lower()
            if special_characters not in POSSIBLE_INPUTS:
                raise ValueError('Invalid input for Special characters')

            capital_characters = input('Does your password has capital characters: (y/n): ').strip().lower()
            if capital_characters not in POSSIBLE_INPUTS:
                raise ValueError('Invalid input for Capital characters')

            lowercase_characters = input('Does your password has Lowercase characters: (y/n): ').strip().lower()
            if lowercase_characters not in POSSIBLE_INPUTS:
                raise ValueError('Invalid input for Lower case characters')

            numeric_characters = input('Does your password has Numeric characters: (y/n): ').strip().lower()
            if numeric_characters not in POSSIBLE_INPUTS:
                raise ValueError('Invalid input for Numeric characters')
            print("*" * 143)

            length = int(input('Enter length of password: '))
            if length < 4 :
                raise ValueError('Invalid length')

            generated_password = get_password(length, special_characters, capital_characters, lowercase_characters, numeric_characters)

            print("*" * 143)
            print(f"Generated Password as per your requirements:{generated_password}")
            print("*" * 143)

            user_want_to_continue = input("Do you want to continue? (y/n): ").strip().lower()
            if user_want_to_continue != 'y':
                print("Thank you for using password generator.!")
                exit(0)

        except ValueError:
            print('You have entered invalid value. Please try again.')
            continue
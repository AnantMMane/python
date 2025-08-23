
# user input: The die is cast cahracter shift: 25 expected output: Sgd chd hr bzrs
# write a Python script that encrypts user input by shifting characters in the ASCII table.
# The script should handle both uppercase and lowercase letters, leaving non-alphabetic characters unchanged.
# The script should also allow the user to specify the character shift value, which should be between 1 and 25.
# The script should continue to prompt for input until the user provides a valid input or chooses to exit.
# The script should print the encrypted string after each valid input.

def caesar_shift(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            # Shift within uppercase/lowercase separately
            base = ord('A') if char.isupper() else ord('a')
            # apply shift with wrap-around using modulo
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # keep spaces/punctuation unchanged
            result.append(char)
    return ''.join(result)


while True:
    usr_input = input("Enter the string to encrypt: ")
    char_shift = input("Enter the character shift value ranging between 1 to 25: ")
    if not usr_input:
        continue
    if not char_shift.isdigit() or not (1 <= int(char_shift) <= 25):
        print("Invalid character shift value. Please enter a number between 1 and 25.")
        continue
    else:
        encrypted = caesar_shift(usr_input, int(char_shift))
        print("Encrypted string:", encrypted)  # Output: Encrypted string: <encrypted_string>
    print("Exiting the program.")    
    break
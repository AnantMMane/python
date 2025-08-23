def check_pallindrome(user_input):
    cleaned = ''.join(char for char in user_input if char.isalnum())
    front_pointer = 0
    back_pointer = len(cleaned) - 1
    while front_pointer < back_pointer:
        if cleaned[front_pointer] != cleaned[back_pointer]:
            print("It's not a palindrome")        
            return
        front_pointer +=1
        back_pointer -=1
    print("It's a palindrome")
    
while True:
    user_input = input('Please enter a string to check for palindrome: ')
    if not user_input:
        print("No input provided. Exiting the program.")
        continue
    else:
        check_pallindrome(user_input.strip().lower())
        break

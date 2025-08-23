# input: <length_of_input>
# input: 1 2 3 4
# Output: Total sum of numbers: 10
while True:
    usr_input = input("Enter the length of input: ")
    if not usr_input:
        print("Length must be at least 1. Existing the program.")
        break
    else:
        numbers = usr_input.split()
        total = 0
        for num in numbers:
            try:
                total += int(num)
            except ValueError:
                print(f"'{num}' is not a valid number, skipping.")
        print("Total sum of numbers:", total)  # Output: Total sum of numbers: <calculated_sum>

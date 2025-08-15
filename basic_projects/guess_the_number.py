# This is guess the number game.
import random

print('Hello, What is your name?')
name = input()

secretNumber = random.randint(1,20)

print(f"Well, {name}, I am thinking of a number between 1 to 20.")

guess = 0

for i in range(1,7):
    print(f'Take a guess, {name}.')
    guess = int(input())
    if guess > secretNumber:
        print(f"Your guess is too High, {name}")
    elif guess < secretNumber:
        print(f"Your guess is too low, {name}")
    else:
        break

if guess == secretNumber:
    print(f"Good Job, {name}! You have done a great Job.You have guessed the Number in {i} guess.")
else:
    print(f"Nope. The numner I was thinking was {secretNumber}.")

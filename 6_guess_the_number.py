import random

print("Welcome to KBC Guess the Number !!")
number=random.randint(1,10)
guess=None
while guess!=number:
    guess = int(input("Guess the  number between 1 to 10!  "))

    if guess==number:
        print("Congratulations! You guessed the right number.")
    elif guess > number:
        print("Its to high . try again")
    elif guess < number:
        print("Its too low . try again")

    elif guess >10 and guess <0:
        print("Invalid number .Try again")
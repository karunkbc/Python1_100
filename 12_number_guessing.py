import random

EASY_LEVEL=10
HARD_LEVEL=5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Its too high.")
        return turns - 1

    elif user_guess < actual_answer:
        print("Its too low")
        return turns -1
    else:
        print(f"You have got it the answer is {actual_answer}")
def diffulity():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level =="easy":
         return  EASY_LEVEL
    else:
        return HARD_LEVEL

def play_game():
    print("Welcome to Karunn NumberGuessing ~! ")
    print("I'm thinking of a number between 1 and 100.")

    answer=random.randint(1,101)
    # print(answer)
    print("You have 10 attempts remaining to guess the number.")
    turns=diffulity()
    game=0
    while game!=answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_answer=int(input("Make a Guess :"))
        turns = check_answer(guess_answer, answer, turns)
        if turns==0:
            print("You've run out of guesses. Refresh the page to run again.")
            return answer
        elif guess_answer==answer:
            print("You win .")
        elif guess_answer!=answer:
            print("guess again")




play_game()
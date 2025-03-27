import random
# Just a try I will improve this in future
print("Its a demo account")
total_amount=300
print("You have $300 for demo !")

game_con=True

while game_con:
    bet_amount = int(input("Enter a bet amount : $"))
    if bet_amount < 20:
        print("Sorry , Bet must be greater than $20")
        game_con = False
    elif bet_amount > total_amount:
        print("You can't bet more than your current balance!")
        game_con = False
    else:

        user=input("Enter under 7 or over 7 or equal 7:").lower()
        random_num=random.randint(1,14)
        if random_num==7 and user=="equal":
            wining=bet_amount*5.8
            total_amount+=wining
            print("You win x5.8")
            print(f"You have {total_amount}")
        elif random_num >7 and user==" over":
            print("You win x2.3")
            wining=bet_amount*2.3
            total_amount+=wining
            print(f"You have {total_amount}")

        elif random_num<7 and user=="under":
            print("You wun x2.3")
            wining=bet_amount*2.3
            total_amount+=wining
            print(f"You have {total_amount}")

        else:
            print("You lose. Better luck next time!")

            total_amount-=bet_amount
            print(f"You have {total_amount}")

    restart=input(" Enter to play game 'yes' if you wana quit then 'no'")
    if restart=="no":
        game_con=False
        print(f"The total amount is %{total_amount}")


    elif restart=="yes":
        game_con=True
        print(f"The total amount is ${total_amount}")



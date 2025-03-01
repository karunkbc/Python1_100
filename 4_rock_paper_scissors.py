import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to KBC rock_paper_scissors!")
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
image=[rock,paper,scissors]
print(image[user_choice])
computer_choice=random.randint(0,2)
print(f"Computer choice : {computer_choice}")
print(image[computer_choice])
# condition !
if user_choice >=2 or user_choice <0:
    print("Invalid ,try again ! ")
elif user_choice==computer_choice:
    print("Its a draw!")
elif user_choice <computer_choice:
    print("You lose!")
elif user_choice> computer_choice:
    print("You win!")
elif user_choice==0 and computer_choice==2:
    print("You win!")
elif user_choice ==2 and computer_choice==0 :
    print("You lose!")
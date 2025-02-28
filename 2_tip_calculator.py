print("Welcome to the kbc tip calculator!")
bill = float(input("What was the total bill? Rs "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_amount=bill+(bill*tip/100)
each_person=total_amount/people
final_amount=round(each_person,2)
print(f"Each person should pay: Rs {final_amount} ")
print("Welcome to the KBC rollercoaster!!")
height=int(input("Enter your height="))

if height>=120:
    print("You can ride a Rollercoaster !!")
    price=0
    age = int(input("Enter your age ="))

    if age > 10 and age <12 :
        price +=50
        print("Tickets for child is Rs50")
    elif age <10 :
        print("You can't ride .You are underage!")
    elif age >=12 and age <=18:

        price +=70
        print("Tickets for teen is Rs70")
    elif age >18 and age <=50:
        price +=120
        print("Tickets for adult is Rs120")
    elif age >50:
        price +=0
        print("Tickets for old age is Rs0 . Please Enjoy your ride !")
    want_photo=input("Do you want photo . Type 'y' for yes and 'n' for no .").lower()
    if age>10:
        if want_photo=="y":
            price +=30

        print(f"The total price is {price}")
        print("Enjoy your ride !")

else:
    print("Sorry ,You can't ride a rollercoaster!")
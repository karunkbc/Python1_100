print("Welcome to KBC! Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
price=0
if size =='S' :
    price=150
    print("The price for Small pizza is Rs 150")

elif size=="M":
    price=200
    print("The price for Medium pizza is Rs 200")

elif size=="L":
    price=250
    print("The price for Large pizza is Rs 250")

else:
    print("Sorrry Invalid !!!")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
    if size=='S':
        price +=20
    elif size=="M " and size=="L":
        price +=30

extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese=="Y":
    price +=10

print(f" The total price is RS { price}")


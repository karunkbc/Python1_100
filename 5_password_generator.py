import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the KBC Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# This is for Eassy password !
# password_0=""
# for char in range(0,nr_numbers):
#     password_0+=random.choice(letters)
# for num in range(0, nr_numbers):
#     password_0+=random.choice(numbers)
# for sym in range(0,nr_symbols):
#     password_0+=random.choice(symbols)
# print(f"Your Easy password is {password_0}")

# This is for hard password !!
passw=[]
for char in range(0,nr_letters):
    passw.append(random.choice(letters))
for num in range(0,nr_numbers):
    passw.append(random.choice(numbers))
for sym in range(0,nr_symbols):
    passw.append(random.choice(symbols))
random.shuffle(passw)
print(passw)
password_1=""
for p_ass in passw:
    password_1+=p_ass
print(f"Your hard password is {password_1}")
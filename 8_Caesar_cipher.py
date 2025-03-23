
def logo():
    logo = """
     ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
    a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
    8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
    "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
     `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
                88             88
               ""             88
                              88
     ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
    a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
    8b         88 88       d8 88       88 8PP""""""" 88
    "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
     `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
                  88
                  88
    """
    user=input("Do you want logo. If you want 'yes' if not for 'no' \n")
    if user=="yes":
        print(logo)

logo()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(original_text,shift_amount ,encode_or_decode):
    if encode_or_decode=="decode":

        shift_amount*=-1
    output_text=""
    for letter in original_text:
        if letter not in alphabet:
            output_text+=letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


game_con=True
while game_con:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type a shift number :\n"))
    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart=input("Enter 'yes' for restart 'no' for end !")
    if restart=="no":
        game_con=False
        print("Good bye !")


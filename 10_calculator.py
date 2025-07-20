def logo():
    logo = r"""
     _____________________
    |  _________________  |
    | |kbccalculator   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """
    return logo


def add(n1, n2):
    return n1 + n2


def sub(n1,n2):
    return n1 -n2
def multiply(n1,n2):
    return n1 *n2
def divide(n1,n2):
    return n1 / n2


operation={
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide,
}
def calculator():
    print("Welcome to kbc calculator ")
    x=logo()
    print(x)
    should_continue=True
    n1=int(input("Enter a first Number :"))
    while should_continue:
        for operation_ in operation:
            print(operation_)

        select_operation=input("Pick an operation :")
        n2=int(input("Enter a second number :"))
        answer=operation[select_operation](n1,n2)
        print(f"The answer is {n1} {select_operation} {n2} = {answer}")
        choice=input("Type 'y' to continue  or type 'n' to start a new calculation: ")
        if choice=="y":
            n1=answer
        elif choice=="n":
            should_continue=False
            print("\n"*20)
            calculator()

calculator()
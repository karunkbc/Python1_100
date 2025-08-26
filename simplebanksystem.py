class Account:
    
    def __init__(self,balance,acc):
        self.balance=balance
        self.account_no=acc

        
    def debit(self,amount):
        self.balance-=amount
        print(f"Rs {amount} was debited.")
        print(f"Total Balance =  Rs {self.get_balance()}")

    
    def credit(self,amount):
        self.balance+=amount
        print(f"Rs {amount} was credited ! ")
        print(f"Total Balance =Rs {self.get_balance()}")

    def get_balance(self):
        return self.balance
    
acc1=Account(10000,12345)
print("         Click '1' for credit and '2' for debit ")
choice=input("what do u want  (credit/debit) :")
if choice=="1":
    acc1.credit(int(input("Enter a Total Balance to credit :")))
elif choice=="2":
    acc1.debit(int(input("Enter a Total Balance to debit :")))

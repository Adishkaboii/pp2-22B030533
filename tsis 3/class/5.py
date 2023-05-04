class BankAcc():
    def __init__(self, owner = "Adi Dossabayev", balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        print(self.balance)
    
    def withdrawal(self):
        amount = int(input())
        if(self.balance-amount >= 0):
            self.balance = self.balance-amount
            print("Done!")
            print("Now balance is", self.balance)
        else:
            print("Oops((")
            print("You dont have much money. Take a bit lower!!")
            print("Your balance: ", self.balance)

a = BankAcc("Adi Dossabayev", 1000)
a.deposit()
a.withdrawal()
a.withdrawal()

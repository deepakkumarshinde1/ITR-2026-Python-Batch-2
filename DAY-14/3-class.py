# class start
class Bank:

    balance = 0
    def __init__(self,balance):
        self.balance = balance

    def printBalance(self):
        print(f"Your current account balance is ₹{self.balance}/- INR")
    
    def deposit(self,amount):
        # self.balance =  self.balance + amount
        self.balance +=  amount
        print(f"Rupees {amount} is deposited to your account, your new bank account balance is ₹{self.balance}/- INR.")

# class end

bank = Bank(1000)
bank.printBalance()
bank.deposit(700)



def add(a,b):
    print(a+b)

add(10,20)
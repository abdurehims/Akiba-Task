# bank account 
class Account:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        if ammount >= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
    def get_balance(self):
        return self.balance
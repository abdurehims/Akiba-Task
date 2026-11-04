class BankAccount:

    def init(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful!")
        else:
            print("Invalid deposit amount!")


    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount!")
        else:
            self.__balance -= amount
            print("Withdrawal successful!")


    def get_balance(self):
        print("Current Balance:", self.__balance, "Birr")


account1 = BankAccount("Abdurehim", 5000)

print("Account Holder:", account1.account_holder)
account1.deposit(1000)
account1.withdraw(2000)
account1.get_balance()
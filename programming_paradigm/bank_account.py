class BankAccount:
    def __init__ (self, initial_balance = 0):
        self.account_balance = initial_balance
    #encapsulation
    def deposit(self,amount):
        self.account_balance = self.account_balance + amount
    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False
    def display(self):
        print(f"Your current balance is: {self.account_balance}")


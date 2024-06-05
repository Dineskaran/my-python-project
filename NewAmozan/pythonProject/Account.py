class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit{amount} new Balance: {self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance -1000:
            self.balance -= amount
            return f"withdraw {amount} New balance: {self.balance}"
        else:
            return "invalid balance"

    def check_balance(self):
        return f" your current balance is : {self.balance}"

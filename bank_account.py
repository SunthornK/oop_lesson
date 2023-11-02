class Account:
    def __init__(self, num, acc_type, account, balance):
        self.account_number = num
        self.type = acc_type
        self.account_name = account
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return f'{{{self.account_number}, {self.type}, {self.account_name}, {self.balance}}}'


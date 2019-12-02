class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, n):
        self.balance += n

    def withdraw(self, n):
        self.balance -= n


account1 = BankAccount('Mhiloca')
print(account1.get_balance())
account1.deposit(34.00)
print(account1.balance)

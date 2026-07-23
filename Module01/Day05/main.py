class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount

    def statement(self):
        print(f"{self.owner}: ${self._balance}")


class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0, rate=0.05):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        self._balance += self._balance * self.rate

    def statement(self):
        print(f"Savings Account -> {self.owner}: ${self._balance:.2f}")


class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance=0, overdraft=500):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if self._balance + self.overdraft >= amount:
            self._balance -= amount
        else:
            print("Overdraft limit exceeded.")

    def statement(self):
        print(f"Current Account -> {self.owner}: ${self._balance:.2f}")


accounts = [
    SavingsAccount("Abebe", "1001", 1000),
    CurrentAccount("Sara", "1002", 500)
]

accounts[0].add_interest()
accounts[1].withdraw(700)

for account in accounts:
    account.statement()
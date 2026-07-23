class Account:
    def __init__(self, owner, number):
        self.owner = owner
        self.number = number
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(("withdraw", amount))

    def undo_last(self):
        if not self.history:
            print("Nothing to undo.")
            return

        action, amount = self.history.pop()

        if action == "deposit":
            self.balance -= amount
        else:
            self.balance += amount

    def statement(self):
        print(self.owner, self.balance)


class AccountRegistry:
    def __init__(self):
        self.accounts = {}

    def add(self, account):
        self.accounts[account.number] = account

    def find(self, number):
        return self.accounts.get(number)

    def list_all(self):
        for account in self.accounts.values():
            account.statement()


registry = AccountRegistry()

a1 = Account("Abebe", "1001")
a2 = Account("Sara", "1002")

registry.add(a1)
registry.add(a2)

a1.deposit(1000)
a1.withdraw(300)
a1.undo_last()

registry.list_all()
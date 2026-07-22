from abc import ABC, abstractmethod



# Base Account Class

class Account(ABC):

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

        # Transaction history (Stack)
        self.history = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self._balance += amount

        # Save transaction
        self.history.append(("deposit", amount))

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount

        # Save transaction
        self.history.append(("withdraw", amount))

    # Undo the latest transaction
    def undo_last(self):

        if not self.history:
            print("No transaction to undo.")
            return

        action, amount = self.history.pop()

        if action == "deposit":
            self._balance -= amount
            print(f"Undo deposit of {amount} ETB")

        elif action == "withdraw":
            self._balance += amount
            print(f"Undo withdrawal of {amount} ETB")

    @abstractmethod
    def statement(self):
        pass



# Savings Account

class SavingsAccount(Account):

    def __init__(self, owner, account_number, interest_rate, balance=0):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate

    def statement(self):
        print("----- Savings Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print(f"Interest Rate: {self.interest_rate}%")
        print("---------------------------")



# Checking Account
class CheckingAccount(Account):

    def __init__(self, owner, account_number, overdraft_limit, balance=0):
        super().__init__(owner, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")

        self._balance -= amount

        self.history.append(("withdraw", amount))

    def statement(self):
        print("----- Checking Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print(f"Overdraft Limit: {self.overdraft_limit} ETB")
        print("----------------------------")


# Factory Pattern


class AccountFactory:

    @staticmethod
    def create(account_type, owner, number, balance=0):

        if account_type.lower() == "savings":
            return SavingsAccount(
                owner,
                number,
                interest_rate=5,
                balance=balance
            )

        elif account_type.lower() == "checking":
            return CheckingAccount(
                owner,
                number,
                overdraft_limit=2000,
                balance=balance
            )

        else:
            raise ValueError("Invalid account type")



# Account Registry


class AccountRegistry:

    def __init__(self):

        # O(1) lookup
        self.by_number = {}

        # Keep insertion order
        self.order = []

    def add(self, account):

        self.by_number[account.account_number] = account
        self.order.append(account.account_number)

    # O(1)
    def find(self, number):

        return self.by_number.get(number)

    # Return accounts in insertion order
    def list_all(self):

        return [self.by_number[number] for number in self.order]



# Test Program


registry = AccountRegistry()

acc1 = AccountFactory.create(
    "savings",
    "Alazar",
    "ACC1001",
    5000
)

acc2 = AccountFactory.create(
    "checking",
    "Sara",
    "ACC1002",
    8000
)

registry.add(acc1)
registry.add(acc2)

# Transactions
acc1.deposit(2000)
acc1.withdraw(500)

acc2.deposit(1000)
acc2.withdraw(3000)

# O(1) Lookup
print("Finding ACC1001...\n")

found = registry.find("ACC1001")

if found:
    found.statement()

# List all accounts
print("\nAll Accounts\n")

for account in registry.list_all():
    account.statement()

# Undo last transaction
print("\nUndo Last Transaction")

acc1.undo_last()

print("\nBalance After Undo")

acc1.statement()
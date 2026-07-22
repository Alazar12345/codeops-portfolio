from abc import ABC, abstractmethod


# Singleton Pattern
# Only one BankSettings object can exist.


class BankSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


# Observer Pattern


class Customer:

    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} Notification: {message}")



# Account (Subject)

class Account(ABC):

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
        self.observers = []

    @property
    def balance(self):
        return self._balance

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self._balance += amount
        self.notify(f"{amount} ETB deposited.")

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount
        self.notify(f"{amount} ETB withdrawn.")

    @abstractmethod
    def statement(self):
        pass


# Savings Account


class SavingsAccount(Account):

    def __init__(self, owner, account_number, interest_rate, balance=0):
        super().__init__(owner, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.deposit(interest)

    def statement(self):
        print("\n----- Savings Account -----")
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
        self.notify(f"{amount} ETB withdrawn.")

    def statement(self):
        print("\n----- Checking Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print(f"Overdraft Limit: {self.overdraft_limit} ETB")
        print("----------------------------")


# Factory Pattern


class AccountFactory:

    @staticmethod
    def create(account_type, owner, account_number, balance=0):

        if account_type.lower() == "savings":
            return SavingsAccount(
                owner,
                account_number,
                interest_rate=5,
                balance=balance
            )

        elif account_type.lower() == "checking":
            return CheckingAccount(
                owner,
                account_number,
                overdraft_limit=2000,
                balance=balance
            )

        else:
            raise ValueError("Unknown account type")



# Test Program


settings = BankSettings()

print(f"Bank Currency: {settings.currency}")

customer1 = Customer("Sara")
customer2 = Customer("John")

savings = AccountFactory.create(
    "savings",
    "Sara",
    "SAV1001",
    10000
)

checking = AccountFactory.create(
    "checking",
    "John",
    "CHK1001",
    5000
)

savings.add_observer(customer1)
checking.add_observer(customer2)

savings.deposit(2000)
savings.add_interest()

checking.withdraw(4000)

accounts = [savings, checking]

print("\n====== Account Statements ======")

for account in accounts:
    account.statement()
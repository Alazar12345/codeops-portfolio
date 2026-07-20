class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

    # Read-only property
    @property
    def balance(self):
        return self._balance

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self._balance += amount

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance -= amount

    # Display account information
    def statement(self):
        print("----- Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance:.2f} ETB")
        print("-------------------")


# Savings Account


class SavingsAccount(Account):

    def __init__(self, owner, account_number, balance=0, rate=0.05):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        # Reuse deposit()
        self.deposit(self.balance * self.rate)

    # Override statement()
    def statement(self):
        print("----- Savings Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Interest Rate: {self.rate * 100:.0f}%")
        print(f"Balance: {self.balance:.2f} ETB")
        print("---------------------------")



# Current Account


class CurrentAccount(Account):

    def __init__(self, owner, account_number, balance=0, overdraft=1000):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    # Override withdraw()
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.balance + self.overdraft:
            raise ValueError("Overdraft limit exceeded.")

        self._balance -= amount

    # Override statement()
    def statement(self):
        print("----- Current Account -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Overdraft Limit: {self.overdraft} ETB")
        print(f"Balance: {self.balance:.2f} ETB")
        print("---------------------------")



# Create Accounts


account = Account("Alazar", "ACC1001", 5000)

savings = SavingsAccount(
    "Sara",
    "SAV2001",
    balance=10000,
    rate=0.05
)

current = CurrentAccount(
    "John",
    "CUR3001",
    balance=3000,
    overdraft=2000
)

# Perform Transactions


# Add interest to savings account
savings.add_interest()

# Withdraw using overdraft
current.withdraw(4500)


# Polymorphism


accounts = [account, savings, current]

for acc in accounts:
    acc.statement()
    print()
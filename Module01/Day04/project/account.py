class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    # Read-only property
    @property
    def balance(self):
        return self.__balance

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        self.__balance += amount

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        self.__balance -= amount

    # Display account information
    def statement(self):
        print("----- Account Statement -----")
        print(f"Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.__balance} ETB")
        print("-----------------------------")



account1 = Account("Alazar", "ACC1001")

account1.statement()


account1.deposit(5000)

print("\nAfter depositing 5000 ETB:")
account1.statement()


account1.withdraw(1500)

print("\nAfter withdrawing 1500 ETB:")
account1.statement()

print(f"\nCurrent Balance: {account1.balance} ETB")
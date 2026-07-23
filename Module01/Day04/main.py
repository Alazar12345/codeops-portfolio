class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return

        self.__balance += amount
        print(f"${amount} deposited.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient funds.")
            return

        self.__balance -= amount
        print(f"${amount} withdrawn.")

    def statement(self):
        print("----------------------")
        print("Owner:", self.owner)
        print("Account:", self.account_number)
        print("Balance:", self.__balance)
        print("----------------------")


account1 = Account("Abebe", "1001", 1000)
account2 = Account("Sara", "1002", 500)

account1.deposit(300)
account1.withdraw(200)

account2.deposit(100)
account2.withdraw(700)

account1.statement()
account2.statement()
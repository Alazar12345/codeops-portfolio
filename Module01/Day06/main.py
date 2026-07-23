class SMSAlert:
    def update(self, message):
        print("SMS:", message)


class Account:
    def __init__(self, owner, number):
        self.owner = owner
        self.number = number
        self.balance = 0
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)

    def deposit(self, amount):
        self.balance += amount
        self.notify(f"{self.owner} deposited ${amount}")

    def statement(self):
        print(self.owner, self.balance)


class SavingsAccount(Account):
    pass


class CurrentAccount(Account):
    pass


class AccountFactory:
    @staticmethod
    def create(kind, owner, number):
        if kind.lower() == "savings":
            return SavingsAccount(owner, number)
        elif kind.lower() == "current":
            return CurrentAccount(owner, number)
        else:
            raise ValueError("Invalid account type")


sms = SMSAlert()

acc1 = AccountFactory.create("savings", "Abebe", "1001")
acc2 = AccountFactory.create("current", "Sara", "1002")

acc1.subscribe(sms)
acc2.subscribe(sms)

acc1.deposit(500)
acc2.deposit(800)

acc1.statement()
acc2.statement()
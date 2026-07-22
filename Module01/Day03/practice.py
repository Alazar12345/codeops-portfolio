#BOOK
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(self.title, self.author, self.pages)


book1 = Book("Atomic Habits", "James Clear", 320)
book2 = Book("Python Crash Course", "Eric Matthes", 544)

book1.describe()
book2.describe()
#PRODUCT
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        self.__quantity += n

    def sell(self, n):
        if self.__quantity - n >= 0:
            self.__quantity -= n
        else:
            print("Not enough stock")


product1 = Product("Phone", 15000, 10)
product2 = Product("Laptop", 50000, 5)
product3 = Product("Mouse", 800, 20)

product1.sell(3)

print(product1.quantity)
print(product2.quantity)
print(product3.quantity)

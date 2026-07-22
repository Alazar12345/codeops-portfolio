class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        print(f"{self.title} by {self.author} - {self.pages} pages")


# Create two books
durader = Book("Durader", "Dostoevsky", 270)
animal_farm = Book("Animal Farm", "George Orwell", 112)

durader.describe()
animal_farm.describe()


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.__quantity = quantity  

    # Getter
    @property
    def quantity(self):
        return self.__quantity

    def restock(self, n):
        if n < 0:
            raise ValueError("Restock amount cannot be negative.")
        self.__quantity += n

    def sell(self, n):
        if n < 0:
            raise ValueError("Cannot sell a negative amount.")

        if n > self.__quantity:
            raise ValueError("Not enough stock.")

        self.__quantity -= n


# Create three products
shampoo = Product("Shampoo", 321, 30)
coconut_oil = Product("Coconut Oil", 432, 54)
perfume = Product("Perfume", 212, 11)

# Prove independence
print("Before selling:")
print("Shampoo:", shampoo.quantity)
print("Coconut Oil:", coconut_oil.quantity)
print("Perfume:", perfume.quantity)

# Sell some shampoo
shampoo.sell(10)

print("\nAfter selling 10 shampoos:")
print("Shampoo:", shampoo.quantity)
print("Coconut Oil:", coconut_oil.quantity)
print("Perfume:", perfume.quantity)

# Restock perfume
perfume.restock(5)

print("\nAfter restocking perfume:")
print("Shampoo:", shampoo.quantity)
print("Coconut Oil:", coconut_oil.quantity)
print("Perfume:", perfume.quantity)
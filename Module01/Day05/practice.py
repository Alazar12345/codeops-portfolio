# OOP: Inheritance, super(), Overriding, Polymorphism,
# and Abstract Base Classes


from abc import ABC, abstractmethod



# 1 & 5. Vehicle Base Class (Abstract)

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        print(f"{self.make} {self.model}")

    @abstractmethod
    def wheels(self):
        pass



# 1. Car Subclass

class Car(Vehicle):

    def __init__(self, make, model):
        super().__init__(make, model)

    def wheels(self):
        return 4



# 2 & 3. Truck Subclass


class Truck(Vehicle):

    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity

    # Override describe()
    def describe(self):
        print(f"{self.make} {self.model} - Capacity: {self.capacity}")

    def wheels(self):
        return 6



# Create Objects


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

truck1 = Truck("Volvo", "FH16", "20 Tons")
truck2 = Truck("Mercedes", "Actros", "18 Tons")



# 4. Polymorphism


vehicles = [car1, car2, truck1, truck2]

for vehicle in vehicles:
    vehicle.describe()
    print(f"Wheels: {vehicle.wheels()}")
    print("-" * 30)
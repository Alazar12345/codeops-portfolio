# Day 06 Practice
# SOLID Principles & Design Patterns

from abc import ABC, abstractmethod
import math



# Exercise 1: Single Responsibility Principle (SRP)


class Report:
    def build(self):
        print("Building report...")


class ReportSaver:
    def save(self):
        print("Saving report to file...")


class ReportEmailer:
    def email(self):
        print("Sending report by email...")


print("===== Exercise 1 =====")
report = Report()
report.build()

saver = ReportSaver()
saver.save()

emailer = ReportEmailer()
emailer.email()


# Exercise 2: Open/Closed Principle (OCP)

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print("\n===== Exercise 2 =====")

shapes = [
    Circle(5),
    Square(4),
    Triangle(6, 3)
]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")



# Exercise 3: Singleton Pattern

class AppSettings:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = "ETB"
        return cls._instance


print("\n===== Exercise 3 =====")

settings1 = AppSettings()
settings2 = AppSettings()

print(settings1.currency)
print(settings1 is settings2)


# Exercise 4: Factory Pattern


class ShapeFactory:

    @staticmethod
    def create(kind):

        if kind.lower() == "circle":
            return Circle(5)

        elif kind.lower() == "square":
            return Square(4)

        elif kind.lower() == "triangle":
            return Triangle(6, 3)

        else:
            raise ValueError("Unknown shape")


print("\n===== Exercise 4 =====")

shape = ShapeFactory.create("circle")
print(f"Area: {shape.area():.2f}")

shape = ShapeFactory.create("square")
print(f"Area: {shape.area():.2f}")

shape = ShapeFactory.create("triangle")
print(f"Area: {shape.area():.2f}")



# Exercise 5: Observer Pattern


class NewsAgency:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)


class EmailSubscriber:

    def update(self, news):
        print(f"Email Subscriber received: {news}")


class SMSSubscriber:

    def update(self, news):
        print(f"SMS Subscriber received: {news}")


print("\n===== Exercise 5 =====")

agency = NewsAgency()

email = EmailSubscriber()
sms = SMSSubscriber()

agency.subscribe(email)
agency.subscribe(sms)

agency.notify("Python 3.15 has been released!")
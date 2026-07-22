customers = [
    ("Abel", 1200),
    ("Sara", 750),
    ("Marta", 450),
    ("Daniel", 1000),
    ("Hanna", 300)
]

def tier(balance):
    if balance >= 1000:
        return "Premium"
    elif balance >= 500:
        return "Standard"
    else:
        return "Basic"

premium = 0
standard = 0
basic = 0

for name, balance in customers:
    customer_tier = tier(balance)
    print(name, customer_tier, balance, "ETB")

    if customer_tier == "Premium":
        premium += 1
    elif customer_tier == "Standard":
        standard += 1
    else:
        basic += 1

print("Premium:", premium)
print("Standard:", standard)
print("Basic:", basic)
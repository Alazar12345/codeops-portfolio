totals = {}

try:
    with open("transactions.txt", "r") as file:
        for line in file:
            name, amount = line.strip().split(",")
            amount = float(amount)

            totals[name] = totals.get(name, 0) + amount

    print("Transaction Summary")

    for customer, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(customer, total)

    with open("report.txt", "w") as report:
        for customer, total in sorted(totals.items(), key=lambda x: x[1], reverse=True):
            report.write(f"{customer}: {total}\n")

except FileNotFoundError:
    print("transactions.txt not found.")
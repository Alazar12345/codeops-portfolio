# 1. Temperature label
temperature = float(input("Enter the temperature in °C: "))

if temperature < 15:
    print("cold")
elif temperature <= 28:
    print("warm")
else:
    print("hot")

# 2. Receipt loop
for number in range(1, 11):
    print(f"Receipt #{number}")

# 3. Even numbers
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

# 4. Discount function
def apply_discount(price, percent=10):
    return price - (price * percent / 100)

print(apply_discount(100))
print(apply_discount(100, 20))

# 5. Countdown
count = 5

while count >= 1:
    print(count)
    count -= 1

print("Liftoff!")
# Day 5: store many expenses in a list and total them

amounts = []

print("=== Add Expenses ===")

while True:
    amount = float(input("Amount (or 0 to finish): "))
    if amount == 0:
        break
    amounts.append(amount)

print()
print("--- Your Expenses ---")
for number, amount in enumerate(amounts, start=1):
    print(f"{number}. ${amount:.2f}")

print("-" * 25)
print(f"Count: {len(amounts)}")
print(f"Total: ${sum(amounts):.2f}")

if amounts:
    print(f"Biggest: ${max(amounts):.2f}")
    print(f"Average: ${sum(amounts) / len(amounts):.2f}")

total = 0
for amount in amounts:
    total = total + amount
print(f"Total (by loop): ${total:.2f}")

print("--- Expenses Over 50 ---")
print("-" * 25)
totalOverFifty = []
for amount in amounts:
    if amount > 50:
        totalOverFifty.append(amount)
print(f"Total expenses over 50: {len(totalOverFifty)}")

for number, amount in enumerate(totalOverFifty, start=1):
    print(f"{number}. ${amount:.2f}")

print("--- Sorted List and Pop Feature ---")
sortedExpenses = sorted(amounts, reverse=True)
print(f"Top 3 Expenses:")
for number, amount in enumerate (sortedExpenses[:3], start=1):
    print(f"{number}. ${amount:.2f}")

removeLast = amounts.pop()
lastTotal = total - removeLast

print(f"Expenses after last item removed: ${lastTotal:.2f}")


print("--- Categories Loop ---")
categories = ["Food", "Transport", "Rent", "Food"]

for category in categories:
    print(category)

print("Food appears", categories.count("Food"), "times")
print("Unique categories:", set(categories))


# Day 4: flag expenses as high, medium, or low

HIGH_THRESHOLD = 200.00

print("=== Check an Expense ===")

amount = float(input("Amount: "))
category = input("Category: ").strip().title()

if amount <= 0:
    print("Amount must be positive")

if category == "Food" and amount > 30:
    flag = "HIGH"
elif amount > HIGH_THRESHOLD:
    flag = "VERY HIGH"
elif amount > 50:
    flag = "HIGH"
elif amount > 20:
    flag = "MEDIUM"
else:
    flag = "LOW"

print(f"{category}: ${amount:.2f} -> {flag}")

if flag == "HIGH":
    print("Warning: this is a big expense. Is it planned?")

if category == "Entertainment" and amount > 30:
    print("Tip: entertainment spending is adding up.")

if category in ["Rent", "Utilities"]:
    print("This is a fixed monthly cost.")
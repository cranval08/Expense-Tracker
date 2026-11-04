amount = 12.50
category = "Coffee"
description = "Cafe Mocha"
date = "2026-11-04"
is_recurring = False
payment_method = "Cash"

print("--- Expense ---")
print("Amount:", amount)
print("Category:", category)
print("Description:", description)
print("Date", date)
print("Recurring:", is_recurring)
print("Payment Method:", payment_method)

print("--- Expense ---")
print("Amount:", amount)
print("Category:", category)
print("Description:", description)
print("Date", date)
print("Recurring:", is_recurring)
print("Payment Method:", payment_method)

print(type(amount))
print(type(category))
print(type(is_recurring))

tax = amount * 0.10
total = amount + tax
print("Tax:", tax)
print("Total with tax:", total)
# Day 3: ask the user for an expense and print it with f-strings

print("=== Add an Expense ===")

amount = float(input("Amount: "))
category = input("Category (eg. Food, Transport): ").strip().title()
description = input("Description: ").strip().upper()
date = input("Date (YYYY-MM-DD): ").strip()
payment_method = input("Payment Method (eg. Cash, Card): ").strip()

print()     # blank line
print("--- Expense Saved ---")
print(f"Amount:         ${amount:.2f}")
print(f"Category:       {category}")
print(f"Description:    {description}")
print(f"Date:           {date}")
print(f"Paymend Method: {payment_method}")
print()
print(f"Summary: {description} ({category}) cost ${amount:,.2f} on {date} using {payment_method}.")
print("-" * 30)
print(f"{'Category':<15}{'Amount':>10}")
print(f"{category:<15}{amount:>10.2f}")
print("-" * 30)